# Chess.com Local Review — v0.1.8

## v0.1.8 — hide debug card only

The bottom-left debug card is disabled. Diagnostics still appear in Chrome
DevTools Console with the `[local-review]` prefix. Review calculations, quota
handling, engine files, speech/audio, and Chess.com's review UI are unchanged.
No experimental Torch Human or engine-tuning changes are included.

Extract the v0.1.8 hide-debug update ZIP **over your existing working extension
folder**, replacing the included files. Do not delete the existing folder or
its engine files. Reload the extension at `chrome://extensions`, then refresh
all open Chess.com tabs to remove the old card. This is a small update ZIP,
not a standalone installation. The hook's internal version label remains
0.1.6 because the core socket/quota implementation is still that version.

---

## Previous v0.1.7 update notes

## Install this update

1. Extract the v0.1.7 update ZIP into your existing unpacked extension folder
   (the folder containing manifest.json). Replace files when prompted; preserve
   the other existing files and engines.
2. Open `chrome://extensions` and click **Reload** on this extension.
3. Refresh the Chess.com tab and rerun Game Review.

The Chrome extension version is 0.1.7. The on-page hook still reports 0.1.6:
its working quota/socket code is deliberately unchanged, byte for byte.
This ZIP is an update, not a standalone extension installation.

## What changed

The old review builder independently searched Stockfish positions, applied
centipawn-loss thresholds for labels, used a homemade accuracy curve, and
estimated ratings with a formula and a floor of 400. Those calculations have
been removed from the production review builder.

The extension now calls Chess.com's bundled CEE NewGame + GameReview features
and wraps the result in the real CEAC response envelope. It preserves native
classifications, accuracy, tallies, rating output, speech hashes, explanation
markings, opening, result, and PGN output. It does not substitute fixture
results or make game-specific corrections.

The bundled CEE currently omits the optional newer gameRatingV2 field. For the
page's V2-enabled rating display, the adapter copies CEE's effectiveRating
(legacy Game Rating) into that field. It does not calculate a new rating.
Diagnostics record the source as effectiveRating.

Whole-game CEE calls may take a while without intermediate progress. The
extension sends keepalive progress frames at the last known progress rather
than claiming a made-up percentage.

## Verified example: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED]

| Metric | Old extension (user report) | v0.1.7 local test | Chess.com target |
| --- | ---: | ---: | ---: |
| White accuracy | 57.5 | 60.0 | 71.7 |
| Black accuracy | 88.8 | 95.5 | 99.0 |
| White Game Rating | 400 | 300 | 100 |
| Black Game Rating | 400 | 1000 | 1000 |
| White blunders | 4 | 1 | 1 |
| Black Great moves | 2 | 1 | 1 |
| Black mistakes | 2 | 0 | 0 |

Full classification comparison:

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

## Still open

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

## Tests

- `node test/quota-test.mjs`: exhausted quota + uncached review gate regressions.
- `node test/hook-test.mjs`: brand-checked WebSocket regression suite.
- `node test/run-test.mjs`: genuine CEE wasm + response codec + example comparison.
- `node test/browser-cee-test.mjs`: actual Chromium extension Worker/wasm test,
  plus hook -> content bridge -> service worker -> real offscreen document ->
  CEE -> success, on a simulated Chess.com page with quota exhausted and no
  cached review. Requires Playwright and Chromium.

These tests passed in the development environment. The live Chess.com frontend
still needs user confirmation. The quota hook was already confirmed working
by the user in v0.1.6 and is unchanged here.
