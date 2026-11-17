// Probe 4: RunSearch behavior — engine_id variants, gameReviewSearchSettings, response shape.
import { createRequire } from 'node:module';
import path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
globalThis.postMessage = (msg) => {
  if (typeof msg === 'string') return;
  const head = pending[0];
  if (!head) return;
  if (msg.error) { pending.shift(); head.reject(new Error(msg.error)); return; }
  if (head.call === 'CEE_Run' && 'proto' in msg) { if (msg.is_final) { pending.shift(); head.resolve(msg.proto); } return; }
  if ('retval' in msg) { pending.shift(); head.resolve(msg.retval); return; }
  if (msg.call && String(msg.call).endsWith('_done')) { pending.shift(); head.resolve(msg); return; }
};
const KOMODO_TEP = require(path.join(CEE_DIR, 'explanation-engine.js'));
const engine = KOMODO_TEP(path.join(CEE_DIR, 'explanation-engine.wasm'));
function api(call, args) {
  return new Promise((resolve, reject) => {
    pending.push({ resolve, reject, call });
    try { engine.postMessage({ call, args }, false, true); } catch (e) { pending.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, RUN_SEARCH:29, SET_GAME_RESULT:30 };
async function feature(gp, fid, typeName, obj) {
  const req = encodeMessage(typeName, obj);
  const handle = await api('CEE_NewFeature', [gp, fid, req]);
  try { return decodeMessage(typeName.replace(/Request$/, 'Response'), await api('CEE_Run', [handle])); }
  finally { api('CEE_DisposeFeature', [handle]).catch(()=>{}); }
}
const pgn = `[Event "T"][White "A"][Black "B"][Result "1-0"]

1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O d3 8. Qb3 Qf6 9. e5 Qg6 10. Re1 Nge7 11. Ba3 d5 12. Bxd5 Nxd5 13. c4 1-0`;

const ng = await feature(-1, F.NEW_GAME, '.chesscom.explanation_engine.v1.NewGameRequest', {
  newGame: { from: { case:'pgnGame', value:{ pgn, takeFirstGameOnly:true } },
    settings: { locale:'en_US' } } });   // NO search settings — like the real CEAC request
const root = ng.playedLine[0].gamePoint;
console.log('root', root, 'played', ng.playedLine.length);

// A) RunSearch at root, gameReviewSearchSettings STANDARD, no engine_id
try {
  const t0 = Date.now();
  const rs = await feature(root, F.RUN_SEARCH, '.chesscom.explanation_engine.v1.RunSearchRequest', {
    search: { case:'gameReviewSearchSettings', value:{ strength: 2 } },  // STRENGTH_STANDARD
    searchMoves: [], streamResults: false, heartbeatIntervalSeconds: 0 });
  console.log('RunSearch(no engine_id) took', ((Date.now()-t0)/1000).toFixed(1)+'s');
  console.log('  evals:', (rs.evaluations||[]).length, 'progress:', rs.progress, 'aborted:', rs.aborted);
  const e0 = (rs.evaluations||[])[0];
  if (e0) console.log('  eval0:', JSON.stringify(e0).slice(0,300));
} catch (e) { console.log('RunSearch(no engine_id) FAILED:', String(e.message).slice(0,300)); }

// B) GameReview WITHOUT search settings — does it use RunSearch's evals?
try {
  const t0 = Date.now();
  const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', { startingGamePoint: root });
  console.log('GetGameReview took', ((Date.now()-t0)/1000).toFixed(1)+'s');
  const eg = gr.gameReview?.evalGraph?.evalGraphTicks || [];
  console.log('ticks:', eg.length, 'tick0:', JSON.stringify(eg[0]));
  console.log('accuracy:', JSON.stringify(gr.gameReview?.highlights?.accuracy));
} catch (e) { console.log('GetGameReview FAILED:', String(e.message).slice(0,300)); }
process.exit(0);
