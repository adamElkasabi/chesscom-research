# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30960"></a>
## FND-30960 — module-002 export dynCall_iijji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iijji", "kind": "function", "index": 23025, "signature": {"parameters": ["i32", "i32", "i64", "i64", "i32"], "results": ["i32"]}, "type_index": 104, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114737, "loader_excerpt": "nCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_ji", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30961"></a>
## FND-30961 — module-002 export dynCall_vdii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vdii", "kind": "function", "index": 23026, "signature": {"parameters": ["i32", "f64", "i32", "i32"], "results": []}, "type_index": 67, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114899, "loader_excerpt": "l_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30962"></a>
## FND-30962 — module-002 export dynCall_idiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_idiiii", "kind": "function", "index": 23027, "signature": {"parameters": ["i32", "f64", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 106, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114955, "loader_excerpt": "iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dy", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30963"></a>
## FND-30963 — module-002 export dynCall_vji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vji", "kind": "function", "index": 23028, "signature": {"parameters": ["i32", "i64", "i32"], "results": []}, "type_index": 33, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115007, "loader_excerpt": "_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30964"></a>
## FND-30964 — module-002 export dynCall_viiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiii", "kind": "function", "index": 23029, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 9, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114218, "loader_excerpt": "Call_iiiiiii,dynCall_i=dynCalls.i=wasmExports.dynCall_i,dynCall_viiiiii=dynCalls.viiiiii=wasmExports.dynCall_viiiiii,dynCall_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30965"></a>
## FND-30965 — module-002 export dynCall_ji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_ji", "kind": "function", "index": 23030, "signature": {"parameters": ["i32", "i32"], "results": ["i64"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114448, "loader_excerpt": "iiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30966"></a>
## FND-30966 — module-002 export dynCall_viiji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiji", "kind": "function", "index": 23031, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": []}, "type_index": 45, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115164, "loader_excerpt": "ynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30967"></a>
## FND-30967 — module-002 export dynCall_iij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iij", "kind": "function", "index": 23032, "signature": {"parameters": ["i32", "i32", "i64"], "results": ["i32"]}, "type_index": 26, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114677, "loader_excerpt": "Call_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30968"></a>
## FND-30968 — module-002 export dynCall_iif

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iif", "kind": "function", "index": 23033, "signature": {"parameters": ["i32", "i32", "f32"], "results": ["i32"]}, "type_index": 107, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115264, "loader_excerpt": ".dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30969"></a>
## FND-30969 — module-002 export dynCall_viiiffi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiffi", "kind": "function", "index": 23034, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f32", "f32", "i32"], "results": []}, "type_index": 108, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115321, "loader_excerpt": "ll_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30970"></a>
## FND-30970 — module-002 export dynCall_jiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jiii", "kind": "function", "index": 23035, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i64"]}, "type_index": 38, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115376, "loader_excerpt": ",dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fi", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30971"></a>
## FND-30971 — module-002 export dynCall_jii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jii", "kind": "function", "index": 23036, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i64"]}, "type_index": 20, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115376, "loader_excerpt": ",dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fi", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30972"></a>
## FND-30972 — module-002 export dynCall_iiiij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiij", "kind": "function", "index": 23037, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "type_index": 39, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115479, "loader_excerpt": "nCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30973"></a>
## FND-30973 — module-002 export dynCall_iiij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiij", "kind": "function", "index": 23038, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i32"]}, "type_index": 34, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115532, "loader_excerpt": "ll_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30974"></a>
## FND-30974 — module-002 export dynCall_jiij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jiij", "kind": "function", "index": 23039, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": ["i64"]}, "type_index": 68, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115584, "loader_excerpt": "all_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30975"></a>
## FND-30975 — module-002 export dynCall_jiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jiiii", "kind": "function", "index": 23040, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "type_index": 110, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115638, "loader_excerpt": "ll_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30976"></a>
## FND-30976 — module-002 export dynCall_vij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vij", "kind": "function", "index": 23041, "signature": {"parameters": ["i32", "i32", "i64"], "results": []}, "type_index": 24, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115689, "loader_excerpt": "all_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiij", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30977"></a>
## FND-30977 — module-002 export dynCall_jiiiijjj

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jiiiijjj", "kind": "function", "index": 23042, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64", "i64"], "results": ["i64"]}, "type_index": 111, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115748, "loader_excerpt": "iiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30978"></a>
## FND-30978 — module-002 export dynCall_iiiji

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiji", "kind": "function", "index": 23043, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": ["i32"]}, "type_index": 112, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115806, "loader_excerpt": "all_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30979"></a>
## FND-30979 — module-002 export dynCall_jiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_jiiiiiii", "kind": "function", "index": 23044, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "type_index": 109, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115867, "loader_excerpt": "ynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30980"></a>
## FND-30980 — module-002 export dynCall_viiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiii", "kind": "function", "index": 23045, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 18, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114338, "loader_excerpt": "Call_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30981"></a>
## FND-30981 — module-002 export dynCall_vidii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vidii", "kind": "function", "index": 23046, "signature": {"parameters": ["i32", "i32", "f64", "i32", "i32"], "results": []}, "type_index": 113, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115989, "loader_excerpt": "all_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30982"></a>
## FND-30982 — module-002 export dynCall_dii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_dii", "kind": "function", "index": 23047, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f64"]}, "type_index": 46, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116040, "loader_excerpt": "viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30983"></a>
## FND-30983 — module-002 export dynCall_fii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_fii", "kind": "function", "index": 23048, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f32"]}, "type_index": 47, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116089, "loader_excerpt": ".dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30984"></a>
## FND-30984 — module-002 export dynCall_idi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_idi", "kind": "function", "index": 23049, "signature": {"parameters": ["i32", "f64", "i32"], "results": ["i32"]}, "type_index": 186, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114955, "loader_excerpt": "iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dy", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30985"></a>
## FND-30985 — module-002 export dynCall_di

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_di", "kind": "function", "index": 23050, "signature": {"parameters": ["i32", "i32"], "results": ["f64"]}, "type_index": 19, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116040, "loader_excerpt": "viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30986"></a>
## FND-30986 — module-002 export dynCall_iddi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iddi", "kind": "function", "index": 23051, "signature": {"parameters": ["i32", "f64", "f64", "i32"], "results": ["i32"]}, "type_index": 187, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116235, "loader_excerpt": "rts.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30987"></a>
## FND-30987 — module-002 export dynCall_fiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_fiii", "kind": "function", "index": 23052, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f32"]}, "type_index": 53, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116287, "loader_excerpt": "ynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.dii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30988"></a>
## FND-30988 — module-002 export dynCall_iiiiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiiiiiiiiii", "kind": "function", "index": 23053, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 54, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116355, "loader_excerpt": "l_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30989"></a>
## FND-30989 — module-002 export dynCall_iiijii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiijii", "kind": "function", "index": 23054, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "type_index": 48, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116419, "loader_excerpt": "ii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30990"></a>
## FND-30990 — module-002 export dynCall_viij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viij", "kind": "function", "index": 23055, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": []}, "type_index": 23, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115164, "loader_excerpt": "ynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30991"></a>
## FND-30991 — module-002 export dynCall_iiiijii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiiijii", "kind": "function", "index": 23056, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "type_index": 86, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116531, "loader_excerpt": "jii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=w", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30992"></a>
## FND-30992 — module-002 export dynCall_iiijj

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiijj", "kind": "function", "index": 23057, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "type_index": 87, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116588, "loader_excerpt": "ynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30993"></a>
## FND-30993 — module-002 export dynCall_viiijii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiijii", "kind": "function", "index": 23058, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "type_index": 114, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116647, "loader_excerpt": ",dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30994"></a>
## FND-30994 — module-002 export dynCall_viijii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viijii", "kind": "function", "index": 23059, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "type_index": 55, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116706, "loader_excerpt": "Call_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_ii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30995"></a>
## FND-30995 — module-002 export dynCall_viiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiiii", "kind": "function", "index": 23060, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 27, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116772, "loader_excerpt": "viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30996"></a>
## FND-30996 — module-002 export dynCall_iid

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iid", "kind": "function", "index": 23061, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["i32"]}, "type_index": 88, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116828, "loader_excerpt": "l_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30997"></a>
## FND-30997 — module-002 export dynCall_viid

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viid", "kind": "function", "index": 23062, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": []}, "type_index": 40, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116879, "loader_excerpt": "l_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30998"></a>
## FND-30998 — module-002 export dynCall_fiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_fiiiiiiii", "kind": "function", "index": 23063, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "type_index": 115, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116941, "loader_excerpt": "dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30999"></a>
## FND-30999 — module-002 export dynCall_diiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_diiiii", "kind": "function", "index": 23064, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f64"]}, "type_index": 116, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117002, "loader_excerpt": "iiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExport", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31000"></a>
## FND-31000 — module-002 export dynCall_viiiid

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiid", "kind": "function", "index": 23065, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": []}, "type_index": 117, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117060, "loader_excerpt": "dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExpor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31001"></a>
## FND-31001 — module-002 export dynCall_viiidi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiidi", "kind": "function", "index": 23066, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32"], "results": []}, "type_index": 89, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117118, "loader_excerpt": "dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExpor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31002"></a>
## FND-31002 — module-002 export dynCall_vifii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vifii", "kind": "function", "index": 23067, "signature": {"parameters": ["i32", "i32", "f32", "i32", "i32"], "results": []}, "type_index": 118, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117174, "loader_excerpt": "d,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31003"></a>
## FND-31003 — module-002 export dynCall_viiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiiiii", "kind": "function", "index": 23068, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 90, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117241, "loader_excerpt": "_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31004"></a>
## FND-31004 — module-002 export dynCall_viiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiiiiiiii", "kind": "function", "index": 23069, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 69, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117320, "loader_excerpt": "iiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31005"></a>
## FND-31005 — module-002 export dynCall_diii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_diii", "kind": "function", "index": 23070, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f64"]}, "type_index": 70, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117002, "loader_excerpt": "iiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExport", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31006"></a>
## FND-31006 — module-002 export dynCall_iiidi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iiidi", "kind": "function", "index": 23071, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": ["i32"]}, "type_index": 119, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117436, "loader_excerpt": "iiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31007"></a>
## FND-31007 — module-002 export dynCall_vidi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vidi", "kind": "function", "index": 23072, "signature": {"parameters": ["i32", "i32", "f64", "i32"], "results": []}, "type_index": 71, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115989, "loader_excerpt": "all_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31008"></a>
## FND-31008 — module-002 export dynCall_viiiiiiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiiiiiiiii", "kind": "function", "index": 23073, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 56, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117563, "loader_excerpt": "=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31009"></a>
## FND-31009 — module-002 export dynCall_viiiiiiiiiiii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiiiiiiii", "kind": "function", "index": 23074, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 57, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117320, "loader_excerpt": "iiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31010"></a>
## FND-31010 — module-002 export dynCall_vif

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_vif", "kind": "function", "index": 23075, "signature": {"parameters": ["i32", "i32", "f32"], "results": []}, "type_index": 72, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117174, "loader_excerpt": "d,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31011"></a>
## FND-31011 — module-002 export dynCall_viiiiiij

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiiiij", "kind": "function", "index": 23076, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i64"], "results": []}, "type_index": 120, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117762, "loader_excerpt": "iiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynC", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31012"></a>
## FND-31012 — module-002 export dynCall_viiid

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiid", "kind": "function", "index": 23077, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64"], "results": []}, "type_index": 58, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117118, "loader_excerpt": "dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExpor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31013"></a>
## FND-31013 — module-002 export dynCall_viiiddi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiddi", "kind": "function", "index": 23078, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "f64", "i32"], "results": []}, "type_index": 188, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117879, "loader_excerpt": ",dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31014"></a>
## FND-31014 — module-002 export dynCall_did

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_did", "kind": "function", "index": 23079, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["f64"]}, "type_index": 59, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117932, "loader_excerpt": "id,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31015"></a>
## FND-31015 — module-002 export dynCall_diid

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_diid", "kind": "function", "index": 23080, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": ["f64"]}, "type_index": 121, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117983, "loader_excerpt": "Call_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCal", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31016"></a>
## FND-31016 — module-002 export dynCall_iddd

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_iddd", "kind": "function", "index": 23081, "signature": {"parameters": ["i32", "f64", "f64", "f64"], "results": ["i32"]}, "type_index": 122, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118035, "loader_excerpt": "nCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31017"></a>
## FND-31017 — module-002 export dynCall_diddd

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_diddd", "kind": "function", "index": 23082, "signature": {"parameters": ["i32", "i32", "f64", "f64", "f64"], "results": ["f64"]}, "type_index": 124, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118089, "loader_excerpt": "ll_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynC", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31018"></a>
## FND-31018 — module-002 export dynCall_viidi

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viidi", "kind": "function", "index": 23083, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": []}, "type_index": 60, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118144, "loader_excerpt": "iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31019"></a>
## FND-31019 — module-002 export dynCall_viiiidii

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
{"module_id": "module-002", "direction": "export", "name": "dynCall_viiiidii", "kind": "function", "index": 23084, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "type_index": 123, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118205, "loader_excerpt": "ynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viif=dynCalls.viif=wasmExports.dynCall_viif,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
