# extension — findings 1–14

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18943"></a>
## FND-18943: Main-world hook and isolated bridge have distinct responsibilities

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Manifest injects page-hook.js at document_start in MAIN across matching frames; bridge.js uses isolated content context. Page hook intercepts review sockets and patches client launch flags; bridge moves data to service-worker/offscreen. They are not website-native scripts.

### Evidence

- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 880.

```text
m/*"
      ],
      "js": [
        "page-hook.js"
      ],
      "run_at": "document_start",
      "world": "MAIN",
      "all_frames": true,
      "match_about_blank": true
    }
  ],
  "web_accessible_resources": [
    {
      "resources": [
        "engines/**"
      ],
      "matches": [
        "https://*.chess.com/*"
      ]
    }
  ]
}

```
- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
- **SRC-0029** `extension/bridge.js` — [preserved redacted evidence](../evidence/text/1b4678db6b14a69259f8a5a53b4dc9f3d54889c1c915c3bfa6b12f6ed4adc208.js)

**Source references:** SRC-0050, SRC-0053, SRC-0029  
**URL references:** None independently associated  
**Related findings:** FND-18954, FND-18956, FND-18891, FND-18944

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18944"></a>
## FND-18944: Quota launch checks are canCreate and locked, not just unlimited review

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Historical quota fix patches local analysis permission flags before the page snapshots them, preserving original PGN/config and handling later assignments or replacement objects. It is a local presentation/transport intervention; it does not change server membership,quota,library permissions or cloud storage.

### Evidence

- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 5786.

```text
ion
  // store at module initialization. In particular, its pre-socket gate is:
  //   !permissions.canCreate && permissions.uiLocked
  // where uiLocked comes from analysis.locked. hasUnlimitedReview alone only
  // affects report-card/upgrade UI; it does NOT let a new review start.
  // Change only local analysis permissions, never account membership or cloud
  // save/library rights. Getters also survive ordinary 
```
- **SRC-0061** `extension/test/quota-test.mjs` — [preserved redacted evidence](../evidence/text/884a4d3d79bedad907bb7c7c9dd44f17dfe7f5af254c96ec26b36a316b53d1ce.mjs)
  Character offset 763.

```text
ry:[\s\S]*?uiLocked:!!fq\.locked\}\)/)?.[0];
const gate = bundle.match(/function TZ\(\)\{return!pq\.canCreate&&pq\.uiLocked\}/)?.[0];
assert.ok(bootstrap && gate, 'reference page permission bootstrap/gate found');

function exhausted() {
  return { hasUnlimitedReview: false, canCreate: false, locked: true,
    canConfigure: false, canViewMoveFeedback: false, canViewCoachCommentary: false,
    canViewCompleteBasicAnal
```
- **SRC-0003** `QUOTA-FIX-INSTALL.txt` — [preserved redacted evidence](../evidence/text/f4743bdea513c51e8409333bf289915a738ede9623295bc57bf8a6c50aa02999.txt)
  Character offset 723.

```text
ed.

WHAT CHANGED
The old hook patched hasUnlimitedReview, but the page's actual launch gate
checks canCreate and locked before opening a review socket. Those local
analysis permissions are now patched before the page snapshots them.
Existing page configuration/PGN is preserved. Later normal quota assignments
and replacement analysis configurations are handled as well.

This does not change account membership, server
```

**Source references:** SRC-0053, SRC-0061, SRC-0003  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18943, FND-21049

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18945"></a>
## FND-18945: WebSocket brand-check regression is explicit

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Native prototype binaryType accessors reject unbranded receivers. The hook harness proves bare objects throw Illegal invocation, then exercises intercepted constructor,open,send,close,retry and passthrough with brand checks. This explains older superficially passing fake-socket tests being inadequate.

### Evidence

- **SRC-0059** `extension/test/hook-test.mjs` — [preserved redacted evidence](../evidence/text/098b1d1bcbda96d6a647a97d2cf62263510f843c76604ff0b5b87dd30912cb66.mjs)
  Character offset 143.

```text
tension/page-hook.js.
//
// WHY THIS EXISTS: v0.1.3 passed the old harness but threw
// `TypeError: Illegal invocation` in real Chrome. FakeReviewSocket inherits
// the native WebSocket.prototype, whose WebIDL accessors are brand-checked:
// assigning `this.binaryType = 'blob'` invoked the NATIVE setter with a
// non-WebSocket receiver and killed the constructor (-> S3e rejects ->
// "Could not connect to the analysi
```
- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 10095.

