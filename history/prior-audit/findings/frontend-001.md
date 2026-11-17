# frontend — findings 1–7

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18917"></a>
## FND-18917: Quick Analysis has a dedicated lazy client

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The example game page package is play2026.11.4. Static dependency tracing reaches client.e0da4c65.BIjoPk3wAJ.chunk.js. Its store extension.quick-analysis keeps resultsMap,engine,evaluationEngines,cee,preloadAssetsPromise,pendingBrilliantVerifications. Package imports are code observations, not proof all clients initialize for every session.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
- **SRC-0765** `research/refinement/live-chunks/shared.b9742e37.Cgvw1kitOr.chunk.js` — [preserved redacted evidence](../evidence/text/e8926465fd4ff293b5496aa7f47c964b3aa6acfc548b48ab3ac5faeb3a3a76ac.js)
  Character offset 1276.

```text
ind`,Tricky:`tricky`,Inaccuracy:`inaccuracy`,Miss:`miss`,Mistake:`mistake`}})),c,l=e((()=>{n(),c=t(`extension.quick-analysis`,()=>({resultsMap:a(new Map),engine:null,evaluationEngines:[],cee:null,preloadAssetsPromise:null,pendingBrilliantVerifications:a(new Set)}))}));function u(e){return c().resultsMap.get(e)||null}var d=e((()=>{l()}));function f(e){return+(i(e)===1)}var p=e((()=>{r()}));export{u as a,c,s as i,p as 
```

**Source references:** SRC-0752, SRC-0765  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18918, FND-19435, FND-19824

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18918"></a>
## FND-18918: Quick Analysis binary-interface gate

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

An() tests web_quick_analysis_cee_binary_interface. The binary path calls createNewGame then getGameReview; the old path initializes CEE plus separate evaluation engines and fetches analysis.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
  Character offset 4061.

```text
ll}).filter(e=>e!==null)}var kn=t((()=>{}));function An(){return window.chesscom.features.includes(`web_quick_analysis_cee_binary_interface`)}var jn=t((()=>{}));function Mn(){return window.chesscom.features.includes(`web_verify_brilliant_engine_match`)}var Nn=t((()=>{}));function Pn(e,t){return new Promise((n,r)=>{let i=setTimeout(()=>{e.quit(),r(Error(`Engine not ready after ${t}ms`))},t);e.isready(()=>{clearTimeout
```

**Source references:** SRC-0752  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18917

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18919"></a>
## FND-18919: Quick Analysis binary search settings

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

G defines defaultDepth10,multiPv2. $i creates NewGame with searchSettings/searchParameters depthLimit10,numLines2. Coach mode selects classificationV3 and userColor; no-coach mode selects V2. These are not the named Torch Human+Fast whole-review settings.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
  Character offset 3766.

```text
urprised`,`happy`,`sad`,`impressed`,`shocked`,`thinking`,`concerned`,`greeting`]})),G,En=t((()=>{G={defaultDepth:10,multiPv:2}})),K,Dn=t((()=>{K={ceeFetch:3e4,initialTimeout:15e3,retryTimeout:6e4,bestMove:1e4}}));function On(e){return e.map(e=>{let t=e.filter(e=>e!==null);return t.length>0?t:null}).filter(e=>e!==null)}var kn=t((()=>{}));function An(){return window.chesscom.features.includes(`web_quick_analysis_cee_bi
```

**Source references:** SRC-0752  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18917, FND-18918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18920"></a>
## FND-18920: Legacy Quick Analysis supplies external evaluations

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

lr returns action analysis,evals,moves,startFen,variant,WhiteElo,BlackElo,ClassificationV3true,DoProgressUpdatestrue,uciCommands. hr builds evaluation workers from engine asset paths, and br/xr distribute position searches. This is separate from the CEE internal search route.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
  Character offset 6865.

```text
:`analysis`,evals:e,moves:t,startFen:n.startingFen,variant:n.variant,options:{WhiteElo:i,BlackElo:a,ClassificationV3:!0,DoProgressUpdates:!0},uciCommands:r}}var ur=t((()=>{de()}));async function dr(e,t,n,r=K.bestMove,i={}){if(window.chesscom.features.includes(`fix_evaluation_engine_fetch_timeout`))return fr(e,t,n,r,i);let a=new Promise(r=>{let i=Array(n);e.getBestMove(t,()=>r(i),e=>{pr(e)&&e.multipv&&(i[e.multipv-1]=
```

**Source references:** SRC-0752  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18917, FND-18918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18921"></a>
## FND-18921: Quick Analysis worker parallelism derives from device concurrency

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

kr uses navigator.hardwareConcurrency fallback1, a special condition returning1, otherwise max(floor(concurrency/2)-1,1). This worker-count policy is distinct from sequential research trials that avoid sandbox OOM.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
  Character offset 13526.

```text
nt:0,excellent:0,good:0,greatFind:0,tricky:0,inaccuracy:0,miss:0,mistake:0}}}}var Or=t((()=>{v()}));function kr(){let e=window?.navigator?.hardwareConcurrency??1;return bt()?1:Math.max(Math.floor(e/2)-1,1)}var Ar=t((()=>{ze()}));async function jr(e,t=[]){let n=B();if(n.engine?.fetchRequestId===e)return;if(await qn(),n.engine&&(Un(n.engine.fetchRequestId),q()),window.chesscom.mockQuickAnalysisResponse!==void 0){n.resu
```

**Source references:** SRC-0752  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18917, FND-18918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18923"></a>
## FND-18923: Binary debug switch has initialization requirements

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Ri checks location.search for logBIMessages. Ni creates binary client with a Pi logger when enabled; Pi exposes window.chesscom.getCeeBinaryInterfaceLogs. This function does not have to exist before that client initializes or in another frame/isolated world.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
  Character offset 28814.

```text
mes??[]]},n.mechanism&&delete n.mechanism.exception_id,{...e,exception:{...e.exception,values:[n]}}}function Ri(){return window.location.search.includes(`logBIMessages`)}var zi=t((()=>{Mi(),ye(),M(),_t()}));function Bi(){let e=B();if(!e.cee){let t=Ni();e.cee={client:t,ready:t.getCeeVersion({}).then(()=>{},n=>{throw e.cee?.client===t&&(t.dispose(),e.cee=null),n})}}return e.cee.ready}var Vi=t((()=>{H(),zi()}));function
```

**Source references:** SRC-0752  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18917, FND-18918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18925"></a>
## FND-18925: CEE asset version and SIMD selection are flag-dependent

**Category:** frontend  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Saved live-shared eager source chooses R2 assets when explanation_engine_r2 is enabled outside dev/test; WJ selects default package1.130.285 or staff-config version/fallback1.130.254. explanation_engine_no_simd and WebAssembly SIMD validation choose default/no-simd. Legacy fallback uses bundles/app/js/vendor/explanation-engine or -staff.

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1912205.

```text
,{value:3,label:()=>`3`},{value:4,label:()=>`4`},{value:5,label:()=>`5`}]},read:[HJ],write:[HJ]}}));function act(){return!!window.chesscom?.features?.includes(`explanation_engine_r2`)&&window.context.environment!==`dev`&&window.context.environment!==`test`}function WJ(){if(window.chesscom?.features?.includes(`explanation_engine_staff`)){let e=window.chesscom?.featuresConfig?.explanation_engine_staff;return e?.version
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
