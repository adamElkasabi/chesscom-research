# Memory and data layout

[WASM master index](00_WASM_MASTER_INDEX.md) · [Website master index](../chapters/00_MASTER_INDEX.md)

| Module | Declared memory | Data segments |
| --- | --- | --- |
| module-001 | [{"flags": 1, "minimum": 6176, "shared": false, "memory64": false, "maximum": 32768}] | 4270 |
| module-002 | [{"flags": 1, "minimum": 6176, "shared": false, "memory64": false, "maximum": 32768}] | 4272 |
| module-003 | [{"module": "a", "name": "a", "kind": "memory", "limits": {"flags": 3, "minimum": 8192, "shared": true, "memory64": false, "maximum": 8192}}] | 27 |
| module-004 | [{"flags": 1, "minimum": 1024, "shared": false, "memory64": false, "maximum": 32768}] | 93 |
| module-005 | [{"flags": 1, "minimum": 8192, "shared": false, "memory64": false, "maximum": 8192}] | 1312 |

Memorypagesare64KiB. CEEinitial6176pages=386MiB,max32768pages=2GiB,non-shared. Stockfishno-Workerimports8192pages512MiBfixedsharedmemory;singleStockfishdefines1024pages64MiBinitial/max2GiBnon-shared. TorchLitedefines8192pages512MiBfixednon-shared. Declaredlinearaddressspaceisnotresidentphysicalmemory.

GlobalsandAsyncifystatesdonotconstitutearecoveredC++classlayout. Datasegmentmapsandactiveconstantexpressionsareexact;model tensor structure and heap object ownership beyond wrapper buffer lifetime are mostly unknown.
