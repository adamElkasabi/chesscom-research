# historical_documentation — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00001"></a>
## FND-00001: Install this update — block 5

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

1. Extract the v0.1.7 update ZIP into your existing unpacked extension folder
   (the folder containing manifest.json). Replace files when prompted; preserve
   the other existing files and engines.
2. Open `chrome://extensions` and click **Reload** on this extension.
3. Refresh the Chess.com tab and rerun Game Review.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 5–9.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00002"></a>
## FND-00002: Install this update — block 11

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The Chrome extension version is 0.1.7. The on-page hook still reports 0.1.6:
its working quota/socket code is deliberately unchanged, byte for byte.
This ZIP is an update, not a standalone extension installation.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 11–13.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00003"></a>
## FND-00003: What changed — block 17

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The old review builder independently searched Stockfish positions, applied
centipawn-loss thresholds for labels, used a homemade accuracy curve, and
estimated ratings with a formula and a floor of 400. Those calculations have
been removed from the production review builder.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 17–20.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00004"></a>
## FND-00004: What changed — block 22

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The extension now calls Chess.com's bundled CEE NewGame + GameReview features
and wraps the result in the real CEAC response envelope. It preserves native
classifications, accuracy, tallies, rating output, speech hashes, explanation
markings, opening, result, and PGN output. It does not substitute fixture
results or make game-specific corrections.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 22–26.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00005"></a>
## FND-00005: What changed — block 28

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The bundled CEE currently omits the optional newer gameRatingV2 field. For the
page's V2-enabled rating display, the adapter copies CEE's effectiveRating
(legacy Game Rating) into that field. It does not calculate a new rating.
Diagnostics record the source as effectiveRating.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 28–31.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00006"></a>
## FND-00006: What changed — block 33

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Whole-game CEE calls may take a while without intermediate progress. The
extension sends keepalive progress frames at the last known progress rather
than claiming a made-up percentage.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 33–35.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00007"></a>
## FND-00007: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 39

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Metric | Old extension (user report) | v0.1.7 local test | Chess.com target |
| --- | ---: | ---: | ---: |
| White accuracy | 57.5 | 60.0 | 71.7 |
| Black accuracy | 88.8 | 95.5 | 99.0 |
| White Game Rating | 400 | 300 | 100 |
| Black Game Rating | 400 | 1000 | 1000 |
| White blunders | 4 | 1 | 1 |
| Black Great moves | 2 | 1 | 1 |
| Black mistakes | 2 | 0 | 0 |

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 39–47.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00008"></a>
## FND-00008: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 49

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Full classification comparison:

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 49–49.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00009"></a>
## FND-00009: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 51

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Category | White local / target | Black local / target |
| --- | ---: | ---: |
| Brilliant | 0 / 0 | 0 / 0 |
| Great | 0 / 0 | 1 / 1 |
| Book | 2 / 2 | 2 / 2 |
| Best | 0 / 0 | 4 / 2 |
| Excellent | 0 / 4 | 2 / 5 |
| Good | 2 / 1 | 1 / 0 |
| Inaccuracy | 1 / 0 | 0 / 0 |
| Mistake | 4 / 2 | 0 / 0 |
| Miss | 0 / 0 | 0 / 0 |
| Blunder | 1 / 1 | 0 / 0 |

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 51–62.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00010"></a>
## FND-00010: Still open — block 66

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- Exact cloud parity is NOT achieved. The page requests TORCH_HUMAN (12), but
  this local CEE search returns TORCH_3 (11). Scores retain their actual engine
  ID, and diagnostics report the mismatch rather than silently relabeling it.
- White's rating above is the native legacy rating, not a verified V2 rating.
- Coach audio playback is not confirmed fixed. Native audio hashes are now
  retained (29/29 speech sentences in the example), but this update is focused
  on the evaluation/classification pipeline.
- Threat-arrow fetching and selected-coach asset loading are separate work.
- Native CEE output may omit report categories unavailable to this local build;
  the adapter does not invent replacement category statistics.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 66–75.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00011"></a>
## FND-00011: Tests — block 79

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- `node test/quota-test.mjs`: exhausted quota + uncached review gate regressions.
- `node test/hook-test.mjs`: brand-checked WebSocket regression suite.
- `node test/run-test.mjs`: genuine CEE wasm + response codec + example comparison.
- `node test/browser-cee-test.mjs`: actual Chromium extension Worker/wasm test,
  plus hook -> content bridge -> service worker -> real offscreen document ->
  CEE -> success, on a simulated Chess.com page with quota exhausted and no
  cached review. Requires Playwright and Chromium.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 79–85.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00012"></a>
## FND-00012: Tests — block 87

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

These tests passed in the development environment. The live Chess.com frontend
still needs user confirmation. The quota hook was already confirmed working
by the user in v0.1.6 and is unchanged here.

### Evidence

