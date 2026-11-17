# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30600"></a>
## FND-30600 — module-001 export CEE_WaitForNotification

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_WaitForNotification", "kind": "function", "index": 1712, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111901, "loader_excerpt": "isableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30601"></a>
## FND-30601 — module-001 export CEE_StopNotificationWaiting

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_StopNotificationWaiting", "kind": "function", "index": 1713, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111973, "loader_excerpt": "tForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__21", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30602"></a>
## FND-30602 — module-001 export CEE_GetLastError

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_GetLastError", "kind": "function", "index": 1714, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112038, "loader_excerpt": "StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module._", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30603"></a>
## FND-30603 — module-001 export CEE_ClearLastError

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_ClearLastError", "kind": "function", "index": 1716, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112094, "loader_excerpt": "Waiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pb", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30604"></a>
## FND-30604 — module-001 export CEE_EnableLog

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_EnableLog", "kind": "function", "index": 1717, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121555, "loader_excerpt": "=args[0];Module.ccall(\"CEE_DisposeFeature\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAPU8[key_buf+key_len]=0}let ret=Module.ccall(\"CEE_LoadCharmModel\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[c_buf,c_buf_size,key_buf,key_len]);re", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30605"></a>
## FND-30605 — module-001 export CEE_DisableLog

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_DisableLog", "kind": "function", "index": 1718, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121653, "loader_excerpt": "},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAPU8[key_buf+key_len]=0}let ret=Module.ccall(\"CEE_LoadCharmModel\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[c_buf,c_buf_size,key_buf,key_len]);ret<0&&console.log(\"error loading charm model\"+(model_key?\": \"+model_key:\"\")),success=ret>=0}finally", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30606"></a>
## FND-30606 — module-001 export CEE_IsValidGamePoint

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_IsValidGamePoint", "kind": "function", "index": 1719, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112252, "loader_excerpt": "EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30607"></a>
## FND-30607 — module-001 export uci_interrupt_commands

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
{"module_id": "module-001", "direction": "export", "name": "uci_interrupt_commands", "kind": "function", "index": 1763, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112316, "loader_excerpt": "le._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThre", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30608"></a>
## FND-30608 — module-001 export uci_command_after_interrupt

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
{"module_id": "module-001", "direction": "export", "name": "uci_command_after_interrupt", "kind": "function", "index": 1765, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112387, "loader_excerpt": "nterrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscri", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30609"></a>
## FND-30609 — module-001 export CEE_LoadApplicabilityIndex

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_LoadApplicabilityIndex", "kind": "function", "index": 4089, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 122504, "loader_excerpt": "le._free(c_buf),postMessage({call:\"CEE_LoadCharmModel_done\",key:model_key||null,success:success})}},CEE_LoadApplicabilityIndex:(Module,args)=>{let index_data=args[0],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,index_data),result={success:!1,error:\"applicability index load failed\"};try{let status_str=Module.ccall(\"CEE_LoadApplicabilityIndex\",\"string\",[\"number\",\"number\"],[c_buf,c_buf_size]);try{result=JSON.parse(status_str)}catch(e){result={success:!1,error:\"could not parse index load status: \"+e}}result.success||console.log(\"error loading applicability index: \"+(result.error||\"unknown\"))}finally{0!==c_buf&&Module._free(c_buf),postMessage(Object.assign({call:\"CEE_LoadApplicabilityIndex_done\"},result))}},CEE_AddArtifact:(Module,args)=>{let artifact=args[0],key=args[1]||null,[c_buf,c_buf_size]=j", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30610"></a>
## FND-30610 — module-001 export CEE_LoadCharmModel

Named CEE native API; wrapper passes protobuf handles/buffers where present.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "export", "name": "CEE_LoadCharmModel", "kind": "function", "index": 8497, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 10, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121753, "loader_excerpt": "CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAPU8[key_buf+key_len]=0}let ret=Module.ccall(\"CEE_LoadCharmModel\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[c_buf,c_buf_size,key_buf,key_len]);ret<0&&console.log(\"error loading charm model\"+(model_key?\": \"+model_key:\"\")),success=ret>=0}finally{0!==key_buf&&Module._free(key_buf),0!==c_buf&&Module._free(c_buf),postMessage({call:\"CEE_LoadCharmM", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30611"></a>
## FND-30611 — module-001 export _ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

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
{"module_id": "module-001", "direction": "export", "name": "_ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE", "kind": "function", "index": 8581, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112648, "loader_excerpt": "Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exceptio", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30612"></a>
## FND-30612 — module-001 export _ZN3TEP2pbEy

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
{"module_id": "module-001", "direction": "export", "name": "_ZN3TEP2pbEy", "kind": "function", "index": 8582, "signature": {"parameters": ["i64"], "results": []}, "type_index": 150, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112762, "loader_excerpt": "ntENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30613"></a>
## FND-30613 — module-001 export _ZN3TEP2pbEyNS_6SquareE

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
{"module_id": "module-001", "direction": "export", "name": "_ZN3TEP2pbEyNS_6SquareE", "kind": "function", "index": 8583, "signature": {"parameters": ["i64", "i32"], "results": []}, "type_index": 64, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112819, "loader_excerpt": "atorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30614"></a>
## FND-30614 — module-001 export _ZN3TEP2pbEyNS_6SquareES0_

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
{"module_id": "module-001", "direction": "export", "name": "_ZN3TEP2pbEyNS_6SquareES0_", "kind": "function", "index": 8584, "signature": {"parameters": ["i64", "i32", "i32"], "results": []}, "type_index": 151, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112890, "loader_excerpt": "P2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30615"></a>
## FND-30615 — module-001 export emscripten_builtin_memalign

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
{"module_id": "module-001", "direction": "export", "name": "emscripten_builtin_memalign", "kind": "function", "index": 22211, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112958, "loader_excerpt": "P2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30616"></a>
## FND-30616 — module-001 export setThrew

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
{"module_id": "module-001", "direction": "export", "name": "setThrew", "kind": "function", "index": 22221, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113008, "loader_excerpt": "quareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30617"></a>
## FND-30617 — module-001 export _emscripten_tempret_set

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
{"module_id": "module-001", "direction": "export", "name": "_emscripten_tempret_set", "kind": "function", "index": 22222, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113054, "loader_excerpt": "orts.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30618"></a>
## FND-30618 — module-001 export _emscripten_stack_restore

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
{"module_id": "module-001", "direction": "export", "name": "_emscripten_stack_restore", "kind": "function", "index": 22971, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113117, "loader_excerpt": ",__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30619"></a>
## FND-30619 — module-001 export _emscripten_stack_alloc

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
{"module_id": "module-001", "direction": "export", "name": "_emscripten_stack_alloc", "kind": "function", "index": 22972, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113180, "loader_excerpt": "_emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30620"></a>
## FND-30620 — module-001 export emscripten_stack_get_current

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
{"module_id": "module-001", "direction": "export", "name": "emscripten_stack_get_current", "kind": "function", "index": 22973, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113246, "loader_excerpt": "emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30621"></a>
## FND-30621 — module-001 export __cxa_decrement_exception_refcount

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
{"module_id": "module-001", "direction": "export", "name": "__cxa_decrement_exception_refcount", "kind": "function", "index": 22930, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113323, "loader_excerpt": "get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=w", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30622"></a>
## FND-30622 — module-001 export __cxa_increment_exception_refcount

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
{"module_id": "module-001", "direction": "export", "name": "__cxa_increment_exception_refcount", "kind": "function", "index": 22929, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113406, "loader_excerpt": "count=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30623"></a>
## FND-30623 — module-001 export __cxa_can_catch

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
{"module_id": "module-001", "direction": "export", "name": "__cxa_can_catch", "kind": "function", "index": 22960, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113470, "loader_excerpt": "ement_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30624"></a>
## FND-30624 — module-001 export __cxa_get_exception_ptr

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
{"module_id": "module-001", "direction": "export", "name": "__cxa_get_exception_ptr", "kind": "function", "index": 22961, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113523, "loader_excerpt": "exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_ii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30625"></a>
## FND-30625 — module-001 export dynCall_vii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vii", "kind": "function", "index": 22974, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "type_index": 5, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113584, "loader_excerpt": "ch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30626"></a>
## FND-30626 — module-001 export dynCall_viii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viii", "kind": "function", "index": 22975, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "type_index": 6, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113635, "loader_excerpt": "xception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30627"></a>
## FND-30627 — module-001 export dynCall_iiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiii", "kind": "function", "index": 22976, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113687, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30628"></a>
## FND-30628 — module-001 export dynCall_ii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_ii", "kind": "function", "index": 22977, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113687, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30629"></a>
## FND-30629 — module-001 export dynCall_vi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vi", "kind": "function", "index": 22978, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113584, "loader_excerpt": "ch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30630"></a>
## FND-30630 — module-001 export dynCall_v

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_v", "kind": "function", "index": 22979, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113584, "loader_excerpt": "ch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30631"></a>
## FND-30631 — module-001 export dynCall_iii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iii", "kind": "function", "index": 22980, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113687, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30632"></a>
## FND-30632 — module-001 export dynCall_iiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiiii", "kind": "function", "index": 22981, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 21, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113929, "loader_excerpt": "Call_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30633"></a>
## FND-30633 — module-001 export dynCall_i

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_i", "kind": "function", "index": 22982, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113687, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30634"></a>
## FND-30634 — module-001 export dynCall_viiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiii", "kind": "function", "index": 22983, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 16, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114033, "loader_excerpt": "Call_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30635"></a>
## FND-30635 — module-001 export dynCall_viiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiii", "kind": "function", "index": 22984, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 7, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114033, "loader_excerpt": "Call_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30636"></a>
## FND-30636 — module-001 export dynCall_viiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiii", "kind": "function", "index": 22985, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 43, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114153, "loader_excerpt": "Call_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30637"></a>
## FND-30637 — module-001 export dynCall_iiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiii", "kind": "function", "index": 22986, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 12, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113929, "loader_excerpt": "Call_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30638"></a>
## FND-30638 — module-001 export dynCall_jij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jij", "kind": "function", "index": 22987, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i64"]}, "type_index": 25, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114263, "loader_excerpt": "iiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30639"></a>
## FND-30639 — module-001 export dynCall_iiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiii", "kind": "function", "index": 22988, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 15, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113929, "loader_excerpt": "Call_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30640"></a>
## FND-30640 — module-001 export dynCall_vjjii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vjjii", "kind": "function", "index": 22989, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32"], "results": []}, "type_index": 83, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114374, "loader_excerpt": "j,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30641"></a>
## FND-30641 — module-001 export dynCall_ijjiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_ijjiiii", "kind": "function", "index": 22990, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 103, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114433, "loader_excerpt": ",dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30642"></a>
## FND-30642 — module-001 export dynCall_iijiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iijiii", "kind": "function", "index": 22991, "signature": {"parameters": ["i32", "i32", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 100, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114492, "loader_excerpt": "Call_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30643"></a>
## FND-30643 — module-001 export dynCall_iijjiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iijjiii", "kind": "function", "index": 22992, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 101, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114552, "loader_excerpt": "nCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_ji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30644"></a>
## FND-30644 — module-001 export dynCall_iiji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiji", "kind": "function", "index": 22993, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": ["i32"]}, "type_index": 44, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114492, "loader_excerpt": "Call_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30645"></a>
## FND-30645 — module-001 export dynCall_iijji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iijji", "kind": "function", "index": 22994, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32"], "results": ["i32"]}, "type_index": 102, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114552, "loader_excerpt": "nCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_ji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30646"></a>
## FND-30646 — module-001 export dynCall_vdii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vdii", "kind": "function", "index": 22995, "signature": {"parameters": ["i32", "f64", "i32", "i32"], "results": []}, "type_index": 67, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114714, "loader_excerpt": "l_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30647"></a>
## FND-30647 — module-001 export dynCall_idiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_idiiii", "kind": "function", "index": 22996, "signature": {"parameters": ["i32", "f64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 104, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114770, "loader_excerpt": "iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dy", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30648"></a>
## FND-30648 — module-001 export dynCall_vji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vji", "kind": "function", "index": 22997, "signature": {"parameters": ["i32", "i64", "i32"], "results": []}, "type_index": 33, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114822, "loader_excerpt": "_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30649"></a>
## FND-30649 — module-001 export dynCall_viiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiii", "kind": "function", "index": 22998, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 9, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114033, "loader_excerpt": "Call_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30650"></a>
## FND-30650 — module-001 export dynCall_ji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_ji", "kind": "function", "index": 22999, "signature": {"parameters": ["i32", "i32"], "results": ["i64"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114263, "loader_excerpt": "iiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30651"></a>
## FND-30651 — module-001 export dynCall_viiji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiji", "kind": "function", "index": 23000, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": []}, "type_index": 45, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114979, "loader_excerpt": "ynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30652"></a>
## FND-30652 — module-001 export dynCall_iij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iij", "kind": "function", "index": 23001, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i32"]}, "type_index": 26, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114492, "loader_excerpt": "Call_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30653"></a>
## FND-30653 — module-001 export dynCall_iif

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iif", "kind": "function", "index": 23002, "signature": {"parameters": ["i32", "i32", "f32"], "results": ["i32"]}, "type_index": 105, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115079, "loader_excerpt": ".dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30654"></a>
## FND-30654 — module-001 export dynCall_viiiffi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiffi", "kind": "function", "index": 23003, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f32", "f32", "i32"], "results": []}, "type_index": 106, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115136, "loader_excerpt": "ll_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30655"></a>
## FND-30655 — module-001 export dynCall_jiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jiii", "kind": "function", "index": 23004, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i64"]}, "type_index": 38, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115191, "loader_excerpt": ",dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fi", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30656"></a>
## FND-30656 — module-001 export dynCall_jii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jii", "kind": "function", "index": 23005, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i64"]}, "type_index": 20, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115191, "loader_excerpt": ",dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fi", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30657"></a>
## FND-30657 — module-001 export dynCall_iiiij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiij", "kind": "function", "index": 23006, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "type_index": 39, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115294, "loader_excerpt": "nCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30658"></a>
## FND-30658 — module-001 export dynCall_iiij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiij", "kind": "function", "index": 23007, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i32"]}, "type_index": 34, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115347, "loader_excerpt": "ll_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30659"></a>
## FND-30659 — module-001 export dynCall_jiij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jiij", "kind": "function", "index": 23008, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i64"]}, "type_index": 68, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115399, "loader_excerpt": "all_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
