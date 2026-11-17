// Builds a full chess.com `GameReviewResponse` from a `GameReviewRequest`
// using a local engine, so the shipped UI renders a real review without ever
// reaching analysis.chess.com.

import { decodeMessage, encodeMessage } from './protobuf.js';
import { Board, START_FEN, positionMessageToFen, squareEnumToAlg, algToSquareEnum, pgnToUci } from './chess.js';
import { UciEngine, ENGINE_PRESETS } from './engines.js';
import { wdl } from './client-math.js';

/* ------------------------------------------------------------------ enums */

// chesscom.explanation_engine.v1.MoveClassification
export const MC = {
  UNSPECIFIED: 0, BOOK: 1, BRILLIANT: 2, GREAT_FIND: 3, BEST: 4, EXCELLENT: 5,
  GOOD: 6, INACCURACY: 7, MISTAKE: 8, BLUNDER: 9, MISSED: 10, FORCED: 11, TRICKY: 20,
};
const MC_NAME = Object.fromEntries(Object.entries(MC).map(([k, v]) => [v, k]));

// chesscom.chess.v1.Color / GamePhase / Result / ResultType
const COLOR_WHITE = 1, COLOR_BLACK = 2;
const PHASE = { OPENING: 1, MIDDLEGAME: 2, ENDGAME: 3 };
const RESULT = { WHITE_WIN: 1, BLACK_WIN: 2, DRAW: 3 };
const RESULT_TYPE = { CHECKMATE: 1, RESIGNATION: 4, TIMEOUT: 6, DRAW_OFFER: 5 };
// chesscom.stats.v1.AdvancedStatType — category ids used by the report card
const STAT = { OPENING: 100, TACTICS: 101, STRATEGY: 102, ENDGAME: 103, CLOCK: 104 };

const DEPTH_BY_STRENGTH = { STRENGTH_FAST: 17, STRENGTH_STANDARD: 21, STRENGTH_DEEP: 24, STRENGTH_MAXIMUM: 26 };
const ENGINE_ENUM = { 'stockfish-nnue-16': 10, torch: 11, 'torch-lite': 11 };

/* --------------------------------------------------------- loss -> class */

// Our own thresholds, documented in README.  `loss` is centipawns the mover
// threw away relative to best play (their own point of view).
const T = { excellent: 10, good: 35, inaccuracy: 90, mistake: 220 };
const GREAT_FIND_GAP = 120;   // cp gap between best and 2nd best line
const BRILLIANT_SAC = 2;      // pawns of material the mover must give up

function classify({ playedUci, bestUci, loss, onlyMove, lines, sacForMover, mateForMover, mateMissed }) {
  if (onlyMove) return MC.FORCED;
  if (mateMissed) return MC.MISSED;
  if (playedUci && playedUci === bestUci) {
    if (sacForMover && loss <= T.excellent) return MC.BRILLIANT;
    const gap = lines.length > 1 && lines[0].cp != null && lines[1].cp != null
      ? Math.abs(lines[0].cp - lines[1].cp) : 0;
    if (!mateForMover && gap >= GREAT_FIND_GAP) return MC.GREAT_FIND;
    return MC.BEST;
  }
  if (loss <= T.excellent) return MC.EXCELLENT;
  if (loss <= T.good) return MC.GOOD;
  if (loss <= T.inaccuracy) return MC.INACCURACY;
  if (loss <= T.mistake) return MC.MISTAKE;
  return MC.BLUNDER;
}

/** CAPS-style per-move accuracy: 100 at zero loss, ~0 by 500cp. */
function moveAccuracy(loss) {
  const l = Math.max(0, loss);
  return 100 * Math.exp(-Math.pow(l / 220, 1.5));
}

/* ----------------------------------------------------------- book lookup */

let bookIndex = null; // { prefixes:Set, entries:[{seq:[uci], name, eco, tcn, depth}] }

const ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?';
const FILES = 'abcdefgh';
const algOf = (i) => FILES[i % 8] + String(Math.floor(i / 8) + 1);

function decodeTcn(m) {
  const out = [];
  for (let k = 0; k + 1 < m.length; k += 2) {
    const a = ALPHA.indexOf(m[k]), b = ALPHA.indexOf(m[k + 1]);
    if (a < 0 || b < 0) return out;
    out.push(algOf(a) + algOf(b));
  }
  return out;
}

export async function loadBook(fetchImpl = fetch) {
  if (bookIndex) return bookIndex;
  const url = (typeof chrome !== 'undefined' && chrome.runtime)
    ? chrome.runtime.getURL('engines/book/book-small.json')
    : new URL('../engines/book/book-small.json', import.meta.url).href;
  let data;
  try {
    const res = await fetchImpl(url);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    data = await res.json();
  } catch {
    // Node test harness: fetch() has no file:// support.
    const { readFile } = await import('node:fs/promises');
    const { fileURLToPath } = await import('node:url');
    data = JSON.parse(await readFile(fileURLToPath(url), 'utf8'));
  }
  const entries = [];
  const prefixes = new Set();
  for (const v of Object.values(data)) {
    if (!v || typeof v !== 'object' || !v.m) continue;
    const seq = decodeTcn(v.m);
    if (!seq.length) continue;
    entries.push({ seq, name: v.n || '', eco: v.c || '', tcn: v.m, popularity: v.s || 0 });
    for (let i = 1; i <= seq.length; i++) prefixes.add(seq.slice(0, i).join(' '));
  }
  entries.sort((a, b) => a.seq.length - b.seq.length);
  bookIndex = { prefixes, entries };
  return bookIndex;
}

function openingFor(book, uciMoves) {
  if (!book) return null;
  let best = null;
  for (const e of book.entries) {
    if (e.seq.length > uciMoves.length) break;
    let hit = true;
    for (let i = 0; i < e.seq.length; i++) if (e.seq[i] !== uciMoves[i]) { hit = false; break; }
    if (hit && (!best || e.seq.length > best.seq.length)) best = e;
    if (best && e.seq.length < best.seq.length) break;
  }
  return best;
}

/* ------------------------------------------------------------ extraction */

const PROMO = { 1: 'n', 2: 'b', 3: 'r', 4: 'q' };

function movesFromCoord(gameMoves) {
  const out = [];
  for (const gm of gameMoves || []) {
    const m = gm.move || gm; // GameMove{move} or a bare Move
    const from = squareEnumToAlg(m.from), to = squareEnumToAlg(m.to);
    if (!from || !to) continue;
    const promo = PROMO[Number(m.promotionPieceType || 0)];
    out.push(from + to + (promo || ''));
  }
  return out;
}

function fenFromInitial(init) {
  if (!init) return START_FEN;
  const ip = init.initialPosition;
  if (ip && ip.case === 'fen' && typeof ip.value === 'string') return ip.value;
  if (ip && ip.case === 'position') return positionMessageToFen(ip.value);
  return START_FEN;
}

