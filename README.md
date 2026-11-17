# Chess.com forensic research: navigation

This collection documents a partial forensic architecture audit of Chess.com client material, including WebAssembly analysis, historical findings, supporting evidence, and a focused Torch Human and bot-personality follow-up. It does not establish private server implementation details or a complete semantic reconstruction. Consult the linked reports for their evidence and limits.

**Navigation update:** The original arrangement remains in place while a full content and publication-safety review is outstanding. No evidence has been removed or moved as part of this navigation update. Existing audit and overlay manifests describe their recorded snapshots; this README has since changed.

## Recommended reading order

1. [Executive overview](01_EXECUTIVE_OVERVIEW.md) — scope, major findings, and limitations.
2. [Master index](00_MASTER_INDEX.md) — the numbered architecture chapters and evidence indexes.
3. [WASM master index](wasm-analysis/00_WASM_MASTER_INDEX.md) — the initial five-binary investigation.
4. [Deep WASM follow-up](wasm-deep-follow-up/reports/00-START-HERE.md) — expanded structural coverage, case studies, limitations, and packaging.
5. [Torch Human and bot-personality update](torch-human-bots-update/00_START_HERE.md) — focused evidence grades, corrections, and remaining questions.
6. [Findings index](findings/FINDINGS_INDEX.md) and [packaging and storage](PACKAGING_AND_STORAGE.md) — detailed records, provenance, and exclusions.

## Collection map

| Location | Contents |
| --- | --- |
| Root numbered chapters | Overview, site and frontend/backend architecture, technology, security, diagrams, and gaps. |
| wasm-analysis | Initial module reports, binary structure, imports/exports, runtime and known unknowns. |
| wasm-deep-follow-up | Later reports and analysis artifacts; see its packaging chapter for retained and omitted payloads. |
| torch-human-bots-update | Focused Human and bot research, evidence, tools, and corrections. |
| findings and audit-metadata | Detailed findings, machine ledgers, source manifests, checksums, metrics, and quality-control records. |
| evidence, registries, and diagrams | Supporting public artifacts, structured inventories, and Mermaid diagrams. |
| history and original-documentation | Earlier audit material and labelled documentation copies. |
| tools and preserved-workspace | Research and restoration scripts and retained workspace assets. |

Relative links are for a downloaded collection with the same layout; Drive links address the original items directly. The reports label confidence and distinguish structural inspection, experiments, historical observations and unknowns. Structural coverage is not the same as semantic understanding, and an observed artifact is not proof of the current production system.

---

## Original README text

# Chess.com extended forensic architecture and WASM audit


## Focused Torch Human / bot-personality follow-up

An incremental focused Torch Human / bot-personality audit is included. Read its overview and overlay manifest; the original full ZIP, source IDs and archived documentation remain unchanged.

[Evidence-graded focused update](torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

Startwith[00_MASTER_INDEX.md](00_MASTER_INDEX.md).

**PARTIALLY AUDITED**,not a complete private-source/database/schemaorall-function decompilation. OriginalfiveWASMbytesandgranularrecoveryevidenceareincluded. Historicalclaimsremainseparatefromnewpublicevidence.

- [Technology stack](06_TECHNOLOGY_STACK.md)
- [WASM master](wasm-analysis/00_WASM_MASTER_INDEX.md)
- [All findings](findings/FINDINGS_INDEX.md)
- [Exact counts](audit-metadata/completeness-metrics.json)
- [Packaging and exclusions](PACKAGING_AND_STORAGE.md)
- [QC report](audit-metadata/qa-report.json)

MermaiddiagramsareplaintextandcanberenderedwithaMermaid-capableviewer;noexternalresourcesarerequiredtoreadtheMarkdown. GzipfilescontainplainWAT/JSONL/pseudo code as labelled.
