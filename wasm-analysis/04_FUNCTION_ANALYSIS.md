# Function-level analysis

[WASM master index](00_WASM_MASTER_INDEX.md) · [Website master index](../chapters/00_MASTER_INDEX.md)

| Module | Defined | Direct caller/callee pairs | Indirect call sites |
| --- | --- | --- | --- |
| module-001 | 22922 | 97169 | 9438 |
| module-002 | 22953 | 97403 | 9451 |
| module-003 | 756 | 1994 | 736 |
| module-004 | 709 | 1898 | 655 |
| module-005 | 749 | 1853 | 642 |

Allfunctionsareindexedwithtype,bodyoffset/size,exportnames,opcode counts and direct callees. FullWATtranslationwasusedforinstructiondecoding;this is not a regex guess at raw opcodes. `call_indirect`targets remain unresolved and may hide important dispatch paths. Taildirectcallsarecountedwhenpresent.

10focusedCEEexportbodiesdecompiledwithtyped-stubcallees;bothStockfishmoduleshavefullnative-WABTdecompilation;TorchLitehasfullJS-WABTdecompilationwithcode-onlypackagedcopy. CEEfulltooldecompilationfailedwithpreservederrors. `selected-functions.wat`containsnear50KB-cappedexcerpts;long al locator bodies can end mid-function. Exactoriginalbinariesandcompletedefinition/call inventories remain.

NoexactCAPS2/ratingalgorithmornativeMLweightsemanticswerefullyreconstructed. Pseudocodevariablesandtypesaredecompilerinferences,notoriginalsource.
