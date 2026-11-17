# historical_documentation — findings 201–274

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00201"></a>
## FND-00201: 10.3 The stronger check — block 831

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The field numbers in this document were recovered by reading descriptors, so the
real test is whether they match a *real* protobuf implementation.
`crosscheck/` does that: it builds the message with libprotobuf, serialises it,
and compares my decoder's output field by field. It needs Google's runtime,
which is not part of this workspace — `pip install protobuf grpcio-tools` first.
The generated `analysis_subset_pb2.py` is committed, so only the `protobuf`
runtime is strictly required.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 831–837.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00202"></a>
## FND-00202: 10.3 The stronger check — block 839

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```
$ cd /home/user/chesscom/crosscheck && python3 crosscheck.py
PASS  accuracy_white         encoded=     87.25  decoded=87.25
PASS  effective_rating       encoded=      2040  decoded=2040
PASS  tactics_change         encoded=       -60  decoded=-60
PASS  negative_cp            encoded=      -310  decoded=-310
...
23/23 cross-checks passed — libprotobuf frame was 362 bytes
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 839–847.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00203"></a>
## FND-00203: 10.3 The stronger check — block 849

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

That is the evidence that the schema in this document is right, independent of
chess.com being reachable.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 849–850.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00204"></a>
## FND-00204: 10.4 No-network statement — block 854

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

This sandbox has no route to chess.com and no account. Every claim above is
from static analysis of the downloaded bundles, every formula was executed
locally (Node), and every schema was validated against libprotobuf offline.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 854–856.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00205"></a>
## FND-00205: 10.4 No-network statement — block 858

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 858–858.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00206"></a>
## FND-00206: 11. What is computed where — block 862

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Number the user sees | Producer | Where in the bundle |
| --- | --- | --- |
| Accuracy % | server, CAPS2 | `highlights.accuracy` → `pqe()` 1,699,347 |
| Elo estimate | server, report card | `report_card.*.gameRatingV2` → `jqe()` 1,701,418 |
| Per-phase accuracy | server | `reports_by_phase[].accuracy` |
| Per-category rating + delta | server | `reports_by_category[].new_rating / rating_change` |
| Move classification | server | `Move.move_classification`, `EvalGraphTick` |
| Tally counts | server | `ClassificationTallies` |
| Eval graph points | server | `EvalGraph.eval_graph_ticks[].move_score` |
| Explanation sentences | server (CEE), pre-rendered | `Move.speech`, `explain_line` |
| Arrows / highlights | server | `BoardMarkings` |
| Annotated PGN | server | `Metadata.annotated_pgn` |
| "Winning / better / equal" band | **client** | `xSt()` 2,768,546 |
| Which sentence variant | **client** | `ESt()` + 10-key (downgrade) table |
| Show-or-hide the report card | **client** | `vp()` in `tab-review...` |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 862–876.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00207"></a>
## FND-00207: 11. What is computed where — block 878

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

One line: the client owns **word choice and visibility**, the server owns
**every number**.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 878–879.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00208"></a>
## FND-00208: 11. What is computed where — block 881

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 881–881.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00209"></a>
## FND-00209: 12. What this means for the eval-bar extension — block 885

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Nothing here changes the extension, and nothing here should. The extension
drives the *live board's* `wc-evaluation-bar`, which is a different code path:
that bar is fed by a local Stockfish worker and `onEvaluationUpdate({score,
mateIn, depth})`, not by CEAC. The premium review is a batched, server-side,
post-game product.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 885–889.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00210"></a>
## FND-00210: 12. What this means for the eval-bar extension — block 891

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Three things are worth borrowing:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 891–891.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00211"></a>
## FND-00211: 12. What this means for the eval-bar extension — block 893

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

1. **`Engine.TORCH_HUMAN` explains the "Great/Brilliant" mystery.** Those badges
   are not thresholds on centipawn loss; they come from an engine that models
   plausible human moves. A local Stockfish bar will never reproduce them, and
   it should not try.
2. **The rating-scaled bands (§7.2) are a genuinely good idea for the hover
   preview.** "How big an advantage counts as winning" genuinely depends on the
   level of play. The band table is already inverted for us: 2.77 pawns at 2000,
   1.93 at 2800. It is a sentence-picker, so it must stay out of the numeric
   readout — but it is a defensible way to choose a *colour* for a hover cue.
3. **The `Score` message is the one convention to keep.** Everything is
   `score_centipawns_white` — always White's point of view, never the side to
   move's. The extension already normalises this way; the premium stack proves
   it is the house style.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 893–905.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00212"></a>
## FND-00212: 12. What this means for the eval-bar extension — block 907

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 907–907.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00213"></a>
## FND-00213: 13. Appendix: files — block 911

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Path | What |
| --- | --- |
| `PREMIUM-ANALYSIS.md` | this document |
| `CLIENT-SIDE.md` | inventory of everything that runs in the browser + what was extracted |
| `schemas/*.proto` | 28 extracted schemas, package-prefixed |
| `ALL-SCHEMAS.proto` | all 422 descriptors rendered (12,971 lines) |
| `client/` | extracted tables + `analysis-client.mjs` + 100-check test |
| `tools/ceac-dump.mjs` | dependency-free frame decoder + 20-check selftest + fixture writer |
| `tools/protoread.py` | descriptor → `.proto` renderer |
| `tools/extract-client-tables.py` | regenerates `client/*.json` from the bundles |
| `crosscheck/` | libprotobuf round-trip proof (23 checks) |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 911–921.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00214"></a>
## FND-00214: 13. Appendix: files — block 923

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The raw bundles (`raw/`) and descriptor blobs (`proto/`) were deleted to keep
the workspace small; both are re-derivable — see `REDOWNLOAD.md`. The rendered
schemas, the extracted tables and the tests were kept, so everything that
*proves* the claims still runs offline.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 923–926.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00215"></a>
## FND-00215: Offsets cited above — block 930

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

All are character offsets into `chunks/shared.eager.BOGLllgUUR.chunk.js`
(3,660,286 bytes) unless stated.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 930–931.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00216"></a>
## FND-00216: Offsets cited above — block 933

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Offset | Symbol |
| --- | --- |
| 315,764 | `af()` unlimited-review entitlement |
| 327,157 | `Om()` locked-takeaway check |
| 522,636 | `wdl()` rating → win/draw/loss model |
| 1,133,145 | empty CAPS / tallies accumulator |
| 1,699,347 | `pqe()` accuracy → UI |
| 1,701,418 | `jqe()` report card → UI |
| 1,711,579 | `AJe()` response → gameProps |
| 1,812,384 | `EW.Urls` endpoint table |
| 1,813,143 | `M4e()` report-card entitlement |
| 1,813,265 | `P4e()` depth → strength |
| 1,814,722 | `W4e()` request builder |
| 1,836,513 | `C3e()` frame decoder |
| 2,768,245 | `ySt()` band → pawn thresholds |
| 2,768,546 | `xSt()` move → band classifier |
| 46,853 / 47,090 / 49,042 | `tab-review...`: rating display rules, tooltip text |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 933–949.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00217"></a>
## FND-00217: How Chess.com builds and gates its evaluation bar — block 3

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Target:** production bundles served to `www.chess.com/play/computer` and `/analysis`
**Method:** static analysis of shipped JavaScript + REA (`analyze-javascript-application`) Evidence
**Date:** 2026-11-11
**Artifacts analysed**

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 3–6.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00218"></a>
## FND-00218: How Chess.com builds and gates its evaluation bar — block 8

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| File | Bytes | Source |
| --- | --- | --- |
| `play-computer.js` | 417,849 | `/r2/client-packages/play-computer/2026.11.5/play-computer.js` |
| `shared.eager.B4_eyo3T4t.chunk.js` | 2,991,929 | `/r2/client-packages/play-computer/2026.11.5/` |
| `analysis.js` | 297,210 | `/r2/client-packages/analysis/2026.11.7/analysis.js` |
| `analysis-shared.eager.chunk.js` | 3,660,662 | `/r2/client-packages/analysis/2026.11.7/` |
| 36 lazy `client.*.chunk.js` / `tab-*.chunk.js` | 4.3 MB | same package roots |

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 8–14.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00219"></a>
## FND-00219: How Chess.com builds and gates its evaluation bar — block 16

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

REA Evidence record: `ev_a9a06871d585d6f7e3034afca02807f6a559738b9db111ce2259360bf479bcce`
(`chesscom/evidence/app-bundle.json`, 2,355 static findings, 178 analysed records).
Two 3 MB chunks exceeded REA's 1 GiB worker heap and are recorded as **explicit unknowns**
(`resource_constraint`, `max_heap_mb=1024`); facts below that come from those files were
recovered with byte-offset reads, which is flagged per claim.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 16–20.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00220"></a>
## FND-00220: How Chess.com builds and gates its evaluation bar — block 22

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Everything in this document is one of: **[observed]** = literal string/expression in the
shipped file at the cited offset; **[inferred]** = reasoning over observed facts;
**[unknown]** = not established.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 22–24.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00221"></a>
## FND-00221: How Chess.com builds and gates its evaluation bar — block 26

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 26–26.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00222"></a>
## FND-00222: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 30

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `play-computer.js` registers a tag → constructor map:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 30–30.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00223"></a>
## FND-00223: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 32

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 32–44.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00224"></a>
## FND-00224: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 46

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`Al` is re-exported as internal `dt` (`play-computer.js @47381`, export map `dt as Al`) and
imported from the shared eager chunk (`import { dt as Al } from "./shared.eager.B4_eyo3T4t.chunk.js"`).
Registration goes through Chess.com's helper:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 46–48.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00225"></a>
## FND-00225: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 50

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
// shared.eager chunk @252125
function Ig(e, t) {
  typeof customElements < 'u' && !customElements.get(e) && customElements.define(e, t);
}
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 50–55.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00226"></a>
## FND-00226: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 57

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

and the app bootstrap hands that map to the runtime:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 57–57.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00227"></a>
## FND-00227: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 59

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
// play-computer.js @417180
function t6() {
  Uu(W3).mount(document.createElement("div"));
  tr({ clients: vL, controllers: N$, elements: l1, extensions: B3, hooks: {...} });
}
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 59–65.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00228"></a>
## FND-00228: 1. The rendering source of truth: `<wc-evaluation-bar>` — block 67

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[inferred]** The bar is a *custom element* whose class is reachable at runtime via
`customElements.get('wc-evaluation-bar')`, and whose constructor is the Svelte-ish class
`OSt extends K7 extends HTMLElement`.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 67–69.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00229"></a>
## FND-00229: 1.1 The component contract — block 73

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `shared.eager` @2,943,076 and following — the component's own methods:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 73–73.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00230"></a>
## FND-00230: 1.1 The component contract — block 75

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 75–125.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00231"></a>
## FND-00231: 1.1 The component contract — block 127

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** Attribute names come from `W7.ObservedAttributes` (shared.eager @2,892,030):
`board-id`, `engine-name`, `game-id`, `update-manually`, plus `is-display-engine-details`,
`is-default-fen-automatic`, `display-type`, `is-active`.
Base class `K7` resolves its board with `document.getElementById(this.boardId)` and only calls
`boardReady()` once that element exposes a `.game` object (@2,893,531).

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 127–131.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00232"></a>
## FND-00232: 1.1 The component contract — block 133

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** Event bus is a module-local emitter, not a DOM event:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 133–133.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00233"></a>
## FND-00233: 1.1 The component contract — block 135

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
// shared.eager @2,940,467 region
pSt, N9 = (VJ(), { createEventEmitter: pSt } = zJ, pSt());
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 135–138.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00234"></a>
## FND-00234: 1.1 The component contract — block 140

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** Settings store and its persistence (same region):

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 140–140.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00235"></a>
## FND-00235: 1.1 The component contract — block 142

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 142–158.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00236"></a>
## FND-00236: 1.1 The component contract — block 160

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Consequence [inferred]:** the bar takes an *object* shaped
`{ score: <pawns, white POV>, mateIn?: number, stalemate?: boolean, tablebaseOutcome?: string,
multipv?: number, depth?: number }`, and there are two ways to drive it: emit on the private
bus, or call the instance method `onEvaluationUpdate(payload)` directly. The method is a
normal prototype method, so the second route needs no access to minified module scope.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 160–164.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00237"></a>
## FND-00237: 1.1 The component contract — block 166

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 166–166.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00238"></a>
## FND-00238: 2. The score maths (what any substitute implementation must reproduce) — block 170

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `shared.eager` @2,657,030:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 170–170.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00239"></a>
## FND-00239: 2. The score maths (what any substitute implementation must reproduce) — block 172

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
G_ = { BAR_MARGIN: 10, BAR_WIDTH: 20, DEFAULT_BAR_PERCENTAGE: 50,
       DEFAULT_LOADING_COLOR: '#769656', SCORE_CALC_COEFFICIENT: 45, SCORE_CAP: 4 }
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 172–175.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00240"></a>
## FND-00240: 2. The score maths (what any substitute implementation must reproduce) — block 177

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `shared.eager` @2,901,384:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 177–177.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00241"></a>
## FND-00241: 2. The score maths (what any substitute implementation must reproduce) — block 179

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 179–211.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00242"></a>
## FND-00242: 2. The score maths (what any substitute implementation must reproduce) — block 213

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Notes for reimplementers **[inferred]**:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 213–213.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00243"></a>
## FND-00243: 2. The score maths (what any substitute implementation must reproduce) — block 215

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

* `yyt` decides the *percentage* from the **sign of `score`**, even for mate — so a mate
  payload must carry a signed `score` (±4 is what the engine wrapper produces) or the bar
  renders full for the wrong side.
* `dyt` (the number printed *on* the bar) is magnitude-only; the signed value lives in the
  hover element (`n9`/`myt`).
* Everything is White point of view. A UCI `score cp` is side-to-move POV and must be negated
  when Black is to move.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 215–221.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00244"></a>
## FND-00244: 2. The score maths (what any substitute implementation must reproduce) — block 223

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The extension's `test/logic.test.mjs` transcribes these functions verbatim and asserts the
shipped `page-agent.js` reproduces them — 60/60 checks pass, including mate, stalemate and
tablebase cases.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 223–225.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00245"></a>
## FND-00245: 2. The score maths (what any substitute implementation must reproduce) — block 227

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 227–227.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00246"></a>
## FND-00246: 3. The visibility gate — block 231

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `play-computer.js` @386,899:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 231–231.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00247"></a>
## FND-00247: 3. The visibility gate — block 233

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
function H2() { return cu().loaded && Fe().evaluationBar }
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 233–235.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00248"></a>
## FND-00248: 3. The visibility gate — block 237

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** the same module feeds that predicate into the page's dependency-injection
context (@386,899 region):

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 237–238.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00249"></a>
## FND-00249: 3. The visibility gate — block 240

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 240–250.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00250"></a>
## FND-00250: 3. The visibility gate — block 252

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

So the bar is shown when **the engine client reports `loaded`** *and* **the assistance
setting `evaluationBar` is on**. `shouldDisableEvaluationIfPlaying` returning `false` on this
page means the "kill evaluation while playing" path is *not* what suppresses the bar — the
`cu().loaded` term is.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 252–255.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00251"></a>
## FND-00251: 3. The visibility gate — block 257

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** the engine client is behind a lazy loader:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 257–257.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00252"></a>
## FND-00252: 3. The visibility gate — block 259

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
// play-computer.js @386,899 region
R2 = es({
  triggers: _m() ? [() => $c(et)] : [],
  shouldLoad: () => _m() && !bn(),
  loader: () => O(() => e(() => import('./client.03a446da.Bw4BRYjdl2.chunk.js'), ...))
});
B2 = Fl({ clients: [R2], context: td });
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 259–267.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00253"></a>
## FND-00253: 3. The visibility gate — block 269

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`_m()` and `bn()` are defined in the play shared chunk's module graph; REA did not resolve
them (`[unknown]`). What is observable is the effect: on a fresh bot game the engine chunk is
not fetched until the loader's triggers fire, and until then `cu().loaded` is `false`, so
`H2()` is `false` even with the setting on.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 269–272.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00254"></a>
## FND-00254: 3.1 The setting is per game mode — and two modes already turn it on — block 276

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `shared.eager` @1,732,753:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 276–276.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00255"></a>
## FND-00255: 3.1 The setting is per game mode — and two modes already turn it on — block 278

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 278–291.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00256"></a>
## FND-00256: 3.1 The setting is per game mode — and two modes already turn it on — block 293

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[inferred]** In a bot game the eval bar is a first-class *assistance* feature: the
**Assisted** and **Coach** presets ship with `evaluationBar: true`. The bar is not hidden
because "evaluation is forbidden during play" — it is hidden because *that preset* disables
it and/or because the engine client has not loaded yet. The UI string is the same one the
settings modal renders (@218,655):

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 293–297.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00257"></a>
## FND-00257: 3.1 The setting is per game mode — and two modes already turn it on — block 299

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
evaluationBar: { label: 'Evaluation Bar', tooltip: 'See what side is winning.' }
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 299–301.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00258"></a>
## FND-00258: 3.1 The setting is per game mode — and two modes already turn it on — block 303

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

This matches the reported `shouldDisableEvaluationIfPlaying: () => !1`.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 303–303.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00259"></a>
## FND-00259: 3.1 The setting is per game mode — and two modes already turn it on — block 305

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 305–305.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00260"></a>
## FND-00260: 4. The engine stack — block 309

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** `analysis.js` @~121,000 (engine bootstrap):

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 309–309.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00261"></a>
## FND-00261: 4. The engine stack — block 311

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 311–325.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00262"></a>
## FND-00262: 4. The engine stack — block 327

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[inferred]** the client is a UCI-shaped worker wrapper — `send(cmd, cb)`, `stopFast(cb, ms)`,
custom verbs such as `fetch threats` — with a local-engine variant behind the same interface.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 327–328.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00263"></a>
## FND-00263: 4. The engine stack — block 330

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** engine asset catalogue (`analysis-shared.eager` @~133,018 and the string map
@~295,326). Torch:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 330–331.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00264"></a>
## FND-00264: 4. The engine stack — block 333

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
nP = {
  full: { multiThreaded:  { loader: '/r2/assets-chess-engine/Torch/torch-2-85193a7.js' },
          singleThreaded: { loader: '/r2/assets-chess-engine/Torch/torch-2-single-697050e.js' } },
  lite: { multiThreaded:  { loader: '/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js' },
          singleThreaded: { loader: '/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js' } }
}
```

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 333–340.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00265"></a>
## FND-00265: 4. The engine stack — block 342

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Stockfish (same table, `iP[QN.STOCKFISH_NNUE]`): display name `Stockfish 16.1`, `66MB`,
`paths.settings: { Threads: '1' }`, `pathToBook` = `bundles/app/js/engine/books/eco.json`
unless the `analysis_engine_skip_book` feature flag is set.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 342–344.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00266"></a>
## FND-00266: 4. The engine stack — block 346

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Files shipped under `bundles/app/js/engine/`: `stockfish-nnue-15.1{,-no-Worker,-no-simd}.{js,wasm}`,
`stockfish-nnue-16{,-no-Worker,-no-simd,-single}.{js,wasm}`, `stockfish{,-single}.{js,wasm}`,
`stockfish.asm.js`, `torch{,-lite}.{js,wasm}` and NNUE nets `nn-5af11540bbfe.nnue`,
`nn-ad9b42354671.nnue`. **These are byte-identical filenames to the `stockfish@16.0.0` npm
build**, i.e. Chess.com ships that upstream Emscripten build with its multi-threaded /
single-threaded / no-SIMD fallbacks.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 346–351.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00267"></a>
## FND-00267: 4. The engine stack — block 353

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**[observed]** page-level engine settings live in `localStorage['analysis_engine_settings']`
(see §1.1), default depth 20, 3 PVs, 5 s time limit.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 353–354.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00268"></a>
## FND-00268: 4. The engine stack — block 356

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 356–356.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00269"></a>
## FND-00269: 5. What this means for a browser extension — block 360

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Goal restated:** make the *native* bar visible and correct during a game, without writing a
new bar.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 360–361.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00270"></a>
## FND-00270: 5. What this means for a browser extension — block 363

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Three levers exist, in increasing order of fragility:

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 363–363.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00271"></a>
## FND-00271: 5. What this means for a browser extension — block 365

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 365–376.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00272"></a>
## FND-00272: 5. What this means for a browser extension — block 378

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The extension in `chess-eval-bar/` uses **1 → 2**, and falls back to markup that reuses the
same `evaluation-bar-*` classes and maths if the tag is ever unregistered.

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 378–379.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00273"></a>
## FND-00273: 5. What this means for a browser extension — block 381

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Unknowns / limits of this analysis**

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 381–381.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00274"></a>
## FND-00274: 5. What this means for a browser extension — block 383

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Lines 383–392.

**Source references:** SRC-2048  
**URL references:** None independently associated  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.
