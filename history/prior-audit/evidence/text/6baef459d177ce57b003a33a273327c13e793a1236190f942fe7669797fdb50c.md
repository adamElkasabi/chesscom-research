# How Chess.com builds and gates its evaluation bar

**Target:** production bundles served to `www.chess.com/play/computer` and `/analysis`
**Method:** static analysis of shipped JavaScript + REA (`analyze-javascript-application`) Evidence
**Date:** 2026-11-11
**Artifacts analysed**

| File | Bytes | Source |
| --- | --- | --- |
| `play-computer.js` | 417,849 | `/r2/client-packages/play-computer/2026.11.5/play-computer.js` |
| `shared.eager.B4_eyo3T4t.chunk.js` | 2,991,929 | `/r2/client-packages/play-computer/2026.11.5/` |
| `analysis.js` | 297,210 | `/r2/client-packages/analysis/2026.11.7/analysis.js` |
| `analysis-shared.eager.chunk.js` | 3,660,662 | `/r2/client-packages/analysis/2026.11.7/` |
| 36 lazy `client.*.chunk.js` / `tab-*.chunk.js` | 4.3 MB | same package roots |

REA Evidence record: `ev_a9a06871d585d6f7e3034afca02807f6a559738b9db111ce2259360bf479bcce`
(`chesscom/evidence/app-bundle.json`, 2,355 static findings, 178 analysed records).
Two 3 MB chunks exceeded REA's 1 GiB worker heap and are recorded as **explicit unknowns**
(`resource_constraint`, `max_heap_mb=1024`); facts below that come from those files were
recovered with byte-offset reads, which is flagged per claim.

Everything in this document is one of: **[observed]** = literal string/expression in the
shipped file at the cited offset; **[inferred]** = reasoning over observed facts;
**[unknown]** = not established.

---

## 1. The rendering source of truth: `<wc-evaluation-bar>`

**[observed]** `play-computer.js` registers a tag → constructor map:

```js
// play-computer.js @369409
u1 = n((() => {
  X$(), su(), n1(), c1(),
  l1 = {
    "wc-eco-opening":     Y$,
    "wc-evaluation-bar":  Al,
    "wc-evaluation-lines": t1,
    "wc-move-list":       s1,
    "wc-simple-move-list": o1
  }
}))
```

`Al` is re-exported as internal `dt` (`play-computer.js @47381`, export map `dt as Al`) and
imported from the shared eager chunk (`import { dt as Al } from "./shared.eager.B4_eyo3T4t.chunk.js"`).
Registration goes through Chess.com's helper:

```js
// shared.eager chunk @252125
function Ig(e, t) {
  typeof customElements < 'u' && !customElements.get(e) && customElements.define(e, t);
}
```

and the app bootstrap hands that map to the runtime:

```js
// play-computer.js @417180
function t6() {
  Uu(W3).mount(document.createElement("div"));
  tr({ clients: vL, controllers: N$, elements: l1, extensions: B3, hooks: {...} });
}
```

**[inferred]** The bar is a *custom element* whose class is reachable at runtime via
`customElements.get('wc-evaluation-bar')`, and whose constructor is the Svelte-ish class
`OSt extends K7 extends HTMLElement`.

### 1.1 The component contract

**[observed]** `shared.eager` @2,943,076 and following — the component's own methods:

```js
OSt = class extends K7 {
  static get observedAttributes() {
    return [W7.ObservedAttributes.BoardId, W7.ObservedAttributes.EngineName,
            W7.ObservedAttributes.UpdateManually, W7.ObservedAttributes.GameId];
  }

  boardReady() {
    this.removeListeners(); this.addListeners(); this.onUpdateOptions();
    this.hasAttribute(W7.ObservedAttributes.UpdateManually) || this.onEvaluationUpdate();
  }

  addListeners() {
    this.hasAttribute('update-manually')
      ? N9.on('evaluation.override', this.onEvaluationUpdateHandler)
      : N9.on('evaluation.update',   this.onEvaluationUpdateHandler);
    this.addBoardEventListener(B.OptionsEvents.Update, this.onUpdateOptionsHandler);
  }

  componentReady() {
    this.readEngineName();
    this.style.flex = '1 1 auto';
    this.innerHTML = `
      <div class="evaluation-bar-bar evaluation-bar-thin-bar ...">
        <span class="evaluation-bar-scoreAbbreviated"></span>
        <span class="evaluation-bar-score"></span>
        <div class="evaluation-bar-fill">
          <div class="evaluation-bar-color evaluation-bar-black"></div>
          <div class="evaluation-bar-color evaluation-bar-draw"></div>
          <div class="evaluation-bar-color evaluation-bar-white" style="transform: translate3d(0, 50%, 0)">
            <span class="evaluation-bar-critical"></span>
          </div>
        </div>
      </div>`;
    this.barElement = this.querySelector('.evaluation-bar-color.evaluation-bar-white');
    ...
  }

  onEvaluationUpdate(e) {
    let t = e ?? I9().lines[0];             // payload, or the analysis store's PV1
    ...
    let n = yyt(t);                         // score -> percentage
    if (n !== this.barPercentage) { this.barPercentage = n; this.updateBar(); }
    this.updateScore(t);
  }

  updateBar() {
    this.barElement.style.transform = `translate3d(0, ${100 - this.barPercentage}%, 0)`;
  }
}
```