function extractGame(req) {
  const ng = req.newGameReq;
  const src = ng && ng.newGame && ng.newGame.from;
  if (src && src.case === 'game') {
    const game = src.value || {};
    return {
      startFen: game.startingPosition ? positionMessageToFen(game.startingPosition) : START_FEN,
      uci: movesFromCoord(game.moves),
      meta: game.metadata || null,
    };
  }

  if (src && src.case === 'positionWithMoves') {
    const v = src.value || {};
    const ml = v.moveList;
    let uci = [];
    if (ml && ml.case === 'uciMoves') uci = (ml.value && ml.value.moves || []).slice();
    else if (ml && ml.case === 'moves') uci = movesFromCoord(ml.value && ml.value.moves);
    return { startFen: fenFromInitial(v.initialPosition), uci, meta: (v.initialPosition && v.initialPosition.metadata) || null };
  }

  if (src && src.case === 'tcnGame') {
    const v = src.value || {};
    return { startFen: v.initialFen || START_FEN, uci: decodeTcn(v.tcn || ''), meta: v.metadata || null };
  }

  if (src && src.case === 'pgnGame') {
    const v = src.value || {};
    return { startFen: START_FEN, uci: pgnToUci(v.pgn || ''), meta: v.metadata || null };
  }

  if (src && src.case === 'initialPosition') {
    const v = src.value || {};
    return { startFen: fenFromInitial(v), uci: [], meta: v.metadata || null };
  }

  // Fallback: ask the host page for a FEN + UCI list (page-hook provides it).
  const alt = req.__pageGame;
  if (alt && alt.startFen) return { startFen: alt.startFen, uci: alt.uci || [], meta: null };
  throw new Error('GameReviewRequest carries no game we can read');
}

function resultInfo(meta, startFen) {
  const res = meta && meta.result;
  if (!res || !res.result) return { result: RESULT.DRAW, resultType: 0 };
  const n = Number(res.result);
  const t = Number(res.resultType || 0);
  const typeMap = {
    1: RESULT_TYPE.CHECKMATE, 4: RESULT_TYPE.RESIGNATION, 5: RESULT_TYPE.DRAW_OFFER,
    6: RESULT_TYPE.TIMEOUT, 8: RESULT_TYPE.CHECKMATE,
  };
  return { result: n, resultType: typeMap[t] || 0 };
}

function playerRating(meta, color) {
  const players = (meta && meta.players) || [];
  const p = players.find((x) => Number(x.color) === color);
  const r = p && p.ratings && p.ratings[0];
  return r ? Number(r.rating) : 2000;
}

/* --------------------------------------------------------------- helpers */

const whiteView = (line, sideToMove) => {
  if (!line) return { cp: null, mate: null };
  const sign = sideToMove === 'w' ? 1 : -1;
  if (line.mate != null) {
    // score mate N: N>0 = side to move mates in N, N<0 = gets mated in N
    const whiteMate = line.mate * sign;
    return { cp: null, mate: whiteMate };
  }
  return { cp: line.cp != null ? line.cp * sign : null, mate: null };
};

/**
 * `chesscom.engine.v1.Score` = { score: chess.v1.Score, depth, engine, ... }
 * and `chess.v1.Score` carries the oneof `score` -> {case,value}.
 */
function toEngineScore(v, depth, engineEnum, strengthEnum) {
  const inner = (v.mate != null)
    ? (v.mate > 0
      ? { case: 'mateInWhite', value: v.mate }
      : { case: 'mateInBlack', value: -v.mate })
    : { case: 'scoreCentipawnsWhite', value: Math.round(v.cp ?? 0) };
  return {
    score: { score: inner },
    depth,
    engine: engineEnum,
    variation: null,
    strength: strengthEnum,
    nodes: null,
  };
}

/* ----------------------------------------------------------- main review */

/**
 * @param {object} o
 * @param {Uint8Array} o.requestBytes  raw GameReviewRequest frame payload
 * @param {string} [o.engineKey]       preset key
 * @param {(p:number)=>void} [o.onProgress]
 * @param {(m:string)=>void} [o.onLog]
 * @param {{startFen:string, uci:string[]}} [o.pageGame]
 * @param {string} [o.pgn]             original PGN, used for annotatedPgn
 * @returns {Promise<{bytes:Uint8Array, stats:object}>}
 */