- **SRC-0016** `chess-local-review-v0.1.7-cee-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/b083363e77f52270e4e61973949eeea53c339fed097dce44501b8536cc19b27c.md)
  Lines 87–89.

**Source references:** SRC-0016  
**URL references:** None independently associated  
**Related findings:** FND-00001, FND-00002, FND-00003

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00013"></a>
## FND-00013: v0.1.8 — hide debug card only — block 5

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The bottom-left debug card is disabled. Diagnostics still appear in Chrome
DevTools Console with the `[local-review]` prefix. Review calculations, quota
handling, engine files, speech/audio, and Chess.com's review UI are unchanged.
No experimental Torch Human or engine-tuning changes are included.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 5–8.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00014"></a>
## FND-00014: v0.1.8 — hide debug card only — block 10

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Extract the v0.1.8 hide-debug update ZIP **over your existing working extension
folder**, replacing the included files. Do not delete the existing folder or
its engine files. Reload the extension at `chrome://extensions`, then refresh
all open Chess.com tabs to remove the old card. This is a small update ZIP,
not a standalone installation. The hook's internal version label remains
0.1.6 because the core socket/quota implementation is still that version.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 10–15.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00015"></a>
## FND-00015: v0.1.8 — hide debug card only — block 17

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 17–17.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00016"></a>
## FND-00016: Install this update — block 23

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

1. Extract the v0.1.7 update ZIP into your existing unpacked extension folder
   (the folder containing manifest.json). Replace files when prompted; preserve
   the other existing files and engines.
2. Open `chrome://extensions` and click **Reload** on this extension.
3. Refresh the Chess.com tab and rerun Game Review.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 23–27.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00017"></a>
## FND-00017: Install this update — block 29

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The Chrome extension version is 0.1.7. The on-page hook still reports 0.1.6:
its working quota/socket code is deliberately unchanged, byte for byte.
This ZIP is an update, not a standalone extension installation.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 29–31.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00018"></a>
## FND-00018: What changed — block 35

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The old review builder independently searched Stockfish positions, applied
centipawn-loss thresholds for labels, used a homemade accuracy curve, and
estimated ratings with a formula and a floor of 400. Those calculations have
been removed from the production review builder.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 35–38.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00019"></a>
## FND-00019: What changed — block 40

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The extension now calls Chess.com's bundled CEE NewGame + GameReview features
and wraps the result in the real CEAC response envelope. It preserves native
classifications, accuracy, tallies, rating output, speech hashes, explanation
markings, opening, result, and PGN output. It does not substitute fixture
results or make game-specific corrections.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 40–44.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00020"></a>
## FND-00020: What changed — block 46

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The bundled CEE currently omits the optional newer gameRatingV2 field. For the
page's V2-enabled rating display, the adapter copies CEE's effectiveRating
(legacy Game Rating) into that field. It does not calculate a new rating.
Diagnostics record the source as effectiveRating.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 46–49.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00021"></a>
## FND-00021: What changed — block 51

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Whole-game CEE calls may take a while without intermediate progress. The
extension sends keepalive progress frames at the last known progress rather
than claiming a made-up percentage.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 51–53.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00022"></a>
## FND-00022: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 57

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Metric | Old extension (user report) | v0.1.7 local test | Chess.com target |
| --- | ---: | ---: | ---: |
| White accuracy | 57.5 | 60.0 | 71.7 |
| Black accuracy | 88.8 | 95.5 | 99.0 |
| White Game Rating | 400 | 300 | 100 |
| Black Game Rating | 400 | 1000 | 1000 |
| White blunders | 4 | 1 | 1 |
| Black Great moves | 2 | 1 | 1 |
| Black mistakes | 2 | 0 | 0 |

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 57–65.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00023"></a>
## FND-00023: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 67

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Full classification comparison:

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 67–67.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00024"></a>
## FND-00024: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 69

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Category | White local / target | Black local / target |
| --- | ---: | ---: |
| Brilliant | 0 / 0 | 0 / 0 |
| Great | 0 / 0 | 1 / 1 |
| Book | 2 / 2 | 2 / 2 |
| Best | 0 / 0 | 4 / 2 |
| Excellent | 0 / 4 | 2 / 5 |
| Good | 2 / 1 | 1 / 0 |
| Inaccuracy | 1 / 0 | 0 / 0 |
| Mistake | 4 / 2 | 0 / 0 |
| Miss | 0 / 0 | 0 / 0 |
| Blunder | 1 / 1 | 0 / 0 |

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 69–80.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00025"></a>
## FND-00025: Still open — block 84

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- Exact cloud parity is NOT achieved. The page requests TORCH_HUMAN (12), but
  this local CEE search returns TORCH_3 (11). Scores retain their actual engine
  ID, and diagnostics report the mismatch rather than silently relabeling it.
- White's rating above is the native legacy rating, not a verified V2 rating.
- Coach audio playback is not confirmed fixed. Native audio hashes are now
  retained (29/29 speech sentences in the example), but this update is focused
  on the evaluation/classification pipeline.
- Threat-arrow fetching and selected-coach asset loading are separate work.
- Native CEE output may omit report categories unavailable to this local build;
  the adapter does not invent replacement category statistics.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 84–93.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00026"></a>
## FND-00026: Tests — block 97

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- `node test/quota-test.mjs`: exhausted quota + uncached review gate regressions.
- `node test/hook-test.mjs`: brand-checked WebSocket regression suite.
- `node test/run-test.mjs`: genuine CEE wasm + response codec + example comparison.
- `node test/browser-cee-test.mjs`: actual Chromium extension Worker/wasm test,
  plus hook -> content bridge -> service worker -> real offscreen document ->
  CEE -> success, on a simulated Chess.com page with quota exhausted and no
  cached review. Requires Playwright and Chromium.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 97–103.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00027"></a>
## FND-00027: Tests — block 105

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

