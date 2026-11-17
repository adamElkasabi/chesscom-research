// Regression: a NEW, uncached game must reach the LOCAL review socket even
// with exhausted quota. Run: node test/quota-test.mjs
// Runs the real hook in isolated page worlds, then uses the permission
// bootstrap and pre-socket gate extracted from the saved chess.com bundle.
import assert from 'node:assert/strict';
import vm from 'node:vm';
import fs from 'node:fs';

const hook = fs.readFileSync(new URL('../page-hook.js', import.meta.url), 'utf8');
const bundle = fs.readFileSync(new URL('../../research/shared.eager.BOGLllgUUR.chunk.js', import.meta.url), 'utf8');
const bootstrap = bundle.match(/\(\{analysis:fq\}=window\.chesscom\),pq=A\(\{canAddToLibrary:[\s\S]*?uiLocked:!!fq\.locked\}\)/)?.[0];
const gate = bundle.match(/function TZ\(\)\{return!pq\.canCreate&&pq\.uiLocked\}/)?.[0];
assert.ok(bootstrap && gate, 'reference page permission bootstrap/gate found');

function exhausted() {
  return { hasUnlimitedReview: false, canCreate: false, locked: true,
    canConfigure: false, canViewMoveFeedback: false, canViewCoachCommentary: false,
    canViewCompleteBasicAnalysis: false, canBookmark: false, libraryLocked: true,
    pgn: '1. e4 e5 *', userDetails: { white: { name: 'A' }, black: { name: 'B' } } };
}
function world(initial) {
  const messages = [];
  function NativeWS() { throw new Error('Unexpected REAL network connection'); }
  Object.assign(NativeWS, { CONNECTING: 0, OPEN: 1, CLOSING: 2, CLOSED: 3 });
  const c = vm.createContext({
    console: { log() {}, warn() {}, error() {} }, URL, TextEncoder,
    ArrayBuffer, Uint8Array, Map, Set, WeakMap, DOMException,
    WebSocket: NativeWS, chesscom: initial,
    document: { documentElement: null, body: null },
    postMessage(m) { messages.push(m); }, addEventListener() {},
    queueMicrotask, setTimeout, setInterval() { return 1; }, clearInterval() {},
  });
  vm.runInContext('window=globalThis; top=window;', c);
  vm.runInContext(hook, c);
  return { c, messages };
}
function snapshot(c) {
  vm.runInContext(`var fq,pq; var A=x=>x; ${bootstrap}; ${gate}`, c);
  return vm.runInContext('({ blocked:TZ(), ...pq })', c);
}

// Control: the unmodified page DOES block exhausted accounts.
const control = vm.createContext({ window: { chesscom: { analysis: exhausted() } } });
assert.equal(snapshot(control).blocked, true);
console.log('PASS control: original page blocks a fresh review with exhausted quota');

for (const timing of ['preexisting config', 'late chesscom assignment', 'late analysis assignment', 'replaced analysis', 'replaced chesscom']) {
  const original = exhausted();
  const initial = timing === 'preexisting config' ? { analysis: original, features: ['keep-me'] } : undefined;
  const { c, messages } = world(initial);
  if (!initial) c.chesscom = { features: ['keep-me'] };
  if (!initial) c.chesscom.analysis = original;
  if (timing === 'replaced analysis') c.chesscom.analysis = exhausted();
  if (timing === 'replaced chesscom') c.chesscom = { analysis: exhausted(), features: ['keep-me'] };
  const config = c.chesscom.analysis;
  assert.equal(config.pgn, original.pgn, 'PGN survives patching');
  assert.equal(config.userDetails.white.name, 'A', 'player metadata survives patching');
  assert.equal(c.chesscom.features.includes('keep-me'), true);
  Object.assign(config, { locked: true, canCreate: false, hasUnlimitedReview: false });
  const permissions = snapshot(c);
  assert.equal(permissions.blocked, false, timing);
  assert.equal(permissions.canViewCoachCommentary, true);
  assert.equal(permissions.canViewMoveFeedback, true);
  assert.equal(permissions.canAddToLibrary, false, 'no cloud library permissions forged');
  assert.equal(permissions.canSaveLibraryGames, false);
  // Reproduce the key launch condition with NO cached analysis; only use the
  // fake socket if the actual page gate allows the request.
  vm.runInContext(`
    var cachedAnalysis = null;
    if (!cachedAnalysis && !TZ()) {
      var socket = new WebSocket('wss://analysis.chess.com/v2/game-review');
      socket.onopen = () => socket.send(new Uint8Array([10, 0]).buffer);
    }
  `, c);
  await new Promise(resolve => setTimeout(resolve, 5));
  assert.ok(messages.some(m => m.kind === 'frame'), 'fresh request reaches local engine bridge');
  assert.equal(messages.find(m => m.kind === 'frame').pgn, original.pgn);
  vm.runInContext('socket.close()', c);
  console.log(`PASS ${timing}: exhausted quota + no cache reaches LOCAL review`);
}
console.log('ALL PASS');
