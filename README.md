# Chess.com forensic research: navigation

This collection documents a partial forensic architecture audit of Chess.com client material, including WebAssembly analysis, historical findings, supporting evidence, and a focused Torch Human and bot-personality follow-up. It does not establish private server implementation details or a complete semantic reconstruction. Consult the linked reports for their evidence and limits.

**Status: PARTIALLY AUDITED** — not a complete private-source, database, schema or all-function decompilation. The original five WASM bytes and granular recovery evidence are included. Historical claims remain separate from new public evidence. The audit and overlay manifests describe their recorded snapshots; this README and the folder layout have changed since those snapshots were taken.

## Recommended reading order

1. [Executive overview](chapters/01_EXECUTIVE_OVERVIEW.md) — scope, major findings, and limitations.
2. [Master index](chapters/00_MASTER_INDEX.md) — the numbered architecture chapters and evidence indexes.
3. [WASM master index](wasm-analysis/00_WASM_MASTER_INDEX.md) — the initial five-binary investigation.
4. [Deep WASM follow-up](wasm-deep-follow-up/reports/00-START-HERE.md) — expanded structural coverage, case studies, limitations, and packaging. See also its [package entry note](wasm-deep-follow-up/START-HERE-DEEP-WASM.md).
5. [Torch Human and bot-personality update](torch-human-bots-update/00_START_HERE.md) — focused evidence grades, corrections, and remaining questions, with its [overlay change manifest](torch-human-bots-update/TORCH_HUMAN_BOTS_PATCH_MANIFEST.md) and [verification script](tools/verify-torch-human-bots-patch.py).
6. [Findings index](findings/FINDINGS_INDEX.md) and [packaging and storage](PACKAGING_AND_STORAGE.md) — detailed records, provenance, and exclusions.

## Collection map

| Location | Contents |
| --- | --- |
| [chapters](chapters/) | Overview, site and frontend/backend architecture, technology, security, diagrams, and gaps. |
| [wasm-analysis](wasm-analysis/) | Initial module reports, binary structure, imports/exports, runtime and known unknowns. |
| [wasm-deep-follow-up](wasm-deep-follow-up/) | Later reports and analysis artifacts; see its packaging chapter for retained and omitted payloads. |
| [torch-human-bots-update](torch-human-bots-update/) | Focused Human and bot research, evidence, tools, corrections, and overlay manifests. |
| [findings](findings/) and [audit-metadata](audit-metadata/) | Detailed findings, machine ledgers, source manifests, checksums, metrics, and quality-control records. |
| [evidence](evidence/), [registries](registries/), and [diagrams](diagrams/) | Supporting public artifacts, structured inventories, and Mermaid diagrams. |
| [history](history/) and [original-documentation](original-documentation/) | Earlier audit material and labelled documentation copies. |
| [tools](tools/) and [preserved-workspace](preserved-workspace/) | Research, restoration and verification scripts, and retained workspace assets. |

## Reference

- [Technology stack](chapters/06_TECHNOLOGY_STACK.md)
- [Exact counts](audit-metadata/completeness-metrics.json)
- [QC report](audit-metadata/qa-report.json)

Mermaid diagrams are plaintext and can be rendered with a Mermaid-capable viewer; no external resources are required to read the Markdown. Gzip files contain plain WAT/JSONL/pseudo code as labelled.

All links are relative to this repository. The reports label confidence and distinguish structural inspection, experiments, historical observations and unknowns. Structural coverage is not the same as semantic understanding, and an observed artifact is not proof of the current production system.
