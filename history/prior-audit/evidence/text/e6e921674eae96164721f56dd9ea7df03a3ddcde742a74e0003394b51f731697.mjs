// End-to-end test: request -> local engine -> GameReviewResponse, plus the
// protobuf and chess plumbing it depends on.  Run with:  node test/run-test.mjs

import { NodeWorkerShim } from './worker-shim.mjs';
globalThis.Worker = NodeWorkerShim;

process.on('unhandledRejection', (e) => console.warn('[unhandledRejection]', (e && e.message) || e));
process.on('uncaughtException', (e) => console.warn('[uncaughtException]', (e && e.message) || e));

const { encodeMessage, decodeMessage, frame, unframe } = await import('../lib/protobuf.js');
const { buildGameReview, loadBook, annotatePgn } = await import('../lib/review.js');
const { START_FEN, pgnToUci, Board, algToSquareEnum, sanToUci } = await import('../lib/chess.js');

let failures = 0;
const ok = (cond, label, extra = '') => {
  if (cond) console.log(`  PASS  ${label}${extra ? '  ' + extra : ''}`);
  else { failures++; console.log(`  FAIL  ${label}${extra ? '  ' + extra : ''}`); }
};

console.log('== 1. book ==');
const book = await loadBook();
console.log(`  ${book.entries.length} openings, ${book.prefixes.size} line prefixes`);
ok(book.entries.length > 5000, 'book loaded');

console.log('== 2. SAN / PGN ==');
const pgn = [
  '[Event "Test Game"]', '[Site "?"]', '[Date "????.??.??"]',
  '[White "Alice"]', '[Black "Bob"]', '[Result "*"]', '',
  '1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O d3',
  '8. Qb3 Qf6 9. e5 Qg6 10. Re1 Nge7 *',
].join('\n');
const uci = pgnToUci(pgn);
console.log('  uci:', uci.join(' '));
ok(uci.length === 20, 'parsed 20 plies from PGN', `got ${uci.length}`);

{
  const b = new Board(START_FEN);
  for (const m of uci) {
    const r = sanToUci(b, 'e4'); // sanity only on first
    void r;
    b.apply(m);
  }
  ok(b.fullmove === 11 && b.turn === 'w', 'board walk lands on move 11, white to play',
    `fullmove=${b.fullmove} turn=${b.turn}`);
}

console.log('== 3. request encode / decode ==');
const game = {
  startingPosition: null,
  moves: uci.map((m) => ({
    move: {
      from: algToSquareEnum(m.slice(0, 2)),
      to: algToSquareEnum(m.slice(2, 4)),
      promotionPieceType: m[4] ? ({ n: 1, b: 2, r: 3, q: 4 })[m[4]] : null,
      castlingDetails: null,
    },
    metadata: null,
    variations: [],
  })),
  metadata: {
    players: [
      { name: 'Alice', color: 1, ratings: [{ rating: 1420 }] },
      { name: 'Bob', color: 2, ratings: [{ rating: 1385 }] },
    ],
    result: { result: 1, resultType: 4 },
    timeControl: null,
    timestamps: null,
    rules: null,
    chesscomMetadata: null,
    link: null,
    timeClass: null,
    isRated: null,
    pgnHeaders: [],
  },
};
const request = {
  newGameReq: { newGame: { from: { case: 'game', value: game } }, enableTypedInvalidGameErrors: false },
  runSearchReq: {
    search: { case: 'gameReviewSearchSettings', value: { strength: 1 } },
  },
  engine: 10,
  gameEvaluationOptions: null,
  requestMetadata: null,
  requestOptions: null,
  setCoach: null,
  charmInfReq: null,
  gameReviewOptions: null,
};

const requestBytes = encodeMessage('.chesscom.ceac.v2.GameReviewRequest', request);
console.log(`  request is ${requestBytes.length} bytes`);
const back = decodeMessage('.chesscom.ceac.v2.GameReviewRequest', requestBytes);
ok(back.newGameReq?.newGame?.from?.case === 'game', 'request round-trips the oneof case',
  String(back.newGameReq?.newGame?.from?.case));
ok(back.newGameReq?.newGame?.from?.value?.moves?.length === 20, 'request round-trips 20 moves',
  String(back.newGameReq?.newGame?.from?.value?.moves?.length));
ok(back.newGameReq?.newGame?.from?.value?.metadata?.players?.[0]?.ratings?.[0]?.rating === 1420,
  'player rating round-trips',
  JSON.stringify(back.newGameReq?.newGame?.from?.value?.metadata?.players?.[0]));
ok(back.runSearchReq?.search?.case === 'gameReviewSearchSettings', 'strength oneof round-trips',
  String(back.runSearchReq?.search?.case));
ok(back.runSearchReq?.search?.value?.strength === 1, 'strength value round-trips',
  String(back.runSearchReq?.search?.value?.strength));

