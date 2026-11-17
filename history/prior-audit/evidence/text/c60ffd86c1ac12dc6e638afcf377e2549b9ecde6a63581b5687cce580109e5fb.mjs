// Probe 2: charm inference (grv2), stats, takeaways, setGameResult — what fills reportCard?
import { createRequire } from 'node:module';
import path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
globalThis.postMessage = (msg) => {
  if (typeof msg === 'string') return;
  const head = pending[0];
  if (!head) { console.log('[cee] unsolicited:', Object.keys(msg)); return; }
  if (msg.error) { pending.shift(); head.reject(new Error(msg.error)); return; }
  if (head.call === 'CEE_Run' && 'proto' in msg) { if (msg.is_final) { pending.shift(); head.resolve(msg.proto); } return; }
  if ('retval' in msg) { pending.shift(); head.resolve(msg.retval); return; }
  if (msg.call && head.call==='CEE_LoadCharmModel' && String(msg.call).endsWith('_done')) { pending.shift(); head.resolve(msg); return; }
  console.log('[cee] unexpected for', head.call, Object.keys(msg));
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
const F = { NEW_GAME:26, GAME_REVIEW:42, CHARM_INFERENCE:68, SET_GAME_RESULT:30, ADD_CHARM_INFERENCE:69 };
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
    settings: { locale:'en_US', search:{case:'preset', value:4}, enabledFeatureFlags:['cee_tricky_classification','cee_charm_inference_grv2'], moveClassificationVersion:2, gameAnalysisSpeechVersion:2 } } });
const root = ng.playedLine[0].gamePoint;
console.log('root', root);

// A) charm inference grv2 directly
try {
  const ci = await feature(root, F.CHARM_INFERENCE, '.chesscom.explanation_engine.v1.CharmInferenceRequest', { grv2: {} });
  console.log('CHARM grv2 results:', JSON.stringify(ci.results).slice(0,600));
} catch (e) { console.log('CHARM grv2 FAILED:', e.message); }

// B) set game result (white wins 1-0)
try {
  const r = await feature(root, F.SET_GAME_RESULT, '.chesscom.explanation_engine.v1.SetGameResultRequest', {
    claimedGameResult: { winner:{case:'color', value:1}, resultType:{case:'resultType', value:2} } });
  console.log('setGameResult:', JSON.stringify(r));
} catch (e) { console.log('setGameResult FAILED:', e.message); }

// C) game review with takeaways
const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', {
  startingGamePoint: root, includeTrainTakeaways: true, canAccessLockedTakeaways: false,
  stats: { advancedStatsUser: { advancedStatsPercentiles: [], categoryPerformances: [] } } });
const h = gr.gameReview.highlights || {};
console.log('reportCard:', JSON.stringify(h.reportCard)?.slice(0,1200));
console.log('takeaways:', JSON.stringify(h.takeaways)?.slice(0,400));
console.log('result:', JSON.stringify(gr.gameReview.result)?.slice(0,300));
process.exit(0);
