// CEAC envelope adapter, not a second chess evaluator.
// Accuracy, classifications, tallies, report cards, annotations, speech hashes,
// and explanation markings come from the bundled Chess.com CEE GameReview.
// No CP thresholds, sacrifice guesses, accuracy curve, or rating formula.
import { encodeMessage, decodeMessage } from './protobuf.js';
import { CeeClient } from './cee.js';

export const MC = Object.freeze({
  UNSPECIFIED: 0, BOOK: 1, BRILLIANT: 2, GREAT_FIND: 3, BEST: 4,
  EXCELLENT: 5, GOOD: 6, INACCURACY: 7, MISTAKE: 8, BLUNDER: 9,
  MISSED: 10, FORCED: 11, TRICKY: 20,
});

function newGameRequest(request, { pageGame, pgn } = {}) {
  let source = request.newGameReq?.newGame;
  if (!source?.from?.case) {
    if (pgn) source = { from: { case: 'pgnGame', value: { pgn, takeFirstGameOnly: true } } };
    else if (pageGame?.startFen) source = { from: { case: 'positionWithMoves', value: {
      initialPosition: { initialPosition: { case: 'fen', value: pageGame.startFen } },
      moveList: { case: 'uciMoves', value: { moves: pageGame.uci || [] } },
    } } };
    else throw new Error('GameReviewRequest has no game');
  }
  // CEAC normally merges runSearchReq into NewGame settings on its server.
  // Do that merge locally, preserving player metadata and all source formats.
  const settings = { ...source.settings };
  const search = request.runSearchReq?.search;
  if (search?.case === 'gameReviewSearchSettings') settings.search = search;
  else if (search?.case === 'searchParameters') settings.search = {
    case: 'searchSettings', value: {
      searchParameters: search.value,
      nullMoveSearchParameters: request.runSearchReq.nullMoveSearchParameters,
    },
  };
  if (!settings.search?.case) settings.search = { case: 'gameReviewSearchSettings', value: { strength: 1 } };
  if (settings.locale == null) settings.locale = 'en_US';
  return { ...request.newGameReq, newGame: { ...source, settings } };
}

export function reviewStats(gameReview, requestedEngine, ratingSources = {}) {
  const highlights = gameReview.highlights || {};
  const ticks = gameReview.evalGraph?.evalGraphTicks || [];
  const actualEngines = [...new Set(ticks.map(t => t.moveScore?.engine).filter(x => x != null))];
  const moves = gameReview.review?.playedMoves || [];
  let speechSentences = 0, audioHashes = 0, explanationArrows = 0;
  for (const entry of moves) for (const move of [entry.playedMove, entry.bestAlternativeMove]) {
    if (!move) continue;
    explanationArrows += move.boardMarkings?.arrows?.length || 0;
    for (const sentence of move.speech?.sentences || []) {
      speechSentences++;
      if (sentence.audioUrlHash) audioHashes++;
      for (const fragment of sentence.sentenceFragments || []) explanationArrows += fragment.arrowsAndSquares?.arrows?.length || 0;
    }
  }
  const card = highlights.reportCard || {};
  return {
    moves: moves.length,
    engine: 'Chess.com CEE (local)', requestedEngine, actualEngines,
    engineMatchesRequest: !requestedEngine || (actualEngines.length > 0 && actualEngines.every(e => e === requestedEngine)),
    accuracy: highlights.accuracy || {},
    tallies: highlights.classificationTallies || {},
    ratings: { white: card.white?.gameRatingV2 ?? card.white?.effectiveRating,
      black: card.black?.gameRatingV2 ?? card.black?.effectiveRating },
    ratingSources,
    opening: gameReview.opening?.openingName || null,
    ceeVersion: gameReview.metadata?.ceeVersion,
    speechSentences, audioHashes, explanationArrows,
  };
}