These tests passed in the development environment. The live Chess.com frontend
still needs user confirmation. The quota hook was already confirmed working
by the user in v0.1.6 and is unchanged here.

### Evidence

- **SRC-0020** `chess-local-review-v0.1.8-hide-debug-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/875c24fb52697f44865b9a42705da20558e1eb69912a27f7d8fd7794840477fb.md)
  Lines 105–107.

**Source references:** SRC-0020  
**URL references:** None independently associated  
**Related findings:** FND-00013, FND-00014, FND-00015

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00028"></a>
## FND-00028: v0.1.9 — measured-duration progress estimate — block 5

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The existing percentage bar now estimates progress from measured, successful
review durations on this device, scaled by the number of positions in the game.
Only reviews with identical search settings are compared. Up to seven nearby
lengths are used and their scaled durations are combined with a median, reducing
the influence of unusually slow runs. The latest 40 successful samples are kept
locally; only move counts, search-setting keys, and durations are stored.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 5–10.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00029"></a>
## FND-00029: v0.1.9 — measured-duration progress estimate — block 12

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Calibration:** the first successful review for each search setting still shows
coarse 0% / 2% / 100% progress. It provides the real timing measurement for later
reviews. There is no made-up first-run timing. Samples survive extension reloads
when browser local storage is available; otherwise learning is memory-only.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 12–15.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00030"></a>
## FND-00030: v0.1.9 — measured-duration progress estimate — block 17

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

After calibration, estimated progress updates once per second. This is a
wall-clock estimate, not a count of engine positions actually completed.
Different positions, CPU load, and game length can make it inaccurate. It caps
at 95% if the review exceeds its predicted time and reaches 100% only when CEE
has produced the result. Failed or cancelled reviews do not train the model.
Console diagnostics explicitly identify the estimate and show the predicted
duration and sample count; Chess.com's existing percentage UI is retained.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 17–23.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00031"></a>
## FND-00031: v0.1.9 — measured-duration progress estimate — block 25

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The debug card remains hidden. Analysis settings, scores, quota handling, native
audio hashes, and the engine assets are unchanged. No research tuning or
experimental Torch Human changes are included.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 25–27.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00032"></a>
## FND-00032: Install v0.1.9 — block 31

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

1. Extract the v0.1.9 measured-progress update ZIP **over the existing working
   extension folder**, replacing the included files. Keep all other files.
2. Reload the extension at `chrome://extensions`.
3. Refresh Chess.com. Finish one review to calibrate, then run another review
   using the same analysis strength to see the measured-time estimate.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 31–35.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00033"></a>
## FND-00033: Install v0.1.9 — block 37

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

This small update is not a standalone extension installation.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 37–37.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00034"></a>
## FND-00034: Install v0.1.9 — block 39

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 39–39.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00035"></a>
## FND-00035: v0.1.8 — hide debug card only — block 45

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The bottom-left debug card is disabled. Diagnostics still appear in Chrome
DevTools Console with the `[local-review]` prefix. Review calculations, quota
handling, engine files, speech/audio, and Chess.com's review UI are unchanged.
No experimental Torch Human or engine-tuning changes are included.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 45–48.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00036"></a>
## FND-00036: v0.1.8 — hide debug card only — block 50

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Extract the v0.1.8 hide-debug update ZIP **over your existing working extension
folder**, replacing the included files. Do not delete the existing folder or
its engine files. Reload the extension at `chrome://extensions`, then refresh
all open Chess.com tabs to remove the old card. This is a small update ZIP,
not a standalone installation. The hook's internal version label remains
0.1.6 because the core socket/quota implementation is still that version.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 50–55.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00037"></a>
## FND-00037: v0.1.8 — hide debug card only — block 57

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 57–57.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00038"></a>
## FND-00038: Install this update — block 63

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

1. Extract the v0.1.7 update ZIP into your existing unpacked extension folder
   (the folder containing manifest.json). Replace files when prompted; preserve
   the other existing files and engines.
