# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30420"></a>
## FND-30420 — module-001 new controlled instantiation

Bounded Node instantiation succeeded with explicitly stubbed imports; this is not engine search/review correctness. Initial module003failed due unhandled imported memory,then passed using exact descriptor limits. Stack-query exports were called only when present.

- Category: wasm_runtime
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No native whole-game review rerun,new server query,or cloud parity test. Historical successful full CEE/Human tests retained separately.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/runtime-observation.json)

```text
{"status": "instantiated with function import stubs", "imports": 154, "exports": 152, "memories": [{"name": "memory", "bytes": 404750336, "shared": false}], "import_calls_during_instantiation": [], "elapsed_ms": 145.148545, "algorithm_calls": [{"name": "emscripten_stack_get_current", "result": 26689936}], "limitation": "No wrapper runtime constructors/search/review invoked; stub instantiation is not a functional engine validation. No original application inputs used."}
```

<a id="FND-30421"></a>
## FND-30421 — module-001 import env.invoke_vii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vii", "kind": "function", "type_index": 5, "function_index": 0, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103089, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30422"></a>
## FND-30422 — module-001 import env.__cxa_find_matching_catch_3

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_3", "kind": "function", "type_index": 2, "function_index": 1, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74910, "loader_excerpt": "ion_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new Cpp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30423"></a>
## FND-30423 — module-001 import env.llvm_eh_typeid_for

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "llvm_eh_typeid_for", "kind": "function", "type_index": 2, "function_index": 2, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 109894, "loader_excerpt": "y=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),wasmExports.__wasm_call_ctors(),FS.ignorePermissions=!1,Module.onRuntimeInitialized?.(),function(){var postRun=Module.postRun;postRun&&(\"function\"==typeof po", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30424"></a>
## FND-30424 — module-001 import env.__cxa_begin_catch

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_begin_catch", "kind": "function", "type_index": 2, "function_index": 3, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74318, "loader_excerpt": "nsole).awaitLines(id,Module.ceeInterruptMailbox);return null===joined?0:stringToNewUTF8(joined)}))},__cxa_begin_catch:ptr=>{var info=new ExceptionInfo(ptr);return info.get_caught()||(info.set_caught(!0),uncaughtExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught.length)return 0;var info=exceptionCaught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30425"></a>
## FND-30425 — module-001 import env.invoke_viii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viii", "kind": "function", "type_index": 6, "function_index": 4, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103605, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiddi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiddi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidi:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiidi(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30426"></a>
## FND-30426 — module-001 import env.invoke_iiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiii", "kind": "function", "type_index": 10, "function_index": 5, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95798, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30427"></a>
## FND-30427 — module-001 import env.invoke_ii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_ii", "kind": "function", "type_index": 3, "function_index": 6, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94935, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ii:function(index,a1){var sp=stackSave();try{return dynCall_ii(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iid:function(index,a1,a2){var sp=stackSave();try{return dynCall_iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(in", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30428"></a>
## FND-30428 — module-001 import env.exit

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "exit", "kind": "function", "type_index": 0, "function_index": 7, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 90052, "loader_excerpt": "tring of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30429"></a>
## FND-30429 — module-001 import env.invoke_vi

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vi", "kind": "function", "type_index": 1, "function_index": 8, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102237, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30430"></a>
## FND-30430 — module-001 import env.__cxa_find_matching_catch_2

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_2", "kind": "function", "type_index": 8, "function_index": 9, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74856, "loader_excerpt": "var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30431"></a>
## FND-30431 — module-001 import env.__cxa_end_catch

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_end_catch", "kind": "function", "type_index": 13, "function_index": 10, "signature": {"parameters": [], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74720, "loader_excerpt": "ught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_e", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30432"></a>
## FND-30432 — module-001 import env.invoke_v

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_v", "kind": "function", "type_index": 0, "function_index": 11, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101917, "loader_excerpt": "a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stac", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30433"></a>
## FND-30433 — module-001 import env.__resumeException

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__resumeException", "kind": "function", "type_index": 0, "function_index": 12, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 75884, "loader_excerpt": "n(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return stream.flags=-289793&stream.flags|289792&arg,0;case 12:arg=syscallGetVarargP();return HEAP16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64:function(fd,buf){try{return SYSCALLS.writeStat(buf,F", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30434"></a>
## FND-30434 — module-001 import env.invoke_iii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iii", "kind": "function", "type_index": 4, "function_index": 13, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95440, "loader_excerpt": "iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30435"></a>
## FND-30435 — module-001 import env.__cxa_throw

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_throw", "kind": "function", "type_index": 5, "function_index": 14, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75627, "loader_excerpt": "ughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return st", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30436"></a>
## FND-30436 — module-001 import env.invoke_iiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiiii", "kind": "function", "type_index": 21, "function_index": 15, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96554, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_iiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30437"></a>
## FND-30437 — module-001 import env.__assert_fail

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__assert_fail", "kind": "function", "type_index": 6, "function_index": 16, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 73883, "loader_excerpt": "ge({error:\"CEE was unable to write a proto message to a js buffer\"})}};var wasmExports,wasmImports={__assert_fail:(condition,filename,line,func)=>abort(`Assertion failed: ${UTF8ToString(condition)}, at: `+[filename?UTF8ToString(filename):\"unknown filename\",line,func?UTF8ToString(func):\"unknown function\"]),__asyncjs__cee_worker_await_lines:function(id){return Asyncify.handleAsync((async()=>{var joined=await engineWorkersOf(Module,console).awaitLines(id,Module.ceeInterruptMailbox);return null===joined?0:stringToNewUTF8(joined)}))},__cxa_begin_catch:ptr=>{var info=new ExceptionInfo(ptr);return info.get_caught()||(info.set_caught(!0),uncaughtExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30438"></a>
## FND-30438 — module-001 import env.invoke_viiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiii", "kind": "function", "type_index": 7, "function_index": 17, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104733, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30439"></a>
## FND-30439 — module-001 import env.invoke_viiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiii", "kind": "function", "type_index": 16, "function_index": 18, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105493, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30440"></a>
## FND-30440 — module-001 import env.invoke_viiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiii", "kind": "function", "type_index": 9, "function_index": 19, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105305, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30441"></a>
## FND-30441 — module-001 import env.invoke_ji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_ji", "kind": "function", "type_index": 14, "function_index": 20, "signature": {"parameters": ["i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100365, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Emscripte", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30442"></a>
## FND-30442 — module-001 import env.invoke_i

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_i", "kind": "function", "type_index": 2, "function_index": 21, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94056, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddi:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idi:function(index,a1,a2){var sp=stackSave();try{return dynCall_idi(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idiiii:fu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30443"></a>
## FND-30443 — module-001 import env.invoke_viiiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiii", "kind": "function", "type_index": 43, "function_index": 22, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106105, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stackSave();try{dynCall_viiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10){var sp=stackSave();try{dynCall_viiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30444"></a>
## FND-30444 — module-001 import env.invoke_iiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiii", "kind": "function", "type_index": 15, "function_index": 23, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96359, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynC", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30445"></a>
## FND-30445 — module-001 import env.invoke_iiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiii", "kind": "function", "type_index": 12, "function_index": 24, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95977, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}cat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30446"></a>
## FND-30446 — module-001 import env.invoke_jij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jij", "kind": "function", "type_index": 25, "function_index": 25, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101736, "loader_excerpt": "a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCall_jij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30447"></a>
## FND-30447 — module-001 import env.__cxa_find_matching_catch_4

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_4", "kind": "function", "type_index": 3, "function_index": 26, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74970, "loader_excerpt": "ching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw n", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30448"></a>
## FND-30448 — module-001 import env.invoke_iijiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iijiii", "kind": "function", "type_index": 100, "function_index": 27, "signature": {"parameters": ["i32", "i32", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99577, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30449"></a>
## FND-30449 — module-001 import env.invoke_iijjiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iijjiii", "kind": "function", "type_index": 101, "function_index": 28, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99959, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30450"></a>
## FND-30450 — module-001 import env.invoke_iiji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiji", "kind": "function", "type_index": 44, "function_index": 29, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99398, "loader_excerpt": "iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRe", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30451"></a>
## FND-30451 — module-001 import env.invoke_iijji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iijji", "kind": "function", "type_index": 102, "function_index": 30, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99772, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijjiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iijjiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30452"></a>
## FND-30452 — module-001 import env.invoke_vjjii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vjjii", "kind": "function", "type_index": 83, "function_index": 31, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109463, "loader_excerpt": "vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPr", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30453"></a>
## FND-30453 — module-001 import env.invoke_ijjiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_ijjiiii", "kind": "function", "type_index": 103, "function_index": 32, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100162, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ijjiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_ijjiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ji:function(index,a1){var sp=stackSave();try{return dynCall_ji(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30454"></a>
## FND-30454 — module-001 import env.invoke_vdii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vdii", "kind": "function", "type_index": 67, "function_index": 33, "signature": {"parameters": ["i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102065, "loader_excerpt": "dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:function(index,a1){var sp=stackSave();try{dynCall_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30455"></a>
## FND-30455 — module-001 import env.invoke_idiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_idiiii", "kind": "function", "type_index": 104, "function_index": 34, "signature": {"parameters": ["i32", "f64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94740, "loader_excerpt": "idi(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_idiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_ii:function(index,a1){var sp=stackSave();try{return dynCall_ii(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iid:function(index,a1,a2){var sp=stackSave();try{return dynCall_iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30456"></a>
## FND-30456 — module-001 import env.invoke_vji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vji", "kind": "function", "type_index": 33, "function_index": 35, "signature": {"parameters": ["i32", "i64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109299, "loader_excerpt": "vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30457"></a>
## FND-30457 — module-001 import env.__cxa_rethrow

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_rethrow", "kind": "function", "type_index": 13, "function_index": 36, "signature": {"parameters": [], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75124, "loader_excerpt": "atch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptio", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30458"></a>
## FND-30458 — module-001 import env.invoke_viiji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiji", "kind": "function", "type_index": 45, "function_index": 37, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108767, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30459"></a>
## FND-30459 — module-001 import env.__cxa_find_matching_catch_5

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_find_matching_catch_5", "kind": "function", "type_index": 4, "function_index": 38, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75042, "loader_excerpt": "=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-1),ptr=info.excPtr;throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_r", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30460"></a>
## FND-30460 — module-001 import env.invoke_iij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iij", "kind": "function", "type_index": 26, "function_index": 39, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99227, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iijji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30461"></a>
## FND-30461 — module-001 import env.invoke_iif

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iif", "kind": "function", "type_index": 105, "function_index": 40, "signature": {"parameters": ["i32", "i32", "f32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95269, "loader_excerpt": "iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30462"></a>
## FND-30462 — module-001 import env.invoke_viiiffi

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiffi", "kind": "function", "type_index": 106, "function_index": 41, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f32", "f32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104537, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiffi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiffi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(sta", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30463"></a>
## FND-30463 — module-001 import env.invoke_jiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jiii", "kind": "function", "type_index": 38, "function_index": 42, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100719, "loader_excerpt": "a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_ji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30464"></a>
## FND-30464 — module-001 import env.invoke_jii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jii", "kind": "function", "type_index": 20, "function_index": 43, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100538, "loader_excerpt": "ex,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jii:function(index,a1,a2){var sp=stackSave();try{return dynCall_jii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30465"></a>
## FND-30465 — module-001 import env.invoke_jiiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jiiiiiii", "kind": "function", "type_index": 107, "function_index": 44, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101105, "loader_excerpt": "a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiijjj(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCal", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30466"></a>
## FND-30466 — module-001 import env.invoke_iiiij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiij", "kind": "function", "type_index": 39, "function_index": 45, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98089, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30467"></a>
## FND-30467 — module-001 import env.invoke_iiij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiij", "kind": "function", "type_index": 34, "function_index": 46, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98479, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e in", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30468"></a>
## FND-30468 — module-001 import env.invoke_jiij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jiij", "kind": "function", "type_index": 68, "function_index": 47, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101547, "loader_excerpt": "a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCall_jij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30469"></a>
## FND-30469 — module-001 import env.invoke_jiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jiiii", "kind": "function", "type_index": 108, "function_index": 48, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100908, "loader_excerpt": "a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiijjj(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{r", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30470"></a>
## FND-30470 — module-001 import env.invoke_vij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vij", "kind": "function", "type_index": 24, "function_index": 49, "signature": {"parameters": ["i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109135, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).sl", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30471"></a>
## FND-30471 — module-001 import env.invoke_jiiiijjj

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_jiiiijjj", "kind": "function", "type_index": 109, "function_index": 50, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64", "i64"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101326, "loader_excerpt": "a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiijjj(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCall_jij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30472"></a>
## FND-30472 — module-001 import env.invoke_iiiji

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiji", "kind": "function", "type_index": 110, "function_index": 51, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98658, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30473"></a>
## FND-30473 — module-001 import env.invoke_viiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiii", "kind": "function", "type_index": 18, "function_index": 52, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105901, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stackSave();try{dynCall_viiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30474"></a>
## FND-30474 — module-001 import env.cee_worker_spawn

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "cee_worker_spawn", "kind": "function", "type_index": 2, "function_index": 53, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88465, "loader_excerpt": "rker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscript", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30475"></a>
## FND-30475 — module-001 import env.cee_worker_terminate

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "cee_worker_terminate", "kind": "function", "type_index": 0, "function_index": 54, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88561, "loader_excerpt": ":0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)retu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30476"></a>
## FND-30476 — module-001 import env.cee_worker_post

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "cee_worker_post", "kind": "function", "type_index": 3, "function_index": 55, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88359, "loader_excerpt": "engineWorkersOf(Module,console).error(id);return null===description?0:stringToNewUTF8(description)},cee_worker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30477"></a>
## FND-30477 — module-001 import env.cee_worker_error

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "cee_worker_error", "kind": "function", "type_index": 2, "function_index": 56, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88213, "loader_excerpt": "n(){var command=Module.ceeInterruptMailbox.take();return null===command?0:stringToNewUTF8(command)},cee_worker_error:function(id){var description=engineWorkersOf(Module,console).error(id);return null===description?0:stringToNewUTF8(description)},cee_worker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3)", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30478"></a>
## FND-30478 — module-001 import env.__asyncjs__cee_worker_await_lines

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__asyncjs__cee_worker_await_lines", "kind": "function", "type_index": 2, "function_index": 57, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 74090, "loader_excerpt": "ilename?UTF8ToString(filename):\"unknown filename\",line,func?UTF8ToString(func):\"unknown function\"]),__asyncjs__cee_worker_await_lines:function(id){return Asyncify.handleAsync((async()=>{var joined=await engineWorkersOf(Module,console).awaitLines(id,Module.ceeInterruptMailbox);return null===joined?0:stringToNewUTF8(joined)}))},__cxa_begin_catch:ptr=>{var info=new ExceptionInfo(ptr);return info.get_caught()||(info.set_caught(!0),uncaughtExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught.length)return 0;var info=exceptionCaught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30479"></a>
## FND-30479 — module-001 import env.cee_take_uci_interrupt

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "cee_take_uci_interrupt", "kind": "function", "type_index": 8, "function_index": 58, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88083, "loader_excerpt": "mmerName,dst_name,17)):(stringToUTF8(winterName,dst_name,17),stringToUTF8(summerName,std_name,17))},cee_take_uci_interrupt:function(){var command=Module.ceeInterruptMailbox.take();return null===command?0:stringToNewUTF8(command)},cee_worker_error:function(id){var description=engineWorkersOf(Module,console).error(id);return null===description?0:stringToNewUTF8(description)},cee_worker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&cl", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
