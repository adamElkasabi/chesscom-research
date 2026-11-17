// Offscreen document: hosts the local engines and answers chess.com's
// GameReviewRequest frames with a locally computed GameReviewResponse.
//
// Dials out to the service worker as soon as the module graph is evaluated, so
// the SW never has to guess when we are ready.

import { frame, encodeMessage, decodeMessage } from './lib/protobuf.js';
import { buildGameReview } from './lib/review.js';

const RT = '.chesscom.ceac.v2.GameReviewResponse';

const log = (...a) => { try { console.log('[local-review:engine]', ...a); } catch { /* */ } };
const warn = (...a) => { try { console.warn('[local-review:engine]', ...a); } catch { /* */ } };

const B64_CHUNK = 0x8000;
const b64FromBytes = (bytes) => {
  const u8 = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  let s = '';
  for (let i = 0; i < u8.length; i += B64_CHUNK) s += String.fromCharCode.apply(null, u8.subarray(i, i + B64_CHUNK));
  return btoa(s);
};
const bytesFromB64 = (s) => {
  const bin = atob(s);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
};

const cancelled = new Set();
const queue = [];
let running = false;
let boundPort = null;

const post = (msg) => {
  if (!boundPort) return false;
  try { boundPort.postMessage(msg); return true; } catch { return false; }
};
const out = (session, data) => post({ kind: 'feed', session, data: b64FromBytes(data) });
const status = (session, msg, tone) => post({ kind: 'status', session, msg, tone });
const fail = (session, message) => post({ kind: 'error', session, message });

const progressFrame = (p) =>
  frame(encodeMessage(RT, { result: { case: 'progress', value: { progress: Math.max(0, Math.min(1, p)) } } }));

const failureFrame = () =>
  frame(encodeMessage(RT, {
    result: {
      case: 'failure',
      value: {
        reason: 'GENERAL_ERROR',
        error: { case: 'generalError', value: {} },
      },
    },
  }));

function toBytes(data) {
  if (typeof data === 'string') return bytesFromB64(data);
  if (data instanceof ArrayBuffer) return new Uint8Array(data);
  if (ArrayBuffer.isView(data)) return new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
  throw new Error('unsupported frame payload: ' + Object.prototype.toString.call(data));
}

async function run({ session, data, pgn }) {
  let bytes;
  try {
    bytes = toBytes(data);
  } catch (e) {
    warn('bad request payload', e);
    status(session, 'bad request payload', 'err');
    out(session, failureFrame());
    return;
  }

  status(session, 'request ' + bytes.byteLength + ' B \u2192 starting engine\u2026', 'busy');
  out(session, progressFrame(0));

  let lastAnnounced = -1;
  const announce = (p) => {
    const pct = Math.max(0, Math.min(100, Math.round(p * 100)));
    if (pct === lastAnnounced) return;
    lastAnnounced = pct;
    status(session, 'analysing ' + pct + '%', 'busy');
  };
  announce(0);

  // CEE performs a whole-game review in one feature call; it may not emit
  // intermediate progress. Keep the client alive without inventing progress.
  let currentProgress = 0;
  const keepAlive = setInterval(() => {
    if (!cancelled.has(session)) out(session, progressFrame(currentProgress));
  }, 4000);
  try {
    const res = await buildGameReview({
      requestBytes: bytes,
      pgn: pgn || null,
      onProgress: (p) => {
        currentProgress = p;
        announce(p);
        if (!cancelled.has(session)) out(session, progressFrame(p));
      },
      onLog: (m) => log(m),
    });
    if (cancelled.has(session)) { cancelled.delete(session); status(session, 'cancelled', 'ok'); return; }
    out(session, frame(res.bytes));
    status(session, 'review done \u00b7 ' + res.stats.moves + ' moves, acc ' +
      Number(res.stats.accuracy.white).toFixed(1) + '/' + Number(res.stats.accuracy.black).toFixed(1), 'ok');
    log('review built', res.stats);
  } catch (e) {
    console.error('[local-review] review failed', e);
    status(session, 'failed: ' + String((e && e.message) || e), 'err');
    if (!cancelled.has(session)) out(session, failureFrame());
    fail(session, String((e && e.message) || e));
  } finally {
    clearInterval(keepAlive);
  }
}

async function drain() {
  if (running) return;
  const item = queue.shift();
  if (!item) return;
  running = true;
  try { await run(item); } finally { running = false; drain(); }
}

/* ------------------------------------------------------------ SW binding */

function bindToSW(attempt = 0) {
  let port;
  try {
    port = chrome.runtime.connect({ name: 'engine' });
  } catch (e) {
    warn('connect to service worker failed', e);
    setTimeout(() => bindToSW(attempt + 1), Math.min(5000, 500 * (attempt + 1)));
    return;
  }

  boundPort = port;

  port.onMessage.addListener((msg) => {
    if (!msg) return;
    if (msg.kind === 'frame') {
      queue.push({ session: msg.session, data: msg.data, pgn: msg.pgn });
      log('queued frame from', msg.session, typeof msg.data === 'string' ? (msg.data.length + ' b64 chars') : 'bytes');
      drain();
    } else if (msg.kind === 'socket-close') {
      cancelled.add(msg.session);
      log('socket closed', msg.session);
    } else if (msg.kind === 'socket-open') {
      cancelled.delete(msg.session);
      log('socket open', msg.session);
    }
  });

  port.onDisconnect.addListener(() => {
    if (boundPort === port) boundPort = null;
    const why = chrome.runtime.lastError && chrome.runtime.lastError.message;
    warn('service worker gone' + (why ? ': ' + why : '') + ' - rebinding');
    setTimeout(() => bindToSW(0), 500);
  });

  try { port.postMessage({ kind: 'ready', session: null }); } catch { /* ignore */ }
  log('bound to service worker (attempt ' + attempt + ')');
}

bindToSW();

// Surface module errors instead of dying silently.
window.addEventListener('error', (e) => console.error('[local-review] window error', e.message));
window.addEventListener('unhandledrejection', (e) => console.error('[local-review] unhandled', e.reason));
log('engine host booted, modules loaded');