**[observed]** Attribute names come from `W7.ObservedAttributes` (shared.eager @2,892,030):
`board-id`, `engine-name`, `game-id`, `update-manually`, plus `is-display-engine-details`,
`is-default-fen-automatic`, `display-type`, `is-active`.
Base class `K7` resolves its board with `document.getElementById(this.boardId)` and only calls
`boardReady()` once that element exposes a `.game` object (@2,893,531).

**[observed]** Event bus is a module-local emitter, not a DOM event:

```js
// shared.eager @2,940,467 region
pSt, N9 = (VJ(), { createEventEmitter: pSt } = zJ, pSt());
```

**[observed]** Settings store and its persistence (same region):

```js
F9 = { depth: 20, timeLimit: 5, linesCount: 3, engineName: a5,
       isWdlBarSupported: false, hasChosenComplexityBar: false, wdlBarEnabled: false,
       tbBarEnabled: false, criticalPositionEnabled: false,
       maxThreads: Math.min(Math.ceil((navigator.hardwareConcurrency || 0) * 0.2), 5) }

function gSt(e) {                       // save
  Object.assign(F9, e);
  localStorage.setItem(q_, JSON.stringify(F9));   // q_ = "analysis_engine_settings"
  N9.emit('evaluation.settings-update');
}

L9 = ue(mde())                          // evaluation store: { fen, evaluatedFen,
                                        //   isCriticalPosition, isRunning, lines: [], ... }
function ESt(e) { ... L9.lines[e.multipv - 1] = e ... }
function I9() { return L9; }
```

**Consequence [inferred]:** the bar takes an *object* shaped
`{ score: <pawns, white POV>, mateIn?: number, stalemate?: boolean, tablebaseOutcome?: string,
multipv?: number, depth?: number }`, and there are two ways to drive it: emit on the private
bus, or call the instance method `onEvaluationUpdate(payload)` directly. The method is a
normal prototype method, so the second route needs no access to minified module scope.

---

## 2. The score maths (what any substitute implementation must reproduce)

**[observed]** `shared.eager` @2,657,030:

```js
G_ = { BAR_MARGIN: 10, BAR_WIDTH: 20, DEFAULT_BAR_PERCENTAGE: 50,
       DEFAULT_LOADING_COLOR: '#769656', SCORE_CALC_COEFFICIENT: 45, SCORE_CAP: 4 }
```

**[observed]** `shared.eager` @2,901,384:

```js
fyt = (e = 0) => e === null ? e : Math.max(-4, Math.min(4, e));          // clamp
pyt = (e = 0) => 3 - String(Math.floor(Math.abs(e))).length;             // decimals
myt = (e = 0) => `${e > 0 ? '+' : ''}${e.toFixed(pyt(Math.min(100, Math.abs(e))))}`;
hyt = e => (e !== null && e > 0) ? 100 : 0;
gyt = e => 50 - Math.abs(e ?? 0) * 45 / 4;
_yt = e => (e ?? 0) * 45 / 4 + 50;

X7 = (e = {}) => e.mateIn === 0;                     // checkmate
Z7 = (e = {}) => e.tablebaseOutcome;
Q7 = (e = {}) => e.stalemate;
$7 = (e = {}) => typeof e.mateIn === 'number';       // mate
vyt = e => e.tablebaseOutcome === '1-0' ? 100 : e.tablebaseOutcome === '0-1' ? 0 : 50;
t9 = (e = 0) => e !== null && e > 0;
e9 = (e = 0) => e !== null && e < 0;

yyt = (e = {}) => {
  const t = fyt(e?.score ?? null);
  return $7(e) ? hyt(t) : Z7(e) ? vyt(e) : t9(t) ? _yt(t) : e9(t) ? gyt(t) : 50;
};

n9  = e => X7(e) ? (t9(e.score) ? '1-0' : '0-1') : Q7(e) ? '½-½' : $7(e)
          ? `M${Math.abs(e.mateIn ?? 0)}`
          : typeof e.score !== 'number' || Number.isNaN(e.score) ? ''
          : myt(Math.min(100, e.score));

uyt = e => { /* magnitude, trimmed: 0 -> "0.0", 3 -> "3.0", 12.5 -> "12.5", 7.25 -> "7.25" */ };
dyt = e => X7(e) ? (t9(e.score) ? '1-0' : '0-1')
        : Q7(e) ? '½'
        : $7(e) ? `M${Math.abs(e.mateIn ?? 0)}`
        : Z7(e) ? 'TB'
        : uyt(e.score);
```

