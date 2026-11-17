// Brand-checking regression harness for extension/page-hook.js.
//
// WHY THIS EXISTS: v0.1.3 passed the old harness but threw
// `TypeError: Illegal invocation` in real Chrome. FakeReviewSocket inherits
// the native WebSocket.prototype, whose WebIDL accessors are brand-checked:
// assigning `this.binaryType = 'blob'` invoked the NATIVE setter with a
// non-WebSocket receiver and killed the constructor (-> S3e rejects ->
// "Could not connect to the analysis server.", badge sock✗ eng✗).
// The old harness's fake WebSocket used plain data properties, so it had no
// brand checks and could never catch this class of bug.
//
// This harness models Chrome faithfully: every native accessor/method on
// NativeWS.prototype throws `TypeError: Illegal invocation` unless the
// receiver is a branded NativeWS instance. A `model validation` step proves
// the teeth exist (bare object + .binaryType= must throw), then the real
// page-hook.js must survive the full S3e/C3e flow without one.

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const PAGE_HOOK = join(here, '..', 'page-hook.js');   // extension/test/ -> extension/

/* ------------------------------------------------------------ page world */

const captured = [];                 // outbound window.postMessage (toContent)
const pageListeners = new Map();     // inbound 'message' listeners
const logs = [];                     // console.log/warn/error lines

globalThis.window = globalThis;
globalThis.top = globalThis;
let debugDomCreations = 0;
globalThis.document = {
  documentElement: { appendChild() {} },
  body: null,
  createElement: () => { debugDomCreations++; return { style: {}, setAttribute() {}, appendChild() {} }; },
};
globalThis.postMessage = (m) => { captured.push(m); };
globalThis.addEventListener = (t, f) => {
  if (!pageListeners.has(t)) pageListeners.set(t, []);
  pageListeners.get(t).push(f);
};

const origLog = console.log;
for (const m of ['log', 'warn', 'error']) {
  console[m] = (...a) => {
    logs.push(a.map((x) => { try { return typeof x === 'string' ? x : (x && x.message) || String(x); } catch { return '?'; } }).join(' '));
    origLog.apply(console, m === 'log' ? a : [`[${m}]`, ...a]);
  };
}

/* ------------------------------------- brand-checked native WebSocket model */

const branded = new WeakSet();
const brand = (o) => { if (!branded.has(o)) throw new TypeError('Illegal invocation'); };

function NativeWS(url, protocols) {
  branded.add(this);
  this._url = String(url);
  this._protocols = protocols;
  this._rs = NativeWS.CONNECTING;     // readyState — brand-checked getter
  this._bt = 'blob';                  // binaryType — brand-checked get/set
  this._on = Object.create(null);
}
NativeWS.CONNECTING = 0;
NativeWS.OPEN = 1;
NativeWS.CLOSING = 2;
NativeWS.CLOSED = 3;

const ev = (name) => ({
  get() { brand(this); return this._on[name] || null; },
  set(v) { brand(this); this._on[name] = typeof v === 'function' ? v : null; },
  enumerable: true, configurable: true,
});

Object.defineProperties(NativeWS.prototype, {
  // --- the six WebIDL attributes, exactly as Chrome has them ---
  url:            { get() { brand(this); return this._url; }, enumerable: true, configurable: true },
  readyState:     { get() { brand(this); return this._rs; }, enumerable: true, configurable: true },
  bufferedAmount: { get() { brand(this); return 0; }, enumerable: true, configurable: true },
  extensions:     { get() { brand(this); return ''; }, enumerable: true, configurable: true },
  protocol:       { get() { brand(this); return ''; }, enumerable: true, configurable: true },
  binaryType:     { get() { brand(this); return this._bt; }, set(v) { brand(this); this._bt = v; }, enumerable: true, configurable: true },
  // --- event handler IDL attributes (also interface attributes -> branded) ---
  onopen: ev('open'), onclose: ev('close'), onerror: ev('error'), onmessage: ev('message'),
  // --- methods ---
  send:      { value() { brand(this); }, enumerable: true, configurable: true, writable: true },
  close:     { value() { brand(this); }, enumerable: true, configurable: true, writable: true },
  addEventListener:    { value() { brand(this); }, enumerable: true, configurable: true, writable: true },
  removeEventListener: { value() { brand(this); }, enumerable: true, configurable: true, writable: true },
  dispatchEvent:       { value() { brand(this); return true; }, enumerable: true, configurable: true, writable: true },
});

globalThis.WebSocket = NativeWS;

/* --------------------------------------------------- model validation */

let teeth = false;
try {
  const bare = Object.create(NativeWS.prototype);
  bare.binaryType = 'arraybuffer';          // must throw — this is v0.1.3's bug
} catch (e) {
  teeth = e instanceof TypeError && /Illegal invocation/.test(e.message);
}
if (!teeth) { origLog('FATAL: brand-check model has no teeth — harness cannot catch Illegal invocation'); process.exit(1); }
origLog('model validation OK: bare object .binaryType= throws Illegal invocation');

/* ------------------------------------------------------- load page-hook */

(0, eval)(readFileSync(PAGE_HOOK, 'utf8'));
const loadLogs = logs.slice();   // load-time lines (hook/ws steps, version banner)

/* ------------------------------------------------------------ utilities */

const fail = [];
const ok = (cond, msg) => { if (cond) origLog('  PASS ' + msg); else { fail.push(msg); origLog('  FAIL ' + msg); } };
const saw = (re) => logs.some((l) => re.test(l));
const drain = (ms = 25) => new Promise((r) => setTimeout(r, ms));

function deliverToPage(data) {           // inbound window message (bridge -> page)
  for (const f of pageListeners.get('message') || []) f({ source: globalThis, data });
}

