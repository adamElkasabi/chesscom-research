# Reference-game comparison: Chess.com, extension, local Torch human mode

Game: [PUBLIC_PLAYER_HANDLE_REDACTED] (White) vs [PUBLIC_PLAYER_HANDLE_REDACTED] (Black), live game 186934806892, 20 plies, 0–1. This is the original reference, not the newer example link used for source inspection.

All paired values below are **White / Black**. Chess.com figures are the user's supplied reference, not newly fetched scores. Extension figures are the saved working v0.1.7 baseline. The human-mode column is a newly executed, research-only pipeline using native engine outputs.

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

## What this experiment verifies
- Native GetGameReviewEvaluations feature79 with Fast strength and torchSearchMode.human was run at each of 21 game points (initial position plus 20 plies).
- All 21 calls completed with progress=1. The logs contain 20 human PV-tree searches (the terminal position needs no search), as well as auxiliary ordinary searches.
- Returned evaluations were added through the native AddEvaluations API, and native GameReview feature42 generated the accuracy, ratings and classifications above.
- No additional engine-search commands were recorded during that final review-generation step. No fetch attempts or warnings were recorded. Local WASM execution used its Node wrapper; this was not an installed Chrome integration test.
- Normalize/Hash tuning from the earlier sweep was NOT applied. The production extension was not modified.

## Important limits
This demonstrates a complete local experimental review built after human-mode evaluation, not parity with Chess.com's server-side Torch Human setup. Human-mode search logs use the internal default **rating 2100**; that has not been established as the server's configuration for this game. Underlying evaluation metadata remains engine11.

A matched research control (the same explicit per-position preload pipeline without human mode) returned accuracy 60.2 / 96.1 and ratings 300 / 1000. It differs slightly from the direct production baseline. Therefore the human column versus production is a pipeline comparison, not a perfectly isolated one-setting benchmark. Relative to the matched control, human mode also moves both accuracy figures farther from the supplied reference.

**Conclusion:** This local human-mode configuration does not improve the reference match. Keep v0.1.7 unchanged.

## Move-by-move local classifications
The supplied Chess.com reference contains aggregate counts, not a classification for each individual move, so no per-move Chess.com labels are invented here.

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

## Raw evidence
- research/refinement/results/comparison-human.json
- research/refinement/results/comparison-control.json
- research/refinement/results/baseline.json
- research/refinement/comparison-trial.mjs
- research/refinement/configs/comparison-human.json
- research/refinement/target.json
