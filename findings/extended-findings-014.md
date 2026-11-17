# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30780"></a>
## FND-30780 — module-002 import env.invoke_iiiij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiij", "kind": "function", "type_index": 39, "function_index": 45, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98102, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30781"></a>
## FND-30781 — module-002 import env.invoke_iiij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiij", "kind": "function", "type_index": 34, "function_index": 46, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98492, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e in", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30782"></a>
## FND-30782 — module-002 import env.invoke_jiij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jiij", "kind": "function", "type_index": 68, "function_index": 47, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101560, "loader_excerpt": "a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCall_jij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vdii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vdii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vi:", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30783"></a>
## FND-30783 — module-002 import env.invoke_jiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jiiii", "kind": "function", "type_index": 110, "function_index": 48, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 100921, "loader_excerpt": "a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_jiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiijjj(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{r", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30784"></a>
## FND-30784 — module-002 import env.invoke_vij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vij", "kind": "function", "type_index": 24, "function_index": 49, "signature": {"parameters": ["i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109320, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).sl", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30785"></a>
## FND-30785 — module-002 import env.invoke_jiiiijjj

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_jiiiijjj", "kind": "function", "type_index": 111, "function_index": 50, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64", "i64"], "results": ["i64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 101339, "loader_excerpt": "a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiiiijjj:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_jiiiijjj(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_jiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_jij:function(index,a1,a2){var sp=stackSave();try{return dynCall_jij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;return _setThrew(1,0),0n}},invoke_v:function(index){var sp=stackSave();try{dynCall_v(index)}catch(e){if(stackRestore(sp),!(e instanceof ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30786"></a>
## FND-30786 — module-002 import env.invoke_iiiji

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiji", "kind": "function", "type_index": 112, "function_index": 51, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98671, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30787"></a>
## FND-30787 — module-002 import env.invoke_viiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiii", "kind": "function", "type_index": 18, "function_index": 52, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106086, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stackSave();try{dynCall_viiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30788"></a>
## FND-30788 — module-002 import env.cee_worker_spawn

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "cee_worker_spawn", "kind": "function", "type_index": 2, "function_index": 53, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88478, "loader_excerpt": "rker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscript", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30789"></a>
## FND-30789 — module-002 import env.cee_worker_terminate

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "cee_worker_terminate", "kind": "function", "type_index": 0, "function_index": 54, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88574, "loader_excerpt": ":0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)retu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30790"></a>
## FND-30790 — module-002 import env.cee_worker_post

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "cee_worker_post", "kind": "function", "type_index": 3, "function_index": 55, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88372, "loader_excerpt": "engineWorkersOf(Module,console).error(id);return null===description?0:stringToNewUTF8(description)},cee_worker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30791"></a>
## FND-30791 — module-002 import env.cee_worker_error

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "cee_worker_error", "kind": "function", "type_index": 2, "function_index": 56, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88226, "loader_excerpt": "n(){var command=Module.ceeInterruptMailbox.take();return null===command?0:stringToNewUTF8(command)},cee_worker_error:function(id){var description=engineWorkersOf(Module,console).error(id);return null===description?0:stringToNewUTF8(description)},cee_worker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3)", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30792"></a>
## FND-30792 — module-002 import env.__asyncjs__cee_worker_await_lines

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__asyncjs__cee_worker_await_lines", "kind": "function", "type_index": 2, "function_index": 57, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 74103, "loader_excerpt": "ilename?UTF8ToString(filename):\"unknown filename\",line,func?UTF8ToString(func):\"unknown function\"]),__asyncjs__cee_worker_await_lines:function(id){return Asyncify.handleAsync((async()=>{var joined=await engineWorkersOf(Module,console).awaitLines(id,Module.ceeInterruptMailbox);return null===joined?0:stringToNewUTF8(joined)}))},__cxa_begin_catch:ptr=>{var info=new ExceptionInfo(ptr);return info.get_caught()||(info.set_caught(!0),uncaughtExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught.length)return 0;var info=exceptionCaught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30793"></a>
## FND-30793 — module-002 import env.cee_take_uci_interrupt

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "cee_take_uci_interrupt", "kind": "function", "type_index": 8, "function_index": 58, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88096, "loader_excerpt": "mmerName,dst_name,17)):(stringToUTF8(winterName,dst_name,17),stringToUTF8(summerName,std_name,17))},cee_take_uci_interrupt:function(){var command=Module.ceeInterruptMailbox.take();return null===command?0:stringToNewUTF8(command)},cee_worker_error:function(id){var description=engineWorkersOf(Module,console).error(id);return null===description?0:stringToNewUTF8(description)},cee_worker_post:function(id,line){return engineWorkersOf(Module,console).post(id,UTF8ToString(line))?1:0},cee_worker_spawn:function(url){return engineWorkersOf(Module,console).spawn(UTF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&cl", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30794"></a>
## FND-30794 — module-002 import env.invoke_vidii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vidii", "kind": "function", "type_index": 113, "function_index": 59, "signature": {"parameters": ["i32", "i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102578, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30795"></a>
## FND-30795 — module-002 import env.invoke_dii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_dii", "kind": "function", "type_index": 46, "function_index": 60, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92589, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30796"></a>
## FND-30796 — module-002 import env.invoke_fii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_fii", "kind": "function", "type_index": 47, "function_index": 61, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93313, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30797"></a>
## FND-30797 — module-002 import env.invoke_di

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_di", "kind": "function", "type_index": 19, "function_index": 62, "signature": {"parameters": ["i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92068, "loader_excerpt": "turn HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},invoke_di:function(index,a1){var sp=stackSave();try{return dynCall_di(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_did:function(index,a1,a2){var sp=stackSave();try{return dynCall_did(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diddd:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_diddd(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30798"></a>
## FND-30798 — module-002 import env.js_alloc

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "js_alloc", "kind": "function", "type_index": 2, "function_index": 63, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 109828, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30799"></a>
## FND-30799 — module-002 import env.emscripten_asm_const_int

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "emscripten_asm_const_int", "kind": "function", "type_index": 4, "function_index": 64, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 88967, "loader_excerpt": "ow():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;fo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30800"></a>
## FND-30800 — module-002 import env.js_post_proto

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "js_post_proto", "kind": "function", "type_index": 5, "function_index": 65, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 109922, "loader_excerpt": ",0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30801"></a>
## FND-30801 — module-002 import env.js_free

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "js_free", "kind": "function", "type_index": 0, "function_index": 66, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 109881, "loader_excerpt": "tanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_alloc:function(size){return Module._malloc(size)},js_free:function(ptr){Module._free(ptr)},js_post_proto:function(ptr,size,is_final){let result_array=Module.HEAPU8.subarray(ptr,ptr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSIn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30802"></a>
## FND-30802 — module-002 import env.invoke_fiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_fiii", "kind": "function", "type_index": 53, "function_index": 67, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93484, "loader_excerpt": "fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30803"></a>
## FND-30803 — module-002 import env.invoke_iiiiiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiiiiiiiii", "kind": "function", "type_index": 54, "function_index": 68, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 97200, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11){var sp=stackSave();try{return dynCall_iiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{return dynCall_iiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiij:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiij(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30804"></a>
## FND-30804 — module-002 import env.invoke_iiijii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiijii", "kind": "function", "type_index": 48, "function_index": 69, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98858, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30805"></a>
## FND-30805 — module-002 import env.invoke_viij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viij", "kind": "function", "type_index": 23, "function_index": 70, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108780, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30806"></a>
## FND-30806 — module-002 import env.invoke_iiiijii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiijii", "kind": "function", "type_index": 86, "function_index": 71, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 98289, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRe", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30807"></a>
## FND-30807 — module-002 import env.invoke_iiijj

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiijj", "kind": "function", "type_index": 87, "function_index": 72, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 99053, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiijj:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiijj(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iij:function(index,a1,a2){var sp=stackSave();try{return dynCall_iij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiji:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiji(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iijiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iijiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30808"></a>
## FND-30808 — module-002 import env.invoke_viiijii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiijii", "kind": "function", "type_index": 114, "function_index": 73, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108584, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30809"></a>
## FND-30809 — module-002 import env.invoke_viijii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viijii", "kind": "function", "type_index": 55, "function_index": 74, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 109132, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viijii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viijii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vij:function(index,a1,a2){var sp=stackSave();try{dynCall_vij(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vji:function(index,a1,a2){var sp=stackSave();try{dynCall_vji(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vjjii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vjjii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},js_a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30810"></a>
## FND-30810 — module-002 import env.invoke_viiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiiii", "kind": "function", "type_index": 27, "function_index": 75, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106502, "loader_excerpt": ",a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stackSave();try{dynCall_viiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10){var sp=stackSave();try{dynCall_viiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{dynCall_viiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30811"></a>
## FND-30811 — module-002 import env.invoke_iid

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iid", "kind": "function", "type_index": 88, "function_index": 76, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95111, "loader_excerpt": "all_ii(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iid:function(index,a1,a2){var sp=stackSave();try{return dynCall_iid(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iif:function(index,a1,a2){var sp=stackSave();try{return dynCall_iif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iii:function(index,a1,a2){var sp=stackSave();try{return dynCall_iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30812"></a>
## FND-30812 — module-002 import env.invoke_viid

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viid", "kind": "function", "type_index": 40, "function_index": 77, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103266, "loader_excerpt": "vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viif:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viif(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30813"></a>
## FND-30813 — module-002 import env.invoke_fiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_fiiiiiiii", "kind": "function", "type_index": 115, "function_index": 78, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93850, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddi:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30814"></a>
## FND-30814 — module-002 import env.invoke_diiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_diiiii", "kind": "function", "type_index": 116, "function_index": 79, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93118, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Emscrip", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30815"></a>
## FND-30815 — module-002 import env.invoke_viiiid

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiid", "kind": "function", "type_index": 117, "function_index": 80, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105098, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30816"></a>
## FND-30816 — module-002 import env.invoke_viiidi

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiidi", "kind": "function", "type_index": 89, "function_index": 81, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104338, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidi:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiidi(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiidii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiffi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiffi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30817"></a>
## FND-30817 — module-002 import env.invoke_vifii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vifii", "kind": "function", "type_index": 118, "function_index": 82, "signature": {"parameters": ["i32", "i32", "f32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102922, "loader_excerpt": "vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30818"></a>
## FND-30818 — module-002 import env.invoke_viiiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiii", "kind": "function", "type_index": 90, "function_index": 83, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106722, "loader_excerpt": ",a5,a6,a7,a8,a9)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10){var sp=stackSave();try{dynCall_viiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{dynCall_viiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13){var sp=stackSave();try{dynCall_viiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30819"></a>
## FND-30819 — module-002 import env.invoke_viiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiiii", "kind": "function", "type_index": 69, "function_index": 84, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107202, "loader_excerpt": ",a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13){var sp=stackSave();try{dynCall_viiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14){var sp=stackSave();try{dynCall_viiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15){var sp=stackSave();try{dynCall_viiiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30820"></a>
## FND-30820 — module-002 import env.invoke_diii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_diii", "kind": "function", "type_index": 70, "function_index": 85, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92939, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_fiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30821"></a>
## FND-30821 — module-002 import env.invoke_iiidi

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiidi", "kind": "function", "type_index": 119, "function_index": 86, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 95624, "loader_excerpt": "iii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e in", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30822"></a>
## FND-30822 — module-002 import env._embind_register_void

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_void", "kind": "function", "type_index": 1, "function_index": 87, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 84610, "loader_excerpt": "uctors.push(_free,ptr),ptr},readValueFromPointer:readPointer,destructorFunction(ptr){_free(ptr)}})},_embind_register_void:(rawType,name)=>{registerType(rawType,{isVoid:!0,name:name=AsciiToString(name),fromWireType:()=>{},toWireType:(destructors,o)=>{}})},_gmtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getUTCSeconds(),HEAP32[tmPtr+4>>2]=date.getUTCMinutes(),HEAP32[tmPtr+8>>2]=date.getUTCHours(),HEAP32[tmPtr+12>>2]=date.getUTCDate(),HEAP32[tmPtr+16>>2]=date.getUTCMonth(),HEAP32[tmPtr+20>>2]=date.getUTCFullYear()-1900,HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,0},_localtime_js:funct", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30823"></a>
## FND-30823 — module-002 import env._embind_register_bool

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_bool", "kind": "function", "type_index": 6, "function_index": 88, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81322, "loader_excerpt": "dValueFromPointer:integerReadValueFromPointer(name,size,!isUnsignedType),destructorFunction:null})},_embind_register_bool:(rawType,name,trueValue,falseValue)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:function(wt){return!!wt},toWireType:function(destructors,o){return o?trueValue:falseValue},readValueFromPointer:function(pointer){return this.fromWireType(HEAPU8[pointer])},destructorFunction:null})},_embind_register_emval:rawType=>registerType(rawType,EmValType),_embind_register_float:(rawType,name,size)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:value=>value,toWireType:(destructors,value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRan", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30824"></a>
## FND-30824 — module-002 import env._embind_register_integer

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_integer", "kind": "function", "type_index": 7, "function_index": 89, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81957, "loader_excerpt": ",value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);let fromWireType=value=>value;if(0===minRange){var bitshift=32-8*size;fromWireType=value=>value<<bitshift>>>bitshift,maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>value,readValueFromPointer:integerReadValueFromPointer(name,size,0!==minRange),destructorFunction:null})},_embind_register_memory_view:(rawType,dataTypeIndex,name)=>{var TA=[Int8Array,Uint8Array,Int16Array,Uint16Array,Int32Array,Uint32Array,Float32Array,Float64Array,BigInt64Array,BigUint64Array][dataTypeIndex];function decodeMemoryView(handle){var size=HEAP", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30825"></a>
## FND-30825 — module-002 import env._embind_register_bigint

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_bigint", "kind": "function", "type_index": 158, "function_index": 90, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i64"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 80787, "loader_excerpt": "h))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType=0n===minRange;let fromWireType=value=>value;if(isUnsignedType){const bitSize=8*size;fromWireType=value=>BigInt.asUintN(bitSize,value),maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>(\"number\"==typeof value&&(value=BigInt(value)),value),readValueFromPointer:integerReadValueFromPointer(name,size,!isUnsignedType),destructorFunction:null})},_embind_register_bool:(rawType,name,trueValue,falseValue)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:function(wt){return!!wt},toWireType:func", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30826"></a>
## FND-30826 — module-002 import env._embind_register_float

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_float", "kind": "function", "type_index": 5, "function_index": 91, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81711, "loader_excerpt": "inter])},destructorFunction:null})},_embind_register_emval:rawType=>registerType(rawType,EmValType),_embind_register_float:(rawType,name,size)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:value=>value,toWireType:(destructors,value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);let fromWireType=value=>value;if(0===minRange){var bitshift=32-8*size;fromWireType=value=>value<<bitshift>>>bitshift,maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>value,readValueFromPointer:integerReadValueFromPointer(name,size,0!==minRange),destructorFunction:null})},_embind", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30827"></a>
## FND-30827 — module-002 import env._embind_register_std_string

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_std_string", "kind": "function", "type_index": 1, "function_index": 92, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 82893, "loader_excerpt": "ireType:decodeMemoryView,readValueFromPointer:decodeMemoryView},{ignoreDuplicateRegistrations:!0})},_embind_register_std_string:(rawType,name)=>{name=AsciiToString(name);registerType(rawType,{name:name,fromWireType(value){var str,length=HEAPU32[value>>2],payload=value+4;return str=UTF8ToString(payload,length,!0),_free(value),str},toWireType(destructors,value){var length;value instanceof ArrayBuffer&&(value=new Uint8Array(value));var valueIsOfTypeString=\"string\"==typeof value;valueIsOfTypeString||ArrayBuffer.isView(value)&&1==value.BYTES_PER_ELEMENT||throwBindingError(\"Cannot pass non-string to std::string\"),length=valueIsOfTypeString?lengthBytesUTF8(value):value.length;var base=_malloc(4+length+1),ptr=base+4;(HEAPU32[base>>2]=length,valueIsOfTypeString)?stringToUTF8(value,ptr,length+1):HEA", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30828"></a>
## FND-30828 — module-002 import env._embind_register_std_wstring

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_std_wstring", "kind": "function", "type_index": 5, "function_index": 93, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 83746, "loader_excerpt": "tors.push(_free,base),base},readValueFromPointer:readPointer,destructorFunction(ptr){_free(ptr)}})},_embind_register_std_wstring:(rawType,charSize,name)=>{var decodeString,encodeString,lengthBytesUTF;name=AsciiToString(name),2===charSize?(decodeString=UTF16ToString,encodeString=stringToUTF16,lengthBytesUTF=lengthBytesUTF16):(decodeString=UTF32ToString,encodeString=stringToUTF32,lengthBytesUTF=lengthBytesUTF32),registerType(rawType,{name:name,fromWireType:value=>{var length=HEAPU32[value>>2],str=decodeString(value+4,length*charSize,!0);return _free(value),str},toWireType:(destructors,value)=>{\"string\"!=typeof value&&throwBindingError(`Cannot pass non-string to C++ string type ${name}`);var length=lengthBytesUTF(value),ptr=_malloc(4+length+charSize);return HEAPU32[ptr>>2]=length/charSize,enc", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30829"></a>
## FND-30829 — module-002 import env._embind_register_emval

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_emval", "kind": "function", "type_index": 0, "function_index": 94, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 81647, "loader_excerpt": "FromPointer:function(pointer){return this.fromWireType(HEAPU8[pointer])},destructorFunction:null})},_embind_register_emval:rawType=>registerType(rawType,EmValType),_embind_register_float:(rawType,name,size)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:value=>value,toWireType:(destructors,value)=>value,readValueFromPointer:floatReadValueFromPointer(name,size),destructorFunction:null})},_embind_register_integer:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);let fromWireType=value=>value;if(0===minRange){var bitshift=32-8*size;fromWireType=value=>value<<bitshift>>>bitshift,maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>value,readValueFromPointer:integerReadValueFromPo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30830"></a>
## FND-30830 — module-002 import env._embind_register_memory_view

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_embind_register_memory_view", "kind": "function", "type_index": 5, "function_index": 95, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 82404, "loader_excerpt": "readValueFromPointer:integerReadValueFromPointer(name,size,0!==minRange),destructorFunction:null})},_embind_register_memory_view:(rawType,dataTypeIndex,name)=>{var TA=[Int8Array,Uint8Array,Int16Array,Uint16Array,Int32Array,Uint32Array,Float32Array,Float64Array,BigInt64Array,BigUint64Array][dataTypeIndex];function decodeMemoryView(handle){var size=HEAPU32[handle>>2],data=HEAPU32[handle+4>>2];return new TA(HEAP8.buffer,data,size)}registerType(rawType,{name:name=AsciiToString(name),fromWireType:decodeMemoryView,readValueFromPointer:decodeMemoryView},{ignoreDuplicateRegistrations:!0})},_embind_register_std_string:(rawType,name)=>{name=AsciiToString(name);registerType(rawType,{name:name,fromWireType(value){var str,length=HEAPU32[value>>2],payload=value+4;return str=UTF8ToString(payload,length,!", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30831"></a>
## FND-30831 — module-002 import env.invoke_vidi

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vidi", "kind": "function", "type_index": 71, "function_index": 96, "signature": {"parameters": ["i32", "i32", "f64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102406, "loader_excerpt": "all_vi(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidi:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_vidi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vidii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vidii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30832"></a>
## FND-30832 — module-002 import env.invoke_viiiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiiiii", "kind": "function", "type_index": 56, "function_index": 97, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107462, "loader_excerpt": "a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14){var sp=stackSave();try{dynCall_viiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15){var sp=stackSave();try{dynCall_viiiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiij:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiij(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30833"></a>
## FND-30833 — module-002 import env.invoke_viiiiiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiii", "kind": "function", "type_index": 57, "function_index": 98, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 106952, "loader_excerpt": "a6,a7,a8,a9,a10)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{dynCall_viiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13){var sp=stackSave();try{dynCall_viiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14){var sp=stackSave();try{dynCall_viiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14)}cat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30834"></a>
## FND-30834 — module-002 import env.invoke_vif

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_vif", "kind": "function", "type_index": 72, "function_index": 99, "signature": {"parameters": ["i32", "i32", "f32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 102758, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vif:function(index,a1,a2){var sp=stackSave();try{dynCall_vif(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vifii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_vifii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_vii:function(index,a1,a2){var sp=stackSave();try{dynCall_vii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viid:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:functio", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30835"></a>
## FND-30835 — module-002 import env.invoke_viiiiiij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiij", "kind": "function", "type_index": 120, "function_index": 100, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108012, "loader_excerpt": "a12,a13,a14,a15)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiij:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiij(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiji(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(sta", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30836"></a>
## FND-30836 — module-002 import env.invoke_viiid

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiid", "kind": "function", "type_index": 58, "function_index": 101, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103962, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiddi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiddi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidi:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiidi(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiidii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30837"></a>
## FND-30837 — module-002 import env.invoke_did

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_did", "kind": "function", "type_index": 59, "function_index": 102, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92231, "loader_excerpt": "all_di(index,a1)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_did:function(index,a1,a2){var sp=stackSave();try{return dynCall_did(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diddd:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_diddd(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30838"></a>
## FND-30838 — module-002 import env.invoke_diid

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_diid", "kind": "function", "type_index": 121, "function_index": 103, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92760, "loader_excerpt": "dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_diiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fii:function(index,a1,a2){var sp=stackSave();try{return dynCall_fii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30839"></a>
## FND-30839 — module-002 import env.invoke_iddd

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iddd", "kind": "function", "type_index": 122, "function_index": 104, "signature": {"parameters": ["i32", "f64", "f64", "f64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 94224, "loader_excerpt": "dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddi:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddi(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idi:function(index,a1,a2){var sp=stackSave();try{return dynCall_idi(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_idiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_idiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))t", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
