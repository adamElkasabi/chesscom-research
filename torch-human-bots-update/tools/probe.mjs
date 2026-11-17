import fs from 'node:fs';import{createRequire}from'node:module';import crypto from'node:crypto';import{DESCRIPTORS}from'./lib/descriptors.js';
const D=new URL('../evidence/',import.meta.url).pathname;for(const p of fs.readdirSync(D+'native-descriptors'))if(p.endsWith('.bin'))DESCRIPTORS['native/'+p]=fs.readFileSync(D+'native-descriptors/'+p).toString('base64');
for(const d of JSON.parse(fs.readFileSync(D+'current-descriptors.json')))DESCRIPTORS['current/'+d.offset]=d.base64;
const{encodeMessage,decodeMessage}=await import('./lib/protobuf.js');const require=createRequire(import.meta.url);const engineDir=process.env.CEE_DIR;if(!engineDir?.endsWith('/'))throw Error('Set CEE_DIR to an existing directory ending in / with hash-verified original wrapper and WASM.');const mode=process.argv[2]||'legacy';const out={mode,started:new Date().toISOString(),tests:[],networkAttempts:[],binaries:{}};for(const p of ['explanation-engine.js','explanation-engine.wasm'])out.binaries[p]=crypto.createHash('sha256').update(fs.readFileSync(engineDir+p)).digest('hex');let lines=[],pending=[];
console.log=console.warn=console.info=(...x)=>lines.push(x.join(' '));console.error=(...x)=>lines.push('STDERR '+x.join(' '));
globalThis.fetch=async(...a)=>{out.networkAttempts.push(String(a[0]));throw Error('network forbidden by probe fetch hook')};
globalThis.postMessage=m=>{if(typeof m!=='object'||!m)return;let h=pending[0];if(!h)return;if(m.error){pending.shift();h.reject(Error(String(m.error)));return}if(h.call==='CEE_Run'&&m.proto!=null){if(m.is_final){pending.shift();h.resolve(m.proto)}return}if(Object.hasOwn(m,'retval')){pending.shift();h.resolve(m.retval);return}if(m.call===h.call+'_done'){pending.shift();h.resolve(m)}};
const make=require(engineDir+'explanation-engine.js');const engine=make(engineDir+'explanation-engine.wasm',{onmessage:m=>{if(typeof m==='string')lines.push(m);else globalThis.postMessage(m)}});
function api(call,args=[]){return new Promise((resolve,reject)=>{pending.push({call,resolve,reject});try{let p=engine.postMessage({call,args},false,true);p?.catch?.(reject)}catch(e){pending.shift();reject(e)}})}
async function feature(gp,id,name,obj={}){let full='.chesscom.explanation_engine.v1.'+name;const h=await api('CEE_NewFeature',[gp,id,encodeMessage(full,obj)]);try{return decodeMessage(full.replace(/Request$/,'Response'),await api('CEE_Run',[h]))}finally{await api('CEE_DisposeFeature',[h])}}
function finish(code=0){out.elapsedSeconds=(Date.now()-start)/1000;out.logs=lines;out.decodedApiLogs=lines.filter(s=>s.includes('API_LOG: ')).map(s=>Buffer.from(s.split('API_LOG: ')[1],'base64').toString('hex'));fs.writeFileSync((process.env.RESULT_DIR||D)+'runtime-'+mode+'.json',JSON.stringify(out,null,2));process.exit(code)}
const start=Date.now();setTimeout(()=>{out.error='hard timeout 75s';finish(1)},75000);process.on('uncaughtException',e=>{out.error=String(e.stack);finish(1)});process.on('unhandledRejection',e=>{out.error=String(e.stack);finish(1)});
try{
 out.nativeVersion=await feature(-1,2,'CeeVersionRequest',{});
 const ng=await feature(-1,26,'NewGameRequest',{newGame:{from:{case:'pgnGame',value:{pgn:'[Event "Isolated audit probe"]\n\n1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 *',takeFirstGameOnly:true}},settings:{locale:'en_US',userColor:1,search:{case:'gameReviewSearchSettings',value:{strength:1}}}}});const gp=ng.playedLine.at(-1).gamePoint;out.gamePoint=gp;
 if(mode==='legacy'){
  for(const personality of [0,3,5,7,8]){const req={engine:1,options:{rating:1200,adaptive:false,personality,timeLimits:{timeLimitMs:100}}};const i=lines.length,t=Date.now();try{out.tests.push({feature:9,request:req,response:await feature(gp,9,'GetBotMoveRequest',req),seconds:(Date.now()-t)/1000,logStart:i})}catch(e){out.tests.push({feature:9,request:req,error:String(e)})}}
 }else if(mode.startsWith('charm')){
  if(mode!=='charm-missing')out.loadResult=await api('CEE_LoadCharmModel',[new Uint8Array(fs.readFileSync((process.env.CHARM_MODEL||D+'topaz_jackdaw.bin.q8mix'))),'m-topaz-jackdaw']);
  // Synthetic diagnostic configuration using actual schema and public model key, NOT a recovered production bot configuration.
  const protoConfig={id:'audit-diagnostic-only',settings:{searchLimit:{case:'depth',value:2}},mode:{case:'nnmult',value:{nTopNnCandidates:5,nn:{arch:2,model:'m-topaz-jackdaw',rating:1200,weight:1,charmInputSearchDepth:2,temperature:1}}}};
  out.configurationOrigin='Synthetic diagnostic, not production bot values';
  out.tests.push({feature:70,request:{protoConfig},response:await feature(-1,70,'BotConfigResourcesRequest',{protoConfig})});
  const bookConfig={...protoConfig,settings:{...protoConfig.settings,book:{name:'beginner',moveCount:12}}};
  out.tests.push({feature:70,request:{protoConfig:bookConfig},response:await feature(-1,70,'BotConfigResourcesRequest',{protoConfig:bookConfig})});
  out.tests.push({feature:61,request:{protoConfig},response:await feature(gp,61,'BotMoveFromConfigRequest',{protoConfig})});
 }else if(mode.startsWith('human')){
 const request={search:{case:'searchParameters',value:{nodesLimit:1000,numLines:1}}};
 if(mode!=='human-normal')request.torchSearchMode={mode:{case:'human',value:mode==='human-no-maia'?{disableMaia:true}:{}}};
 out.tests.push({feature:29,request,response:await feature(gp,29,'RunSearchRequest',request)});
 }
 finish();
}catch(e){out.error=String(e.stack);finish(1)}
