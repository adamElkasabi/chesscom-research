// Probe 5: search settings inside NewGame (automatic continuation) + full move dump.
import { createRequire } from 'node:module';
import path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(a.join(' '));}; const _err=console.error; console.error=(...a)=>{out.push('ERR: '+a.join(' '));};
process.on('unhandledRejection', e => { console.error('UNHANDLED:', e && e.message || e); require('fs').writeFileSync('/tmp/proto5.out', out.join('\n')+'\nERROR: '+(e&&e.message||e)); require('fs').writeFileSync('/tmp/proto5.out', out.join('\n')+'\nUNHANDLED'); process.exit(1); });
process.on('uncaughtException', e => { console.error('UNCAUGHT:', e && e.message || e); require('fs').writeFileSync('/tmp/proto5.out', out.join('\n')+'\nERROR: '+(e&&e.message||e)); require('fs').writeFileSync('/tmp/proto5.out', out.join('\n')+'\nUNHANDLED'); process.exit(1); });
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
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async function feature(gp, fid, typeName, obj) {
  const req = encodeMessage(typeName, obj);
  const handle = await api('CEE_NewFeature', [gp, fid, req]);
  try { return decodeMessage(typeName.replace(/Request$/, 'Response'), await api('CEE_Run', [handle])); }
  finally { api('CEE_DisposeFeature', [handle]).catch(()=>{}); }
}
const pgn = process.argv[2] || `[Event "T"][White "A"][Black "B"][Result "1-0"][WhiteElo "1850"][BlackElo "1790"]

1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O d3 8. Qb3 Qf6 9. e5 Qg6 10. Re1 Nge7 11. Ba3 d5 12. Bxd5 Nxd5 13. c4 1-0`;

// search = gameReviewSearchSettings INSIDE NewGame settings (like analysis.js does with preset)
const ng = await feature(-1, F.NEW_GAME, '.chesscom.explanation_engine.v1.NewGameRequest', {
  newGame: { from: { case:'pgnGame', value:{ pgn, takeFirstGameOnly:true,
      metadata: { players: [ { color: 1, ratings: [{rating: 1850}], name: 'PlayerW' }, { color: 2, ratings: [{rating: 1790}], name: 'PlayerB' } ] } } },
    settings: { locale:'en_US',
      search: { case:'gameReviewSearchSettings', value:{ strength: 2 } },
      moveClassificationVersion: 2, gameAnalysisSpeechVersion: 2 } } });
const root = ng.playedLine[0].gamePoint;
console.log('root', root);
try { await feature(root, F.SET_GAME_RESULT, '.chesscom.explanation_engine.v1.SetGameResultRequest', { claimedGameResult:{ result:1, resultType:4 } }); } catch(e){ console.error('SetGameResult failed:', e.message); }
try {
const t0 = Date.now();
const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', { startingGamePoint: root });
console.log('GetGameReview took', ((Date.now()-t0)/1000).toFixed(1)+'s');
const h = gr.gameReview.highlights || {};
console.log('accuracy:', JSON.stringify(h.accuracy));
console.log('reportCard:', JSON.stringify(h.reportCard)?.slice(0,700));
const moves = gr.gameReview.review?.playedMoves || [];
console.log('moves:', moves.length);
let withArrows = 0, withSpeechArrows = 0;
for (const m of moves) {
  const pm = m.playedMove || {};
  if ((pm.boardMarkings?.arrows||[]).length) withArrows++;
  for (const s of pm.speech?.sentences||[]) for (const f of s.sentenceFragments||[]) if (f.arrowsAndSquares) withSpeechArrows++;
}
console.log('moves with boardMarkings arrows:', withArrows, ' speech fragments with arrowsAndSquares:', withSpeechArrows);
for (const m of moves) {
  const pm = m.playedMove || {};
  const cls = pm.moveClassification;
  if (cls && cls !== 1) {
    const bm = pm.boardMarkings?.arrows||[];
    const sp = (pm.speech?.sentences||[]).map(s=>(s.sentenceFragments||[]).map(f=>f.fragment).join('')).join(' | ');
    const arrowsInSpeech = (pm.speech?.sentences||[]).some(s=>(s.sentenceFragments||[]).some(f=>f.arrowsAndSquares));
    console.log(`  cls=${cls} ${pm.move?.from}-${pm.move?.to} bmArrows=${bm.length} speechArrows=${arrowsInSpeech} hash=${pm.speech?.sentences?.[0]?.audioUrlHash? 'Y':'N'} :: ${sp.slice(0,90)}`);
  }
}
const eg = gr.gameReview.evalGraph?.evalGraphTicks||[];
console.log('tick engines:', [...new Set(eg.map(t=>t.moveScore?.engine))], 'depths:', eg.map(t=>t.moveScore?.depth).join(','));
require('fs').writeFileSync('/tmp/proto5.out', out.join('\n')); process.exit(0); } catch(e){ console.error('GetGameReview failed:', e.message); require('fs').writeFileSync('/tmp/proto5.out', out.join('\n')+'\nERROR: '+(e&&e.message||e)); process.exit(1); }