```text
 // `protocol` are getter-only (sloppy-mode writes silently no-op, so a
    // later *read* throws "Illegal invocation"), and `binaryType` has a real
    // native setter, so a plain `this.binaryType = 'blob'` throws
    // `TypeError: Illegal invocation` the instant a real browser constructs
    // this object (v0.1.3's exact failure — the Node harness has no brand
    // checks, so it passed there).  Own data prope
```

**Source references:** SRC-0059, SRC-0053  
**URL references:** None independently associated  
**Related findings:** FND-18946, FND-21051, FND-18891, FND-18943, FND-18944

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18946"></a>
## FND-18946: Only Game Review sockets loop back locally

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Hook route predicate intercepts configured CEAC game-review URLs, including same-origin variation; other sockets pass through native WebSocket. It handles ArrayBuffer binary frames and retains instanceof behavior. This is not a general network proxy.

### Evidence

- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 16957.

```text
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
  HookedWS.prototype.constructor = Ori
```
- **SRC-0059** `extension/test/hook-test.mjs` — [preserved redacted evidence](../evidence/text/098b1d1bcbda96d6a647a97d2cf62263510f843c76604ff0b5b87dd30912cb66.mjs)
  Character offset 9156.

```text
 { /* */ } }   // drain so open fires first

/* ------------------------------------------------ 3. passthrough socket */

origLog('\n=== passthrough: wss://www.chess.com/pubsub?uid=x ===');
captured.length = 0;
let real = null, realThrew = null;
try { real = new globalThis.WebSocket('wss://www.chess.com/pubsub?uid=x'); } catch (e) { realThrew = e; }
ok(!realThrew, 'passthrough constructor did not throw');
ok(!!real 
```

**Source references:** SRC-0053, SRC-0059  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18943, FND-18944, FND-18945, FND-21051

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18947"></a>
## FND-18947: Chrome runtime messaging needs base64 for binary

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bridge.js comments and functions document JSON serialization turning ArrayBuffer into{}. Binary data crosses chrome.runtime Port as base64 then converts back to bytes for window.postMessage/socket events. Encoding uses0x8000 chunks to avoid huge apply calls.

### Evidence

- **SRC-0029** `extension/bridge.js` — [preserved redacted evidence](../evidence/text/1b4678db6b14a69259f8a5a53b4dc9f3d54889c1c915c3bfa6b12f6ed4adc208.js)
  Character offset 685.

```text
t warn = (...a) => { try { console.warn('[local-review:bridge]', ...a); } catch { /* */ } };

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
  cons
```
- **SRC-0052** `extension/offscreen.js` — [preserved redacted evidence](../evidence/text/759114d70c5393f11a5d5b45883722267b7ed99f16753bccef415b1765c2a61d.js)
  Character offset 1321.

```text
t warn = (...a) => { try { console.warn('[local-review:engine]', ...a); } catch { /* */ } };

const B64_CHUNK = 0x8000;
const b64FromBytes = (bytes) => {
  const u8 = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  let s = '';
  for (let i = 0; i < u8.length; i += B64_CHUNK) s += String.fromCharCode.apply(null, u8.subarray(i, i + B64_CHUNK));
  return btoa(s);
};
const bytesFromB64 = (s) => {
  const b
```

**Source references:** SRC-0029, SRC-0052  
**URL references:** None independently associated  
**Related findings:** FND-18943, FND-18949, FND-18948

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18948"></a>
## FND-18948: Offscreen host dials out to avoid lost initial ports

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Offscreen module connects as engine after module graph initialization; SW binds/queues until ready rather than dialing into an unregistered listener. SW engine-bind timeout15seconds; it creates offscreen.html for WORKERS. Session keys route frames to content ports.

### Evidence

- **SRC-0054** `extension/service-worker.js` — [preserved redacted evidence](../evidence/text/8ee40f0e7d9bd5b241f2257f803fae4aaa77a41583f22e1e6f2863b1523338ef.js)
  Character offset 697.

```text
const warn = (...a) => { try { console.warn('[local-review:sw]', ...a); } catch { /* */ } };

const ENGINE_BIND_TIMEOUT_MS = 15000;

let offscreenPort = null;
let engineBound = null;          // resolver for the in-flight ensureEngine() wait
let engineReadyPromise = null;
const pendingToEngine = [];      // frames waiting for the engine host
const contentPorts = new Map();  // session -> port

async function hasOffsc
```
- **SRC-0052** `extension/offscreen.js` — [preserved redacted evidence](../evidence/text/759114d70c5393f11a5d5b45883722267b7ed99f16753bccef415b1765c2a61d.js)