export async function buildGameReview(o) {
  const { requestBytes, onProgress = () => {}, onLog = () => {}, pageGame, pgn } = o;
  const req = decodeMessage('.chesscom.ceac.v2.GameReviewRequest', requestBytes);
  if (pageGame) req.__pageGame = pageGame;

  const { startFen, uci, meta } = extractGame(req);
  const n = uci.length;

  // strength / engine
  let strengthName = 'STRENGTH_STANDARD';
  const rs = req.runSearchReq && req.runSearchReq.search;
  let ss = null;
  if (rs && rs.case === 'gameReviewSearchSettings') ss = rs.value;
  const gs = req.newGameReq && req.newGameReq.newGame && req.newGameReq.newGame.settings;
  if (!ss && gs && gs.search && gs.search.case === 'gameReviewSearchSettings') ss = gs.search.value;
  if (ss && ss.strength != null) {
    strengthName = ['STRENGTH_UNSPECIFIED', 'STRENGTH_FAST', 'STRENGTH_STANDARD', 'STRENGTH_DEEP', 'STRENGTH_MAXIMUM'][Number(ss.strength)] || strengthName;
  }
  const depth = o.depth || DEPTH_BY_STRENGTH[strengthName] || 21;
  const engineKey = o.engineKey || 'stockfish-nnue-16';
  const engineEnum = ENGINE_ENUM[engineKey] ?? 10;
  const strengthEnum = { STRENGTH_FAST: 1, STRENGTH_STANDARD: 2, STRENGTH_DEEP: 3, STRENGTH_MAXIMUM: 4 }[strengthName] || 2;

  onLog(`game: ${n} moves, start ${startFen}`);
  onLog(`engine ${engineKey} depth ${depth} (strength ${strengthName})`);

  const book = await loadBook();
  const isBookPly = new Array(n + 1).fill(false);
  {
    const board = new Board(startFen);
    const seq = [];
    for (let i = 0; i < n; i++) {
      seq.push(uci[i]);
      isBookPly[i] = book.prefixes.has(seq.join(' '));
      board.apply(uci[i]);
    }
  }

  // ---- search every position once and reuse (N+1 searches)
  const engine = new UciEngine(engineKey);
  await engine.ready;
  const evals = new Array(n + 1);   // white-POV value of position i
  const bests = new Array(n + 1);   // best move (UCI) from position i
  const lineSets = new Array(n + 1);
  const sides = new Array(n + 1);
  const materialBefore = new Array(n + 1);

  {
    const b = new Board(startFen);
    for (let i = 0; i <= n; i++) {
      sides[i] = b.turn;
      materialBefore[i] = b.materialBalance();
      if (i < n) b.apply(uci[i]);
    }
  }

  for (let i = 0; i <= n; i++) {
    const prefix = uci.slice(0, i);
    const cmd = `position fen ${startFen}` + (prefix.length ? ` moves ${prefix.join(' ')}` : '');
    const { lines, bestmove } = await engine.search(cmd, { depth, multipv: 2 });
    const side = sides[i];
    const best = lines.length ? lines[0] : null;
    lineSets[i] = lines;
    evals[i] = whiteView(best, side);
    bests[i] = (best && best.pv && best.pv[0]) || bestmove || null;
    onProgress((i + 1) / (n + 1));
    if (i % 10 === 0) onLog(`  ply ${i}/${n} eval ${evals[i].cp ?? 'm' + evals[i].mate} best ${bests[i]}`);
  }

  // ---- per-move classification + accuracy
  const played = [];
  const losses = [];
  const classifications = [];
  for (let i = 0; i < n; i++) {
    const mover = sides[i];                       // side to move at ply i
    const before = evals[i], after = evals[i + 1];
    const val = (v) => (v.mate != null ? (v.mate > 0 ? 1000 : -1000) : (v.cp ?? 0));
    let loss = mover === 'w' ? val(before) - val(after) : val(after) - val(before);
    if (!Number.isFinite(loss)) loss = 0;
    loss = Math.max(0, loss);

    const lines = lineSets[i];
    const onlyMove = lines.length < 2;
    const bestUci = bests[i];

    // did the mover miss a forced mate?
    const mateForMover = before.mate != null && (mover === 'w' ? before.mate > 0 : before.mate < 0);
    const mateMissed = mateForMover && !!bestUci && bestUci !== uci[i];

    // sacrifice detection: mover's material dropped by >= BRILLIANT_SAC pawns
    const matDelta = mover === 'w'
      ? (materialBefore[i + 1] - materialBefore[i])
      : (materialBefore[i] - materialBefore[i + 1]);
    const sacForMover = matDelta <= -BRILLIANT_SAC;

    let cls;
    if (isBookPly[i] && loss < 120) cls = MC.BOOK;
    else {
      cls = classify({
        playedUci: uci[i], bestUci, loss, onlyMove, lines,
        sacForMover, mateForMover, mateMissed,
      });
    }
    classifications.push(cls);
    losses.push(loss);
    played.push({ uci: uci[i], loss, cls, side: mover });
  }

  // ---- tallies + accuracy
  const tally = { w: {}, b: {} };
  for (const p of played) {
    const key = MC_NAME[p.cls] || 'UNSPECIFIED';
    const bag = p.side === 'w' ? tally.w : tally.b;
    bag[key] = (bag[key] || 0) + 1;
  }
  const accW = mean(played.filter((p) => p.side === 'w').map((p) => moveAccuracy(p.loss)));
  const accB = mean(played.filter((p) => p.side === 'b').map((p) => moveAccuracy(p.loss)));

  // ---- eval graph ticks
  const ticks = [];
  for (let i = 0; i < n; i++) {
    const side = sides[i];
    const sideEnum = side === 'w' ? COLOR_WHITE : COLOR_BLACK;
    const sc = evals[i];
    const scoreMsg = toEngineScore(sc, depth, engineEnum, strengthEnum);
    ticks.push({
      moveClassification: classifications[i],
      moveScore: scoreMsg,
      isKeyMoment: classifications[i] === MC.BLUNDER || classifications[i] === MC.MISTAKE
        || classifications[i] === MC.BRILLIANT || classifications[i] === MC.MISSED,
      __side: sideEnum,
    });
    void sc;
  }

  // ---- played move messages
  const opening = openingFor(book, uci);
  const playedMoves = [];
  for (let i = 0; i < n; i++) {
    const side = sides[i];
    const from = uci[i].slice(0, 2), to = uci[i].slice(2, 4);
    const promo = uci[i][4];
    const bestUci = bests[i] || null;
    const cls = classifications[i];

    const moveMsg = {
      from: algToSquareEnum(from),
      to: algToSquareEnum(to),
      promotionPieceType: promo ? ({ n: 1, b: 2, r: 3, q: 4 })[promo] : null,
      castlingDetails: null,
    };

    const pm = {
      isKeyMoment: ticks[i].isKeyMoment,
      playedMove: { move: moveMsg, moveClassification: cls, score: null, speech: null, showMovesButtons: null, boardMarkings: null },
      bestAlternativeMove: null,
      movedColor: side === 'w' ? COLOR_WHITE : COLOR_BLACK,
      coachEmotion: null,
      skillsEarned: null,
      explainLine: null,
      bestNextMove: null,
    };

    // score attached to the move the player actually played = value after it
    const afterVal = evals[i + 1];
    pm.playedMove.score = toEngineScore(afterVal, depth, engineEnum, strengthEnum);

    if (bestUci && bestUci !== uci[i]) {
      pm.bestAlternativeMove = {
        move: {
          from: algToSquareEnum(bestUci.slice(0, 2)),
          to: algToSquareEnum(bestUci.slice(2, 4)),
          promotionPieceType: bestUci[4] ? ({ n: 1, b: 2, r: 3, q: 4 })[bestUci[4]] : null,
          castlingDetails: null,
        },
        moveClassification: MC.BEST, score: null, speech: null,
        showMovesButtons: null, boardMarkings: null,
      };
    }
    if (bestUci) {
      pm.bestNextMove = {
        from: algToSquareEnum(bestUci.slice(0, 2)),
        to: algToSquareEnum(bestUci.slice(2, 4)),
        promotionPieceType: bestUci[4] ? ({ n: 1, b: 2, r: 3, q: 4 })[bestUci[4]] : null,
        castlingDetails: null,
      };
    }
    pm.playedMove.speech = { sentences: [{ sentenceFragments: [{ fragment: sentenceFor(cls, played[i].loss, side) }] }] };
    pm.playedMove.showMovesButtons = {
      movesToShow: pm.bestAlternativeMove ? [pm.bestAlternativeMove] : [],
      showText: 'Show',
      hideText: 'Hide',
    };
    playedMoves.push(pm);
  }

  // ---- report card
  const metaPlayers = (meta && meta.players) || [];
  const whitePlayer = metaPlayers.find((p) => Number(p.color) === COLOR_WHITE);
  const blackPlayer = metaPlayers.find((p) => Number(p.color) === COLOR_BLACK);
  const whiteName = (whitePlayer && whitePlayer.name) || 'White';
  const blackName = (blackPlayer && blackPlayer.name) || 'Black';
  const whiteElo = playerRating(meta, COLOR_WHITE);
  const blackElo = playerRating(meta, COLOR_BLACK);

  const res = resultInfo(meta, startFen);
  const score = res.result === RESULT.WHITE_WIN ? 1 : res.result === RESULT.BLACK_WIN ? 0 : 0.5;
  const wdlW = wdl(whiteElo, blackElo);

  const card = (color, acc, ownElo, oppElo, name) => {
    const ownScore = color === COLOR_WHITE ? score : 1 - score;
    const oppScore = 1 - ownScore;
    const perf = perfRating(oppElo, ownScore);
    const accRating = Math.round(ownElo + (acc - 65) * 5);
    const gameRating = Math.round(0.55 * perf + 0.45 * accRating);
    const phase = (phAcc, p) => ({
      accuracyGlyph: MC.BEST,
      phase: p,
      accuracy: round1(phAcc),
      newRating: clampRating(Math.round(ownElo + (phAcc - 65) * 5)),
      ratingChange: clampDelta(Math.round((phAcc - 70) * 2.5)),
      name: `${name} vs ${color === COLOR_WHITE ? blackName : whiteName}`,
    });
    const phaseAcc = phaseAccuracies(played, color);
    return {
      playerName: name,
      reportsByPhase: [
        phase(phaseAcc.opening, PHASE.OPENING),
        phase(phaseAcc.middlegame, PHASE.MIDDLEGAME),
        phase(phaseAcc.endgame, PHASE.ENDGAME),
      ],
      reportsByCategory: [
        { statType: STAT.OPENING, accuracy: round1(phaseAcc.opening) },
        { statType: STAT.TACTICS, accuracy: round1(phaseAcc.tactics) },
        { statType: STAT.STRATEGY, accuracy: round1(phaseAcc.strategy) },
        { statType: STAT.ENDGAME, accuracy: round1(phaseAcc.endgame) },
      ],
      effectiveRating: clampRating(Math.round(ownElo + (acc - 65) * 3.5)),
      gameRatingV2: clampRating(gameRating),
      score: oppScore,
      __performance: perf,
      __accRating: accRating,
      __own: ownElo,
      __wdl: color === COLOR_WHITE ? wdlW : { w: wdlW.b, b: wdlW.w, d: wdlW.d },
      __phaseRaw: phaseAcc,
    };
  };

  const whiteCard = card(COLOR_WHITE, accW, whiteElo, blackElo, whiteName);
  const blackCard = card(COLOR_BLACK, accB, blackElo, whiteElo, blackName);

  // ---- summary / takeaways (our own wording)
  const accs = [accW, accB];
  const better = accW >= accB ? whiteName : blackName;
  const summary = `${whiteName} played with ${accW.toFixed(1)}% accuracy, ` +
    `${blackName} with ${accB.toFixed(1)}%. ${better} had the more accurate game.`;
  const worst = played.reduce((a, b) => (b.loss > a.loss ? b : a), played[0] || { loss: 0, cls: MC.BEST });
  const takeaways = [
    { takeaways: [`${better} was the more accurate player (${Math.max(accW, accB).toFixed(1)}% vs ${Math.min(accW, accB).toFixed(1)}%).`],
      playerName: better },
    { takeaways: [`${countCls(played, MC.BLUNDER)} blunder(s), ${countCls(played, MC.MISTAKE)} mistake(s) and ${countCls(played, MC.INACCURACY)} inaccuracy(s) were played in this game.`],
      playerName: 'both' },
    { takeaways: [`The biggest single loss was ${Math.round(worst.loss)} centipawns.`], playerName: 'both' },
  ];

  const finalBoard = new Board(startFen);
  for (const m of uci) finalBoard.apply(m);

  const reportCard = {
    white: whiteCard,
    black: blackCard,
    speech: '',
  };

  const gameReview = {
    evalGraph: { evalGraphTicks: ticks.map(({ __side, ...t }) => t) },
    highlights: {
      gameSummary: summary,
      accuracy: { white: round1(accW), black: round1(accB) },
      classificationTallies: {
        white: tallyList(tally.w),
        black: tallyList(tally.b),
      },
      reportCard,
      takeaways: { takeaways },
      gameSummaryCoachEmotion: null,
      gameSummaryPlay: summary,
    },
    review: {
      gameSummary: summary,
      startingFen: startFen,
      playedMoves,
      finalFen: finalBoard.fen(),
    },
    result: { result: res.result, resultType: res.resultType },
    metadata: {
      ceeVersion: { major: 1, minor: 211, patch: 5 },
      annotatedPgn: pgn ? annotatePgn(pgn, played, classifications) : null,
    },
    opening: opening ? {
      openingName: opening.name,
      ecoCode: opening.eco,
      url: 'https://www.chess.com/openings/' + opening.name.replace(/\s+/g, '-'),
      tcnMoves: opening.tcn,
    } : null,
  };

  const response = {
    result: { case: 'success', value: { gameReview, ceeC_APICalls: [] } },
  };

  const bytes = encodeMessage('.chesscom.ceac.v2.GameReviewResponse', response);
  onProgress(1);
  engine.terminate();

  return {
    bytes,
    stats: {
      moves: n, depth, engine: engineKey,
      accuracy: { white: round1(accW), black: round1(accB) },
      tallies: { white: tallyList(tally.w), black: tallyList(tally.b) },
      ratings: { white: whiteCard.gameRatingV2, black: blackCard.gameRatingV2 },
      opening: opening ? opening.name : null,
    },
  };
}

