# Executive overview and scope

[Master index](00_MASTER_INDEX.md)

This is an offline forensic recovery of the Chess.com investigation and its local extension, not a newly authenticated whole-site audit. All original files remain intact. Every original file and archive member was read for content/checksum/type-specific extraction, but not every function in multi-megabyte minified bundles or every WASM instruction has been semantically audited. **Overall status: partially audited.**

The new corpus preserves redacted evidence, every original Markdown block, exact schema namespaces/fields, every recovered URL occurrence, route declarations, trial outcomes, and claim conflicts. No production website mutation or new endpoint probing was performed.

## Actual metrics

| Metric | Result |
| --- | --- |
| audit_status | PARTIALLY AUDITED — complete byte/text scan and structured recovery; incomplete semantic interpretation of large bundles/native algorithms |
| original_documentation_files_discovered | 6 |
| original_documentation_files_inspected | 6 |
| archived_markdown_members_inspected | 4 |
| unique_original_markdown_contents | 8 |
| original_workspace_files_inventoried | 1135 |
| total_source_records_processed | 2049 |
| other_artifacts_content_processed | 2038 |
| memory_conversation_sources_accessed | 1 |
| findings_recovered | 21056 |
| findings_classified_verified_observation | 20774 |
| findings_verification_status_verified | 17159 |
| inferred_findings | 5 |
| hypotheses | 0 |
| unknown_or_documentary_unverified_claims | 277 |
| absolute_urls | 415 |
| relative_references | 1510 |
| all_unique_url_and_relative_references | 1925 |
| url_occurrences | 8487 |
| api_endpoint_declarations_or_candidates | 235 |
| rpc_methods_declared_in_native_descriptors | 241 |
| declared_route_records | 321 |
| saved_page_artifacts | 2 |
| unresolved_knowledge_gaps | 16 |
| contradictions_or_version_distinctions | 13 |
| inaccessible_source_entries | 18 |
| curated_semantic_findings | 200 |
| schema_records | 17254 |
| original_document_blocks_preserved | 274 |
| unique_trial_result_records | 83 |

## Main corrections

- Website Game Review uses a server in the inspected native frontend, while shipped CEE can nevertheless calculate reviews locally.
- Legacy analysis and compact CEE classifications are different enums.
- Low-level engine11 does not rule out an active human-mode search.
- A complete experimental human-preloaded review exists, but cloud parity does not.
- Old audio-unknown notes were followed by user confirmation.
- 2%progress was a coarse milestone, not a confirmed hidden-badge regression.
- v0.1.9progress is a calibrated local duration estimate, not engine position progress.
- Schema coexistence of CAPS2andaverageCP loss does not reveal the accuracy formula.