Notes for reimplementers **[inferred]**:

* `yyt` decides the *percentage* from the **sign of `score`**, even for mate — so a mate
  payload must carry a signed `score` (±4 is what the engine wrapper produces) or the bar
  renders full for the wrong side.
* `dyt` (the number printed *on* the bar) is magnitude-only; the signed value lives in the
  hover element (`n9`/`myt`).
* Everything is White point of view. A UCI `score cp` is side-to-move POV and must be negated
  when Black is to move.

The extension's `test/logic.test.mjs` transcribes these functions verbatim and asserts the
shipped `page-agent.js` reproduces them — 60/60 checks pass, including mate, stalemate and
tablebase cases.

---

## 3. The visibility gate

**[observed]** `play-computer.js` @386,899:

```js
function H2() { return cu().loaded && Fe().evaluationBar }
```

**[observed]** the same module feeds that predicate into the page's dependency-injection
context (@386,899 region):

```js
W2 = {
  getEvaluationProgress: () => 1,
  isDefaultFenAutomatic: () => false,
  isEvaluationBarVisible: H2,
  isWdlBarEnabled: () => false,
  shouldDisableEvaluationIfPlaying: () => false,
  showFairPlayMessageOnPresenceChange: () => true,
  updateManually: () => false
}, G2 = B2(W2)
```

So the bar is shown when **the engine client reports `loaded`** *and* **the assistance
setting `evaluationBar` is on**. `shouldDisableEvaluationIfPlaying` returning `false` on this
page means the "kill evaluation while playing" path is *not* what suppresses the bar — the
`cu().loaded` term is.

**[observed]** the engine client is behind a lazy loader:

```js
// play-computer.js @386,899 region
R2 = es({
  triggers: _m() ? [() => $c(et)] : [],
  shouldLoad: () => _m() && !bn(),
  loader: () => O(() => e(() => import('./client.03a446da.Bw4BRYjdl2.chunk.js'), ...))
});
B2 = Fl({ clients: [R2], context: td });
```

`_m()` and `bn()` are defined in the play shared chunk's module graph; REA did not resolve
them (`[unknown]`). What is observable is the effect: on a fresh bot game the engine chunk is
not fetched until the loader's triggers fire, and until then `cu().loaded` is `false`, so
`H2()` is `false` even with the setting on.

### 3.1 The setting is per game mode — and two modes already turn it on

**[observed]** `shared.eager` @1,732,753:

```js
OX   = { botChat: true, showHint: false, evaluationBar: false, threats: false,
         suggestions: false, feedback: false, lines: false, takebacks: false };  // Challenge / Custom
nVe  = { botChat: true, showHint: true,  evaluationBar: false, threats: false,
         suggestions: false, feedback: false, lines: false, takebacks: true  };  // Friendly
rVe  = { botChat: true, showHint: true,  evaluationBar: true,  threats: true,
         suggestions: true,  feedback: false, lines: true,  takebacks: true  };  // Assisted
iVe  = { suggestions: false, threats: false, evaluationBar: true, feedback: true,
         lines: false, botChat: true, showHint: true, takebacks: true };         // Coach

kX = { [Modes.Types.Assisted]: rVe, [Modes.Types.Challenge]: OX,
       [Modes.Types.Custom]: OX,   [Modes.Types.Friendly]: nVe,
       [Modes.Types.Coach]: iVe };
```

**[inferred]** In a bot game the eval bar is a first-class *assistance* feature: the
**Assisted** and **Coach** presets ship with `evaluationBar: true`. The bar is not hidden
because "evaluation is forbidden during play" — it is hidden because *that preset* disables
it and/or because the engine client has not loaded yet. The UI string is the same one the
settings modal renders (@218,655):

