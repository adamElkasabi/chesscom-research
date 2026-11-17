# evaluation_bar — findings 1–7

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18926"></a>
## FND-18926: Native evaluation bar custom element

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

Historical play-computer static research identifies wc-evaluation-bar registration, customElements.get/define, instance onEvaluationUpdate and updateBar transform translate3d(0,100-percentage%,0). Some quoted play-computer bundles are absent, so retain this as documented historical evidence, not a new runtime verification.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 1454.

```text
 over observed facts;
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
    "wc-simple-move-lis
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18927"></a>
## FND-18927: Evaluation-bar event bus and manual override

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

Historical component listens to private evaluation.update or evaluation.override when update-manually is present. It is a module-local emitter, not a DOM event. Instance method invocation was proposed as a way to avoid minified-module access.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 3252.

```text
EvaluationUpdate();
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
 
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18928"></a>
## FND-18928: Evaluation-bar attributes and board readiness

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

The documented attributes include board-id,engine-name,game-id,update-manually,is-display-engine-details,is-default-fen-automatic,display-type,is-active. Base element waits for document.getElementById(boardId).game.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 4754.

```text
}
```

**[observed]** Attribute names come from `W7.ObservedAttributes` (shared.eager @2,892,030):
`board-id`, `engine-name`, `game-id`, `update-manually`, plus `is-display-engine-details`,
`is-default-fen-automatic`, `display-type`, `is-active`.
Base class `K7` resolves its board with `document.getElementById(this.boardId)` and only calls
`boardReady()` once that element exposes a `.game` object (@2,893,531).

**[ob
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18929"></a>
## FND-18929: Evaluation-bar default settings

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

Historical settings:depth20,timeLimit5,linesCount3,bar toggles false, maxThreads=min(ceil(hardwareConcurrency*0.2),5); analysis_engine_settings localStorage; emits evaluation.settings-update.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 5744.

```text
         // save
  Object.assign(F9, e);
  localStorage.setItem(q_, JSON.stringify(F9));   // q_ = "analysis_engine_settings"
  N9.emit('evaluation.settings-update');
}

L9 = ue(mde())                          // evaluation store: { fen, evaluatedFen,
                                        //   isCriticalPosition, isRunning, lines: [], ... }
function ESt(e) { ... L9.lines[e.multipv - 1] = e ... }
function I9() { ret
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18930"></a>
## FND-18930: Evaluation-bar score mapping

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

The documented score clamp is[-4,+4]pawns; coefficient45 and midpoint50 yield5%-95% for ordinary capped scores, mate/tablebase use0/100/50. Mate payload sign matters, and printed bar score can be magnitude-only. Full formatter/edge-case functions remain in preserved documentary blocks.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 6741.

```text
BAR_MARGIN: 10, BAR_WIDTH: 20, DEFAULT_BAR_PERCENTAGE: 50,
       DEFAULT_LOADING_COLOR: '#769656', SCORE_CALC_COEFFICIENT: 45, SCORE_CAP: 4 }
```

**[observed]** `shared.eager` @2,901,384:

```js
fyt = (e = 0) => e === null ? e : Math.max(-4, Math.min(4, e));          // clamp
pyt = (e = 0) => 3 - String(Math.floor(Math.abs(e))).length;             // decimals
myt = (e = 0) => `${e > 0 ? '+' : ''}${e.toFixed(pyt(Mat
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18931"></a>
## FND-18931: Bot-mode assistance visibility differs by preset

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

Historical play/computer gate H2 requires engine client loaded AND assistance.evaluationBar. Assisted/Coach presets set evaluationBartrue; Challenge/Custom/Friendly defaultfalse. shouldDisableEvaluationIfPlaying returnsfalse in that page context; do not generalize permission to live rated games.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 8984.

```text
ablebase cases.

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
  isWdlBarEnabled: () =>
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18932"></a>
## FND-18932: Unresolved bot lazy-loader predicates

**Category:** evaluation_bar  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Historical document was read in full; some underlying bundles/runtime traces cited there are not available.

_m() and bn() meanings were not resolved in original historical investigation. Their call-site effects were described, but actual semantics remain unknown; no REA evidence backend is accessible here.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 9881.

```text
ne client is behind a lazy loader:

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
them (`[unknown]`). What is o
```

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
