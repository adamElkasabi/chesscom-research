# Chess.com forensic research: navigation

This collection documents a partial forensic architecture audit of Chess.com client material, including WebAssembly analysis, historical findings, supporting evidence, and a focused Torch Human and bot-personality follow-up. It does not establish private server implementation details or a complete semantic reconstruction. Consult the linked reports for their evidence and limits.

**Navigation update:** The original arrangement remains in place while a full content and publication-safety review is outstanding. No evidence has been removed or moved as part of this navigation update. Existing audit and overlay manifests describe their recorded snapshots; this README has since changed.

## Recommended reading order

1. [Executive overview](01_EXECUTIVE_OVERVIEW.md) — scope, major findings, and limitations. [Open in Drive](https://drive.google.com/file/d/1KIv4PAWxxQ7Q280u8CAjiLqJivTHLiKy/view)
2. [Master index](00_MASTER_INDEX.md) — the numbered architecture chapters and evidence indexes. [Open in Drive](https://drive.google.com/file/d/1IdAjc_gxywIZBaxZZ0N0vYzbTgOQffdt/view)
3. [WASM master index](wasm-analysis/00_WASM_MASTER_INDEX.md) — the initial five-binary investigation. [Open in Drive](https://drive.google.com/file/d/1DGw8PXc9CpTlj5uZE2yt_zHDM2TTDOVD/view)
4. [Deep WASM follow-up](wasm-deep-follow-up/reports/00-START-HERE.md) — expanded structural coverage, case studies, limitations, and packaging. [Open in Drive](https://drive.google.com/file/d/1A5GSNW-4j9rwB-WewEB0vU5wsbDKUUsT/view)
5. [Torch Human and bot-personality update](torch-human-bots-update/00_START_HERE.md) — focused evidence grades, corrections, and remaining questions. [Open in Drive](https://drive.google.com/file/d/1MuctKOVA6N0dQQH_m5uFvhTIcGWmrhRy/view)
6. [Findings index](findings/FINDINGS_INDEX.md) and [packaging and storage](PACKAGING_AND_STORAGE.md) — detailed records, provenance, and exclusions. [Findings in Drive](https://drive.google.com/file/d/1o6wUZM7djNVySr4ffF-whOCVKwuclQ7n/view) · [Packaging in Drive](https://drive.google.com/file/d/1hZGHx1SpPehbl7LjtiTMFDFy-xX8Mu98/view)

## Collection map

| Location | Contents |
| --- | --- |
| Root numbered chapters | Overview, site and frontend/backend architecture, technology, security, diagrams, and gaps. |
| [wasm-analysis](https://drive.google.com/drive/folders/1cOqKdnSRUX5YNOTYVHcnLibBNwUuPdiL) | Initial module reports, binary structure, imports/exports, runtime and known unknowns. |
| [wasm-deep-follow-up](https://drive.google.com/drive/folders/1MItwuLgLBfImXo6VMBrVjeqnSH-xsPaV) | Later reports and analysis artifacts; see its packaging chapter for retained and omitted payloads. |
| [torch-human-bots-update](https://drive.google.com/drive/folders/10ID1BZqNpTkmwilsi5EhtO9VRjuwmkXg) | Focused Human and bot research, evidence, tools, and corrections. |
| [findings](https://drive.google.com/drive/folders/1L7YAojavefMSUpZm4bkN-CWkUmiDlnS3) and [audit-metadata](https://drive.google.com/drive/folders/1OL1-1JpONzah7efcPHtVv5hL5kn5MEIa) | Detailed findings, machine ledgers, source manifests, checksums, metrics, and quality-control records. |
| [evidence](https://drive.google.com/drive/folders/1jzHtq13ZrOahdb9HtQe5ARoaMW5bqAs0), [registries](https://drive.google.com/drive/folders/1zn0hCK6E7Q--Z8zvp4sQ8aOS5Ci63VoD), and [diagrams](https://drive.google.com/drive/folders/1ELjzpquRF7XeuURg6FfB4N-noxDE82O7) | Supporting public artifacts, structured inventories, and Mermaid diagrams. |
| [history](https://drive.google.com/drive/folders/1kGFoGvysieRF5zUMJGqYOG8ViDLq6kTn) and [original-documentation](https://drive.google.com/drive/folders/1tWkbJUrXRUhIDNh4JQnzUHvj0pc1LZga) | Earlier audit material and labelled documentation copies. |
| [tools](https://drive.google.com/drive/folders/1hLJXjmPDeG2d09vUz2OthlDxxOyfKjZD) and [preserved-workspace](https://drive.google.com/drive/folders/1hnFa9Y8P7phsuaO_f79s2jxPims_bWLH) | Research and restoration scripts and retained workspace assets. |

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