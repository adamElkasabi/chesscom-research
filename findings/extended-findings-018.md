# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-31020"></a>
## FND-31020 — module-002 export dynCall_viiidii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiidii", "kind": "function", "index": 23085, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "type_index": 73, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118267, "loader_excerpt": "viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31021"></a>
## FND-31021 — module-002 export dynCall_fiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_fiiii", "kind": "function", "index": 23086, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "type_index": 125, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116941, "loader_excerpt": "dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31022"></a>
## FND-31022 — module-002 export dynCall_viiiiiiff

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiff", "kind": "function", "index": 23087, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "f32", "f32"], "results": []}, "type_index": 126, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118387, "loader_excerpt": "Call_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31023"></a>
## FND-31023 — module-002 export dynCall_viif

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viif", "kind": "function", "index": 23088, "signature": {"parameters": ["i32", "i32", "i32", "f32"], "results": []}, "type_index": 74, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118444, "loader_excerpt": "ll_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_ii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31024"></a>
## FND-31024 — module-002 export dynCall_viiij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiij", "kind": "function", "index": 23089, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": []}, "type_index": 127, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116647, "loader_excerpt": ",dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31025"></a>
## FND-31025 — module-002 export dynCall_iiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiiiiii", "kind": "function", "index": 23090, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 61, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116355, "loader_excerpt": "l_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31026"></a>
## FND-31026 — module-002 export dynCall_viiiji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiji", "kind": "function", "index": 23091, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32"], "results": []}, "type_index": 75, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116647, "loader_excerpt": ",dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31027"></a>
## FND-31027 — module-002 export dynCall_viji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viji", "kind": "function", "index": 23092, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": []}, "type_index": 22, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118663, "loader_excerpt": "ynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_u", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31028"></a>
## FND-31028 — module-002 export dynCall_vifi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vifi", "kind": "function", "index": 23093, "signature": {"parameters": ["i32", "i32", "f32", "i32"], "results": []}, "type_index": 189, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117174, "loader_excerpt": "d,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31029"></a>
## FND-31029 — module-002 export dynCall_jiji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jiji", "kind": "function", "index": 23094, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": ["i64"]}, "type_index": 190, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118741, "loader_excerpt": "Calls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31030"></a>
## FND-31030 — module-002 export dynCall_iidiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iidiiiii", "kind": "function", "index": 23095, "signature": {"parameters": ["i32", "i32", "f64", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 191, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118784, "loader_excerpt": "s.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31031"></a>
## FND-31031 — module-002 export dynCall_iiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiiiii", "kind": "function", "index": 23096, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 17, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116355, "loader_excerpt": "l_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31032"></a>
## FND-31032 — module-002 export dynCall_iiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiiiiiiiiii", "kind": "function", "index": 23097, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 192, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118922, "loader_excerpt": "Calls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryVie", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31033"></a>
## FND-31033 — module-002 export dynCall_viiiiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiiiiiiiiii", "kind": "function", "index": 23098, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 129, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119007, "loader_excerpt": "iii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instan", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31034"></a>
## FND-31034 — module-002 export dynCall_iiiiij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiij", "kind": "function", "index": 23099, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "type_index": 91, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119075, "loader_excerpt": "lls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise(", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31035"></a>
## FND-31035 — module-002 export dynCall_iiiiid

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiid", "kind": "function", "index": 23100, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": ["i32"]}, "type_index": 128, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119133, "loader_excerpt": "dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInst", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31036"></a>
## FND-31036 — module-002 export dynCall_iiiiijj

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiijj", "kind": "function", "index": 23101, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "type_index": 63, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119193, "loader_excerpt": "nCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31037"></a>
## FND-31037 — module-002 export dynCall_iiiiiijj

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiiijj", "kind": "function", "index": 23102, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "type_index": 193, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119239, "loader_excerpt": "ll_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instanc", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31038"></a>
## FND-31038 — module-002 export asyncify_start_unwind

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
{"module_id": "module-002", "direction": "export", "name": "asyncify_start_unwind", "kind": "function", "index": 23103, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119291, "loader_excerpt": "ts.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31039"></a>
## FND-31039 — module-002 export asyncify_stop_unwind

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
{"module_id": "module-002", "direction": "export", "name": "asyncify_stop_unwind", "kind": "function", "index": 23104, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119347, "loader_excerpt": "_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitializ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31040"></a>
## FND-31040 — module-002 export asyncify_start_rewind

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
{"module_id": "module-002", "direction": "export", "name": "asyncify_start_rewind", "kind": "function", "index": 23105, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119403, "loader_excerpt": "art_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_erro", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31041"></a>
## FND-31041 — module-002 export asyncify_stop_rewind

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
{"module_id": "module-002", "direction": "export", "name": "asyncify_stop_rewind", "kind": "function", "index": 23106, "signature": {"parameters": [], "results": []}, "type_index": 12, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119459, "loader_excerpt": "op_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_error(Module){return Module.ccall(\"CEE_GetLastError\",\"string", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31042"></a>
## FND-31042 — module-002 export asyncify_get_state

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
{"module_id": "module-002", "direction": "export", "name": "asyncify_get_state", "kind": "function", "index": 23107, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": null, "loader_excerpt": "", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31043"></a>
## FND-31043 — module-002 exact protobuf buffer boundary

js_buf_to_c_buf allocates length*BYTES_PER_ELEMENT,HEAPU8.set copies bytes. CEE_NewFeature(gamePoint,featureId,ptr,len) returns handle and frees input buffer in finally. CEE_Run(handle,0) is async; imported callback copies HEAPU8.subarray(ptr,ptr+size).slice() into postMessage({proto,is_final}). The protocol payload is real protobuf,not JSON.

- Category: wasm_javascript
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/javascript-bridge-excerpt.js)

```text
CEE_NewFeature has native(i32,i32,i32,i32)->i32;CEE_Run(i32,i32)->i32. Import callback and exact wrapper retained.
```

<a id="FND-31044"></a>
## FND-31044 — module-002 actual CEE_InitWithOpts native signature

Binary export CEE_InitWithOpts has two i32parameters and no result. It forwards to an internal function through Asyncify instrumentation. Earlier JS-functionlength0was not the native ABI. Interpretation as(ptr,len) is supported by protobuf wrapper conventions but the generic initialization call itself is not proven by this signature alone.

- Category: wasm_javascript
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016, SRC-3017
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No claim of arbitrary initialization-option compatibility or a successful TorchHuman toggle from InitWithOpts.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/focused-decompilation/CEE_InitWithOpts.pseudocode.txt)

```text
{"name": "CEE_InitWithOpts", "kind": "function", "index": 1666, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1}
```

<a id="FND-31045"></a>
## FND-31045 — module-002 focused native function reconstruction

Five export bodies decompiled using analysis-only modules with signature-correct imported stubs for all other functions; globals/tables/memory declarations retained,but original data omitted. Full decompilation attempts failed: JS WABT memory-out-of-bounds; native process killed137under2GiBaddressspace/60sCPUbound. These failures are tooling/resource outcomes,not proof of engine invalidity.

- Category: wasm_decompilation
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3016
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30730
- [Exact supporting artifact](../wasm-analysis/modules/module-002/focused-decompilation/results.json)

```text
CEE_Init,CEE_InitWithOpts,CEE_NewFeature,CEE_DisposeFeature,CEE_Run each decompiled successfully. Numeric fields/types/names in pseudocode are decompiler assignments,not recovered source identifiers.
```

<a id="FND-31046"></a>
## FND-31046 — module-003 complete structural inventory

693497bytes; SHA256064234cfc56dc28a18ced0b35630bc8f2dc1a7c689073fb1e2b78ede7c2a6b35; 756defined functions,41imported functions,32exports. All section offsets,types,limits,globals,elements,data and function body spans retained.

- Category: wasm_structure
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../wasm-analysis/modules/module-003/structure.json)

```text
Magic0061736d;version1;no custom sections.
```

<a id="FND-31047"></a>
## FND-31047 — module-003 function and call-graph analysis

1994direct caller/callee pairs;4396static direct-call sites;736indirect-call sites. Exact direct call indices recovered from full WAT. Indirect dispatch targets not resolved; opcode frequencies are syntactic counts,not execution profiling.

- Category: wasm_functions
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/functions.json)

```text
See call-graph.jsonl.gz and opcode-statistics.json.
```

<a id="FND-31048"></a>
## FND-31048 — module-003 strings and data offsets

860ASCII candidates,51keyword-relevant candidates,8UTF16candidates. Strings linked to original file offsets and active data memory addresses when constant-resolvable. Random code/weight bytes can resemble text.

- Category: wasm_strings
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/strings.txt)

