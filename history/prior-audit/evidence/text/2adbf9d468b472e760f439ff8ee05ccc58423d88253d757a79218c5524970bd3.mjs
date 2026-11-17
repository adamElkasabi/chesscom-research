// Real headless Chromium extension origin + native Worker + bundled wasm.
// Requires: npm install --no-save playwright && npx playwright install chromium
import { chromium } from 'playwright';
import fs from 'node:fs';
import assert from 'node:assert/strict';
import { encodeMessage, decodeMessage } from '../lib/protobuf.js';
import { fileURLToPath } from 'node:url';
const extension = fileURLToPath(new URL('../', import.meta.url));
const context = await chromium.launchPersistentContext('', {
  channel: 'chromium', headless: true,
  args: ['--no-sandbox', `--disable-extensions-except=${extension}`, `--load-extension=${extension}`],
});
try {
  const sw = context.serviceWorkers()[0] || await context.waitForEvent('serviceworker', { timeout: 20000 });
  const swUrl = new URL(sw.url());
  const origin = swUrl.protocol + '//' + swUrl.host;
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', message => {
    if (message.type() === 'error') errors.push(message.text());
  });
  await page.goto(origin + '/offscreen.html');
  const pgn = fs.readFileSync(new URL('../../research/fixtures/doting-prospect.pgn', import.meta.url), 'utf8');
  const result = await page.evaluate(async pgn => {
    const { buildGameReview } = await import('./lib/review.js');
    const { encodeMessage, decodeMessage } = await import('./lib/protobuf.js');
    const logs = [];
    const request = {
      newGameReq: { newGame: { from: { case: 'pgnGame', value: { pgn, takeFirstGameOnly: true,
        metadata: { players: [ { color: 1, name: '[PUBLIC_PLAYER_HANDLE_REDACTED]', ratings: [{ rating: 100 }] },
          { color: 2, name: '[PUBLIC_PLAYER_HANDLE_REDACTED]', ratings: [{ rating: 333 }] } ], result: { result: 2, resultType: 1 },
          timeControl: { control: { case: 'base', value: { baseMs: 600000n, incrementMs: 0n } } },
          isRated: true, chesscomMetadata: { legacyGameId: 186934806892n, gameSource: 2 } },
      } }, settings: { userColor: 2, enableSkills: true } } },
      runSearchReq: { search: { case: 'gameReviewSearchSettings', value: { strength: 1 } } }, engine: 12,
    };
    const built = await buildGameReview({ requestBytes: encodeMessage('.chesscom.ceac.v2.GameReviewRequest', request), onLog: line => logs.push(line) });
    const decoded = decodeMessage('.chesscom.ceac.v2.GameReviewResponse', built.bytes);
    return { stats: built.stats, resultCase: decoded.result.case, logs };
  }, pgn);
  assert.equal(result.resultCase, 'success');
  assert.equal(result.stats.moves, 20);
  assert.ok(result.stats.audioHashes > 0);
  assert.deepEqual(result.stats.actualEngines, [11]);
  assert.deepEqual(errors, [], 'no page/module/worker errors');
  fs.writeFileSync(new URL('../../research/browser-cee-test.json', import.meta.url), JSON.stringify({ ...result, errors }, null, 2));
  console.log(JSON.stringify(result, null, 2));
  console.log('PASS REAL CHROMIUM: extension origin + native CEE Worker + wasm');

  // Close the ordinary extension tab. The next request must create and use
  // the actual MV3 offscreen document via bridge -> service worker.
  await page.close();
  await context.route('https://www.chess.com/**', route => route.fulfill({
    status: 200, contentType: 'text/html',
    body: '<!doctype html><title>Fresh uncached game / quota exhausted</title><script>window.chesscom={features:[],analysis:{canCreate:false,locked:true,hasUnlimitedReview:false,pgn:' + JSON.stringify(pgn) + '}};</script>',
  }));
  const gamePage = await context.newPage();
  let socketResult;
  const statuses = [];
  await gamePage.exposeFunction('acceptResponse', array => {
    const decoded = decodeMessage('.chesscom.ceac.v2.GameReviewResponse', Uint8Array.from(array));
    if (decoded.result?.case === 'failure') throw new Error('Local review returned failure');
    if (decoded.result?.case !== 'success') return false;
    socketResult = decoded.result.value.gameReview;
    return true;
  });
  gamePage.on('console', message => { if (/local-review/.test(message.text())) statuses.push(message.text()); });
  await gamePage.goto('https://www.chess.com/analysis/game/live/186934806892/review');
  const requestBytes = encodeMessage('.chesscom.ceac.v2.GameReviewRequest', {
    newGameReq: { newGame: { from: { case: 'pgnGame', value: { pgn, takeFirstGameOnly: true } }, settings: { userColor: 2 } } },
    runSearchReq: { search: { case: 'gameReviewSearchSettings', value: { strength: 1 } } }, engine: 12,
  });
  const socketCheck = await gamePage.evaluate(async array => {
    if (!window.chesscom.analysis.canCreate || window.chesscom.analysis.locked) throw new Error('Quota fix regressed');
    return await new Promise((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error('Socket round trip timeout')), 90000);
      const socket = new WebSocket('wss://analysis.chess.com/v2/game-review');
      socket.onopen = () => socket.send(Uint8Array.from(array).buffer);
      socket.onerror = () => reject(new Error('Local socket error'));
      socket.onmessage = async event => {
        try {
          if (await window.acceptResponse(Array.from(new Uint8Array(event.data)))) {
            clearTimeout(timer); socket.close(); resolve(true);
          }
        } catch (error) { clearTimeout(timer); reject(error); }
      };
    });
  }, Array.from(requestBytes));
  assert.equal(socketCheck, true);
  assert.equal(socketResult.review.playedMoves.length, 20);
  assert.ok(statuses.some(line => line.includes('intercepted game-review socket')), 'request was intercepted locally');
  fs.writeFileSync(new URL('../../research/browser-pipeline-test.json', import.meta.url), JSON.stringify({
    quotaExhausted: true, cachedReview: false, moves: socketResult.review.playedMoves.length,
    accuracy: socketResult.highlights.accuracy, statuses,
  }, null, 2));
  console.log('PASS FULL CHROMIUM PIPELINE: exhausted quota + fresh game -> hook -> bridge -> service worker -> offscreen CEE -> success');
} finally { await context.close(); }
