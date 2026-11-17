# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-31140"></a>
## FND-31140 — module-004 import a.k

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "k", "kind": "function", "type_index": 17, "function_index": 10, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 14650, "loader_excerpt": "else{if(1!==e&&4!==e)return g[He()>>2]=28,-1;e=me()}return g[n>>2]=e/1e3|0,g[n+4>>2]=e%1e3*1e6|0,0},k:function(){return!l},o:function(e,n,t){C.copyWithin(e,n,n+t)},d:function(e){var n=C.length;if(!(2147483648<(e>>>=0)))for(var t=1;t<=4;t*=2){var r=n*(1+.2/t),r=Math.min(r,e+100663296);0<(r=Math.max(e,r))%65536&&(r+=65536-r%65536);e:{try{z.grow(Math.min(2147483648,r)-K.byteLength+65535>>>16),ee();var o=1;break e}catch(e){}o=void 0}if(o)return!0}return!1},b:function(t){Ue(function(e){var n;n=e,setTimeout(function(){j(n)},t)})},j:function(e,t,n,r,o){function a(e,n){he(e,n.response,function(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)},function(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)})}function i(e){j(function(){y?P.apply(null,[y,e]):o&&o(e)},_)}function u(e){j(function(){d?P.app", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31141"></a>
## FND-31141 — module-004 import a.l

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "l", "kind": "function", "type_index": 17, "function_index": 11, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 2481, "loader_excerpt": "function(e,n){return q=q||require(\"fs\"),e=(W=W||require(\"path\")).normalize(e),q.readFileSync(e,n?null:\"utf8\")},c=function(e){return(e=(e=Y(e,!0)).buffer?e:new Uint8Array(e)).buffer||_(\"Assertion failed: undefined\"),e},1<process.argv.length&&(u=process.argv[1].replace(/\\\\/g,\"/\")),N=process.argv.slice(2),process.on(\"uncaughtException\",function(e){if(!(e instanceof qe))throw e}),process.on(\"unhandledRejection\",_),s=function(e,n){if(V||0<ie)throw process.exitCode=e,n;process.exit(e)},i.inspect=function(){return\"[Emscripten Module object]\"}):(B||l)&&(l?p=self.location.href:\"undefined\"!=typeof document&&document.currentScript&&(p=document.currentScript.src),p=0!==(p=Xe?Xe:p).indexOf(\"blob:\")?p.substr(0,p.lastIndexOf(\"/\")+1):\"\",Y=function(e){var n=new XMLHttpRequest;return n.open(\"GET\",e,!1),n.se", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31142"></a>
## FND-31142 — module-004 import a.m

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "m", "kind": "function", "type_index": 11, "function_index": 12, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 17585, "loader_excerpt": " c=C[i+s],f=pe[e];0===c||10===c?((1===e?X:d)(Q(f,0)),f.length=0):f.push(c)}o+=u}return g[r>>2]=o,0},m:function(){i.pauseQueue()},t:Ee,e:function(){i.unpauseQueue()}},Pe=(!function(){function n(e){e=Le(e=e.exports),i.asm=e,z=i.asm.w,ee(),re.unshift(i.asm.x),ce()}function t(e){n(e.instance)}function r(e){return(f||!B&&!l||\"function\"!=typeof fetch?Promise.resolve().then(le):fetch(h,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+h+\"'\"}).catch(le)).then(function(e){return WebAssembly.instantiate(e,o)}).then(function(e){return e}).then(e,function(e){d(\"failed to asynchronously prepare wasm: \"+e),_(e)})}var o={a:ke};if(se(),i.instantiateWasm)try{var e=i.instantiateWasm(o,n);return Le(e)}catch(e){return d(\"Module.instantiate", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31143"></a>
## FND-31143 — module-004 import a.n

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "n", "kind": "function", "type_index": 6, "function_index": 13, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 701, "loader_excerpt": "on(e,n){D=e,I=n}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var t,r={open:function(e,n){t=n},send:function(){require(\"fs\").readFile(t,function(e,n){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=n,r.onreadystatechange(),r.onload())})}};return r}),\"undefined\"!=typeof global&&\"[object process]\"===Object.prototype.toString.call(global.process)&&\"undefined\"!=typeof fetch&&(fetch=null),i.postCustomMessage=function(e){if(\"undefined\"!=typeof PThread)for(var n of PThread.ba)n.postMessage({cmd:\"custom\",userData:e})},i.queue=(t=[],{get:async function(){return 0<t.length?t.shift():await new Promise(function(e){return n=e})},put:function(e){n?(n(e),n=null):t.push(e)}}),i.onCustomMessage=function(e){A?H.push(e):i.queue.put(e)};var A,r,", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31144"></a>
## FND-31144 — module-004 import a.o

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "o", "kind": "function", "type_index": 3, "function_index": 14, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 14673, "loader_excerpt": "turn g[He()>>2]=28,-1;e=me()}return g[n>>2]=e/1e3|0,g[n+4>>2]=e%1e3*1e6|0,0},k:function(){return!l},o:function(e,n,t){C.copyWithin(e,n,n+t)},d:function(e){var n=C.length;if(!(2147483648<(e>>>=0)))for(var t=1;t<=4;t*=2){var r=n*(1+.2/t),r=Math.min(r,e+100663296);0<(r=Math.max(e,r))%65536&&(r+=65536-r%65536);e:{try{z.grow(Math.min(2147483648,r)-K.byteLength+65535>>>16),ee();var o=1;break e}catch(e){}o=void 0}if(o)return!0}return!1},b:function(t){Ue(function(e){var n;n=e,setTimeout(function(){j(n)},t)})},j:function(e,t,n,r,o){function a(e,n){he(e,n.response,function(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)},function(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)})}function i(e){j(function(){y?P.apply(null,[y,e]):o&&o(e)},_)}function u(e){j(function(){d?P.apply(null,[d,e]):n&&n(e)}", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31145"></a>
## FND-31145 — module-004 import a.p

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "p", "kind": "function", "type_index": 3, "function_index": 15, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 14426, "loader_excerpt": "of ENVIRONMENT_IS_FETCH_WORKER&&ENVIRONMENT_IS_FETCH_WORKER||se();var je,ke={f:function(){return 0},p:function(){return 0},q:function(){},i:function(e){delete ye[e-1]},a:function(){_()},h:function(e,n){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return g[He()>>2]=28,-1;e=me()}return g[n>>2]=e/1e3|0,g[n+4>>2]=e%1e3*1e6|0,0},k:function(){return!l},o:function(e,n,t){C.copyWithin(e,n,n+t)},d:function(e){var n=C.length;if(!(2147483648<(e>>>=0)))for(var t=1;t<=4;t*=2){var r=n*(1+.2/t),r=Math.min(r,e+100663296);0<(r=Math.max(e,r))%65536&&(r+=65536-r%65536);e:{try{z.grow(Math.min(2147483648,r)-K.byteLength+65535>>>16),ee();var o=1;break e}catch(e){}o=void 0}if(o)return!0}return!1},b:function(t){Ue(function(e){var n;n=e,setTimeout(function(){j(n)},t)})},j:function(e,t,n,r,o){function a(e,n){he(e,n.r", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31146"></a>
## FND-31146 — module-004 import a.q

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "q", "kind": "function", "type_index": 3, "function_index": 16, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 14449, "loader_excerpt": "_WORKER&&ENVIRONMENT_IS_FETCH_WORKER||se();var je,ke={f:function(){return 0},p:function(){return 0},q:function(){},i:function(e){delete ye[e-1]},a:function(){_()},h:function(e,n){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return g[He()>>2]=28,-1;e=me()}return g[n>>2]=e/1e3|0,g[n+4>>2]=e%1e3*1e6|0,0},k:function(){return!l},o:function(e,n,t){C.copyWithin(e,n,n+t)},d:function(e){var n=C.length;if(!(2147483648<(e>>>=0)))for(var t=1;t<=4;t*=2){var r=n*(1+.2/t),r=Math.min(r,e+100663296);0<(r=Math.max(e,r))%65536&&(r+=65536-r%65536);e:{try{z.grow(Math.min(2147483648,r)-K.byteLength+65535>>>16),ee();var o=1;break e}catch(e){}o=void 0}if(o)return!0}return!1},b:function(t){Ue(function(e){var n;n=e,setTimeout(function(){j(n)},t)})},j:function(e,t,n,r,o){function a(e,n){he(e,n.response,function(e){j(f", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31147"></a>
## FND-31147 — module-004 import a.r

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "r", "kind": "function", "type_index": 7, "function_index": 17, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 17384, "loader_excerpt": "unction(){return 0},s:function(e,n,t,r){return e=de.aa(e),n=de.$(e,n,t),g[r>>2]=n,0},n:function(){},r:function(e,n,t,r){for(var o=0,a=0;a<t;a++){for(var i=g[n+8*a>>2],u=g[n+(8*a+4)>>2],s=0;s<u;s++){var c=C[i+s],f=pe[e];0===c||10===c?((1===e?X:d)(Q(f,0)),f.length=0):f.push(c)}o+=u}return g[r>>2]=o,0},m:function(){i.pauseQueue()},t:Ee,e:function(){i.unpauseQueue()}},Pe=(!function(){function n(e){e=Le(e=e.exports),i.asm=e,z=i.asm.w,ee(),re.unshift(i.asm.x),ce()}function t(e){n(e.instance)}function r(e){return(f||!B&&!l||\"function\"!=typeof fetch?Promise.resolve().then(le):fetch(h,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+h+\"'\"}).catch(le)).then(function(e){return WebAssembly.instantiate(e,o)}).then(function(e){retur", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31148"></a>
## FND-31148 — module-004 import a.s

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "s", "kind": "function", "type_index": 7, "function_index": 18, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 55, "loader_excerpt": "/*!\n * Stockfish.js 16 (c) 2023, Chess.com, LLC\n * https://github.com/nmrugg/stockfish.js\n * License: GPLv3\n *\n * Based on stockfish.wasm (c)\n * Niklas Fiekas <niklas.fiekas@backscattering.de>\n * Hiroshi Ogawa <hi.ogawa.zz@gmail.com>\n * https://github.com/niklasf/stockfish.wasm\n * https://github.com/hi-ogawa/Stockfish\n *\n * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.\n * https://github.com/official-stockfish/Stockfish\n */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(void 0!==e?e:{})).ready=new Promise(function(e,n){D=e,I=n}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var t,r={open:function(e,n){t=n},send:function(){require(\"fs\").rea", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31149"></a>
## FND-31149 — module-004 import a.t

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "t", "kind": "function", "type_index": 6, "function_index": 19, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 1199, "loader_excerpt": "!=typeof PThread)for(var n of PThread.ba)n.postMessage({cmd:\"custom\",userData:e})},i.queue=(t=[],{get:async function(){return 0<t.length?t.shift():await new Promise(function(e){return n=e})},put:function(e){n?(n(e),n=null):t.push(e)}}),i.onCustomMessage=function(e){A?H.push(e):i.queue.put(e)};var A,r,H=[],o=(i.pauseQueue=function(){A=!0},i.unpauseQueue=function(){var e=H;A=!(H=[]),e.forEach(function(e){i.queue.put(e)})},i.postMessage=i.postCustomMessage,[]),a=(i.addMessageListener=function(e){o.push(e)},i.removeMessageListener=function(e){0<=(e=o.indexOf(e))&&o.splice(e,1)},i.print=i.printErr=function(e){if(0===o.length)return console.log(e);for(var n of o)n(e)},i.terminate=function(){\"undefined\"!=typeof PThread&&PThread.da()},i.__IS_SINGLE_THREADED__=!0,i._origOnCustomMessage=i.onCustomMe", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31150"></a>
## FND-31150 — module-004 import a.u

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "u", "kind": "function", "type_index": 2, "function_index": 20, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 16229, "loader_excerpt": "\"IndexedDB not available!\")}else if(w){if(v)return 0;ge(e,h?a:c,u,s,i)}else{var F=e;var D=c;var I=v?u:h?function(e){ge(e,a,u,s,i)}:function(e){ge(e,c,u,s,i)};l=L;if(l){g=O[F+112+64>>2];g=R(g=g||O[F+8>>2]);try{var A=l.transaction([\"FILES\"],\"readonly\").objectStore(\"FILES\").get(g);A.onsuccess=function(e){var n,t;e.target.result?(n=(e=e.target.result).byteLength||e.length,t=k(n),C.set(new Uint8Array(e),t),O[F+12>>2]=t,U(F+16,n),U(F+24,0),U(F+32,n),x[F+40>>1]=4,x[F+42>>1]=200,T(\"OK\",C,F+44,64),D(F,0,e)):(x[F+40>>1]=4,x[F+42>>1]=404,T(\"Not Found\",C,F+44,64),I(F,0,\"no data\"))},A.onerror=function(e){x[F+40>>1]=4,x[F+42>>1]=404,T(\"Not Found\",C,F+44,64),I(F,0,e)}}catch(e){I(F,0,e)}}else I(F,0,\"IndexedDB not available!\")}return e},l:function(){return n=async()=>{var e=await i.queue.get(),n=$(e)+1,t=k", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31151"></a>
## FND-31151 — module-004 import a.v

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "import", "module": "a", "name": "v", "kind": "function", "type_index": 2, "function_index": 21, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 17152, "loader_excerpt": "t=o+a;for(n=g[r+4*n>>2]=t,t=0;t<e.length;++t)y[n++>>0]=e.charCodeAt(t);y[n>>0]=0,a+=e.length+1}),0},v:function(e,n){var t=_e(),r=(g[e>>2]=t.length,0);return t.forEach(function(e){r+=e.length+1}),g[n>>2]=r,0},c:function(e){Be(e)},g:function(){return 0},s:function(e,n,t,r){return e=de.aa(e),n=de.$(e,n,t),g[r>>2]=n,0},n:function(){},r:function(e,n,t,r){for(var o=0,a=0;a<t;a++){for(var i=g[n+8*a>>2],u=g[n+(8*a+4)>>2],s=0;s<u;s++){var c=C[i+s],f=pe[e];0===c||10===c?((1===e?X:d)(Q(f,0)),f.length=0):f.push(c)}o+=u}return g[r>>2]=o,0},m:function(){i.pauseQueue()},t:Ee,e:function(){i.unpauseQueue()}},Pe=(!function(){function n(e){e=Le(e=e.exports),i.asm=e,z=i.asm.w,ee(),re.unshift(i.asm.x),ce()}function t(e){n(e.instance)}function r(e){return(f||!B&&!l||\"function\"!=typeof fetch?Promise.resolve().th", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31152"></a>
## FND-31152 — module-004 export w

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "w", "kind": "memory", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 132, "loader_excerpt": " Chess.com, LLC\n * https://github.com/nmrugg/stockfish.js\n * License: GPLv3\n *\n * Based on stockfish.wasm (c)\n * Niklas Fiekas <niklas.fiekas@backscattering.de>\n * Hiroshi Ogawa <hi.ogawa.zz@gmail.com>\n * https://github.com/niklasf/stockfish.wasm\n * https://github.com/hi-ogawa/Stockfish\n *\n * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.\n * https://github.com/official-stockfish/Stockfish\n */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(void 0!==e?e:{})).ready=new Promise(function(e,n){D=e,I=n}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var t,r={open:function(e,n){t=n},send:function(){require(\"fs\").readFile(t,function(e,n){r.readyState=4,e?(console.error(e),r.status=404,r.onerr", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31153"></a>
## FND-31153 — module-004 export x

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "x", "kind": "function", "index": 289, "signature": {"parameters": [], "results": []}, "type_index": 11, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 17738, "loader_excerpt": "useQueue()}},Pe=(!function(){function n(e){e=Le(e=e.exports),i.asm=e,z=i.asm.w,ee(),re.unshift(i.asm.x),ce()}function t(e){n(e.instance)}function r(e){return(f||!B&&!l||\"function\"!=typeof fetch?Promise.resolve().then(le):fetch(h,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+h+\"'\"}).catch(le)).then(function(e){return WebAssembly.instantiate(e,o)}).then(function(e){return e}).then(e,function(e){d(\"failed to asynchronously prepare wasm: \"+e),_(e)})}var o={a:ke};if(se(),i.instantiateWasm)try{var e=i.instantiateWasm(o,n);return Le(e)}catch(e){return d(\"Module.instantiateWasm callback failed with error: \"+e)}(f||\"function\"!=typeof WebAssembly.instantiateStreaming||fe()||\"function\"!=typeof fetch?r(t):fetch(h,{credentials:\"", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31154"></a>
## FND-31154 — module-004 export y

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "y", "kind": "function", "index": 730, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 18780, "loader_excerpt": "{return(i.___wasm_call_ctors=i.asm.x).apply(null,arguments)},i._main=function(){return(i._main=i.asm.y).apply(null,arguments)},i._free=function(){return(Pe=i._free=i.asm.z).apply(null,arguments)}),k=(i._stop=function(){return(i._stop=i.asm.A).apply(null,arguments)},i._ponderhit=function(){return(i._ponderhit=i.asm.B).apply(null,arguments)},i._malloc=function(){return(k=i._malloc=i.asm.C).apply(null,arguments)}),He=i.___errno_location=function(){return(He=i.___errno_location=i.asm.D).apply(null,arguments)},Ne=i.stackAlloc=function(){return(Ne=i.stackAlloc=i.asm.E).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.G).apply(null,arguments)},Ye=i.dynCall_v=function(){return(Ye=i.dynCall_v=i.asm.H).apply(null,arguments)};function qe(e){this.name=\"ExitStatus\",this.mess", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31155"></a>
## FND-31155 — module-004 export z

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "z", "kind": "function", "index": 22, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 219, "loader_excerpt": " on stockfish.wasm (c)\n * Niklas Fiekas <niklas.fiekas@backscattering.de>\n * Hiroshi Ogawa <hi.ogawa.zz@gmail.com>\n * https://github.com/niklasf/stockfish.wasm\n * https://github.com/hi-ogawa/Stockfish\n *\n * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.\n * https://github.com/official-stockfish/Stockfish\n */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(void 0!==e?e:{})).ready=new Promise(function(e,n){D=e,I=n}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var t,r={open:function(e,n){t=n},send:function(){require(\"fs\").readFile(t,function(e,n){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=n,r.onreadystatechange(),r.onload())})}};return r}),\"un", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31156"></a>
## FND-31156 — module-004 export A

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "A", "kind": "function", "index": 710, "signature": {"parameters": [], "results": []}, "type_index": 11, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 18919, "loader_excerpt": "tion(){return(Pe=i._free=i.asm.z).apply(null,arguments)}),k=(i._stop=function(){return(i._stop=i.asm.A).apply(null,arguments)},i._ponderhit=function(){return(i._ponderhit=i.asm.B).apply(null,arguments)},i._malloc=function(){return(k=i._malloc=i.asm.C).apply(null,arguments)}),He=i.___errno_location=function(){return(He=i.___errno_location=i.asm.D).apply(null,arguments)},Ne=i.stackAlloc=function(){return(Ne=i.stackAlloc=i.asm.E).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.G).apply(null,arguments)},Ye=i.dynCall_v=function(){return(Ye=i.dynCall_v=i.asm.H).apply(null,arguments)};function qe(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",this.status=e}function We(a){function e(){if(!je&&(je=!0,i.calledRun=!0,!m)){if(b(re),b(oe),D(i),", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31157"></a>
## FND-31157 — module-004 export B

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "B", "kind": "function", "index": 709, "signature": {"parameters": [], "results": []}, "type_index": 11, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 18995, "loader_excerpt": "n(){return(i._stop=i.asm.A).apply(null,arguments)},i._ponderhit=function(){return(i._ponderhit=i.asm.B).apply(null,arguments)},i._malloc=function(){return(k=i._malloc=i.asm.C).apply(null,arguments)}),He=i.___errno_location=function(){return(He=i.___errno_location=i.asm.D).apply(null,arguments)},Ne=i.stackAlloc=function(){return(Ne=i.stackAlloc=i.asm.E).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.G).apply(null,arguments)},Ye=i.dynCall_v=function(){return(Ye=i.dynCall_v=i.asm.H).apply(null,arguments)};function qe(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",this.status=e}function We(a){function e(){if(!je&&(je=!0,i.calledRun=!0,!m)){if(b(re),b(oe),D(i),i.onRuntimeInitialized&&i.onRuntimeInitialized(),Ge){var n=a,e=i._main,t=(n=", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31158"></a>
## FND-31158 — module-004 export C

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "C", "kind": "function", "index": 44, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 19067, "loader_excerpt": "(){return(i._ponderhit=i.asm.B).apply(null,arguments)},i._malloc=function(){return(k=i._malloc=i.asm.C).apply(null,arguments)}),He=i.___errno_location=function(){return(He=i.___errno_location=i.asm.D).apply(null,arguments)},Ne=i.stackAlloc=function(){return(Ne=i.stackAlloc=i.asm.E).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.G).apply(null,arguments)},Ye=i.dynCall_v=function(){return(Ye=i.dynCall_v=i.asm.H).apply(null,arguments)};function qe(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",this.status=e}function We(a){function e(){if(!je&&(je=!0,i.calledRun=!0,!m)){if(b(re),b(oe),D(i),i.onRuntimeInitialized&&i.onRuntimeInitialized(),Ge){var n=a,e=i._main,t=(n=n||[]).length+1,r=Ne(4*(t+1));g[r>>2]=Z(u);for(var o=1;o<t;o++)g[(r>>2)+", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31159"></a>
## FND-31159 — module-004 export D

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "D", "kind": "function", "index": 701, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 17, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 8524, "loader_excerpt": "ilable!\")}var ve,we={};function _e(){if(!ve){var e,n={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:u||\"./this.program\"};for(e in we)void 0===we[e]?delete n[e]:n[e]=we[e];var t=[];for(e in n)t.push(e+\"=\"+n[e]);ve=t}return ve}function S(e){return 0==e%4&&(0!=e%100||0==e%400)}function be(e,n){for(var t=0,r=0;r<=n;t+=e[r++]);return t}var M=[31,29,31,30,31,30,31,31,30,31,30,31],Se=[31,28,31,30,31,30,31,31,30,31,30,31];function Me(e,n){for(e=new Date(e.getTime());0<n;){var t=e.getMonth(),r=(S(e.getFullYear())?M:Se)[t];if(!(n>r-e.getDate())){e.setDate(e.getDate()+n);break}n-=r-e.getDate()+1,e.setDate(1),t<11?e.setMonth(t+1):(e.setMonth(0),e.setFullYear(e.get", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31160"></a>
## FND-31160 — module-004 export E

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "E", "kind": "function", "index": 708, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 8500, "loader_excerpt": "r(n,0,\"IndexedDB not available!\")}var ve,we={};function _e(){if(!ve){var e,n={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:u||\"./this.program\"};for(e in we)void 0===we[e]?delete n[e]:n[e]=we[e];var t=[];for(e in n)t.push(e+\"=\"+n[e]);ve=t}return ve}function S(e){return 0==e%4&&(0!=e%100||0==e%400)}function be(e,n){for(var t=0,r=0;r<=n;t+=e[r++]);return t}var M=[31,29,31,30,31,30,31,31,30,31,30,31],Se=[31,28,31,30,31,30,31,31,30,31,30,31];function Me(e,n){for(e=new Date(e.getTime());0<n;){var t=e.getMonth(),r=(S(e.getFullYear())?M:Se)[t];if(!(n>r-e.getDate())){e.setDate(e.getDate()+n);break}n-=r-e.getDate()+1,e.setDate(1),t<11?e.setMonth(t+1):(e.setMont", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31161"></a>
## FND-31161 — module-004 export F

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "F", "kind": "table", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 10195, "loader_excerpt": "Year()-1}var c,f=g[r+40>>2];for(c in r={X:g[r>>2],W:g[r+4>>2],O:g[r+8>>2],N:g[r+12>>2],M:g[r+16>>2],F:g[r+20>>2],P:g[r+24>>2],R:g[r+28>>2],ea:g[r+32>>2],V:g[r+36>>2],Y:f?R(f):\"\"},t=R(t),f={\"%c\":\"%a %b %d %H:%M:%S %Y\",\"%D\":\"%m/%d/%y\",\"%F\":\"%Y-%m-%d\",\"%h\":\"%b\",\"%r\":\"%I:%M:%S %p\",\"%R\":\"%H:%M\",\"%T\":\"%H:%M:%S\",\"%x\":\"%m/%d/%y\",\"%X\":\"%H:%M:%S\",\"%Ec\":\"%c\",\"%EC\":\"%C\",\"%Ex\":\"%m/%d/%y\",\"%EX\":\"%H:%M:%S\",\"%Ey\":\"%y\",\"%EY\":\"%Y\",\"%Od\":\"%d\",\"%Oe\":\"%e\",\"%OH\":\"%H\",\"%OI\":\"%I\",\"%Om\":\"%m\",\"%OM\":\"%M\",\"%OS\":\"%S\",\"%Ou\":\"%u\",\"%OU\":\"%U\",\"%OV\":\"%V\",\"%Ow\":\"%w\",\"%OW\":\"%W\",\"%Oy\":\"%y\"})t=t.replace(new RegExp(c,\"g\"),f[c]);var l,p,d=\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\".split(\" \"),m=\"January February March April May June July August September October November December\".split(\" \");for(c in f={\"%a\":funct", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31162"></a>
## FND-31162 — module-004 export G

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "G", "kind": "function", "index": 473, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 8555, "loader_excerpt": " _e(){if(!ve){var e,n={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:u||\"./this.program\"};for(e in we)void 0===we[e]?delete n[e]:n[e]=we[e];var t=[];for(e in n)t.push(e+\"=\"+n[e]);ve=t}return ve}function S(e){return 0==e%4&&(0!=e%100||0==e%400)}function be(e,n){for(var t=0,r=0;r<=n;t+=e[r++]);return t}var M=[31,29,31,30,31,30,31,31,30,31,30,31],Se=[31,28,31,30,31,30,31,31,30,31,30,31];function Me(e,n){for(e=new Date(e.getTime());0<n;){var t=e.getMonth(),r=(S(e.getFullYear())?M:Se)[t];if(!(n>r-e.getDate())){e.setDate(e.getDate()+n);break}n-=r-e.getDate()+1,e.setDate(1),t<11?e.setMonth(t+1):(e.setMonth(0),e.setFullYear(e.getFullYear()+1))}return e}functio", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31163"></a>
## FND-31163 — module-004 export H

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "H", "kind": "function", "index": 470, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 8516, "loader_excerpt": " not available!\")}var ve,we={};function _e(){if(!ve){var e,n={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:u||\"./this.program\"};for(e in we)void 0===we[e]?delete n[e]:n[e]=we[e];var t=[];for(e in n)t.push(e+\"=\"+n[e]);ve=t}return ve}function S(e){return 0==e%4&&(0!=e%100||0==e%400)}function be(e,n){for(var t=0,r=0;r<=n;t+=e[r++]);return t}var M=[31,29,31,30,31,30,31,31,30,31,30,31],Se=[31,28,31,30,31,30,31,31,30,31,30,31];function Me(e,n){for(e=new Date(e.getTime());0<n;){var t=e.getMonth(),r=(S(e.getFullYear())?M:Se)[t];if(!(n>r-e.getDate())){e.setDate(e.getDate()+n);break}n-=r-e.getDate()+1,e.setDate(1),t<11?e.setMonth(t+1):(e.setMonth(0),e.setFullYe", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31164"></a>
## FND-31164 — module-004 export I

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "I", "kind": "function", "index": 468, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 10361, "loader_excerpt": "Y:f?R(f):\"\"},t=R(t),f={\"%c\":\"%a %b %d %H:%M:%S %Y\",\"%D\":\"%m/%d/%y\",\"%F\":\"%Y-%m-%d\",\"%h\":\"%b\",\"%r\":\"%I:%M:%S %p\",\"%R\":\"%H:%M\",\"%T\":\"%H:%M:%S\",\"%x\":\"%m/%d/%y\",\"%X\":\"%H:%M:%S\",\"%Ec\":\"%c\",\"%EC\":\"%C\",\"%Ex\":\"%m/%d/%y\",\"%EX\":\"%H:%M:%S\",\"%Ey\":\"%y\",\"%EY\":\"%Y\",\"%Od\":\"%d\",\"%Oe\":\"%e\",\"%OH\":\"%H\",\"%OI\":\"%I\",\"%Om\":\"%m\",\"%OM\":\"%M\",\"%OS\":\"%S\",\"%Ou\":\"%u\",\"%OU\":\"%U\",\"%OV\":\"%V\",\"%Ow\":\"%w\",\"%OW\":\"%W\",\"%Oy\":\"%y\"})t=t.replace(new RegExp(c,\"g\"),f[c]);var l,p,d=\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\".split(\" \"),m=\"January February March April May June July August September October November December\".split(\" \");for(c in f={\"%a\":function(e){return d[e.P].substring(0,3)},\"%A\":function(e){return d[e.P]},\"%b\":function(e){return m[e.M].substring(0,3)},\"%B\":function(e){return m[e.M]},\"%C\":function(e){r", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31165"></a>
## FND-31165 — module-004 export J

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "J", "kind": "function", "index": 467, "signature": {"parameters": [], "results": []}, "type_index": 11, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 20587, "loader_excerpt": "sm.I).apply(null,arguments)},i._asyncify_stop_unwind=function(){return(i._asyncify_stop_unwind=i.asm.J).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.K).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.L).apply(null,arguments)},w=function e(){je||We(),je||(w=e)},i.run=We,i.preInit)for(\"function\"==typeof i.preInit&&(i.preInit=[i.preInit]);0<i.preInit.length;)i.preInit.pop()();var Ge=!0;return i.noInitialRun&&(Ge=!1),We(),i.onSpecialMessage=i.postCustomMessage,e.ready}var Xe;Xe=\"undefined\"!=typeof document&&document.currentScript?document.currentScript.src:void 0,\"undefined\"!=typeof __filename&&(Xe=Xe||__filename);return\"object\"==typeof exports&&\"object\"==typeof module?module.exports=e:\"function\"", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31166"></a>
## FND-31166 — module-004 export K

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "K", "kind": "function", "index": 466, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 20687, "loader_excerpt": ".J).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.K).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.L).apply(null,arguments)},w=function e(){je||We(),je||(w=e)},i.run=We,i.preInit)for(\"function\"==typeof i.preInit&&(i.preInit=[i.preInit]);0<i.preInit.length;)i.preInit.pop()();var Ge=!0;return i.noInitialRun&&(Ge=!1),We(),i.onSpecialMessage=i.postCustomMessage,e.ready}var Xe;Xe=\"undefined\"!=typeof document&&document.currentScript?document.currentScript.src:void 0,\"undefined\"!=typeof __filename&&(Xe=Xe||__filename);return\"object\"==typeof exports&&\"object\"==typeof module?module.exports=e:\"function\"==typeof define&&define.amd?define([],function(){return e}):\"object\"==typeof exports&&(exports.Stock", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31167"></a>
## FND-31167 — module-004 export L

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020, SRC-3021
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/imports-exports-annotated.json)

```text
{"module_id": "module-004", "direction": "export", "name": "L", "kind": "function", "index": 465, "signature": {"parameters": [], "results": []}, "type_index": 11, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 20785, "loader_excerpt": "sm.K).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.L).apply(null,arguments)},w=function e(){je||We(),je||(w=e)},i.run=We,i.preInit)for(\"function\"==typeof i.preInit&&(i.preInit=[i.preInit]);0<i.preInit.length;)i.preInit.pop()();var Ge=!0;return i.noInitialRun&&(Ge=!1),We(),i.onSpecialMessage=i.postCustomMessage,e.ready}var Xe;Xe=\"undefined\"!=typeof document&&document.currentScript?document.currentScript.src:void 0,\"undefined\"!=typeof __filename&&(Xe=Xe||__filename);return\"object\"==typeof exports&&\"object\"==typeof module?module.exports=e:\"function\"==typeof define&&define.amd?define([],function(){return e}):\"object\"==typeof exports&&(exports.Stockfish=e),e}\"undefined\"!=typeof self&&\"worker\"===self.location.hash.split(\",\")[1]||\"undefined\"!=type", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31168"></a>
## FND-31168 — module-005 complete structural inventory

7234687bytes; SHA25659b8ac9e04022617118154bc3ce32aaf505c95ab58c04996301f07eda82a4559; 749defined functions,18imported functions,17exports. All section offsets,types,limits,globals,elements,data and function body spans retained.

- Category: wasm_structure
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../wasm-analysis/modules/module-005/structure.json)

```text
Magic0061736d;version1;no custom sections.
```

<a id="FND-31169"></a>
## FND-31169 — module-005 function and call-graph analysis

1853direct caller/callee pairs;3797static direct-call sites;642indirect-call sites. Exact direct call indices recovered from full WAT. Indirect dispatch targets not resolved; opcode frequencies are syntactic counts,not execution profiling.

- Category: wasm_functions
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/functions.json)

```text
See call-graph.jsonl.gz and opcode-statistics.json.
```

<a id="FND-31170"></a>
## FND-31170 — module-005 strings and data offsets

61023ASCII candidates,61keyword-relevant candidates,16UTF16candidates. Strings linked to original file offsets and active data memory addresses when constant-resolvable. Random code/weight bytes can resemble text.

- Category: wasm_strings
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/strings.txt)

```text
All-ASCII candidates are separately gzipped; relevant output is not a semantic analysis of every string.
```

<a id="FND-31171"></a>
## FND-31171 — module-005 memory/host boundary

{"defined_memories": [{"flags": 1, "minimum": 8192, "shared": false, "memory64": false, "maximum": 8192}], "imported_memories": [], "tables": [{"element_type": "funcref", "limits": {"flags": 1, "minimum": 566, "shared": false, "memory64": false, "maximum": 566}}], "data_segments": 1312}

- Category: wasm_memory
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/structure.json)

```text
Memory limits use64KiBpages; shared flag is explicit.
```

<a id="FND-31172"></a>
## FND-31172 — module-005 new controlled instantiation

Bounded Node instantiation succeeded with explicitly stubbed imports; this is not engine search/review correctness. Initial module003failed due unhandled imported memory,then passed using exact descriptor limits. Stack-query exports were called only when present.

- Category: wasm_runtime
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No native whole-game review rerun,new server query,or cloud parity test. Historical successful full CEE/Human tests retained separately.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/runtime-observation.json)

```text
{"status": "instantiated with function import stubs", "imports": 18, "exports": 17, "memories": [{"name": "s", "bytes": 536870912, "shared": false}], "import_calls_during_instantiation": [], "elapsed_ms": 20.778331, "algorithm_calls": [], "limitation": "No wrapper runtime constructors/search/review invoked; stub instantiation is not a functional engine validation. No original application inputs used."}
```

<a id="FND-31173"></a>
## FND-31173 — module-005 import a.a

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "a", "kind": "function", "type_index": 1, "function_index": 0, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 4393, "loader_excerpt": "+\". Build with -s ASSERTIONS=1 for more info.\");l(a);throw a;}function xa(){return P.startsWith(\"data:application/octet-stream;base64,\")}var P;P=\"torch-$TORCH_VERSION-lite-single.wasm\";if(!xa()){var ya=P;P=c.locateFile?c.locateFile(ya,A):A+ya}function za(){var a=P;try{if(a==P&&G)return new Uint8Array(G);if(B)return B(a);throw\"both async and sync fetching of the wasm failed\";}catch(b){H(b)}}\nfunction Aa(){return G||!ca&&!z||\"function\"!=typeof fetch?Promise.resolve().then(function(){return za()}):fetch(P,{credentials:\"same-origin\"}).then(function(a){if(!a.ok)throw\"failed to load wasm binary file at '\"+P+\"'\";return a.arrayBuffer()}).catch(function(){return za()})}function Q(a){for(;0<a.length;){var b=a.shift();if(\"function\"==typeof b)b(c);else{var e=b.T;\"number\"==typeof e?void 0===b.R?dynCall", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31174"></a>
## FND-31174 — module-005 import a.b

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "b", "kind": "function", "type_index": 1, "function_index": 1, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 2201, "loader_excerpt": "document.currentScript&&(A=document.currentScript.src),_scriptDir&&(A=_scriptDir),0!==A.indexOf(\"blob:\")?A=A.substr(0,A.replace(/[?#].*/,\"\").lastIndexOf(\"/\")+1):A=\"\",ea=a=>{var b=new XMLHttpRequest;b.open(\"GET\",a,!1);b.send(null);return b.responseText},z&&(B=a=>{var b=new XMLHttpRequest;b.open(\"GET\",a,!1);\nb.responseType=\"arraybuffer\";b.send(null);return new Uint8Array(b.response)});var ia=c.print||console.log.bind(console),E=c.printErr||console.warn.bind(console);Object.assign(c,ba);ba=null;c.arguments&&(v=c.arguments);c.thisProgram&&(w=c.thisProgram);c.quit&&(x=c.quit);var G;c.wasmBinary&&(G=c.wasmBinary);var noExitRuntime=c.noExitRuntime||!0;\"object\"!=typeof WebAssembly&&H(\"no native wasm support detected\");var ja,I=!1,ka=\"undefined\"!=typeof TextDecoder?new TextDecoder(\"utf8\"):void 0;\nf", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31175"></a>
## FND-31175 — module-005 import a.c

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "c", "kind": "function", "type_index": 13, "function_index": 2, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11519, "loader_excerpt": "b,e){(new Ca(a)).U(b,e);Da++;throw a;},f:function(){return 0},k:function(){return 0},l:function(){},c:function(){H(\"\")},q:function(a,b){if(0===a)a=Date.now();else if(1===a||4===a)a=Ga();else return M[ab()>>2]=28,-1;M[b>>2]=a/1E3|0;M[b+4>>2]=a%1E3*1E6|0;return 0},r:function(a,b,e){J.copyWithin(a,b,b+e)},d:function(){H(\"OOM\")},a:function(a){Za(b=>Ja(b,a))},o:function(a,b){var e=0;La().forEach(function(f,h){var g=b+e;h=M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31176"></a>
## FND-31176 — module-005 import a.d

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "d", "kind": "function", "type_index": 0, "function_index": 3, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 732, "loader_excerpt": "ned\"===typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var a,b={open:function(e,f){a=f},send:function(){require(\"fs\").readFile(a,function(e,f){b.readyState=4;e?(console.error(e),b.status=404,b.onerror(e)):(b.status=200,b.response=f,b.onreadystatechange(),b.onload())})}};return b}),fetch=null);c.print=function(a){c.listener?c.listener(a):console.log(a)};\nc.printErr=function(a){c.listener?c.listener(a):console.error(a)};c.terminate=function(){\"undefined\"!==typeof PThread&&PThread.ga()};var ba=Object.assign({},c),v=[],w=\"./this.program\",x=(a,b)=>{throw b;},ca=\"object\"==typeof window,z=\"function\"==typeof importScripts,da=\"object\"==typeof process&&\"object\"==typeof process.versions&&\"string\"==typeof process.versions.node,A=\"\",ea,B,fs,fa,ha;\nif(da)A=z?require(\"path\").dirname(A)+\"/\":__dir", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31177"></a>
## FND-31177 — module-005 import a.e

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "e", "kind": "function", "type_index": 0, "function_index": 4, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 10592, "loader_excerpt": "!=typeof Fibers&&Fibers.ia()))}}:h})(e);return b}function Wa(){return new Promise((a,b)=>{Ta={resolve:a,reject:b}})}\nfunction Xa(){var a=Ya(10485772),b=a+12;M[a>>2]=b;M[a+4>>2]=b+10485760;b=Y[0];var e=Qa[b];void 0===e&&(e=Sa++,Qa[b]=e,Ra[e]=b);M[a+8>>2]=e;return a}\nfunction Za(a){if(!I)if(0===W){var b=!1,e=!1;a(()=>{if(!I&&(b=!0,e)){W=2;V(()=>c._asyncify_start_rewind(X));\"undefined\"!=typeof Browser&&Browser.S.T&&Browser.S.resume();var f=!1;try{var h=(0,c.asm[Ra[M[X+8>>2]]])()}catch(r){h=r,f=!0}var g=!1;if(!X){var k=Ta;k&&(Ta=null,(f?k.reject:k.resolve)(h),g=!0)}if(f&&!g)throw h;}});e=!0;b||(W=1,X=Xa(),V(()=>c._asyncify_start_unwind(X)),\"undefined\"!=typeof Browser&&Browser.S.T&&Browser.S.pause())}else 2===W?(W=0,V(c._asyncify_stop_rewind),$a(X),X=null,Ua.forEach(f=>\nHa(f))):H(\"invalid state", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31178"></a>
## FND-31178 — module-005 import a.f

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "f", "kind": "function", "type_index": 4, "function_index": 5, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 2069, "loader_excerpt": "xit(a)},c.inspect=function(){return\"[Emscripten Module object]\"};else if(ca||z)z?A=self.location.href:\"undefined\"!=typeof document&&document.currentScript&&(A=document.currentScript.src),_scriptDir&&(A=_scriptDir),0!==A.indexOf(\"blob:\")?A=A.substr(0,A.replace(/[?#].*/,\"\").lastIndexOf(\"/\")+1):A=\"\",ea=a=>{var b=new XMLHttpRequest;b.open(\"GET\",a,!1);b.send(null);return b.responseText},z&&(B=a=>{var b=new XMLHttpRequest;b.open(\"GET\",a,!1);\nb.responseType=\"arraybuffer\";b.send(null);return new Uint8Array(b.response)});var ia=c.print||console.log.bind(console),E=c.printErr||console.warn.bind(console);Object.assign(c,ba);ba=null;c.arguments&&(v=c.arguments);c.thisProgram&&(w=c.thisProgram);c.quit&&(x=c.quit);var G;c.wasmBinary&&(G=c.wasmBinary);var noExitRuntime=c.noExitRuntime||!0;\"object\"!=typeo", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31179"></a>
## FND-31179 — module-005 import a.g

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "g", "kind": "function", "type_index": 8, "function_index": 6, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11406, "loader_excerpt": "n Pa(a){var b=Array(oa(a)+1);na(a,b,0,b.length);return b}\nvar cb={h:function(a){return Ya(a+16)+16},g:function(a,b,e){(new Ca(a)).U(b,e);Da++;throw a;},f:function(){return 0},k:function(){return 0},l:function(){},c:function(){H(\"\")},q:function(a,b){if(0===a)a=Date.now();else if(1===a||4===a)a=Ga();else return M[ab()>>2]=28,-1;M[b>>2]=a/1E3|0;M[b+4>>2]=a%1E3*1E6|0;return 0},r:function(a,b,e){J.copyWithin(a,b,b+e)},d:function(){H(\"OOM\")},a:function(a){Za(b=>Ja(b,a))},o:function(a,b){var e=0;La().forEach(function(f,h){var g=b+e;h=M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31180"></a>
## FND-31180 — module-005 import a.h

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "h", "kind": "function", "type_index": 0, "function_index": 7, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11372, "loader_excerpt": "))):H(\"invalid state: \"+W)}function Pa(a){var b=Array(oa(a)+1);na(a,b,0,b.length);return b}\nvar cb={h:function(a){return Ya(a+16)+16},g:function(a,b,e){(new Ca(a)).U(b,e);Da++;throw a;},f:function(){return 0},k:function(){return 0},l:function(){},c:function(){H(\"\")},q:function(a,b){if(0===a)a=Date.now();else if(1===a||4===a)a=Ga();else return M[ab()>>2]=28,-1;M[b>>2]=a/1E3|0;M[b+4>>2]=a%1E3*1E6|0;return 0},r:function(a,b,e){J.copyWithin(a,b,b+e)},d:function(){H(\"OOM\")},a:function(a){Za(b=>Ja(b,a))},o:function(a,b){var e=0;La().forEach(function(f,h){var g=b+e;h=M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31181"></a>
## FND-31181 — module-005 import a.i

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "i", "kind": "function", "type_index": 7, "function_index": 8, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 12174, "loader_excerpt": "nction(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){var k=M[b>>2],r=M[b+4>>2];b+=8;for(var u=0;u<r;u++){var p=J[k+u],q=Ea[a];0===p||10===p?((1===a?ia:E)(la(q,0)),q.length=0):q.push(p)}h+=r}M[f>>2]=h;return 0},n:function(a,\nb,e,f){return Oa(a,b,e,f)}};\n(function(){function a(g){g=g.exports;g=Va(g);c.asm=g;ja=c.asm.s;g=ja.buffer;c.HEAP8=L=new Int8Array(g);c.HEAP16=new Int16Array(g);c.HEAP32=M=new Int32Array(g);c.HEAPU8=J=new Uint8Array(g);c.HEAPU16=new Uint16Array(g);c.HEAPU32=new Uint32Array(g);c.HEAPF32=new Float32Array(g);c.HEAPF64=new Float64Array(g);ra.unshift(c.asm.t);N--;c.monitorRunDependencies&&c.monitorRunDependencies(N);0==N&&(null!==wa&&(clearInterval(wa),wa=null),O&&(g=O,O=null,g()))}fun", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31182"></a>
## FND-31182 — module-005 import a.j

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "j", "kind": "function", "type_index": 7, "function_index": 9, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 12093, "loader_excerpt": "forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){var k=M[b>>2],r=M[b+4>>2];b+=8;for(var u=0;u<r;u++){var p=J[k+u],q=Ea[a];0===p||10===p?((1===a?ia:E)(la(q,0)),q.length=0):q.push(p)}h+=r}M[f>>2]=h;return 0},n:function(a,\nb,e,f){return Oa(a,b,e,f)}};\n(function(){function a(g){g=g.exports;g=Va(g);c.asm=g;ja=c.asm.s;g=ja.buffer;c.HEAP8=L=new Int8Array(g);c.HEAP16=new Int16Array(g);c.HEAP32=M=new Int32Array(g);c.HEAPU8=J=new Uint8Array(g);c.HEAPU16=new Uint16Array(g);c.HEAPU32=new Uint32Array(g);c.HEAPF32=new Float32Array(g);c.HEAPF64=new Float64Array(g);ra.unshift(c.asm.t);N--;c.monitorRunDependencies&&c.monitorRunDepen", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31183"></a>
## FND-31183 — module-005 import a.k

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "k", "kind": "function", "type_index": 4, "function_index": 10, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 3174, "loader_excerpt": "92==(h&224))f+=String.fromCharCode((h&31)<<6|g);else{var k=a[b++]&63;h=224==(h&240)?(h&15)<<12|g<<6|k:(h&7)<<18|g<<12|k<<6|a[b++]&63;65536>h?f+=String.fromCharCode(h):(h-=65536,f+=String.fromCharCode(55296|h>>10,56320|h&1023))}}else f+=String.fromCharCode(h)}return f}function ma(a){return a?la(J,a,void 0):\"\"}\nfunction na(a,b,e,f){if(0<f){f=e+f-1;for(var h=0;h<a.length;++h){var g=a.charCodeAt(h);if(55296<=g&&57343>=g){var k=a.charCodeAt(++h);g=65536+((g&1023)<<10)|k&1023}if(127>=g){if(e>=f)break;b[e++]=g}else{if(2047>=g){if(e+1>=f)break;b[e++]=192|g>>6}else{if(65535>=g){if(e+2>=f)break;b[e++]=224|g>>12}else{if(e+3>=f)break;b[e++]=240|g>>18;b[e++]=128|g>>12&63}b[e++]=128|g>>6&63}b[e++]=128|g&63}}b[e]=0}}\nfunction oa(a){for(var b=0,e=0;e<a.length;++e){var f=a.charCodeAt(e);55296<=f&&57343>=f&", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31184"></a>
## FND-31184 — module-005 import a.l

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "l", "kind": "function", "type_index": 4, "function_index": 11, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 5158, "loader_excerpt": "ber\"==typeof e?void 0===b.R?dynCall_v.call(null,e):dynCall_vi.apply(null,[e,b.R]):e(void 0===b.R?null:b.R)}}}\nfunction Ba(a){a instanceof C||\"unwind\"==a||x(1,a)}function Ca(a){this.L=a-16;this.Z=function(b){M[this.L+4>>2]=b};this.W=function(b){M[this.L+8>>2]=b};this.X=function(){M[this.L>>2]=0};this.V=function(){L[this.L+12>>0]=0};this.Y=function(){L[this.L+13>>0]=0};this.U=function(b,e){this.Z(b);this.W(e);this.X();this.V();this.Y()}}var Da=0,Ea=[null,[],[]],Fa={},Ga;Ga=da?()=>{var a=process.hrtime();return 1E3*a[0]+a[1]/1E6}:()=>performance.now();function Ha(a){if(!ua&&!I)try{a()}catch(b){Ba(b)}}\nfunction Ja(a,b){return setTimeout(function(){Ha(a)},b)}var Ka={};function La(){if(!Ma){var a={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof na", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31185"></a>
## FND-31185 — module-005 import a.m

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "m", "kind": "function", "type_index": 6, "function_index": 12, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 9008, "loader_excerpt": "\\t\"},\"%u\":function(d){return d.O||7},\"%U\":function(d){var m=new Date(d.J+1900,0,1),n=0===m.getDay()?m:U(m,7-m.getDay());d=new Date(d.J+1900,d.K,d.M);return 0>k(n,d)?g(Math.ceil((31-n.getDate()+\n(Na(R(d.getFullYear())?S:T,d.getMonth()-1)-31)+d.getDate())/7),2):0===k(n,m)?\"01\":\"00\"},\"%V\":function(d){var m=new Date(d.J+1901,0,4),n=r(new Date(d.J+1900,0,4));m=r(m);var F=U(new Date(d.J+1900,0,1),d.P);return 0>k(F,n)?\"53\":0>=k(m,F)?\"01\":g(Math.ceil((n.getFullYear()<d.J+1900?d.P+32-n.getDate():d.P+1-n.getDate())/7),2)},\"%w\":function(d){return d.O},\"%W\":function(d){var m=new Date(d.J,0,1),n=1===m.getDay()?m:U(m,0===m.getDay()?1:7-m.getDay()+1);d=new Date(d.J+1900,d.K,d.M);return 0>k(n,d)?g(Math.ceil((31-\nn.getDate()+(Na(R(d.getFullYear())?S:T,d.getMonth()-1)-31)+d.getDate())/7),2):0===k(n,m)?\"01\":", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31186"></a>
## FND-31186 — module-005 import a.n

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "n", "kind": "function", "type_index": 6, "function_index": 13, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 708, "loader_excerpt": "==typeof fetch&&(\"undefined\"===typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var a,b={open:function(e,f){a=f},send:function(){require(\"fs\").readFile(a,function(e,f){b.readyState=4;e?(console.error(e),b.status=404,b.onerror(e)):(b.status=200,b.response=f,b.onreadystatechange(),b.onload())})}};return b}),fetch=null);c.print=function(a){c.listener?c.listener(a):console.log(a)};\nc.printErr=function(a){c.listener?c.listener(a):console.error(a)};c.terminate=function(){\"undefined\"!==typeof PThread&&PThread.ga()};var ba=Object.assign({},c),v=[],w=\"./this.program\",x=(a,b)=>{throw b;},ca=\"object\"==typeof window,z=\"function\"==typeof importScripts,da=\"object\"==typeof process&&\"object\"==typeof process.versions&&\"string\"==typeof process.versions.node,A=\"\",ea,B,fs,fa,ha;\nif(da)A=z?require(\"pat", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31187"></a>
## FND-31187 — module-005 import a.o

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "o", "kind": "function", "type_index": 2, "function_index": 14, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11776, "loader_excerpt": "rn 0},r:function(a,b,e){J.copyWithin(a,b,b+e)},d:function(){H(\"OOM\")},a:function(a){Za(b=>Ja(b,a))},o:function(a,b){var e=0;La().forEach(function(f,h){var g=b+e;h=M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){var k=M[b>>2],r=M[b+4>>2];b+=8;for(var u=0;u<r;u++){var p=J[k+u],q=Ea[a];0===p||10===p?((1===a?ia:E)(la(q,0)),q.length=0):q.push(p)}h+=r}M[f>>2]=h;return 0},n:function(a,\nb,e,f){return Oa(a,b,e,f)}};\n(function(){function a(g){g=g.exports;g=Va(g);c.asm=g;ja=", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31188"></a>
## FND-31188 — module-005 import a.p

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "p", "kind": "function", "type_index": 2, "function_index": 15, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11939, "loader_excerpt": "M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){var k=M[b>>2],r=M[b+4>>2];b+=8;for(var u=0;u<r;u++){var p=J[k+u],q=Ea[a];0===p||10===p?((1===a?ia:E)(la(q,0)),q.length=0):q.push(p)}h+=r}M[f>>2]=h;return 0},n:function(a,\nb,e,f){return Oa(a,b,e,f)}};\n(function(){function a(g){g=g.exports;g=Va(g);c.asm=g;ja=c.asm.s;g=ja.buffer;c.HEAP8=L=new Int8Array(g);c.HEAP16=new Int16Array(g);c.HEAP32=M=new Int32Array(g);c.HEAPU8=J=new Uint8Array(g);c.HEAPU16=new Uint16Array(g);c.", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31189"></a>
## FND-31189 — module-005 import a.q

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "q", "kind": "function", "type_index": 2, "function_index": 16, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11539, "loader_excerpt": ",e);Da++;throw a;},f:function(){return 0},k:function(){return 0},l:function(){},c:function(){H(\"\")},q:function(a,b){if(0===a)a=Date.now();else if(1===a||4===a)a=Ga();else return M[ab()>>2]=28,-1;M[b>>2]=a/1E3|0;M[b+4>>2]=a%1E3*1E6|0;return 0},r:function(a,b,e){J.copyWithin(a,b,b+e)},d:function(){H(\"OOM\")},a:function(a){Za(b=>Ja(b,a))},o:function(a,b){var e=0;La().forEach(function(f,h){var g=b+e;h=M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){var k=M[b>>2],r=M[b+", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31190"></a>
## FND-31190 — module-005 import a.r

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3022, SRC-3023
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31168
- [Exact supporting artifact](../wasm-analysis/modules/module-005/imports-exports-annotated.json)

```text
{"module_id": "module-005", "direction": "import", "module": "a", "name": "r", "kind": "function", "type_index": 4, "function_index": 17, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 11682, "loader_excerpt": "if(1===a||4===a)a=Ga();else return M[ab()>>2]=28,-1;M[b>>2]=a/1E3|0;M[b+4>>2]=a%1E3*1E6|0;return 0},r:function(a,b,e){J.copyWithin(a,b,b+e)},d:function(){H(\"OOM\")},a:function(a){Za(b=>Ja(b,a))},o:function(a,b){var e=0;La().forEach(function(f,h){var g=b+e;h=M[a+4*h>>2]=g;for(g=0;g<f.length;++g)L[h++>>\n0]=f.charCodeAt(g);L[h>>0]=0;e+=f.length+1});return 0},p:function(a,b){var e=La();M[a>>2]=e.length;var f=0;e.forEach(function(h){f+=h.length+1});M[b>>2]=f;return 0},b:function(a){bb(a)},e:function(){return 0},j:function(a,b,e,f){a=Fa.fa(a);b=Fa.ea(a,b,e);M[f>>2]=b;return 0},m:function(){},i:function(a,b,e,f){for(var h=0,g=0;g<e;g++){var k=M[b>>2],r=M[b+4>>2];b+=8;for(var u=0;u<r;u++){var p=J[k+u],q=Ea[a];0===p||10===p?((1===a?ia:E)(la(q,0)),q.length=0):q.push(p)}h+=r}M[f>>2]=h;return 0},n:func", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31191"></a>
## FND-31191 — module-005 export s

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
{"module_id": "module-005", "direction": "export", "name": "s", "kind": "memory", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 4812, "loader_excerpt": "ca&&!z||\"function\"!=typeof fetch?Promise.resolve().then(function(){return za()}):fetch(P,{credentials:\"same-origin\"}).then(function(a){if(!a.ok)throw\"failed to load wasm binary file at '\"+P+\"'\";return a.arrayBuffer()}).catch(function(){return za()})}function Q(a){for(;0<a.length;){var b=a.shift();if(\"function\"==typeof b)b(c);else{var e=b.T;\"number\"==typeof e?void 0===b.R?dynCall_v.call(null,e):dynCall_vi.apply(null,[e,b.R]):e(void 0===b.R?null:b.R)}}}\nfunction Ba(a){a instanceof C||\"unwind\"==a||x(1,a)}function Ca(a){this.L=a-16;this.Z=function(b){M[this.L+4>>2]=b};this.W=function(b){M[this.L+8>>2]=b};this.X=function(){M[this.L>>2]=0};this.V=function(){L[this.L+12>>0]=0};this.Y=function(){L[this.L+13>>0]=0};this.U=function(b,e){this.Z(b);this.W(e);this.X();this.V();this.Y()}}var Da=0,Ea=[nu", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31192"></a>
## FND-31192 — module-005 export t

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
{"module_id": "module-005", "direction": "export", "name": "t", "kind": "function", "index": 283, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 10601, "loader_excerpt": "Fibers&&Fibers.ia()))}}:h})(e);return b}function Wa(){return new Promise((a,b)=>{Ta={resolve:a,reject:b}})}\nfunction Xa(){var a=Ya(10485772),b=a+12;M[a>>2]=b;M[a+4>>2]=b+10485760;b=Y[0];var e=Qa[b];void 0===e&&(e=Sa++,Qa[b]=e,Ra[e]=b);M[a+8>>2]=e;return a}\nfunction Za(a){if(!I)if(0===W){var b=!1,e=!1;a(()=>{if(!I&&(b=!0,e)){W=2;V(()=>c._asyncify_start_rewind(X));\"undefined\"!=typeof Browser&&Browser.S.T&&Browser.S.resume();var f=!1;try{var h=(0,c.asm[Ra[M[X+8>>2]]])()}catch(r){h=r,f=!0}var g=!1;if(!X){var k=Ta;k&&(Ta=null,(f?k.reject:k.resolve)(h),g=!0)}if(f&&!g)throw h;}});e=!0;b||(W=1,X=Xa(),V(()=>c._asyncify_start_unwind(X)),\"undefined\"!=typeof Browser&&Browser.S.T&&Browser.S.pause())}else 2===W?(W=0,V(c._asyncify_stop_rewind),$a(X),X=null,Ua.forEach(f=>\nHa(f))):H(\"invalid state: \"+W)}fu", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31193"></a>
## FND-31193 — module-005 export u

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
{"module_id": "module-005", "direction": "export", "name": "u", "kind": "function", "index": 18, "signature": {"parameters": ["i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 4114, "loader_excerpt": ",L,e,b);return e}var L,J,M,qa=[],ra=[],sa=[],ta=[],ua=!1,D=0;function va(){var a=c.preRun.shift();qa.unshift(a)}var N=0,wa=null,O=null;c.preloadedImages={};c.preloadedAudios={};\nfunction H(a){if(c.onAbort)c.onAbort(a);a=\"Aborted(\"+a+\")\";E(a);I=!0;a=new WebAssembly.RuntimeError(a+\". Build with -s ASSERTIONS=1 for more info.\");l(a);throw a;}function xa(){return P.startsWith(\"data:application/octet-stream;base64,\")}var P;P=\"torch-$TORCH_VERSION-lite-single.wasm\";if(!xa()){var ya=P;P=c.locateFile?c.locateFile(ya,A):A+ya}function za(){var a=P;try{if(a==P&&G)return new Uint8Array(G);if(B)return B(a);throw\"both async and sync fetching of the wasm failed\";}catch(b){H(b)}}\nfunction Aa(){return G||!ca&&!z||\"function\"!=typeof fetch?Promise.resolve().then(function(){return za()}):fetch(P,{credentials:", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31194"></a>
## FND-31194 — module-005 export v

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
{"module_id": "module-005", "direction": "export", "name": "v", "kind": "function", "index": 676, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 1316, "loader_excerpt": "peof window,z=\"function\"==typeof importScripts,da=\"object\"==typeof process&&\"object\"==typeof process.versions&&\"string\"==typeof process.versions.node,A=\"\",ea,B,fs,fa,ha;\nif(da)A=z?require(\"path\").dirname(A)+\"/\":__dirname+\"/\",ha=()=>{fa||(fs=require(\"fs\"),fa=require(\"path\"))},ea=function(a,b){ha();a=fa.normalize(a);return fs.readFileSync(a,b?void 0:\"utf8\")},B=a=>{a=ea(a,!0);a.buffer||(a=new Uint8Array(a));return a},1<process.argv.length&&(w=process.argv[1].replace(/\\\\/g,\"/\")),v=process.argv.slice(2),process.on(\"uncaughtException\",function(a){if(!(a instanceof C))throw a;}),process.on(\"unhandledRejection\",function(a){throw a;}),x=(a,b)=>{if(noExitRuntime||0<D)throw process.exitCode=\na,b;b instanceof C||E(\"exiting due to exception: \"+b);process.exit(a)},c.inspect=function(){return\"[Emscripten", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31195"></a>
## FND-31195 — module-005 export w

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
{"module_id": "module-005", "direction": "export", "name": "w", "kind": "function", "index": 675, "signature": {"parameters": ["i32"], "results": []}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 2550, "loader_excerpt": ";return new Uint8Array(b.response)});var ia=c.print||console.log.bind(console),E=c.printErr||console.warn.bind(console);Object.assign(c,ba);ba=null;c.arguments&&(v=c.arguments);c.thisProgram&&(w=c.thisProgram);c.quit&&(x=c.quit);var G;c.wasmBinary&&(G=c.wasmBinary);var noExitRuntime=c.noExitRuntime||!0;\"object\"!=typeof WebAssembly&&H(\"no native wasm support detected\");var ja,I=!1,ka=\"undefined\"!=typeof TextDecoder?new TextDecoder(\"utf8\"):void 0;\nfunction la(a,b,e){var f=b+e;for(e=b;a[e]&&!(e>=f);)++e;if(16<e-b&&a.subarray&&ka)return ka.decode(a.subarray(b,e));for(f=\"\";b<e;){var h=a[b++];if(h&128){var g=a[b++]&63;if(192==(h&224))f+=String.fromCharCode((h&31)<<6|g);else{var k=a[b++]&63;h=224==(h&240)?(h&15)<<12|g<<6|k:(h&7)<<18|g<<12|k<<6|a[b++]&63;65536>h?f+=String.fromCharCode(h):(h-=65536", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31196"></a>
## FND-31196 — module-005 export x

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
{"module_id": "module-005", "direction": "export", "name": "x", "kind": "function", "index": 42, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 14018, "loader_excerpt": "rn(c._command=c.asm.w).apply(null,arguments)};\nvar Ya=c._malloc=function(){return(Ya=c._malloc=c.asm.x).apply(null,arguments)},ab=c.___errno_location=function(){return(ab=c.___errno_location=c.asm.y).apply(null,arguments)},db=c.stackSave=function(){return(db=c.stackSave=c.asm.A).apply(null,arguments)},eb=c.stackRestore=function(){return(eb=c.stackRestore=c.asm.B).apply(null,arguments)},K=c.stackAlloc=function(){return(K=c.stackAlloc=c.asm.C).apply(null,arguments)},dynCall_vi=c.dynCall_vi=function(){return(dynCall_vi=c.dynCall_vi=c.asm.D).apply(null,\narguments)},dynCall_v=c.dynCall_v=function(){return(dynCall_v=c.dynCall_v=c.asm.E).apply(null,arguments)};c._asyncify_start_unwind=function(){return(c._asyncify_start_unwind=c.asm.F).apply(null,arguments)};c._asyncify_stop_unwind=function(){ret", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31197"></a>
## FND-31197 — module-005 export y

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
{"module_id": "module-005", "direction": "export", "name": "y", "kind": "function", "index": 671, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 19, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 15202, "loader_excerpt": "n(t){var y=0;if(null!==t&&void 0!==t&&0!==t){var d=(t.length<<2)+1;y=K(d);na(t,J,y,d)}return y},array:function(t){var y=K(t.length);L.set(t,y);return y}};a=c[\"_\"+a];var r=[],u=0;if(f)for(var p=0;p<f.length;p++){var q=k[e[p]];q?(0===u&&(u=db()),r[p]=q(f[p])):r[p]=f[p]}e=X;f=a.apply(null,r);D+=1;h=h&&h.async;if(X!=e)return Wa().then(g);f=g(f);return h?Promise.resolve(f):f};var Z;\nfunction C(a){this.name=\"ExitStatus\";this.message=\"Program terminated with exit(\"+a+\")\";this.status=a}O=function fb(){Z||gb();Z||(O=fb)};\nfunction gb(a){function b(){if(!Z&&(Z=!0,c.calledRun=!0,!I)){Q(ra);Q(sa);aa(c);if(c.onRuntimeInitialized)c.onRuntimeInitialized();if(hb){var e=a,f=c._main;e=e||[];var h=e.length+1,g=K(4*(h+1));M[g>>2]=pa(w);for(var k=1;k<h;k++)M[(g>>2)+k]=pa(e[k-1]);M[(g>>2)+h]=0;try{var r=f(h,g);", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31198"></a>
## FND-31198 — module-005 export z

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
{"module_id": "module-005", "direction": "export", "name": "z", "kind": "table", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": null, "loader_excerpt": "", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31199"></a>
## FND-31199 — module-005 export A

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
{"module_id": "module-005", "direction": "export", "name": "A", "kind": "function", "index": 697, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 19, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 14194, "loader_excerpt": "errno_location=c.asm.y).apply(null,arguments)},db=c.stackSave=function(){return(db=c.stackSave=c.asm.A).apply(null,arguments)},eb=c.stackRestore=function(){return(eb=c.stackRestore=c.asm.B).apply(null,arguments)},K=c.stackAlloc=function(){return(K=c.stackAlloc=c.asm.C).apply(null,arguments)},dynCall_vi=c.dynCall_vi=function(){return(dynCall_vi=c.dynCall_vi=c.asm.D).apply(null,\narguments)},dynCall_v=c.dynCall_v=function(){return(dynCall_v=c.dynCall_v=c.asm.E).apply(null,arguments)};c._asyncify_start_unwind=function(){return(c._asyncify_start_unwind=c.asm.F).apply(null,arguments)};c._asyncify_stop_unwind=function(){return(c._asyncify_stop_unwind=c.asm.G).apply(null,arguments)};c._asyncify_start_rewind=function(){return(c._asyncify_start_rewind=c.asm.H).apply(null,arguments)};c._asyncify_stop", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```