2. Open `chrome://extensions` and click **Reload** on this extension.
3. Refresh the Chess.com tab and rerun Game Review.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 63–67.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00039"></a>
## FND-00039: Install this update — block 69

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The Chrome extension version is 0.1.7. The on-page hook still reports 0.1.6:
its working quota/socket code is deliberately unchanged, byte for byte.
This ZIP is an update, not a standalone extension installation.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 69–71.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00040"></a>
## FND-00040: What changed — block 75

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The old review builder independently searched Stockfish positions, applied
centipawn-loss thresholds for labels, used a homemade accuracy curve, and
estimated ratings with a formula and a floor of 400. Those calculations have
been removed from the production review builder.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 75–78.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00041"></a>
## FND-00041: What changed — block 80

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The extension now calls Chess.com's bundled CEE NewGame + GameReview features
and wraps the result in the real CEAC response envelope. It preserves native
classifications, accuracy, tallies, rating output, speech hashes, explanation
markings, opening, result, and PGN output. It does not substitute fixture
results or make game-specific corrections.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 80–84.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00042"></a>
## FND-00042: What changed — block 86

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The bundled CEE currently omits the optional newer gameRatingV2 field. For the
page's V2-enabled rating display, the adapter copies CEE's effectiveRating
(legacy Game Rating) into that field. It does not calculate a new rating.
Diagnostics record the source as effectiveRating.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 86–89.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00043"></a>
## FND-00043: What changed — block 91

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Whole-game CEE calls may take a while without intermediate progress. The
extension sends keepalive progress frames at the last known progress rather
than claiming a made-up percentage.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 91–93.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00044"></a>
## FND-00044: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 97

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Metric | Old extension (user report) | v0.1.7 local test | Chess.com target |
| --- | ---: | ---: | ---: |
| White accuracy | 57.5 | 60.0 | 71.7 |
| Black accuracy | 88.8 | 95.5 | 99.0 |
| White Game Rating | 400 | 300 | 100 |
| Black Game Rating | 400 | 1000 | 1000 |
| White blunders | 4 | 1 | 1 |
| Black Great moves | 2 | 1 | 1 |
| Black mistakes | 2 | 0 | 0 |

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 97–105.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00045"></a>
## FND-00045: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 107

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Full classification comparison:

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 107–107.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00046"></a>
## FND-00046: Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 109

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Category | White local / target | Black local / target |
| --- | ---: | ---: |
| Brilliant | 0 / 0 | 0 / 0 |
| Great | 0 / 0 | 1 / 1 |
| Book | 2 / 2 | 2 / 2 |
| Best | 0 / 0 | 4 / 2 |
| Excellent | 0 / 4 | 2 / 5 |
| Good | 2 / 1 | 1 / 0 |
| Inaccuracy | 1 / 0 | 0 / 0 |
| Mistake | 4 / 2 | 0 / 0 |
| Miss | 0 / 0 | 0 / 0 |
| Blunder | 1 / 1 | 0 / 0 |

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 109–120.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00047"></a>
## FND-00047: Still open — block 124

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- Exact cloud parity is NOT achieved. The page requests TORCH_HUMAN (12), but
  this local CEE search returns TORCH_3 (11). Scores retain their actual engine
  ID, and diagnostics report the mismatch rather than silently relabeling it.
- White's rating above is the native legacy rating, not a verified V2 rating.
- Coach audio playback is not confirmed fixed. Native audio hashes are now
  retained (29/29 speech sentences in the example), but this update is focused
  on the evaluation/classification pipeline.
- Threat-arrow fetching and selected-coach asset loading are separate work.
- Native CEE output may omit report categories unavailable to this local build;
  the adapter does not invent replacement category statistics.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 124–133.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00048"></a>
## FND-00048: Tests — block 137

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- `node test/quota-test.mjs`: exhausted quota + uncached review gate regressions.
- `node test/hook-test.mjs`: brand-checked WebSocket regression suite.
- `node test/run-test.mjs`: genuine CEE wasm + response codec + example comparison.
- `node test/browser-cee-test.mjs`: actual Chromium extension Worker/wasm test,
  plus hook -> content bridge -> service worker -> real offscreen document ->
  CEE -> success, on a simulated Chess.com page with quota exhausted and no
  cached review. Requires Playwright and Chromium.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 137–143.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00049"></a>
## FND-00049: Tests — block 145

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

These tests passed in the development environment. The live Chess.com frontend
still needs user confirmation. The quota hook was already confirmed working
by the user in v0.1.6 and is unchanged here.

### Evidence

- **SRC-0027** `chess-local-review-v0.1.9-measured-progress-update.zip!/README.md` — [preserved redacted evidence](../evidence/text/cbc034528976a1318d02ecaeb8c7f5bcc901c1aacf89a205d39c0e3cd9413f64.md)
  Lines 145–147.

**Source references:** SRC-0027, SRC-0028  
**URL references:** None independently associated  
**Related findings:** FND-00028, FND-00029, FND-00030

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00050"></a>
## FND-00050: Confirmed execution, not just strings — block 4

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Using the shipped explanation-engine.wasm (CEE 1.130.285), isolated RunSearch feature 29 accepted torchSearchMode human and completed a 1000-node opening-position search. Both control and human probes completed with progress=1. Fetch was replaced with a rejecting function; neither made a fetch attempt. The engine was executed locally through its Node wrapper, not in a browser UI, so this is local WASM execution proof, not a Chrome Game Review integration test.

### Evidence

- **SRC-0871** `research/refinement/torch-human-client-verdict.md` — [preserved redacted evidence](../evidence/text/adfa0d5be5ca5cab8b234826bda61c5923eafc675d4ee1f4ca3ea879764f09f4.md)
  Lines 4–4.

**Source references:** SRC-0871  
**URL references:** None independently associated  
**Related findings:** FND-00051, FND-00052

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00051"></a>
## FND-00051: Confirmed execution, not just strings — block 6

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Both responses log `engine: Torch master-20260925-87ee25a`. Ordinary mode returns score +17cp, depth 6; human mode +18cp, depth 5, with different returned variations. Decoded internal API logs show ordinary `go nodes 1000 searchmoves ...` versus human `go nodes 1000 pvtrees ... rating 2100 ... ep_loss_margin 0.02`. No errors/warnings recorded. The human request is therefore not simply ignored. Low-level evaluations retain engine enum 11; this alone does not prove the human mode was disabled.

### Evidence

- **SRC-0871** `research/refinement/torch-human-client-verdict.md` — [preserved redacted evidence](../evidence/text/adfa0d5be5ca5cab8b234826bda61c5923eafc675d4ee1f4ca3ea879764f09f4.md)
  Lines 6–6.

