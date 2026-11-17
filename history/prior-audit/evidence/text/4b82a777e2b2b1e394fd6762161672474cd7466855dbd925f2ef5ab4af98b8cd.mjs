// Probe 6: example game ([PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED], 1-0 checkmate) through the
// proven local review flow. Prints accuracy / reportCard / tallies so they can be
// compared with chess.com's own display (user paste, authoritative):
//   white acc 86.8  Great 4 Best 20 Excellent 22 Mistake 0 Miss 1 Blunder 0  rating 1850
//   black acc 79.8  Great 0 Best 18 Excellent 21 Mistake 5 Miss 1 Blunder 1  rating 1500
//
// Usage: node cee-proto6.mjs [strength 1..4] [versions 0|2] [outfile]
//   strength 1 = Fast (default page depth 18), 2 = Standard (depth 22)
//   MODE=preset → settings.search = {case:'preset', value:<strength>} (SearchPreset enum, page Uk style)
//   versions 0 = settings.ver unspecified (as the real W4e request sends), 2 = V3/2 (proto5 style)
import { createRequire } from 'node:module';
import path from 'node:path';
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const VERSIONS = Number(process.argv[3] || 0);
const OUT = process.argv[4] || `/tmp/proto6.s${STRENGTH}.v${VERSIONS}.out`;

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
const engine = KOMODO_TEP(path.join(CEE_DIR, 'explanation-engine.wasm'));
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

const pgn = fs.readFileSync('/home/user/research/fixtures/example-game.pgn', 'utf8');

const settings = {
  locale: 'en_US',
  search: process.env.MODE === 'preset'
    ? { case: 'preset', value: STRENGTH }
    : { case: 'gameReviewSearchSettings', value: { strength: STRENGTH } },
};
if (process.env.FLAGS) settings.enabledFeatureFlags = process.env.FLAGS.split(',');
if (VERSIONS) { settings.moveClassificationVersion = 2; settings.gameAnalysisSpeechVersion = 2; }

const t00 = Date.now();
const ng = await feature(-1, F.NEW_GAME, '.chesscom.explanation_engine.v1.NewGameRequest', {
  newGame: {
    from: {
      case: 'pgnGame',
      value: {
        pgn, takeFirstGameOnly: true,
        metadata: {
          players: [
            { color: 1, ratings: [{ rating: 1016 }], name: '[PUBLIC_PLAYER_HANDLE_REDACTED]' },
            { color: 2, ratings: [{ rating: 1300 }], name: '[PUBLIC_PLAYER_HANDLE_REDACTED]' },
          ],
          // TimeControl "?" -> page builder X4e() drops it; result carried via SetGameResult below
        },
      },
    },
    settings,
  },
});
const root = ng.playedLine[0].gamePoint;
console.log('root', root, 'NewGame took', ((Date.now() - t00) / 1000).toFixed(1) + 's');
try { await feature(root, F.SET_GAME_RESULT, '.chesscom.explanation_engine.v1.SetGameResultRequest', { claimedGameResult: { result: 1, resultType: 1 } }); }
catch (e) { console.error('SetGameResult failed:', e.message); }
try {
  const t0 = Date.now();
  const gr = await feature(root, F.GAME_REVIEW, '.chesscom.explanation_engine.v1.GameReviewRequest', { startingGamePoint: root });
  console.log('GetGameReview took', ((Date.now() - t0) / 1000).toFixed(1) + 's');
  const g = gr.gameReview || {};
  const h = g.highlights || {};
  console.log('accuracy:', JSON.stringify(h.accuracy));
  console.log('reportCard:', JSON.stringify(h.reportCard)?.slice(0, 900));
  console.log('gameSummary:', JSON.stringify(h.gameSummary));
  console.log('takeaways:', JSON.stringify(h.takeaways)?.slice(0, 400));
  const tallies = h.classificationTallies || {};
  console.log('tallies.white:', JSON.stringify(tallies.white));
  console.log('tallies.black:', JSON.stringify(tallies.black));
  const moves = g.review?.playedMoves || [];
  console.log('moves:', moves.length);
  console.log('opening:', JSON.stringify(g.opening));
  console.log('metadata:', JSON.stringify(g.metadata)?.slice(0, 300));
  console.log('result:', JSON.stringify(g.result));
  let withArrows = 0, withSpeechArrows = 0, withHash = 0, sentences = 0;
  const clsList = [];
  for (const m of moves) {
    const pm = m.playedMove || {};
    clsList.push(pm.moveClassification);
    if ((pm.boardMarkings?.arrows || []).length) withArrows++;
    for (const s of pm.speech?.sentences || []) {
      sentences++;
      if (s.audioUrlHash) withHash++;
      for (const f of s.sentenceFragments || []) if (f.arrowsAndSquares) withSpeechArrows++;
    }
  }
  console.log('classifications:', clsList.join(','));
  console.log('moves with boardMarkings arrows:', withArrows, ' speech fragments w/ arrows:', withSpeechArrows);
  console.log('sentences:', sentences, ' with audioUrlHash:', withHash);
  const eg = g.evalGraph?.evalGraphTicks || [];
  console.log('ticks:', eg.length, 'engines:', [...new Set(eg.map(t => t.moveScore?.engine))].join(','), 'depths:', eg.map(t => t.moveScore?.depth).join(','));
  // full per-move dump for classified (non-book) moves
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
