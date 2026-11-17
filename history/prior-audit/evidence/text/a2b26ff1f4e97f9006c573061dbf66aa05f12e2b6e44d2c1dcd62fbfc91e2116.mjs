// Probe 3: correct SetGameResult + full `game` from-case with player ratings → reportCard?
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
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, GET_GAME_RESULT:7, MAKE_MOVES:24 };
async function feature(gp, fid, typeName, obj) {
  const req = encodeMessage(typeName, obj);
  const handle = await api('CEE_NewFeature', [gp, fid, req]);
  try { return decodeMessage(typeName.replace(/Request$/, 'Response'), await api('CEE_Run', [handle])); }
  finally { api('CEE_DisposeFeature', [handle]).catch(()=>{}); }
}
const pgn = `[Event "T"][White "PlayerW"][Black "PlayerB"][Result "1-0"][WhiteElo "1850"][BlackElo "1790"]

1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O d3 8. Qb3 Qf6 9. e5 Qg6 10. Re1 Nge7 11. Ba3 d5 12. Bxd5 Nxd5 13. c4 1-0`;

const ng = await feature(-1, F.NEW_GAME, '.chesscom.explanation_engine.v1.NewGameRequest', {
  newGame: { from: { case:'pgnGame', value:{ pgn, takeFirstGameOnly:true,
      metadata: { players: [
        { color: 1, ratings: [{rating: 1850}], name: 'PlayerW' },
        { color: 2, ratings: [{rating: 1790}], name: 'PlayerB' },
      ], timeControl: { /* unknown fields ok */ } } } },
    settings: { locale:'en_US', search:{case:'preset', value:4} } } });
const root = ng.playedLine[0].gamePoint;
console.log('root', root);

// correct GameResult: plain enums
try {
  await feature(root, F.SET_GAME_RESULT, '.chesscom.explanation_engine.v1.SetGameResultRequest', {
    claimedGameResult: { result: 1, resultType: 4 } });  // WHITE_WIN, RESIGNATION
  console.log('setGameResult OK');
} catch (e) { console.log('setGameResult FAILED:', String(e.message).slice(0,200)); }

const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', {
  startingGamePoint: root, includeTrainTakeaways: false });
const h = gr.gameReview.highlights || {};
console.log('reportCard:', JSON.stringify(h.reportCard)?.slice(0,1500));
console.log('result:', JSON.stringify(gr.gameReview.result));
console.log('accuracy:', JSON.stringify(h.accuracy));
process.exit(0);
