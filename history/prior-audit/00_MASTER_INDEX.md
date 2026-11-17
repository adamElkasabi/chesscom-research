# Chess.com — forensic knowledge recovery and internal audit

**Status: PARTIALLY AUDITED, with full source-content/structured-extraction inventory.** This is not a claim to have recovered unavailable conversations or exhaustively interpreted every native instruction/minified function. See [completeness and QC](21_COMPLETENESS_AND_QC.md). Originals are preserved. All technical claims retain provenance and verification limits.

## Counts

| Measure | Actual count |
| --- | --- |
| total_source_records_processed | 2049 |
| findings_recovered | 21056 |
| absolute_urls | 415 |
| relative_references | 1510 |
| api_endpoint_declarations_or_candidates | 235 |
| declared_route_records | 321 |
| unresolved_knowledge_gaps | 16 |
| contradictions_or_version_distinctions | 13 |

## Chapters

- [01_EXECUTIVE_OVERVIEW.md](01_EXECUTIVE_OVERVIEW.md)
- [02_SOURCE_INVENTORY.md](02_SOURCE_INVENTORY.md)
- [03_RECOVERED_KNOWLEDGE.md](03_RECOVERED_KNOWLEDGE.md)
- [04_SITE_MAP_AND_ROUTES.md](04_SITE_MAP_AND_ROUTES.md)
- [05_PAGE_INVENTORY.md](05_PAGE_INVENTORY.md)
- [06_FRONTEND_ARCHITECTURE.md](06_FRONTEND_ARCHITECTURE.md)
- [07_BACKEND_ARCHITECTURE.md](07_BACKEND_ARCHITECTURE.md)
- [08_API_AND_NETWORK_INVENTORY.md](08_API_AND_NETWORK_INVENTORY.md)
- [09_AUTHENTICATION_AND_SESSIONS.md](09_AUTHENTICATION_AND_SESSIONS.md)
- [10_FORMS_AND_BUSINESS_LOGIC.md](10_FORMS_AND_BUSINESS_LOGIC.md)
- [11_DATA_MODELS_AND_RELATIONSHIPS.md](11_DATA_MODELS_AND_RELATIONSHIPS.md)
- [12_INFRASTRUCTURE_AND_DEPLOYMENT.md](12_INFRASTRUCTURE_AND_DEPLOYMENT.md)
- [13_SECURITY_OBSERVATIONS.md](13_SECURITY_OBSERVATIONS.md)
- [14_UI_AND_USER_WORKFLOWS.md](14_UI_AND_USER_WORKFLOWS.md)
- [15_EXTERNAL_SERVICES_AND_DEPENDENCIES.md](15_EXTERNAL_SERVICES_AND_DEPENDENCIES.md)
- [16_URL_AND_REFERENCE_INDEX.md](16_URL_AND_REFERENCE_INDEX.md)
- [17_HISTORICAL_FINDINGS.md](17_HISTORICAL_FINDINGS.md)
- [18_KNOWLEDGE_GAPS_AND_UNCERTAINTIES.md](18_KNOWLEDGE_GAPS_AND_UNCERTAINTIES.md)
- [19_CONTRADICTIONS_AND_DUPLICATES.md](19_CONTRADICTIONS_AND_DUPLICATES.md)
- [20_ORIGINAL_DOCUMENT_COVERAGE.md](20_ORIGINAL_DOCUMENT_COVERAGE.md)
- [21_COMPLETENESS_AND_QC.md](21_COMPLETENESS_AND_QC.md)

## Granular evidence and registries

- [All detailed finding files](findings/FINDINGS_INDEX.md)
- [Machine finding ledger](audit-metadata/findings-ledger.jsonl)
- [Source manifest](audit-metadata/source-manifest.json)
- [Every URL occurrence](audit-metadata/urls.jsonl)
- [Original file hashes](audit-metadata/original-snapshot.json)
- [Conversation reconstruction,not transcript search](audit-metadata/conversation-recovery.txt)
- [Metadata and registry file index](audit-metadata/ALL_FILES.md)
- [Checkpoint and remaining work](audit-metadata/audit-progress.md)

## How to read this corpus

1. Start with the overview/scope,then use chapter/category links for semantic findings.
2. Schema/route/URL records preserve fine-grained declarations; these are not automatically current runtime observations.
3. Follow SRCIDs to full redacted evidence copies/checksums and FNDIDs to detailed claims.
4. Compare claim conflicts before reusing old implementation conclusions.
5. Consult the checkpoint before claiming completion or extending the audit.

## Privacy and time provenance

Copied evidence redacts fixture player handles,email/credential-like literals,session/public-ingestion-keyvalues where detected. Original files were not changed. Binary engines/modelweightsarenotduplicatedintheZIP; hashes,relevant strings and native schema interfaces preserve the audited evidence. Session date and artifact timestamps conflict; source-embedded dates are retained as historical provenance,not silently normalized into a deployment date.
