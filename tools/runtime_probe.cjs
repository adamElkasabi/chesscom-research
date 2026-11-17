// Controlled structural instantiation, not a game review or a cloud-parity test.
const fs=require('node:fs');
const filename=process.argv[2];
globalThis.fetch=()=>{throw Error('network forbidden')};
const begin=process.hrtime.bigint();
const bytes=fs.readFileSync(filename);const moduleObject=new WebAssembly.Module(bytes);
const descriptors=WebAssembly.Module.imports(moduleObject), imports={},calls=[];
const structure=process.argv[3]?JSON.parse(fs.readFileSync(process.argv[3],'utf8')):null;
for(const imp of descriptors){imports[imp.module]??={};if(imp.kind==='function')imports[imp.module][imp.name]=(...args)=>{if(calls.length<30)calls.push({module:imp.module,name:imp.name,args:args.map(x=>typeof x==='bigint'?String(x):x)});return 0;};else if(imp.kind==='memory' && structure){const d=structure.imports.find(x=>x.module===imp.module && x.name===imp.name).limits;imports[imp.module][imp.name]=new WebAssembly.Memory({initial:d.minimum,maximum:d.maximum,shared:d.shared});}else throw Error('Non-function import requires explicit descriptor-aware mock: '+JSON.stringify(imp));}
const instance=new WebAssembly.Instance(moduleObject,imports);
const memories=Object.entries(instance.exports).filter(([n,x])=>x instanceof WebAssembly.Memory).map(([name,x])=>({name,bytes:x.buffer.byteLength,shared:typeof SharedArrayBuffer!=='undefined'&&x.buffer instanceof SharedArrayBuffer}));
const output={status:'instantiated with function import stubs',imports:descriptors.length,exports:WebAssembly.Module.exports(moduleObject).length,memories,import_calls_during_instantiation:calls,elapsed_ms:Number(process.hrtime.bigint()-begin)/1e6,algorithm_calls:[],limitation:'No wrapper runtime constructors/search/review invoked; stub instantiation is not a functional engine validation. No original application inputs used.'};
// Address/stack queries have no caller-controlled pointers and no data mutation.
for(const name of ['emscripten_stack_get_base','emscripten_stack_get_end','emscripten_stack_get_current'])if(typeof instance.exports[name]==='function'){try{output.algorithm_calls.push({name,result:instance.exports[name]()});}catch(e){output.algorithm_calls.push({name,error:String(e)});}}
console.log(JSON.stringify(output,null,2));
