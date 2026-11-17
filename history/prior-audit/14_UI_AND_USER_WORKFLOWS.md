# UI and user workflows

[Master index](00_MASTER_INDEX.md)

The page renders native response numbers,classifications,annotations,speech hashes and arrows; the extension preserves its CEAC decode/dispatch path. User sound/UIconfirmationisdistinctfrommockbrowserorexecutableWASMtests. The progress-estimation and hidden-card sequence is preserved,including the explicit retraction of the original failure report.

See [full reference comparison](evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md) and [native review move findings](findings/FINDINGS_INDEX.md). No cloud per-move labels have been invented.

## Detailed findings

- [FND-18957](findings/progress-001.md#FND-18957) — Original coarse progress was0/2/100, not a hidden-card regression
- [FND-18958](findings/progress-001.md#FND-18958) — v0.1.9 progress uses real local successful-duration samples
- [FND-18959](findings/progress-001.md#FND-18959) — First matching review is calibration, not smooth estimated progress
- [FND-18960](findings/progress-001.md#FND-18960) — Estimated percentage is time-based and caps below completion
- [FND-18961](findings/progress-001.md#FND-18961) — History persistence excludes personal game contents
- [FND-18962](findings/progress-001.md#FND-18962) — Progress metadata callback is presentation-only
- [FND-18926](findings/evaluation_bar-001.md#FND-18926) — Native evaluation bar custom element
- [FND-18927](findings/evaluation_bar-001.md#FND-18927) — Evaluation-bar event bus and manual override
- [FND-18928](findings/evaluation_bar-001.md#FND-18928) — Evaluation-bar attributes and board readiness
- [FND-18929](findings/evaluation_bar-001.md#FND-18929) — Evaluation-bar default settings
- [FND-18930](findings/evaluation_bar-001.md#FND-18930) — Evaluation-bar score mapping
- [FND-18931](findings/evaluation_bar-001.md#FND-18931) — Bot-mode assistance visibility differs by preset
- [FND-18932](findings/evaluation_bar-001.md#FND-18932) — Unresolved bot lazy-loader predicates
