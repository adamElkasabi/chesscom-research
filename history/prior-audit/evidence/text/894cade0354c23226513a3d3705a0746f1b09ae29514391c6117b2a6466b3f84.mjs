// Prototype: drive chess.com's CEE wasm (explanation-engine) directly in Node.
// Protocol: CEE_NewFeature(gamePoint, featureId, requestBytes) -> retval handle;
//           CEE_Run(handle) -> {proto, is_final} via global postMessage.
import { createRequire } from 'node:module';
import path from 'node:path';

const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

// ---- capture global postMessage (api responses) ----
const pending = [];   // {resolve, reject, call}
let logLines = [];
globalThis.postMessage = (msg) => {
  if (typeof msg === 'string') { logLines.push(msg); if (process.env.CEE_LOG) console.log('[cee-log]', msg); return; }
  const head = pending[0];
  if (!head) { console.log('[cee] unsolicited:', Object.keys(msg), msg.error || ''); return; }
  if (msg.error) { pending.shift(); head.reject(new Error(msg.error)); return; }
  if (head.call === 'CEE_Run' && Object.prototype.hasOwnProperty.call(msg, 'proto')) {
    if (msg.is_final) { pending.shift(); head.resolve(msg.proto); }
    return; // intermediate stream chunk
  }
  if (Object.prototype.hasOwnProperty.call(msg, 'retval')) { pending.shift(); head.resolve(msg.retval); return; }
  console.log('[cee] unexpected msg for', head.call, Object.keys(msg));
};

const KOMODO_TEP = require(path.join(CEE_DIR, 'explanation-engine.js'));
const engine = KOMODO_TEP(path.join(CEE_DIR, 'explanation-engine.wasm'));
engine.onmessage = (line) => { if (process.env.CEE_LOG) console.log('[uci]', line); };

function api(call, args) {
  return new Promise((resolve, reject) => {
    pending.push({ resolve, reject, call });
    try { engine.postMessage({ call, args }, false, true); }
    catch (e) { pending.shift(); reject(e); }
  });
}

// ---- our protobuf codec ----
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');

const F = { ADD_EVALUATIONS:1, MOVE_CLASSIFICATION:25, NEW_GAME:26, RUN_SEARCH:29, SIMPLE_THREATS:31,
            GAME_REVIEW:42, SET_COACH:41, LOAD_AND_SET_COACH:48, MAKE_MOVES:24, GET_OPENING:16 };

async function feature(gamePoint, featureId, typeName, obj) {
  const req = encodeMessage(typeName, obj);
  const handle = await api('CEE_NewFeature', [gamePoint, featureId, req]);
  try {
    const resp = await api('CEE_Run', [handle]);
    return decodeMessage(typeName.replace(/Request$/, 'Response'), resp);
  } finally {
    api('CEE_DisposeFeature', [handle]).catch(() => {});
  }
}

const pgn = process.argv[2] || `[Event "Test"]
[White "A"]
[Black "B"]
[Result "1-0"]

1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O d3 8. Qb3 Qf6 9. e5 Qg6 10. Re1 Nge7 11. Ba3 d5 12. Bxd5 Nxd5 13. c4 1-0`;

console.log('== CreateNewGame (feature 26, gamePoint -1)');
const ng = await feature(-1, F.NEW_GAME, '.chesscom.explanation_engine.v1.NewGameRequest', {
  newGame: {
    from: { case: 'pgnGame', value: { pgn, takeFirstGameOnly: true, metadata: { rules: { isChess960: false } } } },
    settings: {
      locale: 'en_US',
      search: { case: 'preset', value: 4 },   // SEARCH_PRESET_GAME_REVIEW_STANDARD=4
      enabledFeatureFlags: ['cee_tricky_classification'],
      moveClassificationVersion: 2,
      gameAnalysisSpeechVersion: 2,
    },
  },
});
if (ng.invalidGame) { console.error('INVALID GAME', JSON.stringify(ng.invalidGame)); process.exit(1); }
const root = ng.playedLine?.[0]?.gamePoint;
console.log('root game point:', root, ' played line length:', ng.playedLine?.length);
console.log('sample game points:', ng.playedLine?.slice(0,4).map(g => g.gamePoint));

console.log('== GetGameReview (feature 42)');
const t0 = Date.now();
const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', {
  startingGamePoint: root,
  includeTrainTakeaways: false,
  canAccessLockedTakeaways: false,
});
console.log('took', ((Date.now()-t0)/1000).toFixed(1), 's');
const review = gr.gameReview;
if (!review) { console.error('NO game_review; keys:', Object.keys(gr)); process.exit(1); }

// ---- summarize ----
const h = review.highlights || {};
console.log('accuracy:', JSON.stringify(h.accuracy));
console.log('tallies:', JSON.stringify(h.classificationTallies));
console.log('reportCard:', JSON.stringify(h.reportCard)?.slice(0, 800));
console.log('gameSummary:', JSON.stringify(h.gameSummary)?.slice(0, 300));
const moves = review.review?.playedMoves || [];
console.log('playedMoves:', moves.length);
for (const m of moves.slice(0, 12)) {
  const pm = m.playedMove || {};
  const sp = pm.speech?.sentences?.[0]?.sentenceFragments?.map(f=>f.fragment).join('') ?? '';
  const bm = pm.boardMarkings?.arrows?.length ?? 0;
  console.log(`  move ${pm.move?.from}-${pm.move?.to} cls=${pm.moveClassification} score=${JSON.stringify(pm.score)} arrows=${bm} speech="${sp.slice(0,70)}" hash=${pm.speech?.sentences?.[0]?.audioUrlHash ?? '-'}`);
}
const eg = review.evalGraph?.evalGraphTicks || [];
console.log('evalGraph ticks:', eg.length, 'first:', JSON.stringify(eg[0]), 'tick5:', JSON.stringify(eg[5]));
console.log('opening:', JSON.stringify(review.opening)?.slice(0,200));
console.log('metadata ceeVersion:', review.metadata?.ceeVersion, ' annotatedPgn len:', (review.metadata?.annotatedPgn||'').length);
console.log('annotatedPgn head:', (review.metadata?.annotatedPgn||'').slice(0,400));
console.log('log lines:', logLines.length);
process.exit(0);