**Source references:** SRC-0054, SRC-0052  
**URL references:** None independently associated  
**Related findings:** FND-18949, FND-18947

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18949"></a>
## FND-18949: Service-worker keepalive and computation progress are separate

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bridge sends ping every20000ms, service-worker handles port lifecycle, and offscreen sends progress keepalives. These are not engine work completion. SW lifecycle behavior should not be inferred solely from page percentage.

### Evidence

- **SRC-0029** `extension/bridge.js` — [preserved redacted evidence](../evidence/text/1b4678db6b14a69259f8a5a53b4dc9f3d54889c1c915c3bfa6b12f6ed4adc208.js)
  Character offset 3708.

```text
 kept seeing "port disconnected").
setInterval(() => { push({ kind: 'ping', session: SESSION }); }, 20000);

```
- **SRC-0054** `extension/service-worker.js` — [preserved redacted evidence](../evidence/text/8ee40f0e7d9bd5b241f2257f803fae4aaa77a41583f22e1e6f2863b1523338ef.js)
- **SRC-0052** `extension/offscreen.js` — [preserved redacted evidence](../evidence/text/759114d70c5393f11a5d5b45883722267b7ed99f16753bccef415b1765c2a61d.js)

**Source references:** SRC-0029, SRC-0054, SRC-0052  
**URL references:** None independently associated  
**Related findings:** FND-18943, FND-18947, FND-18948

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18950"></a>
## FND-18950: CEE API client serializes no-request-ID calls

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CeeClient maintains tail,pending,timer; CEE_Run accepts message.proto updates until is_final; logs/UCI notifications are not ordinary API replies. Worker errors fail and terminate the client. Default timeout240000ms; feature handles disposed in finally and worker disposed at review end.

### Evidence

- **SRC-0042** `extension/lib/cee.js` — [preserved redacted evidence](../evidence/text/90a0e507f5653d17af06df0f7b355441c3db75d8e958c3c3c17c57776e606af9.js)
  Character offset 681.

```text
 () => {}, timeoutMs = 240000 } = {}) {
    this.onLog = onLog;
    this.timeoutMs = timeoutMs;
    this.tail = Promise.resolve();
    this.pending = null;
    this.closed = false;
    this.worker = workerFactory(asset('engines/cee/explanation-engine.js') + '#' + asset('engines/cee/explanation-engine.wasm'));
    this.worker.onmessage = event => this.receive(event.data);
    this.worker.onerror = event => this.fail(n
```

**Source references:** SRC-0042  
**URL references:** None independently associated  
**Related findings:** FND-19429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18951"></a>
## FND-18951: Native review adapter merges CEAC search settings

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

newGameRequest merges runSearchReq search into NewGame settings, supports PGN or positionWithMoves fallback,defaults Fast and localeen_US. It forwards explicit result metadata and validates review move count against native playedLine.

### Evidence

- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)
  Character offset 595.

```text
LENT: 5, GOOD: 6, INACCURACY: 7, MISTAKE: 8, BLUNDER: 9,
  MISSED: 10, FORCED: 11, TRICKY: 20,
});

function newGameRequest(request, { pageGame, pgn } = {}) {
  let source = request.newGameReq?.newGame;
  if (!source?.from?.case) {
    if (pgn) source = { from: { case: 'pgnGame', value: { pgn, takeFirstGameOnly: true } } };
    else if (pageGame?.startFen) source = { from: { case: 'positionWithMoves', value: {
      
```

**Source references:** SRC-0049  
**URL references:** None independently associated  
**Related findings:** FND-18888, FND-18889, FND-18891

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18952"></a>
## FND-18952: Legacy effectiveRating alias is transparent, not verified V2 prediction

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

If CEE omits gameRatingV2, adapter copies effectiveRating to that optional field so current UI can display it, while diagnostics retain ratingSources. This is compatibility aliasing, not proof native V2 generation or a guessed curve.

### Evidence

- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)
  Character offset 6600.

```text
RatingV2' : 'effectiveRating';
      if (card.gameRatingV2 == null && card.effectiveRating != null) card.gameRatingV2 = card.effectiveRating;
    }
    const stats = reviewStats(gameReview, request.engine, ratingSources);
    if (!stats.engineMatchesRequest) onLog('Engine mismatch: requested=' + request.engine + ', actual=' + stats.actualEngines.join(',') + '; cloud parity is not yet established');
    onLog('CEE acc
```

