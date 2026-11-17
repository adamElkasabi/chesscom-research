# 05 — Corrections, supersession and unresolved semantics

[Start](00_START_HERE.md)

## Supersession matrix — originals remain untouched

| Earlier or tempting statement | Supported replacement |
|---|---|
| “Human mode might be ignored because evaluation engine remains11.” | Rejected. Historical UCI commands differ; new matched-position ordinary/Human outputs differ while both retain engine11. |
| “No local Human review completed.” | Superseded by preserved original SRC-1628: feature79/per-position evaluation preload + feature1 + feature42 completed. Earlier SRC-1629/SRC-1631 failures remain historical evidence, not the latest result. |
| “Torch Human gives website parity / improved parity.” | Not shown. The completed historical comparison did not match reference metrics; no production tuning is recommended. |
| “The web Game Review pipeline is therefore entirely local.” | Rejected. SRC-1137 assembles a CEAC request routed to remote Game Review; local capability does not identify private cloud execution. |
| “A bot with Human personality uses Torch Human.” | Rejected for the inspected legacy callsite: it explicitly requests Komodo with personality7. New configuration behavior depends on actual resolved config, not the label alone. |
| “The model is just a loader stub / no actual model was recovered.” | Narrowly superseded: exact newly discovered Topaz public bytes were retrieved, structurally parsed, natively loaded and used through feature61. Old failed coach/Charm URLs remain failed; this is a different source. |
| “Charm-small is Maia / the Torch Human cloud model.” | Unproven. They have distinct schema/model/activation identities; optional Maia controls do not identify the underlying bytes. |
| “CEE native version1.130.285.” | Qualify as package/UCI/banner. Executed baseline module-002 feature2 reports native CEE1.211.5 and UCI1.130.285. |
| “No nn resource returned means no NN is used.” | Rejected by positive/negative controls: the same config reports the key only when the model is not already loaded. |
| “Personality enums can be passed through / Danny maps14.” | Not at this callsite. Explicit `Npt` mapping includes DANNY metadata9→UNSPECIFIED0; several other values also differ. |
| “Bot displayed rating directly sets legacy strength.” | Rejected at this adapter: `Mpt` uses skill fields; displayed rating seeds game metadata separately. |
| “Configured moves always fall back to book/legacy on error/empty.” | Not in `Z5`: configured branch returns directly; empty/error does not fall through there. Setup NotFound handling is a separate stage. |
| “Every bot's exact style formula is recovered.” | Not established. Schema knobs, adapter translation and selected native responses are recovered; precise native equations/production settings remain incomplete. |

## What is actually still missing

1. Authenticated/resolved production bot configs, per-experiment assignments, versions, private overrides and all actual weights/temperatures/thresholds. The offline fallback is not a live inventory.
2. Exact legacy native personality parameter sets, adaptive rating algorithm, strength calibration and random-seed/state effects. Five equal one-position moves do not establish a null personality effect.
3. Full additive/nnmult decision algebra, candidate/rule order, sampling distribution, legality filtering details, fallback logic and effect of all context/coherence settings.
4. Independent full model forward pass, tensor shape reconstruction for every tensor, board/token encoding, head-index semantics, dequantization use, training source/losses, and calibration. Complete container parsing is not complete neural semantic recovery.
5. Precise Torch Human tree-selection/pruning/likelihood formula and the condition under which optional Maia affects output. A single position with equal Human/default-disable outputs is not decisive.
6. Private remote Game Review binary/model versions and budgets, cache semantics beyond request flags, pool configuration, aggregation and classification/calibration policy.
7. Full browser lifecycle exercise for gate transitions, cached/stale book possibilities, model reload on worker replacement and config-fetch/book-fetch failure UX. These are explicit questions, not asserted defects.
8. A statistically designed multi-position style/strength/latency benchmark. Current tests deliberately remain fast and bounded; they are interface/behavior controls, not production tuning.
9. Every native function's semantic explanation. Existing29-WASM structural coverage remains valid as previously scoped; this focused update does not expand it into exhaustive decompilation.

## Evidence hygiene

The original full audit ZIP is unchanged. Original documentation, IDs, baseline evidence, source/function coverage metrics and archived failed findings remain untouched. Replaced report files get explicit additive update notices rather than silently rewriting archived source documents. New evidence IDs use the `THB-` namespace, not reassigned SRC IDs. Old ALL_FILES/source/QA counts remain **baseline snapshots**; the overlay's manifest and evidence index enumerate this addition separately.

Public scripts are stored losslessly. HTTP cookies, reporting tokens and the request-context-bearing raw HTML are not delivered; only allowlisted headers and a minimal page-observation record are included. Artificial runtime fixture metadata contains no real player identity. Historical engine-log excerpts omit their PGN/identity section. The public offline bot catalog is shipped as a source file, not mistaken for a list of human accounts.

No production extension code, debug card, quotas, progress UI or audio was changed. Nothing in this audit update promotes an experimental setting into the working extension.
