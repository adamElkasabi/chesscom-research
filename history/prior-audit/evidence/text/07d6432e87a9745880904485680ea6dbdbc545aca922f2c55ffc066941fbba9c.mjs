// Reproducible bounded search. All mutations are research-only config files.
// Ranking loss is NOT an accuracy/rating formula: it compares engine outputs
// against the user-supplied aggregate reference; actual results stay untouched.
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
const dir=path.dirname(new URL(import.meta.url).pathname);
const configs=path.join(dir,'configs'), results=path.join(dir,'results');
fs.mkdirSync(configs,{recursive:true});fs.mkdirSync(results,{recursive:true});
const target={accuracy:{white:71.7,black:99},ratings:{white:100,black:1000},tallies:{
  white:{1:2,2:0,3:0,4:0,5:4,6:1,7:0,8:2,9:1,10:0,11:0,20:0},
  black:{1:2,2:0,3:1,4:2,5:5,6:0,7:0,8:0,9:0,10:0,11:0,20:0}}};
fs.writeFileSync(path.join(dir,'target.json'),JSON.stringify(target,null,2));
const plan=[];const add=(id,config={})=>plan.push({id,...config});
add('baseline',{saveReview:true});
for(const strength of [1,2,3,4])for(const version of [0,1,2]){
 if(strength===1&&version===0)continue;
 add(`strength-${strength}-class-${version}`,{strength,settings:version?{moveClassificationVersion:version}:{}});
}
const options=[
 ['elo-sensitive',{EloSensitivePD:true}],
 ['classification-v3',{ClassificationV3:true}],
 ['forgiving-400',{ForgivingClassificationsElo:400}],
 ['forgiving-1000',{ForgivingClassificationsElo:1000}],
 ['forgiving-2000',{ForgivingClassificationsElo:2000}],
 ['normalize-off',{Normalize:false}],
 ['soft-nodes',{UseSoftNodes:true}],
 ['hard-soft-50',{HardSoftNodeFactor:50}],
 ['hard-soft-200',{HardSoftNodeFactor:200}],
 ['node-fudging-100',{NodeFudging:100}],
 ['node-fudging-1000',{NodeFudging:1000}],
 ['hash-64',{Hash:64}],
 ['clear-between',{ClearBetweenSearches:true}],
 ['multipv-2',{MultiPV:2}],
 ['classification-combo',{EloSensitivePD:true,ClassificationV3:true,ForgivingClassificationsElo:1000}],
];
for(const[id,uciAfter]of options)add('uci-'+id,{uciAfter});
add('tricky-on',{experimental:{allowTrickyClassification:true}});
for(const depth of [12,16,18,22])add('depth-'+depth,{settings:{search:{case:'searchSettings',value:{searchParameters:{depthLimit:depth,numLines:2},nullMoveSearchParameters:{depthLimit:depth,numLines:1}}}}});
for(const nodes of [40000,150000,300000,600000])add('nodes-'+nodes,{settings:{search:{case:'searchSettings',value:{searchParameters:{nodesLimit:nodes,numLines:2},nullMoveSearchParameters:{nodesLimit:nodes,numLines:1}}}}});
add('embedded-human-pvtrees',{pvtrees:{request:{search:{case:'searchParameters',value:{nodesLimit:300000,numLines:1}},torchSearchMode:{mode:{case:'human',value:{}}}},pvtreeOptions:{rating:100}}});
// V2/V3 already gave identical outputs at both Fast and Standard. Avoid
// repeating that inert dimension in expensive Deep/Maximum combinations.
const pruned=[];
for(let i=plan.length-1;i>=0;i--)if(/^strength-[34]-class-[12]$/.test(plan[i].id)){pruned.push(plan[i]);plan.splice(i,1);}
for(const p of plan)if(/^strength-[34]|^depth-(18|22)$/.test(p.id))p.timeoutSeconds=60;
fs.writeFileSync(path.join(dir,'pruned.json'),JSON.stringify({reason:'No numerical effect of explicit V2/V3 at Fast or Standard; prune redundant higher-strength cross-products',configs:pruned},null,2));
const wholeGameSearch={search:{case:'gameReviewSearchSettings',value:{strength:1}}};
// The native whole-game evaluator has an explicit Torch human mode. Test it
// before expensive generic parameter combinations, without relabeling scores.
plan.unshift(
 {id:'evaluate-human',evaluateGame:{...wholeGameSearch,torchSearchMode:{mode:{case:'human',value:{}}}},saveReview:true},
 {id:'evaluate-normal',evaluateGame:wholeGameSearch},
 {id:'evaluate-human-no-maia',evaluateGame:{...wholeGameSearch,torchSearchMode:{mode:{case:'human',value:{disableMaia:true}}}}},
 {id:'evaluate-human-at-root',evaluateAtRoot:true,evaluateGame:{...wholeGameSearch,torchSearchMode:{mode:{case:'human',value:{}}}}}
);
if(process.env.PHASE==='2') {
 const tuned=[];const tune=(id,config={})=>tuned.push({id:'normalized-'+id,...config,uciAfter:{Normalize:false,...config.uciAfter}});
 tune('repeat-1',{saveReview:true}); tune('repeat-2');
 tune('evaluate-normal',{evaluateGame:wholeGameSearch});
 tune('standard',{strength:2});
 tune('class-v2',{settings:{moveClassificationVersion:1}});
 for(const [name,value]of [['UseSoftNodes',true],['HardSoftNodeFactor',50],['HardSoftNodeFactor',200],['NodeFudging',100],['NodeFudging',1000],['Hash',64],['ClearBetweenSearches',true],['Minimal',true]])tune(name+'-'+value,{uciAfter:{[name]:value}});
 for(const nodes of [40000,75000,300000,600000])tune('nodes-'+nodes,{settings:{search:{case:'searchSettings',value:{searchParameters:{depthLimit:6,nodesLimit:nodes,numLines:2},nullMoveSearchParameters:{depthLimit:6,nodesLimit:40000,numLines:1}}}}});
 tune('human',{timeoutSeconds:90,evaluateGame:{...wholeGameSearch,torchSearchMode:{mode:{case:'human',value:{}}}},saveReview:true});
 tune('human-no-maia',{timeoutSeconds:90,evaluateGame:{...wholeGameSearch,torchSearchMode:{mode:{case:'human',value:{disableMaia:true}}}}});

 plan.splice(0,plan.length,...tuned);
}
if(process.env.PHASE==='3') {
 // Local neighborhood of the best phase-2 candidates; no Elo/header tuning.
 const follow=[];const addFollow=(id,options)=>follow.push({id:'followup-'+id,uciAfter:{Normalize:false,...options},saveReview:true});
 addFollow('hash64-repeat',{Hash:64});
 for(const hash of [32,64,128])for(const soft of [false,true])addFollow('hash'+hash+'-soft'+soft,{Hash:hash,UseSoftNodes:soft});
 for(const factor of [50,200])addFollow('soft-factor'+factor,{UseSoftNodes:true,HardSoftNodeFactor:factor});
 plan.splice(0,plan.length,...follow);
}
fs.writeFileSync(path.join(dir,process.env.PHASE?'plan-phase'+process.env.PHASE+'.json':'plan.json'),JSON.stringify(plan,null,2));
function metric(result){
 if(!result.actual)return null;
 let accuracyAbs=0,tallyL1=0,ratingAbs=0;
 for(const c of ['white','black']){
  accuracyAbs+=Math.abs(result.actual.accuracy[c]-target.accuracy[c]);
  ratingAbs+=Math.abs(result.actual.ratings[c]-target.ratings[c]);
  for(const[id,count]of Object.entries(target.tallies[c]))tallyL1+=Math.abs((result.actual.tallies[c][id]||0)-count);
 }
 return {accuracyAbs,tallyL1,ratingAbs,loss:accuracyAbs+2*tallyL1+ratingAbs/100};
}
function leaderboard(){
 const rows=plan.map(p=>{const file=path.join(results,p.id+'.json');if(!fs.existsSync(file))return null;const r=JSON.parse(fs.readFileSync(file));return{id:p.id,...metric(r),actual:r.actual,engines:r.engines,numericHash:r.numericHash,error:r.error,elapsedSeconds:r.elapsedSeconds,warnings:r.warnings}}).filter(Boolean);
 rows.sort((a,b)=>(a.loss??Infinity)-(b.loss??Infinity));
 fs.writeFileSync(path.join(dir,process.env.PHASE?'leaderboard-phase'+process.env.PHASE+'.json':'leaderboard.json'),JSON.stringify({target,ranking:'accuracy absolute error + 2 * tally L1 + rating absolute error / 100',completed:rows.length,planned:plan.length,rows},null,2));
 return rows;
}
let cursor=0,completed=0;
async function worker(){while(cursor<plan.length){
 const config=plan[cursor++];const input=path.join(configs,config.id+'.json'),output=path.join(results,config.id+'.json');
 fs.writeFileSync(input,JSON.stringify(config,null,2));
 if(fs.existsSync(output)){completed++;continue;}
 console.log('START',config.id);
 await new Promise(resolve=>{const p=spawn(process.execPath,[path.join(dir,'trial.mjs'),input,output],{stdio:['ignore','ignore','pipe']});let err='';p.stderr.on('data',x=>err+=x);p.on('exit',code=>{if(!fs.existsSync(output))fs.writeFileSync(output,JSON.stringify({config,error:'exit '+code+' '+err.slice(-2000)}));resolve()})});
 completed++;const rows=leaderboard();const r=rows.find(r=>r.id===config.id);console.log('DONE',completed+'/'+plan.length,config.id,r.error?'ERROR '+r.error.slice(0,180):JSON.stringify({accuracy:r.actual.accuracy,ratings:r.actual.ratings,loss:r.loss,tallyL1:r.tallyL1}));
}}
await Promise.all(Array.from({length:Number(process.env.CONCURRENCY||1)},worker));
const rows=leaderboard();console.log('COMPLETE',rows.length,'trials. Best:',rows.filter(r=>!r.error).slice(0,5).map(r=>[r.id,r.loss]));
