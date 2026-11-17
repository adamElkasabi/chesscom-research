// Holdout validation: do not select new options using these games.
import fs from 'node:fs';
import path from 'node:path';
import {spawn} from 'node:child_process';
const dir=path.dirname(new URL(import.meta.url).pathname),dest=path.join(dir,'holdout');fs.mkdirSync(dest,{recursive:true});
const references={
 'human-game':{accuracy:{white:76.8,black:70.2},ratings:{white:1350,black:600},tallies:{white:{3:1,4:13,5:12,8:2,10:1,9:1},black:{3:0,4:10,5:9,8:6,10:3,9:0}}},
 'example-game':{accuracy:{white:86.8,black:79.8},ratings:{white:1850,black:1500},tallies:{white:{3:4,4:20,5:22,8:0,10:1,9:0},black:{3:0,4:18,5:21,8:5,10:1,9:1}}},
};
const results=[];
for(const fixture of Object.keys(references))for(const variant of [
 {name:'baseline',options:{Normalize:true}},
 {name:'normalize-off',options:{Normalize:false}},
 {name:'refined-hash64',options:{Normalize:false,Hash:64}},
]){
 const config={id:fixture+'-'+variant.name,fixture,settings:{userColor:fixture==='example-game'?1:2},uciAfter:variant.options,timeoutSeconds:200};
 const input=path.join(dest,config.id+'.config.json'),output=path.join(dest,config.id+'.json');
 fs.writeFileSync(input,JSON.stringify(config,null,2));
 if(!fs.existsSync(output)){
  console.log('START',config.id);
  await new Promise(resolve=>{const p=spawn(process.execPath,[path.join(dir,'trial.mjs'),input,output],{stdio:'ignore'});p.on('exit',(code,signal)=>{if(!fs.existsSync(output))fs.writeFileSync(output,JSON.stringify({config,error:'exit '+code+' signal '+signal}));resolve()})});
 }
 const r=JSON.parse(fs.readFileSync(output)),target=references[fixture];
 const error={accuracyAbs:0,ratingAbs:0,displayedTalliesL1:0};
 if(r.actual)for(const c of ['white','black']){
  error.accuracyAbs+=Math.abs(r.actual.accuracy[c]-target.accuracy[c]);
  error.ratingAbs+=Math.abs(r.actual.ratings[c]-target.ratings[c]);
  for(const[k,count]of Object.entries(target.tallies[c]))error.displayedTalliesL1+=Math.abs((r.actual.tallies[c][k]||0)-count);
 }
 results.push({id:config.id,target,actual:r.actual,error:r.error||error,engines:r.engines,speech:r.speech});
 fs.writeFileSync(path.join(dir,'holdout-validation.json'),JSON.stringify(results,null,2));
 console.log('DONE',config.id,JSON.stringify({actual:r.actual?.accuracy,ratings:r.actual?.ratings,error:r.error||error}));
}
console.log('HOLDOUT VALIDATION COMPLETE');
