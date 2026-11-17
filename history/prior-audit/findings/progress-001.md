# progress — findings 1–6

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18957"></a>
## FND-18957: Original coarse progress was0/2/100, not a hidden-card regression

**Category:** progress  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

v0.1.7 offscreen repeated the last native milestone every4seconds. User initially reported a stall at0.019999999552965164 then clarified review succeeded and only percentage was wrong. There was no confirmed full review failure caused by hiding the badge.

### Evidence

- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 6893.

```text
serted the hidden card creates no elements.
- User initially reported the update stopped at progress0.019999999552965164, then explicitly corrected: "Sorry it worked BUT the analysis progress doesnt work!". No rollback was implemented. The apparent breakage was a coarse progress issue, not confirmed failure of the hidden-card update.
- Offscreen originally emitted0,0.02,1 and repeated its last value every4seconds bec
```
- **SRC-0011** `chess-local-review-v0.1.7-cee-update.zip!/offscreen.js` — [preserved redacted evidence](../evidence/text/fdd4dc3a8cf78d029619db86ee72233c302e05eed704972cc6f095f554377a72.js)

**Source references:** SRC-2049, SRC-0011  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18924, FND-18938, FND-19399, FND-19400

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18958"></a>
## FND-18958: v0.1.9 progress uses real local successful-duration samples

**Category:** progress  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ReviewProgressEstimator retains last40valid samples, groups by exact searchKey,selects up to7nearest lengths by absolute log position ratio,scales each duration by(currentPlies+1)/(samplePlies+1),then takes median. No stock timing constant trains a first-run estimate.

### Evidence

- **SRC-0047** `extension/lib/progress.js` — [preserved redacted evidence](../evidence/text/e2c47053d48c5a2dfa7e0dbd67b5109050c44a2bc63809345b1a7560d6f142e9.js)
  Character offset 739.

```text
st matches = this.samples.filter(s => s.searchKey === searchKey)
      .map(s => ({ ...s, distance: Math.abs(Math.log((plies + 1) / (s.plies + 1))) }))
      .sort((a, b) => a.distance - b.distance).slice(0, 7);
    // Scale by number of positions; use the median to resist unusually slow runs.
    const predictions = matches.map(s => s.durationMs * (plies + 1) / (s.plies + 1)).sort((a,b) => a-b);
    const mid = Math
```

**Source references:** SRC-0047  
**URL references:** None independently associated  
**Related findings:** FND-18959, FND-18960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18959"></a>
## FND-18959: First matching review is calibration, not smooth estimated progress

**Category:** progress  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

begin returns expectedMsnull without matching history; progress returnsnull. Original coarse milestones remain for that first review/strength. Later successful reviews train history. This deliberate limitation must be disclosed during installation.

### Evidence

- **SRC-0047** `extension/lib/progress.js` — [preserved redacted evidence](../evidence/text/e2c47053d48c5a2dfa7e0dbd67b5109050c44a2bc63809345b1a7560d6f142e9.js)
  Character offset 1101.