```text
All-ASCII candidates are separately gzipped; relevant output is not a semantic analysis of every string.
```

<a id="FND-31049"></a>
## FND-31049 — module-003 memory/host boundary

{"defined_memories": [], "imported_memories": [{"module": "a", "name": "a", "kind": "memory", "limits": {"flags": 3, "minimum": 8192, "shared": true, "memory64": false, "maximum": 8192}}], "tables": [{"element_type": "funcref", "limits": {"flags": 1, "minimum": 464, "shared": false, "memory64": false, "maximum": 464}}], "data_segments": 27}

- Category: wasm_memory
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/structure.json)

```text
Memory limits use64KiBpages; shared flag is explicit.
```

<a id="FND-31050"></a>
## FND-31050 — module-003 new controlled instantiation

Bounded Node instantiation succeeded with explicitly stubbed imports; this is not engine search/review correctness. Initial module003failed due unhandled imported memory,then passed using exact descriptor limits. Stack-query exports were called only when present.

- Category: wasm_runtime
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No native whole-game review rerun,new server query,or cloud parity test. Historical successful full CEE/Human tests retained separately.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/runtime-observation.json)

```text
{"status": "instantiated with function import stubs", "imports": 42, "exports": 32, "memories": [], "import_calls_during_instantiation": [], "elapsed_ms": 18.180257, "algorithm_calls": [], "limitation": "No wrapper runtime constructors/search/review invoked; stub instantiation is not a functional engine validation. No original application inputs used."}
```