/* ---------------------------------------------- 1. review socket (S3e) */

origLog('\n=== review socket: wss://analysis.chess.com:443/v2/game-review ===');
captured.length = 0; logs.length = 0;

let s = null, ctorThrew = null;
try { s = new globalThis.WebSocket('wss://analysis.chess.com:443/v2/game-review'); }
catch (e) { ctorThrew = e; }

ok(!ctorThrew, 'constructor did not throw' + (ctorThrew ? ' — ' + ctorThrew.message : ''));
ok(!!s, 'a socket object was returned');
if (s) {
  ok(!branded.has(s), 'intercepted socket is the fake (not a real NativeWS)');
  ok(s instanceof globalThis.WebSocket, 'fake still satisfies instanceof WebSocket');
  ok(captured.some((m) => m.kind === 'socket-open'), 'socket-open posted to bridge (drives eng step)');

  // S3e does this immediately after `new WebSocket()`:
  let btThrew = null;
  try { s.binaryType = 'arraybuffer'; } catch (e) { btThrew = e; }
  ok(!btThrew && s.binaryType === 'arraybuffer', "S3e's binaryType='arraybuffer' assignment works");
  ok(s.readyState === 0, 'readyState readable === CONNECTING before open');
  ok(s.url === 'wss://analysis.chess.com:443/v2/game-review', 'url readable');

  // S3e's connect promise: onopen resolves, k3e timer rejects, onerror rejects
  let opened = false, openErr = null;
  const p = new Promise((res, rej) => {
    const t = setTimeout(() => { s.readyState !== globalThis.WebSocket.OPEN && (s.close(), rej(new Error('TIMEOUT'))); }, 10000);
    s.onopen = () => { clearTimeout(t); opened = true; res(s); };
    s.onerror = () => { clearTimeout(t); rej(new Error('FAILED')); };
  });
  p.catch((e) => { openErr = e.message; });
  await drain();
  ok(opened && !openErr, 'S3e resolved: onopen fired (microtask beat k3e timer)');
  ok(s.readyState === 1, 'readyState === OPEN after open');

  // chess.com sends the request (C3e -> T3e frame)
  let got = null;
  s.onmessage = (ev2) => { got = ev2.data; };
  let sendThrew = null;
  try { s.send(new Uint8Array([10, 5, 1, 2, 3, 4, 5]).buffer); } catch (e) { sendThrew = e; }
  ok(!sendThrew, 'send() did not throw');
  ok(captured.some((m) => m.kind === 'frame'), 'request frame posted to bridge');

  // engine response: bridge -> page 'feed' -> socket onmessage
  deliverToPage({ __clr: 'chesscom-local-review', kind: 'feed', data: new Uint8Array([9, 9, 9]).buffer });
  await drain(10);
  ok(got instanceof ArrayBuffer && got.byteLength === 3, 'engine frame reached socket.onmessage as ArrayBuffer');

  // teardown
  s.close();
  ok(s.readyState === 3, 'readyState === CLOSED after close()');
  ok(captured.some((m) => m.kind === 'socket-close'), 'socket-close posted to bridge');
}

/* --------------------------------------------- 2. second review attempt */

origLog('\n=== review socket retry (chess.com re-runs S3e on failure) ===');
captured.length = 0;
let s2 = null, ctor2Threw = null;
try { s2 = new globalThis.WebSocket('wss://www.chess.com/v2/game-review'); } catch (e) { ctor2Threw = e; }
ok(!ctor2Threw && !!s2, 'same-origin review URL also intercepted without throwing');
ok(captured.some((m) => m.kind === 'socket-open'), 'socket-open posted for retry');
if (s2) { await drain(); try { s2.close(); } catch { /* */ } }   // drain so open fires first

/* ------------------------------------------------ 3. passthrough socket */

origLog('\n=== passthrough: wss://www.chess.com/pubsub?uid=x ===');
captured.length = 0;
let real = null, realThrew = null;
try { real = new globalThis.WebSocket('wss://www.chess.com/pubsub?uid=x'); } catch (e) { realThrew = e; }
ok(!realThrew, 'passthrough constructor did not throw');
ok(!!real && branded.has(real), 'non-CEAC URL returns a real branded NativeWS');
ok(!captured.some((m) => m.kind === 'socket-open'), 'no socket-open for passthrough');
ok(saw(/WS passthrough \[other\]/), 'passthrough logged');
if (real) {
  let rsend = null;
  try { real.send('x'); rsend = true; } catch (e) { rsend = e.message; }
  ok(rsend === true, 'real socket send() works (brand intact)');
}

/* --------------------------------------------------- 4. no leaks / steps */

origLog('\n=== diagnostics ===');
ok(!saw(/HookedWS FAILED/), 'no HookedWS FAILED logged');
ok(!saw(/Illegal invocation/), 'no Illegal invocation anywhere in page-hook output');
ok(loadLogs.some((l) => /step hook OK/.test(l)) && loadLogs.some((l) => /step ws OK/.test(l)), 'hook + ws steps set');
ok(saw(/step sock OK/) && saw(/step open OK/) && saw(/step req OK/), 'sock + open + req steps set');
ok(loadLogs.some((l) => /hook installed v0\.1\.6/.test(l)), 'page-hook reports v0.1.6');

ok(debugDomCreations === 0, 'hidden debug card never creates DOM elements; console diagnostics remain active');

/* ----------------------------------------------------------------- done */

origLog(fail.length === 0 ? '\nALL PASS' : `\n${fail.length} FAILURE(S):\n - ` + fail.join('\n - '));
process.exit(fail.length === 0 ? 0 : 1);