```text
 / (s.plies + 1)).sort((a,b) => a-b);
    const mid = Math.floor(predictions.length / 2);
    const expectedMs = predictions.length ? (predictions.length % 2 ? predictions[mid] :
      (predictions[mid - 1] + predictions[mid]) / 2) : null;
    this.active = { plies, searchKey, startedAt: now, expectedMs, sampleCount: matches.length };
    return { expectedMs, sampleCount: matches.length };
  }

  progress(now) {
    
```
- **SRC-0028** `extension/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)

**Source references:** SRC-0047, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-18958, FND-18960, FND-00028, FND-00029, FND-00030

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18960"></a>
## FND-18960: Estimated percentage is time-based and caps below completion

**Category:** progress  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

progress=min(0.95,0.02+0.93*elapsed/expectedMs). Offscreen ticks each1000ms,uses max to prevent backward movement and only reaches1when native result exists. At/after predicted duration it holds95%; not a position-completion counter or guaranteed ETA.

### Evidence

- **SRC-0047** `extension/lib/progress.js` — [preserved redacted evidence](../evidence/text/e2c47053d48c5a2dfa7e0dbd67b5109050c44a2bc63809345b1a7560d6f142e9.js)
  Character offset 1640.

```text
 completion for the actual result. If late, hold at 95%, not 100%.
    return Math.min(0.95, 0.02 + 0.93 * elapsed / this.active.expectedMs);
  }

  complete(now) {
    if (!this.active) return null;
    const { plies, searchKey, startedAt } = this.active;
    const sample = { plies, searchKey, durationMs: now - startedAt };
    this.active = null;
    if (!valid(sample)) return null;
    this.samples.push(sample);
 
```
- **SRC-0052** `extension/offscreen.js` — [preserved redacted evidence](../evidence/text/759114d70c5393f11a5d5b45883722267b7ed99f16753bccef415b1765c2a61d.js)

**Source references:** SRC-0047, SRC-0052  
**URL references:** None independently associated  
**Related findings:** FND-18958, FND-18959, FND-18947, FND-18948, FND-18949

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18961"></a>
## FND-18961: History persistence excludes personal game contents

**Category:** progress  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

localStorage key clr.review-timings.cee-1.130.285.pipeline1 stores plies,searchKey,durationMs only; no PGN/handle. Storage errors fall back to in-memory model. Failed/cancelled reviews do not complete/train samples. This is extension-local storage, not Chess.com page localStorage.

### Evidence

- **SRC-0052** `extension/offscreen.js` — [preserved redacted evidence](../evidence/text/759114d70c5393f11a5d5b45883722267b7ed99f16753bccef415b1765c2a61d.js)
  Character offset 639.

```text
Version the history when the engine/pipeline changes, not for cosmetic updates.
const TIMING_KEY = 'clr.review-timings.cee-1.130.285.pipeline1';
let timingHistory = [];
try { timingHistory = JSON.parse(localStorage.getItem(TIMING_KEY) || '[]'); } catch { /* memory-only fallback */ }
const timingModel = new ReviewProgressEstimator(timingHistory);
function saveTimings() {
  try { localStorage.setItem(TIMING_KEY, JSON.s
```
- **SRC-0047** `extension/lib/progress.js` — [preserved redacted evidence](../evidence/text/e2c47053d48c5a2dfa7e0dbd67b5109050c44a2bc63809345b1a7560d6f142e9.js)

**Source references:** SRC-0052, SRC-0047  
**URL references:** None independently associated  
**Related findings:** FND-18947, FND-18948, FND-18949, FND-18958, FND-18959

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18962"></a>
## FND-18962: Progress metadata callback is presentation-only

**Category:** progress  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

buildGameReview calls onWorkload after native NewGame with actual playedLine count and serialized search settings. It does not pre-search positions or change the CEE review call. Progress tests exercise mocked offscreen clock/history/failure/cancellation and real native review regression separately.

### Evidence

- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)
  Character offset 4793.

```text
ame point');
    // Timing metadata only. Does not change CEE settings or search order.
    options.onWorkload?.({
      plies: Math.max(0, (newGame.playedLine?.length || 1) - 1),
      searchKey: JSON.stringify(strength),
    });
    onProgress(0.02);
    // CEE infers checkmate/PGN results; forward explicit coordinate-game
    // metadata too, rather than assuming a winner from the review user's color.
    const me
```
- **SRC-0060** `extension/test/progress-test.mjs` — [preserved redacted evidence](../evidence/text/ed2ebd175d07d00a6e8e2acd5669b407f4519f487f352651247196a639084fd0.mjs)
  Character offset 2384.

```text
.stringify(obj)),decodeMessage:()=>({}),
  buildGameReview:async opts=>{
   opts.onProgress(0);opts.onWorkload({plies:20,searchKey:key});opts.onProgress(0.02);
   for(const time of [2500,5000,15000]) {now=time;for(const tick of timers.values())tick()}
   if(cancel)listener({kind:'socket-close',session:'test'});
   if(fail)throw Error('test engine failed');
   opts.onProgress(1);
   return {bytes:new TextEncoder().enc
```

**Source references:** SRC-0049, SRC-0060  
**URL references:** None independently associated  
**Related findings:** FND-18888, FND-18889, FND-18891

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
