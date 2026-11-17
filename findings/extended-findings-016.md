# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30900"></a>
## FND-30900 — module-002 export CEE_InitWithOpts

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
{"module_id": "module-002", "direction": "export", "name": "CEE_InitWithOpts", "kind": "function", "index": 1666, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111285, "loader_excerpt": "free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30901"></a>
## FND-30901 — module-002 export CEE_DisposeGame

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
{"module_id": "module-002", "direction": "export", "name": "CEE_DisposeGame", "kind": "function", "index": 1673, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120383, "loader_excerpt": "T,c_buf=Module._malloc(c_buf_size);return Module.HEAPU8.set(js_buf,c_buf),[c_buf,c_buf_size]}return{CEE_DisposeGame:(Module,args)=>{let game_point=args[0];Module.ccall(\"CEE_DisposeGame\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_Play:(Module,args)=>{let game_point=args[0],uci_move=args[1],new_game_point=Module.ccall(\"CEE_Play\",\"number\",[\"number\",\"string\"],[game_point,uci_move]);new_game_point<0?postMessage({error:get_last_error(Module)}):postMessage({retval:new_game_point})},CEE_GetLastMove:(Module,args)=>{let game_point=args[0],uci_move=Module.ccall(\"CEE_GetLastMove\",\"string\",[\"number\"],[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30902"></a>
## FND-30902 — module-002 export CEE_DisposeAllGames

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
{"module_id": "module-002", "direction": "export", "name": "CEE_DisposeAllGames", "kind": "function", "index": 1675, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111394, "loader_excerpt": "WithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_Wai", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30903"></a>
## FND-30903 — module-002 export CEE_Play

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
{"module_id": "module-002", "direction": "export", "name": "CEE_Play", "kind": "function", "index": 1681, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120526, "loader_excerpt": "int=args[0];Module.ccall(\"CEE_DisposeGame\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_Play:(Module,args)=>{let game_point=args[0],uci_move=args[1],new_game_point=Module.ccall(\"CEE_Play\",\"number\",[\"number\",\"string\"],[game_point,uci_move]);new_game_point<0?postMessage({error:get_last_error(Module)}):postMessage({retval:new_game_point})},CEE_GetLastMove:(Module,args)=>{let game_point=args[0],uci_move=Module.ccall(\"CEE_GetLastMove\",\"string\",[\"number\"],[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to_c_buf(Module,args[2]),buf=c_buf[0],size=c_buf[1];try{let feature_handle=Module.ccall(\"CEE_NewFeature\",\"number\",[\"number\",\"number\",\"number\",\"nu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30904"></a>
## FND-30904 — module-002 export CEE_GetLastMove

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
{"module_id": "module-002", "direction": "export", "name": "CEE_GetLastMove", "kind": "function", "index": 1684, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120781, "loader_excerpt": ";new_game_point<0?postMessage({error:get_last_error(Module)}):postMessage({retval:new_game_point})},CEE_GetLastMove:(Module,args)=>{let game_point=args[0],uci_move=Module.ccall(\"CEE_GetLastMove\",\"string\",[\"number\"],[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to_c_buf(Module,args[2]),buf=c_buf[0],size=c_buf[1];try{let feature_handle=Module.ccall(\"CEE_NewFeature\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[game_point,feature_id,buf,size]);if(feature_handle<0)return void postMessage({error:get_last_error(Module)});postMessage({retval:feature_handle})}finally{0!==buf&&Module._free(buf)}},CEE_Run:(Module,args)=>{let feature_handle=args[0];return Promis", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30905"></a>
## FND-30905 — module-002 export CEE_NewFeature

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
{"module_id": "module-002", "direction": "export", "name": "CEE_NewFeature", "kind": "function", "index": 1694, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 10, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120995, "loader_excerpt": ",[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to_c_buf(Module,args[2]),buf=c_buf[0],size=c_buf[1];try{let feature_handle=Module.ccall(\"CEE_NewFeature\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[game_point,feature_id,buf,size]);if(feature_handle<0)return void postMessage({error:get_last_error(Module)});postMessage({retval:feature_handle})}finally{0!==buf&&Module._free(buf)}},CEE_Run:(Module,args)=>{let feature_handle=args[0];return Promise.resolve(Module.ccall(\"CEE_Run\",\"number\",[\"number\",\"number\"],[feature_handle,0],{async:!0})).then((ret=>{ret<=0&&postMessage({error:get_last_error(Module)})}))},CEE_DisposeFeature:(Module,args)=>{let game_point=ar", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30906"></a>
## FND-30906 — module-002 export CEE_DisposeFeature

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
{"module_id": "module-002", "direction": "export", "name": "CEE_DisposeFeature", "kind": "function", "index": 1697, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121643, "loader_excerpt": "[feature_handle,0],{async:!0})).then((ret=>{ret<=0&&postMessage({error:get_last_error(Module)})}))},CEE_DisposeFeature:(Module,args)=>{let game_point=args[0];Module.ccall(\"CEE_DisposeFeature\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAP", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30907"></a>
## FND-30907 — module-002 export CEE_Run

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
{"module_id": "module-002", "direction": "export", "name": "CEE_Run", "kind": "function", "index": 1699, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121417, "loader_excerpt": ":get_last_error(Module)});postMessage({retval:feature_handle})}finally{0!==buf&&Module._free(buf)}},CEE_Run:(Module,args)=>{let feature_handle=args[0];return Promise.resolve(Module.ccall(\"CEE_Run\",\"number\",[\"number\",\"number\"],[feature_handle,0],{async:!0})).then((ret=>{ret<=0&&postMessage({error:get_last_error(Module)})}))},CEE_DisposeFeature:(Module,args)=>{let game_point=args[0];Module.ccall(\"CEE_DisposeFeature\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_dat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30908"></a>
## FND-30908 — module-002 export CEE_Stop

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
{"module_id": "module-002", "direction": "export", "name": "CEE_Stop", "kind": "function", "index": 1701, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111677, "loader_excerpt": "ture=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30909"></a>
## FND-30909 — module-002 export CEE_Join

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
{"module_id": "module-002", "direction": "export", "name": "CEE_Join", "kind": "function", "index": 1703, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111715, "loader_excerpt": "dule._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsVali", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30910"></a>
## FND-30910 — module-002 export CEE_AddArtifact

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
{"module_id": "module-002", "direction": "export", "name": "CEE_AddArtifact", "kind": "function", "index": 1704, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "type_index": 4, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 123350, "loader_excerpt": "&&Module._free(c_buf),postMessage(Object.assign({call:\"CEE_LoadApplicabilityIndex_done\"},result))}},CEE_AddArtifact:(Module,args)=>{let artifact=args[0],key=args[1]||null,[c_buf,c_buf_size]=js_buf_to_c_buf(Module,artifact);try{let artifact_id=Module.ccall(\"CEE_AddArtifact\",\"string\",[\"number\",\"number\",\"string\"],[c_buf,c_buf_size,key]);if(!artifact_id)return void postMessage({error:get_last_error(Module)});postMessage({retval:artifact_id})}finally{0!==c_buf&&Module._free(c_buf)}}}}();return function(){var CREATE_KTEP_WORKER_API,Module=null;return(CREATE_KTEP_WORKER_API=function(WasmPath,options){var workerObj,kTepConsole,EngineReady=!1,callInFlight=!1,pendingApiCalls=[],interruptMailbox=makeInterruptMailbox(),interruptCommands={},wait=\"function\"==typeof setImmediate?setImmediate:setTimeout;f", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30911"></a>
## FND-30911 — module-002 export CEE_AddArtifactFromFile

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
{"module_id": "module-002", "direction": "export", "name": "CEE_AddArtifactFromFile", "kind": "function", "index": 1707, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111820, "loader_excerpt": "Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_comm", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30912"></a>
## FND-30912 — module-002 export CEE_DisposeArtifact

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
{"module_id": "module-002", "direction": "export", "name": "CEE_DisposeArtifact", "kind": "function", "index": 1710, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111884, "loader_excerpt": "_CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30913"></a>
## FND-30913 — module-002 export CEE_EnableNotifications

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
{"module_id": "module-002", "direction": "export", "name": "CEE_EnableNotifications", "kind": "function", "index": 1711, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111948, "loader_excerpt": "ule._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30914"></a>
## FND-30914 — module-002 export CEE_DisableNotifications

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
{"module_id": "module-002", "direction": "export", "name": "CEE_DisableNotifications", "kind": "function", "index": 1712, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112017, "loader_excerpt": "EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30915"></a>
## FND-30915 — module-002 export CEE_WaitForNotification

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
{"module_id": "module-002", "direction": "export", "name": "CEE_WaitForNotification", "kind": "function", "index": 1713, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112086, "loader_excerpt": "isableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30916"></a>
## FND-30916 — module-002 export CEE_StopNotificationWaiting

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
{"module_id": "module-002", "direction": "export", "name": "CEE_StopNotificationWaiting", "kind": "function", "index": 1714, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112158, "loader_excerpt": "tForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__21", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30917"></a>
## FND-30917 — module-002 export CEE_GetLastError

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
{"module_id": "module-002", "direction": "export", "name": "CEE_GetLastError", "kind": "function", "index": 1715, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112223, "loader_excerpt": "StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module._", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30918"></a>
## FND-30918 — module-002 export CEE_ClearLastError

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
{"module_id": "module-002", "direction": "export", "name": "CEE_ClearLastError", "kind": "function", "index": 1717, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112279, "loader_excerpt": "Waiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pb", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30919"></a>
## FND-30919 — module-002 export CEE_EnableLog

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
{"module_id": "module-002", "direction": "export", "name": "CEE_EnableLog", "kind": "function", "index": 1718, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121792, "loader_excerpt": "=args[0];Module.ccall(\"CEE_DisposeFeature\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAPU8[key_buf+key_len]=0}let ret=Module.ccall(\"CEE_LoadCharmModel\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[c_buf,c_buf_size,key_buf,key_len]);re", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30920"></a>
## FND-30920 — module-002 export CEE_DisableLog

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
{"module_id": "module-002", "direction": "export", "name": "CEE_DisableLog", "kind": "function", "index": 1719, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121890, "loader_excerpt": "},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAPU8[key_buf+key_len]=0}let ret=Module.ccall(\"CEE_LoadCharmModel\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[c_buf,c_buf_size,key_buf,key_len]);ret<0&&console.log(\"error loading charm model\"+(model_key?\": \"+model_key:\"\")),success=ret>=0}finally", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30921"></a>
## FND-30921 — module-002 export CEE_IsValidGamePoint

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
{"module_id": "module-002", "direction": "export", "name": "CEE_IsValidGamePoint", "kind": "function", "index": 1720, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 112437, "loader_excerpt": "EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30922"></a>
## FND-30922 — module-002 export uci_interrupt_commands

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
{"module_id": "module-002", "direction": "export", "name": "uci_interrupt_commands", "kind": "function", "index": 1764, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112501, "loader_excerpt": "le._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThre", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30923"></a>
## FND-30923 — module-002 export uci_command_after_interrupt

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
{"module_id": "module-002", "direction": "export", "name": "uci_command_after_interrupt", "kind": "function", "index": 1766, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112572, "loader_excerpt": "nterrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE_LoadCharmModel,Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscri", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30924"></a>
## FND-30924 — module-002 export CEE_LoadApplicabilityIndex

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
{"module_id": "module-002", "direction": "export", "name": "CEE_LoadApplicabilityIndex", "kind": "function", "index": 4091, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 122741, "loader_excerpt": "le._free(c_buf),postMessage({call:\"CEE_LoadCharmModel_done\",key:model_key||null,success:success})}},CEE_LoadApplicabilityIndex:(Module,args)=>{let index_data=args[0],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,index_data),result={success:!1,error:\"applicability index load failed\"};try{let status_str=Module.ccall(\"CEE_LoadApplicabilityIndex\",\"string\",[\"number\",\"number\"],[c_buf,c_buf_size]);try{result=JSON.parse(status_str)}catch(e){result={success:!1,error:\"could not parse index load status: \"+e}}result.success||console.log(\"error loading applicability index: \"+(result.error||\"unknown\"))}finally{0!==c_buf&&Module._free(c_buf),postMessage(Object.assign({call:\"CEE_LoadApplicabilityIndex_done\"},result))}},CEE_AddArtifact:(Module,args)=>{let artifact=args[0],key=args[1]||null,[c_buf,c_buf_size]=j", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30925"></a>
## FND-30925 — module-002 export CEE_LoadCharmModel

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
{"module_id": "module-002", "direction": "export", "name": "CEE_LoadCharmModel", "kind": "function", "index": 8526, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 10, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121990, "loader_excerpt": "CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAPU8[key_buf+key_len]=0}let ret=Module.ccall(\"CEE_LoadCharmModel\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[c_buf,c_buf_size,key_buf,key_len]);ret<0&&console.log(\"error loading charm model\"+(model_key?\": \"+model_key:\"\")),success=ret>=0}finally{0!==key_buf&&Module._free(key_buf),0!==c_buf&&Module._free(c_buf),postMessage({call:\"CEE_LoadCharmM", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30926"></a>
## FND-30926 — module-002 export _ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

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
{"module_id": "module-002", "direction": "export", "name": "_ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE", "kind": "function", "index": 8610, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112833, "loader_excerpt": "Module.__ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE=wasmExports._ZN3TEP7ktprintENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exceptio", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30927"></a>
## FND-30927 — module-002 export _ZN3TEP2pbEy

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
{"module_id": "module-002", "direction": "export", "name": "_ZN3TEP2pbEy", "kind": "function", "index": 8611, "signature": {"parameters": ["i64"], "results": []}, "type_index": 151, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 112947, "loader_excerpt": "ntENSt3__212basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30928"></a>
## FND-30928 — module-002 export _ZN3TEP2pbEyNS_6SquareE

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
{"module_id": "module-002", "direction": "export", "name": "_ZN3TEP2pbEyNS_6SquareE", "kind": "function", "index": 8612, "signature": {"parameters": ["i64", "i32"], "results": []}, "type_index": 64, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113004, "loader_excerpt": "atorIcEEEE,Module.__ZN3TEP2pbEy=wasmExports._ZN3TEP2pbEy,Module.__ZN3TEP2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30929"></a>
## FND-30929 — module-002 export _ZN3TEP2pbEyNS_6SquareES0_

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
{"module_id": "module-002", "direction": "export", "name": "_ZN3TEP2pbEyNS_6SquareES0_", "kind": "function", "index": 8613, "signature": {"parameters": ["i64", "i32", "i32"], "results": []}, "type_index": 152, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113075, "loader_excerpt": "P2pbEyNS_6SquareE=wasmExports._ZN3TEP2pbEyNS_6SquareE,Module.__ZN3TEP2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30930"></a>
## FND-30930 — module-002 export emscripten_builtin_memalign

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
{"module_id": "module-002", "direction": "export", "name": "emscripten_builtin_memalign", "kind": "function", "index": 22242, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113143, "loader_excerpt": "P2pbEyNS_6SquareES0_=wasmExports._ZN3TEP2pbEyNS_6SquareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30931"></a>
## FND-30931 — module-002 export setThrew

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
{"module_id": "module-002", "direction": "export", "name": "setThrew", "kind": "function", "index": 22252, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113193, "loader_excerpt": "quareES0_,_emscripten_builtin_memalign=wasmExports.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30932"></a>
## FND-30932 — module-002 export _emscripten_tempret_set

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
{"module_id": "module-002", "direction": "export", "name": "_emscripten_tempret_set", "kind": "function", "index": 22253, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113239, "loader_excerpt": "orts.emscripten_builtin_memalign,_setThrew=wasmExports.setThrew,__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30933"></a>
## FND-30933 — module-002 export _emscripten_stack_restore

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
{"module_id": "module-002", "direction": "export", "name": "_emscripten_stack_restore", "kind": "function", "index": 23002, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113302, "loader_excerpt": ",__emscripten_tempret_set=wasmExports._emscripten_tempret_set,__emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30934"></a>
## FND-30934 — module-002 export _emscripten_stack_alloc

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
{"module_id": "module-002", "direction": "export", "name": "_emscripten_stack_alloc", "kind": "function", "index": 23003, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113365, "loader_excerpt": "_emscripten_stack_restore=wasmExports._emscripten_stack_restore,__emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30935"></a>
## FND-30935 — module-002 export emscripten_stack_get_current

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
{"module_id": "module-002", "direction": "export", "name": "emscripten_stack_get_current", "kind": "function", "index": 23004, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113431, "loader_excerpt": "emscripten_stack_alloc=wasmExports._emscripten_stack_alloc,_emscripten_stack_get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30936"></a>
## FND-30936 — module-002 export __cxa_decrement_exception_refcount

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
{"module_id": "module-002", "direction": "export", "name": "__cxa_decrement_exception_refcount", "kind": "function", "index": 22961, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113508, "loader_excerpt": "get_current=wasmExports.emscripten_stack_get_current,___cxa_decrement_exception_refcount=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=w", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30937"></a>
## FND-30937 — module-002 export __cxa_increment_exception_refcount

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
{"module_id": "module-002", "direction": "export", "name": "__cxa_increment_exception_refcount", "kind": "function", "index": 22960, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113591, "loader_excerpt": "count=wasmExports.__cxa_decrement_exception_refcount,___cxa_increment_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30938"></a>
## FND-30938 — module-002 export __cxa_can_catch

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
{"module_id": "module-002", "direction": "export", "name": "__cxa_can_catch", "kind": "function", "index": 22991, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113655, "loader_excerpt": "ement_exception_refcount=wasmExports.__cxa_increment_exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30939"></a>
## FND-30939 — module-002 export __cxa_get_exception_ptr

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
{"module_id": "module-002", "direction": "export", "name": "__cxa_get_exception_ptr", "kind": "function", "index": 22992, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113708, "loader_excerpt": "exception_refcount,___cxa_can_catch=wasmExports.__cxa_can_catch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_ii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30940"></a>
## FND-30940 — module-002 export dynCall_vii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vii", "kind": "function", "index": 23005, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "type_index": 5, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113769, "loader_excerpt": "ch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30941"></a>
## FND-30941 — module-002 export dynCall_viii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viii", "kind": "function", "index": 23006, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "type_index": 6, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113820, "loader_excerpt": "xception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30942"></a>
## FND-30942 — module-002 export dynCall_iiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiii", "kind": "function", "index": 23007, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113872, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30943"></a>
## FND-30943 — module-002 export dynCall_ii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_ii", "kind": "function", "index": 23008, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113872, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30944"></a>
## FND-30944 — module-002 export dynCall_vi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vi", "kind": "function", "index": 23009, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113769, "loader_excerpt": "ch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30945"></a>
## FND-30945 — module-002 export dynCall_v

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_v", "kind": "function", "index": 23010, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113769, "loader_excerpt": "ch,___cxa_get_exception_ptr=wasmExports.__cxa_get_exception_ptr,dynCall_vii=dynCalls.vii=wasmExports.dynCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30946"></a>
## FND-30946 — module-002 export dynCall_iii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iii", "kind": "function", "index": 23011, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113872, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30947"></a>
## FND-30947 — module-002 export dynCall_iiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiiii", "kind": "function", "index": 23012, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 21, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114114, "loader_excerpt": "Call_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30948"></a>
## FND-30948 — module-002 export dynCall_i

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_i", "kind": "function", "index": 23013, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 113872, "loader_excerpt": "nCall_vii,dynCall_viii=dynCalls.viii=wasmExports.dynCall_viii,dynCall_iiii=dynCalls.iiii=wasmExports.dynCall_iiii,dynCall_ii=dynCalls.ii=wasmExports.dynCall_ii,dynCall_vi=dynCalls.vi=wasmExports.dynCall_vi,dynCall_v=dynCalls.v=wasmExports.dynCall_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30949"></a>
## FND-30949 — module-002 export dynCall_viiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiii", "kind": "function", "index": 23014, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 16, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114218, "loader_excerpt": "Call_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30950"></a>
## FND-30950 — module-002 export dynCall_viiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiii", "kind": "function", "index": 23015, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 7, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114218, "loader_excerpt": "Call_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30951"></a>
## FND-30951 — module-002 export dynCall_viiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiii", "kind": "function", "index": 23016, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 43, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114338, "loader_excerpt": "Call_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30952"></a>
## FND-30952 — module-002 export dynCall_iiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiii", "kind": "function", "index": 23017, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114114, "loader_excerpt": "Call_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30953"></a>
## FND-30953 — module-002 export dynCall_jij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jij", "kind": "function", "index": 23018, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i64"]}, "type_index": 25, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114448, "loader_excerpt": "iiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30954"></a>
## FND-30954 — module-002 export dynCall_iiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiii", "kind": "function", "index": 23019, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 15, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114114, "loader_excerpt": "Call_v,dynCall_iii=dynCalls.iii=wasmExports.dynCall_iii,dynCall_iiiiiii=dynCalls.iiiiiii=wasmExports.dynCall_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30955"></a>
## FND-30955 — module-002 export dynCall_vjjii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vjjii", "kind": "function", "index": 23020, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32"], "results": []}, "type_index": 85, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114559, "loader_excerpt": "j,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30956"></a>
## FND-30956 — module-002 export dynCall_ijjiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_ijjiiii", "kind": "function", "index": 23021, "signature": {"parameters": ["i32", "i64", "i64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 105, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114618, "loader_excerpt": ",dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30957"></a>
## FND-30957 — module-002 export dynCall_iijiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iijiii", "kind": "function", "index": 23022, "signature": {"parameters": ["i32", "i32", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 102, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114677, "loader_excerpt": "Call_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30958"></a>
## FND-30958 — module-002 export dynCall_iijjiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iijjiii", "kind": "function", "index": 23023, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 103, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114737, "loader_excerpt": "nCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_ji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30959"></a>
## FND-30959 — module-002 export dynCall_iiji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiji", "kind": "function", "index": 23024, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": ["i32"]}, "type_index": 44, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114677, "loader_excerpt": "Call_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
