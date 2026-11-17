// MAIN-world hook.  Runs at document_start before chess.com's app code.
//
//  1. Forces the client-side entitlement flags that gate Game Review.
//  2. Replaces WebSocket for the CEAC game-review endpoint with an in-page
//     loopback: frames chess.com "sends" are handed to our extension engine,
//     and the engine's frames are fed back as `message` events, so the real
//     decode/dispatch path in shared.eager (C3e -> T3e -> AJe/wJe/pJe/VU/Jp)
//     runs unchanged.
//  3. Shows a small on-page badge so it is always obvious whether the hook is
//     alive and how far the local review has got.
//
// It never talks to a real analysis.chess.com socket.

(() => {
  if (window.__chessLocalReviewInstalled) return;
  window.__chessLocalReviewInstalled = true;

  const CHANNEL = 'chesscom-local-review';
  const VERSION = '0.1.6';
  const toContent = (msg) => { try { window.postMessage({ __clr: CHANNEL, ...msg }, '*'); } catch (e) { console.warn('[local-review] postMessage failed', e); } };
  const safeStr = (x) => { try { return String(x); } catch { return '<unstringifiable>'; } };
  // Child frames re-emit every line into the top frame so a single console
  // shows all of them (Chrome attributes iframe logs to their own frame).
  const forward = (text) => {
    try { if (window.top !== window) window.top.postMessage({ __clr: CHANNEL, kind: 'log', text }, '*'); } catch { /* */ }
  };
  const log = (...a) => {
    try { console.log('[local-review]', ...a); } catch { /* */ }
    forward('[local-review] ' + a.map(safeStr).join(' '));
  };
  const warn = (...a) => {
    try { console.warn('[local-review]', ...a); } catch { /* */ }
    forward('[local-review:warn] ' + a.map(safeStr).join(' '));
  };

  /* ------------------------------------------------------------- badge */

  let badgeEl = null;
  let badgeLabel = null;
  let badgeLine1 = null;
  let lastStatus = { msg: 'hook installed', tone: 'ok' };
  let badgeTimer = null;

  function buildBadge() {
    if (badgeEl && badgeEl.isConnected) return true;
    const host = document.documentElement || document.body;
    if (!host) return false;
    try {
      badgeEl = document.createElement('div');
      badgeEl.setAttribute('data-clr', '1');
      badgeEl.style.cssText = [
        'position:fixed', 'left:8px', 'bottom:8px', 'z-index:2147483647',
        'font:12px/1.45 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace',
        'padding:6px 10px', 'border-radius:8px', 'opacity:.94',
        'pointer-events:none', 'max-width:360px',
        'white-space:nowrap', 'overflow:hidden', 'text-overflow:ellipsis',
        'box-shadow:0 2px 10px rgba(0,0,0,.45)',
      ].join(';');
      badgeLine1 = document.createElement('div');
      badgeLine1.style.cssText = 'font-weight:600;letter-spacing:.2px';
      badgeLabel = document.createElement('div');
      badgeLabel.style.cssText = 'opacity:.85;margin-top:2px';
      badgeEl.appendChild(badgeLine1);
      badgeEl.appendChild(badgeLabel);
      host.appendChild(badgeEl);
      render();
      return true;
    } catch (e) {
      badgeEl = null;
      return false;
    }
  }

  function paintBadge() {
    if (!badgeEl || !badgeEl.isConnected || !badgeLabel) return;
    if (badgeLine1) badgeLine1.textContent = '\u25c8 local review \u00b7 ' + pipeline();
    const tone = lastStatus.tone;
    const fg = tone === 'err' ? '#ffb3b3' : tone === 'busy' ? '#ffe08a' : '#b9ffb9';
    const bg = tone === 'err' ? '#3a1010' : tone === 'busy' ? '#3a2f0c' : '#0e2a12';
    badgeLabel.textContent = '◈ local review · ' + lastStatus.msg;
    badgeEl.style.color = fg;
    badgeEl.style.background = bg;
    badgeEl.style.borderColor = fg;
    badgeEl.style.border = '1px solid ' + fg;
  }

  const STEPS = ['hook', 'ws', 'sock', 'open', 'req', 'eng'];
  const stepState = { hook: false, ws: false, sock: false, open: false, req: false, eng: false };
  function setStep(name) {
    if (!(name in stepState)) return;
    if (stepState[name]) return;
    stepState[name] = true;
    log('step ' + name + ' OK');
    try {
      if (window.top !== window) window.top.postMessage({ __clr: CHANNEL, kind: 'step', name }, '*');
      else render();
    } catch { /* */ }
  }
  function pipeline() {
    return STEPS.map((k) => k + (stepState[k] ? '\u2713' : '\u2717')).join(' ');
  }

  function render() {
    if (window.top !== window) return;
    if (!buildBadge()) return;
    if (badgeLine1) badgeLine1.textContent = '\u25c8 local review \u00b7 ' + pipeline();
    paintBadge();
  }

  function setStatus(msg, tone) {
    lastStatus = { msg: String(msg), tone: tone || 'ok' };
    log(lastStatus.msg);
    if (window.top !== window) return;          // one badge per tab only
    if (buildBadge()) { render(); return; }
    if (!badgeTimer) {
      let n = 0;
      badgeTimer = setInterval(() => {
        if (buildBadge() || ++n > 120) { clearInterval(badgeTimer); badgeTimer = null; }
        else render();
      }, 500);
    }
  }

  /* ---------------------------------------------------------- entitlements */

  const FORCE = new Set([
    'game_review_platinum_report_card',
    'game_review_report_card',
    'game_review_annotated_pgn',
    'web_game_rating_v2',
    'web_game_rating_v2_display_old_rating_tooltip',
    'cee_charm_inference_grv2',
    'analysis_depth_selector',
    'analysis_game_report',
  ]);
  const wanted = (name) =>
    FORCE.has(name) ||
    name.startsWith('game_review') ||
    name.includes('rating_v2') ||
    name.includes('report_card');

  // The review launcher snapshots these values into its reactive permission
  // store at module initialization. In particular, its pre-socket gate is:
  //   !permissions.canCreate && permissions.uiLocked
  // where uiLocked comes from analysis.locked. hasUnlimitedReview alone only
  // affects report-card/upgrade UI; it does NOT let a new review start.
  // Change only local analysis permissions, never account membership or cloud
  // save/library rights. Getters also survive ordinary late quota assignments.
  function forceUnlimited(obj) {
    if (!obj || typeof obj !== 'object') return obj;
    const localPermissions = {
      hasUnlimitedReview: true,
      canCreate: true,
      locked: false,
      canConfigure: true,
      canViewMoveFeedback: true,
      canViewCoachCommentary: true,
      canViewCompleteBasicAnalysis: true,
    };
    for (const [key, value] of Object.entries(localPermissions)) {
      try {
        Object.defineProperty(obj, key, {
          configurable: true, enumerable: true, get: () => value, set: () => {},
        });
      } catch { /* A non-configurable host property cannot be replaced. */ }
    }
    return obj;
  }

  /** Proxy over the *live* array so later pushes by the page still show up. */
  function featuresProxy(raw) {
    const proxy = new Proxy(raw, {
      get(t, p, r) {
        if (p === 'includes') {
          return (name) => (typeof name === 'string' && wanted(name)) ? true : t.includes(name);
        }
        const v = Reflect.get(t, p, r);
        return typeof v === 'function' ? v.bind(t) : v;
      },
    });
    try { Object.defineProperty(proxy, '__clrPatched', { value: true }); } catch { /* */ }
    return proxy;
  }

  function patchChesscom(cc) {
    if (!cc || typeof cc !== 'object' || cc.__clrPatched) return;
    try {
      Object.defineProperty(cc, '__clrPatched', { value: true, configurable: false });
    } catch { /* frozen object — patch it anyway */ }

    // Capture BEFORE installing the accessor: reading cc.analysis afterwards
    // would read our empty backing variable and lose an existing config/PGN.
    let analysis = forceUnlimited(cc.analysis);
    try {
      Object.defineProperty(cc, 'analysis', {
        configurable: true,
        get() { return analysis; },
        set(v) { analysis = forceUnlimited(v); },
      });
    } catch {
      if (cc.analysis) forceUnlimited(cc.analysis);
    }

    try {
      let raw = Array.isArray(cc.features) ? cc.features : [];
      Object.defineProperty(cc, 'features', {
        configurable: true,
        get() { return featuresProxy(raw); },
        set(v) {
          if (Array.isArray(v) && v !== raw && !v.__clrPatched) raw = v;
        },
      });
    } catch { /* leave as-is */ }
  }

  try {
    let current = window.chesscom;
    patchChesscom(current);
    Object.defineProperty(window, 'chesscom', {
      configurable: true,
      get() { return current; },
      set(v) { current = v; patchChesscom(v); },
    });
  } catch { patchChesscom(window.chesscom); /* already non-configurable */ }

  /* ------------------------------------------------- review socket loopback */

  const OrigWS = window.WebSocket;

  /**
   * Identify a CEAC endpoint by *path*, not host: chess.com can point the
   * client at prod, staging, sandbox, or even same-origin
   * (analysis.ceacSocketSameOrigin), and only the path is stable across all
   * of those.  Getting this wrong means `new WebSocket(...)` returns a real
   * socket, it never opens, S3e times out after 10 s and the UI reports
   * "Could not connect to the analysis server."
   */
  function classify(url) {
    let u;
    try { u = new URL(String(url)); } catch { return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other';
    return null;
  }

  function readPgn() {
    try {
      const p = window.chesscom && window.chesscom.analysis && window.chesscom.analysis.pgn;
      return typeof p === 'string' && p ? p : null;   // must be cloneable
    } catch { return null; }
  }

  function FakeReviewSocket(url) {
    // The six WebIDL attributes on the *native* WebSocket.prototype are
    // brand-checked: `url`/`readyState`/`bufferedAmount`/`extensions`/
    // `protocol` are getter-only (sloppy-mode writes silently no-op, so a
    // later *read* throws "Illegal invocation"), and `binaryType` has a real
    // native setter, so a plain `this.binaryType = 'blob'` throws
    // `TypeError: Illegal invocation` the instant a real browser constructs
    // this object (v0.1.3's exact failure — the Node harness has no brand
    // checks, so it passed there).  Own data properties shadow the
    // prototype accessors: reads/writes hit the own property and no native
    // getter/setter ever runs with this non-WebSocket as receiver.
    // MUST be the first statements of the constructor.
    Object.defineProperties(this, {
      url:            { value: String(url), writable: true, enumerable: true, configurable: true },
      readyState:     { value: FakeReviewSocket.CONNECTING, writable: true, enumerable: true, configurable: true },
      bufferedAmount: { value: 0, writable: true, enumerable: true, configurable: true },
      extensions:     { value: '', writable: true, enumerable: true, configurable: true },
      protocol:       { value: '', writable: true, enumerable: true, configurable: true },
      binaryType:     { value: 'blob', writable: true, enumerable: true, configurable: true },
    });
    this._listeners = new Map();

    // Accessor-backed `on*` handlers: chess.com assigns r.onopen immediately
    // AFTER `new WebSocket()` returns.  With a plain property we depend on
    // winning a race against S3e's own timeout timer; with an accessor the
    // handler is invoked the moment it is attached, regardless of ordering,
    // so `open` can never be missed.
    for (const type of ['open', 'message', 'close', 'error']) {
      let handler = null;
      Object.defineProperty(this, 'on' + type, {
        configurable: true, enumerable: true,
        get() { return handler; },
        set(fn) {
          handler = typeof fn === 'function' ? fn : null;
          if (type === 'open' && handler && this.readyState === FakeReviewSocket.OPEN && !this._openFired) {
            this._openFired = true;
            try { handler.call(this, { type: 'open', target: this }); } catch (e) { console.error('[local-review] onopen', e); }
          }
        },
      });
    }
    this._openFired = false;

    toContent({ kind: 'socket-open', url: this.url, pgn: readPgn() });

    const doOpen = () => {
      if (this._openFired || this.readyState !== FakeReviewSocket.CONNECTING) return;
      this._openFired = true;
      this.readyState = FakeReviewSocket.OPEN;
      this._fire('open', { type: 'open', target: this });
      setStep('open');
      setStatus('socket loopback open', 'ok');
    };
    // Microtask first: always drains before any macrotask timer, so S3e's
    // `k3e` timeout can never fire first even if k3e were 0/undefined.
    queueMicrotask(doOpen);
    setTimeout(doOpen, 0);
  }
  FakeReviewSocket.CONNECTING = 0;
  FakeReviewSocket.OPEN = 1;
  FakeReviewSocket.CLOSING = 2;
  FakeReviewSocket.CLOSED = 3;

  FakeReviewSocket.prototype = Object.create(OrigWS && OrigWS.prototype ? OrigWS.prototype : null);
  FakeReviewSocket.prototype.constructor = FakeReviewSocket;

  Object.defineProperties(FakeReviewSocket.prototype, {
    send: {
      value(data) {
        if (this.readyState !== FakeReviewSocket.OPEN) {
          throw new DOMException('InvalidStateError', 'InvalidStateError');
        }
        let bytes = null;
        if (data instanceof ArrayBuffer) bytes = data;
        else if (ArrayBuffer.isView(data)) bytes = data.buffer.slice(data.byteOffset, data.byteOffset + data.byteLength);
        else if (typeof data === 'string') bytes = new TextEncoder().encode(data).buffer;
        if (bytes) {
          setStep('req');
          setStatus('request ' + bytes.byteLength + ' B → analysing…', 'busy');
          toContent({ kind: 'frame', data: bytes, pgn: readPgn() });
        }
      },
    },
    close: {
      value(code = 1000, reason = '') {
        if (this.readyState === FakeReviewSocket.CLOSED) return;
        const neverOpened = this.readyState === FakeReviewSocket.CONNECTING;
        this.readyState = FakeReviewSocket.CLOSED;
        sockets.delete(this);
        if (activeSocket === this) activeSocket = null;
        toContent({ kind: 'socket-close' });
        if (neverOpened) {
          // S3e's k3e timer called close() before our `open` ran -> that is
          // exactly what produces the "Could not connect" toaster.
          console.error('[local-review] socket CLOSED BEFORE OPEN - S3e timeout won the race', new Error('stack'));
          setStatus('closed before open (S3e timeout race)', 'err');
          return;
        }
        setStatus('socket closed (' + code + ')', 'ok');
        this._fire('close', { type: 'close', target: this, code, reason, wasClean: code === 1000 });
      },
    },
    addEventListener: {
      value(type, fn) {
        if (typeof fn !== 'function') return;
        if (!this._listeners.has(type)) this._listeners.set(type, []);
        this._listeners.get(type).push(fn);
      },
    },
    removeEventListener: {
      value(type, fn) {
        const l = this._listeners.get(type);
        if (!l) return;
        const i = l.indexOf(fn);
        if (i >= 0) l.splice(i, 1);
      },
    },
    dispatchEvent: {
      value(ev) { this._fire(ev && ev.type, ev); return true; },
    },
  });

  FakeReviewSocket.prototype._fire = function (type, ev) {
    if (!type) return;
    const handler = this['on' + type];
    if (typeof handler === 'function') {
      try { handler.call(this, ev); } catch (e) { console.error('[local-review] handler', e); }
    }
    const l = this._listeners.get(type);
    if (l) for (const fn of l.slice()) { try { fn.call(this, ev); } catch (e) { console.error(e); } }
  };

  /** Deliver a frame from the extension engine to chess.com's C3e dispatcher. */
  FakeReviewSocket.prototype.feed = function (bytes) {
    if (this.readyState !== FakeReviewSocket.OPEN) return;
    const ab = bytes instanceof ArrayBuffer
      ? bytes
      : bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
    this._fire('message', { type: 'message', data: ab, target: this, origin: '', lastEventId: '' });
  };

  /* --------------------------------------------------- page <-> extension */

  const sockets = new Set();
  let activeSocket = null;   // the socket the engine should answer

  function HookedWS(url, protocols) {
    const u = safeStr(url);          // FIRST line: proves this hook ran at all
    log('WS ←', u, 'protocols=' + safeStr(protocols));
    try {
      const kind = classify(u);
      if (kind === 'review') {
        const s = new FakeReviewSocket(u);
        sockets.add(s);
        activeSocket = s;
        setStep('sock');
        log('intercepted game-review socket →', u);
        return s;
      }
      const s = protocols === undefined ? new OrigWS(u) : new OrigWS(u, protocols);
      log('WS passthrough [' + (kind || 'other') + '] →', u);
      return s;
    } catch (e) {
      console.error('[local-review] HookedWS FAILED for', u, e);
      setStatus('WS hook error: ' + ((e && e.message) || e), 'err');
      throw e;
    }
  }
  HookedWS.prototype = OrigWS.prototype;
  HookedWS.prototype.constructor = OrigWS;
  for (const k of ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED']) HookedWS[k] = OrigWS[k];

  function installHook() {
    try {
      if (window.WebSocket !== HookedWS) {
        // writable:false so a later `window.WebSocket = x` cannot undo us.
        Object.defineProperty(window, 'WebSocket', { configurable: true, writable: false, value: HookedWS });
        log('WebSocket hook installed');
      }
    } catch (e) {
      console.error('[local-review] cannot patch WebSocket', e);
      return;
    }
    if (window.WebSocket === HookedWS) {
      setStep('ws');
    } else {
      console.error('[local-review] WebSocket patch did NOT take:', safeStr(window.WebSocket));
    }
  }
  installHook();

  // Chess.com (or a polyfill) may reassign window.WebSocket later — keep ours.
  setInterval(() => {
    installHook();
    try { patchChesscom(window.chesscom); } catch { /* */ }
  }, 500);

  window.addEventListener('message', (ev) => {
    if (ev.source !== window) return;
    const d = ev.data;
    if (!d || d.__clr !== CHANNEL) return;
    if (d.kind === 'feed') {
      const target = activeSocket || Array.from(sockets).pop();
      if (target) {
        target.feed(d.data instanceof ArrayBuffer ? new Uint8Array(d.data) : d.data);
      } else {
        warn('engine frame arrived with no open socket');
      }
    } else if (d.kind === 'log') {
      if (window.top === window) { try { console.log(d.text); } catch { /* */ } }
    } else if (d.kind === 'step') {
      if (window.top === window) setStep(d.name);
    } else if (d.kind === 'status') {
      if (/engine host/i.test(String(d.msg))) setStep('eng');
      lastStatus = { msg: String(d.msg), tone: d.tone || 'ok' };
      if (window.top === window) { if (buildBadge()) paintBadge(); }
    } else if (d.kind === 'shutdown') {
      for (const s of sockets) { try { s.close(1001, 'ext'); } catch { /* */ } }
      sockets.clear();
    }
  });

  window.addEventListener('load', () => {
    try { patchChesscom(window.chesscom); } catch { /* */ }
    installHook();
  });

  window.__chessLocalReview = {
    force() { try { patchChesscom(window.chesscom); } catch { /* */ } installHook(); },
    get sockets() { return sockets; },
    get status() { return lastStatus; },
    version: VERSION,
  };

  setStep('hook');
  setStatus('hook installed v' + VERSION, 'ok');
})();