**Source references:** SRC-0871  
**URL references:** None independently associated  
**Related findings:** FND-00050, FND-00052

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00052"></a>
## FND-00052: Confirmed execution, not just strings — block 8

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Evidence files: results/probe-normal-offline.json, results/probe-human-offline.json; probe-normal-decoded-log.txt, probe-human-decoded-log.txt; human-probe.mjs and configs/probe-*.json. Human-no-Maia also completed in a separate unblocked-fetch test, with the same aggregate score as human.

### Evidence

- **SRC-0871** `research/refinement/torch-human-client-verdict.md` — [preserved redacted evidence](../evidence/text/adfa0d5be5ca5cab8b234826bda61c5923eafc675d4ee1f4ca3ea879764f09f4.md)
  Lines 8–8.

**Source references:** SRC-0871  
**URL references:** None independently associated  
**Related findings:** FND-00050, FND-00051

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00053"></a>
## FND-00053: Website Game Review routing — block 11

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Saved analysis frontend shared.eager.BOGLllgUUR.chunk.js:
- A4e chooses TORCH_HUMAN (12) when web_analysis_torch_human_v2 is enabled and selected engine is not Stockfish16.
- W4e serializes that engine in a CEAC GameReviewRequest with Fast/Standard/etc; disables game-state cache for Torch Human.
- x3e encodes it and sends over WebSocket via S3e to server selected by O4e, normally wss://analysis.chess.com:443/v2/game-review.
- C3e processes responses from that server.
Thus the inspected website full-review path requests Torch Human from a server; it is not proof of browser-side full Torch Human Game Review. Local worker loading for quick analysis/other features must not be conflated with this route.

### Evidence

- **SRC-0871** `research/refinement/torch-human-client-verdict.md` — [preserved redacted evidence](../evidence/text/adfa0d5be5ca5cab8b234826bda61c5923eafc675d4ee1f4ca3ea879764f09f4.md)
  Lines 11–16.

**Source references:** SRC-0871  
**URL references:** <wss://analysis.chess.com:443/v2/game-review>  
**Related findings:** FND-00050, FND-00051, FND-00052

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00054"></a>
## FND-00054: Remaining limitations — block 19

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

No successful full human-mode Game Review, no parity with cloud scores, no confirmed separate humanLine or Maia prediction output. Internal feature288 PVtrees probes with rating100 still timed out even at1000nodes. Normal and human EvaluateGame54 earlier aborted. Do not promote those failures to evidence the local RunSearch mode is unsupported.

### Evidence

- **SRC-0871** `research/refinement/torch-human-client-verdict.md` — [preserved redacted evidence](../evidence/text/adfa0d5be5ca5cab8b234826bda61c5923eafc675d4ee1f4ca3ea879764f09f4.md)
  Lines 19–19.

**Source references:** SRC-0871  
**URL references:** None independently associated  
**Related findings:** FND-00050, FND-00051, FND-00052

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00055"></a>
## FND-00055: Remaining limitations — block 21

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Extension production files unchanged; all five working-v0.1.7.sha256 checks passed after this investigation.

### Evidence

- **SRC-0871** `research/refinement/torch-human-client-verdict.md` — [preserved redacted evidence](../evidence/text/adfa0d5be5ca5cab8b234826bda61c5923eafc675d4ee1f4ca3ea879764f09f4.md)
  Lines 21–21.

**Source references:** SRC-0871  
**URL references:** None independently associated  
**Related findings:** FND-00050, FND-00051, FND-00052

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00056"></a>
## FND-00056: Reference-game comparison: Chess.com, extension, local Torch human mode — block 3

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Game: [PUBLIC_PLAYER_HANDLE_REDACTED] (White) vs [PUBLIC_PLAYER_HANDLE_REDACTED] (Black), live game 186934806892, 20 plies, 0–1. This is the original reference, not the newer example link used for source inspection.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 3–3.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00057"></a>
## FND-00057: Reference-game comparison: Chess.com, extension, local Torch human mode — block 5

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

All paired values below are **White / Black**. Chess.com figures are the user's supplied reference, not newly fetched scores. Extension figures are the saved working v0.1.7 baseline. The human-mode column is a newly executed, research-only pipeline using native engine outputs.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 5–5.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00058"></a>
## FND-00058: Reference-game comparison: Chess.com, extension, local Torch human mode — block 7

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Metric (White / Black) | Chess.com reference | Working extension v0.1.7 | Local Torch human mode (experimental) |
| --- | --- | --- | --- |
| Accuracy (%) | 71.7 / 99.0 | 60.0 / 95.5 | 59.0 / 95.4 |
| Game Rating | 100 / 1000 | 300 / 1000 | 400 / 1000 |
| Brilliant | 0 / 0 | 0 / 0 | 0 / 0 |
| Great | 0 / 1 | 0 / 1 | 0 / 1 |
| Book | 2 / 2 | 2 / 2 | 2 / 2 |
| Best | 0 / 2 | 0 / 4 | 0 / 4 |
| Excellent | 4 / 5 | 0 / 2 | 0 / 2 |
| Good | 1 / 0 | 2 / 1 | 1 / 1 |
| Inaccuracy | 0 / 0 | 1 / 0 | 1 / 0 |
| Mistake | 2 / 0 | 4 / 0 | 6 / 0 |
| Miss | 0 / 0 | 0 / 0 | 0 / 0 |
| Blunder | 1 / 0 | 1 / 0 | 0 / 0 |

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 7–20.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00059"></a>
## FND-00059: What this experiment verifies — block 23

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- Native GetGameReviewEvaluations feature79 with Fast strength and torchSearchMode.human was run at each of 21 game points (initial position plus 20 plies).
- All 21 calls completed with progress=1. The logs contain 20 human PV-tree searches (the terminal position needs no search), as well as auxiliary ordinary searches.
- Returned evaluations were added through the native AddEvaluations API, and native GameReview feature42 generated the accuracy, ratings and classifications above.
- No additional engine-search commands were recorded during that final review-generation step. No fetch attempts or warnings were recorded. Local WASM execution used its Node wrapper; this was not an installed Chrome integration test.
- Normalize/Hash tuning from the earlier sweep was NOT applied. The production extension was not modified.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 23–27.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00060"></a>
## FND-00060: Important limits — block 30

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

