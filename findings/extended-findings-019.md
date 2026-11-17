# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-31080"></a>
## FND-31080 — module-003 import a.E

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "E", "kind": "function", "type_index": 10, "function_index": 29, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 18345, "loader_excerpt": "default\",\"low-power\",\"high-performance\"],Ze={};function et(){if(!Je){var e,t={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:Y||\"./this.program\"};for(e in Ze)void 0===Ze[e]?delete t[e]:t[e]=Ze[e];var n=[];for(e in t)n.push(e+\"=\"+t[e]);Je=n}return Je}function tt(r,a){var o;return f?w(8,1,r,a):(o=0,et().forEach(function(e,t){var n=a+o;for(t=_[r+4*t>>2]=n,n=0;n<e.length;++n)h[t++>>0]=e.charCodeAt(n);h[t>>0]=0,o+=e.length+1}),0)}function nt(e,t){var n,r;return f?w(9,1,e,t):(n=et(),_[e>>2]=n.length,r=0,n.forEach(function(e){r+=e.length+1}),_[t>>2]=r,0)}function rt(e){return f?w(10,1,e):0}function at(e,t,n,r){return f?w(11,1,e,t,n,r):(e=Fe.Bb(e),t=Fe.Ab(e,t,n", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31081"></a>
## FND-31081 — module-003 import a.F

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "F", "kind": "function", "type_index": 25, "function_index": 30, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["f64"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 27110, "loader_excerpt": "e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];return(e<0?Ae[-e-1]:Mt[e]).apply(null,qe)},v:function(){y(\"OOM\")},G:function(e,t,n){return(Ne(e)?He:Ye)(e,t,n)},m:function(){},M:function(e,t,n){return R+=1,setTimeout(function(){--R,j(function(){P.apply(null,[e,n])})},t)},c:function(n){At(function(e){var t;t=e,R+=1,$t(function(){--R,j(t)},n)})},o:function(e,n,t,r,a){function o(e,t){Qe(e,t.response,function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)},function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)})}function i(e){j(function(){h?P.apply(null,[h,e]):a&&a(e)},w)}function s(e){--R,j(function(){p?P.apply(null,[p,e]):t&&t(e)},w)}function u(e){j(function", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31082"></a>
## FND-31082 — module-003 import a.G

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "G", "kind": "function", "type_index": 3, "function_index": 31, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 18400, "loader_excerpt": " et(){if(!Je){var e,t={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:Y||\"./this.program\"};for(e in Ze)void 0===Ze[e]?delete t[e]:t[e]=Ze[e];var n=[];for(e in t)n.push(e+\"=\"+t[e]);Je=n}return Je}function tt(r,a){var o;return f?w(8,1,r,a):(o=0,et().forEach(function(e,t){var n=a+o;for(t=_[r+4*t>>2]=n,n=0;n<e.length;++n)h[t++>>0]=e.charCodeAt(n);h[t>>0]=0,o+=e.length+1}),0)}function nt(e,t){var n,r;return f?w(9,1,e,t):(n=et(),_[e>>2]=n.length,r=0,n.forEach(function(e){r+=e.length+1}),_[t>>2]=r,0)}function rt(e){return f?w(10,1,e):0}function at(e,t,n,r){return f?w(11,1,e,t,n,r):(e=Fe.Bb(e),t=Fe.Ab(e,t,n),_[r>>2]=t,0)}function ot(e,t,n,r,a){if(f)return w(12,", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31083"></a>
## FND-31083 — module-003 import a.H

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "H", "kind": "function", "type_index": 2, "function_index": 32, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 18361, "loader_excerpt": "wer\",\"high-performance\"],Ze={};function et(){if(!Je){var e,t={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:Y||\"./this.program\"};for(e in Ze)void 0===Ze[e]?delete t[e]:t[e]=Ze[e];var n=[];for(e in t)n.push(e+\"=\"+t[e]);Je=n}return Je}function tt(r,a){var o;return f?w(8,1,r,a):(o=0,et().forEach(function(e,t){var n=a+o;for(t=_[r+4*t>>2]=n,n=0;n<e.length;++n)h[t++>>0]=e.charCodeAt(n);h[t>>0]=0,o+=e.length+1}),0)}function nt(e,t){var n,r;return f?w(9,1,e,t):(n=et(),_[e>>2]=n.length,r=0,n.forEach(function(e){r+=e.length+1}),_[t>>2]=r,0)}function rt(e){return f?w(10,1,e):0}function at(e,t,n,r){return f?w(11,1,e,t,n,r):(e=Fe.Bb(e),t=Fe.Ab(e,t,n),_[r>>2]=t,0)}f", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31084"></a>
## FND-31084 — module-003 import a.I

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "I", "kind": "function", "type_index": 0, "function_index": 33, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 20862, "loader_excerpt": "b:f?O(f):\"\"},n=O(n),f={\"%c\":\"%a %b %d %H:%M:%S %Y\",\"%D\":\"%m/%d/%y\",\"%F\":\"%Y-%m-%d\",\"%h\":\"%b\",\"%r\":\"%I:%M:%S %p\",\"%R\":\"%H:%M\",\"%T\":\"%H:%M:%S\",\"%x\":\"%m/%d/%y\",\"%X\":\"%H:%M:%S\",\"%Ec\":\"%c\",\"%EC\":\"%C\",\"%Ex\":\"%m/%d/%y\",\"%EX\":\"%H:%M:%S\",\"%Ey\":\"%y\",\"%EY\":\"%Y\",\"%Od\":\"%d\",\"%Oe\":\"%e\",\"%OH\":\"%H\",\"%OI\":\"%I\",\"%Om\":\"%m\",\"%OM\":\"%M\",\"%OS\":\"%S\",\"%Ou\":\"%u\",\"%OU\":\"%U\",\"%OV\":\"%V\",\"%Ow\":\"%w\",\"%OW\":\"%W\",\"%Oy\":\"%y\"})n=n.replace(new RegExp(c,\"g\"),f[c]);var l,d,p=\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\".split(\" \"),m=\"January February March April May June July August September October November December\".split(\" \");for(c in f={\"%a\":function(e){return p[e.La].substring(0,3)},\"%A\":function(e){return p[e.La]},\"%b\":function(e){return m[e.Ca].substring(0,3)},\"%B\":function(e){return m[e.Ca]},\"%C\":function(", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31085"></a>
## FND-31085 — module-003 import a.J

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "J", "kind": "function", "type_index": 2, "function_index": 34, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 25771, "loader_excerpt": ".xb=\"spawnThread\",postMessage(n,a),0):ke(n)},I:function(e){throw f?v.ab(e):(v.Za(),Xt(e)),\"unwind\"},J:function(e,t){var n=e,r=t;if(!n)return l(\"pthread_join attempted on a null thread pointer!\"),71;if(f&&x()==n)return l(\"PThread \"+n+\" is attempting to join to itself!\"),16;if(!f&&Tt()==n)return l(\"Main thread \"+n+\" is attempting to join to itself!\"),16;if(_[n+12>>2]!==n)return l(\"pthread_join attempted on thread \"+n+\", which does not point to a valid thread, or does not exist anymore!\"),71;if(Atomics.load(C,n+64>>2))return l(\"Attempted to join thread \"+n+\", which was already detached!\"),28;for(Ie();;){var a=Atomics.load(C,n>>2);if(1==a)return a=Atomics.load(C,n+4>>2),r&&(_[r>>2]=a),Atomics.store(C,n+64>>2,1),f?postMessage({cmd:\"cleanupThread\",thread:n}):Me(n),0;Ft(),f||Dt(),Te(n,a,f?100:1)}", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31086"></a>
## FND-31086 — module-003 import a.K

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "K", "kind": "function", "type_index": 6, "function_index": 35, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 25122, "loader_excerpt": "me\",n,r?O(r):\"unknown function\"])},b:Se,p:function(e,t){v.Sa.push(function(){P.apply(null,[e,t])})},K:function(e,t,n,r){if(\"undefined\"==typeof SharedArrayBuffer)return l(\"Current environment does not support SharedArrayBuffer, pthreads are not available!\"),6;if(!e)return l(\"pthread_create called with a null thread pointer!\"),28;var a=[];if(f&&0===a.length)return It(687865856,e,t,n,r);var o,i=0,s=0;t&&-1!=t?(o=_[t>>2],o+=81920,i=_[t+8>>2],s=0!==_[t+12>>2]):o=2097152,(t=0==i)?i=Ht(16,o):re(0<(i-=o));for(var u=U(228),c=0;c<57;++c)C[(u>>2)+c]=0;return _[e>>2]=u,_[u+12>>2]=u,_[(e=u+152)>>2]=e,n={za:i,Ba:o,Na:t,detached:s,nb:n,Ia:u,Aa:r,ub:a},f?(n.xb=\"spawnThread\",postMessage(n,a),0):ke(n)},I:function(e){throw f?v.ab(e):(v.Za(),Xt(e)),\"unwind\"},J:function(e,t){var n=e,r=t;if(!n)return l(\"pthread", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31087"></a>
## FND-31087 — module-003 import a.L

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "L", "kind": "function", "type_index": 10, "function_index": 36, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 29773, "loader_excerpt": ":_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"!=typeof fetch?Promise.resolve().then(Ee):fetch(p,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file at '\"+p+\"'\"}).catch(Ee)).then(function(e){return WebAssembly.instantiate(e,a)}).then(e,function(e){l(\"failed to asynchronously prepare wasm: \"+e),y(e)})}var a={a:St};if", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31088"></a>
## FND-31088 — module-003 import a.M

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "M", "kind": "function", "type_index": 45, "function_index": 37, "signature": {"parameters": ["i32", "f64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 20804, "loader_excerpt": ",La:_[r+24>>2],Ma:_[r+28>>2],Ib:_[r+32>>2],qb:_[r+36>>2],tb:f?O(f):\"\"},n=O(n),f={\"%c\":\"%a %b %d %H:%M:%S %Y\",\"%D\":\"%m/%d/%y\",\"%F\":\"%Y-%m-%d\",\"%h\":\"%b\",\"%r\":\"%I:%M:%S %p\",\"%R\":\"%H:%M\",\"%T\":\"%H:%M:%S\",\"%x\":\"%m/%d/%y\",\"%X\":\"%H:%M:%S\",\"%Ec\":\"%c\",\"%EC\":\"%C\",\"%Ex\":\"%m/%d/%y\",\"%EX\":\"%H:%M:%S\",\"%Ey\":\"%y\",\"%EY\":\"%Y\",\"%Od\":\"%d\",\"%Oe\":\"%e\",\"%OH\":\"%H\",\"%OI\":\"%I\",\"%Om\":\"%m\",\"%OM\":\"%M\",\"%OS\":\"%S\",\"%Ou\":\"%u\",\"%OU\":\"%U\",\"%OV\":\"%V\",\"%Ow\":\"%w\",\"%OW\":\"%W\",\"%Oy\":\"%y\"})n=n.replace(new RegExp(c,\"g\"),f[c]);var l,d,p=\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\".split(\" \"),m=\"January February March April May June July August September October November December\".split(\" \");for(c in f={\"%a\":function(e){return p[e.La].substring(0,3)},\"%A\":function(e){return p[e.La]},\"%b\":function(e){return m[e.Ca].subst", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31089"></a>
## FND-31089 — module-003 import a.N

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "N", "kind": "function", "type_index": 2, "function_index": 38, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 26518, "loader_excerpt": "ead\",thread:n}):Me(n),0;Ft(),f||Dt(),Te(n,a,f?100:1)}},k:Re,w:je,x:Le,O:function(e){delete Ve[e-1]},N:function(e,t){if(e==t)postMessage({cmd:\"processQueuedMainThreadWork\"});else if(f)postMessage({targetThread:e,cmd:\"processThreadQueue\"});else{if(!(e=(e=v.va[e])&&e.worker))return;e.postMessage({cmd:\"processThreadQueue\"})}return 1},d:Ue,D:function(e,t){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return _[Ut()>>2]=28,-1;e=De()}return _[t>>2]=e/1e3|0,_[t+4>>2]=e%1e3*1e6|0,0},P:function(e,t,n){var r;for(Pe.length=0,n>>=2;r=I[t++];)(r=r<105)&&1&n&&n++,Pe.push(r?oe[n++>>1]:_[n]),++n;return Ae[e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];return(e<0?Ae[-e-1]:Mt[e]).apply(null,", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31090"></a>
## FND-31090 — module-003 import a.O

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "O", "kind": "function", "type_index": 0, "function_index": 39, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 26488, "loader_excerpt": "f?postMessage({cmd:\"cleanupThread\",thread:n}):Me(n),0;Ft(),f||Dt(),Te(n,a,f?100:1)}},k:Re,w:je,x:Le,O:function(e){delete Ve[e-1]},N:function(e,t){if(e==t)postMessage({cmd:\"processQueuedMainThreadWork\"});else if(f)postMessage({targetThread:e,cmd:\"processThreadQueue\"});else{if(!(e=(e=v.va[e])&&e.worker))return;e.postMessage({cmd:\"processThreadQueue\"})}return 1},d:Ue,D:function(e,t){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return _[Ut()>>2]=28,-1;e=De()}return _[t>>2]=e/1e3|0,_[t+4>>2]=e%1e3*1e6|0,0},P:function(e,t,n){var r;for(Pe.length=0,n>>=2;r=I[t++];)(r=r<105)&&1&n&&n++,Pe.push(r?oe[n++>>1]:_[n]),++n;return Ae[e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];return(e", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31091"></a>
## FND-31091 — module-003 import a.P

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "P", "kind": "function", "type_index": 3, "function_index": 40, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 26893, "loader_excerpt": "else{if(1!==e&&4!==e)return _[Ut()>>2]=28,-1;e=De()}return _[t>>2]=e/1e3|0,_[t+4>>2]=e%1e3*1e6|0,0},P:function(e,t,n){var r;for(Pe.length=0,n>>=2;r=I[t++];)(r=r<105)&&1&n&&n++,Pe.push(r?oe[n++>>1]:_[n]),++n;return Ae[e].apply(null,Pe)},E:Ie,n:function(){},r:Be,g:Te,f:xe,h:De,u:function(e,t,n){I.copyWithin(e,t,t+n)},F:function(e,t,n){qe.length=t,n>>=3;for(var r=0;r<t;r++)qe[r]=oe[n+r];return(e<0?Ae[-e-1]:Mt[e]).apply(null,qe)},v:function(){y(\"OOM\")},G:function(e,t,n){return(Ne(e)?He:Ye)(e,t,n)},m:function(){},M:function(e,t,n){return R+=1,setTimeout(function(){--R,j(function(){P.apply(null,[e,n])})},t)},c:function(n){At(function(e){var t;t=e,R+=1,$t(function(){--R,j(t)},n)})},o:function(e,n,t,r,a){function o(e,t){Qe(e,t.response,function(e){--R,j(function(){d?P.apply(null,[d,e]):n&&n(e)},w)", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31092"></a>
## FND-31092 — module-003 import a.a

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
{"module_id": "module-003", "direction": "import", "module": "a", "name": "a", "kind": "memory", "limits": {"flags": 3, "minimum": 8192, "shared": true, "memory64": false, "maximum": 8192}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 999, "loader_excerpt": ")}};return r}),i.postCustomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.forEach(function(e){i.queue.put(e)}),i.queue.process()},i.postMessage=i.postCustomMessage,[]),N=(i.addMessageListener=function(e){W.push(e)},i.removeMessageListener=function(e){0<=(e=W.indexOf(e))&&W.splice(e,1)},i.print=i.printErr=function(e){if(\"Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthrea", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31093"></a>
## FND-31093 — module-003 export Q

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "Q", "kind": "function", "index": 505, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 23980, "loader_excerpt": "=e||0,r=!0,a)&&(b=2,pt(function(){i._asyncify_start_rewind(E)}),\"undefined\"!=typeof Browser&&Browser.Qa.Pa&&Browser.Qa.resume(),n=i.asm[yt[_[E+8>>2]]],--R,t=n(),E||(e=wt,wt=[],e.forEach(function(e){e(t)})))}),a=!0,r||(b=1,e=U(4108),t=e+12,_[e>>2]=t,_[e+4>>2]=t+4096,t=ht[0],void 0===(n=_t[t])&&(n=gt++,_t[t]=n,yt[n]=t),_[e+8>>2]=n,E=e,pt(function(){i._asyncify_start_unwind(E)}),\"undefined\"!=typeof Browser&&Browser.Qa.Pa&&Browser.Qa.pause())):2===b?(b=0,pt(i._asyncify_stop_rewind),A(E),E=null,bt.forEach(function(e){j(e)})):y(\"invalid state: \"+b),mt}f||v.gb(),f||(function(t,n){try{var e=indexedDB.open(\"emscripten_filesystem\",1)}catch(e){return n(e)}e.onupgradeneeded=function(e){(e=e.target.result).objectStoreNames.contains(\"FILES\")&&e.deleteObjectStore(\"FILES\"),e.createObjectStore(\"FILES\")},e.", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31094"></a>
## FND-31094 — module-003 export R

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "R", "kind": "function", "index": 794, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 18326, "loader_excerpt": " 0}}var Ke,Je,$e=[\"default\",\"low-power\",\"high-performance\"],Ze={};function et(){if(!Je){var e,t={USER:\"web_user\",LOGNAME:\"web_user\",PATH:\"/\",PWD:\"/\",HOME:\"/home/web_user\",LANG:(\"object\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:Y||\"./this.program\"};for(e in Ze)void 0===Ze[e]?delete t[e]:t[e]=Ze[e];var n=[];for(e in t)n.push(e+\"=\"+t[e]);Je=n}return Je}function tt(r,a){var o;return f?w(8,1,r,a):(o=0,et().forEach(function(e,t){var n=a+o;for(t=_[r+4*t>>2]=n,n=0;n<e.length;++n)h[t++>>0]=e.charCodeAt(n);h[t>>0]=0,o+=e.length+1}),0)}function nt(e,t){var n,r;return f?w(9,1,e,t):(n=et(),_[e>>2]=n.length,r=0,n.forEach(function(e){r+=e.length+1}),_[t>>2]=r,0)}function rt(e){return f?w(10,1,e):0}function at(e,t,n,r){return f?w(11,1,e,t,n,r):(e=Fe.", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31095"></a>
## FND-31095 — module-003 export S

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "S", "kind": "function", "index": 41, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 568, "loader_excerpt": "\n */!function(){var $t,e,n,t,r,a;function i(){function e(S){var i,k,T,t,n;S=S||{},(i=i||(void 0!==S?S:{})).ready=new Promise(function(e,t){k=e,T=t}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var n,r={open:function(e,t){n=t},send:function(){require(\"fs\").readFile(n,function(e,t){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=t,r.onreadystatechange(),r.onload())})}};return r}),i.postCustomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};va", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31096"></a>
## FND-31096 — module-003 export T

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "T", "kind": "function", "index": 476, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 9317, "loader_excerpt": ",lb:function(e){_[Vt>>2]=0;try{e()}finally{_[Vt>>2]=1}},kb:function(){},pb:function(){for(var e in v.Ta)v.Ta[e]()},Xa:function(a,o){a.onmessage=function(e){var t=e.data,n=t.cmd;if(a.ua&&(v.bb=a.ua.wa),t.targetThread&&t.targetThread!=x()){var r=v.va[t.Hb];r?r.worker.postMessage(e.data,t.transferList):l('Internal error! Worker sent a message \"'+n+'\" to target pthread '+t.targetThread+\", but that thread no longer exists!\")}else if(\"processQueuedMainThreadWork\"===n)Dt();else if(\"spawnThread\"===n)ke(e.data);else if(\"cleanupThread\"===n)Me(t.thread);else if(\"killThread\"===n){if(e=t.thread,f)throw\"Internal Error! killThread() can only ever be called from main application thread!\";if(!e)throw\"Internal Error! Null pthread_ptr in killThread!\";_[e+12>>2]=0,t=v.va[e],delete v.va[e],t.worker.terminate()", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31097"></a>
## FND-31097 — module-003 export U

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "U", "kind": "table", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 20692, "loader_excerpt": ")-1}var c,f=_[r+40>>2];for(c in r={sb:_[r>>2],rb:_[r+4>>2],Ka:_[r+8>>2],Ea:_[r+12>>2],Ca:_[r+16>>2],U:_[r+20>>2],La:_[r+24>>2],Ma:_[r+28>>2],Ib:_[r+32>>2],qb:_[r+36>>2],tb:f?O(f):\"\"},n=O(n),f={\"%c\":\"%a %b %d %H:%M:%S %Y\",\"%D\":\"%m/%d/%y\",\"%F\":\"%Y-%m-%d\",\"%h\":\"%b\",\"%r\":\"%I:%M:%S %p\",\"%R\":\"%H:%M\",\"%T\":\"%H:%M:%S\",\"%x\":\"%m/%d/%y\",\"%X\":\"%H:%M:%S\",\"%Ec\":\"%c\",\"%EC\":\"%C\",\"%Ex\":\"%m/%d/%y\",\"%EX\":\"%H:%M:%S\",\"%Ey\":\"%y\",\"%EY\":\"%Y\",\"%Od\":\"%d\",\"%Oe\":\"%e\",\"%OH\":\"%H\",\"%OI\":\"%I\",\"%Om\":\"%m\",\"%OM\":\"%M\",\"%OS\":\"%S\",\"%Ou\":\"%u\",\"%OU\":\"%U\",\"%OV\":\"%V\",\"%Ow\":\"%w\",\"%OW\":\"%W\",\"%Oy\":\"%y\"})n=n.replace(new RegExp(c,\"g\"),f[c]);var l,d,p=\"Sunday Monday Tuesday Wednesday Thursday Friday Saturday\".split(\" \"),m=\"January February March April May June July August September October November December\".split(\" \");for(c in f={\"%a\":f", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31098"></a>
## FND-31098 — module-003 export V

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "V", "kind": "function", "index": 60, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 17276, "loader_excerpt": "e,r=U(8),_[r+4>>2]=x(),a={Cb:r,attributes:e,version:e.jb,Fa:o},o.canvas&&(o.canvas.Ga=a),(void 0===e.Va||e.Va)&&!(o=(o=a)||Ke).fb){o.fb=!0;var i=t=o.Fa,s=i.getExtension(\"ANGLE_instanced_arrays\"),u=(s&&(i.vertexAttribDivisor=function(e,t){s.vertexAttribDivisorANGLE(e,t)},i.drawArraysInstanced=function(e,t,n,r){s.drawArraysInstancedANGLE(e,t,n,r)},i.drawElementsInstanced=function(e,t,n,r,a){s.drawElementsInstancedANGLE(e,t,n,r,a)}),t),c=u.getExtension(\"OES_vertex_array_object\"),f=(c&&(u.createVertexArray=function(){return c.createVertexArrayOES()},u.deleteVertexArray=function(e){c.deleteVertexArrayOES(e)},u.bindVertexArray=function(e){c.bindVertexArrayOES(e)},u.isVertexArray=function(e){return c.isVertexArrayOES(e)}),t),l=f.getExtension(\"WEBGL_draw_buffers\");l&&(f.drawBuffers=function(e,t){l", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31099"></a>
## FND-31099 — module-003 export W

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "W", "kind": "function", "index": 461, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 2981, "loader_excerpt": "reads\" module is not supported in this node.js build - perhaps a newer version is needed?'),e}global.Worker=d.Worker}else(z||o)&&(o?a=self.location.href:\"undefined\"!=typeof document&&document.currentScript&&(a=document.currentScript.src),a=0!==(a=Jt?Jt:a).indexOf(\"blob:\")?a.substr(0,a.lastIndexOf(\"/\")+1):\"\",s?(X=function(e,t){return r=r||require(\"fs\"),e=(V=V||require(\"path\")).normalize(e),r.readFileSync(e,t?null:\"utf8\")},K=function(e){return re((e=(e=X(e,!0)).buffer?e:new Uint8Array(e)).buffer),e}):(X=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.send(null),t.responseText},o&&(K=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.responseType=\"arraybuffer\",t.send(null),new Uint8Array(t.response)})));s&&\"undefined\"==typeof performance&&(global.performance=req", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31100"></a>
## FND-31100 — module-003 export X

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "X", "kind": "function", "index": 763, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 660, "loader_excerpt": "d 0!==S?S:{})).ready=new Promise(function(e,t){k=e,T=t}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var n,r={open:function(e,t){n=t},send:function(){require(\"fs\").readFile(n,function(e,t){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=t,r.onreadystatechange(),r.onload())})}};return r}),i.postCustomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.fo", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31101"></a>
## FND-31101 — module-003 export Y

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "Y", "kind": "function", "index": 762, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 14284, "loader_excerpt": "r(e):void 0)}function He(e,t,n){var r,a,o,i,s=Ne(e);return s?(s.Ha&&(_[s.Ha>>2]=t,_[s.Ha+4>>2]=n),!s.Ya&&s.yb?s.Ha?(s=_[s.Ha+8>>2],e=e?O(e):\"\",r=Bt(),a=Wt(12),o=0,e&&(o=ue(e)+1,i=U(o),F(e,I,i,o),o=i),_[a>>2]=o,_[a+4>>2]=t,_[a+8>>2]=n,Ot(0,s,657457152,0,o,a),qt(r),1):-4:(e=!1,(s=s.Ya?s.Ya:s).Ga&&s.Ga.Fa&&(e=0===(e=s.Ga.Fa.getParameter(2978))[0]&&0===e[1]&&e[2]===s.width&&e[3]===s.height),s.width=t,s.height=n,e&&s.Ga.Fa.viewport(0,0,t,n),0)):-4}function Ye(e,t,n){return f?w(7,1,e,t,n):He(e,t,n)}function j(e,t){if(!c)if(t)e();else{try{e()}catch(e){if(e instanceof M)return;if(\"unwind\"!==e)throw e&&\"object\"==typeof e&&e.stack&&l(\"exception thrown: \"+[e,e.stack]),e}if(!_e())try{(f?Rt:Xt)(ne)}catch(e){if(!(e instanceof M))throw e}}}var Ge,Ve=[];function L(e,t){C[e>>2]=t,C[e+4>>2]=t/4294967296|0}f", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31102"></a>
## FND-31102 — module-003 export Z

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "Z", "kind": "function", "index": 761, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 7, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 13590, "loader_excerpt": "tion(){return performance.now()},Ce=[null,[],[]];function Oe(e,t){var n=Ce[e];0===t||10===t?((1===e?Z:l)(se(n,0)),n.length=0):n.push(t)}var Fe={};function Re(e,t,n){return f?w(2,1,e,t,n):0}function je(e,t,n){return f?w(3,1,e,t,n):0}function Le(e,t,n){if(f)return w(4,1,e,t,n)}function Ue(){if(f)return w(5,1);y()}var Pe=[];function Be(e){if(f)return w(6,1,e);ee=!1,R=0,Xt(e)}function w(e,t){for(var n=arguments.length-2,r=Bt(),a=Wt(8*n),o=a>>3,i=0;i<n;i++)oe[o+i]=arguments[2+i];return n=Ct(e,n,a,t),qt(r),n}var qe=[],We=[0,\"undefined\"!=typeof document?document:0,\"undefined\"!=typeof window?window:0];function Ne(e){return e=2<e?O(e):e,We[e]||(\"undefined\"!=typeof document?document.querySelector(e):void 0)}function He(e,t,n){var r,a,o,i,s=Ne(e);return s?(s.Ha&&(_[s.Ha>>2]=t,_[s.Ha+4>>2]=n),!s.Ya&&s", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31103"></a>
## FND-31103 — module-003 export _

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "_", "kind": "function", "index": 297, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 18507, "loader_excerpt": "ect\"==typeof navigator&&navigator.languages&&navigator.languages[0]||\"C\").replace(\"-\",\"_\")+\".UTF-8\",_:Y||\"./this.program\"};for(e in Ze)void 0===Ze[e]?delete t[e]:t[e]=Ze[e];var n=[];for(e in t)n.push(e+\"=\"+t[e]);Je=n}return Je}function tt(r,a){var o;return f?w(8,1,r,a):(o=0,et().forEach(function(e,t){var n=a+o;for(t=_[r+4*t>>2]=n,n=0;n<e.length;++n)h[t++>>0]=e.charCodeAt(n);h[t>>0]=0,o+=e.length+1}),0)}function nt(e,t){var n,r;return f?w(9,1,e,t):(n=et(),_[e>>2]=n.length,r=0,n.forEach(function(e){r+=e.length+1}),_[t>>2]=r,0)}function rt(e){return f?w(10,1,e):0}function at(e,t,n,r){return f?w(11,1,e,t,n,r):(e=Fe.Bb(e),t=Fe.Ab(e,t,n),_[r>>2]=t,0)}function ot(e,t,n,r,a){if(f)return w(12,1,e,t,n,r,a)}function it(e,t,n,r){if(f)return w(13,1,e,t,n,r);for(var a=0,o=0;o<n;o++){for(var i=_[t+8*o>>2", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31104"></a>
## FND-31104 — module-003 export $

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "$", "kind": "function", "index": 760, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["f64"]}, "type_index": 74, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 8631, "loader_excerpt": ".store(C,e+0>>2,1),xe(e+0,2147483647),jt(0,0,0)},mb:function(e){ne=e},ab:function(e){var t=x();t&&(v.$a(t,e),f)&&postMessage({cmd:\"exit\"})},ob:function(){v.$a(x(),-1),postMessage({cmd:\"cancelDone\"})},Ra:function(){for(var e in v.va){var t=v.va[e];t&&t.worker&&v.Ja(t.worker)}for(v.va={},e=0;e<v.xa.length;++e){var n=v.xa[e];n.terminate()}for(v.xa=[],e=0;e<v.ya.length;++e)t=(n=v.ya[e]).ua,v.Oa(t),n.terminate();v.ya=[]},Oa:function(e){var t;e&&(e.wa&&(t=_[e.wa+100>>2],_[e.wa+100>>2]=0,A(t),A(e.wa)),e.wa=0,e.Na&&e.za&&A(e.za),e.za=0,e.worker)&&(e.worker.ua=null)},Ja:function(e){v.lb(function(){delete v.va[e.ua.wa],v.xa.push(e),v.ya.splice(v.ya.indexOf(e),1),v.Oa(e.ua),e.ua=void 0})},lb:function(e){_[Vt>>2]=0;try{e()}finally{_[Vt>>2]=1}},kb:function(){},pb:function(){for(var e in v.Ta)v.Ta[e]()}", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31105"></a>
## FND-31105 — module-003 export aa

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "aa", "kind": "function", "index": 758, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 5, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 32295, "loader_excerpt": "rguments)},Ot=i.__emscripten_call_on_thread=function(){return(Ot=i.__emscripten_call_on_thread=i.asm.aa).apply(null,arguments)},Ft=i._pthread_testcancel=function(){return(Ft=i._pthread_testcancel=i.asm.ba).apply(null,arguments)},x=i._pthread_self=function(){return(x=i._pthread_self=i.asm.ca).apply(null,arguments)},Rt=i._pthread_exit=function(){return(Rt=i._pthread_exit=i.asm.da).apply(null,arguments)},jt=i.__emscripten_thread_init=function(){return(jt=i.__emscripten_thread_init=i.asm.ea).apply(null,arguments)},Lt=i._emscripten_get_global_libc=function(){return(Lt=i._emscripten_get_global_libc=i.asm.fa).apply(null,arguments)},Ut=i.___errno_location=function(){return(Ut=i.___errno_location=i.asm.ga).apply(null,arguments)},Pt=i.___pthread_tsd_run_dtors=function(){return(Pt=i.___pthread_tsd_ru", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31106"></a>
## FND-31106 — module-003 export ba

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ba", "kind": "function", "index": 239, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 32396, "loader_excerpt": "aa).apply(null,arguments)},Ft=i._pthread_testcancel=function(){return(Ft=i._pthread_testcancel=i.asm.ba).apply(null,arguments)},x=i._pthread_self=function(){return(x=i._pthread_self=i.asm.ca).apply(null,arguments)},Rt=i._pthread_exit=function(){return(Rt=i._pthread_exit=i.asm.da).apply(null,arguments)},jt=i.__emscripten_thread_init=function(){return(jt=i.__emscripten_thread_init=i.asm.ea).apply(null,arguments)},Lt=i._emscripten_get_global_libc=function(){return(Lt=i._emscripten_get_global_libc=i.asm.fa).apply(null,arguments)},Ut=i.___errno_location=function(){return(Ut=i.___errno_location=i.asm.ga).apply(null,arguments)},Pt=i.___pthread_tsd_run_dtors=function(){return(Pt=i.___pthread_tsd_run_dtors=i.asm.ha).apply(null,arguments)},Bt=i.stackSave=function(){return(Bt=i.stackSave=i.asm.ia).ap", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31107"></a>
## FND-31107 — module-003 export ca

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ca", "kind": "function", "index": 750, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 4259, "loader_excerpt": "this.decode=function(e){return e.buffer instanceof SharedArrayBuffer&&(e=new Uint8Array(e)),t.decode.call(t,e)}}var h,I,D,_,C,oe,ie=\"undefined\"!=typeof TextDecoder?new ae(\"utf8\"):void 0;function se(e,t,n){var r=t+n;for(n=t;e[n]&&!(r<=n);)++n;if(16<n-t&&e.subarray&&ie)return ie.decode(e.subarray(t,n));for(r=\"\";t<n;){var a,o,i=e[t++];128&i?(a=63&e[t++],192==(224&i)?r+=String.fromCharCode((31&i)<<6|a):(o=63&e[t++],(i=224==(240&i)?(15&i)<<12|a<<6|o:(7&i)<<18|a<<12|o<<6|63&e[t++])<65536?r+=String.fromCharCode(i):(i-=65536,r+=String.fromCharCode(55296|i>>10,56320|1023&i)))):r+=String.fromCharCode(i)}return r}function O(e){return e?se(I,e,void 0):\"\"}function F(e,t,n,r){if(0<r){r=n+r-1;for(var a=0;a<e.length;++a){var o=e.charCodeAt(a);if((o=55296<=o&&o<=57343?65536+((1023&o)<<10)|1023&e.charCodeAt", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31108"></a>
## FND-31108 — module-003 export da

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "da", "kind": "function", "index": 756, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 9380, "loader_excerpt": "tion(){},pb:function(){for(var e in v.Ta)v.Ta[e]()},Xa:function(a,o){a.onmessage=function(e){var t=e.data,n=t.cmd;if(a.ua&&(v.bb=a.ua.wa),t.targetThread&&t.targetThread!=x()){var r=v.va[t.Hb];r?r.worker.postMessage(e.data,t.transferList):l('Internal error! Worker sent a message \"'+n+'\" to target pthread '+t.targetThread+\", but that thread no longer exists!\")}else if(\"processQueuedMainThreadWork\"===n)Dt();else if(\"spawnThread\"===n)ke(e.data);else if(\"cleanupThread\"===n)Me(t.thread);else if(\"killThread\"===n){if(e=t.thread,f)throw\"Internal Error! killThread() can only ever be called from main application thread!\";if(!e)throw\"Internal Error! Null pthread_ptr in killThread!\";_[e+12>>2]=0,t=v.va[e],delete v.va[e],t.worker.terminate(),v.Oa(t),v.ya.splice(v.ya.indexOf(t.worker),1),t.worker.ua=void", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31109"></a>
## FND-31109 — module-003 export ea

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ea", "kind": "function", "index": 725, "signature": {"parameters": ["i32", "i32", "i32"], "results": []}, "type_index": 8, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 32683, "loader_excerpt": "null,arguments)},jt=i.__emscripten_thread_init=function(){return(jt=i.__emscripten_thread_init=i.asm.ea).apply(null,arguments)},Lt=i._emscripten_get_global_libc=function(){return(Lt=i._emscripten_get_global_libc=i.asm.fa).apply(null,arguments)},Ut=i.___errno_location=function(){return(Ut=i.___errno_location=i.asm.ga).apply(null,arguments)},Pt=i.___pthread_tsd_run_dtors=function(){return(Pt=i.___pthread_tsd_run_dtors=i.asm.ha).apply(null,arguments)},Bt=i.stackSave=function(){return(Bt=i.stackSave=i.asm.ia).apply(null,arguments)},qt=i.stackRestore=function(){return(qt=i.stackRestore=i.asm.ja).apply(null,arguments)},Wt=i.stackAlloc=function(){return(Wt=i.stackAlloc=i.asm.ka).apply(null,arguments)},Nt=i._emscripten_stack_set_limits=function(){return(Nt=i._emscripten_stack_set_limits=i.asm.la).", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31110"></a>
## FND-31110 — module-003 export fa

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "fa", "kind": "function", "index": 755, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 32800, "loader_excerpt": "rguments)},Lt=i._emscripten_get_global_libc=function(){return(Lt=i._emscripten_get_global_libc=i.asm.fa).apply(null,arguments)},Ut=i.___errno_location=function(){return(Ut=i.___errno_location=i.asm.ga).apply(null,arguments)},Pt=i.___pthread_tsd_run_dtors=function(){return(Pt=i.___pthread_tsd_run_dtors=i.asm.ha).apply(null,arguments)},Bt=i.stackSave=function(){return(Bt=i.stackSave=i.asm.ia).apply(null,arguments)},qt=i.stackRestore=function(){return(qt=i.stackRestore=i.asm.ja).apply(null,arguments)},Wt=i.stackAlloc=function(){return(Wt=i.stackAlloc=i.asm.ka).apply(null,arguments)},Nt=i._emscripten_stack_set_limits=function(){return(Nt=i._emscripten_stack_set_limits=i.asm.la).apply(null,arguments)},Ht=i._memalign=function(){return(Ht=i._memalign=i.asm.ma).apply(null,arguments)},P=i.dynCall_v", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31111"></a>
## FND-31111 — module-003 export ga

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ga", "kind": "function", "index": 754, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 32897, "loader_excerpt": "asm.fa).apply(null,arguments)},Ut=i.___errno_location=function(){return(Ut=i.___errno_location=i.asm.ga).apply(null,arguments)},Pt=i.___pthread_tsd_run_dtors=function(){return(Pt=i.___pthread_tsd_run_dtors=i.asm.ha).apply(null,arguments)},Bt=i.stackSave=function(){return(Bt=i.stackSave=i.asm.ia).apply(null,arguments)},qt=i.stackRestore=function(){return(qt=i.stackRestore=i.asm.ja).apply(null,arguments)},Wt=i.stackAlloc=function(){return(Wt=i.stackAlloc=i.asm.ka).apply(null,arguments)},Nt=i._emscripten_stack_set_limits=function(){return(Nt=i._emscripten_stack_set_limits=i.asm.la).apply(null,arguments)},Ht=i._memalign=function(){return(Ht=i._memalign=i.asm.ma).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.na).apply(null,arguments)},Yt=i.dynCall_ii=function(){re", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31112"></a>
## FND-31112 — module-003 export ha

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ha", "kind": "function", "index": 535, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 29440, "loader_excerpt": "e(e)+1,n=U(t);return F(e,I,n,t),n},At(function(e){t().then(e)});var t},H:function(e,t){return t={alpha:!!_[t>>=2],depth:!!_[t+1],stencil:!!_[t+2],antialias:!!_[t+3],premultipliedAlpha:!!_[t+4],preserveDrawingBuffer:!!_[t+5],powerPreference:$e[_[t+6]],failIfMajorPerformanceCaveat:!!_[t+7],jb:_[t+8],Db:_[t+9],Va:_[t+10],cb:_[t+11],Fb:_[t+12],Gb:_[t+13]},!(e=Ne(e))||t.cb?0:Xe(e,t)},B:tt,C:nt,i:function(e){Xt(e)},l:rt,z:at,t:ot,y:it,L:function(){v.hb()},a:u||i.wasmMemory,s:function(){i.pauseQueue()},A:dt,j:function(){i.unpauseQueue()}},A=(!function(){function t(e,t){var n;e=Et(e=e.exports),i.asm=e,de.unshift(i.asm.Q),v.Ta.push(i.asm.T),te=t,f||(n=v.xa.length,v.xa.forEach(function(e){v.Xa(e,function(){--n||we()})}))}function n(e){t(e.instance,e.module)}function r(e){return($||!z&&!o||\"function\"", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31113"></a>
## FND-31113 — module-003 export ia

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ia", "kind": "function", "index": 766, "signature": {"parameters": [], "results": ["i32"]}, "type_index": 14, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33089, "loader_excerpt": "tsd_run_dtors=i.asm.ha).apply(null,arguments)},Bt=i.stackSave=function(){return(Bt=i.stackSave=i.asm.ia).apply(null,arguments)},qt=i.stackRestore=function(){return(qt=i.stackRestore=i.asm.ja).apply(null,arguments)},Wt=i.stackAlloc=function(){return(Wt=i.stackAlloc=i.asm.ka).apply(null,arguments)},Nt=i._emscripten_stack_set_limits=function(){return(Nt=i._emscripten_stack_set_limits=i.asm.la).apply(null,arguments)},Ht=i._memalign=function(){return(Ht=i._memalign=i.asm.ma).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.na).apply(null,arguments)},Yt=i.dynCall_ii=function(){return(Yt=i.dynCall_ii=i.asm.oa).apply(null,arguments)},Gt=i.dynCall_v=function(){return(Gt=i.dynCall_v=i.asm.pa).apply(null,arguments)},Vt=(i._asyncify_start_unwind=function(){return(i._asyncif", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31114"></a>
## FND-31114 — module-003 export ja

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ja", "kind": "function", "index": 764, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33176, "loader_excerpt": "ackSave=i.asm.ia).apply(null,arguments)},qt=i.stackRestore=function(){return(qt=i.stackRestore=i.asm.ja).apply(null,arguments)},Wt=i.stackAlloc=function(){return(Wt=i.stackAlloc=i.asm.ka).apply(null,arguments)},Nt=i._emscripten_stack_set_limits=function(){return(Nt=i._emscripten_stack_set_limits=i.asm.la).apply(null,arguments)},Ht=i._memalign=function(){return(Ht=i._memalign=i.asm.ma).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.na).apply(null,arguments)},Yt=i.dynCall_ii=function(){return(Yt=i.dynCall_ii=i.asm.oa).apply(null,arguments)},Gt=i.dynCall_v=function(){return(Gt=i.dynCall_v=i.asm.pa).apply(null,arguments)},Vt=(i._asyncify_start_unwind=function(){return(i._asyncify_start_unwind=i.asm.qa).apply(null,arguments)},i._asyncify_stop_unwind=function(){retu", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31115"></a>
## FND-31115 — module-003 export ka

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ka", "kind": "function", "index": 759, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 1, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33259, "loader_excerpt": "tackRestore=i.asm.ja).apply(null,arguments)},Wt=i.stackAlloc=function(){return(Wt=i.stackAlloc=i.asm.ka).apply(null,arguments)},Nt=i._emscripten_stack_set_limits=function(){return(Nt=i._emscripten_stack_set_limits=i.asm.la).apply(null,arguments)},Ht=i._memalign=function(){return(Ht=i._memalign=i.asm.ma).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.na).apply(null,arguments)},Yt=i.dynCall_ii=function(){return(Yt=i.dynCall_ii=i.asm.oa).apply(null,arguments)},Gt=i.dynCall_v=function(){return(Gt=i.dynCall_v=i.asm.pa).apply(null,arguments)},Vt=(i._asyncify_start_unwind=function(){return(i._asyncify_start_unwind=i.asm.qa).apply(null,arguments)},i._asyncify_stop_unwind=function(){return(i._asyncify_stop_unwind=i.asm.ra).apply(null,arguments)},i._asyncify_start_rewin", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31116"></a>
## FND-31116 — module-003 export la

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "la", "kind": "function", "index": 682, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 3166, "loader_excerpt": "cument.currentScript&&(a=document.currentScript.src),a=0!==(a=Jt?Jt:a).indexOf(\"blob:\")?a.substr(0,a.lastIndexOf(\"/\")+1):\"\",s?(X=function(e,t){return r=r||require(\"fs\"),e=(V=V||require(\"path\")).normalize(e),r.readFileSync(e,t?null:\"utf8\")},K=function(e){return re((e=(e=X(e,!0)).buffer?e:new Uint8Array(e)).buffer),e}):(X=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.send(null),t.responseText},o&&(K=function(e){var t=new XMLHttpRequest;return t.open(\"GET\",e,!1),t.responseType=\"arraybuffer\",t.send(null),new Uint8Array(t.response)})));s&&\"undefined\"==typeof performance&&(global.performance=require(\"perf_hooks\").performance);var J,$,Z=i.print||console.log.bind(console),l=i.printErr||console.warn.bind(console);for(e in N)N.hasOwnProperty(e)&&(i[e]=N[e]);N=null,i.arguments&&(H=", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31117"></a>
## FND-31117 — module-003 export ma

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ma", "kind": "function", "index": 322, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 11129, "loader_excerpt": "(\"error\",function(e){a.onerror(e)}),a.on(\"exit\",function(){})),a.postMessage({cmd:\"load\",urlOrBlob:i.mainScriptUrlOrBlob||Jt,wasmMemory:u,wasmModule:te})},Ua:function(){var e=Q(\"stockfish.worker.js\");v.xa.push(new Worker(e))},eb:function(){return 0==v.xa.length&&(v.Ua(),v.Xa(v.xa[0])),v.xa.pop()},wb:function(e){for(e=performance.now()+e;performance.now()<e;);}};function Se(e,t){if(f)return w(1,1,e,t);me.unshift({Pa:e,Aa:t})}function ke(e){if(f)throw\"Internal Error! spawnThread() can only ever be called from main application thread!\";var t=v.eb();if(!t)return 6;if(void 0!==t.ua)throw\"Internal error!\";if(!e.Ia)throw\"Internal error, no pthread ptr!\";v.ya.push(t);for(var n=U(512),r=0;r<128;++r)_[n+4*r>>2]=0;var a=e.za+e.Ba,o=(r=v.va[e.Ia]={worker:t,za:e.za,Ba:e.Ba,Na:e.Na,wa:e.Ia}).wa>>2,i=(At", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31118"></a>
## FND-31118 — module-003 export na

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "na", "kind": "function", "index": 519, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 4, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33540, "loader_excerpt": "t=i._memalign=i.asm.ma).apply(null,arguments)},P=i.dynCall_vi=function(){return(P=i.dynCall_vi=i.asm.na).apply(null,arguments)},Yt=i.dynCall_ii=function(){return(Yt=i.dynCall_ii=i.asm.oa).apply(null,arguments)},Gt=i.dynCall_v=function(){return(Gt=i.dynCall_v=i.asm.pa).apply(null,arguments)},Vt=(i._asyncify_start_unwind=function(){return(i._asyncify_start_unwind=i.asm.qa).apply(null,arguments)},i._asyncify_stop_unwind=function(){return(i._asyncify_stop_unwind=i.asm.ra).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.sa).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.ta).apply(null,arguments)},i.__emscripten_allow_main_runtime_queued_calls=29752),zt=i.__emscripten_main_thread_futex=1246688;functi", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31119"></a>
## FND-31119 — module-003 export oa

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "oa", "kind": "function", "index": 518, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33623, "loader_excerpt": ".dynCall_vi=i.asm.na).apply(null,arguments)},Yt=i.dynCall_ii=function(){return(Yt=i.dynCall_ii=i.asm.oa).apply(null,arguments)},Gt=i.dynCall_v=function(){return(Gt=i.dynCall_v=i.asm.pa).apply(null,arguments)},Vt=(i._asyncify_start_unwind=function(){return(i._asyncify_start_unwind=i.asm.qa).apply(null,arguments)},i._asyncify_stop_unwind=function(){return(i._asyncify_stop_unwind=i.asm.ra).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.sa).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.ta).apply(null,arguments)},i.__emscripten_allow_main_runtime_queued_calls=29752),zt=i.__emscripten_main_thread_futex=1246688;function M(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",t", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31120"></a>
## FND-31120 — module-003 export pa

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "pa", "kind": "function", "index": 516, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 1283, "loader_excerpt": ".length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.forEach(function(e){i.queue.put(e)}),i.queue.process()},i.postMessage=i.postCustomMessage,[]),N=(i.addMessageListener=function(e){W.push(e)},i.removeMessageListener=function(e){0<=(e=W.indexOf(e))&&W.splice(e,1)},i.print=i.printErr=function(e){if(\"Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread\"!==e){if(0===W.length)return console.log(e);for(var t of W)t(e)}},i.terminate=function(){v.Ra()},i.__IS_NON_NESTED__=!0,{});for(e in i)i.hasOwnProperty(e)&&(N[e]=i[e]);var H=[],Y=\"./this.program\";function G(e,t){if(0!==e)throw t}var r,V,z=\"", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31121"></a>
## FND-31121 — module-003 export qa

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "qa", "kind": "function", "index": 515, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33809, "loader_excerpt": "apply(null,arguments)},Vt=(i._asyncify_start_unwind=function(){return(i._asyncify_start_unwind=i.asm.qa).apply(null,arguments)},i._asyncify_stop_unwind=function(){return(i._asyncify_stop_unwind=i.asm.ra).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.sa).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.ta).apply(null,arguments)},i.__emscripten_allow_main_runtime_queued_calls=29752),zt=i.__emscripten_main_thread_futex=1246688;function M(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",this.status=e}function Qt(o){function e(){if(!xt&&(xt=!0,i.calledRun=!0,!c)){if(f||g(de),f||g(pe),k(i),i.onRuntimeInitialized&&i.onRuntimeInitialized(),Kt){var t=o,e=i._main,n=(t=t||[]).l", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31122"></a>
## FND-31122 — module-003 export ra

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ra", "kind": "function", "index": 514, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 33908, "loader_excerpt": "m.qa).apply(null,arguments)},i._asyncify_stop_unwind=function(){return(i._asyncify_stop_unwind=i.asm.ra).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.sa).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.ta).apply(null,arguments)},i.__emscripten_allow_main_runtime_queued_calls=29752),zt=i.__emscripten_main_thread_futex=1246688;function M(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",this.status=e}function Qt(o){function e(){if(!xt&&(xt=!0,i.calledRun=!0,!c)){if(f||g(de),f||g(pe),k(i),i.onRuntimeInitialized&&i.onRuntimeInitialized(),Kt){var t=o,e=i._main,n=(t=t||[]).length+1,r=Wt(4*(n+1));_[r>>2]=ce(Y);for(var a=1;a<n;a++)_[(r>>2)+a]=ce(t[a-1]);_[(r>>2)+n]=0;try{Xt", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31123"></a>
## FND-31123 — module-003 export sa

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "sa", "kind": "function", "index": 513, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 34009, "loader_excerpt": "ra).apply(null,arguments)},i._asyncify_start_rewind=function(){return(i._asyncify_start_rewind=i.asm.sa).apply(null,arguments)},i._asyncify_stop_rewind=function(){return(i._asyncify_stop_rewind=i.asm.ta).apply(null,arguments)},i.__emscripten_allow_main_runtime_queued_calls=29752),zt=i.__emscripten_main_thread_futex=1246688;function M(e){this.name=\"ExitStatus\",this.message=\"Program terminated with exit(\"+e+\")\",this.status=e}function Qt(o){function e(){if(!xt&&(xt=!0,i.calledRun=!0,!c)){if(f||g(de),f||g(pe),k(i),i.onRuntimeInitialized&&i.onRuntimeInitialized(),Kt){var t=o,e=i._main,n=(t=t||[]).length+1,r=Wt(4*(n+1));_[r>>2]=ce(Y);for(var a=1;a<n;a++)_[(r>>2)+a]=ce(t[a-1]);_[(r>>2)+n]=0;try{Xt(e(n,r),!0)}catch(e){e instanceof M||\"unwind\"==e||((t=e)&&\"object\"==typeof e&&e.stack&&(t=[e,e.stack]", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31124"></a>
## FND-31124 — module-003 export ta

Runtime/engine export; semantic identity requires wrapper/call-site evidence.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3018, SRC-3019
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-31046
- [Exact supporting artifact](../wasm-analysis/modules/module-003/imports-exports-annotated.json)

```text
{"module_id": "module-003", "direction": "export", "name": "ta", "kind": "function", "index": 512, "signature": {"parameters": [], "results": []}, "type_index": 10, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 998, "loader_excerpt": "})}};return r}),i.postCustomMessage=function(e){for(var t of v.ya)t.postMessage({cmd:\"custom\",userData:e})},i.queue=(n=[],{get:async function(){return!B&&0<n.length?n.shift():await new Promise(function(e){return t=e})},put:function(e){t?(t(e),t=null):n.push(e)},process:function(){t&&n.length&&t(n.shift())}}),i.onCustomMessage=function(e){B?q.push(e):i.queue.put(e)};var B,e,q=[],W=(i.pauseQueue=function(){B=!0},i.unpauseQueue=function(){var e=q;B=!(q=[]),e.forEach(function(e){i.queue.put(e)}),i.queue.process()},i.postMessage=i.postCustomMessage,[]),N=(i.addMessageListener=function(e){W.push(e)},i.removeMessageListener=function(e){0<=(e=W.indexOf(e))&&W.splice(e,1)},i.print=i.printErr=function(e){if(\"Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthre", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31125"></a>
## FND-31125 — module-004 complete structural inventory

574106bytes; SHA256198c952007aa12b24aa649525f049f9508178fbfd5a3298810d7e87d91229a04; 709defined functions,22imported functions,16exports. All section offsets,types,limits,globals,elements,data and function body spans retained.

- Category: wasm_structure
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../wasm-analysis/modules/module-004/structure.json)

```text
Magic0061736d;version1;no custom sections.
```

<a id="FND-31126"></a>
## FND-31126 — module-004 function and call-graph analysis

1898direct caller/callee pairs;4312static direct-call sites;655indirect-call sites. Exact direct call indices recovered from full WAT. Indirect dispatch targets not resolved; opcode frequencies are syntactic counts,not execution profiling.

- Category: wasm_functions
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/functions.json)

```text
See call-graph.jsonl.gz and opcode-statistics.json.
```

<a id="FND-31127"></a>
## FND-31127 — module-004 strings and data offsets

812ASCII candidates,42keyword-relevant candidates,8UTF16candidates. Strings linked to original file offsets and active data memory addresses when constant-resolvable. Random code/weight bytes can resemble text.

- Category: wasm_strings
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/strings.txt)

```text
All-ASCII candidates are separately gzipped; relevant output is not a semantic analysis of every string.
```

<a id="FND-31128"></a>
## FND-31128 — module-004 memory/host boundary

{"defined_memories": [{"flags": 1, "minimum": 1024, "shared": false, "memory64": false, "maximum": 32768}], "imported_memories": [], "tables": [{"element_type": "funcref", "limits": {"flags": 1, "minimum": 460, "shared": false, "memory64": false, "maximum": 460}}], "data_segments": 93}

- Category: wasm_memory
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/structure.json)

```text
Memory limits use64KiBpages; shared flag is explicit.
```

<a id="FND-31129"></a>
## FND-31129 — module-004 new controlled instantiation

Bounded Node instantiation succeeded with explicitly stubbed imports; this is not engine search/review correctness. Initial module003failed due unhandled imported memory,then passed using exact descriptor limits. Stack-query exports were called only when present.

- Category: wasm_runtime
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3020
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No native whole-game review rerun,new server query,or cloud parity test. Historical successful full CEE/Human tests retained separately.
- Related findings: FND-31125
- [Exact supporting artifact](../wasm-analysis/modules/module-004/runtime-observation.json)

```text
{"status": "instantiated with function import stubs", "imports": 22, "exports": 16, "memories": [{"name": "w", "bytes": 67108864, "shared": false}], "import_calls_during_instantiation": [], "elapsed_ms": 8.83601, "algorithm_calls": [], "limitation": "No wrapper runtime constructors/search/review invoked; stub instantiation is not a functional engine validation. No original application inputs used."}
```

<a id="FND-31130"></a>
## FND-31130 — module-004 import a.a

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "a", "kind": "function", "type_index": 11, "function_index": 0, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 1175, "loader_excerpt": "nction(e){if(\"undefined\"!=typeof PThread)for(var n of PThread.ba)n.postMessage({cmd:\"custom\",userData:e})},i.queue=(t=[],{get:async function(){return 0<t.length?t.shift():await new Promise(function(e){return n=e})},put:function(e){n?(n(e),n=null):t.push(e)}}),i.onCustomMessage=function(e){A?H.push(e):i.queue.put(e)};var A,r,H=[],o=(i.pauseQueue=function(){A=!0},i.unpauseQueue=function(){var e=H;A=!(H=[]),e.forEach(function(e){i.queue.put(e)})},i.postMessage=i.postCustomMessage,[]),a=(i.addMessageListener=function(e){o.push(e)},i.removeMessageListener=function(e){0<=(e=o.indexOf(e))&&o.splice(e,1)},i.print=i.printErr=function(e){if(0===o.length)return console.log(e);for(var n of o)n(e)},i.terminate=function(){\"undefined\"!=typeof PThread&&PThread.da()},i.__IS_SINGLE_THREADED__=!0,i._origOnCu", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31131"></a>
## FND-31131 — module-004 import a.b

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "b", "kind": "function", "type_index": 0, "function_index": 1, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 3071, "loader_excerpt": "peof document&&document.currentScript&&(p=document.currentScript.src),p=0!==(p=Xe?Xe:p).indexOf(\"blob:\")?p.substr(0,p.lastIndexOf(\"/\")+1):\"\",Y=function(e){var n=new XMLHttpRequest;return n.open(\"GET\",e,!1),n.send(null),n.responseText},l)&&(c=function(e){var n=new XMLHttpRequest;return n.open(\"GET\",e,!1),n.responseType=\"arraybuffer\",n.send(null),new Uint8Array(n.response)}),i.print||console.log.bind(console)),d=i.printErr||console.warn.bind(console);for(r in a)a.hasOwnProperty(r)&&(i[r]=a[r]);a=null,i.arguments&&(N=i.arguments),i.thisProgram&&(u=i.thisProgram),i.quit&&(s=i.quit),i.wasmBinary&&(f=i.wasmBinary);var V=i.noExitRuntime||!0;\"object\"!=typeof WebAssembly&&_(\"no native wasm support detected\");var z,K,y,C,x,g,O,m=!1,J=\"undefined\"!=typeof TextDecoder?new TextDecoder(\"utf8\"):void 0;fun", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31132"></a>
## FND-31132 — module-004 import a.c

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "c", "kind": "function", "type_index": 0, "function_index": 2, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 17260, "loader_excerpt": "on(e,n){var t=_e(),r=(g[e>>2]=t.length,0);return t.forEach(function(e){r+=e.length+1}),g[n>>2]=r,0},c:function(e){Be(e)},g:function(){return 0},s:function(e,n,t,r){return e=de.aa(e),n=de.$(e,n,t),g[r>>2]=n,0},n:function(){},r:function(e,n,t,r){for(var o=0,a=0;a<t;a++){for(var i=g[n+8*a>>2],u=g[n+(8*a+4)>>2],s=0;s<u;s++){var c=C[i+s],f=pe[e];0===c||10===c?((1===e?X:d)(Q(f,0)),f.length=0):f.push(c)}o+=u}return g[r>>2]=o,0},m:function(){i.pauseQueue()},t:Ee,e:function(){i.unpauseQueue()}},Pe=(!function(){function n(e){e=Le(e=e.exports),i.asm=e,z=i.asm.w,ee(),re.unshift(i.asm.x),ce()}function t(e){n(e.instance)}function r(e){return(f||!B&&!l||\"function\"!=typeof fetch?Promise.resolve().then(le):fetch(h,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to ", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31133"></a>
## FND-31133 — module-004 import a.d

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "d", "kind": "function", "type_index": 1, "function_index": 3, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 725, "loader_excerpt": "ined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var t,r={open:function(e,n){t=n},send:function(){require(\"fs\").readFile(t,function(e,n){r.readyState=4,e?(console.error(e),r.status=404,r.onerror(e)):(r.status=200,r.response=n,r.onreadystatechange(),r.onload())})}};return r}),\"undefined\"!=typeof global&&\"[object process]\"===Object.prototype.toString.call(global.process)&&\"undefined\"!=typeof fetch&&(fetch=null),i.postCustomMessage=function(e){if(\"undefined\"!=typeof PThread)for(var n of PThread.ba)n.postMessage({cmd:\"custom\",userData:e})},i.queue=(t=[],{get:async function(){return 0<t.length?t.shift():await new Promise(function(e){return n=e})},put:function(e){n?(n(e),n=null):t.push(e)}}),i.onCustomMessage=function(e){A?H.push(e):i.queue.put(e)};var A,r,H=[],o=(i.pauseQueue=fun", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31134"></a>
## FND-31134 — module-004 import a.e

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "e", "kind": "function", "type_index": 11, "function_index": 4, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 99, "loader_excerpt": "/*!\n * Stockfish.js 16 (c) 2023, Chess.com, LLC\n * https://github.com/nmrugg/stockfish.js\n * License: GPLv3\n *\n * Based on stockfish.wasm (c)\n * Niklas Fiekas <niklas.fiekas@backscattering.de>\n * Hiroshi Ogawa <hi.ogawa.zz@gmail.com>\n * https://github.com/niklasf/stockfish.wasm\n * https://github.com/hi-ogawa/Stockfish\n *\n * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.\n * https://github.com/official-stockfish/Stockfish\n */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(void 0!==e?e:{})).ready=new Promise(function(e,n){D=e,I=n}),\"undefined\"==typeof XMLHttpRequest&&(global.XMLHttpRequest=function(){var t,r={open:function(e,n){t=n},send:function(){require(\"fs\").readFile(t,function(e,n){r.readyState=4,e?(cons", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31135"></a>
## FND-31135 — module-004 import a.f

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "f", "kind": "function", "type_index": 3, "function_index": 5, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 2954, "loader_excerpt": "ss.exit(e)},i.inspect=function(){return\"[Emscripten Module object]\"}):(B||l)&&(l?p=self.location.href:\"undefined\"!=typeof document&&document.currentScript&&(p=document.currentScript.src),p=0!==(p=Xe?Xe:p).indexOf(\"blob:\")?p.substr(0,p.lastIndexOf(\"/\")+1):\"\",Y=function(e){var n=new XMLHttpRequest;return n.open(\"GET\",e,!1),n.send(null),n.responseText},l)&&(c=function(e){var n=new XMLHttpRequest;return n.open(\"GET\",e,!1),n.responseType=\"arraybuffer\",n.send(null),new Uint8Array(n.response)}),i.print||console.log.bind(console)),d=i.printErr||console.warn.bind(console);for(r in a)a.hasOwnProperty(r)&&(i[r]=a[r]);a=null,i.arguments&&(N=i.arguments),i.thisProgram&&(u=i.thisProgram),i.quit&&(s=i.quit),i.wasmBinary&&(f=i.wasmBinary);var V=i.noExitRuntime||!0;\"object\"!=typeof WebAssembly&&_(\"no nativ", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31136"></a>
## FND-31136 — module-004 import a.g

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "g", "kind": "function", "type_index": 1, "function_index": 6, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 17281, "loader_excerpt": "(g[e>>2]=t.length,0);return t.forEach(function(e){r+=e.length+1}),g[n>>2]=r,0},c:function(e){Be(e)},g:function(){return 0},s:function(e,n,t,r){return e=de.aa(e),n=de.$(e,n,t),g[r>>2]=n,0},n:function(){},r:function(e,n,t,r){for(var o=0,a=0;a<t;a++){for(var i=g[n+8*a>>2],u=g[n+(8*a+4)>>2],s=0;s<u;s++){var c=C[i+s],f=pe[e];0===c||10===c?((1===e?X:d)(Q(f,0)),f.length=0):f.push(c)}o+=u}return g[r>>2]=o,0},m:function(){i.pauseQueue()},t:Ee,e:function(){i.unpauseQueue()}},Pe=(!function(){function n(e){e=Le(e=e.exports),i.asm=e,z=i.asm.w,ee(),re.unshift(i.asm.x),ce()}function t(e){n(e.instance)}function r(e){return(f||!B&&!l||\"function\"!=typeof fetch?Promise.resolve().then(le):fetch(h,{credentials:\"same-origin\"}).then(function(e){if(e.ok)return e.arrayBuffer();throw\"failed to load wasm binary file", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31137"></a>
## FND-31137 — module-004 import a.h

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "h", "kind": "function", "type_index": 2, "function_index": 7, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 6353, "loader_excerpt": "/4294967296|0}function ge(r,t,o,a,n){function i(e){var n=0,t=0;e&&(t=_.response?_.response.byteLength:0,n=k(t),C.set(new Uint8Array(_.response),n)),O[r+12>>2]=n,U(r+16,t)}if(d=O[r+8>>2]){var e=R(d),u=(u=R(g=r+112))||\"GET\",s=O[g+52>>2],c=O[g+56>>2],f=!!O[g+60>>2],l=O[g+68>>2],p=O[g+72>>2],d=O[g+76>>2],m=O[g+80>>2],y=O[g+84>>2],g=O[g+88>>2],h=!!(1&s),v=!!(2&s),s=!!(64&s),l=l?R(l):void 0,p=p?R(p):void 0,w=m?R(m):void 0,_=new XMLHttpRequest;if(_.withCredentials=f,_.open(u,e,!s,l,p),s||(_.timeout=c),_.Z=e,_.responseType=\"arraybuffer\",m&&_.overrideMimeType(w),d)for(;(u=O[d>>2])&&(e=O[d+4>>2]);)d+=8,u=R(u),e=R(e),_.setRequestHeader(u,e);ye.push(_),O[r+0>>2]=ye.length,d=y&&g?C.slice(y,y+g):null,_.onload=function(e){i(h&&!v);var n=_.response?_.response.byteLength:0;U(r+24,0),n&&U(r+32,n),x[r+40>>1]", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31138"></a>
## FND-31138 — module-004 import a.i

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "i", "kind": "function", "type_index": 0, "function_index": 8, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 14464, "loader_excerpt": "NMENT_IS_FETCH_WORKER||se();var je,ke={f:function(){return 0},p:function(){return 0},q:function(){},i:function(e){delete ye[e-1]},a:function(){_()},h:function(e,n){if(0===e)e=Date.now();else{if(1!==e&&4!==e)return g[He()>>2]=28,-1;e=me()}return g[n>>2]=e/1e3|0,g[n+4>>2]=e%1e3*1e6|0,0},k:function(){return!l},o:function(e,n,t){C.copyWithin(e,n,n+t)},d:function(e){var n=C.length;if(!(2147483648<(e>>>=0)))for(var t=1;t<=4;t*=2){var r=n*(1+.2/t),r=Math.min(r,e+100663296);0<(r=Math.max(e,r))%65536&&(r+=65536-r%65536);e:{try{z.grow(Math.min(2147483648,r)-K.byteLength+65535>>>16),ee();var o=1;break e}catch(e){}o=void 0}if(o)return!0}return!1},b:function(t){Ue(function(e){var n;n=e,setTimeout(function(){j(n)},t)})},j:function(e,t,n,r,o){function a(e,n){he(e,n.response,function(e){j(function(){p?P.a", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-31139"></a>
## FND-31139 — module-004 import a.j

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
{"module_id": "module-004", "direction": "import", "module": "a", "name": "j", "kind": "function", "type_index": 0, "function_index": 9, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 15080, "loader_excerpt": " 0}if(o)return!0}return!1},b:function(t){Ue(function(e){var n;n=e,setTimeout(function(){j(n)},t)})},j:function(e,t,n,r,o){function a(e,n){he(e,n.response,function(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)},function(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)})}function i(e){j(function(){y?P.apply(null,[y,e]):o&&o(e)},_)}function u(e){j(function(){d?P.apply(null,[d,e]):n&&n(e)},_)}function s(e){j(function(){m?P.apply(null,[m,e]):r&&r(e)},_)}function c(e){j(function(){p?P.apply(null,[p,e]):t&&t(e)},_)}var f=e+112,l=R(f),p=O[f+36>>2],d=O[f+40>>2],m=O[f+44>>2],y=O[f+48>>2],g=O[f+52>>2],h=!!(4&g),v=!!(32&g),w=!!(16&g),_=!!(64&g);if(\"EM_IDB_STORE\"===l)l=O[f+84>>2],he(e,C.slice(l,l+O[f+88>>2]),c,u);else if(\"EM_IDB_DELETE\"===l){var b=e;var S=c;var M=u;g=L;if(g){f=O[b+112+64>>2];f=R(f", "semantic_confidence": "UNKNOWN", "evidence_confidence": "CONFIRMED declaration"}
```
