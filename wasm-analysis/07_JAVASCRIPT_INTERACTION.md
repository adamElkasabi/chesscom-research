# JavaScript to WASM communication

[WASM master index](00_WASM_MASTER_INDEX.md) · [Website master index](../chapters/00_MASTER_INDEX.md)

## Confirmed CEE bridge

1.Theworkerloaderusesstreamingcompilationwithbufferedfallbackandexplicitwasmpath;the current extension constructs`loader.js#binary.wasm`.
2.EmscriptenModulebindsexportpropertiesandprovidesenv/WASIhostfunctions,HEAPviews,UTF8helpers,ccall,allocatorandAsyncify.
3.ProtobufrequestUint8Arrayscopyintoallocatedlinear-memorybuffers;CEE_NewFeaturetakesgamePoint,id,ptr,len. Inputbufferfreedinafinallyblock.
4.CEE_Run(handle,0)usesasync-ccall;native callback passes ptr,size,is_finaltoglue. GluecopiesHEAPU8slicetopostMessage. CeeClientwaitsforfinalupdateanddisposesfeaturehandles.
5.Genericprotobufcommandarraypathallocatesan8192-byte response buffer,copies returned bytes,and frees both buffers. Thisfixedwrappercapacitydoesnotprovethelargestpossiblenativeresponse.
6.UTF8stringsareencoded/decodedthroughEmscriptenhelpersandTextEncoderwhereexplicit. Charmmodelkeybuffersarenativeinputoptions,no recovered secrets.
7.Theextensionserializesbinarydataasbase64acrossChromeJSONruntimeports;WebSocketpayloadsthemselvesremainrawprotobufmessageframes.

Per-modulejavascript-bridge-excerpt.js and annotated imports/exports preserve exact glue. NodirectDBconnectivityisinferredfromWASM.

[JS/WASM diagram](../diagrams/10-js-wasm.mmd)