/* ------------------------------------------------------------- utilities */

function mean(a) { return a.length ? a.reduce((s, x) => s + x, 0) / a.length : 50; }
function round1(x) { return Math.round(x * 10) / 10; }
function clampRating(r) { return Math.max(400, Math.min(3500, r)); }
function clampDelta(d) { return Math.max(-400, Math.min(400, d)); }

/** Classic Elo performance rating from a score against `oppElo`. */
function perfRating(oppElo, s) {
  if (s <= 0) return oppElo - 400;
  if (s >= 1) return oppElo + 400;
  if (Math.abs(s - 0.5) < 1e-9) return oppElo;
  return clampRating(Math.round(oppElo + 400 * Math.log10(s / (1 - s))));
}

function phaseAccuracies(played, color) {
  const mine = played.filter((p) => p.side === (color === COLOR_WHITE ? 'w' : 'b'));
  if (!mine.length) return { opening: 70, middlegame: 70, endgame: 70, tactics: 70, strategy: 70 };
  const cut = Math.min(10, Math.floor(mine.length / 3));
  const slice = (a, b) => mine.slice(a, b);
  const acc = (arr) => mean(arr.map((p) => moveAccuracy(p.loss)));
  const opening = acc(slice(0, cut));
  const endgame = acc(slice(Math.floor(mine.length * 0.75)));
  const middlegame = acc(slice(cut, Math.floor(mine.length * 0.75)));
  const tactics = mean(mine.filter((p) => [MC.BRILLIANT, MC.GREAT_FIND, MC.BLUNDER, MC.MISSED].includes(p.cls)).map((p) => moveAccuracy(p.loss))) || middlegame;
  const strategy = mean(mine.filter((p) => [MC.BEST, MC.EXCELLENT, MC.GOOD, MC.MISTAKE].includes(p.cls)).map((p) => moveAccuracy(p.loss))) || middlegame;
  return { opening, middlegame, endgame, tactics, strategy };
}

