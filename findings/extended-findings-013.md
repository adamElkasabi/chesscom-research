# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30720"></a>
## FND-30720 — module-001 export dynCall_iiiiijj

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiijj", "kind": "function", "index": 23069, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "type_index": 63, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118956, "loader_excerpt": "nCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30721"></a>
## FND-30721 — module-001 export dynCall_iiiiiijj

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiiijj", "kind": "function", "index": 23070, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "type_index": 192, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119002, "loader_excerpt": "ll_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instanc", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30722"></a>
## FND-30722 — module-001 export asyncify_start_unwind

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "asyncify_start_unwind", "kind": "function", "index": 23071, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119054, "loader_excerpt": "ts.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30723"></a>
## FND-30723 — module-001 export asyncify_stop_unwind

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "asyncify_stop_unwind", "kind": "function", "index": 23072, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119110, "loader_excerpt": "_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitializ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30724"></a>
## FND-30724 — module-001 export asyncify_start_rewind

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "asyncify_start_rewind", "kind": "function", "index": 23073, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119166, "loader_excerpt": "art_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_erro", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30725"></a>
## FND-30725 — module-001 export asyncify_stop_rewind

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "asyncify_stop_rewind", "kind": "function", "index": 23074, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119222, "loader_excerpt": "op_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_error(Module){return Module.ccall(\"CEE_GetLastError\",\"string", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30726"></a>
## FND-30726 — module-001 export asyncify_get_state

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "asyncify_get_state", "kind": "function", "index": 23075, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": null, "loader_excerpt": "", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30727"></a>
## FND-30727 — module-001 exact protobuf buffer boundary

js_buf_to_c_buf allocates length*BYTES_PER_ELEMENT,HEAPU8.set copies bytes. CEE_NewFeature(gamePoint,featureId,ptr,len) returns handle and frees input buffer in finally. CEE_Run(handle,0) is async; imported callback copies HEAPU8.subarray(ptr,ptr+size).slice() into postMessage({proto,is_final}). The protocol payload is real protobuf,not JSON.

- Category: wasm_javascript
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/javascript-bridge-excerpt.js)

```text
CEE_NewFeature has native(i32,i32,i32,i32)->i32;CEE_Run(i32,i32)->i32. Import callback and exact wrapper retained.
```

<a id="FND-30728"></a>
## FND-30728 — module-001 actual CEE_InitWithOpts native signature

Binary export CEE_InitWithOpts has two i32parameters and no result. It forwards to an internal function through Asyncify instrumentation. Earlier JS-functionlength0was not the native ABI. Interpretation as(ptr,len) is supported by protobuf wrapper conventions but the generic initialization call itself is not proven by this signature alone.

- Category: wasm_javascript
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No claim of arbitrary initialization-option compatibility or a successful TorchHuman toggle from InitWithOpts.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/focused-decompilation/CEE_InitWithOpts.pseudocode.txt)

```text
{"name": "CEE_InitWithOpts", "kind": "function", "index": 1665, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1}
```

<a id="FND-30729"></a>
## FND-30729 — module-001 focused native function reconstruction

Five export bodies decompiled using analysis-only modules with signature-correct imported stubs for all other functions; globals/tables/memory declarations retained,but original data omitted. Full decompilation attempts failed: JS WABT memory-out-of-bounds; native process killed137under2GiBaddressspace/60sCPUbound. These failures are tooling/resource outcomes,not proof of engine invalidity.

- Category: wasm_decompilation
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/focused-decompilation/results.json)

```text
CEE_Init,CEE_InitWithOpts,CEE_NewFeature,CEE_DisposeFeature,CEE_Run each decompiled successfully. Numeric fields/types/names in pseudocode are decompiler assignments,not recovered source identifiers.
```

<a id="FND-30730"></a>
## FND-30730 — module-002 complete structural inventory

32922478bytes; SHA256b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373; 22953defined functions,155imported functions,153exports. All section offsets,types,limits,globals,elements,data and function body spans retained.

- Category: wasm_structure
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../wasm-analysis/modules/module-002/structure.json)

```text
Magic0061736d;version1;no custom sections.
```

<a id="FND-30731"></a>
## FND-30731 — module-002 function and call-graph analysis

