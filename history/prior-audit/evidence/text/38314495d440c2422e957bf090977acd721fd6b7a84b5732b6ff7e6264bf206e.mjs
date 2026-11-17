// Probe 7: HUMAN game validation ([PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED], live 187140546024).
// Purpose: check whether proto6's mismatch vs chess.com was caused by the bot-game
// fixture (VsComputer source) or something in our request. Full page-faithful
// metadata this time: gameSource=LIVE, legacyGameId, timeControl 600, isRated,
// player userIds, userColor, enableSkills — exactly what oJe/lJe/W4e build.
//
// chess.com display (user paste, authoritative; card shows only 6 categories —
// Book/Good/Inaccuracy etc. exist in the response but are hidden):
//   white acc 76.8  Great 1 Best 13 Excellent 12 Mistake 2 Miss 1 Blunder 1  rating 1350
//   black acc 70.2  Great 0 Best 10 Excellent 9  Mistake 6 Miss 3 Blunder 0  rating 600
//
// Usage: node cee-proto7.mjs [strength 1..4] [outfile]
import { createRequire } from 'node:module';
import path from 'node:path';
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/proto7.s${STRENGTH}.out`;

const pending = [];
const out = [];
console.log = (...a) => { out.push(a.join(' ')); };
console.error = (...a) => { out.push('ERR: ' + a.join(' ')); };
const finish = (code) => { try { fs.writeFileSync(OUT, out.join('\n')); } catch {} process.exit(code); };
process.on('unhandledRejection', e => { console.error('UNHANDLED:', e && e.message || e); finish(1); });
process.on('uncaughtException', e => { console.error('UNCAUGHT:', e && e.message || e); finish(1); });

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
const engine = KOMODO_TEP(path.join(CEE_DIR, 'explanation-engine.wasm')); engine.onmessage=()=>{};
function api(call, args) {
  return new Promise((resolve, reject) => {
    pending.push({ resolve, reject, call });
    try { engine.postMessage({ call, args }, false, true); } catch (e) { pending.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function feature(gp, fid, typeName, obj) {
  const req = encodeMessage(typeName, obj);
  const handle = await api('CEE_NewFeature', [gp, fid, req]);
  try { return decodeMessage(typeName.replace(/Request$/, 'Response'), await api('CEE_Run', [handle])); }
  finally { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/doting-prospect.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-local
// into NewGame settings (page sends it in runSearchReq — merged server-side).
const settings = {
  locale: 'en_US',
  search: { case: 'gameReviewSearchSettings', value: { strength: STRENGTH } },
  userColor: 2,            // H4e(): reviewing user [PUBLIC_PLAYER_HANDLE_REDACTED] played BLACK
  enableSkills: true,      // NW(): card shows "Skills +3"
  enabledFeatureFlags: ['cee_tricky_classification'],
};

const t00 = Date.now();
const ng = await feature(-1, F.NEW_GAME, '.chesscom.explanation_engine.v1.NewGameRequest', {
  newGame: {
    from: {
      case: 'pgnGame',
      value: {
        pgn, takeFirstGameOnly: true,
        metadata: {
          players: [
            { color: 1, ratings: [{ rating: 100 }], name: '[PUBLIC_PLAYER_HANDLE_REDACTED]', chesscomMetadata: { userId: '[REDACTED_LITERAL]' } },
            { color: 2, ratings: [{ rating: 333 }], name: '[PUBLIC_PLAYER_HANDLE_REDACTED]', chesscomMetadata: { userId: '[REDACTED_LITERAL]' } },
          ],
          // X4e("600") → base 600s + 0 increment
          timeControl: { control: { case: 'base', value: { baseMs: 600000n, incrementMs: 0n } } },
          isRated: true,    // arena game
          chesscomMetadata: {
            legacyGameId: 186934806892n,  // oJe: BigInt ≠ 0 → sent
            gameSource: 2,                // aJe(Live) → CHESSCOM_GAME_SOURCE_LIVE
            // gameUuid unknown (callback 404 logged-out) → gameId omitted, oJe allows partial
          },
        },
      },
    },
    settings,
  },
});
let root = ng.playedLine[0].gamePoint;
function vint(n){const r=[];do{let b=n&127;n>>>=7;r.push(b|(n?128:0));}while(n);return Uint8Array.from(r)}
function cat(...xs){return Uint8Array.from(xs.flatMap(x=>Array.from(x)))}
function ld(n,b){return cat(vint(n*8+2),vint(b.length),b)}
function fields(b){let i=0;const r=[];function v(){let n=0,k=0,c;do{c=b[i++];n+=(c&127)*2**k;k+=7}while(c&128);return n}while(i<b.length){const start=i,t=v();let val;if((t&7)===0)val=v();else if((t&7)===2){let n=v();val=b.slice(i,i+n);i+=n}else if((t&7)===1)i+=8;else if((t&7)===5)i+=4;else throw Error('wire');r.push({n:t>>3,val,raw:b.slice(start,i)})}return r}
const gh=await api('CEE_NewFeature',[root,14,new Uint8Array()]);
const savedRaw=await api('CEE_Run',[gh]);await api('CEE_DisposeFeature',[gh]);
const state=fields(savedRaw).find(f=>f.n===1).val;
const modified=cat(...fields(state).filter(f=>f.n!==5).map(f=>f.raw),vint(5*8),vint(12));
const lh=await api('CEE_NewFeature',[-1,22,ld(1,modified)]);
const loaded=decodeMessage('.chesscom.explanation_engine.v1.LoadGameStateResponse',await api('CEE_Run',[lh]));await api('CEE_DisposeFeature',[lh]);
root=loaded.playedLine[0].gamePoint;
console.log('loaded source', (await feature(root,14,'.chesscom.explanation_engine.v1.GetGameStateRequest',{})).gameState?.defaultEvalSourceEngine);
console.log('root', root, 'NewGame took', ((Date.now() - t00) / 1000).toFixed(1) + 's');
try { await feature(root, F.SET_GAME_RESULT, '.chesscom.explanation_engine.v1.SetGameResultRequest', { claimedGameResult: { result: 2, resultType: 1 } }); }
catch (e) { console.error('SetGameResult failed:', e.message); }
try {
  const t0 = Date.now();
  const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', { startingGamePoint: root });
  console.log('GetGameReview took', ((Date.now() - t0) / 1000).toFixed(1) + 's');
  const g = gr.gameReview || {};
  const h = g.highlights || {};
  fs.writeFileSync('/home/user/research/doting-state12.json', JSON.stringify(g));
  console.log('accuracy:', JSON.stringify(h.accuracy));
  console.log('reportCard:', JSON.stringify(h.reportCard)?.slice(0, 900));
  const tallies = h.classificationTallies || {};
  console.log('tallies.white:', JSON.stringify(tallies.white));
  console.log('tallies.black:', JSON.stringify(tallies.black));
  const moves = g.review?.playedMoves || [];
  console.log('moves:', moves.length);
  console.log('opening:', JSON.stringify(g.opening));
  console.log('metadata:', JSON.stringify(g.metadata)?.slice(0, 300));
  console.log('result:', JSON.stringify(g.result));
  let skills = 0, withArrows = 0, sentences = 0, withHash = 0;
  const clsList = [];
  for (const m of moves) {
    const pm = m.playedMove || {};
    clsList.push(pm.moveClassification);
    if (pm.skillsEarned) skills++;
    if ((pm.boardMarkings?.arrows || []).length) withArrows++;
    for (const s of pm.speech?.sentences || []) {
      sentences++;
      if (s.audioUrlHash) withHash++;
    }
  }
  console.log('classifications:', clsList.join(','));
  console.log('skillsEarned moves:', skills, ' arrows:', withArrows, ' sentences:', sentences, ' withHash:', withHash);
  const eg = g.evalGraph?.evalGraphTicks || [];
  console.log('ticks:', eg.length, 'engines:', [...new Set(eg.map(t => t.moveScore?.engine))].join(','), 'depths:', [...new Set(eg.map(t => t.moveScore?.depth))].join(','));
  for (const m of moves) {
    const pm = m.playedMove || {};
    const cls = pm.moveClassification;
    if (cls && cls !== 1) {
      const sp = (pm.speech?.sentences || []).map(s => (s.sentenceFragments || []).map(f => f.fragment).join('')).join(' | ');
      console.log(`  cls=${cls} ${pm.move?.from}-${pm.move?.to} bm=${(pm.boardMarkings?.arrows || []).length} hash=${pm.speech?.sentences?.[0]?.audioUrlHash ? 'Y' : 'N'} :: ${sp.slice(0, 110)}`);
    }
  }
  finish(0);
} catch (e) { console.error('GetGameReview failed:', e.message); finish(1); }
