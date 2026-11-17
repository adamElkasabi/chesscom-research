# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30480"></a>
## FND-30480 — module-001 import env.invoke_vidii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vidii", "kind": "function", "type_index": 111, "function_index": 59, "signature": {"parameters": ["i32", "i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102565, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30481"></a>
## FND-30481 — module-001 import env.invoke_dii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_dii", "kind": "function", "type_index": 46, "function_index": 60, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92576, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30482"></a>
## FND-30482 — module-001 import env.invoke_fii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_fii", "kind": "function", "type_index": 47, "function_index": 61, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93300, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30483"></a>
## FND-30483 — module-001 import env.invoke_di

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_di", "kind": "function", "type_index": 19, "function_index": 62, "signature": {"parameters": ["i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92055, "loader_excerpt": "turn HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},invoke_di:function(index,a1){var sp=stackSave();try{return dynCall_di(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_did:function(index,a1,a2){var sp=stackSave();try{return dynCall_did(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diddd:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_diddd(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30484"></a>
## FND-30484 — module-001 import env.js_alloc

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "js_alloc", "kind": "function", "type_index": 2, "function_index": 63, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 109643, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30485"></a>
## FND-30485 — module-001 import env.emscripten_asm_const_int

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "emscripten_asm_const_int", "kind": "function", "type_index": 4, "function_index": 64, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 88954, "loader_excerpt": "ow():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;fo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30486"></a>
## FND-30486 — module-001 import env.js_post_proto

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "js_post_proto", "kind": "function", "type_index": 5, "function_index": 65, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 109737, "loader_excerpt": ",0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30487"></a>
## FND-30487 — module-001 import env.js_free

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "js_free", "kind": "function", "type_index": 0, "function_index": 66, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 109696, "loader_excerpt": "tanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSIn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30488"></a>
## FND-30488 — module-001 import env.invoke_fiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_fiii", "kind": "function", "type_index": 53, "function_index": 67, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93471, "loader_excerpt": "fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30489"></a>
## FND-30489 — module-001 import env.invoke_iiiiiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiiiiiiiii", "kind": "function", "type_index": 54, "function_index": 68, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 97187, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11){var sp=stackSave();try{return dynCall_iiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{return dynCall_iiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiij:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiij(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30490"></a>
## FND-30490 — module-001 import env.invoke_iiijii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiijii", "kind": "function", "type_index": 48, "function_index": 69, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98845, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30491"></a>
## FND-30491 — module-001 import env.invoke_viij

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viij", "kind": "function", "type_index": 23, "function_index": 70, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108595, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30492"></a>
## FND-30492 — module-001 import env.invoke_iiiijii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiijii", "kind": "function", "type_index": 84, "function_index": 71, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98276, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRe", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30493"></a>
## FND-30493 — module-001 import env.invoke_iiijj

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiijj", "kind": "function", "type_index": 85, "function_index": 72, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99040, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30494"></a>
## FND-30494 — module-001 import env.invoke_viiijii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiijii", "kind": "function", "type_index": 112, "function_index": 73, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108399, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30495"></a>
## FND-30495 — module-001 import env.invoke_viijii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viijii", "kind": "function", "type_index": 55, "function_index": 74, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108947, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30496"></a>
## FND-30496 — module-001 import env.invoke_viiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiiii", "kind": "function", "type_index": 27, "function_index": 75, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106317, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stackSave();try{dynCall_viiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10){var sp=stackSave();try{dynCall_viiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{dynCall_viiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30497"></a>
## FND-30497 — module-001 import env.invoke_iid

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iid", "kind": "function", "type_index": 86, "function_index": 76, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95098, "loader_excerpt": "all_ii(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iid:function(index,a1,a2){var sp=stackSave();try{return dynCall_iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30498"></a>
## FND-30498 — module-001 import env.invoke_viid

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viid", "kind": "function", "type_index": 40, "function_index": 77, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103253, "loader_excerpt": "vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30499"></a>
## FND-30499 — module-001 import env.invoke_fiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_fiiiiiiii", "kind": "function", "type_index": 113, "function_index": 78, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93837, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddi:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30500"></a>
## FND-30500 — module-001 import env.invoke_diiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_diiiii", "kind": "function", "type_index": 114, "function_index": 79, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93105, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30501"></a>
## FND-30501 — module-001 import env.invoke_viiiid

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiid", "kind": "function", "type_index": 115, "function_index": 80, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104913, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30502"></a>
## FND-30502 — module-001 import env.invoke_viiidi

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiidi", "kind": "function", "type_index": 87, "function_index": 81, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104153, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidi:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiidi(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiidii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiffi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiffi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30503"></a>
## FND-30503 — module-001 import env.invoke_vifii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vifii", "kind": "function", "type_index": 116, "function_index": 82, "signature": {"parameters": ["i32", "i32", "f32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102909, "loader_excerpt": "vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30504"></a>
## FND-30504 — module-001 import env.invoke_viiiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiii", "kind": "function", "type_index": 88, "function_index": 83, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106537, "loader_excerpt": ",a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10){var sp=stackSave();try{dynCall_viiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{dynCall_viiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13){var sp=stackSave();try{dynCall_viiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30505"></a>
## FND-30505 — module-001 import env.invoke_viiiiiiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiiii", "kind": "function", "type_index": 69, "function_index": 84, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107017, "loader_excerpt": ",a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13){var sp=stackSave();try{dynCall_viiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14){var sp=stackSave();try{dynCall_viiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15){var sp=stackSave();try{dynCall_viiiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30506"></a>
## FND-30506 — module-001 import env.invoke_diii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_diii", "kind": "function", "type_index": 70, "function_index": 85, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92926, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30507"></a>
## FND-30507 — module-001 import env.invoke_iiidi

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiidi", "kind": "function", "type_index": 117, "function_index": 86, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95611, "loader_excerpt": "iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e in", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30508"></a>
## FND-30508 — module-001 import env._embind_register_void

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_void", "kind": "function", "type_index": 1, "function_index": 87, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 84597, "loader_excerpt": "uctors.push(_free,ptr),ptr},readValueFromPointer:readPointer,destructorFunction(ptr){_free(ptr)}})},_embind_register_void:(rawType,name)=>{registerType(rawType,{isVoid:!0,name:name=AsciiToString(name),fromWireType:()=>{},toWireType:(destructors,o)=>{}})},_gmtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getUTCSeconds(),HEAP32[tmPtr+4>>2]=date.getUTCMinutes(),HEAP32[tmPtr+8>>2]=date.getUTCHours(),HEAP32[tmPtr+12>>2]=date.getUTCDate(),HEAP32[tmPtr+16>>2]=date.getUTCMonth(),HEAP32[tmPtr+20>>2]=date.getUTCFullYear()-1900,HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,0},_localtime_js:funct", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30509"></a>
## FND-30509 — module-001 import env._embind_register_bool

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_bool", "kind": "function", "type_index": 6, "function_index": 88, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81309, "loader_excerpt": "dValueFromPointer:integerReadValueFromPointer(name,size,!isUnsignedType),destructorFunction:null})},_embind_register_bool:(rawType,name,trueValue,falseValue)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:function(wt){return!!wt},toWireType:function(destructors,o){return o?trueValue:falseValue},readValueFromPointer:function(pointer){return this.fromWireType(HEAPU8[pointer])},destructorFunction:null})},_embind_register_emval:rawType=>registerType(rawType,EmValType),_embind_register_float:(rawType,name,size)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:value=>value,toWireType:(destructors,value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRan", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30510"></a>
## FND-30510 — module-001 import env._embind_register_integer

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_integer", "kind": "function", "type_index": 7, "function_index": 89, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81944, "loader_excerpt": ",value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);let fromWireType=value=>value;if(0===minRange){var bitshift=32-8*size;fromWireType=value=>value<<bitshift>>>bitshift,maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>value,readValueFromPointer:integerReadValueFromPointer(name,size,0!==minRange),destructorFunction:null})},_embind_register_memory_view:(rawType,dataTypeIndex,name)=>{var TA=[Int8Array,Uint8Array,Int16Array,Uint16Array,Int32Array,Uint32Array,Float32Array,Float64Array,BigInt64Array,BigUint64Array][dataTypeIndex];function decodeMemoryView(handle){var size=HEAP", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30511"></a>
## FND-30511 — module-001 import env._embind_register_bigint

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_bigint", "kind": "function", "type_index": 158, "function_index": 90, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i64"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 80774, "loader_excerpt": "h))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType=0n===minRange;let fromWireType=value=>value;if(isUnsignedType){const bitSize=8*size;fromWireType=value=>BigInt.asUintN(bitSize,value),maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>(\"number\"==typeof value&&(value=BigInt(value)),value),readValueFromPointer:integerReadValueFromPointer(name,size,!isUnsignedType),destructorFunction:null})},_embind_register_bool:(rawType,name,trueValue,falseValue)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:function(wt){return!!wt},toWireType:func", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30512"></a>
## FND-30512 — module-001 import env._embind_register_float

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_float", "kind": "function", "type_index": 5, "function_index": 91, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81698, "loader_excerpt": "inter])},destructorFunction:null})},_embind_register_emval:rawType=>registerType(rawType,EmValType),_embind_register_float:(rawType,name,size)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:value=>value,toWireType:(destructors,value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);let fromWireType=value=>value;if(0===minRange){var bitshift=32-8*size;fromWireType=value=>value<<bitshift>>>bitshift,maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>value,readValueFromPointer:integerReadValueFromPointer(name,size,0!==minRange),destructorFunction:null})},_embind", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30513"></a>
## FND-30513 — module-001 import env._embind_register_std_string

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_std_string", "kind": "function", "type_index": 1, "function_index": 92, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 82880, "loader_excerpt": "ireType:decodeMemoryView,readValueFromPointer:decodeMemoryView},{ignoreDuplicateRegistrations:!0})},_embind_register_std_string:(rawType,name)=>{name=AsciiToString(name);registerType(rawType,{name:name,fromWireType(value){var str,length=HEAPU32[value>>2],payload=value+4;return str=UTF8ToString(payload,length,!0),_free(value),str},toWireType(destructors,value){var length;value instanceof ArrayBuffer&&(value=new Uint8Array(value));var valueIsOfTypeString=\"string\"==typeof value;valueIsOfTypeString||ArrayBuffer.isView(value)&&1==value.BYTES_PER_ELEMENT||throwBindingError(\"Cannot pass non-string to std::string\"),length=valueIsOfTypeString?lengthBytesUTF8(value):value.length;var base=_malloc(4+length+1),ptr=base+4;(HEAPU32[base>>2]=length,valueIsOfTypeString)?stringToUTF8(value,ptr,length+1):HEA", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30514"></a>
## FND-30514 — module-001 import env._embind_register_std_wstring

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_std_wstring", "kind": "function", "type_index": 5, "function_index": 93, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 83733, "loader_excerpt": "tors.push(_free,base),base},readValueFromPointer:readPointer,destructorFunction(ptr){_free(ptr)}})},_embind_register_std_wstring:(rawType,charSize,name)=>{var decodeString,encodeString,lengthBytesUTF;name=AsciiToString(name),2===charSize?(decodeString=UTF16ToString,encodeString=stringToUTF16,lengthBytesUTF=lengthBytesUTF16):(decodeString=UTF32ToString,encodeString=stringToUTF32,lengthBytesUTF=lengthBytesUTF32),registerType(rawType,{name:name,fromWireType:value=>{var length=HEAPU32[value>>2],str=decodeString(value+4,length*charSize,!0);return _free(value),str},toWireType:(destructors,value)=>{\"string\"!=typeof value&&throwBindingError(`Cannot pass non-string to C++ string type ${name}`);var length=lengthBytesUTF(value),ptr=_malloc(4+length+charSize);return HEAPU32[ptr>>2]=length/charSize,enc", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30515"></a>
## FND-30515 — module-001 import env._embind_register_emval

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_emval", "kind": "function", "type_index": 0, "function_index": 94, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81634, "loader_excerpt": "FromPointer:function(pointer){return this.fromWireType(HEAPU8[pointer])},destructorFunction:null})},_embind_register_emval:rawType=>registerType(rawType,EmValType),_embind_register_float:(rawType,name,size)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:value=>value,toWireType:(destructors,value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);let fromWireType=value=>value;if(0===minRange){var bitshift=32-8*size;fromWireType=value=>value<<bitshift>>>bitshift,maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>value,readValueFromPointer:integerReadValueFromPo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30516"></a>
## FND-30516 — module-001 import env._embind_register_memory_view

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_embind_register_memory_view", "kind": "function", "type_index": 5, "function_index": 95, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 82391, "loader_excerpt": "readValueFromPointer:integerReadValueFromPointer(name,size,0!==minRange),destructorFunction:null})},_embind_register_memory_view:(rawType,dataTypeIndex,name)=>{var TA=[Int8Array,Uint8Array,Int16Array,Uint16Array,Int32Array,Uint32Array,Float32Array,Float64Array,BigInt64Array,BigUint64Array][dataTypeIndex];function decodeMemoryView(handle){var size=HEAPU32[handle>>2],data=HEAPU32[handle+4>>2];return new TA(HEAP8.buffer,data,size)}registerType(rawType,{name:name=AsciiToString(name),fromWireType:decodeMemoryView,readValueFromPointer:decodeMemoryView},{ignoreDuplicateRegistrations:!0})},_embind_register_std_string:(rawType,name)=>{name=AsciiToString(name);registerType(rawType,{name:name,fromWireType(value){var str,length=HEAPU32[value>>2],payload=value+4;return str=UTF8ToString(payload,length,!", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30517"></a>
## FND-30517 — module-001 import env.invoke_vidi

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vidi", "kind": "function", "type_index": 71, "function_index": 96, "signature": {"parameters": ["i32", "i32", "f64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102393, "loader_excerpt": "all_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30518"></a>
## FND-30518 — module-001 import env.invoke_viiiiiiiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiiiii", "kind": "function", "type_index": 56, "function_index": 97, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107277, "loader_excerpt": "a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14){var sp=stackSave();try{dynCall_viiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15){var sp=stackSave();try{dynCall_viiiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiij:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiij(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30519"></a>
## FND-30519 — module-001 import env.invoke_viiiiiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiii", "kind": "function", "type_index": 57, "function_index": 98, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106767, "loader_excerpt": "a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{dynCall_viiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13){var sp=stackSave();try{dynCall_viiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14){var sp=stackSave();try{dynCall_viiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14)}cat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30520"></a>
## FND-30520 — module-001 import env.invoke_vif

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_vif", "kind": "function", "type_index": 118, "function_index": 99, "signature": {"parameters": ["i32", "i32", "f32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102745, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:functio", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30521"></a>
## FND-30521 — module-001 import env.invoke_viiiiiij

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiij", "kind": "function", "type_index": 119, "function_index": 100, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107827, "loader_excerpt": "a12,a13,a14,a15)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiij:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiij(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiji(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(sta", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30522"></a>
## FND-30522 — module-001 import env.invoke_viiid

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiid", "kind": "function", "type_index": 58, "function_index": 101, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103777, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiddi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiddi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidi:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiidi(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiidii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30523"></a>
## FND-30523 — module-001 import env.invoke_did

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_did", "kind": "function", "type_index": 59, "function_index": 102, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92218, "loader_excerpt": "all_di(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_did:function(index,a1,a2){var sp=stackSave();try{return dynCall_did(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diddd:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_diddd(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30524"></a>
## FND-30524 — module-001 import env.invoke_diid

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_diid", "kind": "function", "type_index": 120, "function_index": 103, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92747, "loader_excerpt": "dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30525"></a>
## FND-30525 — module-001 import env.invoke_iddd

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iddd", "kind": "function", "type_index": 121, "function_index": 104, "signature": {"parameters": ["i32", "f64", "f64", "f64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94211, "loader_excerpt": "dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddi:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idi:function(index,a1,a2){var sp=stackSave();try{return dynCall_idi(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_idiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30526"></a>
## FND-30526 — module-001 import env.invoke_viidi

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viidi", "kind": "function", "type_index": 60, "function_index": 105, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103425, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiddi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiddi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30527"></a>
## FND-30527 — module-001 import env.invoke_viiiidii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiidii", "kind": "function", "type_index": 122, "function_index": 106, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105101, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30528"></a>
## FND-30528 — module-001 import env.invoke_diddd

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_diddd", "kind": "function", "type_index": 123, "function_index": 107, "signature": {"parameters": ["i32", "i32", "f64", "f64", "f64"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92389, "loader_excerpt": "did(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diddd:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_diddd(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30529"></a>
## FND-30529 — module-001 import env.invoke_viiidii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiidii", "kind": "function", "type_index": 72, "function_index": 108, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104341, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiidii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiffi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiffi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30530"></a>
## FND-30530 — module-001 import env.invoke_fiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_fiiii", "kind": "function", "type_index": 124, "function_index": 109, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93650, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30531"></a>
## FND-30531 — module-001 import env.invoke_viiiiiiff

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiff", "kind": "function", "type_index": 125, "function_index": 110, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "f32", "f32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105689, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stac", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30532"></a>
## FND-30532 — module-001 import env.invoke_viiij

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiij", "kind": "function", "type_index": 126, "function_index": 111, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108031, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiji(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30533"></a>
## FND-30533 — module-001 import env.invoke_iiiiiiiii

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiiiiii", "kind": "function", "type_index": 61, "function_index": 112, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96968, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_iiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11){var sp=stackSave();try{return dynCall_iiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{return dynCall_iiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))th", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30534"></a>
## FND-30534 — module-001 import env.invoke_viiiji

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
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiji", "kind": "function", "type_index": 73, "function_index": 113, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108211, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiji(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30535"></a>
## FND-30535 — module-001 import env.emscripten_sleep

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "emscripten_sleep", "kind": "function", "type_index": 0, "function_index": 114, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89558, "loader_excerpt": "nMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=>{var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;for(var string of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf)", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30536"></a>
## FND-30536 — module-001 import env.__syscall_fcntl64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_fcntl64", "kind": "function", "type_index": 4, "function_index": 115, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 75982, "loader_excerpt": "t,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return stream.flags=-289793&stream.flags|289792&arg,0;case 12:arg=syscallGetVarargP();return HEAP16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64:function(fd,buf){try{return SYSCALLS.writeStat(buf,FS.fstat(fd))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_get", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30537"></a>
## FND-30537 — module-001 import env.__syscall_ioctl

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_ioctl", "kind": "function", "type_index": 4, "function_index": 116, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 77598, "loader_excerpt": "lseek(stream,280*idx,0),pos}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_ioctl:function(fd,op,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(op){case 21509:case 21510:case 21511:case 21512:case 21524:case 21515:return stream.tty?0:-59;case 21505:if(!stream.tty)return-59;if(stream.tty.ops.ioctl_tcgets){var termios=stream.tty.ops.ioctl_tcgets(stream),argp=syscallGetVarargP();HEAP32[argp>>2]=termios.c_iflag||0,HEAP32[argp+4>>2]=termios.c_oflag||0,HEAP32[argp+8>>2]=termios.c_cflag||0,HEAP32[argp+12>>2]=termios.c_lflag||0;for(var i=0;i<32;i++)HEAP8[argp+i+17]=termios.c_cc[i]||0;return 0}return 0;case 21506:case 21507:case 21508:if(!stream.tty)return-59;if(stream.tty.ops.ioctl_tcsets){argp=syscallGetVarargP();var c_iflag=", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30538"></a>
## FND-30538 — module-001 import wasi_snapshot_preview1.fd_close

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_close", "kind": "function", "type_index": 2, "function_index": 117, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 90063, "loader_excerpt": "rings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len,offset)}ca", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30539"></a>
## FND-30539 — module-001 import wasi_snapshot_preview1.fd_read

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_read", "kind": "function", "type_index": 10, "function_index": 118, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 90547, "loader_excerpt": "P64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len,offset)}catch(e){if(ret>0&&e instanceof FS.ErrnoError&&(6==e.errno||6==e.errno))break;throw e}if(curr<0)return-1;if(ret+=curr,curr<len)break;void 0!==offset&&(offset+=curr)}return ret})(SYSCALLS.getStreamFromFD(fd),iov,iovcnt);return HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_seek:function(fd,offset,whence,newOffset){offset=bigintToI53Checked(offset);try{if(isNaN(offset))return 22;var stream=SYSCALLS.getStreamFromFD(fd);return FS.llsee", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
