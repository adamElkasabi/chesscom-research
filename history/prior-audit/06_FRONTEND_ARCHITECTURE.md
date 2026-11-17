# Frontend architecture

[Master index](00_MASTER_INDEX.md)

Saved public bundles establish package imports,Vue/Pinia APIs,custom elements,Vite/Rolldown-style packaging,dynamic chunks,feature flags,storage and workers. Different pages/package dates can use different component stacks. Svelte-like interpretation in old evaluation-bar research is an inference,not a version-verified library identity. See preserved source snippets and exact imports.


## Detailed findings

- [FND-18917](findings/frontend-001.md#FND-18917) — Quick Analysis has a dedicated lazy client
- [FND-18918](findings/frontend-001.md#FND-18918) — Quick Analysis binary-interface gate
- [FND-18919](findings/frontend-001.md#FND-18919) — Quick Analysis binary search settings
- [FND-18920](findings/frontend-001.md#FND-18920) — Legacy Quick Analysis supplies external evaluations
- [FND-18921](findings/frontend-001.md#FND-18921) — Quick Analysis worker parallelism derives from device concurrency
- [FND-18923](findings/frontend-001.md#FND-18923) — Binary debug switch has initialization requirements
- [FND-18925](findings/frontend-001.md#FND-18925) — CEE asset version and SIMD selection are flag-dependent
- [FND-18891](findings/architecture-001.md#FND-18891) — Three different analysis pipelines must not be conflated
- [FND-18926](findings/evaluation_bar-001.md#FND-18926) — Native evaluation bar custom element
- [FND-18927](findings/evaluation_bar-001.md#FND-18927) — Evaluation-bar event bus and manual override
- [FND-18928](findings/evaluation_bar-001.md#FND-18928) — Evaluation-bar attributes and board readiness
- [FND-18929](findings/evaluation_bar-001.md#FND-18929) — Evaluation-bar default settings
- [FND-18930](findings/evaluation_bar-001.md#FND-18930) — Evaluation-bar score mapping
- [FND-18931](findings/evaluation_bar-001.md#FND-18931) — Bot-mode assistance visibility differs by preset
- [FND-18932](findings/evaluation_bar-001.md#FND-18932) — Unresolved bot lazy-loader predicates
- [FND-18943](findings/extension-001.md#FND-18943) — Main-world hook and isolated bridge have distinct responsibilities
- [FND-18944](findings/extension-001.md#FND-18944) — Quota launch checks are canCreate and locked, not just unlimited review
- [FND-18945](findings/extension-001.md#FND-18945) — WebSocket brand-check regression is explicit
- [FND-18946](findings/extension-001.md#FND-18946) — Only Game Review sockets loop back locally
- [FND-18947](findings/extension-001.md#FND-18947) — Chrome runtime messaging needs base64 for binary
- [FND-18948](findings/extension-001.md#FND-18948) — Offscreen host dials out to avoid lost initial ports
- [FND-18949](findings/extension-001.md#FND-18949) — Service-worker keepalive and computation progress are separate
- [FND-18950](findings/extension-001.md#FND-18950) — CEE API client serializes no-request-ID calls
- [FND-18951](findings/extension-001.md#FND-18951) — Native review adapter merges CEAC search settings
- [FND-18952](findings/extension-001.md#FND-18952) — Legacy effectiveRating alias is transparent, not verified V2 prediction
- [FND-18953](findings/extension-001.md#FND-18953) — Native speech hashes and arrows survive the adapter
- [FND-18954](findings/extension-001.md#FND-18954) — Manifest permissions and CSP belong to extension, not website
- [FND-18955](findings/extension-001.md#FND-18955) — Update ZIPs are overlays, not standalone installers
- [FND-18956](findings/extension-001.md#FND-18956) — Hook VERSION0.1.6 is retained with manifest0.1.9
- [FND-18957](findings/progress-001.md#FND-18957) — Original coarse progress was0/2/100, not a hidden-card regression
- [FND-18958](findings/progress-001.md#FND-18958) — v0.1.9 progress uses real local successful-duration samples
- [FND-18959](findings/progress-001.md#FND-18959) — First matching review is calibration, not smooth estimated progress
- [FND-18960](findings/progress-001.md#FND-18960) — Estimated percentage is time-based and caps below completion
- [FND-18961](findings/progress-001.md#FND-18961) — History persistence excludes personal game contents
- [FND-18962](findings/progress-001.md#FND-18962) — Progress metadata callback is presentation-only
