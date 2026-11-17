// MV3 service worker: makes sure the offscreen engine host exists and routes
// frames between content scripts and it.
//
// The offscreen document DIALS OUT to us (name 'engine') once its module graph
// — including the 910 KB descriptors.js — has finished evaluating.  We never
// dial in: connecting to a document whose chrome.runtime.onConnect listener is
// not registered yet silently loses the port, and every later frame would go
// nowhere with no error.

const OFFSCREEN_URL = 'offscreen.html';
const log = (...a) => { try { console.log('[local-review:sw]', ...a); } catch { /* */ } };
const warn = (...a) => { try { console.warn('[local-review:sw]', ...a); } catch { /* */ } };

const ENGINE_BIND_TIMEOUT_MS = 15000;

let offscreenPort = null;
let engineBound = null;          // resolver for the in-flight ensureEngine() wait
let engineReadyPromise = null;
const pendingToEngine = [];      // frames waiting for the engine host
const contentPorts = new Map();  // session -> port

async function hasOffscreen() {
  if (!chrome.offscreen || !chrome.offscreen.getAllDocuments) return false;
  const docs = await chrome.offscreen.getAllDocuments();
  return docs.some((d) => d.url === OFFSCREEN_URL);
}

function broadcast(msg) {
  for (const [, p] of contentPorts) { try { p.postMessage(msg); } catch { /* tab gone */ } }
}

function attachEnginePort(port) {
  offscreenPort = port;
  log('engine host bound');

  port.onMessage.addListener((msg) => {
    if (!msg) return;
    if (msg.kind === 'ready') { broadcast({ kind: 'status', msg: 'engine host bound', tone: 'ok' }); return; }
    if (!msg.session) return;
    const p = contentPorts.get(msg.session);
    if (p) { try { p.postMessage(msg); } catch { /* tab gone */ } }
  });

  port.onDisconnect.addListener(() => {
    if (offscreenPort === port) offscreenPort = null;
    engineReadyPromise = null;
    warn('engine host disconnected');
    broadcast({ kind: 'status', msg: 'engine host disconnected', tone: 'err' });
  });

  for (const m of pendingToEngine.splice(0)) { try { port.postMessage(m); } catch { pendingToEngine.push(m); } }

  if (engineBound) { const f = engineBound; engineBound = null; f(); }
}

function deliver(msg) {
  if (offscreenPort) {
    try { offscreenPort.postMessage(msg); return; } catch { offscreenPort = null; }
  }
  pendingToEngine.push(msg);
}

/** Resolves once the offscreen document has created its 'engine' port. */
function ensureEngine(timeoutMs = ENGINE_BIND_TIMEOUT_MS) {
  if (offscreenPort) return Promise.resolve();
  if (engineReadyPromise) return engineReadyPromise;

  const wait = new Promise((resolve, reject) => {
    if (offscreenPort) { resolve(); return; }
    const timer = setTimeout(() => {
      engineBound = null;
      reject(new Error('engine host did not bind within ' + timeoutMs + 'ms'));
    }, timeoutMs);
    engineBound = () => { clearTimeout(timer); resolve(); };
  });

  engineReadyPromise = (async () => {
    try {
      if (!(await hasOffscreen())) {
        await chrome.offscreen.createDocument({
          url: OFFSCREEN_URL,
          reasons: ['WORKERS'],
          justification: 'Run the local chess engines that produce the game review',
        });
        log('offscreen document created');
      }
    } catch (e) {
      if (!String(e).includes('Only a single offscreen')) warn('offscreen create failed', e);
    }
    await wait;   // the document binds back to us when its modules are ready
  })().catch((e) => { engineReadyPromise = null; throw e; });

  return engineReadyPromise;
}

chrome.runtime.onConnect.addListener((port) => {
  const name = port.name || '';

  if (name === 'engine') { attachEnginePort(port); return; }
  if (!name.startsWith('review:')) return;

  const session = name.slice('review:'.length);
  contentPorts.set(session, port);
  log('content script attached', session);
  port.onDisconnect.addListener(() => { contentPorts.delete(session); log('content script detached', session); });

  port.onMessage.addListener((msg) => {
    if (!msg) return;
    if (msg.kind === 'frame' || msg.kind === 'socket-close' || msg.kind === 'socket-open') {
      ensureEngine()
        .then(() => deliver(msg))
        .catch((e) => {
          warn(e);
          broadcast({ kind: 'status', msg: 'engine host failed: ' + e.message, tone: 'err' });
          try { port.postMessage({ kind: 'error', session, message: String(e.message || e) }); } catch { /* */ }
        });
    }
  });

  try { port.postMessage({ kind: 'status', msg: 'extension connected', tone: 'ok' }); } catch { /* ignore */ }
});
