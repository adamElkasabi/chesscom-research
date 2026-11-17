import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import { ReviewProgressEstimator } from '../lib/progress.js';

const key='Fast';
const m=new ReviewProgressEstimator();
assert.equal(m.begin({plies:20,searchKey:key},0).expectedMs,null);
assert.equal(m.progress(5000),null,'no invented first-run duration');
m.complete(10000);
assert.equal(m.begin({plies:20,searchKey:key},0).expectedMs,10000);
assert.ok(Math.abs(m.progress(5000)-0.485)<1e-9);
assert.equal(m.progress(1e9),0.95,'late review never claims completion');
m.cancel();
assert.equal(m.begin({plies:41,searchKey:key},0).expectedMs,20000,'scale by position count');
assert.equal(m.begin({plies:20,searchKey:'Deep'},0).expectedMs,null,'do not mix strengths');
const robust=new ReviewProgressEstimator([10000,11000,900000].map(durationMs=>({plies:20,searchKey:key,durationMs})));
assert.equal(robust.begin({plies:20,searchKey:key},0).expectedMs,11000,'median resists slow outlier');
assert.equal(new ReviewProgressEstimator([{plies:-1,searchKey:key,durationMs:100}]).samples.length,0);
console.log('PASS timing model: calibration, scaling, strengths, median, cap');

// Execute the actual offscreen message handler with a deterministic engine/clock.
const source=fs.readFileSync(new URL('../offscreen.js',import.meta.url),'utf8').replace(/^import .*;\n/gm,'');
const disk=new Map();
async function simulate({fail=false,cancel=false,storageFails=false}={}) {
 let now=0, listener;
 const timers=new Map(),messages=[],logs=[];
 let nextTimer=0;
 const port={postMessage:m=>messages.push(m),onMessage:{addListener:f=>{listener=f}},onDisconnect:{addListener(){}}};
 const localStorage={getItem:k=>{if(storageFails)throw Error('blocked');return disk.get(k)||null},setItem:(k,v)=>{if(storageFails)throw Error('blocked');disk.set(k,v)}};
 const context=vm.createContext({ReviewProgressEstimator,localStorage,Uint8Array,ArrayBuffer,
  performance:{now:()=>now},console:{log:(...x)=>logs.push(x.join(' ')),warn(){},error(){}},
  window:{addEventListener(){}},chrome:{runtime:{connect:()=>port}},
  setTimeout:()=>0,setInterval:f=>{const n=++nextTimer;timers.set(n,f);return n},clearInterval:n=>timers.delete(n),
  btoa,atob,
  frame:x=>x,encodeMessage:(_type,obj)=>new TextEncoder().encode(JSON.stringify(obj)),decodeMessage:()=>({}),
  buildGameReview:async opts=>{
   opts.onProgress(0);opts.onWorkload({plies:20,searchKey:key});opts.onProgress(0.02);
   for(const time of [2500,5000,15000]) {now=time;for(const tick of timers.values())tick()}
   if(cancel)listener({kind:'socket-close',session:'test'});
   if(fail)throw Error('test engine failed');
   opts.onProgress(1);
   return {bytes:new TextEncoder().encode(JSON.stringify({result:{case:'success',value:{accuracy:'untouched'}}})),stats:{moves:20,accuracy:{white:60,black:95}}};
  },
 });
 vm.runInContext(source,context);
 await vm.runInContext("run({session:'test',data:'AQ=='})",context);
 const frames=messages.filter(m=>m.kind==='feed').map(m=>JSON.parse(Buffer.from(m.data,'base64').toString()));
 return {frames,logs,timers,messages};
}
const first=await simulate();
assert.deepEqual(first.frames.filter(x=>x.result.case==='progress').map(x=>x.result.value.progress),[0,0,0.02,0.02,0.02,0.02,1]);
assert.ok(first.logs.some(x=>x.includes('calibration')));
assert.equal(first.timers.size,0);
assert.equal(JSON.parse([...disk.values()][0]).length,1);
const second=await simulate();
const ps=second.frames.filter(x=>x.result.case==='progress').map(x=>x.result.value.progress);
assert.ok(ps.some(x=>x>0.02&&x<0.95),'history restored and intermediate estimate emitted');
assert.equal(ps.at(-2),0.95);assert.equal(ps.at(-1),1);
assert.ok(ps.every((x,i)=>!i||x>=ps[i-1]),'never move backward');
assert.equal(second.frames.at(-1).result.value.accuracy,'untouched');
assert.ok(second.logs.some(x=>x.includes('ESTIMATED')));
const count=JSON.parse([...disk.values()][0]).length;
const failed=await simulate({fail:true});
assert.equal(JSON.parse([...disk.values()][0]).length,count,'failures do not train model');
assert.equal(failed.frames.at(-1).result.case,'failure');
await simulate({cancel:true});
assert.equal(JSON.parse([...disk.values()][0]).length,count,'cancelled reviews do not train model');
await simulate({storageFails:true});
console.log('PASS actual offscreen flow: warm/cold history, estimated frames, real completion, cancellation, errors, unavailable storage');