This demonstrates a complete local experimental review built after human-mode evaluation, not parity with Chess.com's server-side Torch Human setup. Human-mode search logs use the internal default **rating 2100**; that has not been established as the server's configuration for this game. Underlying evaluation metadata remains engine11.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 30–30.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00061"></a>
## FND-00061: Important limits — block 32

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

A matched research control (the same explicit per-position preload pipeline without human mode) returned accuracy 60.2 / 96.1 and ratings 300 / 1000. It differs slightly from the direct production baseline. Therefore the human column versus production is a pipeline comparison, not a perfectly isolated one-setting benchmark. Relative to the matched control, human mode also moves both accuracy figures farther from the supplied reference.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 32–32.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00062"></a>
## FND-00062: Important limits — block 34

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Conclusion:** This local human-mode configuration does not improve the reference match. Keep v0.1.7 unchanged.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 34–34.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00063"></a>
## FND-00063: Move-by-move local classifications — block 37

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The supplied Chess.com reference contains aggregate counts, not a classification for each individual move, so no per-move Chess.com labels are invented here.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 37–37.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00064"></a>
## FND-00064: Move-by-move local classifications — block 39

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Move | Played | Working extension | Local human-mode experiment |
| --- | --- | --- | --- |
| 1. | d4 | Book | Book |
| 1... | d5 | Book | Book |
| 2. | e4 | Book | Book |
| 2... | dxe4 | Book | Book |
| 3. | Be2 | Good | Inaccuracy |
| 3... | Nf6 | Best | Best |
| 4. | Qd3 | Blunder | Mistake |
| 4... | exd3 | Great | Great |
| 5. | cxd3 | Good | Good |
| 5... | Nc6 | Best | Best |
| 6. | Bh5 | Mistake | Mistake |
| 6... | Nxd4 | Good | Good |
| 7. | Bd2 | Inaccuracy | Mistake |
| 7... | Nc2+ | Best | Best |
| 8. | Kf1 | Mistake | Mistake |
| 8... | Nxa1 | Excellent | Excellent |
| 9. | Bc1 | Mistake | Mistake |
| 9... | Qxd3+ | Excellent | Excellent |
| 10. | Ke1 | Mistake | Mistake |
| 10... | Nc2# | Best | Best |

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 39–60.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00065"></a>
## FND-00065: Raw evidence — block 63

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- research/refinement/results/comparison-human.json
- research/refinement/results/comparison-control.json
- research/refinement/results/baseline.json
- research/refinement/comparison-trial.mjs
- research/refinement/configs/comparison-human.json
- research/refinement/target.json

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Lines 63–68.

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00066"></a>
## FND-00066: Decision — block 4

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Keep the working v0.1.7 release unchanged.** Genuine embedded-engine settings can improve the newest reference, but the improvement does not consistently generalize. No new extension release is being claimed or substituted.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 4–4.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00067"></a>
## FND-00067: What was tested — block 7

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

An automated, bounded search executed **61 trial configurations**, including repeat checks. 53 returned complete numeric results; 8 failed or timed out. Separate holdout validation tested the two earlier fixtures. This is not an exhaustive search of every possible parameter value.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 7–7.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00068"></a>
## FND-00068: What was tested — block 9

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Trials run the actual bundled CEE/Torch WASM and preserve its returned scores. No fitted accuracy curves, rating correction formulas, per-game overrides, or relabeling of Torch as Torch Human were used. Search dimensions included supported UCI options, strength, classification version, node/depth limits, hash size, soft nodes, and embedded human-search paths. Raw failures remain recorded rather than treated as successful results.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 9–9.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00069"></a>
## FND-00069: Torch Human — block 12

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The shipped WASM contains TorchHuman/Maia/human-line machinery, and its protobuf descriptors expose human-mode requests. Saved Chess.com frontend code selects engine 12 for the Torch Human feature. This is strong evidence that it is an embedded mode, not evidence of a separately downloadable add-on.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 12–12.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00070"></a>
## FND-00070: Torch Human — block 14

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**I did not successfully activate Torch Human for a complete review.** Completed ordinary reviews still reported engine 11. A native human-PV-tree probe timed out; whole-game EvaluateGame probes aborted, including a normal-mode control. Those failures do not establish that Human is unsupported, and the normal control failure prevents attributing the abort specifically to Human.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 14–14.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00071"></a>
## FND-00071: Newest reference: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 17

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

