// Isolated-world content script: relays frames between the MAIN-world hook
// and the extension's engine host (service worker -> offscreen document).
//
// chrome.runtime Port messages are JSON-serialised, so an ArrayBuffer would
// silently arrive on the other side as `{}`.  Everything binary therefore
// crosses the port as base64 and is turned back into bytes on each side.

const CHANNEL = 'chesscom-local-review';
const SESSION = 's' + Math.random().toString(36).slice(2, 10);

const log = (...a) => { try { console.log('[local-review:bridge]', ...a); } catch { /* */ } };
const warn = (...a) => { try { console.warn('[local-review:bridge]', ...a); } catch { /* */ } };

const B64_CHUNK = 0x8000;
function b64FromBytes(bytes) {
  const u8 = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  let s = '';
  for (let i = 0; i < u8.length; i += B64_CHUNK) {
    s += String.fromCharCode.apply(null, u8.subarray(i, i + B64_CHUNK));
  }
  return btoa(s);
}
function bytesFromB64(s) {
  const bin = atob(s);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}
function toPage(msg) {
  try { window.postMessage({ __clr: CHANNEL, ...msg }, '*'); } catch (e) { warn('page postMessage failed', e); }
}

let port = null;
let connected = false;
const pending = [];

function connect() {
  try {
    port = chrome.runtime.connect({ name: 'review:' + SESSION });
    port.onMessage.addListener((msg) => {
      if (!msg) return;
      if (msg.kind === 'feed') {
        let bytes;
        try {
          bytes = typeof msg.data === 'string' ? bytesFromB64(msg.data) : new Uint8Array(msg.data || []);
        } catch (e) {
          warn('bad engine frame', e);
          return;
        }
        toPage({ kind: 'feed', data: bytes.buffer });
      } else if (msg.kind === 'status') {
        toPage({ kind: 'status', msg: msg.msg, tone: msg.tone });
      } else if (msg.kind === 'error') {
        warn('engine error:', msg.message);
        toPage({ kind: 'status', msg: 'engine error: ' + msg.message, tone: 'err' });
      } else if (msg.kind === 'ready') {
        if (!connected) log('engine host ready');
        connected = true;
        toPage({ kind: 'status', msg: 'engine host ready', tone: 'ok' });
      }
    });
    port.onDisconnect.addListener(() => {
      port = null;
      connected = false;
      const why = chrome.runtime.lastError && chrome.runtime.lastError.message;
      warn('port disconnected' + (why ? ': ' + why : ''), '- retrying');
      setTimeout(connect, 500);
    });
    for (const m of pending.splice(0)) { try { port.postMessage(m); } catch { pending.push(m); } }
  } catch (e) {
    warn('connect failed', e);
    setTimeout(connect, 1000);
  }
}
connect();

window.addEventListener('message', (ev) => {
  if (ev.source !== window) return;
  const d = ev.data;
  if (!d || d.__clr !== CHANNEL) return;

  if (d.kind === 'frame') {
    let b64;
    try { b64 = b64FromBytes(d.data); } catch (e) { warn('cannot encode frame', e); return; }
    push({ kind: 'frame', session: SESSION, data: b64, pgn: typeof d.pgn === 'string' ? d.pgn : null });
  } else if (d.kind === 'socket-open' || d.kind === 'socket-close') {
    push({ kind: d.kind, session: SESSION, url: d.url || null, pgn: typeof d.pgn === 'string' ? d.pgn : null });
  }
});

function push(msg) {
  if (port) { try { port.postMessage(msg); return; } catch { /* reconnecting */ } }
  pending.push(msg);
}

// Keep the MV3 service worker awake while a tab is open: without traffic
// Chrome terminates it and the port drops (we kept seeing "port disconnected").
setInterval(() => { push({ kind: 'ping', session: SESSION }); }, 20000);