console.log('== 4. review build (this is the slow part) ==');
const t0 = Date.now();
const { bytes, stats } = await buildGameReview({
  requestBytes,
  depth: 14,
  pgn,
  onLog: (m) => console.log('   ', m),
  onProgress: (p) => { if (p === 1 || Math.round(p * 20) !== Math.round((p - 0.05) * 20)) process.stdout.write(`\r   ${(p * 100).toFixed(0)}%   `); },
});
console.log(`\n   built in ${((Date.now() - t0) / 1000).toFixed(1)}s, ${bytes.length} bytes`);
console.log('   stats:', JSON.stringify(stats, null, 2));

console.log('== 5. response decode ==');
const resp = decodeMessage('.chesscom.ceac.v2.GameReviewResponse', bytes);
ok(resp.result?.case === 'success', 'result is success', String(resp.result?.case));
const gr = resp.result?.value?.gameReview;
ok(!!gr, 'gameReview present');
ok(gr?.evalGraph?.evalGraphTicks?.length === 20, 'eval graph has 20 ticks',
  String(gr?.evalGraph?.evalGraphTicks?.length));
ok(gr?.review?.playedMoves?.length === 20, 'playedMoves has 20 entries',
  String(gr?.review?.playedMoves?.length));
ok(typeof gr?.review?.startingFen === 'string' && gr.review.startingFen.split(' ')[0].split('/').length === 8,
  'startingFen is an 8-rank FEN', gr?.review?.startingFen);
ok(typeof gr?.review?.finalFen === 'string' && gr.review.finalFen.includes(' '), 'finalFen present',
  gr?.review?.finalFen);
ok(gr?.highlights?.accuracy?.white > 0 && gr.highlights.accuracy.white <= 100,
  'white accuracy in range', String(gr?.highlights?.accuracy?.white));
ok(gr?.highlights?.accuracy?.black > 0 && gr.highlights.accuracy.black <= 100,
  'black accuracy in range', String(gr?.highlights?.accuracy?.black));
ok((gr?.highlights?.classificationTallies?.white || []).length > 0, 'white tallies present');
ok((gr?.highlights?.classificationTallies?.black || []).length > 0, 'black tallies present');
ok((gr?.highlights?.reportCard?.white?.reportsByPhase || []).length === 3, '3 phases on white card');
ok((gr?.highlights?.reportCard?.white?.reportsByCategory || []).length === 4, '4 categories on white card');
ok(typeof gr?.highlights?.reportCard?.white?.gameRatingV2 === 'number',
  'white gameRatingV2', String(gr?.highlights?.reportCard?.white?.gameRatingV2));
ok(typeof gr?.highlights?.reportCard?.white?.effectiveRating === 'number',
  'white effectiveRating', String(gr?.highlights?.reportCard?.white?.effectiveRating));
ok(typeof gr?.metadata?.annotatedPgn === 'string' && gr.metadata.annotatedPgn.includes('{'),
  'annotatedPgn carries comments');
ok(!!gr?.opening, 'opening detected', gr?.opening?.openingName || '(none)');

const first = gr?.review?.playedMoves?.[0];
ok(typeof first?.playedMove?.move?.from === 'number', 'move.from is a Square enum',
  String(first?.playedMove?.move?.from));
ok(typeof first?.playedMove?.moveClassification === 'number', 'moveClassification is an enum number',
  String(first?.playedMove?.moveClassification));
ok(typeof first?.playedMove?.score?.score?.score?.case === 'string',
  'move score oneof present', JSON.stringify(first?.playedMove?.score));
ok(!!first?.playedMove?.speech?.sentences?.[0]?.sentenceFragments?.[0]?.fragment,
  'speech sentence present', JSON.stringify(first?.playedMove?.speech).slice(0, 240));

const tick0 = gr?.evalGraph?.evalGraphTicks?.[0];
ok(typeof tick0?.moveScore?.score?.score?.value === 'number', 'tick score has a numeric value',
  JSON.stringify(tick0?.moveScore?.score));

console.log('== 6. re-encode round trip ==');
const re = encodeMessage('.chesscom.ceac.v2.GameReviewResponse', resp);
ok(re.length === bytes.length, 're-encoded length matches', `${re.length} vs ${bytes.length}`);
const resp2 = decodeMessage('.chesscom.ceac.v2.GameReviewResponse', re);
ok(resp2.result?.value?.gameReview?.review?.playedMoves?.length === 20, 'second decode keeps 20 moves');

console.log('== 7. framing ==');
const framed = frame(bytes);
const parts = unframe(framed);
ok(parts.length === 1 && parts[0].length === bytes.length, 'frame/unframe round trip',
  `${framed.length} bytes, ${parts.length} part(s)`);

console.log('== 8. annotated pgn ==');
console.log(gr?.metadata?.annotatedPgn?.split('\n').slice(-1)[0]?.slice(0, 400));

console.log(failures ? `\n${failures} FAILURES` : '\nALL PASS');
process.exit(failures ? 1 : 0);
