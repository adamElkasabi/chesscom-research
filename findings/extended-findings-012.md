# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30660"></a>
## FND-30660 — module-001 export dynCall_jiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jiiii", "kind": "function", "index": 23009, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "type_index": 108, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115453, "loader_excerpt": "ll_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30661"></a>
## FND-30661 — module-001 export dynCall_vij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vij", "kind": "function", "index": 23010, "signature": {"parameters": ["i32", "i32", "i64"], "results": []}, "type_index": 24, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115504, "loader_excerpt": "all_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiij", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30662"></a>
## FND-30662 — module-001 export dynCall_jiiiijjj

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jiiiijjj", "kind": "function", "index": 23011, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64", "i64"], "results": ["i64"]}, "type_index": 109, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115563, "loader_excerpt": "iiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30663"></a>
## FND-30663 — module-001 export dynCall_iiiji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiji", "kind": "function", "index": 23012, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32"], "results": ["i32"]}, "type_index": 110, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115621, "loader_excerpt": "all_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30664"></a>
## FND-30664 — module-001 export dynCall_jiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jiiiiiii", "kind": "function", "index": 23013, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i64"]}, "type_index": 107, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115682, "loader_excerpt": "ynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExports.dynCall_jiiiiiii,dynCall_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30665"></a>
## FND-30665 — module-001 export dynCall_viiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiii", "kind": "function", "index": 23014, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 18, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114153, "loader_excerpt": "Call_viiii=dynCalls.viiii=wasmExports.dynCall_viiii,dynCall_viiiiiiii=dynCalls.viiiiiiii=wasmExports.dynCall_viiiiiiii,dynCall_iiiii=dynCalls.iiiii=wasmExports.dynCall_iiiii,dynCall_jij=dynCalls.jij=wasmExports.dynCall_jij,dynCall_iiiiii=dynCalls.iiiiii=wasmExports.dynCall_iiiiii,dynCall_vjjii=dynCalls.vjjii=wasmExports.dynCall_vjjii,dynCall_ijjiiii=dynCalls.ijjiiii=wasmExports.dynCall_ijjiiii,dynCall_iijiii=dynCalls.iijiii=wasmExports.dynCall_iijiii,dynCall_iijjiii=dynCalls.iijjiii=wasmExports.dynCall_iijjiii,dynCall_iiji=dynCalls.iiji=wasmExports.dynCall_iiji,dynCall_iijji=dynCalls.iijji=wasmExports.dynCall_iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30666"></a>
## FND-30666 — module-001 export dynCall_vidii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vidii", "kind": "function", "index": 23015, "signature": {"parameters": ["i32", "i32", "f64", "i32", "i32"], "results": []}, "type_index": 111, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115804, "loader_excerpt": "all_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30667"></a>
## FND-30667 — module-001 export dynCall_dii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_dii", "kind": "function", "index": 23016, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f64"]}, "type_index": 46, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115855, "loader_excerpt": "viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30668"></a>
## FND-30668 — module-001 export dynCall_fii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_fii", "kind": "function", "index": 23017, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f32"]}, "type_index": 47, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115904, "loader_excerpt": ".dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30669"></a>
## FND-30669 — module-001 export dynCall_idi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_idi", "kind": "function", "index": 23018, "signature": {"parameters": ["i32", "f64", "i32"], "results": ["i32"]}, "type_index": 185, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114770, "loader_excerpt": "iijji,dynCall_vdii=dynCalls.vdii=wasmExports.dynCall_vdii,dynCall_idiiii=dynCalls.idiiii=wasmExports.dynCall_idiiii,dynCall_vji=dynCalls.vji=wasmExports.dynCall_vji,dynCall_viiiii=dynCalls.viiiii=wasmExports.dynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dy", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30670"></a>
## FND-30670 — module-001 export dynCall_di

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_di", "kind": "function", "index": 23019, "signature": {"parameters": ["i32", "i32"], "results": ["f64"]}, "type_index": 19, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115855, "loader_excerpt": "viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30671"></a>
## FND-30671 — module-001 export dynCall_iddi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iddi", "kind": "function", "index": 23020, "signature": {"parameters": ["i32", "f64", "f64", "i32"], "results": ["i32"]}, "type_index": 186, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116050, "loader_excerpt": "rts.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30672"></a>
## FND-30672 — module-001 export dynCall_fiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_fiii", "kind": "function", "index": 23021, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f32"]}, "type_index": 53, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116102, "loader_excerpt": "ynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.dii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30673"></a>
## FND-30673 — module-001 export dynCall_iiiiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiiiiiiiii", "kind": "function", "index": 23022, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 54, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116170, "loader_excerpt": "l_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30674"></a>
## FND-30674 — module-001 export dynCall_iiijii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiijii", "kind": "function", "index": 23023, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "type_index": 48, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116234, "loader_excerpt": "ii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30675"></a>
## FND-30675 — module-001 export dynCall_viij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viij", "kind": "function", "index": 23024, "signature": {"parameters": ["i32", "i32", "i32", "i64"], "results": []}, "type_index": 23, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 114979, "loader_excerpt": "ynCall_viiiii,dynCall_ji=dynCalls.ji=wasmExports.dynCall_ji,dynCall_viiji=dynCalls.viiji=wasmExports.dynCall_viiji,dynCall_iij=dynCalls.iij=wasmExports.dynCall_iij,dynCall_iif=dynCalls.iif=wasmExports.dynCall_iif,dynCall_viiiffi=dynCalls.viiiffi=wasmExports.dynCall_viiiffi,dynCall_jiii=dynCalls.jiii=wasmExports.dynCall_jiii,dynCall_jii=dynCalls.jii=wasmExports.dynCall_jii,dynCall_iiiij=dynCalls.iiiij=wasmExports.dynCall_iiiij,dynCall_iiij=dynCalls.iiij=wasmExports.dynCall_iiij,dynCall_jiij=dynCalls.jiij=wasmExports.dynCall_jiij,dynCall_jiiii=dynCalls.jiiii=wasmExports.dynCall_jiiii,dynCall_vij=dynCalls.vij=wasmExports.dynCall_vij,dynCall_jiiiijjj=dynCalls.jiiiijjj=wasmExports.dynCall_jiiiijjj,dynCall_iiiji=dynCalls.iiiji=wasmExports.dynCall_iiiji,dynCall_jiiiiiii=dynCalls.jiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30676"></a>
## FND-30676 — module-001 export dynCall_iiiijii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiijii", "kind": "function", "index": 23025, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "type_index": 84, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116346, "loader_excerpt": "jii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=w", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30677"></a>
## FND-30677 — module-001 export dynCall_iiijj

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiijj", "kind": "function", "index": 23026, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "type_index": 85, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116403, "loader_excerpt": "ynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30678"></a>
## FND-30678 — module-001 export dynCall_viiijii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiijii", "kind": "function", "index": 23027, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "type_index": 112, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116462, "loader_excerpt": ",dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30679"></a>
## FND-30679 — module-001 export dynCall_viijii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viijii", "kind": "function", "index": 23028, "signature": {"parameters": ["i32", "i32", "i32", "i64", "i32", "i32"], "results": []}, "type_index": 55, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116521, "loader_excerpt": "Call_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_ii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30680"></a>
## FND-30680 — module-001 export dynCall_viiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiiii", "kind": "function", "index": 23029, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 27, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116587, "loader_excerpt": "viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30681"></a>
## FND-30681 — module-001 export dynCall_iid

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iid", "kind": "function", "index": 23030, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["i32"]}, "type_index": 86, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116643, "loader_excerpt": "l_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30682"></a>
## FND-30682 — module-001 export dynCall_viid

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viid", "kind": "function", "index": 23031, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": []}, "type_index": 40, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116694, "loader_excerpt": "l_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30683"></a>
## FND-30683 — module-001 export dynCall_fiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_fiiiiiiii", "kind": "function", "index": 23032, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "type_index": 113, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116756, "loader_excerpt": "dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30684"></a>
## FND-30684 — module-001 export dynCall_diiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_diiiii", "kind": "function", "index": 23033, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["f64"]}, "type_index": 114, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116817, "loader_excerpt": "iiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExport", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30685"></a>
## FND-30685 — module-001 export dynCall_viiiid

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiid", "kind": "function", "index": 23034, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": []}, "type_index": 115, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116875, "loader_excerpt": "dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExpor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30686"></a>
## FND-30686 — module-001 export dynCall_viiidi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiidi", "kind": "function", "index": 23035, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32"], "results": []}, "type_index": 87, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116933, "loader_excerpt": "dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExpor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30687"></a>
## FND-30687 — module-001 export dynCall_vifii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vifii", "kind": "function", "index": 23036, "signature": {"parameters": ["i32", "i32", "f32", "i32", "i32"], "results": []}, "type_index": 116, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116989, "loader_excerpt": "d,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30688"></a>
## FND-30688 — module-001 export dynCall_viiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiiiii", "kind": "function", "index": 23037, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 88, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117056, "loader_excerpt": "_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30689"></a>
## FND-30689 — module-001 export dynCall_viiiiiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiiiiiiii", "kind": "function", "index": 23038, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 69, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117135, "loader_excerpt": "iiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30690"></a>
## FND-30690 — module-001 export dynCall_diii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_diii", "kind": "function", "index": 23039, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f64"]}, "type_index": 70, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116817, "loader_excerpt": "iiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExport", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30691"></a>
## FND-30691 — module-001 export dynCall_iiidi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiidi", "kind": "function", "index": 23040, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": ["i32"]}, "type_index": 117, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117251, "loader_excerpt": "iiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30692"></a>
## FND-30692 — module-001 export dynCall_vidi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vidi", "kind": "function", "index": 23041, "signature": {"parameters": ["i32", "i32", "f64", "i32"], "results": []}, "type_index": 71, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 115804, "loader_excerpt": "all_viiiiiii=dynCalls.viiiiiii=wasmExports.dynCall_viiiiiii,dynCall_vidii=dynCalls.vidii=wasmExports.dynCall_vidii,dynCall_dii=dynCalls.dii=wasmExports.dynCall_dii,dynCall_fii=dynCalls.fii=wasmExports.dynCall_fii,dynCall_idi=dynCalls.idi=wasmExports.dynCall_idi,dynCall_di=dynCalls.di=wasmExports.dynCall_di,dynCall_iddi=dynCalls.iddi=wasmExports.dynCall_iddi,dynCall_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.v", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30693"></a>
## FND-30693 — module-001 export dynCall_viiiiiiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiiiiiiiii", "kind": "function", "index": 23042, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 56, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117378, "loader_excerpt": "=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30694"></a>
## FND-30694 — module-001 export dynCall_viiiiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiiiiiii", "kind": "function", "index": 23043, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 57, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117135, "loader_excerpt": "iiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30695"></a>
## FND-30695 — module-001 export dynCall_vif

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vif", "kind": "function", "index": 23044, "signature": {"parameters": ["i32", "i32", "f32"], "results": []}, "type_index": 118, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116989, "loader_excerpt": "d,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30696"></a>
## FND-30696 — module-001 export dynCall_viiiiiij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiij", "kind": "function", "index": 23045, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i64"], "results": []}, "type_index": 119, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117577, "loader_excerpt": "iiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,d", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30697"></a>
## FND-30697 — module-001 export dynCall_viiid

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiid", "kind": "function", "index": 23046, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64"], "results": []}, "type_index": 58, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116933, "loader_excerpt": "dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExpor", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30698"></a>
## FND-30698 — module-001 export dynCall_viiiddi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiddi", "kind": "function", "index": 23047, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "f64", "i32"], "results": []}, "type_index": 187, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117694, "loader_excerpt": ",dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30699"></a>
## FND-30699 — module-001 export dynCall_did

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_did", "kind": "function", "index": 23048, "signature": {"parameters": ["i32", "i32", "f64"], "results": ["f64"]}, "type_index": 59, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117747, "loader_excerpt": "id,dynCall_viiiddi=dynCalls.viiiddi=wasmExports.dynCall_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCall", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30700"></a>
## FND-30700 — module-001 export dynCall_diid

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_diid", "kind": "function", "index": 23049, "signature": {"parameters": ["i32", "i32", "i32", "f64"], "results": ["f64"]}, "type_index": 120, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117798, "loader_excerpt": "Call_viiiddi,dynCall_did=dynCalls.did=wasmExports.dynCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30701"></a>
## FND-30701 — module-001 export dynCall_iddd

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iddd", "kind": "function", "index": 23050, "signature": {"parameters": ["i32", "f64", "f64", "f64"], "results": ["i32"]}, "type_index": 121, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117850, "loader_excerpt": "nCall_did,dynCall_diid=dynCalls.diid=wasmExports.dynCall_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dy", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30702"></a>
## FND-30702 — module-001 export dynCall_diddd

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_diddd", "kind": "function", "index": 23051, "signature": {"parameters": ["i32", "i32", "f64", "f64", "f64"], "results": ["f64"]}, "type_index": 123, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117904, "loader_excerpt": "ll_diid,dynCall_iddd=dynCalls.iddd=wasmExports.dynCall_iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasm", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30703"></a>
## FND-30703 — module-001 export dynCall_viidi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viidi", "kind": "function", "index": 23052, "signature": {"parameters": ["i32", "i32", "i32", "f64", "i32"], "results": []}, "type_index": 60, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 117959, "loader_excerpt": "iddd,dynCall_diddd=dynCalls.diddd=wasmExports.dynCall_diddd,dynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30704"></a>
## FND-30704 — module-001 export dynCall_viiiidii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiidii", "kind": "function", "index": 23053, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "type_index": 122, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118020, "loader_excerpt": "ynCall_viidi=dynCalls.viidi=wasmExports.dynCall_viidi,dynCall_viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30705"></a>
## FND-30705 — module-001 export dynCall_viiidii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiidii", "kind": "function", "index": 23054, "signature": {"parameters": ["i32", "i32", "i32", "i32", "f64", "i32", "i32"], "results": []}, "type_index": 72, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118082, "loader_excerpt": "viiiidii=dynCalls.viiiidii=wasmExports.dynCall_viiiidii,dynCall_viiidii=dynCalls.viiidii=wasmExports.dynCall_viiidii,dynCall_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_vii", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30706"></a>
## FND-30706 — module-001 export dynCall_fiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_fiiii", "kind": "function", "index": 23055, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["f32"]}, "type_index": 124, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116756, "loader_excerpt": "dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30707"></a>
## FND-30707 — module-001 export dynCall_viiiiiiff

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiff", "kind": "function", "index": 23056, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "f32", "f32"], "results": []}, "type_index": 125, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118202, "loader_excerpt": "Call_fiiii=dynCalls.fiiii=wasmExports.dynCall_fiiii,dynCall_viiiiiiff=dynCalls.viiiiiiff=wasmExports.dynCall_viiiiiiff,dynCall_viiij=dynCalls.viiij=wasmExports.dynCall_viiij,dynCall_iiiiiiiii=dynCalls.iiiiiiiii=wasmExports.dynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30708"></a>
## FND-30708 — module-001 export dynCall_viiij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiij", "kind": "function", "index": 23057, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64"], "results": []}, "type_index": 126, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116462, "loader_excerpt": ",dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30709"></a>
## FND-30709 — module-001 export dynCall_iiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiiiiii", "kind": "function", "index": 23058, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 61, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116170, "loader_excerpt": "l_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30710"></a>
## FND-30710 — module-001 export dynCall_viiiji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiji", "kind": "function", "index": 23059, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32"], "results": []}, "type_index": 73, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116462, "loader_excerpt": ",dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmExports.dynCall_viiiid,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dyn", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30711"></a>
## FND-30711 — module-001 export dynCall_viji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viji", "kind": "function", "index": 23060, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": []}, "type_index": 22, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118426, "loader_excerpt": "ynCall_iiiiiiiii,dynCall_viiiji=dynCalls.viiiji=wasmExports.dynCall_viiiji,dynCalls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_u", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30712"></a>
## FND-30712 — module-001 export dynCall_vifi

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_vifi", "kind": "function", "index": 23061, "signature": {"parameters": ["i32", "i32", "f32", "i32"], "results": []}, "type_index": 188, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116989, "loader_excerpt": "d,dynCall_viiidi=dynCalls.viiidi=wasmExports.dynCall_viiidi,dynCall_vifii=dynCalls.vifii=wasmExports.dynCall_vifii,dynCall_viiiiiiiiii=dynCalls.viiiiiiiiii=wasmExports.dynCall_viiiiiiiiii,dynCall_viiiiiiiiiiiii=dynCalls.viiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiii,dynCall_diii=dynCalls.diii=wasmExports.dynCall_diii,dynCall_iiidi=dynCalls.iiidi=wasmExports.dynCall_iiidi,dynCall_vidi=dynCalls.vidi=wasmExports.dynCall_vidi,dynCall_viiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiii,dynCall_viiiiiiiiiiii=dynCalls.viiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiii,dynCall_vif=dynCalls.vif=wasmExports.dynCall_vif,dynCall_viiiiiij=dynCalls.viiiiiij=wasmExports.dynCall_viiiiiij,dynCall_viiid=dynCalls.viiid=wasmExports.dynCall_viiid,dynCall_viiiddi=dynCalls.viiiddi=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30713"></a>
## FND-30713 — module-001 export dynCall_jiji

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_jiji", "kind": "function", "index": 23062, "signature": {"parameters": ["i32", "i32", "i64", "i32"], "results": ["i64"]}, "type_index": 189, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118504, "loader_excerpt": "Calls.viji=wasmExports.dynCall_viji,dynCalls.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30714"></a>
## FND-30714 — module-001 export dynCall_iidiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iidiiiii", "kind": "function", "index": 23063, "signature": {"parameters": ["i32", "i32", "f64", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 190, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118547, "loader_excerpt": "s.vifi=wasmExports.dynCall_vifi,dynCalls.jiji=wasmExports.dynCall_jiji,dynCalls.iidiiiii=wasmExports.dynCall_iidiiiii,dynCall_iiiiiiii=dynCalls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,was", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30715"></a>
## FND-30715 — module-001 export dynCall_iiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiiiii", "kind": "function", "index": 23064, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 17, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 116170, "loader_excerpt": "l_fiii=dynCalls.fiii=wasmExports.dynCall_fiii,dynCall_iiiiiiiiiiii=dynCalls.iiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiii,dynCall_iiijii=dynCalls.iiijii=wasmExports.dynCall_iiijii,dynCall_viij=dynCalls.viij=wasmExports.dynCall_viij,dynCall_iiiijii=dynCalls.iiiijii=wasmExports.dynCall_iiiijii,dynCall_iiijj=dynCalls.iiijj=wasmExports.dynCall_iiijj,dynCall_viiijii=dynCalls.viiijii=wasmExports.dynCall_viiijii,dynCall_viijii=dynCalls.viijii=wasmExports.dynCall_viijii,dynCall_viiiiiiiii=dynCalls.viiiiiiiii=wasmExports.dynCall_viiiiiiiii,dynCall_iid=dynCalls.iid=wasmExports.dynCall_iid,dynCall_viid=dynCalls.viid=wasmExports.dynCall_viid,dynCall_fiiiiiiii=dynCalls.fiiiiiiii=wasmExports.dynCall_fiiiiiiii,dynCall_diiiii=dynCalls.diiiii=wasmExports.dynCall_diiiii,dynCall_viiiid=dynCalls.viiiid=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30716"></a>
## FND-30716 — module-001 export dynCall_iiiiiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiiiiiiiiii", "kind": "function", "index": 23065, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 191, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118685, "loader_excerpt": "Calls.iiiiiiii=wasmExports.dynCall_iiiiiiii,dynCall_iiiiiiiiiiiii=dynCalls.iiiiiiiiiiiii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryVie", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30717"></a>
## FND-30717 — module-001 export dynCall_viiiiiiiiiiiiiii

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_viiiiiiiiiiiiiii", "kind": "function", "index": 23066, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "type_index": 128, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118770, "loader_excerpt": "iii=wasmExports.dynCall_iiiiiiiiiiiii,dynCall_viiiiiiiiiiiiiii=dynCalls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instan", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30718"></a>
## FND-30718 — module-001 export dynCall_iiiiij

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiij", "kind": "function", "index": 23067, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "type_index": 89, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118838, "loader_excerpt": "lls.viiiiiiiiiiiiiii=wasmExports.dynCall_viiiiiiiiiiiiiii,dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise(", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30719"></a>
## FND-30719 — module-001 export dynCall_iiiiid

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
{"module_id": "module-001", "direction": "export", "name": "dynCall_iiiiid", "kind": "function", "index": 23068, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": ["i32"]}, "type_index": 127, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 118896, "loader_excerpt": "dynCall_iiiiij=dynCalls.iiiiij=wasmExports.dynCall_iiiiij,dynCall_iiiiid=dynCalls.iiiiid=wasmExports.dynCall_iiiiid,dynCall_iiiiijj=dynCalls.iiiiijj=wasmExports.dynCall_iiiiijj,dynCalls.iiiiiijj=wasmExports.dynCall_iiiiiijj,_asyncify_start_unwind=wasmExports.asyncify_start_unwind,_asyncify_stop_unwind=wasmExports.asyncify_stop_unwind,_asyncify_start_rewind=wasmExports.asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInst", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
