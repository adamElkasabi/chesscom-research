# module-002 — explanation-engine.wasm

[WASM master index](../../00_WASM_MASTER_INDEX.md)

**Original URL from saved script:** <https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm>

**Location:** `extension/engines/cee/explanation-engine.wasm`

**Ownership:** Custom explanation engine / embedded engines

**SHA256:** `b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373`; bytes:32922478

| Measure | Actual |
| --- | --- |
| Defined functions | 22953 |
| Imports | 155 |
| Exports all kinds | 153 |
| Types | 194 |
| Data segments | 4272 |
| Direct call pairs | 97403 |
| Indirect call sites | 9451 |
| Custom sections | 0 |

## Complete supporting artifacts

- [Original binary](module.wasm)
- [Original JS loader](loader.js)
- [All sections/types/globals/elements/data/function details](structure.json)
- [Imports/exports with signatures](imports-exports.json)
- [Every import/export annotated and source-linked](imports-exports-annotated.json)
- [Function inventory and static opcode/call counts](functions.json)
- [Full direct call graph JSONL gzip](call-graph.jsonl.gz)
- [Opcode frequencies](opcode-statistics.json)
- [Data segment addresses/hashes](data-segments.json)
- [Offset-linked relevant strings](strings.txt)
- [All ASCII candidates JSONL gzip](all-ascii-strings.jsonl.gz)
- [UTF16 candidates](utf16-candidates.json)
- [Selected WAT excerpts,capped per function](selected-functions.wat)
- [New controlled instantiation](runtime-observation.json)
- [Focused CEE decompilation results and limitations](focused-decompilation/results.json)

## Limits

Structural/function-indexanddirect-call analysis is complete for this available binary;human semantic review of all functions is not. Currentremote-byte identity was not verified. Memoryminimum/maximum is the declared address space,notameasurementofphysicalRAM. Exacttooloutcomesremaininstructure.json and std err files. Noemptyfailedtoolstdoutispresentedasdecompiledsource.
