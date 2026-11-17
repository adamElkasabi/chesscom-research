# historical — findings 1–6

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18888"></a>
## FND-18888: Superseded v0.1.6 backup used invented classifications and rating heuristics

**Category:** historical  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The retained backup used CP thresholds excellent10/good35/inaccuracy90/mistake220,GreatFind gap120,material sacrifice2,moveAccuracy=100*exp(-(loss/220)^1.5),phase slicing,handwritten sentences and Elo-style rating heuristics. These are agent-authored approximations,not recovered proprietary algorithms. Current extension/lib/review.js instead calls shipped native CEE and carries native output; this backup must never be presented as current parity or silently omitted.

### Evidence

- **SRC-0067** `research/backups/review-v0.1.6.js` — [preserved redacted evidence](../evidence/text/db95e817f9f5c6df4271dbb73cab441c2310cfa0a26ca8fa2f1ed1794217fc3b.js)
  Character offset 1732.

```text
DME.  `loss` is centipawns the mover
// threw away relative to best play (their own point of view).
const T = { excellent: 10, good: 35, inaccuracy: 90, mistake: 220 };
const GREAT_FIND_GAP = 120;   // cp gap between best and 2nd best line
const BRILLIANT_SAC = 2;      // pawns of material the mover must give up

function classify({ playedUci, bestUci, loss, onlyMove, lines, sacForMover, mateForMover, mateMissed }) {
```
- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)

**Source references:** SRC-0067, SRC-0049  
**URL references:** None independently associated  
**Related findings:** FND-19170, FND-19178, FND-18889, FND-18891

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18924"></a>
## FND-18924: User debug-console exception did not establish an engine failure

**Category:** historical  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Directly available user report in the current conversation; cause remains unknown.

The user ran window.chesscom.getCeeBinaryInterfaceLogs() and got TypeError reading the method because window.chesscom was undefined. No exact execution context or cause was established; do not claim the correct frame selection was tested.

### Evidence

- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 4220.

```text
yInterfaceLogs when the appropriate binary-interface client initializes. User tried window.chesscom.getCeeBinaryInterfaceLogs() and got TypeError because window.chesscom was undefined in that console context. The precise cause/frame context was NOT established; it does not prove the API is globally available on every page.
- Static full Game Review path selected engine12 for web_analysis_torch_human_v2, encoded it, a
```

**Source references:** SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18982"></a>
## FND-18982: Audio-confirmation evidence supersedes old release-note unknown

**Category:** historical  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Original v0.1.7 README says audio not confirmed; later user explicitly confirmed sound/UI worked. This is a user runtime observation,not independent verification of all coach choices/threat arrows. Preserve both with dates/provenance.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 1030.

```text
eep it like that step by step".
- User confirmed v0.1.7 UI and audio: "HOLY shit it worked even the sound worked everything turned out perfectly the UI the sound everything is nice now it's refinement time!". This is a user runtime report, not independent playback verification.
- Exact cloud parity was never achieved. User rejected invented accuracy/rating formulas; native Chess.com implementation should supply the n
```

**Source references:** SRC-0016, SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003, FND-18916, FND-18924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18983"></a>
## FND-18983: Original REA analysis cannot be independently re-opened

**Category:** historical  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Exact content of the cited stored artifact; not a claim of current live deployment.

Uploaded documents cite ev_a9a06871d585d6f7e3034afca02807f6a559738b9db111ce2259360bf479bcce with2355static findings/178records and2large chunks hitting1024MBheap/514unknowns. This audit can preserve that report,not claim the external record was accessed or those counts independently reproduced.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 809.

```text
 lazy `client.*.chunk.js` / `tab-*.chunk.js` | 4.3 MB | same package roots |

REA Evidence record: `ev_a9a06871d585d6f7e3034afca02807f6a559738b9db111ce2259360bf479bcce`
(`chesscom/evidence/app-bundle.json`, 2,355 static findings, 178 analysed records).
Two 3 MB chunks exceeded REA's 1 GiB worker heap and are recorded as **explicit unknowns**
(`resource_constraint`, `max_heap_mb=1024`); facts below that come from thos
```
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 473.

```text
** byte-offset reads of the shipped bundles (REA `analyze-javascript-application`,
evidence record `ev_a9a06871…479bcce`) plus protobuf
descriptor extraction; every schema claim is validated offline against libprotobuf (§10.3)
**Date:** 2026-11-11
**Companion:** `REVERSE-ENGINEERING.md` covers the *live-board* evaluation bar that the
extension taps; this document covers the *post-game* premium analysis, which is a
di
```

**Source references:** SRC-2048, SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219, FND-00085, FND-00086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18984"></a>
## FND-18984: User target corrections are authoritative for comparisons

**Category:** historical  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Bot86.8/79.8and1850/1500 supersede older93.7/85.6and1800/1700; human76.8/70.2and1350/600. Old values remain historical reports,not additional simultaneous acceptance targets.

### Evidence

- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 1818.

```text
/1000. Full targets remain in research/refinement/target.json.
- Earlier bot fixture target accuracy86.8/79.8, ratings1850/1500 supersedes older93.7/85.6,1800/1700. Earlier human fixture target76.8/70.2,1350/600. Individual per-move Chess.com labels for these references were not provided.
- Compact tally strings can concatenate White and Black counts; Blunder10 means White1/Black0, not ten blunders. Six visible categ
```
- **SRC-0875** `research/refinement/validate.mjs` — [preserved redacted evidence](../evidence/text/ccce04a549f1b1600d82a1fdd478cf17a877c2003d207bab12a8aa329fd4d688.mjs)
  Character offset 503.

```text
:{3:1,4:13,5:12,8:2,10:1,9:1},black:{3:0,4:10,5:9,8:6,10:3,9:0}}},
 'example-game':{accuracy:{white:86.8,black:79.8},ratings:{white:1850,black:1500},tallies:{white:{3:4,4:20,5:22,8:0,10:1,9:0},black:{3:0,4:18,5:21,8:5,10:1,9:1}}},
};
const results=[];
for(const fixture of Object.keys(references))for(const variant of [
 {name:'baseline',options:{Normalize:true}},
 {name:'normalize-off',options:{Normalize:false}},
 {na
```

**Source references:** SRC-2049, SRC-0875  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18924, FND-18938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18985"></a>
## FND-18985: Coach-model and callback failures must not be reinterpreted as exhaustive absence

**Category:** historical  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** medium — Conversation summary preserves failure class but not every original URL/tool result.

Condensed history reports repeated .bzp/charm404and logged-out game/callback404/HTML. Some exact targets are unavailable. A logged-out404does not prove authenticated route absence; this audit does not invent or re-probe missing URLs.

### Evidence

- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 2449.

```text
 numerical results. Later sweeps ran sequentially.
- Repeated coach .bzp/charm-model probes returned404; their precise URLs are not preserved in the available condensed context. Do not reconstruct guessed URLs or re-probe them.
- Logged-out game/callback JSON probes returned404/HTML; exact targets not all retained. These failures do not establish endpoint absence for authenticated users.
- Raw-state source12 experime
```

**Source references:** SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18924, FND-18938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