function countCls(played, cls) { return played.filter((p) => p.cls === cls).length; }

function tallyList(bag) {
  return Object.entries(bag).map(([name, tally]) => ({ moveClassification: MC[name] ?? 0, tally }));
}

const MC_SENTENCE = {
  [MC.BOOK]: 'Book move.',
  [MC.BRILLIANT]: 'Brilliant!',
  [MC.GREAT_FIND]: 'Great find.',
  [MC.BEST]: 'Best move.',
  [MC.EXCELLENT]: 'Excellent move.',
  [MC.GOOD]: 'Good move.',
  [MC.INACCURACY]: 'This is an inaccuracy.',
  [MC.MISTAKE]: 'This is a mistake.',
  [MC.BLUNDER]: 'This is a blunder.',
  [MC.MISSED]: 'A strong continuation was missed.',
  [MC.FORCED]: 'Forced move.',
  [MC.TRICKY]: 'Tricky move.',
  [MC.UNSPECIFIED]: 'Move played.',
};

function sentenceFor(cls, loss, side) {
  const base = MC_SENTENCE[cls] || MC_SENTENCE[MC.UNSPECIFIED];
  if (cls === MC.BOOK || cls === MC.FORCED) return base;
  const cp = Math.round(loss);
  return cp > 0 ? `${base} It gives away about ${cp} centipawns.` : base;
}