/** Build the exact CEAC success envelope around CEE's own review result.
 * workerFactory is injectable for regression tests, not an engine selector.
 * This CEE build currently reports TORCH_3 (11), not TORCH_HUMAN (12).
 * Preserve that fact in score messages and diagnostics; never relabel scores.
 */
export async function buildGameReview(options) {
  const { onProgress = () => {}, onLog = () => {} } = options;
  const request = decodeMessage('.chesscom.ceac.v2.GameReviewRequest', options.requestBytes);
  const newGameReq = newGameRequest(request, options);
  const strength = newGameReq.newGame.settings.search;
  onLog('CEE review: requested engine=' + (request.engine || 'unspecified') + ', search=' + JSON.stringify(strength));
  const cee = new CeeClient({ workerFactory: options.workerFactory, onLog, timeoutMs: options.timeoutMs });
  try {
    onProgress(0);
    const newGame = await cee.feature(-1, 26, 'NewGameRequest', newGameReq);
    if (newGame.invalidGame) throw new Error('CEE rejected the game: ' + JSON.stringify(newGame.invalidGame));
    const root = newGame.playedLine?.[0]?.gamePoint;
    if (root == null) throw new Error('CEE returned no root game point');
    // Apply to the actual embedded Torch engine, NOT GameReview.uci_options
    // (that map is not forwarded by this worker build). Keep the request's
    // strength and player metadata intact; do not adjust returned scores.
    await cee.command('setoption name Normalize value false');
    onProgress(0.02);
    // CEE infers checkmate/PGN results; forward explicit coordinate-game
    // metadata too, rather than assuming a winner from the review user's color.
    const metadata = newGameReq.newGame.from?.value?.metadata;
    if (metadata?.result?.result) await cee.feature(root, 30, 'SetGameResultRequest', {
      claimedGameResult: metadata.result,
    });
    const reviewOptions = request.gameReviewOptions || {};
    const response = await cee.feature(root, 42, 'GameReviewRequest', {
      startingGamePoint: root,
      includeTrainTakeaways: reviewOptions.includeTrainTakeaways,
      canAccessLockedTakeaways: reviewOptions.canAccessLockedTakeaways,
    });
    const gameReview = response.gameReview;
    if (!gameReview?.review || !gameReview?.highlights) throw new Error('CEE returned an incomplete review');
    const expectedMoves = (newGame.playedLine?.length || 1) - 1;
    if (gameReview.review.playedMoves?.length !== expectedMoves) throw new Error('CEE review does not align with played moves');

    // Older bundled CEE returns effectiveRating but no gameRatingV2. The page
    // has the V2 display flag enabled. Use its native legacy Game Rating as a
    // compatibility alias, NOT the previous synthetic formula/floor of 400.
    // Keep the original effectiveRating and report which field was available.
    const ratingSources = {};
    for (const color of ['white', 'black']) {
      const card = gameReview.highlights.reportCard?.[color];
      if (!card) continue;
      ratingSources[color] = card.gameRatingV2 != null ? 'gameRatingV2' : 'effectiveRating';
      if (card.gameRatingV2 == null && card.effectiveRating != null) card.gameRatingV2 = card.effectiveRating;
    }
    const stats = reviewStats(gameReview, request.engine, ratingSources);
    stats.torchOptions = { Normalize: false };
    if (!stats.engineMatchesRequest) onLog('Engine mismatch: requested=' + request.engine + ', actual=' + stats.actualEngines.join(',') + '; cloud parity is not yet established');
    onLog('CEE accuracy=' + JSON.stringify(stats.accuracy) + ' ratings=' + JSON.stringify(stats.ratings));
    const bytes = encodeMessage('.chesscom.ceac.v2.GameReviewResponse', {
      result: { case: 'success', value: { gameReview, ceeC_APICalls: [] } },
    });
    onProgress(1);
    return { bytes, stats };
  } finally {
    cee.dispose(); // includes worker, wasm memory, feature/game resources
  }
}
