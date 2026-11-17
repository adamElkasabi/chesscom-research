// Isolated real-wasm trial. Research only: never imported by the extension.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import crypto from 'node:crypto';
import { DESCRIPTORS } from '../../extension/lib/descriptors.js';
const here = path.dirname(new URL(import.meta.url).pathname);
for (const name of fs.readdirSync(path.join(here, 'wasm-descriptors'))) {
  if (!name.endsWith('.bin')) continue;
  // The registry uses the embedded file name, not this synthetic key.
  DESCRIPTORS['research/' + name] = fs.readFileSync(path.join(here, 'wasm-descriptors', name)).toString('base64');
}
const { encodeMessage, decodeMessage } = await import('../../extension/lib/protobuf.js');
const config = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const outfile = process.argv[3];
const lines = [], pending = [];
const output = { config, started: new Date().toISOString() };
const require = createRequire(import.meta.url);
const enginePath = path.resolve(here, '../../extension/engines/cee');
console.log = console.info = console.warn = () => {};
console.error = (...args) => lines.push('STDERR ' + args.map(String).join(' '));
globalThis.postMessage = message => {
  if (typeof message !== 'object' || !message) return;
  const head = pending[0]; if (!head) return;
  if (message.error) { pending.shift(); head.reject(new Error(String(message.error))); return; }
  if (head.call === 'CEE_Run' && message.proto != null) {
    if (message.is_final) { pending.shift(); head.resolve(message.proto); }
    return;
  }
  if (Object.hasOwn(message,'retval')) { pending.shift(); head.resolve(message.retval); }
};
globalThis.fetch = async (...args) => { output.networkAttempts ??= []; output.networkAttempts.push(String(args[0])); throw new Error('Network forbidden in local Torch Human probe'); };
const make = require(path.join(enginePath,'explanation-engine.js'));
const engine = make(path.join(enginePath,'explanation-engine.wasm'), { onmessage: message => {
  if (typeof message === 'string') lines.push(message);
  else globalThis.postMessage(message);
} });
function api(call,args=[]) { return new Promise((resolve,reject) => {
  pending.push({call,resolve,reject});
  try { const p=engine.postMessage({call,args},false,true); p?.catch?.(reject); } catch(e) { pending.shift();reject(e); }
}); }
async function feature(gp,id,name,obj={}) {
  if (!name.startsWith('.')) name='.chesscom.explanation_engine.v1.'+name;
  const handle=await api('CEE_NewFeature',[gp,id,encodeMessage(name,obj)]);
  try{return decodeMessage(name.replace(/Request$/,'Response'),await api('CEE_Run',[handle]));}
  finally{await api('CEE_DisposeFeature',[handle]);}
}
async function uci(options) {
  for (const [name,value] of Object.entries(options||{})) await engine.postMessage(`setoption name ${name} value ${value}`,false,true);
}
function finish(code=0) {
  output.warnings=lines.filter(s=>/warning|error|unknown|wrong|not supported/i.test(s)).map(s=>s.slice(0,1000));
  fs.mkdirSync(path.dirname(outfile),{recursive:true});fs.writeFileSync(outfile,JSON.stringify(output,null,2));process.exit(code);
}
process.on('uncaughtException',error=>{output.error=String(error.stack||error);finish(1)});
process.on('unhandledRejection',error=>{output.error=String(error.stack||error);finish(1)});
setTimeout(()=>{output.error='trial timeout after '+(config.timeoutSeconds||150)+'s';finish(1)},(config.timeoutSeconds||150)*1000);
const start=Date.now();
try {
  await uci(config.uciBefore);
  const fixture=config.fixture||'doting-prospect';
  const pgn=fs.readFileSync(path.join(here,'../fixtures',fixture+'.pgn'),'utf8');
  const settings={ locale:'en_US', userColor:2, enableSkills:true,
    search:{case:'gameReviewSearchSettings',value:{strength:config.strength||1}}, ...config.settings };
  const ng=await feature(-1,26,'NewGameRequest',{newGame:{from:{case:'pgnGame',value:{pgn,takeFirstGameOnly:true}},settings}});
  const root=ng.playedLine[0].gamePoint;
  await uci(config.uciAfter);
  if(config.experimental) output.experimental=await feature(root,46,'UpdateExperimentalOptionsRequest',{options:config.experimental});
  if(config.evaluateGame) {
    const evaluation=await feature(config.evaluateAtRoot?root:ng.playedLine.at(-1).gamePoint,54,'EvaluateGameRequest',{
      startingGamePoint:root, ...config.evaluateGame,
    });
    output.evaluateGame={progress:evaluation.progress,count:evaluation.evaluatedPositionsCount,source:evaluation.gameState?.defaultEvalSourceEngine};
  }
  if(config.pvtrees) {
    output.pvtrees=await feature(root,288,'.chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesRequest',config.pvtrees);
  }
  if(config.preSearch) {
    output.preSearch=[];
    for(const point of (config.rootOnly?ng.playedLine.slice(0,1):ng.playedLine)){
      const rs=await feature(point.gamePoint,29,'RunSearchRequest',config.preSearch);
      output.preSearch.push({gamePoint:point.gamePoint,score:rs.evaluations?.[0]?.score,response:rs});
      if(config.addPreSearch)await feature(point.gamePoint,1,'AddEvaluationsRequest',{evaluations:rs.evaluations});
    }
  }
  if(config.searchOnly){output.elapsedSeconds=(Date.now()-start)/1000;output.searchLogs=lines.slice(-30);finish();}
  const response=await feature(root,42,'GameReviewRequest',{startingGamePoint:root});
  const g=response.gameReview;
  const h=g.highlights;
  output.actual={accuracy:h.accuracy,ratings:Object.fromEntries(['white','black'].map(c=>[c,h.reportCard?.[c]?.gameRatingV2??h.reportCard?.[c]?.effectiveRating])),
    tallies:Object.fromEntries(['white','black'].map(c=>[c,Object.fromEntries(h.classificationTallies[c].map(t=>[t.moveClassification,t.tally||0]))]))};
  output.engines=[...new Set(g.evalGraph.evalGraphTicks.map(t=>t.moveScore?.engine))];
  output.numericHash=crypto.createHash('sha256').update(JSON.stringify(output.actual)).digest('hex');
  output.actualSettings=(await feature(root,14,'GetGameStateRequest',{})).gameState?.gameSettings;
  output.speech={sentences:0,hashes:0};
  for(const move of g.review.playedMoves)for(const s of move.playedMove?.speech?.sentences||[]){output.speech.sentences++;if(s.audioUrlHash)output.speech.hashes++}
  output.elapsedSeconds=(Date.now()-start)/1000;
  if(config.saveReview)output.gameReview=g;
  finish();
} catch(error){output.error=String(error.stack||error);finish(1)}