**Source references:** SRC-0049  
**URL references:** None independently associated  
**Related findings:** FND-18888, FND-18889, FND-18891

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18953"></a>
## FND-18953: Native speech hashes and arrows survive the adapter

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

reviewStats counts speechSentences,audioHashes,boardMarkings and fragment arrows; returned GameReview retains native speech text/hash,explainLine,alternatives,opening,result and PGN. Counts alone do not prove a selected coach or audio fetch played correctly; user confirmation is separate.

### Evidence

- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)
  Character offset 2311.

```text
x => x != null))];
  const moves = gameReview.review?.playedMoves || [];
  let speechSentences = 0, audioHashes = 0, explanationArrows = 0;
  for (const entry of moves) for (const move of [entry.playedMove, entry.bestAlternativeMove]) {
    if (!move) continue;
    explanationArrows += move.boardMarkings?.arrows?.length || 0;
    for (const sentence of move.speech?.sentences || []) {
      speechSentences++;
      if
```
- **SRC-0069** `research/browser-cee-test.json` — [preserved redacted evidence](../evidence/text/c6c37e4eb874e42331d6aaf0fce294d4f22afd71a42b8d421ba813b820bb0245.json)
  Character offset 2214.

```text
n": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "speechSentences": 29,
    "audioHashes": 29,
    "explanationArrows": 27
  },
  "resultCase": "success",
  "logs": [
    "CEE review: requested engine=12, search={\"case\":\"gameReviewSearchSettings\",\"value\":{\"strength\":1}}",
    "Engine mismatch: requested=12, actual=11; cloud parity is not yet established",
    "CEE accuracy={\"white\":59
```

**Source references:** SRC-0049, SRC-0069  
**URL references:** None independently associated  
**Related findings:** FND-18888, FND-18889, FND-18891

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18954"></a>
## FND-18954: Manifest permissions and CSP belong to extension, not website

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Manifest minimumChrome116,permissionoffscreen,script-src self wasm-unsafe-eval/object-src self,service worker and engine web_accessible_resources. Do not report this as the live Chess.com HTTP CSP, CORS policy, or security-header audit.

### Evidence

- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 318.

```text
out server credits.",
  "minimum_chrome_version": "116",
  "permissions": [
    "offscreen"
  ],
  "content_security_policy": {
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self'"
  },
  "background": {
    "service_worker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "bridge.js"
      ],
      "ru
```

**Source references:** SRC-0050  
**URL references:** None independently associated  
**Related findings:** FND-18943, FND-18956

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18955"></a>
## FND-18955: Update ZIPs are overlays, not standalone installers

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

v0.1.6/0.1.8/0.1.9 ZIPs contain selected changed files and depend on existing engine/lib/bridge/SW assets. Delete-and-replace of the entire extension directory can break installation. Reload extension and refresh tabs after overlay.

### Evidence

- **SRC-0028** `extension/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Character offset 2005.

```text
review
   using the same analysis strength to see the measured-time estimate.

This small update is not a standalone extension installation.

---

## Previous v0.1.8 update notes

## v0.1.8 — hide debug card only

The bottom-left debug card is disabled. Diagnostics still appear in Chrome
DevTools Console with the `[local-review]` prefix. Review calculations, quota
handling, engine files, speech/audio, and Chess.com's
```
- **SRC-0003** `QUOTA-FIX-INSTALL.txt` — [preserved redacted evidence](../evidence/text/f4743bdea513c51e8409333bf289915a738ede9623295bc57bf8a6c50aa02999.txt)

**Source references:** SRC-0028, SRC-0003  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030, FND-18944, FND-18980

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18956"></a>
## FND-18956: Hook VERSION0.1.6 is retained with manifest0.1.9

**Category:** extension  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

page-hook internal VERSION stays0.1.6 to identify core quota/socket code; manifest is0.1.9. Badge flagfalse suppresses DOM creation; this version mismatch alone does not mean an update failed.

### Evidence

- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 1760.

```text
n(' '));
  };

  /* ------------------------------------------------------------- badge */

  const SHOW_DEBUG_BADGE = false; // Console diagnostics remain enabled.
  let badgeEl = null;
  let badgeLabel = null;
  let badgeLine1 = null;
  let lastStatus = { msg: 'hook installed', tone: 'ok' };
  let badgeTimer = null;

  function buildBadge() {
    if (!SHOW_DEBUG_BADGE) return true; // No DOM insertion or retry time
```
- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)

**Source references:** SRC-0053, SRC-0050  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18943, FND-18944, FND-18954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
