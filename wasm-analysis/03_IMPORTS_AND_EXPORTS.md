# Imports and exports

[WASM master index](00_WASM_MASTER_INDEX.md) · [Website master index](../chapters/00_MASTER_INDEX.md)

| Module | Imported functions | Exported functions | All exports |
| --- | --- | --- | --- |
| module-001 | 154 | 150 | 152 |
| module-002 | 155 | 151 | 153 |
| module-003 | 41 | 31 | 32 |
| module-004 | 22 | 14 | 16 |
| module-005 | 18 | 15 | 17 |

[All annotated entries and finding IDs](imports-exports-all.json). Everyimport/export retains exactname,kind,index/signature where applicable,loader literal context,qualified purpose and semantic confidence. Minifiednamesarekeptminified. Aloaderliteralhitdoesnotbyitselfproveasemanticmapping.

CEEusesenvandwasi_snapshot_preview1runtimeimports;Stockfish/Torchimportsaremoreheavilyminified. ImportedWASImethodnamesdonotgrantOSfilesystem/network access unless host glue exposes such capabilities.