97403direct caller/callee pairs;235146static direct-call sites;9451indirect-call sites. Exact direct call indices recovered from full WAT. Indirect dispatch targets not resolved; opcode frequencies are syntactic counts,not execution profiling.

- Category: wasm_functions
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/functions.json)

```text
See call-graph.jsonl.gz and opcode-statistics.json.
```

<a id="FND-30732"></a>
## FND-30732 — module-002 strings and data offsets

43264ASCII candidates,2747keyword-relevant candidates,552UTF16candidates. Strings linked to original file offsets and active data memory addresses when constant-resolvable. Random code/weight bytes can resemble text.

- Category: wasm_strings
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/strings.txt)

```text
All-ASCII candidates are separately gzipped; relevant output is not a semantic analysis of every string.
```

<a id="FND-30733"></a>
## FND-30733 — module-002 memory/host boundary

{"defined_memories": [{"flags": 1, "minimum": 6176, "shared": false, "memory64": false, "maximum": 32768}], "imported_memories": [], "tables": [{"element_type": "funcref", "limits": {"flags": 1, "minimum": 26324, "shared": false, "memory64": false, "maximum": 26324}}], "data_segments": 4272}

- Category: wasm_memory
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/structure.json)

```text
Memory limits use64KiBpages; shared flag is explicit.
```

<a id="FND-30734"></a>
## FND-30734 — module-002 new controlled instantiation

Bounded Node instantiation succeeded with explicitly stubbed imports; this is not engine search/review correctness. Initial module003failed due unhandled imported memory,then passed using exact descriptor limits. Stack-query exports were called only when present.

- Category: wasm_runtime
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No native whole-game review rerun,new server query,or cloud parity test. Historical successful full CEE/Human tests retained separately.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/runtime-observation.json)

```text
{"status": "instantiated with function import stubs", "imports": 155, "exports": 153, "memories": [{"name": "memory", "bytes": 404750336, "shared": false}], "import_calls_during_instantiation": [], "elapsed_ms": 103.194706, "algorithm_calls": [{"name": "emscripten_stack_get_current", "result": 26691088}], "limitation": "No wrapper runtime constructors/search/review invoked; stub instantiation is not a functional engine validation. No original application inputs used."}
```

