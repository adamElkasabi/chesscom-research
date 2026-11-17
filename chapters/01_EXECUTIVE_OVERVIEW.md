# Executive overview


## Focused Torch Human / bot-personality follow-up

The focused follow-up separates local Human search, remote Game Review, legacy Komodo personalities and configured Charm-small bots. Overall status remains PARTIALLY AUDITED.

[Evidence-graded focused update](../torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](../torch-human-bots-update/TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

[Master index](00_MASTER_INDEX.md)

**Overall status: PARTIALLY AUDITED.** This extends the preserved Chess.com knowledge recovery with new passive architecture evidence and dedicated offline analysis of all five locally available WASM binaries. It is not a reconstruction of unavailable private source code, a database schema dump, or a semantic explanation of every native function.

## Major architectural discoveries

1. **MySQL is supported by direct published evidence.** A March 11, 2024 Google Cloud article authored by a Chess.com principal engineer describes migration to Cloud SQL for MySQL Enterprise Plus. It also explicitly names ScyllaDB, Elasticsearch, and Redis. This establishes published technology use, not a database-to-endpoint mapping or a guarantee about every current service.
2. **PHP/Symfony are strongly indicated for the web tier.** Public PHP/Symfony job evidence is corroborated by generated route conventions and newly observed `k8s-prod-fpm-catch-all` response-pool labels. The implementation language of the separate CEAC service remains unknown.
3. **The UI uses a real shared implementation layer.** Saved bundles contain Vue/Pinia and Svelte-related compiled-runtime indicators. Four actual referenced CSS files expose a custom cc-* design system. The inventory records 367 implementation declaration variants, 1,240 CSS variable declarations, 633 distinct variable names, and 52 media-query occurrences. These are not a complete runtime component tree or all interactive states.
4. **CEE is substantive native computation, not just presentation.** Its binary interfaces and prior local executions support real search/review/classification/rating machinery. This does not establish parity with cloud engine builds, options, or scoring configuration.
5. **Native parameter types are recoverable despite misleading JavaScript arity.** The binary exports `CEE_InitWithOpts(i32,i32)->void`, `CEE_NewFeature(i32,i32,i32,i32)->i32`, and `CEE_Run(i32,i32)->i32`. JavaScript `.length === 0` was not the native ABI.
6. **WASM builds have materially different memory requirements.** CEE declares 386 MiB initial non-shared memory with a 2 GiB maximum. The Stockfish no-Worker build imports fixed 512 MiB shared memory; the single build defines 64 MiB initial non-shared memory. Torch Lite defines fixed 512 MiB non-shared memory. These are address-space declarations, not resident-memory measurements.

## What the new WASM work actually achieved

All five binaries were structurally parsed and validated. Function signatures, body offsets, imports/exports, globals, tables, element/data segments, opcode frequencies, direct-call graphs, and offset-linked string candidates were recovered. All five instantiated with explicit stub hosts under resource and capability restrictions; that is not a functional game-review test.

Full decompilation succeeded for two Stockfish modules and Torch Lite. Full CEE decompilation failed within the recorded tool/resource bounds; ten focused export-body decompilations succeeded using analysis-only typed stubs for other functions. Those derivatives are explicitly labelled and are not recovered original C++ source.

## Important incomplete areas

Additional referenced WASM versions, Rive assets, and multipart Torch references remain un-retrieved. Many functions have structural accounting but no independently reviewed semantic description. No private controllers, repositories, SQL tables/columns/indexes, ORM configuration, authenticated browser session, complete security policy, or exact cloud algorithm configuration was obtained. Inaccessible conversations and the external REA record remain unavailable.

The source and finding counts below include declarations, protocol fields, literal references, and recorded experimental outputs. They are not counts of independently verified current website features.

## Actual counts

| Metric | Actual |
|---|---|
| overall_status | PARTIALLY AUDITED; private backend/schema/cloud configuration partly UNVERIFIABLE |
| prior_source_occurrences | 2049 |
| new_source_records | 26 |
| total_source_records | 2075 |
| original_markdown_occurrences_inspected | 10 |
| loose_original_markdown_files | 6 |
| unique_original_markdown_contents | 8 |
| offline_files_reprocessed_in_new_batch | 1110 |
| prior_findings | 21056 |
| new_findings | 1208 |
| total_finding_records | 22264 |
| new_findings_by_confidence | {'STRONGLY INDICATED': 6, 'CONFIRMED': 1180, 'PROBABLE': 1, 'UNKNOWN': 21} |
| all_url_relative_reference_literals | 2806 |
| absolute_URL_literals | 1143 |
| prior_route_declarations | 321 |
| prior_endpoint_candidates | 235 |
| prior_declared_RPC_methods | 241 |
| new_public_GET_requests | 9 |
| HTML_artifacts_in_new_page_inventory | 7 |
| target_saved_or_fetched_page_artifacts | 4 |
| implementation_component_declaration_variants | 367 |
| CSS_files_fetched | 4 |
| CSS_variable_declarations | 1240 |
| unique_CSS_variable_names | 633 |
| media_queries | 52 |
| script_import_records | 1213 |
| available_unique_WASM_binaries | 5 |
| WASM_reference_literals_from_prior_evidence | 34 |
| WASM_modules_structurally_analyzed | 5 |
| WASM_modules_validated | 5 |
| WASM_modules_instantiated_with_stubs | 5 |
| defined_WASM_functions | 48089 |
| imported_WASM_functions | 390 |
| exported_WASM_function_entries | 361 |
| WASM_exports_all_kinds | 370 |
| WASM_direct_call_pairs | 200317 |
| focused_CEE_export_decompilations | 10 |
| full_module_decompilations_succeeded | 3 |
| prior_explicit_unavailable_sources | 18 |
| prior_gaps | 16 |
| prior_contradictions | 13 |