```js
evaluationBar: { label: 'Evaluation Bar', tooltip: 'See what side is winning.' }
```

This matches the reported `shouldDisableEvaluationIfPlaying: () => !1`.

---

## 4. The engine stack

**[observed]** `analysis.js` @~121,000 (engine bootstrap):

```js
async function QK() {
  let e = WK();
  return new Promise(t => {
    e.engine ? e.engine.stopFast(n => { e.engine = n; t(); }, 200)
             : (e.engine = (0, $K.default)({ enginePath: Lc(), pathToWasmEngine: bd() }), t());
  });
}

async function tq(e) {
  await QK();
  const t = WK().engine;
  return new Promise(n => { t.send(`position fen ${e}`, () => { t.send('fetch threats', n); }); });
}
```

**[inferred]** the client is a UCI-shaped worker wrapper — `send(cmd, cb)`, `stopFast(cb, ms)`,
custom verbs such as `fetch threats` — with a local-engine variant behind the same interface.

**[observed]** engine asset catalogue (`analysis-shared.eager` @~133,018 and the string map
@~295,326). Torch:

```js
nP = {
  full: { multiThreaded:  { loader: '/r2/assets-chess-engine/Torch/torch-2-85193a7.js' },
          singleThreaded: { loader: '/r2/assets-chess-engine/Torch/torch-2-single-697050e.js' } },
  lite: { multiThreaded:  { loader: '/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js' },
          singleThreaded: { loader: '/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js' } }
}
```

Stockfish (same table, `iP[QN.STOCKFISH_NNUE]`): display name `Stockfish 16.1`, `66MB`,
`paths.settings: { Threads: '1' }`, `pathToBook` = `bundles/app/js/engine/books/eco.json`
unless the `analysis_engine_skip_book` feature flag is set.

Files shipped under `bundles/app/js/engine/`: `stockfish-nnue-15.1{,-no-Worker,-no-simd}.{js,wasm}`,
`stockfish-nnue-16{,-no-Worker,-no-simd,-single}.{js,wasm}`, `stockfish{,-single}.{js,wasm}`,
`stockfish.asm.js`, `torch{,-lite}.{js,wasm}` and NNUE nets `nn-5af11540bbfe.nnue`,
`nn-ad9b42354671.nnue`. **These are byte-identical filenames to the `stockfish@16.0.0` npm
build**, i.e. Chess.com ships that upstream Emscripten build with its multi-threaded /
single-threaded / no-SIMD fallbacks.

**[observed]** page-level engine settings live in `localStorage['analysis_engine_settings']`
(see §1.1), default depth 20, 3 PVs, 5 s time limit.

---

## 5. What this means for a browser extension

**Goal restated:** make the *native* bar visible and correct during a game, without writing a
new bar.

Three levers exist, in increasing order of fragility:

1. **Feed the component directly.** `document.querySelector('wc-evaluation-bar')` returns the
   live element; if the page has not mounted one, `document.createElement('wc-evaluation-bar')`
   produces a real instance as long as the tag is registered. Calling
   `el.onEvaluationUpdate({ score, mateIn, depth })` renders through Chess.com's own code,
   stylesheet and DOM. No minified module scope is touched. **[observed → inferred, high
   confidence]**
2. **Create the element yourself** and attach it to the active board with `board-id` set to the
   board element's DOM id — this bypasses `H2()` entirely, because `H2()` only controls whether
   *the page* mounts the component, not whether the component works.
3. **Flip the setting / force the loader** (`Fe().evaluationBar = true`, or fire `R2.shouldLoad`).
   This is what the "Assisted" preset does. It needs access to minified module state, which is
   only reachable by patching the bundle at load time — brittle across releases. **[inferred]**

The extension in `chess-eval-bar/` uses **1 → 2**, and falls back to markup that reuses the
same `evaluation-bar-*` classes and maths if the tag is ever unregistered.

**Unknowns / limits of this analysis**

* `_m()` and `bn()` (the lazy-loader gates) were not resolved; their semantics are inferred
  from call sites only.
* REA's worker hit its heap limit on both 3 MB eager chunks, so relation coverage for those
  files is partial (`coverage.status: partial`, 514 semantic unknowns). Offsets quoted from
  those files were read directly, not through REA.
* No live browser was available in this environment: the component contract is established
  from shipped code, not from a runtime observation. The extension therefore verifies itself
  at runtime (`test/engine.html`) and degrades to a same-CSS fallback.
* Whether the page's own bar mounts in a given bot-game preset is runtime state we could not
  observe logged-out; the extension handles both cases (adopt if present, instantiate if not).