All numbers below are White / Black. Target: accuracy **71.70 / 99.00**, ratings **100 / 1000**.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 17–17.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00072"></a>
## FND-00072: Newest reference: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 19

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Configuration | Accuracy | Game ratings |
|---|---:|---:|
| baseline | 59.96 / 95.46 | 300 / 1000 |
| uci-normalize-off | 65.74 / 99.14 | 100 / 1000 |
| normalized-UseSoftNodes-true | 66.40 / 98.71 | 100 / 1000 |
| normalized-Hash-64 | 64.80 / 98.81 | 100 / 1000 |
| normalized-standard | 66.58 / 99.24 | 100 / 1000 |

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 19–25.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00073"></a>
## FND-00073: Newest reference: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED] — block 27

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Fast strength was retained except in normalized-standard. The Normalize-off result reproduced exactly in two additional clean trials. Normalize-off plus Hash=64 also reproduced exactly in additional clean trials.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 27–27.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00074"></a>
## FND-00074: Classification trade-off — block 30

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Normalize=false plus Hash=64 was the best aggregate match under the declared comparison objective: sum of absolute accuracy errors + twice the summed absolute tally differences + summed rating errors / 100. This objective only ranks real outputs; it never generates review scores.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 30–30.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00075"></a>
## FND-00075: Classification trade-off — block 32

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

With Normalize=false, Hash=64, all Black classification tallies match the reference exactly: Book 2, Great 1, Best 2, Excellent 5, other categories 0. White remains wrong: Book 2, Excellent 2, Mistake 5, Blunder 1 (other categories 0), versus target Book 2, Excellent 4, Good 1, Mistake 2, Blunder 1. Its accuracy is worse than some other candidates, so there is no single winner on every metric.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 32–32.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00076"></a>
## FND-00076: Cross-game validation — block 35

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Each held-out game was evaluated under baseline, Normalize=false, and Normalize=false plus Hash=64. Player color followed the prior fixture setup; no player rating or PGN header was optimized.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 35–35.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00077"></a>
## FND-00077: Cross-game validation — block 37

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Targets:
- Human fixture: accuracy **76.80 / 70.20**, ratings **1350 / 600**.
- Bot fixture: accuracy **86.80 / 79.80**, ratings **1850 / 1500**.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 37–39.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00078"></a>
## FND-00078: Cross-game validation — block 41

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Fixture / configuration | Accuracy | Game ratings |
|---|---:|---:|
| human-game-baseline | 74.11 / 62.91 | 1250 / 600 |
| human-game-normalize-off | 69.13 / 62.28 | 1000 / 350 |
| human-game-refined-hash64 | 66.73 / 60.90 | 850 / 300 |
| example-game-baseline | 87.73 / 79.54 | 1850 / 1700 |
| example-game-normalize-off | 88.44 / 80.23 | 1850 / 1450 |
| example-game-refined-hash64 | 90.14 / 82.32 | 1900 / 1450 |

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 41–48.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00079"></a>
## FND-00079: Cross-game validation — block 50

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Turning normalization off worsened the earlier human fixture in both accuracy and ratings. The candidate therefore fails the cross-game promotion check, even though it helps the latest reference and improves some bot-game metrics. This is evidence against blindly applying it globally, not proof that all possible configurations have been ruled out.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 50–50.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00080"></a>
## FND-00080: Files and reproducibility — block 53

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

- trial.mjs: isolated actual-WASM trial runner.
- sweep.mjs: bounded search orchestrator and explicit ranking objective.
- configs/, results/: input configurations and raw outcomes, including errors.
- target.json: newest reference aggregate targets.
- leaderboard*.json and plan*.json: phase rankings/plans.
- validate.mjs, holdout/, holdout-validation.json: separate cross-game validation.
- torch-human-evidence.txt, uci-options.txt, wasm-descriptors/: native evidence.
- working-v0.1.7.sha256: checksums for protected production files.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 53–60.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00081"></a>
## FND-00081: Files and reproducibility — block 62

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Commands from the project root:

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 62–62.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00082"></a>
## FND-00082: Files and reproducibility — block 64

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```sh
CONCURRENCY=1 node research/refinement/sweep.mjs
PHASE=2 CONCURRENCY=1 node research/refinement/sweep.mjs
PHASE=3 CONCURRENCY=1 node research/refinement/sweep.mjs
node research/refinement/validate.mjs
node research/refinement/trial.mjs CONFIG.json OUTPUT.json
sha256sum -c research/refinement/working-v0.1.7.sha256
```

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 64–71.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00083"></a>
## FND-00083: Files and reproducibility — block 73

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Existing sweep results are reused. Run one engine trial at a time: parallel WASM reviews exhausted sandbox resources in an earlier attempt. Failed resource-pressure artifacts are kept separate and excluded from the trial count above.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 73–73.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00084"></a>
## FND-00084: Files and reproducibility — block 75

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Staged files, if present, are unvalidated implementation sketches only. They are not production code, not part of a delivered update, and should not be installed.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Lines 75–75.

**Source references:** SRC-1629, SRC-1631  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00085"></a>
## FND-00085: Chess.com premium analysis, end to end — block 3

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