<a id="FND-30735"></a>
## FND-30735 — module-002 import env.invoke_vii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vii", "kind": "function", "type_index": 5, "function_index": 0, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103102, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viif:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viif(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30736"></a>
## FND-30736 — module-002 import env.__cxa_find_matching_catch_3

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_3", "kind": "function", "type_index": 2, "function_index": 1, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74923, "loader_excerpt": "ion_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new Cpp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30737"></a>
## FND-30737 — module-002 import env.llvm_eh_typeid_for

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "llvm_eh_typeid_for", "kind": "function", "type_index": 2, "function_index": 2, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 110079, "loader_excerpt": "y=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),wasmExports.__wasm_call_ctors(),FS.ignorePermissions=!1,Module.onRuntimeInitialized?.(),function(){var postRun=Module.postRun;postRun&&(\"function\"==typeof po", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30738"></a>
## FND-30738 — module-002 import env.__cxa_begin_catch

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_begin_catch", "kind": "function", "type_index": 2, "function_index": 3, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74331, "loader_excerpt": "nsole).awaitLines(id,Module.ceeInterruptMailbox);return null===joined?0:stringToNewUTF8(joined)}))},__cxa_begin_catch:ptr=>{var info=new ExceptionInfo(ptr);return info.get_caught()||(info.set_caught(!0),uncaughtExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught.length)return 0;var info=exceptionCaught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30739"></a>
## FND-30739 — module-002 import env.invoke_viii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viii", "kind": "function", "type_index": 6, "function_index": 4, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103790, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiddi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiddi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidi:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiidi(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30740"></a>
## FND-30740 — module-002 import env.invoke_iiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiii", "kind": "function", "type_index": 10, "function_index": 5, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95811, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30741"></a>
## FND-30741 — module-002 import env.invoke_ii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_ii", "kind": "function", "type_index": 3, "function_index": 6, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94948, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ii:function(index,a1){var sp=stackSave();try{return dynCall_ii(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iid:function(index,a1,a2){var sp=stackSave();try{return dynCall_iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(in", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30742"></a>
## FND-30742 — module-002 import env.exit

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "exit", "kind": "function", "type_index": 0, "function_index": 7, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 90065, "loader_excerpt": "tring of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30743"></a>
## FND-30743 — module-002 import env.invoke_vi

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vi", "kind": "function", "type_index": 1, "function_index": 8, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102250, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30744"></a>
## FND-30744 — module-002 import env.__cxa_find_matching_catch_2

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_2", "kind": "function", "type_index": 8, "function_index": 9, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74869, "loader_excerpt": "var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30745"></a>
## FND-30745 — module-002 import env.__cxa_end_catch

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_end_catch", "kind": "function", "type_index": 12, "function_index": 10, "signature": {"parameters": [], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74733, "loader_excerpt": "ught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_e", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30746"></a>
## FND-30746 — module-002 import env.invoke_v

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_v", "kind": "function", "type_index": 0, "function_index": 11, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101930, "loader_excerpt": "a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stac", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30747"></a>
## FND-30747 — module-002 import env.__resumeException

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__resumeException", "kind": "function", "type_index": 0, "function_index": 12, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 75897, "loader_excerpt": "n(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return stream.flags=-289793&stream.flags|289792&arg,0;case 12:arg=syscallGetVarargP();return HEAP16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64:function(fd,buf){try{return SYSCALLS.writeStat(buf,F", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30748"></a>
## FND-30748 — module-002 import env.invoke_iii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iii", "kind": "function", "type_index": 4, "function_index": 13, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95453, "loader_excerpt": "iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30749"></a>
## FND-30749 — module-002 import env.__cxa_throw

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_throw", "kind": "function", "type_index": 5, "function_index": 14, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75640, "loader_excerpt": "ughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return st", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30750"></a>
## FND-30750 — module-002 import env.invoke_iiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiiii", "kind": "function", "type_index": 21, "function_index": 15, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96567, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_iiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30751"></a>
## FND-30751 — module-002 import env.__assert_fail

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__assert_fail", "kind": "function", "type_index": 6, "function_index": 16, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 73896, "loader_excerpt": "ge({error:\"CEE was unable to write a proto message to a js buffer\"})}};var wasmExports,wasmImports={__assert_fail:(condition,filename,line,func)=>abort(`Assertion failed: ${UTF8ToString(condition)}, at: `+[filename?UTF8ToString(filename):\"unknown filename\",line,func?UTF8ToString(func):\"unknown function\"]),__asyncjs__cee_worker_await_lines:function(id){return Asyncify.handleAsync((async()=>{var joined=await engineWorkersOf(Module,console).awaitLines(id,Module.ceeInterruptMailbox);return null===joined?0:stringToNewUTF8(joined)}))},__cxa_begin_catch:ptr=>{var info=new ExceptionInfo(ptr);return info.get_caught()||(info.set_caught(!0),uncaughtExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30752"></a>
## FND-30752 — module-002 import env.invoke_viiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiii", "kind": "function", "type_index": 7, "function_index": 17, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104918, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30753"></a>
## FND-30753 — module-002 import env.invoke_viiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiii", "kind": "function", "type_index": 16, "function_index": 18, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105678, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30754"></a>
## FND-30754 — module-002 import env.invoke_viiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiii", "kind": "function", "type_index": 9, "function_index": 19, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105490, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30755"></a>
## FND-30755 — module-002 import env.invoke_ji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_ji", "kind": "function", "type_index": 14, "function_index": 20, "signature": {"parameters": ["i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100378, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Emscripte", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30756"></a>
## FND-30756 — module-002 import env.invoke_i

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_i", "kind": "function", "type_index": 2, "function_index": 21, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94069, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddi:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idi:function(index,a1,a2){var sp=stackSave();try{return dynCall_idi(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idiiii:fu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30757"></a>
## FND-30757 — module-002 import env.invoke_viiiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiii", "kind": "function", "type_index": 43, "function_index": 22, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106290, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stackSave();try{dynCall_viiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10){var sp=stackSave();try{dynCall_viiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30758"></a>
## FND-30758 — module-002 import env.invoke_iiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiii", "kind": "function", "type_index": 15, "function_index": 23, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96372, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynC", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30759"></a>
## FND-30759 — module-002 import env.invoke_iiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiii", "kind": "function", "type_index": 13, "function_index": 24, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95990, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}cat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30760"></a>
## FND-30760 — module-002 import env.invoke_jij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jij", "kind": "function", "type_index": 25, "function_index": 25, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101749, "loader_excerpt": "a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCall_jij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30761"></a>
## FND-30761 — module-002 import env.__cxa_find_matching_catch_4

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_4", "kind": "function", "type_index": 3, "function_index": 26, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74983, "loader_excerpt": "ching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw n", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30762"></a>
## FND-30762 — module-002 import env.invoke_iijiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iijiii", "kind": "function", "type_index": 102, "function_index": 27, "signature": {"parameters": ["i32", "i32", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99590, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30763"></a>
## FND-30763 — module-002 import env.invoke_iijjiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iijjiii", "kind": "function", "type_index": 103, "function_index": 28, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99972, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30764"></a>
## FND-30764 — module-002 import env.invoke_iiji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiji", "kind": "function", "type_index": 44, "function_index": 29, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99411, "loader_excerpt": "iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRe", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30765"></a>
## FND-30765 — module-002 import env.invoke_iijji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iijji", "kind": "function", "type_index": 104, "function_index": 30, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99785, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30766"></a>
## FND-30766 — module-002 import env.invoke_vjjii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vjjii", "kind": "function", "type_index": 85, "function_index": 31, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109648, "loader_excerpt": "vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPr", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30767"></a>
## FND-30767 — module-002 import env.invoke_ijjiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_ijjiiii", "kind": "function", "type_index": 105, "function_index": 32, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100175, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30768"></a>
## FND-30768 — module-002 import env.invoke_vdii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vdii", "kind": "function", "type_index": 67, "function_index": 33, "signature": {"parameters": ["i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102078, "loader_excerpt": "dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30769"></a>
## FND-30769 — module-002 import env.invoke_idiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_idiiii", "kind": "function", "type_index": 106, "function_index": 34, "signature": {"parameters": ["i32", "f64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94753, "loader_excerpt": "idi(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_idiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ii:function(index,a1){var sp=stackSave();try{return dynCall_ii(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iid:function(index,a1,a2){var sp=stackSave();try{return dynCall_iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30770"></a>
## FND-30770 — module-002 import env.invoke_vji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vji", "kind": "function", "type_index": 33, "function_index": 35, "signature": {"parameters": ["i32", "i64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109484, "loader_excerpt": "vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30771"></a>
## FND-30771 — module-002 import env.__cxa_rethrow

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_rethrow", "kind": "function", "type_index": 12, "function_index": 36, "signature": {"parameters": [], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75137, "loader_excerpt": "atch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptio", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30772"></a>
## FND-30772 — module-002 import env.invoke_viiji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiji", "kind": "function", "type_index": 45, "function_index": 37, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108952, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30773"></a>
## FND-30773 — module-002 import env.__cxa_find_matching_catch_5

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_5", "kind": "function", "type_index": 4, "function_index": 38, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75055, "loader_excerpt": "=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_r", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30774"></a>
## FND-30774 — module-002 import env.invoke_iij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iij", "kind": "function", "type_index": 26, "function_index": 39, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99240, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30775"></a>
## FND-30775 — module-002 import env.invoke_iif

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iif", "kind": "function", "type_index": 107, "function_index": 40, "signature": {"parameters": ["i32", "i32", "f32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95282, "loader_excerpt": "iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30776"></a>
## FND-30776 — module-002 import env.invoke_viiiffi

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiffi", "kind": "function", "type_index": 108, "function_index": 41, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f32", "f32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104722, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiffi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiffi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(sta", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30777"></a>
## FND-30777 — module-002 import env.invoke_jiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jiii", "kind": "function", "type_index": 38, "function_index": 42, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100732, "loader_excerpt": "a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_ji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30778"></a>
## FND-30778 — module-002 import env.invoke_jii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jii", "kind": "function", "type_index": 20, "function_index": 43, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100551, "loader_excerpt": "ex,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30779"></a>
## FND-30779 — module-002 import env.invoke_jiiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jiiiiiii", "kind": "function", "type_index": 109, "function_index": 44, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101118, "loader_excerpt": "a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiijjj(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCal", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
