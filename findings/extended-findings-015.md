# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30840"></a>
## FND-30840 — module-002 import env.invoke_viidi

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viidi", "kind": "function", "type_index": 60, "function_index": 105, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103438, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viidi:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viidi(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viif:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viif(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30841"></a>
## FND-30841 — module-002 import env.invoke_viiiidii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiidii", "kind": "function", "type_index": 123, "function_index": 106, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105286, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiidii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiidii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30842"></a>
## FND-30842 — module-002 import env.invoke_diddd

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_diddd", "kind": "function", "type_index": 124, "function_index": 107, "signature": {"parameters": ["i32", "i32", "f64", "f64", "f64"], "results": ["f64"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 92402, "loader_excerpt": "did(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diddd:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_diddd(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_dii:function(index,a1,a2){var sp=stackSave();try{return dynCall_dii(index,a1,a2)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diid:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diid(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_diii:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_diii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30843"></a>
## FND-30843 — module-002 import env.invoke_viiidii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiidii", "kind": "function", "type_index": 73, "function_index": 108, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 104526, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiidii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiidii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiffi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiffi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30844"></a>
## FND-30844 — module-002 import env.invoke_fiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_fiiii", "kind": "function", "type_index": 125, "function_index": 109, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 93663, "loader_excerpt": "(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiii:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_fiiii(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_fiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_fiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_i:function(index){var sp=stackSave();try{return dynCall_i(index)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iddd:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iddd(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30845"></a>
## FND-30845 — module-002 import env.invoke_viiiiiiff

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiff", "kind": "function", "type_index": 126, "function_index": 110, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "f32", "f32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 105874, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiff:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiff(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{dynCall_viiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9){var sp=stac", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30846"></a>
## FND-30846 — module-002 import env.invoke_viif

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viif", "kind": "function", "type_index": 74, "function_index": 111, "signature": {"parameters": ["i32", "i32", "i32", "f32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 103618, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viif:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viif(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viii:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viii(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiid:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiid(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiddi:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiiddi(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30847"></a>
## FND-30847 — module-002 import env.invoke_viiij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiij", "kind": "function", "type_index": 127, "function_index": 112, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108216, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiji(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30848"></a>
## FND-30848 — module-002 import env.invoke_iiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiiiiii", "kind": "function", "type_index": 61, "function_index": 113, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96981, "loader_excerpt": ",a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_iiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11){var sp=stackSave();try{return dynCall_iiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12){var sp=stackSave();try{return dynCall_iiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))th", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30849"></a>
## FND-30849 — module-002 import env.invoke_viiiji

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiji", "kind": "function", "type_index": 75, "function_index": 114, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 108396, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{dynCall_viiiji(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{dynCall_viiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viij:function(index,a1,a2,a3){var sp=stackSave();try{dynCall_viij(index,a1,a2,a3)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiji:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiji(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof Ems", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30850"></a>
## FND-30850 — module-002 import env.emscripten_sleep

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "emscripten_sleep", "kind": "function", "type_index": 0, "function_index": 115, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89571, "loader_excerpt": "nMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=>{var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;for(var string of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf)", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30851"></a>
## FND-30851 — module-002 import env.__syscall_fcntl64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_fcntl64", "kind": "function", "type_index": 4, "function_index": 116, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 75995, "loader_excerpt": "t,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return stream.flags=-289793&stream.flags|289792&arg,0;case 12:arg=syscallGetVarargP();return HEAP16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64:function(fd,buf){try{return SYSCALLS.writeStat(buf,FS.fstat(fd))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_get", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30852"></a>
## FND-30852 — module-002 import env.__syscall_ioctl

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_ioctl", "kind": "function", "type_index": 4, "function_index": 117, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 77611, "loader_excerpt": "lseek(stream,280*idx,0),pos}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_ioctl:function(fd,op,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(op){case 21509:case 21510:case 21511:case 21512:case 21524:case 21515:return stream.tty?0:-59;case 21505:if(!stream.tty)return-59;if(stream.tty.ops.ioctl_tcgets){var termios=stream.tty.ops.ioctl_tcgets(stream),argp=syscallGetVarargP();HEAP32[argp>>2]=termios.c_iflag||0,HEAP32[argp+4>>2]=termios.c_oflag||0,HEAP32[argp+8>>2]=termios.c_cflag||0,HEAP32[argp+12>>2]=termios.c_lflag||0;for(var i=0;i<32;i++)HEAP8[argp+i+17]=termios.c_cc[i]||0;return 0}return 0;case 21506:case 21507:case 21508:if(!stream.tty)return-59;if(stream.tty.ops.ioctl_tcsets){argp=syscallGetVarargP();var c_iflag=", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30853"></a>
## FND-30853 — module-002 import wasi_snapshot_preview1.fd_close

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_close", "kind": "function", "type_index": 2, "function_index": 118, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 90076, "loader_excerpt": "rings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len,offset)}ca", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30854"></a>
## FND-30854 — module-002 import wasi_snapshot_preview1.fd_read

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_read", "kind": "function", "type_index": 10, "function_index": 119, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 90560, "loader_excerpt": "P64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len,offset)}catch(e){if(ret>0&&e instanceof FS.ErrnoError&&(6==e.errno||6==e.errno))break;throw e}if(curr<0)return-1;if(ret+=curr,curr<len)break;void 0!==offset&&(offset+=curr)}return ret})(SYSCALLS.getStreamFromFD(fd),iov,iovcnt);return HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_seek:function(fd,offset,whence,newOffset){offset=bigintToI53Checked(offset);try{if(isNaN(offset))return 22;var stream=SYSCALLS.getStreamFromFD(fd);return FS.llsee", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30855"></a>
## FND-30855 — module-002 import wasi_snapshot_preview1.fd_write

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_write", "kind": "function", "type_index": 10, "function_index": 120, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 91481, "loader_excerpt": "ts=null),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_sync:_fd_sync,fd_write:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{if(1==iovcnt)return FS.write(stream,HEAP8,HEAPU32[iov>>2],HEAPU32[iov+4>>2],offset);for(var total=0,i=0,p=iov;i<iovcnt;i++,p+=8)total+=HEAPU32[p+4>>2];var view=new Uint8Array(total),voff=0;for(i=0;i<iovcnt;i++,iov+=8){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];view.set(HEAPU8.subarray(ptr,ptr+len),voff),voff+=len}return FS.write(stream,view,0,total,offset)})(SYSCALLS.getStreamFromFD(fd),iov,iovcnt);return HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},invoke_di:function(index,a1){var sp=stackSave();try{return dynCall_di(index,a1)}catch(e){if(stackRestore(sp),!(e ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30856"></a>
## FND-30856 — module-002 import env._abort_js

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_abort_js", "kind": "function", "type_index": 12, "function_index": 121, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 80763, "loader_excerpt": "riteStat(buf,FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType=0n===minRange;let fromWireType=value=>value;if(isUnsignedType){const bitSize=8*size;fromWireType=value=>BigInt.asUintN(bitSize,value),maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>(\"number\"==typeof value&&(value=BigInt(value)),value),readValueFromPointer:integerReadValueFromPointer(name,size,!isUnsignedType),destructorFunction:null})},_embind_register_bool:(rawType,name,trueValue,falseValue)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:function(wt){ret", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30857"></a>
## FND-30857 — module-002 import wasi_snapshot_preview1.clock_time_get

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
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "clock_time_get", "kind": "function", "type_index": 35, "function_index": 122, "signature": {"parameters": ["i32", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88655, "loader_excerpt": "TF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30858"></a>
## FND-30858 — module-002 import env.emscripten_date_now

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "emscripten_date_now", "kind": "function", "type_index": 62, "function_index": 123, "signature": {"parameters": [], "results": ["f64"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89051, "loader_excerpt": "BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30859"></a>
## FND-30859 — module-002 import env.__syscall_openat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_openat", "kind": "function", "type_index": 10, "function_index": 124, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79869, "loader_excerpt": ".lstat(path):FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_openat:function(dirfd,path,flags,varargs){SYSCALLS.varargs=varargs;try{path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path);var mode=varargs?syscallGetVarargI():0;return 64&flags&&(mode&=~SYSCALLS.currentUmask),FS.open(path,flags,mode).fd}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_readlinkat:function(dirfd,path,buf,bufsize){try{if(path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),bufsize<=0)return-28;var ret=FS.readlink(path),len=Math.min(bufsize,lengthBytesUTF8(ret)),endChar=HEAP8[buf+len];return stringToUTF8(ret,buf,bufsize+1),HEAP8[buf+len]=endChar,len}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30860"></a>
## FND-30860 — module-002 import env.__syscall_fstat64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_fstat64", "kind": "function", "type_index": 3, "function_index": 125, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 76527, "loader_excerpt": "P16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64:function(fd,buf){try{return SYSCALLS.writeStat(buf,FS.fstat(fd))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_getdents64:function(fd,dirp,count){try{var stream=SYSCALLS.getStreamFromFD(fd);stream.getdents||=FS.readdir(stream.path);for(var pos=0,off=FS.llseek(stream,0,1),startIdx=Math.floor(off/280),endIdx=Math.min(stream.getdents.length,startIdx+Math.floor(count/280)),idx=startIdx;idx<endIdx;idx++){var id,type,name=stream.getdents[idx];if(\".\"===name)id=stream.node.id,type=4;else if(\"..\"===name){id=FS.lookupPath(stream.path,{parent:!0}).node.id,type=4}else{var child;try{child=FS.lookupNode(stream.node,name)}catch(e){if(28===e?.errno)conti", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30861"></a>
## FND-30861 — module-002 import env.__syscall_stat64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_stat64", "kind": "function", "type_index": 3, "function_index": 126, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 80579, "loader_excerpt": ",HEAP8[buf+len]=endChar,len}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_stat64:function(path,buf){try{return path=SYSCALLS.getStr(path),SYSCALLS.writeStat(buf,FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType=0n===minRange;let fromWireType=value=>value;if(isUnsignedType){const bitSize=8*size;fromWireType=value=>BigInt.asUintN(bitSize,value),maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>(\"number\"==typeof value&&(value=BigInt(value)),value),readValueFromPointer:integerReadValueFromPointer(name,size,!", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30862"></a>
## FND-30862 — module-002 import env.__syscall_newfstatat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_newfstatat", "kind": "function", "type_index": 10, "function_index": 127, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79538, "loader_excerpt": "ask,FS.mkdir(path,mode,0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_newfstatat:function(dirfd,path,buf,flags){try{path=SYSCALLS.getStr(path);var nofollow=256&flags,allowEmpty=4096&flags;return flags&=-6401,path=SYSCALLS.calculateAt(dirfd,path,allowEmpty),SYSCALLS.writeStat(buf,nofollow?FS.lstat(path):FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_openat:function(dirfd,path,flags,varargs){SYSCALLS.varargs=varargs;try{path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path);var mode=varargs?syscallGetVarargI():0;return 64&flags&&(mode&=~SYSCALLS.currentUmask),FS.open(path,flags,mode).fd}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_readlinkat:function(dirfd,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30863"></a>
## FND-30863 — module-002 import env.__syscall_lstat64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_lstat64", "kind": "function", "type_index": 3, "function_index": 128, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79107, "loader_excerpt": "return 0;default:return-28}}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_lstat64:function(path,buf){try{return path=SYSCALLS.getStr(path),SYSCALLS.writeStat(buf,FS.lstat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_mkdirat:function(dirfd,path,mode){try{return path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),mode&=~SYSCALLS.currentUmask,FS.mkdir(path,mode,0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_newfstatat:function(dirfd,path,buf,flags){try{path=SYSCALLS.getStr(path);var nofollow=256&flags,allowEmpty=4096&flags;return flags&=-6401,path=SYSCALLS.calculateAt(dirfd,path,allowEmpty),SYSCALLS.writeStat(buf,nofollow?FS.lstat(path):FS.stat(path))}catch(e){i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30864"></a>
## FND-30864 — module-002 import wasi_snapshot_preview1.fd_sync

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_sync", "kind": "function", "type_index": 2, "function_index": 129, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 91464, "loader_excerpt": "e&&(stream.getdents=null),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_sync:_fd_sync,fd_write:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{if(1==iovcnt)return FS.write(stream,HEAP8,HEAPU32[iov>>2],HEAPU32[iov+4>>2],offset);for(var total=0,i=0,p=iov;i<iovcnt;i++,p+=8)total+=HEAPU32[p+4>>2];var view=new Uint8Array(total),voff=0;for(i=0;i<iovcnt;i++,iov+=8){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];view.set(HEAPU8.subarray(ptr,ptr+len),voff),voff+=len}return FS.write(stream,view,0,total,offset)})(SYSCALLS.getStreamFromFD(fd),iov,iovcnt);return HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},invoke_di:function(index,a1){var sp=stackSave();try{return dynCall_di(index,a1)}catch(e){if(stac", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30865"></a>
## FND-30865 — module-002 import wasi_snapshot_preview1.environ_sizes_get

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
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "environ_sizes_get", "kind": "function", "type_index": 3, "function_index": 130, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 89817, "loader_excerpt": "uf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=>{var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;for(var string of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"Err", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30866"></a>
## FND-30866 — module-002 import wasi_snapshot_preview1.environ_get

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
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "environ_get", "kind": "function", "type_index": 3, "function_index": 131, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 89606, "loader_excerpt": "GrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=>{var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;for(var string of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamF", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30867"></a>
## FND-30867 — module-002 import wasi_snapshot_preview1.fd_fdstat_get

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_fdstat_get", "kind": "function", "type_index": 3, "function_index": 132, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 90240, "loader_excerpt": ");return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len,offset)}catch(e){if(ret>0&&e instanceof FS.ErrnoError&&(6==e.errno||6==e.errno))break;throw e}if(curr<0)return-1;if(ret+=curr,curr<len)break;void 0!==offset&&(offset+=curr)}r", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30868"></a>
## FND-30868 — module-002 import env.emscripten_get_now

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "emscripten_get_now", "kind": "function", "type_index": 62, "function_index": 133, "signature": {"parameters": [], "results": ["f64"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89131, "loader_excerpt": "code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30869"></a>
## FND-30869 — module-002 import wasi_snapshot_preview1.fd_seek

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_seek", "kind": "function", "type_index": 159, "function_index": 134, "signature": {"parameters": ["i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 91095, "loader_excerpt": "turn HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_seek:function(fd,offset,whence,newOffset){offset=bigintToI53Checked(offset);try{if(isNaN(offset))return 22;var stream=SYSCALLS.getStreamFromFD(fd);return FS.llseek(stream,offset,whence),HEAP64[newOffset>>3]=BigInt(stream.position),stream.getdents&&!offset&&0===whence&&(stream.getdents=null),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_sync:_fd_sync,fd_write:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{if(1==iovcnt)return FS.write(stream,HEAP8,HEAPU32[iov>>2],HEAPU32[iov+4>>2],offset);for(var total=0,i=0,p=iov;i<iovcnt;i++,p+=8)total+=HEAPU32[p+4>>2];var view=new Uint8Array(total),voff=0;for(i=0;i<iovcnt;i++,iov+=8){var ptr=HEAPU32[", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30870"></a>
## FND-30870 — module-002 import env.__syscall_mkdirat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_mkdirat", "kind": "function", "type_index": 4, "function_index": 135, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79293, "loader_excerpt": "iteStat(buf,FS.lstat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_mkdirat:function(dirfd,path,mode){try{return path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),mode&=~SYSCALLS.currentUmask,FS.mkdir(path,mode,0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_newfstatat:function(dirfd,path,buf,flags){try{path=SYSCALLS.getStr(path);var nofollow=256&flags,allowEmpty=4096&flags;return flags&=-6401,path=SYSCALLS.calculateAt(dirfd,path,allowEmpty),SYSCALLS.writeStat(buf,nofollow?FS.lstat(path):FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_openat:function(dirfd,path,flags,varargs){SYSCALLS.varargs=varargs;try{path=SYSCALLS.getStr(path),path=SYSCALLS.ca", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30871"></a>
## FND-30871 — module-002 import env._tzset_js

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_tzset_js", "kind": "function", "type_index": 6, "function_index": 136, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 87242, "loader_excerpt": "getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,date.getTime()/1e3})();return BigInt(ret)},_tzset_js:(timezone,daylight,std_name,dst_name)=>{var currentYear=(new Date).getFullYear(),winter=new Date(currentYear,0,1),summer=new Date(currentYear,6,1),winterOffset=winter.getTimezoneOffset(),summerOffset=summer.getTimezoneOffset(),stdTimezoneOffset=Math.max(winterOffset,summerOffset);HEAPU32[timezone>>2]=60*stdTimezoneOffset,HEAP32[daylight>>2]=Number(winterOffset!=summerOffset);var extractZone=timezoneOffset=>{var sign=timezoneOffset>=0?\"-\":\"+\",absOffset=Math.abs(timezoneOffset);return`UTC${sign}${String(Math.floor(absOffset/60)).padStart(2,\"0\")}${String(absOffset%60).padStart(2,\"0\")}`},winterName=extractZone(winterOffset),summerName=extractZone(summerOffset);summerOffset<winterOffset", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30872"></a>
## FND-30872 — module-002 import env._timegm_js

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_timegm_js", "kind": "function", "type_index": 11, "function_index": 137, "signature": {"parameters": ["i32"], "results": ["i64"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 86804, "loader_excerpt": "dr,stream,len,flags,offset)}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_timegm_js:function(tmPtr){var ret=(()=>{var time=Date.UTC(HEAP32[tmPtr+20>>2]+1900,HEAP32[tmPtr+16>>2],HEAP32[tmPtr+12>>2],HEAP32[tmPtr+8>>2],HEAP32[tmPtr+4>>2],HEAP32[tmPtr>>2],0),date=new Date(time);if(isNaN(date.getTime()))return-1;HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,date.getTime()/1e3})();return BigInt(ret)},_tzset_js:(timezone,daylight,std_name,dst_name)=>{var currentYear=(new Date).getFullYear(),winter=new Date(currentYear,0,1),summer=new Date(currentYear,6,1),winterOffset=winter.getTimezoneOffset(),summerOffset=summer.getTimezoneOffset(),stdTimezoneOffset=Math.ma", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30873"></a>
## FND-30873 — module-002 import env._localtime_js

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_localtime_js", "kind": "function", "type_index": 49, "function_index": 138, "signature": {"parameters": ["i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 85291, "loader_excerpt": "etUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,0},_localtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getSeconds(),HEAP32[tmPtr+4>>2]=date.getMinutes(),HEAP32[tmPtr+8>>2]=date.getHours(),HEAP32[tmPtr+12>>2]=date.getDate(),HEAP32[tmPtr+16>>2]=date.getMonth(),HEAP32[tmPtr+20>>2]=date.getFullYear()-1900,HEAP32[tmPtr+24>>2]=date.getDay();var yday=0|(date=>{var year;return((year=date.getFullYear())%4!=0||year%100==0&&year%400!=0?MONTH_DAYS_REGULAR_CUMULATIVE:MONTH_DAYS_LEAP_CUMULATIVE)[date.getMonth()]+date.getDate()-1})(date);HEAP32[tmPtr+28>>2]=yday,HEAP32[tmPtr+36>>2]=-60*date.getTimezoneOffset();var start=new Date(date.getFullYear(),0,1),summerOf", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30874"></a>
## FND-30874 — module-002 import env._gmtime_js

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_gmtime_js", "kind": "function", "type_index": 49, "function_index": 139, "signature": {"parameters": ["i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 84765, "loader_excerpt": "Type,{isVoid:!0,name:name=AsciiToString(name),fromWireType:()=>{},toWireType:(destructors,o)=>{}})},_gmtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getUTCSeconds(),HEAP32[tmPtr+4>>2]=date.getUTCMinutes(),HEAP32[tmPtr+8>>2]=date.getUTCHours(),HEAP32[tmPtr+12>>2]=date.getUTCDate(),HEAP32[tmPtr+16>>2]=date.getUTCMonth(),HEAP32[tmPtr+20>>2]=date.getUTCFullYear()-1900,HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,0},_localtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getSeconds(),HEAP32[tmPtr", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30875"></a>
## FND-30875 — module-002 import env._munmap_js

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_munmap_js", "kind": "function", "type_index": 91, "function_index": 140, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 86548, "loader_excerpt": "ated,HEAPU32[addr>>2]=ptr,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_munmap_js:function(addr,len,prot,flags,fd,offset){offset=bigintToI53Checked(offset);try{var stream=SYSCALLS.getStreamFromFD(fd);2&prot&&SYSCALLS.doMsync(addr,stream,len,flags,offset)}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_timegm_js:function(tmPtr){var ret=(()=>{var time=Date.UTC(HEAP32[tmPtr+20>>2]+1900,HEAP32[tmPtr+16>>2],HEAP32[tmPtr+12>>2],HEAP32[tmPtr+8>>2],HEAP32[tmPtr+4>>2],HEAP32[tmPtr>>2],0),date=new Date(time);if(isNaN(date.getTime()))return-1;HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,date.getTime()/1e3})();return BigInt(ret)},_tzset", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30876"></a>
## FND-30876 — module-002 import env._mmap_js

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "_mmap_js", "kind": "function", "type_index": 86, "function_index": 141, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 86220, "loader_excerpt": "t&&date.getTimezoneOffset()==Math.min(winterOffset,summerOffset));return HEAP32[tmPtr+32>>2]=dst,0},_mmap_js:function(len,prot,flags,fd,offset,allocated,addr){offset=bigintToI53Checked(offset);try{var stream=SYSCALLS.getStreamFromFD(fd),res=FS.mmap(stream,len,offset,prot,flags),ptr=res.ptr;return HEAP32[allocated>>2]=res.allocated,HEAPU32[addr>>2]=ptr,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_munmap_js:function(addr,len,prot,flags,fd,offset){offset=bigintToI53Checked(offset);try{var stream=SYSCALLS.getStreamFromFD(fd);2&prot&&SYSCALLS.doMsync(addr,stream,len,flags,offset)}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_timegm_js:function(tmPtr){var ret=(()=>{var time=Date.UTC(HEAP32[tmPtr+20>>2]+1900,HEAP32[tmPtr+16>>2],HEAP32[tmPtr", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30877"></a>
## FND-30877 — module-002 import env.__syscall_readlinkat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_readlinkat", "kind": "function", "type_index": 10, "function_index": 142, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 80202, "loader_excerpt": "FS.open(path,flags,mode).fd}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_readlinkat:function(dirfd,path,buf,bufsize){try{if(path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),bufsize<=0)return-28;var ret=FS.readlink(path),len=Math.min(bufsize,lengthBytesUTF8(ret)),endChar=HEAP8[buf+len];return stringToUTF8(ret,buf,bufsize+1),HEAP8[buf+len]=endChar,len}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_stat64:function(path,buf){try{return path=SYSCALLS.getStr(path),SYSCALLS.writeStat(buf,FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30878"></a>
## FND-30878 — module-002 import env.emscripten_resize_heap

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "emscripten_resize_heap", "kind": "function", "type_index": 2, "function_index": 143, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89170, "loader_excerpt": ":_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30879"></a>
## FND-30879 — module-002 import env.__syscall_getdents64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__syscall_getdents64", "kind": "function", "type_index": 4, "function_index": 144, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 76682, "loader_excerpt": "writeStat(buf,FS.fstat(fd))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_getdents64:function(fd,dirp,count){try{var stream=SYSCALLS.getStreamFromFD(fd);stream.getdents||=FS.readdir(stream.path);for(var pos=0,off=FS.llseek(stream,0,1),startIdx=Math.floor(off/280),endIdx=Math.min(stream.getdents.length,startIdx+Math.floor(count/280)),idx=startIdx;idx<endIdx;idx++){var id,type,name=stream.getdents[idx];if(\".\"===name)id=stream.node.id,type=4;else if(\"..\"===name){id=FS.lookupPath(stream.path,{parent:!0}).node.id,type=4}else{var child;try{child=FS.lookupNode(stream.node,name)}catch(e){if(28===e?.errno)continue;throw e}id=child.id,type=FS.isChrdev(child.mode)?2:FS.isDir(child.mode)?4:FS.isLink(child.mode)?10:8}HEAP64[dirp+pos>>3]=BigInt(id),HEAP64[dirp+pos+8>>", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30880"></a>
## FND-30880 — module-002 import env.__cxa_uncaught_exceptions

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_uncaught_exceptions", "kind": "function", "type_index": 8, "function_index": 145, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75844, "loader_excerpt": "exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return stream.flags=-289793&stream.flags|289792&arg,0;case 12:arg=syscallGetVarargP();return HEAP16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30881"></a>
## FND-30881 — module-002 import env.__cxa_current_primary_exception

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_current_primary_exception", "kind": "function", "type_index": 8, "function_index": 146, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74540, "loader_excerpt": "htExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught.length)return 0;var info=exceptionCaught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30882"></a>
## FND-30882 — module-002 import env.__cxa_rethrow_primary_exception

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "__cxa_rethrow_primary_exception", "kind": "function", "type_index": 0, "function_index": 147, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75410, "loader_excerpt": "aughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);swi", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30883"></a>
## FND-30883 — module-002 import env.invoke_iiiiij

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiij", "kind": "function", "type_index": 91, "function_index": 148, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 97704, "loader_excerpt": ",a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiij:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiij(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiijj:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiijj(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30884"></a>
## FND-30884 — module-002 import env.invoke_iiiiid

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiid", "kind": "function", "type_index": 128, "function_index": 149, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96177, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30885"></a>
## FND-30885 — module-002 import env.invoke_iiiiijj

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiijj", "kind": "function", "type_index": 63, "function_index": 150, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 97899, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiijj:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiijj(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30886"></a>
## FND-30886 — module-002 import env.invoke_iiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_iiiiiiii", "kind": "function", "type_index": 17, "function_index": 151, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96770, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_iiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11){var sp=stackSave();try{return dynCall_iiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiiii:fu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30887"></a>
## FND-30887 — module-002 import env.invoke_viiiiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiiiiii", "kind": "function", "type_index": 129, "function_index": 152, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107732, "loader_excerpt": "a11,a12,a13,a14)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15){var sp=stackSave();try{dynCall_viiiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiij:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiij(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30888"></a>
## FND-30888 — module-002 import wasi_snapshot_preview1.random_get

Host-provided random bytes. Does not prove a particular cryptographic protocol.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "import", "module": "wasi_snapshot_preview1", "name": "random_get", "kind": "function", "type_index": 3, "function_index": 153, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Host-provided random bytes. Does not prove a particular cryptographic protocol.", "loader_character_offset": 110109, "loader_excerpt": "tr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),wasmExports.__wasm_call_ctors(),FS.ignorePermissions=!1,Module.onRuntimeInitialized?.(),function(){var postRun=Module.postRun;postRun&&(\"function\"==typeof postRun&&(postRun=[postRun]),onP", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30889"></a>
## FND-30889 — module-002 import env.emscripten_get_heap_max

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
{"module_id": "module-002", "direction": "import", "module": "env", "name": "emscripten_get_heap_max", "kind": "function", "type_index": 8, "function_index": 154, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89092, "loader_excerpt": "(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30890"></a>
## FND-30890 — module-002 export memory

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "memory", "kind": "memory", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119503, "loader_excerpt": ".asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_error(Module){return Module.ccall(\"CEE_GetLastError\",\"string\",[],[])}function js_buf_to_c_buf(Module,js_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30891"></a>
## FND-30891 — module-002 export __wasm_call_ctors

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "__wasm_call_ctors", "kind": "function", "index": 155, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 110633, "loader_excerpt": "etTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),wasmExports.__wasm_call_ctors(),FS.ignorePermissions=!1,Module.onRuntimeInitialized?.(),function(){var postRun=Module.postRun;postRun&&(\"function\"==typeof postRun&&(postRun=[postRun]),onPostRuns.push(...postRun)),callRuntimeCallbacks(onPostRuns)}())}return async function(){function receiveInstance(instance){return wasmExports=instance.exports,function(wasmExports){wasmExports.__getTypeName,Module._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30892"></a>
## FND-30892 — module-002 export __getTypeName

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "__getTypeName", "kind": "function", "index": 4995, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 111000, "loader_excerpt": "tion receiveInstance(instance){return wasmExports=instance.exports,function(wasmExports){wasmExports.__getTypeName,Module._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_J", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30893"></a>
## FND-30893 — module-002 export __indirect_function_table

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "__indirect_function_table", "kind": "table", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119522, "loader_excerpt": "ind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_error(Module){return Module.ccall(\"CEE_GetLastError\",\"string\",[],[])}function js_buf_to_c_buf(Module,js_buf){if(!js_buf)ret", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30894"></a>
## FND-30894 — module-002 export uci_command

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "uci_command", "kind": "function", "index": 168, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 111046, "loader_excerpt": "rts=instance.exports,function(wasmExports){wasmExports.__getTypeName,Module._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30895"></a>
## FND-30895 — module-002 export init

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "init", "kind": "function", "index": 170, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 29972, "loader_excerpt": "),byteArray=await(async(byteArray,fullname)=>{for(var plugin of(\"undefined\"!=typeof Browser&&Browser.init(),preloadPlugins))if(plugin.canHandle(fullname))return plugin.handle(byteArray,fullname);return byteArray})(byteArray,fullname),preFinish?.(),dontCreateFile||((...args)=>{FS.createDataFile(...args)})(parent,name,byteArray,canRead,canWrite,canOwn)}finally{runDependencies--,Module.monitorRunDependencies?.(runDependencies),runDependencies||dependenciesPromiseResolve()}},FS={root:null,mounts:[],devices:{},streams:[],nextInode:1,nameTable:null,currentPath:\"/\",initialized:!1,ignorePermissions:!0,filesystems:null,syncFSRequests:0,ErrnoError:class{name=\"ErrnoError\";constructor(errno){this.errno=errno}},FSStream:class{shared={};get object(){return this.node}set object(val){this.node=val}get isR", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30896"></a>
## FND-30896 — module-002 export CEE_Init

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "CEE_Init", "kind": "function", "index": 1667, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111117, "loader_excerpt": "dule._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30897"></a>
## FND-30897 — module-002 export CEE_Dispose

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "CEE_Dispose", "kind": "function", "index": 1668, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111158, "loader_excerpt": ",Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_D", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30898"></a>
## FND-30898 — module-002 export free

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "free", "kind": "function", "index": 22239, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 39297, "loader_excerpt": "eam:stream=>FS.statfsNode(stream.node),statfsNode(node){var rtn={bsize:4096,frsize:4096,blocks:1e6,bfree:5e5,bavail:5e5,files:FS.nextInode,ffree:FS.nextInode-1,fsid:42,flags:2,namelen:255};return node.node_ops.statfs&&Object.assign(rtn,node.node_ops.statfs(node.mount.opts.root)),rtn},create:(path,mode=438)=>(mode&=4095,mode|=32768,FS.mknod(path,mode,0)),mkdir:(path,mode=511)=>(mode&=1023,mode|=16384,FS.mknod(path,mode,0)),mkdirTree(path,mode){var dirs=path.split(\"/\"),d=\"\";for(var dir of dirs)if(dir){(d||PATH.isAbs(path))&&(d+=\"/\"),d+=dir;try{FS.mkdir(d,mode)}catch(e){if(20!=e.errno)throw e}}},mkdev:(path,mode,dev)=>(void 0===dev&&(dev=mode,mode=438),mode|=8192,FS.mknod(path,mode,dev)),symlink(oldpath,newpath){if(!PATH_FS.resolve(oldpath))throw new FS.ErrnoError(44);var parent=FS.lookupPath", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30899"></a>
## FND-30899 — module-002 export malloc

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/imports-exports-annotated.json)

```text
{"module_id": "module-002", "direction": "export", "name": "malloc", "kind": "function", "index": 22238, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 111241, "loader_excerpt": "spose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasm", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
