# Drive mirror status

Source folder: [Chess.com research (Google Drive)](https://drive.google.com/drive/u/1/folders/1YTjYpPFNeBJlUfeDAayxSttqEqLJPMU6)

This file records exactly what from that folder is in this repository and what is not.
It exists because the source collection is roughly **400+ files / 250 MB+**, which cannot be
transferred in one pass through the Drive connector. Nothing here has been edited: files are
byte copies of the Drive originals, and the Drive copies remain authoritative.

## Included in this repository (top-level report layer)

| Path here | Drive file ID | Bytes |
| --- | --- | --- |
| README.md | 1uAw40ghH1dndeyw0-NvuzvnBE3CaYwpU | 5725 |
| 00_MASTER_INDEX.md | 1IdAjc_gxywIZBaxZZ0N0vYzbTgOQffdt | 3528 |
| 01_EXECUTIVE_OVERVIEW.md | 1KIv4PAWxxQ7Q280u8CAjiLqJivTHLiKy | 6109 |
| 06_TECHNOLOGY_STACK.md | 13xyOb2hK_RybheEM-wc-iqlanx-ayldk | 8916 |
| 23_KNOWLEDGE_GAPS.md | 1jUBLeBIuloOeUVOueHHLvRx1ysGga-DP | 3548 |
| 24_ARCHITECTURE_DIAGRAMS.md | 1fpA3a2Snh-KYBydnutXYwzrqWUMHi11a | 6725 |
| 25_FINAL_ARCHITECTURE_ASSESSMENT.md | 1K9_kBOPkUtgsdMv7zijpMmIfjU81Hd3u | 6193 |
| PACKAGING_AND_STORAGE.md | 1hZGHx1SpPehbl7LjtiTMFDFy-xX8Mu98 | 3060 |

Consequence: relative links in the included reports that point to chapters, indexes or payloads
that have not been mirrored yet (for example `02_SOURCE_INVENTORY.md`,
`findings/FINDINGS_INDEX.md`, `audit-metadata/*`) resolve only in the Drive copy. They are not
broken references in the original collection; they are simply not mirrored here yet.

## Not mirrored yet

| Drive area | Drive link | Contents | Approx. volume |
| --- | --- | --- | --- |
| Root numbered chapters | folder above | 02–05, 07–22 (including 08_UI_COMPONENT_ARCHITECTURE.md, 32 KB) | ~75 KB |
| TORCH_HUMAN_BOTS_PATCH_MANIFEST.json | 1_69QbM59-rU3WlSBRLrD_hqBLiLibXnL | overlay change manifest | 36 KB |
| wasm-analysis/ | [folder](https://drive.google.com/drive/folders/1cOqKdnSRUX5YNOTYVHcnLibBNwUuPdiL) | 13 chapter files, 2 diagrams, 5 module directories (module-001…005) with WAT, structure, imports/exports, functions, call graphs | ~110 MB (two 32 MB `module.wasm` binaries, two ~24 MB `structure.json`, two ~19 MB `functions.json`) |
| wasm-deep-follow-up/ | [folder](https://drive.google.com/drive/folders/1MItwuLgLBfImXo6VMBrVjeqnSH-xsPaV) | 10 reports, 24 analysis tools, 18 MB `analysis-evidence.tar.xz`, retained payloads, retrieved text, Rive recovered sources, CEE slice | ~40 MB |
| torch-human-bots-update/ | [folder](https://drive.google.com/drive/folders/10ID1BZqNpTkmwilsi5EhtO9VRjuwmkXg) | 9 report chapters, evidence and tools subfolders | ~100 KB + evidence |
| findings/ | [folder](https://drive.google.com/drive/folders/1L7YAojavefMSUpZm4bkN-CWkUmiDlnS3) | FINDINGS_INDEX.md and extended-findings-001…021 | ~2.5 MB |
| audit-metadata/ | [folder](https://drive.google.com/drive/folders/1OL1-1JpONzah7efcPHtVv5hL5kn5MEIa) | `findings-ledger.jsonl` (42 MB), `urls.jsonl` (4.6 MB), `source-manifest.json` (3.7 MB), `ALL_FILES.md` (489 KB), `checksums.sha256`, qa-report, metrics | ~52 MB |
| registries/ | [folder](https://drive.google.com/drive/folders/1zn0hCK6E7Q--Z8zvp4sQ8aOS5Ci63VoD) | components.json, design-system.json, script-imports.json and other inventories | ~2.1 MB |
| evidence/ | [folder](https://drive.google.com/drive/folders/1jzHtq13ZrOahdb9HtQe5ARoaMW5bqAs0) | new-public evidence set (not enumerated) | unknown |
| diagrams/ | [folder](https://drive.google.com/drive/folders/1ELjzpquRF7XeuURg6FfB4N-noxDE82O7) | 13 Mermaid `.mmd` sources corresponding to 24_ARCHITECTURE_DIAGRAMS.md | 4.4 KB |
| history/ | [folder](https://drive.google.com/drive/folders/1kGFoGvysieRF5zUMJGqYOG8ViDLq6kTn) | prior-audit corpus and its own findings/registries/metadata/evidence subfolders | ~MB scale |
| original-documentation/ | [folder](https://drive.google.com/drive/folders/1tWkbJUrXRUhIDNh4JQnzUHvj0pc1LZga) | labelled SRC-* documentation copies plus `new-public/` | ~110 KB |
| tools/ | [folder](https://drive.google.com/drive/folders/1hLJXjmPDeG2d09vUz2OthlDxxOyfKjZD) | 11 reproducibility scripts and INDEX.md | ~130 KB |
| preserved-workspace/ | [folder](https://drive.google.com/drive/folders/1hnFa9Y8P7phsuaO_f79s2jxPims_bWLH) | `extension/` retained workspace assets | unknown |

## How to finish the mirror

Either transfer the remaining items in additional batches (the readable Markdown/tooling layer
first, then the payloads), or download the whole Drive folder as a ZIP and copy it over this
tree at the same relative paths — the collection's own README states that its relative links
assume exactly this layout.
