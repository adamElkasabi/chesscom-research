# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30540"></a>
## FND-30540 — module-001 import wasi_snapshot_preview1.fd_write

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_write", "kind": "function", "type_index": 10, "function_index": 119, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 91468, "loader_excerpt": "ts=null),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_sync:_fd_sync,fd_write:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{if(1==iovcnt)return FS.write(stream,HEAP8,HEAPU32[iov>>2],HEAPU32[iov+4>>2],offset);for(var total=0,i=0,p=iov;i<iovcnt;i++,p+=8)total+=HEAPU32[p+4>>2];var view=new Uint8Array(total),voff=0;for(i=0;i<iovcnt;i++,iov+=8){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];view.set(HEAPU8.subarray(ptr,ptr+len),voff),voff+=len}return FS.write(stream,view,0,total,offset)})(SYSCALLS.getStreamFromFD(fd),iov,iovcnt);return HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},invoke_di:function(index,a1){var sp=stackSave();try{return dynCall_di(index,a1)}catch(e){if(stackRestore(sp),!(e ", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30541"></a>
## FND-30541 — module-001 import env._abort_js

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_abort_js", "kind": "function", "type_index": 13, "function_index": 120, "signature": {"parameters": [], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 80750, "loader_excerpt": "riteStat(buf,FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType=0n===minRange;let fromWireType=value=>value;if(isUnsignedType){const bitSize=8*size;fromWireType=value=>BigInt.asUintN(bitSize,value),maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>(\"number\"==typeof value&&(value=BigInt(value)),value),readValueFromPointer:integerReadValueFromPointer(name,size,!isUnsignedType),destructorFunction:null})},_embind_register_bool:(rawType,name,trueValue,falseValue)=>{registerType(rawType,{name:name=AsciiToString(name),fromWireType:function(wt){ret", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30542"></a>
## FND-30542 — module-001 import wasi_snapshot_preview1.clock_time_get

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "clock_time_get", "kind": "function", "type_index": 35, "function_index": 121, "signature": {"parameters": ["i32", "i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 88642, "loader_excerpt": "TF8ToString(url))},cee_worker_terminate:function(id){engineWorkersOf(Module,console).terminate(id)},clock_time_get:function(clk_id,ignored_precision,ptime){if(ignored_precision=bigintToI53Checked(ignored_precision),!((clock_id=clk_id)>=0&&clock_id<=3))return 28;var clock_id,now;now=0===clk_id?_emscripten_date_now():_emscripten_get_now();var nsec=Math.round(1e3*now*1e3);return HEAP64[ptime>>3]=BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30543"></a>
## FND-30543 — module-001 import env.emscripten_date_now

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "emscripten_date_now", "kind": "function", "type_index": 62, "function_index": 122, "signature": {"parameters": [], "results": ["f64"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89038, "loader_excerpt": "BigInt(nsec),0},emscripten_asm_const_int:(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30544"></a>
## FND-30544 — module-001 import env.__syscall_openat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_openat", "kind": "function", "type_index": 10, "function_index": 123, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79856, "loader_excerpt": ".lstat(path):FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_openat:function(dirfd,path,flags,varargs){SYSCALLS.varargs=varargs;try{path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path);var mode=varargs?syscallGetVarargI():0;return 64&flags&&(mode&=~SYSCALLS.currentUmask),FS.open(path,flags,mode).fd}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_readlinkat:function(dirfd,path,buf,bufsize){try{if(path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),bufsize<=0)return-28;var ret=FS.readlink(path),len=Math.min(bufsize,lengthBytesUTF8(ret)),endChar=HEAP8[buf+len];return stringToUTF8(ret,buf,bufsize+1),HEAP8[buf+len]=endChar,len}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30545"></a>
## FND-30545 — module-001 import env.__syscall_fstat64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_fstat64", "kind": "function", "type_index": 3, "function_index": 124, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 76514, "loader_excerpt": "P16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64:function(fd,buf){try{return SYSCALLS.writeStat(buf,FS.fstat(fd))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_getdents64:function(fd,dirp,count){try{var stream=SYSCALLS.getStreamFromFD(fd);stream.getdents||=FS.readdir(stream.path);for(var pos=0,off=FS.llseek(stream,0,1),startIdx=Math.floor(off/280),endIdx=Math.min(stream.getdents.length,startIdx+Math.floor(count/280)),idx=startIdx;idx<endIdx;idx++){var id,type,name=stream.getdents[idx];if(\".\"===name)id=stream.node.id,type=4;else if(\"..\"===name){id=FS.lookupPath(stream.path,{parent:!0}).node.id,type=4}else{var child;try{child=FS.lookupNode(stream.node,name)}catch(e){if(28===e?.errno)conti", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30546"></a>
## FND-30546 — module-001 import env.__syscall_stat64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_stat64", "kind": "function", "type_index": 3, "function_index": 125, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 80566, "loader_excerpt": ",HEAP8[buf+len]=endChar,len}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_stat64:function(path,buf){try{return path=SYSCALLS.getStr(path),SYSCALLS.writeStat(buf,FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType=0n===minRange;let fromWireType=value=>value;if(isUnsignedType){const bitSize=8*size;fromWireType=value=>BigInt.asUintN(bitSize,value),maxRange=fromWireType(maxRange)}registerType(primitiveType,{name:name,fromWireType:fromWireType,toWireType:(destructors,value)=>(\"number\"==typeof value&&(value=BigInt(value)),value),readValueFromPointer:integerReadValueFromPointer(name,size,!", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30547"></a>
## FND-30547 — module-001 import env.__syscall_newfstatat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_newfstatat", "kind": "function", "type_index": 10, "function_index": 126, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79525, "loader_excerpt": "ask,FS.mkdir(path,mode,0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_newfstatat:function(dirfd,path,buf,flags){try{path=SYSCALLS.getStr(path);var nofollow=256&flags,allowEmpty=4096&flags;return flags&=-6401,path=SYSCALLS.calculateAt(dirfd,path,allowEmpty),SYSCALLS.writeStat(buf,nofollow?FS.lstat(path):FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_openat:function(dirfd,path,flags,varargs){SYSCALLS.varargs=varargs;try{path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path);var mode=varargs?syscallGetVarargI():0;return 64&flags&&(mode&=~SYSCALLS.currentUmask),FS.open(path,flags,mode).fd}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_readlinkat:function(dirfd,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30548"></a>
## FND-30548 — module-001 import env.__syscall_lstat64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_lstat64", "kind": "function", "type_index": 3, "function_index": 127, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79094, "loader_excerpt": "return 0;default:return-28}}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_lstat64:function(path,buf){try{return path=SYSCALLS.getStr(path),SYSCALLS.writeStat(buf,FS.lstat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_mkdirat:function(dirfd,path,mode){try{return path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),mode&=~SYSCALLS.currentUmask,FS.mkdir(path,mode,0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_newfstatat:function(dirfd,path,buf,flags){try{path=SYSCALLS.getStr(path);var nofollow=256&flags,allowEmpty=4096&flags;return flags&=-6401,path=SYSCALLS.calculateAt(dirfd,path,allowEmpty),SYSCALLS.writeStat(buf,nofollow?FS.lstat(path):FS.stat(path))}catch(e){i", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30549"></a>
## FND-30549 — module-001 import wasi_snapshot_preview1.fd_sync

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_sync", "kind": "function", "type_index": 2, "function_index": 128, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 91451, "loader_excerpt": "e&&(stream.getdents=null),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_sync:_fd_sync,fd_write:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{if(1==iovcnt)return FS.write(stream,HEAP8,HEAPU32[iov>>2],HEAPU32[iov+4>>2],offset);for(var total=0,i=0,p=iov;i<iovcnt;i++,p+=8)total+=HEAPU32[p+4>>2];var view=new Uint8Array(total),voff=0;for(i=0;i<iovcnt;i++,iov+=8){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];view.set(HEAPU8.subarray(ptr,ptr+len),voff),voff+=len}return FS.write(stream,view,0,total,offset)})(SYSCALLS.getStreamFromFD(fd),iov,iovcnt);return HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},invoke_di:function(index,a1){var sp=stackSave();try{return dynCall_di(index,a1)}catch(e){if(stac", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30550"></a>
## FND-30550 — module-001 import wasi_snapshot_preview1.environ_sizes_get

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "environ_sizes_get", "kind": "function", "type_index": 3, "function_index": 129, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 89804, "loader_excerpt": "uf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=>{var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;for(var string of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"Err", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30551"></a>
## FND-30551 — module-001 import wasi_snapshot_preview1.environ_get

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "environ_get", "kind": "function", "type_index": 3, "function_index": 130, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 89593, "loader_excerpt": "GrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=>{var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;for(var string of strings)bufSize+=lengthBytesUTF8(string)+1;return HEAPU32[penviron_buf_size>>2]=bufSize,0},exit:_exit,fd_close:function(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamF", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30552"></a>
## FND-30552 — module-001 import wasi_snapshot_preview1.fd_fdstat_get

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_fdstat_get", "kind": "function", "type_index": 3, "function_index": 131, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 90227, "loader_excerpt": ");return FS.close(stream),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_fdstat_get:function(fd,pbuf){try{var stream=SYSCALLS.getStreamFromFD(fd),type=stream.tty?2:FS.isDir(stream.mode)?3:FS.isLink(stream.mode)?7:4;return HEAP8[pbuf]=type,HEAP16[pbuf+2>>1]=0,HEAP64[pbuf+8>>3]=BigInt(0),HEAP64[pbuf+16>>3]=BigInt(0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_read:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{for(var ret=0,i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2],len=HEAPU32[iov+4>>2];iov+=8;try{var curr=FS.read(stream,HEAP8,ptr,len,offset)}catch(e){if(ret>0&&e instanceof FS.ErrnoError&&(6==e.errno||6==e.errno))break;throw e}if(curr<0)return-1;if(ret+=curr,curr<len)break;void 0!==offset&&(offset+=curr)}r", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30553"></a>
## FND-30553 — module-001 import env.emscripten_get_now

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "emscripten_get_now", "kind": "function", "type_index": 62, "function_index": 132, "signature": {"parameters": [], "results": ["f64"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89118, "loader_excerpt": "code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30554"></a>
## FND-30554 — module-001 import wasi_snapshot_preview1.fd_seek

WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "fd_seek", "kind": "function", "type_index": 159, "function_index": 133, "signature": {"parameters": ["i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.", "loader_character_offset": 91082, "loader_excerpt": "turn HEAPU32[pnum>>2]=num,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_seek:function(fd,offset,whence,newOffset){offset=bigintToI53Checked(offset);try{if(isNaN(offset))return 22;var stream=SYSCALLS.getStreamFromFD(fd);return FS.llseek(stream,offset,whence),HEAP64[newOffset>>3]=BigInt(stream.position),stream.getdents&&!offset&&0===whence&&(stream.getdents=null),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return e.errno}},fd_sync:_fd_sync,fd_write:function(fd,iov,iovcnt,pnum){try{var num=((stream,iov,iovcnt,offset)=>{if(1==iovcnt)return FS.write(stream,HEAP8,HEAPU32[iov>>2],HEAPU32[iov+4>>2],offset);for(var total=0,i=0,p=iov;i<iovcnt;i++,p+=8)total+=HEAPU32[p+4>>2];var view=new Uint8Array(total),voff=0;for(i=0;i<iovcnt;i++,iov+=8){var ptr=HEAPU32[", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30555"></a>
## FND-30555 — module-001 import env.__syscall_mkdirat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_mkdirat", "kind": "function", "type_index": 4, "function_index": 134, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 79280, "loader_excerpt": "iteStat(buf,FS.lstat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_mkdirat:function(dirfd,path,mode){try{return path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),mode&=~SYSCALLS.currentUmask,FS.mkdir(path,mode,0),0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_newfstatat:function(dirfd,path,buf,flags){try{path=SYSCALLS.getStr(path);var nofollow=256&flags,allowEmpty=4096&flags;return flags&=-6401,path=SYSCALLS.calculateAt(dirfd,path,allowEmpty),SYSCALLS.writeStat(buf,nofollow?FS.lstat(path):FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_openat:function(dirfd,path,flags,varargs){SYSCALLS.varargs=varargs;try{path=SYSCALLS.getStr(path),path=SYSCALLS.ca", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30556"></a>
## FND-30556 — module-001 import env._tzset_js

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_tzset_js", "kind": "function", "type_index": 6, "function_index": 135, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 87229, "loader_excerpt": "getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,date.getTime()/1e3})();return BigInt(ret)},_tzset_js:(timezone,daylight,std_name,dst_name)=>{var currentYear=(new Date).getFullYear(),winter=new Date(currentYear,0,1),summer=new Date(currentYear,6,1),winterOffset=winter.getTimezoneOffset(),summerOffset=summer.getTimezoneOffset(),stdTimezoneOffset=Math.max(winterOffset,summerOffset);HEAPU32[timezone>>2]=60*stdTimezoneOffset,HEAP32[daylight>>2]=Number(winterOffset!=summerOffset);var extractZone=timezoneOffset=>{var sign=timezoneOffset>=0?\"-\":\"+\",absOffset=Math.abs(timezoneOffset);return`UTC${sign}${String(Math.floor(absOffset/60)).padStart(2,\"0\")}${String(absOffset%60).padStart(2,\"0\")}`},winterName=extractZone(winterOffset),summerName=extractZone(summerOffset);summerOffset<winterOffset", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30557"></a>
## FND-30557 — module-001 import env._timegm_js

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_timegm_js", "kind": "function", "type_index": 11, "function_index": 136, "signature": {"parameters": ["i32"], "results": ["i64"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 86791, "loader_excerpt": "dr,stream,len,flags,offset)}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_timegm_js:function(tmPtr){var ret=(()=>{var time=Date.UTC(HEAP32[tmPtr+20>>2]+1900,HEAP32[tmPtr+16>>2],HEAP32[tmPtr+12>>2],HEAP32[tmPtr+8>>2],HEAP32[tmPtr+4>>2],HEAP32[tmPtr>>2],0),date=new Date(time);if(isNaN(date.getTime()))return-1;HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,date.getTime()/1e3})();return BigInt(ret)},_tzset_js:(timezone,daylight,std_name,dst_name)=>{var currentYear=(new Date).getFullYear(),winter=new Date(currentYear,0,1),summer=new Date(currentYear,6,1),winterOffset=winter.getTimezoneOffset(),summerOffset=summer.getTimezoneOffset(),stdTimezoneOffset=Math.ma", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30558"></a>
## FND-30558 — module-001 import env._localtime_js

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_localtime_js", "kind": "function", "type_index": 49, "function_index": 137, "signature": {"parameters": ["i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 85278, "loader_excerpt": "etUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,0},_localtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getSeconds(),HEAP32[tmPtr+4>>2]=date.getMinutes(),HEAP32[tmPtr+8>>2]=date.getHours(),HEAP32[tmPtr+12>>2]=date.getDate(),HEAP32[tmPtr+16>>2]=date.getMonth(),HEAP32[tmPtr+20>>2]=date.getFullYear()-1900,HEAP32[tmPtr+24>>2]=date.getDay();var yday=0|(date=>{var year;return((year=date.getFullYear())%4!=0||year%100==0&&year%400!=0?MONTH_DAYS_REGULAR_CUMULATIVE:MONTH_DAYS_LEAP_CUMULATIVE)[date.getMonth()]+date.getDate()-1})(date);HEAP32[tmPtr+28>>2]=yday,HEAP32[tmPtr+36>>2]=-60*date.getTimezoneOffset();var start=new Date(date.getFullYear(),0,1),summerOf", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30559"></a>
## FND-30559 — module-001 import env._gmtime_js

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_gmtime_js", "kind": "function", "type_index": 49, "function_index": 138, "signature": {"parameters": ["i64", "i32"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 84752, "loader_excerpt": "Type,{isVoid:!0,name:name=AsciiToString(name),fromWireType:()=>{},toWireType:(destructors,o)=>{}})},_gmtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getUTCSeconds(),HEAP32[tmPtr+4>>2]=date.getUTCMinutes(),HEAP32[tmPtr+8>>2]=date.getUTCHours(),HEAP32[tmPtr+12>>2]=date.getUTCDate(),HEAP32[tmPtr+16>>2]=date.getUTCMonth(),HEAP32[tmPtr+20>>2]=date.getUTCFullYear()-1900,HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,0},_localtime_js:function(time,tmPtr){time=bigintToI53Checked(time);var date=new Date(1e3*time);if(isNaN(date.getTime()))return 1;HEAP32[tmPtr>>2]=date.getSeconds(),HEAP32[tmPtr", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30560"></a>
## FND-30560 — module-001 import env._munmap_js

Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_munmap_js", "kind": "function", "type_index": 89, "function_index": 139, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.", "loader_character_offset": 86535, "loader_excerpt": "ated,HEAPU32[addr>>2]=ptr,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_munmap_js:function(addr,len,prot,flags,fd,offset){offset=bigintToI53Checked(offset);try{var stream=SYSCALLS.getStreamFromFD(fd);2&prot&&SYSCALLS.doMsync(addr,stream,len,flags,offset)}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_timegm_js:function(tmPtr){var ret=(()=>{var time=Date.UTC(HEAP32[tmPtr+20>>2]+1900,HEAP32[tmPtr+16>>2],HEAP32[tmPtr+12>>2],HEAP32[tmPtr+8>>2],HEAP32[tmPtr+4>>2],HEAP32[tmPtr>>2],0),date=new Date(time);if(isNaN(date.getTime()))return-1;HEAP32[tmPtr+24>>2]=date.getUTCDay();var start=Date.UTC(date.getUTCFullYear(),0,1,0,0,0,0),yday=(date.getTime()-start)/864e5|0;return HEAP32[tmPtr+28>>2]=yday,date.getTime()/1e3})();return BigInt(ret)},_tzset", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30561"></a>
## FND-30561 — module-001 import env._mmap_js

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "_mmap_js", "kind": "function", "type_index": 84, "function_index": 140, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i64", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 86207, "loader_excerpt": "t&&date.getTimezoneOffset()==Math.min(winterOffset,summerOffset));return HEAP32[tmPtr+32>>2]=dst,0},_mmap_js:function(len,prot,flags,fd,offset,allocated,addr){offset=bigintToI53Checked(offset);try{var stream=SYSCALLS.getStreamFromFD(fd),res=FS.mmap(stream,len,offset,prot,flags),ptr=res.ptr;return HEAP32[allocated>>2]=res.allocated,HEAPU32[addr>>2]=ptr,0}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_munmap_js:function(addr,len,prot,flags,fd,offset){offset=bigintToI53Checked(offset);try{var stream=SYSCALLS.getStreamFromFD(fd);2&prot&&SYSCALLS.doMsync(addr,stream,len,flags,offset)}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_timegm_js:function(tmPtr){var ret=(()=>{var time=Date.UTC(HEAP32[tmPtr+20>>2]+1900,HEAP32[tmPtr+16>>2],HEAP32[tmPtr", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30562"></a>
## FND-30562 — module-001 import env.__syscall_readlinkat

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_readlinkat", "kind": "function", "type_index": 10, "function_index": 141, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 80189, "loader_excerpt": "FS.open(path,flags,mode).fd}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_readlinkat:function(dirfd,path,buf,bufsize){try{if(path=SYSCALLS.getStr(path),path=SYSCALLS.calculateAt(dirfd,path),bufsize<=0)return-28;var ret=FS.readlink(path),len=Math.min(bufsize,lengthBytesUTF8(ret)),endChar=HEAP8[buf+len];return stringToUTF8(ret,buf,bufsize+1),HEAP8[buf+len]=endChar,len}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_stat64:function(path,buf){try{return path=SYSCALLS.getStr(path),SYSCALLS.writeStat(buf,FS.stat(path))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},_abort_js:()=>abort(\"\"),_embind_register_bigint:(primitiveType,name,size,minRange,maxRange)=>{name=AsciiToString(name);const isUnsignedType", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30563"></a>
## FND-30563 — module-001 import env.emscripten_resize_heap

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "emscripten_resize_heap", "kind": "function", "type_index": 2, "function_index": 142, "signature": {"parameters": ["i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89157, "loader_excerpt": ":_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,1/0)+1,envp+=4}return 0},environ_sizes_get:(penviron_count,penviron_buf_size)=", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30564"></a>
## FND-30564 — module-001 import env.__syscall_getdents64

POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__syscall_getdents64", "kind": "function", "type_index": 4, "function_index": 143, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.", "loader_character_offset": 76669, "loader_excerpt": "writeStat(buf,FS.fstat(fd))}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_getdents64:function(fd,dirp,count){try{var stream=SYSCALLS.getStreamFromFD(fd);stream.getdents||=FS.readdir(stream.path);for(var pos=0,off=FS.llseek(stream,0,1),startIdx=Math.floor(off/280),endIdx=Math.min(stream.getdents.length,startIdx+Math.floor(count/280)),idx=startIdx;idx<endIdx;idx++){var id,type,name=stream.getdents[idx];if(\".\"===name)id=stream.node.id,type=4;else if(\"..\"===name){id=FS.lookupPath(stream.path,{parent:!0}).node.id,type=4}else{var child;try{child=FS.lookupNode(stream.node,name)}catch(e){if(28===e?.errno)continue;throw e}id=child.id,type=FS.isChrdev(child.mode)?2:FS.isDir(child.mode)?4:FS.isLink(child.mode)?10:8}HEAP64[dirp+pos>>3]=BigInt(id),HEAP64[dirp+pos+8>>", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30565"></a>
## FND-30565 — module-001 import env.__cxa_uncaught_exceptions

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_uncaught_exceptions", "kind": "function", "type_index": 8, "function_index": 144, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75831, "loader_excerpt": "exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);switch(cmd){case 0:if((arg=syscallGetVarargI())<0)return-28;for(;FS.streams[arg];)arg++;return FS.dupStream(stream,arg).fd;case 1:case 2:case 13:case 14:return 0;case 3:return stream.flags;case 4:var arg=syscallGetVarargI();return stream.flags=-289793&stream.flags|289792&arg,0;case 12:arg=syscallGetVarargP();return HEAP16[arg+0>>1]=2,0}return-28}catch(e){if(void 0===FS||\"ErrnoError\"!==e.name)throw e;return-e.errno}},__syscall_fstat64", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30566"></a>
## FND-30566 — module-001 import env.__cxa_current_primary_exception

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_current_primary_exception", "kind": "function", "type_index": 8, "function_index": 145, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 74527, "loader_excerpt": "htExceptionCount--),info.set_rethrown(!1),exceptionCaught.push(info),___cxa_get_exception_ptr(ptr)},__cxa_current_primary_exception:()=>{if(!exceptionCaught.length)return 0;var info=exceptionCaught[exceptionCaught.length-1];return ___cxa_increment_exception_refcount(info.excPtr),info.excPtr},__cxa_end_catch:()=>{_setThrew(0,0);var info=exceptionCaught.pop();___cxa_decrement_exception_refcount(info.excPtr),exceptionLast=null},__cxa_find_matching_catch_2:()=>findMatchingCatch([]),__cxa_find_matching_catch_3:arg0=>findMatchingCatch([arg0]),__cxa_find_matching_catch_4:(arg0,arg1)=>findMatchingCatch([arg0,arg1]),__cxa_find_matching_catch_5:(arg0,arg1,arg2)=>findMatchingCatch([arg0,arg1,arg2]),__cxa_rethrow:()=>{exceptionCaught.length||abort(\"no exception to throw\");var info=exceptionCaught.at(-", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30567"></a>
## FND-30567 — module-001 import env.__cxa_rethrow_primary_exception

C++ exception-handling ABI support,not a web API.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "__cxa_rethrow_primary_exception", "kind": "function", "type_index": 0, "function_index": 146, "signature": {"parameters": ["i32"], "results": []}, "apparent_purpose": "C++ exception-handling ABI support,not a web API.", "loader_character_offset": 75397, "loader_excerpt": "aughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)},__cxa_rethrow_primary_exception:ptr=>{if(ptr){var info=new ExceptionInfo(ptr);throw info.set_rethrown(!0),info.set_caught(!1),uncaughtExceptionCount++,___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr)}},__cxa_throw:(ptr,type,destructor)=>{throw new ExceptionInfo(ptr).init(type,destructor),___cxa_increment_exception_refcount(ptr),exceptionLast=new CppException(ptr),uncaughtExceptionCount++,exceptionLast},__cxa_uncaught_exceptions:()=>uncaughtExceptionCount,__resumeException:ptr=>{throw exceptionLast||(exceptionLast=new CppException(ptr)),exceptionLast},__syscall_fcntl64:function(fd,cmd,varargs){SYSCALLS.varargs=varargs;try{var stream=SYSCALLS.getStreamFromFD(fd);swi", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30568"></a>
## FND-30568 — module-001 import env.invoke_iiiiij

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiij", "kind": "function", "type_index": 89, "function_index": 147, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 97691, "loader_excerpt": ",a9,a10,a11,a12)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiij:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiij(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiijj:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiijj(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30569"></a>
## FND-30569 — module-001 import env.invoke_iiiiid

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiid", "kind": "function", "type_index": 127, "function_index": 148, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "f64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96164, "loader_excerpt": "dex,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiid:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiid(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiii:function(index,a1,a2,a3,a4,a5){var sp=stackSave();try{return dynCall_iiiiii(index,a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiiii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30570"></a>
## FND-30570 — module-001 import env.invoke_iiiiijj

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiijj", "kind": "function", "type_index": 63, "function_index": 149, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i64", "i64"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 97886, "loader_excerpt": ",a1,a2,a3,a4,a5)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiijj:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiiijj(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{return dynCall_iiiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiijii:function(index,a1,a2,a3,a4,a5,a6){var sp=stackSave();try{return dynCall_iiiijii(index,a1,a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiij:function(index,a1,a2,a3){var sp=stackSave();try{return dynCall_iiij(index,a1,a2,a3)}catch(e){if", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30571"></a>
## FND-30571 — module-001 import env.invoke_iiiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_iiiiiiii", "kind": "function", "type_index": 17, "function_index": 150, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 96757, "loader_excerpt": ",a2,a3,a4,a5,a6)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{return dynCall_iiiiiiii(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8){var sp=stackSave();try{return dynCall_iiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11){var sp=stackSave();try{return dynCall_iiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_iiiiiiiiiiiii:fu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30572"></a>
## FND-30572 — module-001 import env.invoke_viiiiiiiiiiiiiii

Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "invoke_viiiiiiiiiiiiiii", "kind": "function", "type_index": 128, "function_index": 151, "signature": {"parameters": ["i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32", "i32"], "results": []}, "apparent_purpose": "Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.", "loader_character_offset": 107547, "loader_excerpt": "a11,a12,a13,a14)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiiiiiiiiiii:function(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15){var sp=stackSave();try{dynCall_viiiiiiiiiiiiiii(index,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiiiij:function(index,a1,a2,a3,a4,a5,a6,a7){var sp=stackSave();try{dynCall_viiiiiij(index,a1,a2,a3,a4,a5,a6,a7)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiij:function(index,a1,a2,a3,a4){var sp=stackSave();try{dynCall_viiij(index,a1,a2,a3,a4)}catch(e){if(stackRestore(sp),!(e instanceof EmscriptenEH))throw e;_setThrew(1,0)}},invoke_viiiji:function(index,a1,a2,a", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30573"></a>
## FND-30573 — module-001 import wasi_snapshot_preview1.random_get

Host-provided random bytes. Does not prove a particular cryptographic protocol.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "wasi_snapshot_preview1", "name": "random_get", "kind": "function", "type_index": 3, "function_index": 152, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "apparent_purpose": "Host-provided random bytes. Does not prove a particular cryptographic protocol.", "loader_character_offset": 109924, "loader_excerpt": "tr+size).slice();postMessage({proto:result_array,is_final:is_final})},llvm_eh_typeid_for:type=>type,random_get:(buffer,size)=>randomFill(HEAPU8.subarray(buffer,buffer+size))};async function run(){!function(){var preRun=Module.preRun;preRun&&(\"function\"==typeof preRun&&(preRun=[preRun]),onPreRuns.push(...preRun)),callRuntimeCallbacks(onPreRuns)}(),runDependencies&&await(async()=>dependenciesPromise)();var setStatus=Module.setStatus;setStatus&&(setStatus(\"Running...\"),await new Promise((resolve=>setTimeout(resolve,1))),setTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),wasmExports.__wasm_call_ctors(),FS.ignorePermissions=!1,Module.onRuntimeInitialized?.(),function(){var postRun=Module.postRun;postRun&&(\"function\"==typeof postRun&&(postRun=[postRun]),onP", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30574"></a>
## FND-30574 — module-001 import env.emscripten_get_heap_max

Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.

- Category: wasm_imports_exports
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014, SRC-3015
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/imports-exports-annotated.json)

```text
{"module_id": "module-001", "direction": "import", "module": "env", "name": "emscripten_get_heap_max", "kind": "function", "type_index": 8, "function_index": 153, "signature": {"parameters": [], "results": ["i32"]}, "apparent_purpose": "Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.", "loader_character_offset": 89079, "loader_excerpt": "(code,sigPtr,argbuf)=>runEmAsmFunction(code,sigPtr,argbuf),emscripten_date_now:_emscripten_date_now,emscripten_get_heap_max:()=>2147483648,emscripten_get_now:_emscripten_get_now,emscripten_resize_heap:requestedSize=>{var oldSize=HEAPU8.length;if((requestedSize>>>=0)>2147483648)return!1;for(var cutDown=1;cutDown<=4;cutDown*=2){var overGrownHeapSize=oldSize*(1+.2/cutDown);overGrownHeapSize=Math.min(overGrownHeapSize,requestedSize+100663296);var newSize=Math.min(2147483648,alignMemory(Math.max(requestedSize,overGrownHeapSize),65536));if(growMemory(newSize))return!0}return!1},emscripten_sleep:_emscripten_sleep,environ_get:(__environ,environ_buf)=>{var bufSize=0,envp=0;for(var string of getEnvStrings()){var ptr=environ_buf+bufSize;HEAPU32[__environ+envp>>2]=ptr,bufSize+=stringToUTF8(string,ptr,", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30575"></a>
## FND-30575 — module-001 export memory

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
{"module_id": "module-001", "direction": "export", "name": "memory", "kind": "memory", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119266, "loader_excerpt": ".asyncify_start_rewind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_error(Module){return Module.ccall(\"CEE_GetLastError\",\"string\",[],[])}function js_buf_to_c_buf(Module,js_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30576"></a>
## FND-30576 — module-001 export __wasm_call_ctors

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
{"module_id": "module-001", "direction": "export", "name": "__wasm_call_ctors", "kind": "function", "index": 154, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 110448, "loader_excerpt": "etTimeout(setStatus,1,\"\")),ABORT||(Module.noFSInit||FS.initialized||FS.init(),TTY.init(),wasmExports.__wasm_call_ctors(),FS.ignorePermissions=!1,Module.onRuntimeInitialized?.(),function(){var postRun=Module.postRun;postRun&&(\"function\"==typeof postRun&&(postRun=[postRun]),onPostRuns.push(...postRun)),callRuntimeCallbacks(onPostRuns)}())}return async function(){function receiveInstance(instance){return wasmExports=instance.exports,function(wasmExports){wasmExports.__getTypeName,Module._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmEx", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30577"></a>
## FND-30577 — module-001 export __getTypeName

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
{"module_id": "module-001", "direction": "export", "name": "__getTypeName", "kind": "function", "index": 4993, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 110815, "loader_excerpt": "tion receiveInstance(instance){return wasmExports=instance.exports,function(wasmExports){wasmExports.__getTypeName,Module._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_J", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30578"></a>
## FND-30578 — module-001 export __indirect_function_table

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
{"module_id": "module-001", "direction": "export", "name": "__indirect_function_table", "kind": "table", "index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 119285, "loader_excerpt": "ind,_asyncify_stop_rewind=wasmExports.asyncify_stop_rewind,wasmMemory=wasmExports.memory,wasmExports.__indirect_function_table}(wasmExports=Asyncify.instrumentWasmExports(wasmExports)),updateMemoryViews(),wasmExports}var info={env:wasmImports,wasi_snapshot_preview1:wasmImports},instantiateWasm=Module.instantiateWasm;return instantiateWasm?new Promise((resolve=>{instantiateWasm(info,(inst=>resolve(receiveInstance(inst))))})):(wasmBinaryFile??=findWasmBinary(),function(result){return receiveInstance(result.instance)}(await instantiateAsync(undefined,wasmBinaryFile,info)))}().then((()=>run())),Module}var RuntimeInitialized=!1;let api_call_map=function(){function get_last_error(Module){return Module.ccall(\"CEE_GetLastError\",\"string\",[],[])}function js_buf_to_c_buf(Module,js_buf){if(!js_buf)ret", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30579"></a>
## FND-30579 — module-001 export uci_command

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
{"module_id": "module-001", "direction": "export", "name": "uci_command", "kind": "function", "index": 167, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 110861, "loader_excerpt": "rts=instance.exports,function(wasmExports){wasmExports.__getTypeName,Module._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifa", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30580"></a>
## FND-30580 — module-001 export init

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
{"module_id": "module-001", "direction": "export", "name": "init", "kind": "function", "index": 169, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 29972, "loader_excerpt": "),byteArray=await(async(byteArray,fullname)=>{for(var plugin of(\"undefined\"!=typeof Browser&&Browser.init(),preloadPlugins))if(plugin.canHandle(fullname))return plugin.handle(byteArray,fullname);return byteArray})(byteArray,fullname),preFinish?.(),dontCreateFile||((...args)=>{FS.createDataFile(...args)})(parent,name,byteArray,canRead,canWrite,canOwn)}finally{runDependencies--,Module.monitorRunDependencies?.(runDependencies),runDependencies||dependenciesPromiseResolve()}},FS={root:null,mounts:[],devices:{},streams:[],nextInode:1,nameTable:null,currentPath:\"/\",initialized:!1,ignorePermissions:!0,filesystems:null,syncFSRequests:0,ErrnoError:class{name=\"ErrnoError\";constructor(errno){this.errno=errno}},FSStream:class{shared={};get object(){return this.node}set object(val){this.node=val}get isR", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30581"></a>
## FND-30581 — module-001 export CEE_Init

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
{"module_id": "module-001", "direction": "export", "name": "CEE_Init", "kind": "function", "index": 1666, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 110932, "loader_excerpt": "dule._uci_command=wasmExports.uci_command,Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExpo", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30582"></a>
## FND-30582 — module-001 export CEE_Dispose

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
{"module_id": "module-001", "direction": "export", "name": "CEE_Dispose", "kind": "function", "index": 1667, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 110973, "loader_excerpt": ",Module._init=wasmExports.init,Module._CEE_Init=wasmExports.CEE_Init,Module._CEE_Dispose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_D", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30583"></a>
## FND-30583 — module-001 export free

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
{"module_id": "module-001", "direction": "export", "name": "free", "kind": "function", "index": 22208, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 39297, "loader_excerpt": "eam:stream=>FS.statfsNode(stream.node),statfsNode(node){var rtn={bsize:4096,frsize:4096,blocks:1e6,bfree:5e5,bavail:5e5,files:FS.nextInode,ffree:FS.nextInode-1,fsid:42,flags:2,namelen:255};return node.node_ops.statfs&&Object.assign(rtn,node.node_ops.statfs(node.mount.opts.root)),rtn},create:(path,mode=438)=>(mode&=4095,mode|=32768,FS.mknod(path,mode,0)),mkdir:(path,mode=511)=>(mode&=1023,mode|=16384,FS.mknod(path,mode,0)),mkdirTree(path,mode){var dirs=path.split(\"/\"),d=\"\";for(var dir of dirs)if(dir){(d||PATH.isAbs(path))&&(d+=\"/\"),d+=dir;try{FS.mkdir(d,mode)}catch(e){if(20!=e.errno)throw e}}},mkdev:(path,mode,dev)=>(void 0===dev&&(dev=mode,mode=438),mode|=8192,FS.mknod(path,mode,dev)),symlink(oldpath,newpath){if(!PATH_FS.resolve(oldpath))throw new FS.ErrnoError(44);var parent=FS.lookupPath", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30584"></a>
## FND-30584 — module-001 export malloc

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
{"module_id": "module-001", "direction": "export", "name": "malloc", "kind": "function", "index": 22207, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Runtime/engine export; semantic identity requires wrapper/call-site evidence.", "loader_character_offset": 111056, "loader_excerpt": "spose=wasmExports.CEE_Dispose,_free=Module._free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasm", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30585"></a>
## FND-30585 — module-001 export CEE_InitWithOpts

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
{"module_id": "module-001", "direction": "export", "name": "CEE_InitWithOpts", "kind": "function", "index": 1665, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111100, "loader_excerpt": "free=wasmExports.free,_malloc=Module._malloc=wasmExports.malloc,Module._CEE_InitWithOpts=wasmExports.CEE_InitWithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30586"></a>
## FND-30586 — module-001 export CEE_DisposeGame

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
{"module_id": "module-001", "direction": "export", "name": "CEE_DisposeGame", "kind": "function", "index": 1672, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120146, "loader_excerpt": "T,c_buf=Module._malloc(c_buf_size);return Module.HEAPU8.set(js_buf,c_buf),[c_buf,c_buf_size]}return{CEE_DisposeGame:(Module,args)=>{let game_point=args[0];Module.ccall(\"CEE_DisposeGame\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_Play:(Module,args)=>{let game_point=args[0],uci_move=args[1],new_game_point=Module.ccall(\"CEE_Play\",\"number\",[\"number\",\"string\"],[game_point,uci_move]);new_game_point<0?postMessage({error:get_last_error(Module)}):postMessage({retval:new_game_point})},CEE_GetLastMove:(Module,args)=>{let game_point=args[0],uci_move=Module.ccall(\"CEE_GetLastMove\",\"string\",[\"number\"],[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30587"></a>
## FND-30587 — module-001 export CEE_DisposeAllGames

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
{"module_id": "module-001", "direction": "export", "name": "CEE_DisposeAllGames", "kind": "function", "index": 1674, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111209, "loader_excerpt": "WithOpts,Module._CEE_DisposeGame=wasmExports.CEE_DisposeGame,Module._CEE_DisposeAllGames=wasmExports.CEE_DisposeAllGames,Module._CEE_Play=wasmExports.CEE_Play,Module._CEE_GetLastMove=wasmExports.CEE_GetLastMove,Module._CEE_NewFeature=wasmExports.CEE_NewFeature,Module._CEE_DisposeFeature=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_Wai", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30588"></a>
## FND-30588 — module-001 export CEE_Play

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
{"module_id": "module-001", "direction": "export", "name": "CEE_Play", "kind": "function", "index": 1680, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120289, "loader_excerpt": "int=args[0];Module.ccall(\"CEE_DisposeGame\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_Play:(Module,args)=>{let game_point=args[0],uci_move=args[1],new_game_point=Module.ccall(\"CEE_Play\",\"number\",[\"number\",\"string\"],[game_point,uci_move]);new_game_point<0?postMessage({error:get_last_error(Module)}):postMessage({retval:new_game_point})},CEE_GetLastMove:(Module,args)=>{let game_point=args[0],uci_move=Module.ccall(\"CEE_GetLastMove\",\"string\",[\"number\"],[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to_c_buf(Module,args[2]),buf=c_buf[0],size=c_buf[1];try{let feature_handle=Module.ccall(\"CEE_NewFeature\",\"number\",[\"number\",\"number\",\"number\",\"nu", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30589"></a>
## FND-30589 — module-001 export CEE_GetLastMove

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
{"module_id": "module-001", "direction": "export", "name": "CEE_GetLastMove", "kind": "function", "index": 1683, "signature": {"parameters": ["i32"], "results": ["i32"]}, "type_index": 2, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120544, "loader_excerpt": ";new_game_point<0?postMessage({error:get_last_error(Module)}):postMessage({retval:new_game_point})},CEE_GetLastMove:(Module,args)=>{let game_point=args[0],uci_move=Module.ccall(\"CEE_GetLastMove\",\"string\",[\"number\"],[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to_c_buf(Module,args[2]),buf=c_buf[0],size=c_buf[1];try{let feature_handle=Module.ccall(\"CEE_NewFeature\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[game_point,feature_id,buf,size]);if(feature_handle<0)return void postMessage({error:get_last_error(Module)});postMessage({retval:feature_handle})}finally{0!==buf&&Module._free(buf)}},CEE_Run:(Module,args)=>{let feature_handle=args[0];return Promis", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30590"></a>
## FND-30590 — module-001 export CEE_NewFeature

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
{"module_id": "module-001", "direction": "export", "name": "CEE_NewFeature", "kind": "function", "index": 1693, "signature": {"parameters": ["i32", "i32", "i32", "i32"], "results": ["i32"]}, "type_index": 10, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 120758, "loader_excerpt": ",[game_point]);uci_move?postMessage({retval:uci_move}):postMessage({error:get_last_error(Module)})},CEE_NewFeature:(Module,args)=>{let game_point=args[0],feature_id=args[1],c_buf=js_buf_to_c_buf(Module,args[2]),buf=c_buf[0],size=c_buf[1];try{let feature_handle=Module.ccall(\"CEE_NewFeature\",\"number\",[\"number\",\"number\",\"number\",\"number\"],[game_point,feature_id,buf,size]);if(feature_handle<0)return void postMessage({error:get_last_error(Module)});postMessage({retval:feature_handle})}finally{0!==buf&&Module._free(buf)}},CEE_Run:(Module,args)=>{let feature_handle=args[0];return Promise.resolve(Module.ccall(\"CEE_Run\",\"number\",[\"number\",\"number\"],[feature_handle,0],{async:!0})).then((ret=>{ret<=0&&postMessage({error:get_last_error(Module)})}))},CEE_DisposeFeature:(Module,args)=>{let game_point=ar", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30591"></a>
## FND-30591 — module-001 export CEE_DisposeFeature

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
{"module_id": "module-001", "direction": "export", "name": "CEE_DisposeFeature", "kind": "function", "index": 1696, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121406, "loader_excerpt": "[feature_handle,0],{async:!0})).then((ret=>{ret<=0&&postMessage({error:get_last_error(Module)})}))},CEE_DisposeFeature:(Module,args)=>{let game_point=args[0];Module.ccall(\"CEE_DisposeFeature\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_data),key_buf=0,key_len=0,success=!1;try{if(\"string\"==typeof model_key){let key_bytes=(new TextEncoder).encode(model_key);key_len=key_bytes.length,key_buf=Module._malloc(key_len+1),Module.HEAPU8.set(key_bytes,key_buf),Module.HEAP", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30592"></a>
## FND-30592 — module-001 export CEE_Run

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
{"module_id": "module-001", "direction": "export", "name": "CEE_Run", "kind": "function", "index": 1698, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 121180, "loader_excerpt": ":get_last_error(Module)});postMessage({retval:feature_handle})}finally{0!==buf&&Module._free(buf)}},CEE_Run:(Module,args)=>{let feature_handle=args[0];return Promise.resolve(Module.ccall(\"CEE_Run\",\"number\",[\"number\",\"number\"],[feature_handle,0],{async:!0})).then((ret=>{ret<=0&&postMessage({error:get_last_error(Module)})}))},CEE_DisposeFeature:(Module,args)=>{let game_point=args[0];Module.ccall(\"CEE_DisposeFeature\",\"void\",[\"number\"],[game_point]),postMessage({retval:1})},CEE_EnableLog:(Module,args)=>{Module.ccall(\"CEE_EnableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_DisableLog:(Module,args)=>{Module.ccall(\"CEE_DisableLog\",\"void\",[],[]),postMessage({retval:1})},CEE_LoadCharmModel:(Module,args)=>{let model_data=args[0],model_key=args[1],[c_buf,c_buf_size]=js_buf_to_c_buf(Module,model_dat", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30593"></a>
## FND-30593 — module-001 export CEE_Stop

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
{"module_id": "module-001", "direction": "export", "name": "CEE_Stop", "kind": "function", "index": 1700, "signature": {"parameters": ["i32", "i32"], "results": []}, "type_index": 1, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111492, "loader_excerpt": "ture=wasmExports.CEE_DisposeFeature,Module._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExp", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30594"></a>
## FND-30594 — module-001 export CEE_Join

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
{"module_id": "module-001", "direction": "export", "name": "CEE_Join", "kind": "function", "index": 1702, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111530, "loader_excerpt": "dule._CEE_Run=wasmExports.CEE_Run,Module._CEE_Stop=wasmExports.CEE_Stop,Module._CEE_Join=wasmExports.CEE_Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsVali", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30595"></a>
## FND-30595 — module-001 export CEE_AddArtifact

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
{"module_id": "module-001", "direction": "export", "name": "CEE_AddArtifact", "kind": "function", "index": 1703, "signature": {"parameters": ["i32", "i32", "i32"], "results": ["i32"]}, "type_index": 4, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 123113, "loader_excerpt": "&&Module._free(c_buf),postMessage(Object.assign({call:\"CEE_LoadApplicabilityIndex_done\"},result))}},CEE_AddArtifact:(Module,args)=>{let artifact=args[0],key=args[1]||null,[c_buf,c_buf_size]=js_buf_to_c_buf(Module,artifact);try{let artifact_id=Module.ccall(\"CEE_AddArtifact\",\"string\",[\"number\",\"number\",\"string\"],[c_buf,c_buf_size,key]);if(!artifact_id)return void postMessage({error:get_last_error(Module)});postMessage({retval:artifact_id})}finally{0!==c_buf&&Module._free(c_buf)}}}}();return function(){var CREATE_KTEP_WORKER_API,Module=null;return(CREATE_KTEP_WORKER_API=function(WasmPath,options){var workerObj,kTepConsole,EngineReady=!1,callInFlight=!1,pendingApiCalls=[],interruptMailbox=makeInterruptMailbox(),interruptCommands={},wait=\"function\"==typeof setImmediate?setImmediate:setTimeout;f", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30596"></a>
## FND-30596 — module-001 export CEE_AddArtifactFromFile

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
{"module_id": "module-001", "direction": "export", "name": "CEE_AddArtifactFromFile", "kind": "function", "index": 1706, "signature": {"parameters": ["i32", "i32"], "results": ["i32"]}, "type_index": 3, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111635, "loader_excerpt": "Join,Module._CEE_AddArtifact=wasmExports.CEE_AddArtifact,Module._CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_comm", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30597"></a>
## FND-30597 — module-001 export CEE_DisposeArtifact

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
{"module_id": "module-001", "direction": "export", "name": "CEE_DisposeArtifact", "kind": "function", "index": 1709, "signature": {"parameters": ["i32"], "results": []}, "type_index": 0, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111699, "loader_excerpt": "_CEE_AddArtifactFromFile=wasmExports.CEE_AddArtifactFromFile,Module._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30598"></a>
## FND-30598 — module-001 export CEE_EnableNotifications

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
{"module_id": "module-001", "direction": "export", "name": "CEE_EnableNotifications", "kind": "function", "index": 1710, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111763, "loader_excerpt": "ule._CEE_DisposeArtifact=wasmExports.CEE_DisposeArtifact,Module._CEE_EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```

<a id="FND-30599"></a>
## FND-30599 — module-001 export CEE_DisableNotifications

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
{"module_id": "module-001", "direction": "export", "name": "CEE_DisableNotifications", "kind": "function", "index": 1711, "signature": {"parameters": [], "results": []}, "type_index": 13, "apparent_purpose": "Named CEE native API; wrapper passes protobuf handles/buffers where present.", "loader_character_offset": 111832, "loader_excerpt": "EnableNotifications=wasmExports.CEE_EnableNotifications,Module._CEE_DisableNotifications=wasmExports.CEE_DisableNotifications,Module._CEE_WaitForNotification=wasmExports.CEE_WaitForNotification,Module._CEE_StopNotificationWaiting=wasmExports.CEE_StopNotificationWaiting,Module._CEE_GetLastError=wasmExports.CEE_GetLastError,Module._CEE_ClearLastError=wasmExports.CEE_ClearLastError,Module._CEE_EnableLog=wasmExports.CEE_EnableLog,Module._CEE_DisableLog=wasmExports.CEE_DisableLog,Module._CEE_IsValidGamePoint=wasmExports.CEE_IsValidGamePoint,Module._uci_interrupt_commands=wasmExports.uci_interrupt_commands,Module._uci_command_after_interrupt=wasmExports.uci_command_after_interrupt,Module._CEE_LoadApplicabilityIndex=wasmExports.CEE_LoadApplicabilityIndex,Module._CEE_LoadCharmModel=wasmExports.CEE", "semantic_confidence": "PROBABLE", "evidence_confidence": "CONFIRMED declaration"}
```
