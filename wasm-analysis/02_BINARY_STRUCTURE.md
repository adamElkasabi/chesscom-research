# Binary structure

[WASM master index](00_WASM_MASTER_INDEX.md) · [Website master index](../chapters/00_MASTER_INDEX.md)

AllfivehaveWASMmagic0061736d/version1. Types,imports,function type indices,tables,defined/importedmemories,globals,exports,start(ifpresent),elements,data-count,codebodies,data and custom sections are parsed with file offsets. No customsections/name/producers/DWARFwerefoundinthesefive. OriginalheadersummariesandWABTvalidationstatusareincludedpermodule.

No parserremainderisacceptedwithoutQCflag. Functionbodyoffsetsreferoriginalbinarybytes,notWATlinepositions. Datasegmentsretainmode,initializer,fileoffset,lengthandSHA256;active constant offsets map string file positions to linear memory addresses.