/**
 * Inject `{ ... }` comments after each move of a movetext, in order.
 * Falls back to the untouched PGN if the shape is unexpected.
 */
export function annotatePgn(pgn, played, classifications) {
  if (!pgn) return null;
  const commentFor = (i) => {
    if (!played[i]) return '';
    const cls = classifications[i];
    const acc = round1(moveAccuracy(played[i].loss));
    return `{ ${MC_SENTENCE[cls] || ''} (${acc}%) }`;
  };
  const sep = pgn.indexOf('\n\n');
  const headers = sep >= 0 ? pgn.slice(0, sep + 2) : '';
  let body = sep >= 0 ? pgn.slice(sep + 2) : pgn;
  // Strip existing comments so indices stay aligned.
  body = body.replace(/\{[^}]*\}/g, ' ');

  let commentIdx = 0;
  const out = body.split(/(\s+)/).map((tok) => {
    if (/^\s+$/.test(tok) || tok === '') return tok;
    if (/^(1-0|0-1|1\/2-1\/2|\*)$/.test(tok)) return tok;
    if (/^\$\d+$/.test(tok)) return tok;
    if (/^\d+\.{1,3}$/.test(tok)) return tok;
    if (/^\d+\.\.\./.test(tok)) return tok;
    // a move token: contains a piece letter, '.', '#', or '+', and no '['
    if (/[\[\]]/.test(tok)) return tok;
    const c = commentFor(commentIdx++);
    return c ? `${tok} ${c}` : tok;
  }).join('');
  return commentIdx > 0 ? headers + out : pgn;
}
