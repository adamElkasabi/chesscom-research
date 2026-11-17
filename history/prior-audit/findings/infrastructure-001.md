# infrastructure — findings 1–4

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18975"></a>
## FND-18975: Asset probe status206was a deliberate byte-range request

**Category:** infrastructure  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

research/probe.sh runs curl-r0-0,so206with1byte in probe-results is a successful range response,not a complete one-byte engine. Full assets downloaded separately; do not interpret size1 as corruption or availability of full content.

### Evidence

- **SRC-0203** `research/probe.sh` — [preserved redacted evidence](../evidence/text/43b66e3ac963667b2df470e692dd1510b95f807056031e17e613ab51ae2f85a2.sh)
  Character offset 274.

```text
rl -sS -o /dev/null -m 20 -A "$UA" -w '%{http_code} %{size_download} %{content_type} %{time_total}' -r 0-0 "$u" 2>/dev/null)
  printf '%-100s %s\n' "$u" "$out"
}
export -f probe
export UA
cat research/urls.txt | xargs -P 8 -I{} bash -c 'probe "{}"'

```
- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)

**Source references:** SRC-0203, SRC-0202  
**URL references:** None independently associated  
**Related findings:** FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18976"></a>
## FND-18976: Torch multipart loader explains some guessed-path404s

**Category:** infrastructure  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Probe records show404for some guessed full Torch wasm URLs. Download script instead fetches torch-2-single-697050e-part-0..5.wasm and exact existing lite assets. Preserve both observed failed URLs and actual part patterns; no need to re-probe.

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
- **SRC-0064** `fetch-assets.sh` — [preserved redacted evidence](../evidence/text/4fd21605ac735ee70e6717867eb17d057b430580a6adf2918d177c00aef42751.sh)
  Character offset 1483.

```text
-2-single.js" &
for i in 0 1 2 3 4 5; do
  get "r2/assets-chess-engine/Torch/torch-2-single-697050e-part-$i.wasm" "$D/torch/torch-2-single-part-$i.wasm" &
done
get 'r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js'   "$D/torch-lite/torch-2-lite-single.js" &
get 'r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm' "$D/torch-lite/torch-2-lite-single.wasm" &
wait
# --- stockfish ---
get 'bundles/ap
```

**Source references:** SRC-0202, SRC-0064  
**URL references:** None independently associated  
**Related findings:** FND-18975, FND-18986, FND-20342, FND-20462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18977"></a>
## FND-18977: Dependency delivery is versioned and hashed

**Category:** infrastructure  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Saved HTML/play/analysis imports include /r2/client-packages/<package>/<date>/ files,hashed chunk names,/r2/assets-chess/vite/vendors Vue/Pinia imports,engine versions/default/no-simd. These are exposed deployment indicators,not proof of backend framework or hosting vendor.

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 2971.

```text
uage-banner-scripts-type" content="module">



  
    
    
    
      <link rel="stylesheet" href="/r2/client-packages/navigation/2026.11.5/navigation-logged-out-global-styles.HBnLJ7dK8H.css" />
<link rel="stylesheet" href="/r2/client-packages/navigation/2026.11.5/shared.DO_T7DKtPD.css" />
<link rel="stylesheet" href="/r2/client-packages/navigation/2026.11.5/navigation-logged-out.css" />
  

    
  
  
  
  
       
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 3069.

```text
"language-banner-scripts-type" content="module">

    
    
    
      <link rel="stylesheet" href="/r2/client-packages/checkmate/2026.11.13/checkmate.css" />
  


  
    
    
    
      <link rel="stylesheet" href="/r2/client-packages/navigation/2026.11.5/navigation-logged-out-global-styles.HBnLJ7dK8H.css" />
<link rel="stylesheet" href="/r2/client-packages/navigation/2026.11.5/shared.DO_T7DKtPD.css" />
<link rel="
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 121365.

```text
as n,n as r,r as i,t as a}from"./rolldown-runtime.CxRJo09Adt.chunk.js";import{createPinia as o}from"/r2/assets-chess/vite/vendors/pinia.5dQ-li5PSR.js";import{Fragment as s,Transition as c,computed as l,createApp as u,createBlock as d,createCommentVNode as f,createElementBlock as p,createElementVNode as m,createTextVNode as h,createVNode as g,customRef as _,defineAsyncComponent as v,defineComponent as y,getCurrentInst
```

**Source references:** SRC-0065, SRC-0777, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-19909, FND-19910, FND-18979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18978"></a>
## FND-18978: Frontend libraries do not identify the backend

**Category:** infrastructure  
**Classification:** inference  
**Verification:** partially verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Imports establish Vue,Pinia,Vite/Rolldown-style bundles and Sentry integration in saved frontend. Generated route metadata resembles Symfony routing but does not prove a PHP/Symfony backend deployment or database engine. Exact library versions are unknown unless present literally.

### Evidence

- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)
  Character offset 14631.

```text
emplateRef as yh,watch as bh,withAsyncContext as xh,withCtx as $}from"/r2/assets-chess/vite/vendors/vue.CvfZVBJC9Z.js";function Sh(){return window.innerWidth<960}var Ch=t((()=>{})),wh,Th,Eh,Dh,Oh,kh,Ah,jh,Mh,Nh,Ph,Fh,Ih,Lh,Rh,zh,Bh,Vh,Hh,Uh,Wh,Gh,Kh,qh,Jh,Yh,Xh,Zh,Qh,$h,eg,tg,ng,rg,ig,ag,og=t((()=>{wh=`63.999em`,Th=`68.749em`,Eh=`74.999em`,Dh=`78.124em`,Oh=`87.499em`,kh=`20.624em`,Ah=`24.999em`,jh=`29.999em`,Mh=`34.3
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 25074.

```text
icComponent as te,toDisplayString as ne,unref as _,withCtx as re}from"/r2/assets-chess/vite/vendors/vue.CvfZVBJC9Z.js";import{createPinia as ie}from"/r2/assets-chess/vite/vendors/pinia.5dQ-li5PSR.js";var ae=Object.create,oe=Object.defineProperty,se=Object.getOwnPropertyDescriptor,ce=Object.getOwnPropertyNames,v=Object.getPrototypeOf,le=Object.prototype.hasOwnProperty,y=(e,t,n)=>()=>{if(n)throw n[0];try{return e&&(t=e
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 122494.

```text
tx as Me,withDirectives as Ne,withKeys as Pe,withModifiers as Fe}from"/r2/assets-chess/vite/vendors/vue.CvfZVBJC9Z.js";function A(e,t,n){if(typeof e==`function`?e===t:e.has(t))return arguments.length<3?t:n;throw TypeError(`Private element is not present on this object`)}var Ie=r((()=>{}));function Le(e,t){if(t.has(e))throw TypeError(`Cannot initialize the same private elements twice on an object`)}var Re=r((()=>{}));
```

**Source references:** SRC-0780, SRC-0751, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18139, FND-18142, FND-18205, FND-18117, FND-18118

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
