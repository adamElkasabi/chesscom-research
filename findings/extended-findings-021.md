# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-31200"></a>
## FND-31200 — module-005 export B

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "B", "kind": "function", "index": 687, "signature": {"parameters": ["i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 14280, "loader_excerpt": "tackSave=c.asm.A).apply(null,arguments)},eb=c.stackRestore=function(){return(eb=c.stackRestore=c.asm.B).apply(null,arguments)},K=c.stackAlloc=function(){return(K=c.stackAlloc=c.asm.C).apply(null,arguments)},dynCall_vi=c.dynCall_vi=function(){return(dynCall_vi=c.dynCall_vi=c.asm.D).apply(null,\narguments)},dynCall_v=c.dynCall_v=function(){return(dynCall_v=c.dynCall_v=c.asm.E).apply(null,arguments)};c._asyncify_start_unwind=function(){return(c._asyncify_start_unwind=c.asm.F).apply(null,arguments)};c._asyncify_stop_unwind=function(){return(c._asyncify_stop_unwind=c.asm.G).apply(null,arguments)};c._asyncify_start_rewind=function(){return(c._asyncify_start_rewind=c.asm.H).apply(null,arguments)};c._asyncify_stop_rewind=function(){return(c._asyncify_stop_rewind=c.asm.I).apply(null,arguments)};\nc.c", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31201"></a>
## FND-31201 — module-005 export C

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "C", "kind": "function", "index": 679, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 14360, "loader_excerpt": "c.stackRestore=c.asm.B).apply(null,arguments)},K=c.stackAlloc=function(){return(K=c.stackAlloc=c.asm.C).apply(null,arguments)},dynCall_vi=c.dynCall_vi=function(){return(dynCall_vi=c.dynCall_vi=c.asm.D).apply(null,\narguments)},dynCall_v=c.dynCall_v=function(){return(dynCall_v=c.dynCall_v=c.asm.E).apply(null,arguments)};c._asyncify_start_unwind=function(){return(c._asyncify_start_unwind=c.asm.F).apply(null,arguments)};c._asyncify_stop_unwind=function(){return(c._asyncify_stop_unwind=c.asm.G).apply(null,arguments)};c._asyncify_start_rewind=function(){return(c._asyncify_start_rewind=c.asm.H).apply(null,arguments)};c._asyncify_stop_rewind=function(){return(c._asyncify_stop_rewind=c.asm.I).apply(null,arguments)};\nc.ccall=function(a,b,e,f,h){function g(t){--D;0!==u&&eb(u);return\"string\"===b?ma(t)", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31202"></a>
## FND-31202 — module-005 export D

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "D", "kind": "function", "index": 458, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 3, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 5805, "loader_excerpt": "on(){Ha(a)},b)}var Ka={};function La(){if(!Ma){var a={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:w||\"./this.program\"},b;for(b in Ka)void 0===Ka[b]?delete a[b]:a[b]=Ka[b];var e=[];for(b in a)e.push(b+\"=\"+a[b]);Ma=e}return Ma}var Ma;function R(a){return 0===a%4&&(0!==a%100||0===a%400)}\nfunction Na(a,b){for(var e=0,f=0;f<=b;e+=a[f++]);return e}var S=[31,29,31,30,31,30,31,31,30,31,30,31],T=[31,28,31,30,31,30,31,31,30,31,30,31];function U(a,b){for(a=new Date(a.getTime());0<b;){var e=a.getMonth(),f=(R(a.getFullYear())?S:T)[e];if(b>f-a.getDate())b-=f-a.getDate()+1,a.setDate(1),11>e?a.setMonth(e+1):(a.setMonth(0),a.setFullYear(a.getFullYear()+1));else{a.set", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31203"></a>
## FND-31203 — module-005 export E

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "E", "kind": "function", "index": 457, "signature": {"parameters": ["i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 5781, "loader_excerpt": "return setTimeout(function(){Ha(a)},b)}var Ka={};function La(){if(!Ma){var a={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:w||\"./this.program\"},b;for(b in Ka)void 0===Ka[b]?delete a[b]:a[b]=Ka[b];var e=[];for(b in a)e.push(b+\"=\"+a[b]);Ma=e}return Ma}var Ma;function R(a){return 0===a%4&&(0!==a%100||0===a%400)}\nfunction Na(a,b){for(var e=0,f=0;f<=b;e+=a[f++]);return e}var S=[31,29,31,30,31,30,31,31,30,31,30,31],T=[31,28,31,30,31,30,31,31,30,31,30,31];function U(a,b){for(a=new Date(a.getTime());0<b;){var e=a.getMonth(),f=(R(a.getFullYear())?S:T)[e];if(b>f-a.getDate())b-=f-a.getDate()+1,a.setDate(1),11>e?a.setMonth(e+1):(a.setMonth(0),a.setFullYear(a.getF", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31204"></a>
## FND-31204 — module-005 export F

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "F", "kind": "function", "index": 455, "signature": {"parameters": ["i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 14653, "loader_excerpt": ".E).apply(null,arguments)};c._asyncify_start_unwind=function(){return(c._asyncify_start_unwind=c.asm.F).apply(null,arguments)};c._asyncify_stop_unwind=function(){return(c._asyncify_stop_unwind=c.asm.G).apply(null,arguments)};c._asyncify_start_rewind=function(){return(c._asyncify_start_rewind=c.asm.H).apply(null,arguments)};c._asyncify_stop_rewind=function(){return(c._asyncify_stop_rewind=c.asm.I).apply(null,arguments)};\nc.ccall=function(a,b,e,f,h){function g(t){--D;0!==u&&eb(u);return\"string\"===b?ma(t):\"boolean\"===b?!!t:t}var k={string:function(t){var y=0;if(null!==t&&void 0!==t&&0!==t){var d=(t.length<<2)+1;y=K(d);na(t,J,y,d)}return y},array:function(t){var y=K(t.length);L.set(t,y);return y}};a=c[\"_\"+a];var r=[],u=0;if(f)for(var p=0;p<f.length;p++){var q=k[e[p]];q?(0===u&&(u=db()),r[p]=q(", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31205"></a>
## FND-31205 — module-005 export G

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "G", "kind": "function", "index": 454, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 5836, "loader_excerpt": "on La(){if(!Ma){var a={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:w||\"./this.program\"},b;for(b in Ka)void 0===Ka[b]?delete a[b]:a[b]=Ka[b];var e=[];for(b in a)e.push(b+\"=\"+a[b]);Ma=e}return Ma}var Ma;function R(a){return 0===a%4&&(0!==a%100||0===a%400)}\nfunction Na(a,b){for(var e=0,f=0;f<=b;e+=a[f++]);return e}var S=[31,29,31,30,31,30,31,31,30,31,30,31],T=[31,28,31,30,31,30,31,31,30,31,30,31];function U(a,b){for(a=new Date(a.getTime());0<b;){var e=a.getMonth(),f=(R(a.getFullYear())?S:T)[e];if(b>f-a.getDate())b-=f-a.getDate()+1,a.setDate(1),11>e?a.setMonth(e+1):(a.setMonth(0),a.setFullYear(a.getFullYear()+1));else{a.setDate(a.getDate()+b);break}}retu", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31206"></a>
## FND-31206 — module-005 export H

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "H", "kind": "function", "index": 453, "signature": {"parameters": ["i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 5797, "loader_excerpt": "t(function(){Ha(a)},b)}var Ka={};function La(){if(!Ma){var a={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:w||\"./this.program\"},b;for(b in Ka)void 0===Ka[b]?delete a[b]:a[b]=Ka[b];var e=[];for(b in a)e.push(b+\"=\"+a[b]);Ma=e}return Ma}var Ma;function R(a){return 0===a%4&&(0!==a%100||0===a%400)}\nfunction Na(a,b){for(var e=0,f=0;f<=b;e+=a[f++]);return e}var S=[31,29,31,30,31,30,31,31,30,31,30,31],T=[31,28,31,30,31,30,31,31,30,31,30,31];function U(a,b){for(a=new Date(a.getTime());0<b;){var e=a.getMonth(),f=(R(a.getFullYear())?S:T)[e];if(b>f-a.getDate())b-=f-a.getDate()+1,a.setDate(1),11>e?a.setMonth(e+1):(a.setMonth(0),a.setFullYear(a.getFullYear()+1));el", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31207"></a>
## FND-31207 — module-005 export I

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "export", "name": "I", "kind": "function", "index": 451, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 7656, "loader_excerpt": "?\nma(p):\"\"};e=ma(e);p={\"%c\":\"%a %b %d %H:%M:%S %Y\",\"%D\":\"%m/%d/%y\",\"%F\":\"%Y-%m-%d\",\"%h\":\"%b\",\"%r\":\"%I:%M:%S %p\",\"%R\":\"%H:%M\",\"%T\":\"%H:%M:%S\",\"%x\":\"%m/%d/%y\",\"%X\":\"%H:%M:%S\",\"%Ec\":\"%c\",\"%EC\":\"%C\",\"%Ex\":\"%m/%d/%y\",\"%EX\":\"%H:%M:%S\",\"%Ey\":\"%y\",\"%EY\":\"%Y\",\"%Od\":\"%d\",\"%Oe\":\"%e\",\"%OH\":\"%H\",\"%OI\":\"%I\",\"%Om\":\"%m\",\"%OM\":\"%M\",\"%OS\":\"%S\",\"%Ou\":\"%u\",\"%OU\":\"%U\",\"%OV\":\"%V\",\"%Ow\":\"%w\",\"%OW\":\"%W\",\"%Oy\":\"%y\"};for(var q in p)e=e.replace(new RegExp(q,\"g\"),p[q]);var t=\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\".split(\" \"),\ny=\"January February March April May June July August September October November December\".split(\" \");p={\"%a\":function(d){return t[d.O].substring(0,3)},\"%A\":function(d){return t[d.O]},\"%b\":function(d){return y[d.K].substring(0,3)},\"%B\":function(d){return y[d.K]},\"%C\":function(d", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```