<a id="FND-31051"></a>
## FND-31051 — module-003 import a.b

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "b", "kind": "function", "type_index": 3, "function_index": 0, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 3149, "loader_excerpt": "peof document&&document.currentScript&&(a=document.currentScript.src),a=0!==(a=Jt?Jt:a).indexOf(\"blob:\")?a.substr(0,a.lastIndexOf(\"/\")+1):\"\",s?(X=function(e,t){return r=r||require(\"fs\"),e=(V=V||require(\"path\")).normalize(e),r.readFileSync(e,t?null:\"utf8\")},K=function(e){return re((e=(e=X(e,!0)).buffer?e:new Uint8Array(e)).buffer),e}):(X=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.send(null),t.responseText},o&&(K=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.responseType=\"arraybuffer\",t.send(null),new Uint8Array(t.response)})));s&&\"undefined\"==typeof performance&&(global.performance=require(\"perf_hooks\").performance);var J,$,Z=i.print||console.log.bind(console),l=i.printErr||console.warn.bind(console);for(e in N)N.hasOwnProperty(e)&&(i[e]=N[e]);N=null", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31052"></a>
## FND-31052 — module-003 import a.c

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "c", "kind": "function", "type_index": 0, "function_index": 1, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 27403, "loader_excerpt": "){},M:function(e,t,n){return R+=1,setTimeout(function(){--R,j(function(){P.apply(null,[e,n])})},t)},c:function(n){At(function(e){var t;t=e,R+=1,$t(function(){--R,j(t)},n)})},o:function(e,n,t,r,a){function o(e,t){Qe(e,t.response,function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)},function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)})}function i(e){j(function(){h?P.apply(null,[h,e]):a&&a(e)},w)}function s(e){--R,j(function(){p?P.apply(null,[p,e]):t&&t(e)},w)}function u(e){j(function(){m?P.apply(null,[m,e]):r&&r(e)},w)}function c(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)}R+=1;var f=e+112,l=O(f),d=C[f+36>>2],p=C[f+40>>2],m=C[f+44>>2],h=C[f+48>>2],_=C[f+52>>2],y=!!(4&_),g=!!(32&_),v=!!(16&_),w=!!(64&_);if(\"EM_IDB_STORE\"===l)l=C[f+84>>2],Qe(e,I.slice(l,l+C[f+88>", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31053"></a>
## FND-31053 — module-003 import a.d

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "d", "kind": "function", "type_index": 10, "function_index": 2, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 723, "loader_excerpt": "ined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var n,r={open:function(e,t){n=t},send:function(){require(\"fs\").readFile(n,function(e,t){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=t,r.onreadystatechange(),r.onload())})}};return r}),i.postCustomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.forEach(function(e){i.queue.put(e)}),i.queue.process()},i.postMes", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31054"></a>
## FND-31054 — module-003 import a.e

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "e", "kind": "function", "type_index": 9, "function_index": 3, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 96, "loader_excerpt": "/*!\n * Stockfish.js (c) 2023, Chess.com, LLC\n * https://github.com/nmrugg/stockfish.js\n * License: GPLv3\n *\n * Based on stockfish.wasm (c)\n * Niklas Fiekas <niklas.fiekas@backscattering.de>\n * Hiroshi Ogawa <hi.ogawa.zz@gmail.com>\n * https://github.com/niklasf/stockfish.wasm\n * https://github.com/hi-ogawa/Stockfish\n *\n * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.\n * https://github.com/official-stockfish/Stockfish\n */!function(){var $t,e,n,t,r,a;function i(){function e(S){var i,k,T,t,n;S=S||{},(i=i||(void 0!==S?S:{})).ready=new Promise(function(e,t){k=e,T=t}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var n,r={open:function(e,t){n=t},send:function(){require(\"fs\").readFile(n,function(e,t){r.readyState=4,e?(con", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31055"></a>
## FND-31055 — module-003 import a.f

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "f", "kind": "function", "type_index": 2, "function_index": 4, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 3032, "loader_excerpt": "d - perhaps a newer version is needed?'),e}global.Worker=d.Worker}else(z||o)&&(o?a=self.location.href:\"undefined\"!=typeof document&&document.currentScript&&(a=document.currentScript.src),a=0!==(a=Jt?Jt:a).indexOf(\"blob:\")?a.substr(0,a.lastIndexOf(\"/\")+1):\"\",s?(X=function(e,t){return r=r||require(\"fs\"),e=(V=V||require(\"path\")).normalize(e),r.readFileSync(e,t?null:\"utf8\")},K=function(e){return re((e=(e=X(e,!0)).buffer?e:new Uint8Array(e)).buffer),e}):(X=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.send(null),t.responseText},o&&(K=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.responseType=\"arraybuffer\",t.send(null),new Uint8Array(t.response)})));s&&\"undefined\"==typeof performance&&(global.performance=require(\"perf_hooks\").performance);var J,$,Z=i.print||", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31056"></a>
## FND-31056 — module-003 import a.g

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "g", "kind": "function", "type_index": 43, "function_index": 5, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 12119, "loader_excerpt": "s.store(C,29+o,e.detached),n=Lt()+40,Atomics.store(C,43+o,n),t.ua=r,{cmd:\"run\",start_routine:e.nb,arg:e.Aa,threadInfoStruct:e.Ia,stackBase:e.za,stackSize:e.Ba});return t.Da=function(){i.time=performance.now(),t.postMessage(i,e.ub)},t.loaded&&(t.Da(),delete t.Da),0}function Te(e,t,n){if(e<=0||e>h.length||1&e)return-28;if(z){if(Atomics.load(_,e>>2)!=t)return-6;for(n=performance.now()+n,Atomics.exchange(_,zt>>2,e);;){if(n<performance.now())return Atomics.exchange(_,zt>>2,0),-73;if(0==Atomics.exchange(_,zt>>2,0))break;if(Dt(),Atomics.load(_,e>>2)!=t)return-6;Atomics.exchange(_,zt>>2,e)}return 0}if(\"timed-out\"===(e=Atomics.wait(_,e>>2,t,n)))return-73;if(\"not-equal\"===e)return-6;if(\"ok\"===e)return 0;throw\"Atomics.wait returned an unexpected value \"+e}function Ie(){s||o||(J=J||{})[\"Blocking on th", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31057"></a>
## FND-31057 — module-003 import a.h

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "h", "kind": "function", "type_index": 44, "function_index": 6, "signature": {"parameters": [], "results": ["f64"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 15069, "loader_excerpt": "/4294967296|0}function ze(r,n,a,o,t){function i(e){var t=0,n=0;e&&(n=w.response?w.response.byteLength:0,t=U(n),I.set(new Uint8Array(w.response),t)),C[r+12>>2]=t,L(r+16,n)}if(p=C[r+8>>2]){var e=O(p),s=(s=O(_=r+112))||\"GET\",u=C[_+52>>2],c=C[_+56>>2],f=!!C[_+60>>2],l=C[_+68>>2],d=C[_+72>>2],p=C[_+76>>2],m=C[_+80>>2],h=C[_+84>>2],_=C[_+88>>2],y=!!(1&u),g=!!(2&u),u=!!(64&u),l=l?O(l):void 0,d=d?O(d):void 0,v=m?O(m):void 0,w=new XMLHttpRequest;if(w.withCredentials=f,w.open(s,e,!u,l,d),u||(w.timeout=c),w.vb=e,w.responseType=\"arraybuffer\",m&&w.overrideMimeType(v),p)for(;(s=C[p>>2])&&(e=C[p+4>>2]);)p+=8,s=O(s),e=O(e),w.setRequestHeader(s,e);Ve.push(w),C[r+0>>2]=Ve.length,p=h&&_?I.slice(h,h+_):null,w.onload=function(e){i(y&&!g);var t=w.response?w.response.byteLength:0;L(r+24,0),t&&L(r+32,t),D[r+40>>1", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31058"></a>
## FND-31058 — module-003 import a.i

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "i", "kind": "function", "type_index": 0, "function_index": 7, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29732, "loader_excerpt": "_[t+8],Db:_[t+9],Va:_[t+10],cb:_[t+11],Fb:_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to asynchronously ", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31059"></a>
## FND-31059 — module-003 import a.j

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "j", "kind": "function", "type_index": 10, "function_index": 8, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29846, "loader_excerpt": "Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to asynchronously prepare wasm: \"+e),y(e)})}var a={a:St};if(f||ve(),i.instantiateWasm)try{var e=i.instantiateWasm(a,t);return Et(e)}", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31060"></a>
## FND-31060 — module-003 import a.k

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "k", "kind": "function", "type_index": 3, "function_index": 9, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 26473, "loader_excerpt": "e(C,n+64>>2,1),f?postMessage({cmd:\"cleanupThread\",thread:n}):Me(n),0;Ft(),f||Dt(),Te(n,a,f?100:1)}},k:Re,w:je,x:Le,O:function(e){delete Ve[e-1]},N:function(e,t){if(e==t)postMessage({cmd:\"processQueuedMainThreadWork\"});else if(f)postMessage({targetThread:e,cmd:\"processThreadQueue\"});else{if(!(e=(e=v.va[e])&&e.worker))return;e.postMessage({cmd:\"processThreadQueue\"})}return 1},d:Ue,D:function(e,t){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return _[Ut()>>2]=28,-1;e=De()}return _[t>>2]=e/1e3|0,_[t+4>>2]=e%1e3*1e6|0,0},P:function(e,t,n){var r;for(Pe.length=0,n>>=2;r=I[t++];)(r=r<105)&&1&n&&n++,Pe.push(r?oe[n++>>1]:_[n]),++n;return Ae[e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=o", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31061"></a>
## FND-31061 — module-003 import a.l

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "l", "kind": "function", "type_index": 1, "function_index": 10, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 2396, "loader_excerpt": "function(e,t){return r=r||require(\"fs\"),e=(V=V||require(\"path\")).normalize(e),r.readFileSync(e,t?null:\"utf8\")},K=function(e){return re((e=(e=X(e,!0)).buffer?e:new Uint8Array(e)).buffer),e};1<process.argv.length&&(Y=process.argv[1].replace(/\\\\/g,\"/\")),H=process.argv.slice(2),process.on(\"uncaughtException\",function(e){if(!(e instanceof M))throw e}),process.on(\"unhandledRejection\",y),G=function(e,t){if(_e())throw process.exitCode=e,t;process.exit(e)},i.inspect=function(){return\"[Emscripten Module object]\"};try{d=require(\"worker_threads\")}catch(e){throw console.error('The \"worker_threads\" module is not supported in this node.js build - perhaps a newer version is needed?'),e}global.Worker=d.Worker}else(z||o)&&(o?a=self.location.href:\"undefined\"!=typeof document&&document.currentScript&&(a=docum", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31062"></a>
## FND-31062 — module-003 import a.m

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "m", "kind": "function", "type_index": 0, "function_index": 11, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 5673, "loader_excerpt": "ffer;else if(i.wasmMemory)u=i.wasmMemory;else if(!((u=new WebAssembly.Memory({initial:d/65536,maximum:d/65536,shared:!0})).buffer instanceof SharedArrayBuffer))throw l(\"requested a shared WebAssembly.Memory but the returned buffer is not a SharedArrayBuffer, indicating that while the browser has SharedArrayBuffer it does not have WebAssembly threads support - you may need to set a flag\"),s&&console.log(\"(on node you may need: --experimental-wasm-threads --experimental-wasm-bulk-memory and also use a recent version)\"),Error(\"bad memory\");(fe=u?u.buffer:fe).byteLength;var fe=d=fe,le=(i.HEAP8=h=new Int8Array(d),i.HEAP16=new Int16Array(d),i.HEAP32=_=new Int32Array(d),i.HEAPU8=I=new Uint8Array(d),i.HEAPU16=D=new Uint16Array(d),i.HEAPU32=C=new Uint32Array(d),i.HEAPF32=new Float32Array(d),i.HEAPF", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31063"></a>
## FND-31063 — module-003 import a.n

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "n", "kind": "function", "type_index": 4, "function_index": 12, "signature": {"parameters": ["i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 699, "loader_excerpt": "on(e,t){k=e,T=t}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var n,r={open:function(e,t){n=t},send:function(){require(\"fs\").readFile(n,function(e,t){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=t,r.onreadystatechange(),r.onload())})}};return r}),i.postCustomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.forEach(function(e){i.queue.put(e)}),i.qu", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31064"></a>
## FND-31064 — module-003 import a.o

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "o", "kind": "function", "type_index": 0, "function_index": 13, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 4606, "loader_excerpt": "[t++],192==(224&i)?r+=String.fromCharCode((31&i)<<6|a):(o=63&e[t++],(i=224==(240&i)?(15&i)<<12|a<<6|o:(7&i)<<18|a<<12|o<<6|63&e[t++])<65536?r+=String.fromCharCode(i):(i-=65536,r+=String.fromCharCode(55296|i>>10,56320|1023&i)))):r+=String.fromCharCode(i)}return r}function O(e){return e?se(I,e,void 0):\"\"}function F(e,t,n,r){if(0<r){r=n+r-1;for(var a=0;a<e.length;++a){var o=e.charCodeAt(a);if((o=55296<=o&&o<=57343?65536+((1023&o)<<10)|1023&e.charCodeAt(++a):o)<=127){if(r<=n)break;t[n++]=o}else{if(o<=2047){if(r<=n+1)break;t[n++]=192|o>>6}else{if(o<=65535){if(r<=n+2)break;t[n++]=224|o>>12}else{if(r<=n+3)break;t[n++]=240|o>>18,t[n++]=128|o>>12&63}t[n++]=128|o>>6&63}t[n++]=128|63&o}}t[n]=0}}function ue(e){for(var t=0,n=0;n<e.length;++n){var r=e.charCodeAt(n);(r=55296<=r&&r<=57343?65536+((1023&r)<", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31065"></a>
## FND-31065 — module-003 import a.p

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "p", "kind": "function", "type_index": 3, "function_index": 14, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 25062, "loader_excerpt": "y(\"Assertion failed: \"+O(e)+\", at: \"+[t?O(t):\"unknown filename\",n,r?O(r):\"unknown function\"])},b:Se,p:function(e,t){v.Sa.push(function(){P.apply(null,[e,t])})},K:function(e,t,n,r){if(\"undefined\"==typeof SharedArrayBuffer)return l(\"Current environment does not support SharedArrayBuffer, pthreads are not available!\"),6;if(!e)return l(\"pthread_create called with a null thread pointer!\"),28;var a=[];if(f&&0===a.length)return It(687865856,e,t,n,r);var o,i=0,s=0;t&&-1!=t?(o=_[t>>2],o+=81920,i=_[t+8>>2],s=0!==_[t+12>>2]):o=2097152,(t=0==i)?i=Ht(16,o):re(0<(i-=o));for(var u=U(228),c=0;c<57;++c)C[(u>>2)+c]=0;return _[e>>2]=u,_[u+12>>2]=u,_[(e=u+152)>>2]=e,n={za:i,Ba:o,Na:t,detached:s,nb:n,Ia:u,Aa:r,ub:a},f?(n.xb=\"spawnThread\",postMessage(n,a),0):ke(n)},I:function(e){throw f?v.ab(e):(v.Za(),Xt(e)),\"", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31066"></a>
## FND-31066 — module-003 import a.q

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "q", "kind": "function", "type_index": 14, "function_index": 15, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29279, "loader_excerpt": "Not Found\",I,M+44,64),k(M,0,e)}}catch(e){k(M,0,e)}}else k(M,0,\"IndexedDB not available!\")}return e},q:function(){return t=async()=>{var e=await i.queue.get(),t=ue(e)+1,n=U(t);return F(e,I,n,t),n},At(function(e){t().then(e)});var t},H:function(e,t){return t={alpha:!!_[t>>=2],depth:!!_[t+1],stencil:!!_[t+2],antialias:!!_[t+3],premultipliedAlpha:!!_[t+4],preserveDrawingBuffer:!!_[t+5],powerPreference:$e[_[t+6]],failIfMajorPerformanceCaveat:!!_[t+7],jb:_[t+8],Db:_[t+9],Va:_[t+10],cb:_[t+11],Fb:_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T)", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31067"></a>
## FND-31067 — module-003 import a.r

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "r", "kind": "function", "type_index": 0, "function_index": 16, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 6129, "loader_excerpt": "s --experimental-wasm-bulk-memory and also use a recent version)\"),Error(\"bad memory\");(fe=u?u.buffer:fe).byteLength;var fe=d=fe,le=(i.HEAP8=h=new Int8Array(d),i.HEAP16=new Int16Array(d),i.HEAP32=_=new Int32Array(d),i.HEAPU8=I=new Uint8Array(d),i.HEAPU16=D=new Uint16Array(d),i.HEAPU32=C=new Uint32Array(d),i.HEAPF32=new Float32Array(d),i.HEAPF64=oe=new Float64Array(d),[]),de=[],pe=[],me=[],he=[],R=0;function _e(){return ee||0<R}var p,m=0,ye=null,ge=null;function ve(){m++,i.monitorRunDependencies&&i.monitorRunDependencies(m)}function we(){var e;m--,i.monitorRunDependencies&&i.monitorRunDependencies(m),0==m&&(null!==ye&&(clearInterval(ye),ye=null),ge)&&(e=ge,ge=null,e())}function y(e){throw i.onAbort&&i.onAbort(e),re(!f),l(e),c=!0,ne=1,e=new WebAssembly.RuntimeError(\"abort(\"+e+\"). Build with ", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31068"></a>
## FND-31068 — module-003 import a.s

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "s", "kind": "function", "type_index": 10, "function_index": 17, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 52, "loader_excerpt": "/*!\n * Stockfish.js (c) 2023, Chess.com, LLC\n * https://github.com/nmrugg/stockfish.js\n * License: GPLv3\n *\n * Based on stockfish.wasm (c)\n * Niklas Fiekas <niklas.fiekas@backscattering.de>\n * Hiroshi Ogawa <hi.ogawa.zz@gmail.com>\n * https://github.com/niklasf/stockfish.wasm\n * https://github.com/hi-ogawa/Stockfish\n *\n * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.\n * https://github.com/official-stockfish/Stockfish\n */!function(){var $t,e,n,t,r,a;function i(){function e(S){var i,k,T,t,n;S=S||{},(i=i||(void 0!==S?S:{})).ready=new Promise(function(e,t){k=e,T=t}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var n,r={open:function(e,t){n=t},send:function(){require(\"fs\").re", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31069"></a>
## FND-31069 — module-003 import a.t

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "t", "kind": "function", "type_index": 7, "function_index": 18, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 1023, "loader_excerpt": "tomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.forEach(function(e){i.queue.put(e)}),i.queue.process()},i.postMessage=i.postCustomMessage,[]),N=(i.addMessageListener=function(e){W.push(e)},i.removeMessageListener=function(e){0<=(e=W.indexOf(e))&&W.splice(e,1)},i.print=i.printErr=function(e){if(\"Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31070"></a>
## FND-31070 — module-003 import a.u

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "u", "kind": "function", "type_index": 3, "function_index": 19, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 27069, "loader_excerpt": "Pe.push(r?oe[n++>>1]:_[n]),++n;return Ae[e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];return(e<0?Ae[-e-1]:Mt[e]).apply(null,qe)},v:function(){y(\"OOM\")},G:function(e,t,n){return(Ne(e)?He:Ye)(e,t,n)},m:function(){},M:function(e,t,n){return R+=1,setTimeout(function(){--R,j(function(){P.apply(null,[e,n])})},t)},c:function(n){At(function(e){var t;t=e,R+=1,$t(function(){--R,j(t)},n)})},o:function(e,n,t,r,a){function o(e,t){Qe(e,t.response,function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)},function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)})}function i(e){j(function(){h?P.apply(null,[h,e]):a&&a(e)},w)}function s(e){--R,j(function(){p?P.apply(null,[p", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31071"></a>
## FND-31071 — module-003 import a.v

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "v", "kind": "function", "type_index": 1, "function_index": 20, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 27223, "loader_excerpt": "t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];return(e<0?Ae[-e-1]:Mt[e]).apply(null,qe)},v:function(){y(\"OOM\")},G:function(e,t,n){return(Ne(e)?He:Ye)(e,t,n)},m:function(){},M:function(e,t,n){return R+=1,setTimeout(function(){--R,j(function(){P.apply(null,[e,n])})},t)},c:function(n){At(function(e){var t;t=e,R+=1,$t(function(){--R,j(t)},n)})},o:function(e,n,t,r,a){function o(e,t){Qe(e,t.response,function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)},function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)})}function i(e){j(function(){h?P.apply(null,[h,e]):a&&a(e)},w)}function s(e){--R,j(function(){p?P.apply(null,[p,e]):t&&t(e)},w)}function u(e){j(function(){m?P.apply(null,[m,e]):r&&r(e)},w)}function c(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)}R+=1;var f=", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31072"></a>
## FND-31072 — module-003 import a.w

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "w", "kind": "function", "type_index": 3, "function_index": 21, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 14086, "loader_excerpt": ",t),qt(r),n}var qe=[],We=[0,\"undefined\"!=typeof document?document:0,\"undefined\"!=typeof window?window:0];function Ne(e){return e=2<e?O(e):e,We[e]||(\"undefined\"!=typeof document?document.querySelector(e):void 0)}function He(e,t,n){var r,a,o,i,s=Ne(e);return s?(s.Ha&&(_[s.Ha>>2]=t,_[s.Ha+4>>2]=n),!s.Ya&&s.yb?s.Ha?(s=_[s.Ha+8>>2],e=e?O(e):\"\",r=Bt(),a=Wt(12),o=0,e&&(o=ue(e)+1,i=U(o),F(e,I,i,o),o=i),_[a>>2]=o,_[a+4>>2]=t,_[a+8>>2]=n,Ot(0,s,657457152,0,o,a),qt(r),1):-4:(e=!1,(s=s.Ya?s.Ya:s).Ga&&s.Ga.Fa&&(e=0===(e=s.Ga.Fa.getParameter(2978))[0]&&0===e[1]&&e[2]===s.width&&e[3]===s.height),s.width=t,s.height=n,e&&s.Ga.Fa.viewport(0,0,t,n),0)):-4}function Ye(e,t,n){return f?w(7,1,e,t,n):He(e,t,n)}function j(e,t){if(!c)if(t)e();else{try{e()}catch(e){if(e instanceof M)return;if(\"unwind\"!==e)throw e&&\"", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31073"></a>
## FND-31073 — module-003 import a.x

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "x", "kind": "function", "type_index": 3, "function_index": 22, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 26483, "loader_excerpt": "2,1),f?postMessage({cmd:\"cleanupThread\",thread:n}):Me(n),0;Ft(),f||Dt(),Te(n,a,f?100:1)}},k:Re,w:je,x:Le,O:function(e){delete Ve[e-1]},N:function(e,t){if(e==t)postMessage({cmd:\"processQueuedMainThreadWork\"});else if(f)postMessage({targetThread:e,cmd:\"processThreadQueue\"});else{if(!(e=(e=v.va[e])&&e.worker))return;e.postMessage({cmd:\"processThreadQueue\"})}return 1},d:Ue,D:function(e,t){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return _[Ut()>>2]=28,-1;e=De()}return _[t>>2]=e/1e3|0,_[t+4>>2]=e%1e3*1e6|0,0},P:function(e,t,n){var r;for(Pe.length=0,n>>=2;r=I[t++];)(r=r<105)&&1&n&&n++,Pe.push(r?oe[n++>>1]:_[n]),++n;return Ae[e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];ret", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31074"></a>
## FND-31074 — module-003 import a.y

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "y", "kind": "function", "type_index": 6, "function_index": 23, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11163, "loader_excerpt": "),a.on(\"exit\",function(){})),a.postMessage({cmd:\"load\",urlOrBlob:i.mainScriptUrlOrBlob||Jt,wasmMemory:u,wasmModule:te})},Ua:function(){var e=Q(\"stockfish.worker.js\");v.xa.push(new Worker(e))},eb:function(){return 0==v.xa.length&&(v.Ua(),v.Xa(v.xa[0])),v.xa.pop()},wb:function(e){for(e=performance.now()+e;performance.now()<e;);}};function Se(e,t){if(f)return w(1,1,e,t);me.unshift({Pa:e,Aa:t})}function ke(e){if(f)throw\"Internal Error! spawnThread() can only ever be called from main application thread!\";var t=v.eb();if(!t)return 6;if(void 0!==t.ua)throw\"Internal error!\";if(!e.Ia)throw\"Internal error, no pthread ptr!\";v.ya.push(t);for(var n=U(512),r=0;r<128;++r)_[n+4*r>>2]=0;var a=e.za+e.Ba,o=(r=v.va[e.Ia]={worker:t,za:e.za,Ba:e.Ba,Na:e.Na,wa:e.Ia}).wa>>2,i=(Atomics.store(C,16+o,e.detached),Ato", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31075"></a>
## FND-31075 — module-003 import a.z

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "z", "kind": "function", "type_index": 6, "function_index": 24, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29758, "loader_excerpt": "],cb:_[t+11],Fb:_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to asynchronously prepare wasm: \"+e),y(e)})}", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31076"></a>
## FND-31076 — module-003 import a.A

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "A", "kind": "function", "type_index": 7, "function_index": 25, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29841, "loader_excerpt": "n(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to asynchronously prepare wasm: \"+e),y(e)})}var a={a:St};if(f||ve(),i.instantiateWasm)try{var e=i.instantiateWasm(a,t);return E", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31077"></a>
## FND-31077 — module-003 import a.B

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "B", "kind": "function", "type_index": 2, "function_index": 26, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29722, "loader_excerpt": "_[t+7],jb:_[t+8],Db:_[t+9],Va:_[t+10],cb:_[t+11],Fb:_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to async", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31078"></a>
## FND-31078 — module-003 import a.C

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "C", "kind": "function", "type_index": 2, "function_index": 27, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29727, "loader_excerpt": "],jb:_[t+8],Db:_[t+9],Va:_[t+10],cb:_[t+11],Fb:_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to asynchrono", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31079"></a>
## FND-31079 — module-003 import a.D

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "import", "module": "a", "name": "D", "kind": "function", "type_index": 2, "function_index": 28, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 18369, "loader_excerpt": "gh-performance\"],Ze={};function et(){if(!Je){var e,t={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:Y||\"./this.program\"};for(e in Ze)void 0===Ze[e]?delete t[e]:t[e]=Ze[e];var n=[];for(e in t)n.push(e+\"=\"+t[e]);Je=n}return Je}function tt(r,a){var o;return f?w(8,1,r,a):(o=0,et().forEach(function(e,t){var n=a+o;for(t=_[r+4*t>>2]=n,n=0;n<e.length;++n)h[t++>>0]=e.charCodeAt(n);h[t>>0]=0,o+=e.length+1}),0)}function nt(e,t){var n,r;return f?w(9,1,e,t):(n=et(),_[e>>2]=n.length,r=0,n.forEach(function(e){r+=e.length+1}),_[t>>2]=r,0)}function rt(e){return f?w(10,1,e):0}function at(e,t,n,r){return f?w(11,1,e,t,n,r):(e=Fe.Bb(e),t=Fe.Ab(e,t,n),_[r>>2]=t,0)}function ", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```
