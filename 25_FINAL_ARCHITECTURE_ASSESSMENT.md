# Final architecture assessment


## Focused Torch Human / bot-personality follow-up

Important refinement: real Charm-small bytes and native model-dependent bot decisions are demonstrated, while the legacy play-computer callsite explicitly requests Komodo. Human personality7, Torch bot-engine2, engine12 and Human search mode must not be conflated. Native CEE1.211.5 and UCI/package1.130.285 are separate reported versions.

[Evidence-graded focused update](torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

[Master index](00_MASTER_INDEX.md)

**PARTIALLY AUDITED.** Every currently available local WASM binary in this batch was structurally analyzed,but many functions remain semantically unreviewed and other referenced versions remain unretrieved. Importantprivate-serverfactsareUNVERIFIABLEwithavailableevidence.

| Layer | Technology | Confidence | Evidence / scope |
| --- | --- | --- | --- |
| Backend language | PHP | STRONGLY INDICATED | Public job posting explicitly requests PHP/Symfony; live public response pool label k8s-prod-fpm-catch-all. |
| Backend framework | Symfony | STRONGLY INDICATED | PHP job advert names Symfony; saved route token/default/requirement/host tables follow Symfony routing conventions. |
| Database | MySQL / Cloud SQL Enterprise Plus | CONFIRMED | 2024-03-11 Google Cloud article authored by Chess.com principal engineer: migration to Cloud SQL for MySQL Enterprise Plus; independent MySQL customer page. |
| Data systems | ScyllaDB | CONFIRMED | Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases. |
| Data systems | Elasticsearch | CONFIRMED | Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases. |
| Data systems | Redis | CONFIRMED | Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases. |
| ORM / data access | Doctrine | PROBABLE | Expired PHP backend job posting names Doctrine. |
| Frontend | Vue | CONFIRMED | Vue compiled __name,__vccOpts declarations and versioned vendor imports |
| Frontend | Pinia | CONFIRMED | Pinia imports and createPinia usage |
| Frontend | Svelte runtime | STRONGLY INDICATED | svelte-related style/runtime markers and compiled component lifecycle helpers |
| UI framework | Custom cc-* components | CONFIRMED | 367 recovered implementation declarations/references across stored code; cc-button,cc-icon,cc-avatar,cc-select,cc-tooltip among literal names. |
| CSS framework | Custom design system; no generic framework established | CONFIRMED | Four fetched named stylesheets; custom --color/--font/--motion tokens and cc-* selectors. |
| JavaScript | JavaScript and compiled modular bundles | CONFIRMED | Existing source files,ES imports,workers,dynamic chunk names and package paths. |
| Architecture pattern | Hybrid multi-page/client-component frontend | STRONGLY INDICATED | Saved pages contain server-provided HTML/bootstrap data and import page-specific client packages; reactive components update analysis state. |
| Backend architecture | Separate web / analysis / verification service boundaries | CONFIRMED | Game Review WebSocket host,run-search variants,BrilliantVerification RPC definitions and main web routes. |
| Web server / edge | Cloudflare edge | CONFIRMED | New public responses: Server:cloudflare,CF-RAY,cf-cache-status,Cloudflare NEL report host. |
| Application runtime | FPM-named Kubernetes web pool | STRONGLY INDICATED | X-Chesscom-Server-Pool and X-Chesscom-Ingress-Pool: k8s-prod-fpm-catch-all. |
| Hosting | Google Cloud multi-region database deployment | CONFIRMED | Google Cloud engineering article describes databases in several regions and Cloud SQL migration. |
| Build system | Vite-style asset pipeline / hashed client packages | CONFIRMED | /bundles/app/vite/ stylesheets,/r2/client-packages/<page>/<version>/ imports and hashed chunks. |
| WASM compiler | Emscripten-style C/C++ toolchain | STRONGLY INDICATED | Module.ccall,HEAPU8,embind,Asyncify,env.invoke_*,C++ exception imports and native .cc/.cpp strings. |

## Conclusions that can safely be reused

1.TheinspectedwebsiteisnotjustPHPorjustaSPA:server-deliveredwebpages,reactivepageapps,workers,and remote analysis interfaces coexist.
2.PHP/Symfonyarestronglyindicatedforthewebtier;CEACimplementationlanguageisunknown.
3.MySQL/CloudSQLEnterprisePlususageispublishedprimaryevidence;SQLtablesandper-endpoint data sources remain unknown.
4.TheCEEbinarycontainsactualcomputationalmachinery,not just a presentation adapter,but local capability does not establish native cloud configuration parity.
5.TheCEEABIandlinear-memory buffer protocol are confirmed;internal function names and full native algorithm semantics are not recovered.
6.Frontendcallsiteevidenceandengineexperimentsmustnotbeusedtoinventprivatedatabasearchitecture.

## Completion and packaging

See[actualmetrics](audit-metadata/completeness-metrics.json),[QC](audit-metadata/qa-report.json),[storage/exclusions](PACKAGING_AND_STORAGE.md),and[checkpoint](audit-metadata/audit-progress.md). TheprimaryZIPcontainsallpackageddocumentation,prior recovery evidence,allfiveoriginalWASMfiles,selectedWAT,function inventories,callgraphs,pseudocode,tools and explicit omissions.



## Completion statement

The architecture is reconstructed only to the boundary supported by the evidence. The database product can now be identified from primary published material, but its private schema cannot. The web tier is strongly indicated to use PHP/Symfony, but this is not proof that every backend service shares that stack. Every available local WASM binary was structurally processed; every referenced version was not retrieved, and every native function was not semantically explained.

**This remains PARTIALLY AUDITED, with important private internals UNVERIFIABLE from the available evidence.** The continuation checkpoint names the remaining batches. Do not treat the presence of all requested chapter files as full completion.