What actually happens when you press **Game Review**, how accuracy is computed,
where the estimated Elo comes from, and what every classification means —
reconstructed from the production JavaScript bundles, not from documentation.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 3–5.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00086"></a>
## FND-00086: Chess.com premium analysis, end to end — block 7

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**Target:** the Game Review / advanced-analysis stack served to `www.chess.com/analysis`
**Method:** byte-offset reads of the shipped bundles (REA `analyze-javascript-application`,
evidence record `ev_a9a06871…479bcce`) plus protobuf
descriptor extraction; every schema claim is validated offline against libprotobuf (§10.3)
**Date:** 2026-11-11
**Companion:** `REVERSE-ENGINEERING.md` covers the *live-board* evaluation bar that the
extension taps; this document covers the *post-game* premium analysis, which is a
different server and a different protocol.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 7–14.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00087"></a>
## FND-00087: Chess.com premium analysis, end to end — block 16

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Written against these bundles (downloaded to `raw/`, since deleted — see
`REDOWNLOAD.md` to fetch them again):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 16–17.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00088"></a>
## FND-00088: Chess.com premium analysis, end to end — block 19

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| File | Size | What it holds |
| --- | --- | --- |
| `chunks/shared.eager.BOGLllgUUR.chunk.js` | 3.66 MB | CEAC transport, request builder, response → UI mapping, rating model |
| `chunks/tab-review.88a71be6.GEFrxdGEBZ.chunk.js` | 85 KB | the Game Review UI: report card, accuracy, rating display rules |
| `analysis.js` | 297 KB | analysis page bootstrap |
| 422 `FileDescriptorProto` blobs | — | every protobuf schema, rendered to `ALL-SCHEMAS.proto` (12,971 lines) |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 19–24.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00089"></a>
## FND-00089: Chess.com premium analysis, end to end — block 26

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

> **No live calls were made from this sandbox.** Everything below is static
> analysis of downloaded files plus offline round-trip verification (§10.2–10.3).
> §10.1 tells you how to capture a real session on your own machine.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 26–28.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00090"></a>
## FND-00090: Chess.com premium analysis, end to end — block 30

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 30–30.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00091"></a>
## FND-00091: 1. The short version — block 34

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Chess.com's premium analysis is **not** computed in your browser. The browser
sends your game to an analysis server over a protobuf-over-WebSocket protocol
called **CEAC IDL**, and the server streams back a `GameReview` message
containing the accuracy number, the Elo estimate, a classification for every
move, and human-readable explanations.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 34–38.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00092"></a>
## FND-00092: 1. The short version — block 40

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The browser's job is almost entirely **presentation**: it renders the report
card, colours the moves, and plays the sentences. There is exactly *one*
analytic thing it computes locally — a confidence band derived from your rating
that decides which "you lost your winning advantage" sentence to show (§7.2).

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 40–43.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00093"></a>
## FND-00093: 1. The short version — block 45

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```
                        ┌─────────────────────────────────────────┐
  your game  ──────────▶ │  wss://analysis.chess.com:443           │
  (protobuf)             │         /v2/game-review                 │
                         │                                         │
                         │  Stockfish 16.1 NNUE / Torch "human"    │
                         │  + explanation engine (CEE)             │
                         └──────────────┬──────────────────────────┘
                                        │ stream of GameReviewResponse
                                        ▼
        ┌───────────────────────────────────────────────────────┐
        │ browser: accuracy, report card, classifications,      │
        │          sentences, arrows — render only              │
        └───────────────────────────────────────────────────────┘
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 45–59.

**Source references:** SRC-2047  
**URL references:** <wss://analysis.chess.com:443>  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00094"></a>
## FND-00094: 1. The short version — block 61

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 61–61.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00095"></a>
## FND-00095: 2. Where the premium line actually is — block 65

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The paywall is not in the analysis; it is in **which fields the server is asked
to fill in**. Four checks decide it, all in
`shared.eager.BOGLllgUUR.chunk.js`:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 65–67.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00096"></a>
## FND-00096: 2. Where the premium line actually is — block 69

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Function | Offset | Logic | Effect |
| --- | --- | --- | --- |
| `af()` | 315,764 | `analysis?.hasUnlimitedReview === true && user?.isDiamond !== true` | is this account entitled to *unlimited* reviews |
| `M4e()` | 1,813,143 | `features.includes('game_review_platinum_report_card') && af()` | **turns the report card on** |
| `Om(1)` | 327,157 | `return !user?.isDiamond && e > 0` | gates "locked takeaways" |
| `Am()` | — | `context.user && features.includes('web_game_review_train_cta') && features.includes('web_new_train')` | the Train CTA |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 69–74.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00097"></a>
## FND-00097: 2. Where the premium line actually is — block 76

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`M4e()` flows straight into the request (§4):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 76–76.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00098"></a>
## FND-00098: 2. Where the premium line actually is — block 78

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
...l || u ? { gameReviewOptions: HO(zGe, {
    reportCardEntitled: l,                       // <- M4e()
    includeTrainTakeaways: u,                    // <- Am()
    canAccessLockedTakeaways: u && !Om(1),
}) } : {}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 78–84.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00099"></a>
## FND-00099: 2. Where the premium line actually is — block 86

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

So **the Elo estimate is a server feature flag, not a client calculation**. The
client does not compute a rating and then hide it behind a modal — it asks for
`report_card_entitled: true` and the server either populates
`GameReviewPlayerReportCard` or leaves it empty. That is why a free account
cannot obtain the number by patching out a CSS blur.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 86–90.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00100"></a>
## FND-00100: 2. Where the premium line actually is — block 92

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The UI side confirms it (`tab-review...chunk.js`):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 92–92.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.
