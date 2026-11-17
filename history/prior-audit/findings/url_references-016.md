# url_references — findings 1501–1600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-20632"></a>
## FND-20632: bundles/web/voice/vosk.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/web/voice/vosk.js",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01501"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2627705.

```text
ading;let n={kind:`vosk`,modelUrl:yN(`bundles/web/voice/chess.model.tar.gz`),workerUrl:yN(`bundles/web/voice/vosk.js`)};await amt(n);let r=rmt({stt:n},{onReady:()=>{t.status.recognizer=_m.Idle},onPermissionC
```

**Source references:** SRC-0781  
**URL references:** <bundles/web/voice/vosk.js>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20633"></a>
## FND-20633: git+https://github.com/ChessCom/client-packages.git

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "git+https://github.com/ChessCom/client-packages.git",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-0782",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01502"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232705.

```text
ine`,Sle=`1.130.254`,Cle=`WASM build of internal Explanation Engine`,wle={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Tle={registry:`https://npm.pkg.github.com/`},Ele=`UNLICENSED`,Dle=`https://github.com/C
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 233491.

```text
ine`,Ple=`1.130.285`,Fle=`WASM build of internal Explanation Engine`,Ile={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Lle={registry:`https://npm.pkg.github.com/`},to=`UNLICENSED`,no=`https://github.com/Che
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344236.

```text
/../build/bin/build release @chesscom/play-client`},Mye=`UNLICENSED`,Nye={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Pye={registry:`https://npm.pkg.github.com/`},Fye=[`dist/*`,`release-history.md`],Iye={e
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10034.

```text
ine`,Ple=`1.130.285`,Fle=`WASM build of internal Explanation Engine`,Ile={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Lle={registry:`https://npm.pkg.github.com/`},to=`UNLICENSED`,no=`https://github.com/Che
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10906.

```text
ine`,Sle=`1.130.254`,Cle=`WASM build of internal Explanation Engine`,wle={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Tle={registry:`https://npm.pkg.github.com/`},Ele=`UNLICENSED`,Dle=`https://github.com/C
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246443.

```text
ine`,Hse=`1.130.254`,Use=`WASM build of internal Explanation Engine`,Wse={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Gse={registry:`https://npm.pkg.github.com/`},Kse=`UNLICENSED`,qse=`https://github.com/C
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 247235.

```text
ine`,ece=`1.130.285`,tce=`WASM build of internal Explanation Engine`,nce={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},rce={registry:`https://npm.pkg.github.com/`},ice=`UNLICENSED`,ace=`https://github.com/C
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246443.

```text
ine`,Hse=`1.130.254`,Use=`WASM build of internal Explanation Engine`,Wse={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Gse={registry:`https://npm.pkg.github.com/`},Kse=`UNLICENSED`,qse=`https://github.com/C
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 247235.

```text
ine`,ece=`1.130.285`,tce=`WASM build of internal Explanation Engine`,nce={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},rce={registry:`https://npm.pkg.github.com/`},ice=`UNLICENSED`,ace=`https://github.com/C
```

**Source references:** SRC-0781, SRC-0782, SRC-1137, SRC-1165  
**URL references:** <git+https://github.com/ChessCom/client-packages.git>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-19886, FND-20489

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20634"></a>
## FND-20634: http://_

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://_",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01503"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 313010.

```text
(n^n>>>13,3266489909),4294967296*(2097151&r)+(n>>>0)}function Zme(e){try{let t=new URL(e,`http://_`);return`${t.pathname}${t.search}${t.hash}`}catch{return e}}function ef(e,t,n){return Xme
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 317993.

```text
(n^n>>>13,3266489909),4294967296*(2097151&r)+(n>>>0)}function Ede(e){try{let t=new URL(e,`http://_`);return`${t.pathname}${t.search}${t.hash}`}catch{return e}}function Af(e,t,n){return Tde
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 317993.

```text
(n^n>>>13,3266489909),4294967296*(2097151&r)+(n>>>0)}function Ede(e){try{let t=new URL(e,`http://_`);return`${t.pathname}${t.search}${t.hash}`}catch{return e}}function Af(e,t,n){return Tde
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <http://_>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20635"></a>
## FND-20635: http://github.com/nmrugg/stockfish.js)

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://github.com/nmrugg/stockfish.js)",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1141",
    "SRC-1169"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01504"
}

### Evidence

- **SRC-1141** `research/stockfish.js` — [preserved redacted evidence](../evidence/text/2a9661e708b82108c4f17405a8a29093c99bebf5b50ace7fb0d244a22bedb8ec.js)
  Character offset 21.

```text
/*!
 * Stockfish.js (http://github.com/nmrugg/stockfish.js)
 * License: GPL
 */
var Stockfish;
function INIT_ENGINE()
{
var STOCKFISH = function (con
```
- **SRC-1169** `research.zip!/research/stockfish.js` — [preserved redacted evidence](../evidence/text/2a9661e708b82108c4f17405a8a29093c99bebf5b50ace7fb0d244a22bedb8ec.js)
  Character offset 21.

```text
/*!
 * Stockfish.js (http://github.com/nmrugg/stockfish.js)
 * License: GPL
 */
var Stockfish;
function INIT_ENGINE()
{
var STOCKFISH = function (con
```

**Source references:** SRC-1141, SRC-1169  
**URL references:** <http://github.com/nmrugg/stockfish.js)>  
**Related findings:** FND-19887, FND-20179

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20636"></a>
## FND-20636: http://ogp.me/ns#

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://ogp.me/ns#",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01505"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 170.

```text
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og="http://ogp.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 270.

```text
.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 170.

```text
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og="http://ogp.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 270.

```text
.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 170.

```text
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og="http://ogp.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 270.

```text
.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <http://ogp.me/ns#>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20637"></a>
## FND-20637: http://ogp.me/ns/fb#

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://ogp.me/ns/fb#",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01506"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 138.

```text
="http://www.w3.org/1999/xhtml"
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og="http://ogp.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 292.

```text
mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8" />
    <meta name="ROBO
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 138.

```text
="http://www.w3.org/1999/xhtml"
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og="http://ogp.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 292.

```text
mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8" />
    <meta name="ROBO
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 138.

```text
="http://www.w3.org/1999/xhtml"
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og="http://ogp.me/ns#"
  data-color-mode="dark"
  class="user-logged-out dark-mode
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 292.

```text
mode="dark"
  class="user-logged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8" />
    <meta name="ROBO
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <http://ogp.me/ns/fb#>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20638"></a>
## FND-20638: http://ogp.me/ns/game#

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://ogp.me/ns/game#",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01507"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 319.

```text
ogged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8" />
    <meta name="ROBOTS" content="NOODP" />
    <m
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 319.

```text
ogged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8" />
    <meta name="ROBOTS" content="NOODP" />
    <m
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 319.

```text
ogged-out dark-mode">

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# game: http://ogp.me/ns/game#">
    
        <meta charset="utf-8" />
    <meta name="ROBOTS" content="NOODP" />
    <m
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <http://ogp.me/ns/game#>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20639"></a>
## FND-20639: http://www.w3.org/1998/Math/MathML

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://www.w3.org/1998/Math/MathML",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01508"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 81402.

```text
bel`,`name`,`pattern`,`placeholder`,`role`,`summary`,`title`,`value`,`style`,`xmlns`]),A=`http://www.w3.org/1998/Math/MathML`,j=`http://www.w3.org/2000/svg`,M=`http://www.w3.org/1999/xhtml`,N=M,Le=!1,P=null,Re=H({}
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 81402.

```text
bel`,`name`,`pattern`,`placeholder`,`role`,`summary`,`title`,`value`,`style`,`xmlns`]),A=`http://www.w3.org/1998/Math/MathML`,j=`http://www.w3.org/2000/svg`,M=`http://www.w3.org/1999/xhtml`,N=M,Le=!1,P=null,Re=H({}
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 394062.

```text
el`,`name`,`pattern`,`placeholder`,`role`,`summary`,`title`,`value`,`style`,`xmlns`]),Ie=`http://www.w3.org/1998/Math/MathML`,Le=`http://www.w3.org/2000/svg`,Re=`http://www.w3.org/1999/xhtml`,ze=Re,Be=!1,Ve=null,He
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 383217.

```text
el`,`name`,`pattern`,`placeholder`,`role`,`summary`,`title`,`value`,`style`,`xmlns`]),Pe=`http://www.w3.org/1998/Math/MathML`,Fe=`http://www.w3.org/2000/svg`,Ie=`http://www.w3.org/1999/xhtml`,Le=Ie,Re=!1,N=null,ze=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 383217.

```text
el`,`name`,`pattern`,`placeholder`,`role`,`summary`,`title`,`value`,`style`,`xmlns`]),Pe=`http://www.w3.org/1998/Math/MathML`,Fe=`http://www.w3.org/2000/svg`,Ie=`http://www.w3.org/1999/xhtml`,Le=Ie,Re=!1,N=null,ze=
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** <http://www.w3.org/1998/Math/MathML>  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20640"></a>
## FND-20640: http://www.w3.org/1999/xhtml

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://www.w3.org/1999/xhtml",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0090",
    "SRC-0751",
    "SRC-0777",
    "SRC-0781",
    "SRC-1137",
    "SRC-1150",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01509"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 50.

```text















  

<!DOCTYPE html>
<html
  xmlns="http://www.w3.org/1999/xhtml"
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 81472.

```text
style`,`xmlns`]),A=`http://www.w3.org/1998/Math/MathML`,j=`http://www.w3.org/2000/svg`,M=`http://www.w3.org/1999/xhtml`,N=M,Le=!1,P=null,Re=H({},[A,j,M],Rr),F=H({},[`mi`,`mo`,`mn`,`ms`,`mtext`]),ze=H({},[`ann
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 85499.

```text
let t=zr(e,/^[\r\n\t ]+/);r=t&&t[0]}Ve===`application/xhtml+xml`&&N===M&&(e=`<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>`+e+`</body></html>`);let i=_?_.createHTML(e):e;if(N===M)try{t=new f(
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 81472.

```text
style`,`xmlns`]),A=`http://www.w3.org/1998/Math/MathML`,j=`http://www.w3.org/2000/svg`,M=`http://www.w3.org/1999/xhtml`,N=M,Le=!1,P=null,Re=H({},[A,j,M],Rr),F=H({},[`mi`,`mo`,`mn`,`ms`,`mtext`]),ze=H({},[`ann
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 85499.

```text
let t=zr(e,/^[\r\n\t ]+/);r=t&&t[0]}Ve===`application/xhtml+xml`&&N===M&&(e=`<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>`+e+`</body></html>`);let i=_?_.createHTML(e):e;if(N===M)try{t=new f(
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 50.

```text















  

<!DOCTYPE html>
<html
  xmlns="http://www.w3.org/1999/xhtml"
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 394134.

```text
le`,`xmlns`]),Ie=`http://www.w3.org/1998/Math/MathML`,Le=`http://www.w3.org/2000/svg`,Re=`http://www.w3.org/1999/xhtml`,ze=Re,Be=!1,Ve=null,He=vh({},[Ie,Le,Re],Mh),Ue=vh({},[`mi`,`mo`,`mn`,`ms`,`mtext`]),We=v
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 398283.

```text
t t=Nh(e,/^[\r\n\t ]+/);r=t&&t[0]}Ke===`application/xhtml+xml`&&ze===Re&&(e=`<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>`+e+`</body></html>`);let i=b?b.createHTML(e):e;if(ze===Re)try{t=new 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 383289.

```text
le`,`xmlns`]),Pe=`http://www.w3.org/1998/Math/MathML`,Fe=`http://www.w3.org/2000/svg`,Ie=`http://www.w3.org/1999/xhtml`,Le=Ie,Re=!1,N=null,ze=Vh({},[Pe,Fe,Ie],tg),Be=Vh({},[`mi`,`mo`,`mn`,`ms`,`mtext`]),Ve=Vh
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 387433.

```text
t t=ng(e,/^[\r\n\t ]+/);r=t&&t[0]}Ue===`application/xhtml+xml`&&Le===Ie&&(e=`<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>`+e+`</body></html>`);let i=b?b.createHTML(e):e;if(Le===Ie)try{t=new 
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 50.

```text















  

<!DOCTYPE html>
<html
  xmlns="http://www.w3.org/1999/xhtml"
  xml:lang="en-US"
  lang="en-US"
  dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#" xmlns:og
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 383289.

```text
le`,`xmlns`]),Pe=`http://www.w3.org/1998/Math/MathML`,Fe=`http://www.w3.org/2000/svg`,Ie=`http://www.w3.org/1999/xhtml`,Le=Ie,Re=!1,N=null,ze=Vh({},[Pe,Fe,Ie],tg),Be=Vh({},[`mi`,`mo`,`mn`,`ms`,`mtext`]),Ve=Vh
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 387433.

```text
t t=ng(e,/^[\r\n\t ]+/);r=t&&t[0]}Ue===`application/xhtml+xml`&&Le===Ie&&(e=`<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>`+e+`</body></html>`);let i=b?b.createHTML(e):e;if(Le===Ie)try{t=new 
```

**Source references:** SRC-0065, SRC-0090, SRC-0751, SRC-0777, SRC-0781, SRC-1137, SRC-1150, SRC-1165  
**URL references:** <http://www.w3.org/1999/xhtml>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18117, FND-18118

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20641"></a>
## FND-20641: http://www.w3.org/2000/svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "http://www.w3.org/2000/svg",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0090",
    "SRC-0751",
    "SRC-0777",
    "SRC-0781",
    "SRC-1137",
    "SRC-1150",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01510"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 38089.

```text
ze-24 cc-button-icon "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="mark-menu" aria-hidden="true"><path d="m20.07 6h-16.13c-1.6 0-1.93-.33-1.93-
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 39092.

```text
ze-24 cc-button-icon "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="mark-cross" aria-hidden="true"><path d="m6.1 20.77c-1.13 1.13-1.6 1.13-2.73 
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 60832.

```text
20 sidebar-glyph-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="tool-magnifier-blank" aria-hidden="true"><path d="m11 18.33c4.15 0 7.33-3.19
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 61888.

```text
20 sidebar-glyph-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="tool-magnifier-blank" aria-hidden="true"><path d="m11 18.33c4.15 0 7.33-3.19
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 63225.

```text
con sidebar-auth-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="user-badge-plus" aria-hidden="true"><path d="m0 20.03c0-2 .63-2.9 2.47-3.63l
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 64651.

```text
con sidebar-auth-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrow-triangle-enter-right" aria-hidden="true"><path d="m13.33 7.67 3.87 3.8
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 65891.

```text
ebar-footer-link-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="square-fill-question" aria-hidden="true"><path d="m17.03 22h-10.07c-3.67 0-4
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 67152.

```text
ebar-footer-link-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="layout-text-languages" aria-hidden="true"><path d="m11.63 24h-.43c-1.03 0-1.
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 69735.

```text
lyph cc-icon-size-16 "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="utility-cogwheel" aria-hidden="true"><path d="m9.57 20.53-1.17 1.27c-.37.4-.
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 71011.

```text
lyph cc-icon-size-16 "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrow-triangle-flip-vertical" aria-hidden="true"><path d="m18 8.13c0-1.6-.53
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 71950.

```text
lyph cc-icon-size-16 "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="emote-face-smile-badge-plus" aria-hidden="true"><path d="m7 11.33c1.07 0 2-.
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 73077.

```text
rd-layout-icon resize"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrows-stroke-expand-diagonal-b" aria-hidden="true"><path d="m2 9.07v-5.63c0
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 81441.

```text
le`,`summary`,`title`,`value`,`style`,`xmlns`]),A=`http://www.w3.org/1998/Math/MathML`,j=`http://www.w3.org/2000/svg`,M=`http://www.w3.org/1999/xhtml`,N=M,Le=!1,P=null,Re=H({},[A,j,M],Rr),F=H({},[`mi`,`mo`,
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 124411.

```text
,Co=y((()=>{So={"data-glyph":`mark-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wo(e,t){return p(),o(`svg`,To,[...t[0]||=[s(`path`,{d:`m22.57 8.87-9.7 12.6
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 124810.

```text
o={"data-glyph":`membership-tier-diamond`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),Do=y((()=>{Co(),Eo()})),Oo,ko,Ao,jo,Mo,No=y((()=>{ve(),Oo=[`aria-hidden`,`aria-label
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 81441.

```text
le`,`summary`,`title`,`value`,`style`,`xmlns`]),A=`http://www.w3.org/1998/Math/MathML`,j=`http://www.w3.org/2000/svg`,M=`http://www.w3.org/1999/xhtml`,N=M,Le=!1,P=null,Re=H({},[A,j,M],Rr),F=H({},[`mi`,`mo`,
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 124411.

```text
,Co=y((()=>{So={"data-glyph":`mark-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wo(e,t){return p(),o(`svg`,To,[...t[0]||=[s(`path`,{d:`m22.57 8.87-9.7 12.6
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 124810.

```text
o={"data-glyph":`membership-tier-diamond`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),Do=y((()=>{Co(),Eo()})),Oo,ko,Ao,jo,Mo,No=y((()=>{ve(),Oo=[`aria-hidden`,`aria-label
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 33225.

```text
ze-24 cc-button-icon "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="mark-menu" aria-hidden="true"><path d="m20.07 6h-16.13c-1.6 0-1.93-.33-1.93-
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 34228.

```text
ze-24 cc-button-icon "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="mark-cross" aria-hidden="true"><path d="m6.1 20.77c-1.13 1.13-1.6 1.13-2.73 
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 55996.

```text
20 sidebar-glyph-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="tool-magnifier-blank" aria-hidden="true"><path d="m11 18.33c4.15 0 7.33-3.19
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 57052.

```text
20 sidebar-glyph-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="tool-magnifier-blank" aria-hidden="true"><path d="m11 18.33c4.15 0 7.33-3.19
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 58403.

```text
con sidebar-auth-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="user-badge-plus" aria-hidden="true"><path d="m0 20.03c0-2 .63-2.9 2.47-3.63l
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 59843.

```text
con sidebar-auth-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrow-triangle-enter-right" aria-hidden="true"><path d="m13.33 7.67 3.87 3.8
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 61083.

```text
ebar-footer-link-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="square-fill-question" aria-hidden="true"><path d="m17.03 22h-10.07c-3.67 0-4
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 62344.

```text
ebar-footer-link-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="layout-text-languages" aria-hidden="true"><path d="m11.63 24h-.43c-1.03 0-1.
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 71856.

```text
rd-layout-icon resize"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrows-stroke-expand-diagonal-b" aria-hidden="true"><path d="m2 9.07v-5.63c0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 132535.

```text
  `}function vn(e){if(e===void 0)return{width:0,height:0};let t=document.createElementNS(`http://www.w3.org/2000/svg`,`svg`);t.innerHTML=e,document.body.appendChild(t);let n=t.getBBox();return document.body
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 146772.

```text
,!1}var Zee=r((()=>{})),Qee,$ee=r((()=>{Qee=`
<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <image x="7.5" y="7.5" width="25" height="25" />
</svg>
`}));function ete(e){return e
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 204843.

```text
n])||[]).forEach(r=>{t(e[n][r])})})}var Uae=r((()=>{})),Wae,Gae=r((()=>{Wae=`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <path opacity="0.2" d="M29.0815 15.8433C30.0895 13.11
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 213857.

```text
)}var da=r((()=>{})),Doe,Ooe=r((()=>{Doe=`
<svg viewBox="0 0 40 40" fill="#ffa704" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="12.5" width="30" height="15" rx="3" fill="inherit" />
  <text fill="#6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 219880.

```text
 Da({className:e=``,path:t=``,size:n=`24`,viewBox:r=`0 0 18 19`}){return`
    <svg xmlns="http://www.w3.org/2000/svg" class="${e}" width="${n}" height="${n}" viewBox="${r}">
      ${t}
    </svg>
  `}var Oa
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 221888.

```text
e)}var Cse=r((()=>{})),wse,Tse=r((()=>{wse=`
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 19">
  <defs>
    <style>
      .cls-1 {
        opacity: 0.3;
      }


```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 394102.

```text
`,`summary`,`title`,`value`,`style`,`xmlns`]),Ie=`http://www.w3.org/1998/Math/MathML`,Le=`http://www.w3.org/2000/svg`,Re=`http://www.w3.org/1999/xhtml`,ze=Re,Be=!1,Ve=null,He=vh({},[Ie,Le,Re],Mh),Ue=vh({},[
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 556901.

```text
{$Ee={"data-glyph":`arrow-caret-vertical`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tDe(e,t){return O(),p(`svg`,nDe,[...t[0]||=[m(`path`,{d:`m21.13 7.07.07.07c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 557323.

```text
{nDe={"data-glyph":`arrow-chevron-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iDe(e,t){return O(),p(`svg`,aDe,[...t[0]||=[m(`path`,{d:`m17.93 2h.13c1.6 0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 557873.

```text
)=>{aDe={"data-glyph":`arrow-chevron-end`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sDe(e,t){return O(),p(`svg`,cDe,[...t[0]||=[m(`path`,{d:`m16.27 21.13-.07.0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 558294.

```text
=>{cDe={"data-glyph":`arrow-chevron-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uDe(e,t){return O(),p(`svg`,dDe,[...t[0]||=[m(`path`,{d:`m7.73 2.87.07-.07c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 558716.

```text
>{dDe={"data-glyph":`arrow-chevron-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pDe(e,t){return O(),p(`svg`,mDe,[...t[0]||=[m(`path`,{d:`m6.07 22h-.13c-1.6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 559266.

```text
>{mDe={"data-glyph":`arrow-chevron-start`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gDe(e,t){return O(),p(`svg`,_De,[...t[0]||=[m(`path`,{d:`m2.87 16.93-.07-.0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 559687.

```text
)=>{_De={"data-glyph":`arrow-chevron-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yDe(e,t){return O(),p(`svg`,bDe,[...t[0]||=[m(`path`,{d:`m10 3.93c0-1.6.33-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 560176.

```text
)=>{bDe={"data-glyph":`arrow-line-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function SDe(e,t){return O(),p(`svg`,CDe,[...t[0]||=[m(`path`,{d:`m20.07 10c1.6 0 1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 560667.

```text
(()=>{CDe={"data-glyph":`arrow-line-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function TDe(e,t){return O(),p(`svg`,EDe,[...t[0]||=[m(`path`,{d:`m3.93 14c-1.6 0-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 561159.

```text
()=>{EDe={"data-glyph":`arrow-line-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ODe(e,t){return O(),p(`svg`,kDe,[...t[0]||=[m(`path`,{d:`m14 20.07c0 1.6-.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 561653.

```text
((()=>{kDe={"data-glyph":`arrow-line-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function jDe(e,t){return O(),p(`svg`,MDe,[...t[0]||=[m(`path`,{d:`m11 22.47c-6.07 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 562275.

```text
(()=>{MDe={"data-glyph":`arrow-spin-redo`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function PDe(e,t){return O(),p(`svg`,FDe,[...t[0]||=[m(`path`,{d:`m13 22.47c-3.63 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 562894.

```text
(()=>{FDe={"data-glyph":`arrow-spin-undo`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function LDe(e,t){return O(),p(`svg`,RDe,[...t[0]||=[m(`path`,{d:`m8.9 13 9.47-9.43 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 563547.

```text
ta-glyph":`arrow-triangle-exit-right-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function BDe(e,t){return O(),p(`svg`,VDe,[...t[0]||=[m(`path`,{d:`m18 8.13c0-1.6-.53
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 564265.

```text
ata-glyph":`arrow-triangle-flip-vertical`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function UDe(e,t){return O(),p(`svg`,WDe,[...t[0]||=[m(`path`,{d:`m10.5 3.43c0-1.03.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 564894.

```text
ta-glyph":`arrow-triangle-tray-in-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function KDe(e,t){return O(),p(`svg`,qDe,[...t[0]||=[m(`path`,{d:`m13.57 10.5c1.03 0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 565534.

```text
ata-glyph":`arrow-triangle-tray-out-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function YDe(e,t){return O(),p(`svg`,XDe,[...t[0]||=[m(`path`,{d:`m16.67 14h-10.93l-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 566016.

```text
-glyph":`arrow-triangle-turn-bottom-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QDe(e,t){return O(),p(`svg`,$De,[...t[0]||=[m(`path`,{d:`m2 9.07v-5.63c0-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 566679.

```text
-glyph":`arrows-stroke-expand-diagonal-b`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tOe(e,t){return O(),p(`svg`,nOe,[...t[0]||=[m(`path`,{d:`m8.37 22.03h-5.77c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 567570.

```text
lyph":`arrows-triangle-expand-concentric`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iOe(e,t){return O(),p(`svg`,aOe,[...t[0]||=[m(`path`,{d:`m19.17 1.9 4.07 3.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 568441.

```text
e={"data-glyph":`arrows-triangle-shuffle`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sOe(e,t){return O(),p(`svg`,cOe,[...t[0]||=[m(`path`,{d:`m22 4.67v14.67c0 2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 568896.

```text
lOe=r((()=>{cOe={"data-glyph":`board-alt`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uOe(e,t){return O(),p(`svg`,dOe,[...t[0]||=[m(`path`,{d:`m6 8h-4v4h4zm0 0h4
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 569651.

```text
()=>{dOe={"data-glyph":`board-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pOe(e,t){return O(),p(`svg`,mOe,[...t[0]||=[m(`path`,{d:`m22 4.67v7.03l-7.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 570096.

```text
(()=>{mOe={"data-glyph":`board-classroom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gOe(e,t){return O(),p(`svg`,_Oe,[...t[0]||=[m(`path`,{d:`m2 20h4v-4h-4zm4-4
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 570753.

```text
r((()=>{_Oe={"data-glyph":`board-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yOe(e,t){return O(),p(`svg`,bOe,[...t[0]||=[m(`path`,{d:`m19.33 22h-14.67c-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 571201.

```text
>{bOe={"data-glyph":`board-simple-expand`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function SOe(e,t){return O(),p(`svg`,COe,[...t[0]||=[m(`path`,{d:`m2 20h5v-5h-5zm-2-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 572048.

```text
e={"data-glyph":`board-simple-stack-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function TOe(e,t){return O(),p(`svg`,EOe,[...t[0]||=[m(`path`,{d:`m19.33 16h-1.33v-7
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 572535.

```text
=>{EOe={"data-glyph":`board-simple-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function OOe(e,t){return O(),p(`svg`,kOe,[...t[0]||=[m(`path`,{d:`m2 20h2.63c.54.69 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 573163.

```text
=>{kOe={"data-glyph":`board-simple-watch`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function jOe(e,t){return O(),p(`svg`,MOe,[...t[0]||=[m(`path`,{d:`m19.33 22h-14.67c-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 573537.

```text
=r((()=>{MOe={"data-glyph":`board-simple`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function POe(e,t){return O(),p(`svg`,FOe,[...t[0]||=[m(`path`,{d:`m2 20h2.63c.54.69 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 574256.

```text
e=r((()=>{FOe={"data-glyph":`board-watch`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Gy(e,t){return O(),p(`svg`,LOe,[...t[0]||=[m(`path`,{d:`m19.33 22h-14.67c-2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 574708.

```text
LOe,ROe=r((()=>{LOe={"data-glyph":`board`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Ky(e,t){return O(),p(`svg`,zOe,[...t[0]||=[m(`path`,{d:`m4.73 17.86 13.17-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 575151.

```text
=r((()=>{zOe={"data-glyph":`circle-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VOe(e,t){return O(),p(`svg`,HOe,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 575466.

```text
)=>{HOe={"data-glyph":`circle-fill-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WOe(e,t){return O(),p(`svg`,GOe,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 575947.

```text
)=>{GOe={"data-glyph":`circle-fill-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qOe(e,t){return O(),p(`svg`,JOe,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 576555.

```text
)=>{JOe={"data-glyph":`circle-fill-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function XOe(e,t){return O(),p(`svg`,ZOe,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 576960.

```text
(()=>{ZOe={"data-glyph":`circle-fill-dot`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qy(e,t){return O(),p(`svg`,$Oe,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 577512.

```text
e={"data-glyph":`circle-fill-exclamation`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Jy(e,t){return O(),p(`svg`,tke,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 578052.

```text
()=>{tke={"data-glyph":`circle-fill-info`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rke(e,t){return O(),p(`svg`,ike,[...t[0]||=[m(`path`,{d:`m12 1.5c5.8 0 10.5
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 578705.

```text
{ike={"data-glyph":`circle-fill-question`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oke(e,t){return O(),p(`svg`,ske,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 579220.

```text
()=>{ske={"data-glyph":`circle-fill-star`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),lke=r((()=>{}));function uke(e,t){return O(),p(`svg`,dke,[...t[0]||=[m(`path`,{d:`m1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 579639.

```text
>{dke={"data-glyph":`circle-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pke(e,t){return O(),p(`svg`,mke,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.77 0-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 580262.

```text
=>{mke={"data-glyph":`circle-hollow-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gke(e,t){return O(),p(`svg`,_ke,[...t[0]||=[m(`path`,{d:`m11 22.5c-5.77 0-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 581139.

```text
ke={"data-glyph":`circle-target-practice`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yke(e,t){return O(),p(`svg`,bke,[...t[0]||=[m(`path`,{d:`m12 3c-.83 0-1.5-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 581993.

```text
()=>{bke={"data-glyph":`device-bulb-glow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Ske(e,t){return O(),p(`svg`,Cke,[...t[0]||=[m(`path`,{d:`m9.07 20h5.9l-.13-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 582546.

```text
={"data-glyph":`device-computer-analysis`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Tke(e,t){return O(),p(`svg`,Eke,[...t[0]||=[m(`path`,{d:`m1.97 16h.03v-11.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 583184.

```text
e={"data-glyph":`device-computer-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Oke(e,t){return O(),p(`svg`,kke,[...t[0]||=[m(`path`,{d:`m17.33 22h-10.67c-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 583644.

```text
=r((()=>{kke={"data-glyph":`device-phone`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function jke(e,t){return O(),p(`svg`,Mke,[...t[0]||=[m(`path`,{d:`m4.67 22c-2 0-2.67
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 584134.

```text
r((()=>{Mke={"data-glyph":`document-blog`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Pke(e,t){return O(),p(`svg`,Fke,[...t[0]||=[m(`path`,{d:`m6 23.67c-1.03.73-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 584484.

```text
={"data-glyph":`document-book-mark-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),Lke=r((()=>{}));function Rke(e,t){return O(),p(`svg`,zke,[...t[0]||=[m(`path`,{d:`m1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 585191.

```text
=>{zke={"data-glyph":`document-book-pawn`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Vke(e,t){return O(),p(`svg`,Hke,[...t[0]||=[m(`path`,{d:`m2 3.43c0-1.03.4-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 585807.

```text
Hke={"data-glyph":`document-folder-board`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Wke(e,t){return O(),p(`svg`,Gke,[...t[0]||=[m(`path`,{d:`m21 4.33c-.73 0-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 587045.

```text
(()=>{Gke={"data-glyph":`dots-square-4x4`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qke(e,t){return O(),p(`svg`,Jke,[...t[0]||=[m(`path`,{d:`m14.53 22.5c.83.6 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 587882.

```text
{"data-glyph":`element-burst-exclamation`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Yy(e,t){return O(),p(`svg`,Xke,[...t[0]||=[m(`path`,{d:`m14.53 22.5c.83.6 1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 588678.

```text
ke={"data-glyph":`element-burst-verified`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Qke(e,t){return O(),p(`svg`,$ke,[...t[0]||=[m(`path`,{d:`m16.73 22h-10.43l1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 589283.

```text
)=>{$ke={"data-glyph":`element-cloud-off`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tAe(e,t){return O(),p(`svg`,nAe,[...t[0]||=[m(`path`,{d:`m10.5 22h3v-8h2.4c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 589793.

```text
)=>{nAe={"data-glyph":`element-cloud-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iAe(e,t){return O(),p(`svg`,Xy,[...t[0]||=[m(`path`,{d:`m12.1 23c-4.67 0-8.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 590212.

```text
)=>{Xy={"data-glyph":`element-fire-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function aAe(e,t){return O(),p(`svg`,Qy,[...t[0]||=[m(`path`,{d:`m7 11.33c1.07 0 2-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 591166.

```text
data-glyph":`emote-face-smile-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oAe(e,t){return O(),p(`svg`,eb,[...t[0]||=[m(`path`,{d:`m12 18.17c2 0 3.77-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 591760.

```text
(()=>{eb={"data-glyph":`emote-face-smile`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sAe(e,t){return O(),p(`svg`,nb,[...t[0]||=[m(`path`,{d:`m18.13 15.83-6.13 6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 592168.

```text
(()=>{nb={"data-glyph":`emote-heart-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function cAe(e,t){return O(),p(`svg`,ib,[...t[0]||=[m(`path`,{d:`m18.63 16.67-6.63 6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 592759.

```text
)=>{ib={"data-glyph":`emote-heart-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lAe(e,t){return O(),p(`svg`,ob,[...t[0]||=[m(`path`,{d:`m8.8 21.63-5.47 1.5
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 593402.

```text
()=>{ob={"data-glyph":`game-banner-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uAe(e,t){return O(),p(`svg`,cb,[...t[0]||=[m(`path`,{d:`m8.8 21.63-5.47 1.5
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 594883.

```text
cb={"data-glyph":`game-banner-club-arena`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function dAe(e,t){return O(),p(`svg`,ub,[...t[0]||=[m(`path`,{d:`m8.8 21.63-5.47 1.5
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 595841.

```text
(()=>{ub={"data-glyph":`game-banner-club`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fAe(e,t){return O(),p(`svg`,fb,[...t[0]||=[m(`path`,{d:`m19 20v2h-14v-2zm-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 596416.

```text
b=r((()=>{fb={"data-glyph":`game-crown-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pAe(e,t){return O(),p(`svg`,mb,[...t[0]||=[m(`path`,{d:`m3.1 19.57c-.6-.2-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 596873.

```text
e=r((()=>{mb={"data-glyph":`game-crown-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function hAe(e,t){return O(),p(`svg`,hb,[...t[0]||=[m(`path`,{d:`m6.6 22h-.83c-.6 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 597757.

```text
b,gb=r((()=>{hb={"data-glyph":`game-draw`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gAe(e,t){return O(),p(`svg`,_b,[...t[0]||=[m(`path`,{d:`m5.8 21.8h-.13c-1.0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 598340.

```text
b,vb=r((()=>{_b={"data-glyph":`game-flag`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _Ae(e,t){return O(),p(`svg`,yb,[...t[0]||=[m(`path`,{d:`m18 19.83c-4.93 3.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 598930.

```text
((()=>{yb={"data-glyph":`game-lesson-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yAe(e,t){return O(),p(`svg`,bb,[...t[0]||=[m(`path`,{d:`m3.07 13.53-2.03-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 599532.

```text
xb=r((()=>{bb={"data-glyph":`game-lesson`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Sb(e,t){return O(),p(`svg`,Cb,[...t[0]||=[m(`path`,{d:`m2.53 21.47c-.33-.33
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 600630.

```text
wb=r((()=>{Cb={"data-glyph":`game-swords`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function bAe(e,t){return O(),p(`svg`,Tb,[...t[0]||=[m(`path`,{d:`m3 15.2c0-1.03.33-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 601128.

```text
((()=>{Tb={"data-glyph":`game-tactic-pin`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Eb(e,t){return O(),p(`svg`,Db,[...t[0]||=[m(`path`,{d:`m5.77 15c-1.03 0-1.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 601531.

```text
((()=>{Db={"data-glyph":`game-time-blitz`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kb(e,t){return O(),p(`svg`,Ab,[...t[0]||=[m(`path`,{d:`m7.17 15.3 1.43 1.47
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 602108.

```text
(()=>{Ab={"data-glyph":`game-time-bullet`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function SAe(e,t){return O(),p(`svg`,Mb,[...t[0]||=[m(`path`,{d:`m7 20h10c0-4.07-3.9
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 602723.

```text
()=>{Mb={"data-glyph":`game-time-classic`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Nb(e,t){return O(),p(`svg`,Pb,[...t[0]||=[m(`path`,{d:`m.93 11.63c3.3-1.33 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 603527.

```text
((()=>{Pb={"data-glyph":`game-time-daily`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wAe(e,t){return O(),p(`svg`,Ib,[...t[0]||=[m(`path`,{d:`m.2 23.8c3.47-4.67 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 604258.

```text
((()=>{Ib={"data-glyph":`game-time-hyper`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Lb(e,t){return O(),p(`svg`,Rb,[...t[0]||=[m(`path`,{d:`m11.97 14.63c-.9 0-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 604785.

```text
((()=>{Rb={"data-glyph":`game-time-rapid`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Bb(e,t){return O(),p(`svg`,Vb,[...t[0]||=[m(`path`,{d:`m.93 11.63c3.3-1.33 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 605800.

```text
=>{Vb={"data-glyph":`game-type-960-daily`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Ub(e,t){return O(),p(`svg`,Wb,[...t[0]||=[m(`path`,{d:`m15.5 2h-2v1.62c4.2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 606672.

```text
)=>{Wb={"data-glyph":`game-type-960-live`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Kb(e,t){return O(),p(`svg`,qb,[...t[0]||=[m(`path`,{d:`m8.37 16.93c-1.23-.9
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 607761.

```text
((()=>{qb={"data-glyph":`game-type-arena`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),EAe=r((()=>{}));function Yb(e,t){return O(),p(`svg`,Xb,[...t[0]||=[m(`path`,{d:`m3.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 609380.

```text
)=>{Xb={"data-glyph":`game-type-bughouse`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Qb(e,t){return O(),p(`svg`,$b,[...t[0]||=[m(`path`,{d:`m22 4.67v7.03l-7.37-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 609825.

```text
=>{$b={"data-glyph":`game-type-classroom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function OAe(e,t){return O(),p(`svg`,ex,[...t[0]||=[m(`path`,{d:`m10.03 20.17v-2.17h
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 610730.

```text
)=>{ex={"data-glyph":`game-type-computer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tx(e,t){return O(),p(`svg`,nx,[...t[0]||=[m(`path`,{d:`m11.73 18.67c3.07 0 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 611400.

```text
>{nx={"data-glyph":`game-type-crazyhouse`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ix(e,t){return O(),p(`svg`,ax,[...t[0]||=[m(`path`,{d:`m16.1 3.13-3.2 4.1c-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 612038.

```text
>{ax={"data-glyph":`game-type-fourplayer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ox(e,t){return O(),p(`svg`,sx,[...t[0]||=[m(`path`,{d:`m21.17 22h-18.33c-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 612558.

```text
r((()=>{sx={"data-glyph":`game-type-hill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lx(e,t){return O(),p(`svg`,ux,[...t[0]||=[m(`path`,{d:`m5.53 20.53c-1.5 0-2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 613502.

```text
{ux={"data-glyph":`game-type-three-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fx(e,t){return O(),p(`svg`,px,[...t[0]||=[m(`path`,{d:`m21.77 18.7-8.5 4.9c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 615231.

```text
)=>{px={"data-glyph":`game-type-variants`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function jAe(e,t){return O(),p(`svg`,hx,[...t[0]||=[m(`path`,{d:`m12.07 22.03h-.13c-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 616000.

```text
(()=>{hx={"data-glyph":`graph-bars-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function MAe(e,t){return O(),p(`svg`,_x,[...t[0]||=[m(`path`,{d:`m19.6 22h-.53c-2 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 616532.

```text
=>{_x={"data-glyph":`graph-bars-hollow-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NAe(e,t){return O(),p(`svg`,yx,[...t[0]||=[m(`path`,{d:`m19 8.5c-2 0-3.5-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 617040.

```text
()=>{yx={"data-glyph":`graph-nodes-share`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xx(e,t){return O(),p(`svg`,Sx,[...t[0]||=[m(`path`,{d:`m4.43 17.07c-.6-1.9-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 617612.

```text
,Cx=r((()=>{Sx={"data-glyph":`hand-loser`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function PAe(e,t){return O(),p(`svg`,wx,[...t[0]||=[m(`path`,{d:`m10.97 19.13c.83.57
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 618418.

```text
x,Tx=r((()=>{wx={"data-glyph":`hand-pawn`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function FAe(e,t){return O(),p(`svg`,Ex,[...t[0]||=[m(`path`,{d:`m16.17 19.43c-3.13 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 619061.

```text
,Dx=r((()=>{Ex={"data-glyph":`hand-shake`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IAe(e,t){return O(),p(`svg`,Ox,[...t[0]||=[m(`path`,{d:`m9.33 24c-1.57 0-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 619593.

```text
(()=>{Ox={"data-glyph":`hand-thumbs-down`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function LAe(e,t){return O(),p(`svg`,Ax,[...t[0]||=[m(`path`,{d:`m22.47 12-1.33 5.7c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 620199.

```text
r((()=>{Ax={"data-glyph":`hand-thumbs-up`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RAe(e,t){return O(),p(`svg`,Mx,[...t[0]||=[m(`path`,{d:`m22.07 14h-20.13c-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 620543.

```text
Nx=r((()=>{Mx={"data-glyph":`layout-dash`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zAe(e,t){return O(),p(`svg`,Px,[...t[0]||=[m(`path`,{d:`m19.6 11h-4.2c-1.8 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 621228.

```text
((()=>{Px={"data-glyph":`layout-grid-2x2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function BAe(e,t){return O(),p(`svg`,Ix,[...t[0]||=[m(`path`,{d:`m13.37 7.33h-2.73c-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 622561.

```text
((()=>{Ix={"data-glyph":`layout-grid-3x3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VAe(e,t){return O(),p(`svg`,Rx,[...t[0]||=[m(`path`,{d:`m19.33 22h-14.67c-2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 622908.

```text
()=>{Rx={"data-glyph":`layout-grid-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HAe(e,t){return O(),p(`svg`,Bx,[...t[0]||=[m(`path`,{d:`m20.07 6h-16.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 623508.

```text
((()=>{Bx={"data-glyph":`layout-grid-row`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function UAe(e,t){return O(),p(`svg`,Hx,[...t[0]||=[m(`path`,{d:`m4 6c-1.47 0-2.5-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 624356.

```text
)=>{Hx={"data-glyph":`layout-list-bullet`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WAe(e,t){return O(),p(`svg`,Wx,[...t[0]||=[m(`path`,{d:`m2 14.97v-1.23l1.97
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 625494.

```text
>{Wx={"data-glyph":`layout-list-numbered`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GAe(e,t){return O(),p(`svg`,Kx,[...t[0]||=[m(`path`,{d:`m3.5 10h4.5v-6.5h2v
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 626138.

```text
x={"data-glyph":`layout-table-add-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function KAe(e,t){return O(),p(`svg`,Jx,[...t[0]||=[m(`path`,{d:`m14 3.5v4.5h6.5v2h-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 626781.

```text
{Jx={"data-glyph":`layout-table-add-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qAe(e,t){return O(),p(`svg`,Xx,[...t[0]||=[m(`path`,{d:`m10 20.5v-4.5h-6.5v
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 627428.

```text
Xx={"data-glyph":`layout-table-add-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JAe(e,t){return O(),p(`svg`,Qx,[...t[0]||=[m(`path`,{d:`m20.5 14h-4.5v6.5h-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 628074.

```text
>{Qx={"data-glyph":`layout-table-add-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function YAe(e,t){return O(),p(`svg`,eS,[...t[0]||=[m(`path`,{d:`m3 11h18v2h-18zm10-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 628559.

```text
eS={"data-glyph":`layout-table-cells-2x2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function XAe(e,t){return O(),p(`svg`,nS,[...t[0]||=[m(`path`,{d:`m11 21v-18h2v18zm8.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 629028.

```text
nS={"data-glyph":`layout-table-columns-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ZAe(e,t){return O(),p(`svg`,iS,[...t[0]||=[m(`path`,{d:`m8 21v-18h2v18zm8 0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 629510.

```text
iS={"data-glyph":`layout-table-columns-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QAe(e,t){return O(),p(`svg`,oS,[...t[0]||=[m(`path`,{d:`m19 22h-14c-2.23 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 629890.

```text
=>{oS={"data-glyph":`layout-table-format`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function $Ae(e,t){return O(),p(`svg`,cS,[...t[0]||=[m(`path`,{d:`m4 19.33c0 .67 0 .6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 630822.

```text
"data-glyph":`layout-table-remove-column`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eje(e,t){return O(),p(`svg`,uS,[...t[0]||=[m(`path`,{d:`m19.33 20c.67 0 .67
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 631750.

```text
S={"data-glyph":`layout-table-remove-row`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tje(e,t){return O(),p(`svg`,fS,[...t[0]||=[m(`path`,{d:`m19.33 20c.67 0 .67
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 632487.

```text
{"data-glyph":`layout-table-remove-table`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function nje(e,t){return O(),p(`svg`,mS,[...t[0]||=[m(`path`,{d:`m21.07 22h-18.13c-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 633055.

```text
S={"data-glyph":`layout-text-A-underline`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rje(e,t){return O(),p(`svg`,gS,[...t[0]||=[m(`path`,{d:`m17.07 6h-10.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 633665.

```text
"data-glyph":`layout-text-aligned-center`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ije(e,t){return O(),p(`svg`,vS,[...t[0]||=[m(`path`,{d:`m20.07 6h-16.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 634275.

```text
={"data-glyph":`layout-text-aligned-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function aje(e,t){return O(),p(`svg`,bS,[...t[0]||=[m(`path`,{d:`m20.07 6h-16.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 634883.

```text
{"data-glyph":`layout-text-aligned-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oje(e,t){return O(),p(`svg`,SS,[...t[0]||=[m(`path`,{d:`m13.23 17c1.9 0 2.1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 635480.

```text
S={"data-glyph":`layout-text-format-bold`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sje(e,t){return O(),p(`svg`,wS,[...t[0]||=[m(`path`,{d:`m12.37 22h-4.07l3.3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 635989.

```text
{"data-glyph":`layout-text-format-italic`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function cje(e,t){return O(),p(`svg`,ES,[...t[0]||=[m(`path`,{d:`m21.07 22h-18.13c-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 636497.

```text
{"data-glyph":`layout-text-format-marker`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lje(e,t){return O(),p(`svg`,OS,[...t[0]||=[m(`path`,{d:`m12 18.33c-4.5 0-8-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 637063.

```text
ata-glyph":`layout-text-format-underline`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uje(e,t){return O(),p(`svg`,AS,[...t[0]||=[m(`path`,{d:`m22.07 6h-10.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 637770.

```text
)=>{AS={"data-glyph":`layout-text-indent`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function dje(e,t){return O(),p(`svg`,MS,[...t[0]||=[m(`path`,{d:`m22.07 6h-10.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 638481.

```text
=>{MS={"data-glyph":`layout-text-outdent`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fje(e,t){return O(),p(`svg`,PS,[...t[0]||=[m(`path`,{d:`m13.8 22v-3.77c4.07
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 638986.

```text
()=>{PS={"data-glyph":`layout-text-quote`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pje(e,t){return O(),p(`svg`,IS,[...t[0]||=[m(`path`,{d:`m11.57 22.37c-1.73 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 639765.

```text
"data-glyph":`layout-text-strike-through`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function mje(e,t){return O(),p(`svg`,RS,[...t[0]||=[m(`path`,{d:`m3.4 22h-1.87c-1.03
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 640585.

```text
{RS={"data-glyph":`layout-text-subscript`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function hje(e,t){return O(),p(`svg`,BS,[...t[0]||=[m(`path`,{d:`m3.4 22h-1.87c-1.03
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 641409.

```text
S={"data-glyph":`layout-text-superscript`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gje(e,t){return O(),p(`svg`,HS,[...t[0]||=[m(`path`,{d:`m4.93 16.37-4.47-3.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 642221.

```text
>{HS={"data-glyph":`local-door-left-exit`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _je(e,t){return O(),p(`svg`,WS,[...t[0]||=[m(`path`,{d:`m19.07 7.63 4.47 3.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 643020.

```text
{WS={"data-glyph":`local-door-right-exit`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function vje(e,t){return O(),p(`svg`,KS,[...t[0]||=[m(`path`,{d:`m9.67 11.57c.4-.97.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 643502.

```text
r((()=>{KS={"data-glyph":`local-explorer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yje(e,t){return O(),p(`svg`,JS,[...t[0]||=[m(`path`,{d:`m20.87 10h-17.73c-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 644028.

```text
=r((()=>{JS={"data-glyph":`local-library`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function bje(e,t){return O(),p(`svg`,XS,[...t[0]||=[m(`path`,{d:`m8.43 23c-1.7-.03-3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 644617.

```text
,ZS=r((()=>{XS={"data-glyph":`logo-apple`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xje(e,t){return O(),p(`svg`,QS,[...t[0]||=[m(`path`,{d:`m10.3 22.87c-5.23-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 645052.

```text
=r((()=>{QS={"data-glyph":`logo-facebook`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Sje(e,t){return O(),p(`svg`,eC,[...t[0]||=[m(`path`,{d:`m12 22c-2.7 0-3.07 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 646624.

```text
r((()=>{eC={"data-glyph":`logo-instagram`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Cje(e,t){return O(),p(`svg`,nC,[...t[0]||=[m(`path`,{d:`m7.23 22v-2.63h-4.7
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 647019.

```text
rC=r((()=>{nC={"data-glyph":`logo-twitch`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wje(e,t){return O(),p(`svg`,iC,[...t[0]||=[m(`path`,{d:`m.9 22 7.73-9.07-8.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 647356.

```text
C=r((()=>{iC={"data-glyph":`logo-twitter`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Tje(e,t){return O(),p(`svg`,oC,[...t[0]||=[m(`path`,{d:`m.9 22 7.73-9.07-8.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 647687.

```text
r oC,sC=r((()=>{oC={"data-glyph":`logo-x`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Eje(e,t){return O(),p(`svg`,cC,[...t[0]||=[m(`path`,{d:`m2.6 19.9c-1.03-.3-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 648204.

```text
C=r((()=>{cC={"data-glyph":`logo-youtube`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Dje(e,t){return O(),p(`svg`,uC,[...t[0]||=[m(`path`,{d:`m21.2 7.97-11.33 11
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 648597.

```text
,dC=r((()=>{uC={"data-glyph":`mark-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fC(e,t){return O(),p(`svg`,pC,[...t[0]||=[m(`path`,{d:`m6.1 20.77c-1.13 1.1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 649123.

```text
,mC=r((()=>{pC={"data-glyph":`mark-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Oje(e,t){return O(),p(`svg`,hC,[...t[0]||=[m(`path`,{d:`m20 14.5c-1.34 0-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 649598.

```text
={"data-glyph":`mark-ellipsis-horizontal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kje(e,t){return O(),p(`svg`,_C,[...t[0]||=[m(`path`,{d:`m1.17 5.9 3.27-3.27
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 650314.

```text
,vC=r((()=>{_C={"data-glyph":`mark-embed`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Aje(e,t){return O(),p(`svg`,yC,[...t[0]||=[m(`path`,{d:`m15.4 22h-1.13c-1.0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 651029.

```text
C,bC=r((()=>{yC={"data-glyph":`mark-hash`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function jje(e,t){return O(),p(`svg`,xC,[...t[0]||=[m(`path`,{d:`m20.07 6h-16.13c-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 651623.

```text
C,SC=r((()=>{xC={"data-glyph":`mark-menu`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Mje(e,t){return O(),p(`svg`,CC,[...t[0]||=[m(`path`,{d:`m17.07 22h-.13c-1.6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 652094.

```text
,wC=r((()=>{CC={"data-glyph":`mark-pause`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Nje(e,t){return O(),p(`svg`,TC,[...t[0]||=[m(`path`,{d:`m12.07 22h-.13c-1.6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 652575.

```text
C,EC=r((()=>{TC={"data-glyph":`mark-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Pje(e,t){return O(),p(`svg`,DC,[...t[0]||=[m(`path`,{d:`m0 12.33v-1.4c0-.6.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 653303.

```text
ata-glyph":`media-audio-microphone-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Fje(e,t){return O(),p(`svg`,kC,[...t[0]||=[m(`path`,{d:`m3 12.33v-1.4c0-.6.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 654172.

```text
data-glyph":`media-audio-microphone-mute`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Ije(e,t){return O(),p(`svg`,jC,[...t[0]||=[m(`path`,{d:`m3 12.33v-1.4c0-.6.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 654738.

```text
jC={"data-glyph":`media-audio-microphone`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NC(e,t){return O(),p(`svg`,PC,[...t[0]||=[m(`path`,{d:`m18 1.5v3.07l3.97-3.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 655345.

```text
={"data-glyph":`media-audio-speaker-mute`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IC(e,t){return O(),p(`svg`,LC,[...t[0]||=[m(`path`,{d:`m17.33 17c-.4.43-.83
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 656195.

```text
{"data-glyph":`media-audio-speaker-noise`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Lje(e,t){return O(),p(`svg`,zC,[...t[0]||=[m(`path`,{d:`m9.27 22h5.53c-.33 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 656654.

```text
((()=>{zC={"data-glyph":`media-bell-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VC(e,t){return O(),p(`svg`,HC,[...t[0]||=[m(`path`,{d:`m17.33 22h-.67c-2 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 657119.

```text
=>{HC={"data-glyph":`media-control-pause`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Rje(e,t){return O(),p(`svg`,WC,[...t[0]||=[m(`path`,{d:`m20.5 12.8-12.73 8.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 657446.

```text
)=>{WC={"data-glyph":`media-control-play`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zje(e,t){return O(),p(`svg`,KC,[...t[0]||=[m(`path`,{d:`m12 20.3c-1.22 0-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 658235.

```text
=r((()=>{KC={"data-glyph":`media-eye-off`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Bje(e,t){return O(),p(`svg`,JC,[...t[0]||=[m(`path`,{d:`m3.43 7c-1.03 0-1.4
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 658883.

```text
((()=>{JC={"data-glyph":`media-eye-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Vje(e,t){return O(),p(`svg`,XC,[...t[0]||=[m(`path`,{d:`m12 20.3c-5 0-9.13-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 659330.

```text
r((()=>{XC={"data-glyph":`media-eye-seen`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Hje(e,t){return O(),p(`svg`,QC,[...t[0]||=[m(`path`,{d:`m19.33 22h-14.67c-2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 659898.

```text
{QC={"data-glyph":`media-image-landscape`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Uje(e,t){return O(),p(`svg`,ew,[...t[0]||=[m(`path`,{d:`m15.83 7h-7.5c-1.83
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 660648.

```text
=>{ew={"data-glyph":`membership-gift-box`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function nw(e,t){return O(),p(`svg`,rw,[...t[0]||=[m(`path`,{d:`m22.57 8.87-9.7 12.6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 661047.

```text
w={"data-glyph":`membership-tier-diamond`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Wje(e,t){return O(),p(`svg`,aw,[...t[0]||=[m(`path`,{d:`m2.47 10.57c-1.9-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 661488.

```text
>{aw={"data-glyph":`membership-tier-gold`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Kje(e,t){return O(),p(`svg`,ow,[...t[0]||=[m(`path`,{d:`m12.03 22.33c-7.23-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 661896.

```text
={"data-glyph":`membership-tier-platinum`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Jje(e,t){return O(),p(`svg`,sw,[...t[0]||=[m(`path`,{d:`m4.83 21.9-3.13 1.7
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 662513.

```text
{"data-glyph":`message-bubble-fill-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Yje(e,t){return O(),p(`svg`,lw,[...t[0]||=[m(`path`,{d:`m4.83 21.9-3.13 1.7
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 663249.

```text
{"data-glyph":`message-bubble-fill-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Xje(e,t){return O(),p(`svg`,dw,[...t[0]||=[m(`path`,{d:`m22.2 23.13-2.2-1.2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 664098.

```text
={"data-glyph":`message-bubble-fill-pair`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Zje(e,t){return O(),p(`svg`,pw,[...t[0]||=[m(`path`,{d:`m22.3 23.6-3.13-1.7
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 664541.

```text
{"data-glyph":`message-bubble-fill-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Qje(e,t){return O(),p(`svg`,hw,[...t[0]||=[m(`path`,{d:`m19.33 21h-14.67c-2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 664999.

```text
{hw={"data-glyph":`message-envelope-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function $je(e,t){return O(),p(`svg`,_w,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.8 0-10.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 665510.

```text
(()=>{_w={"data-glyph":`move-circle-best`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eMe(e,t){return O(),p(`svg`,yw,[...t[0]||=[m(`path`,{d:`m12.97 15.23h-1.87c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 666142.

```text
=r((()=>{yw={"data-glyph":`move-question`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tMe(e,t){return O(),p(`svg`,xw,[...t[0]||=[m(`path`,{d:`m19.87 22h-7.87v-1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 666825.

```text
)=>{xw={"data-glyph":`piece-color-random`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),nMe=r((()=>{}));function rMe(e,t){return O(),p(`svg`,Cw,[...t[0]||=[m(`path`,{d:`m18
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 667312.

```text
((()=>{Cw={"data-glyph":`piece-fill-pawn`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iMe(e,t){return O(),p(`svg`,Tw,[...t[0]||=[m(`path`,{d:`m7.43 17.83-.93.33c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 668558.

```text
=>{Tw={"data-glyph":`piece-hollow-king-0`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function aMe(e,t){return O(),p(`svg`,Dw,[...t[0]||=[m(`path`,{d:`m5.97 20.5h12.07c0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 669323.

```text
=>{Dw={"data-glyph":`piece-hollow-pawn-1`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),oMe=r((()=>{}));function kw(e,t){return O(),p(`svg`,Aw,[...t[0]||=[m(`path`,{d:`m14.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 669826.

```text
)=>{Aw={"data-glyph":`piece-pawn-brand-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sMe(e,t){return O(),p(`svg`,Mw,[...t[0]||=[m(`path`,{d:`m15.53 22h-15.07c0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 670710.

```text
()=>{Mw={"data-glyph":`piece-pawn-signal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function cMe(e,t){return O(),p(`svg`,Pw,[...t[0]||=[m(`path`,{d:`m19.03 20c2.64 0 2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 671203.

```text
Pw={"data-glyph":`rectangle-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),lMe=r((()=>{}));function uMe(e,t){return O(),p(`svg`,Iw,[...t[0]||=[m(`path`,{d:`m17
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 671676.

```text
(()=>{Iw={"data-glyph":`square-fill-play`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function dMe(e,t){return O(),p(`svg`,Rw,[...t[0]||=[m(`path`,{d:`m17.03 22h-10.07c-3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 672298.

```text
(()=>{Rw={"data-glyph":`square-fill-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fMe(e,t){return O(),p(`svg`,Bw,[...t[0]||=[m(`path`,{d:`m19.33 16h-8.67c-2 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 672777.

```text
w={"data-glyph":`square-fill-stack-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pMe(e,t){return O(),p(`svg`,Hw,[...t[0]||=[m(`path`,{d:`m20.9 20.33h-17.5v-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 673306.

```text
)=>{Hw={"data-glyph":`square-half-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function mMe(e,t){return O(),p(`svg`,Ww,[...t[0]||=[m(`path`,{d:`m20.33 3.1v17.5h-8.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 673832.

```text
()=>{Ww={"data-glyph":`square-half-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function hMe(e,t){return O(),p(`svg`,Kw,[...t[0]||=[m(`path`,{d:`m17.03 19c1.97 0 1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 674316.

```text
=>{Kw={"data-glyph":`square-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gMe(e,t){return O(),p(`svg`,Jw,[...t[0]||=[m(`path`,{d:`m17.03 22h-10.07c-3
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 675109.

```text
)=>{Jw={"data-glyph":`square-hollow-text`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _Me(e,t){return O(),p(`svg`,Xw,[...t[0]||=[m(`path`,{d:`m6.97 22c-3.67 0-4.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 675856.

```text
w={"data-glyph":`time-calendar-fill-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function vMe(e,t){return O(),p(`svg`,Qw,[...t[0]||=[m(`path`,{d:`m6.07 8.5h-.13c-1.0
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 677693.

```text
w={"data-glyph":`time-calendar-fill-week`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yMe(e,t){return O(),p(`svg`,eT,[...t[0]||=[m(`path`,{d:`m0 12c0-5.8 4.7-10.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 678511.

```text
{eT={"data-glyph":`time-clock-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function nT(e,t){return O(),p(`svg`,rT,[...t[0]||=[m(`path`,{d:`m13 22.47c-3.83 0-6.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 679229.

```text
={"data-glyph":`time-clock-hollow-rewind`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function aT(e,t){return O(),p(`svg`,oT,[...t[0]||=[m(`path`,{d:`m15.97 15.3-3.7-2c-.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 679736.

```text
()=>{oT={"data-glyph":`time-clock-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function bMe(e,t){return O(),p(`svg`,cT,[...t[0]||=[m(`path`,{d:`m9 19.67v.33h6v-.33
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 680363.

```text
(()=>{cT={"data-glyph":`time-hourglass-1`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xMe(e,t){return O(),p(`svg`,uT,[...t[0]||=[m(`path`,{d:`m12 22.5c-5.23 0-9.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 681044.

```text
((()=>{uT={"data-glyph":`time-watch-edit`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function CMe(e,t){return O(),p(`svg`,dT,[...t[0]||=[m(`path`,{d:`m5.5 22c-3.03 0-5.5
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 681827.

```text
((()=>{dT={"data-glyph":`tool-binoculars`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wMe(e,t){return O(),p(`svg`,pT,[...t[0]||=[m(`path`,{d:`m17.33 22h-10.77c-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 682389.

```text
(()=>{pT={"data-glyph":`tool-lock-closed`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function TMe(e,t){return O(),p(`svg`,hT,[...t[0]||=[m(`path`,{d:`m11 18.33c4.15 0 7.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 682969.

```text
>{hT={"data-glyph":`tool-magnifier-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function EMe(e,t){return O(),p(`svg`,_T,[...t[0]||=[m(`path`,{d:`m11 18.33c4.15 0 7.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 683615.

```text
={"data-glyph":`tool-magnifier-checker-1`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function DMe(e,t){return O(),p(`svg`,yT,[...t[0]||=[m(`path`,{d:`m7.47 20.53-4.57 1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 684116.

```text
(()=>{yT={"data-glyph":`tool-pencil-line`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function OMe(e,t){return O(),p(`svg`,xT,[...t[0]||=[m(`path`,{d:`m7.47 20.53-4.57 1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 684503.

```text
ST=r((()=>{xT={"data-glyph":`tool-pencil`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kMe(e,t){return O(),p(`svg`,CT,[...t[0]||=[m(`path`,{d:`m.4 12 2.93-8.17c.5
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 685119.

```text
,wT=r((()=>{CT={"data-glyph":`tool-scale`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function AMe(e,t){return O(),p(`svg`,TT,[...t[0]||=[m(`path`,{d:`m8.57 20h-3.9c-2 0-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 685881.

```text
={"data-glyph":`tooltip-fill-center-text`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function MMe(e,t){return O(),p(`svg`,ET,[...t[0]||=[m(`path`,{d:`m21.67 22h-19.37c-2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 686443.

```text
>{ET={"data-glyph":`triangle-exclamation`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NMe(e,t){return O(),p(`svg`,OT,[...t[0]||=[m(`path`,{d:`m3.43 6h17.13c1.03 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 686777.

```text
data-glyph":`triangle-fill-medium-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function PMe(e,t){return O(),p(`svg`,AT,[...t[0]||=[m(`path`,{d:`m18 3.43v17.13c0 1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 687111.

```text
{"data-glyph":`triangle-fill-medium-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function FMe(e,t){return O(),p(`svg`,MT,[...t[0]||=[m(`path`,{d:`m6 20.57v-17.13c0-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 687444.

```text
"data-glyph":`triangle-fill-medium-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IMe(e,t){return O(),p(`svg`,PT,[...t[0]||=[m(`path`,{d:`m20.57 18h-17.13c-1
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 687778.

```text
={"data-glyph":`triangle-fill-medium-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function LMe(e,t){return O(),p(`svg`,IT,[...t[0]||=[m(`path`,{d:`m19 22h-14c-.33-3.2
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 688287.

```text
(()=>{IT={"data-glyph":`trophy-cup-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RT(e,t){return O(),p(`svg`,zT,[...t[0]||=[m(`path`,{d:`m17.1 2h3.47c1.03 0 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 688814.

```text
r((()=>{zT={"data-glyph":`trophy-medal-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RMe(e,t){return O(),p(`svg`,VT,[...t[0]||=[m(`path`,{d:`m0 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 689596.

```text
VT={"data-glyph":`user-badge-arrow-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zMe(e,t){return O(),p(`svg`,UT,[...t[0]||=[m(`path`,{d:`m0 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 690381.

```text
(()=>{UT={"data-glyph":`user-badge-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function BMe(e,t){return O(),p(`svg`,GT,[...t[0]||=[m(`path`,{d:`m0 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 691153.

```text
((()=>{GT={"data-glyph":`user-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VMe(e,t){return O(),p(`svg`,qT,[...t[0]||=[m(`path`,{d:`m0 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 692021.

```text
=>{qT={"data-glyph":`user-badge-question`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HMe(e,t){return O(),p(`svg`,YT,[...t[0]||=[m(`path`,{d:`m0 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 692650.

```text
,XT=r((()=>{YT={"data-glyph":`user-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function UMe(e,t){return O(),p(`svg`,ZT,[...t[0]||=[m(`path`,{d:`m0 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 693279.

```text
T=r((()=>{ZT={"data-glyph":`user-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WMe(e,t){return O(),p(`svg`,$T,[...t[0]||=[m(`path`,{d:`m2 20.43c0-1.6.5-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 694130.

```text
eE=r((()=>{$T={"data-glyph":`user-online`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GMe(e,t){return O(),p(`svg`,tE,[...t[0]||=[m(`path`,{d:`m2 20.03c0-2 .63-2.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 694571.

```text
var tE,nE=r((()=>{tE={"data-glyph":`user`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function KMe(e,t){return O(),p(`svg`,rE,[...t[0]||=[m(`path`,{d:`m8 18v-1.87c0-1.83.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 695366.

```text
ar rE,iE=r((()=>{rE={"data-glyph":`users`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qMe(e,t){return O(),p(`svg`,aE,[...t[0]||=[m(`path`,{d:`m9.57 20.53-1.17 1.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 696430.

```text
(()=>{aE={"data-glyph":`utility-cogwheel`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function YMe(e,t){return O(),p(`svg`,oE,[...t[0]||=[m(`path`,{d:`m9.73 14.77c-.53-.4
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 697205.

```text
oE={"data-glyph":`utility-link-connected`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function XMe(e,t){return O(),p(`svg`,cE,[...t[0]||=[m(`path`,{d:`m11.43 8.63 2.9-2.9
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 697835.

```text
{"data-glyph":`utility-link-disconnected`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uE(e,t){return O(),p(`svg`,dE,[...t[0]||=[m(`path`,{d:`m13.3 23.63c-.93.43-
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 698281.

```text
>{dE={"data-glyph":`utility-shield-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pE(e,t){return O(),p(`svg`,mE,[...t[0]||=[m(`path`,{d:`m6.5 22h11c2.57 0 4.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 698918.

```text
((()=>{mE={"data-glyph":`utility-toggles`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QMe(e,t){return O(),p(`svg`,hE,[...t[0]||=[m(`path`,{d:`m21.07 6h-18.13c-.6
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 699488.

```text
(()=>{hE={"data-glyph":`utility-trashbin`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),_E=r((()=>{eDe(),rDe(),oDe(),lDe(),fDe(),hDe(),vDe(),xDe(),wDe(),DDe(),ADe(),NDe(),I
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1548541.

```text
n XH(e){return document.createElement(e)}function lQe(e){return document.createElementNS(`http://www.w3.org/2000/svg`,e)}function ZH(e){return document.createTextNode(e)}function QH(){return ZH(` `)}functio
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2668821.

```text
46,7.46,0,0,1,17.07,13Z`},null,-1)]])}var Ojt,kjt,Ajt,jjt=r((()=>{He(),Ojt={},kjt={xmlns:`http://www.w3.org/2000/svg`,width:`20`,height:`20`,viewBox:`0 0 20 20`},Ajt=Ve(Ojt,[[`render`,Djt]])})),Mjt,Njt=r(((
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2928092.

```text
switch-button`])},[e.variant===`secondary`?(O(),p(`svg`,{key:0,viewBox:`0 0 90 90`,xmlns:`http://www.w3.org/2000/svg`,class:D(t.$style[`cc-switch-glyph`])},[m(`path`,{d:`m55.6 45 16.9-16.9a2 2 0 0 0 0-3L65 
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2929439.

```text
ked`,`disabled`,`id`,`name`],Lzt=[`for`],Rzt={class:`cc-switch-button`},zzt={key:0,xmlns:`http://www.w3.org/2000/svg`,class:`cc-switch-glyph`,viewBox:`0 0 90 90`},Bzt=y({__name:`cc-switch-legacy`,props:T({a
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3207677.

```text
:`#fff`,d:`M0 0h96v96H0z`})])],-1)]])}var FKt,IKt,LKt,RKt=r((()=>{He(),FKt={},IKt={xmlns:`http://www.w3.org/2000/svg`,fill:`none`,viewBox:`0 0 96 96`},LKt=Ve(FKt,[[`render`,PKt]])})),zKt,BKt,VKt=r((()=>{FK(
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3212491.

```text
,p(`svg`,{key:0,class:D([t.$style.tip,{[t.$style[`tip-obscured`]]:e.tipObscured}]),xmlns:`http://www.w3.org/2000/svg`,width:a.value.width,height:a.value.height,viewBox:a.value.viewBox,fill:`none`},[m(`path`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 150629.

```text
  `}function un(e){if(e===void 0)return{width:0,height:0};let t=document.createElementNS(`http://www.w3.org/2000/svg`,`svg`);t.innerHTML=e,document.body.appendChild(t);let n=t.getBBox();return document.body
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 164005.

```text
w),!1}var Bee=r((()=>{})),mr,Vee=r((()=>{mr=`
<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <image x="7.5" y="7.5" width="25" height="25" />
</svg>
`}));function Hee(e){let{from
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 217646.

```text
ng`,path:`vintage`},wood:{format:`png`,path:`wood`}}})),aie,oie=r((()=>{aie=`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <path opacity="0.2" d="M29.0815 15.8433C30.0895 13.11
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 226264.

```text
)}var la=r((()=>{})),Lie,Rie=r((()=>{Lie=`
<svg viewBox="0 0 40 40" fill="#ffa704" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="12.5" width="30" height="15" rx="3" fill="inherit" />
  <text fill="#6
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 231491.

```text
 Sa({className:e=``,path:t=``,size:n=`24`,viewBox:r=`0 0 18 19`}){return`
    <svg xmlns="http://www.w3.org/2000/svg" class="${e}" width="${n}" height="${n}" viewBox="${r}">
      ${t}
    </svg>
  `}var Ca
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 233499.

```text
e)}var Tae=r((()=>{})),Eae,Dae=r((()=>{Eae=`
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 19">
  <defs>
    <style>
      .cls-1 {
        opacity: 0.3;
      }


```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 383257.

```text
`,`summary`,`title`,`value`,`style`,`xmlns`]),Pe=`http://www.w3.org/1998/Math/MathML`,Fe=`http://www.w3.org/2000/svg`,Ie=`http://www.w3.org/1999/xhtml`,Le=Ie,Re=!1,N=null,ze=Vh({},[Pe,Fe,Ie],tg),Be=Vh({},[`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1713157.

```text
{IJe={"data-glyph":`arrow-caret-vertical`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RJe(e,t){return k(),f(`svg`,zJe,[...t[0]||=[p(`path`,{d:`m21.13 7.07.07.07c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1713579.

```text
{zJe={"data-glyph":`arrow-chevron-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VJe(e,t){return k(),f(`svg`,HJe,[...t[0]||=[p(`path`,{d:`m17.93 2h.13c1.6 0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1714129.

```text
)=>{HJe={"data-glyph":`arrow-chevron-end`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WJe(e,t){return k(),f(`svg`,GJe,[...t[0]||=[p(`path`,{d:`m16.27 21.13-.07.0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1714550.

```text
=>{GJe={"data-glyph":`arrow-chevron-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QU(e,t){return k(),f(`svg`,qJe,[...t[0]||=[p(`path`,{d:`m7.73 2.87.07-.07c1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1714971.

```text
>{qJe={"data-glyph":`arrow-chevron-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function YJe(e,t){return k(),f(`svg`,XJe,[...t[0]||=[p(`path`,{d:`m6.07 22h-.13c-1.6
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1715521.

```text
>{XJe={"data-glyph":`arrow-chevron-start`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QJe(e,t){return k(),f(`svg`,$Je,[...t[0]||=[p(`path`,{d:`m2.87 16.93-.07-.0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1715942.

```text
)=>{$Je={"data-glyph":`arrow-chevron-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tYe(e,t){return k(),f(`svg`,nYe,[...t[0]||=[p(`path`,{d:`m10 3.93c0-1.6.33-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1716431.

```text
)=>{nYe={"data-glyph":`arrow-line-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iYe(e,t){return k(),f(`svg`,aYe,[...t[0]||=[p(`path`,{d:`m20.07 10c1.6 0 1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1716922.

```text
(()=>{aYe={"data-glyph":`arrow-line-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function $U(e,t){return k(),f(`svg`,sYe,[...t[0]||=[p(`path`,{d:`m3.93 14c-1.6 0-1.9
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1717413.

```text
()=>{sYe={"data-glyph":`arrow-line-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lYe(e,t){return k(),f(`svg`,uYe,[...t[0]||=[p(`path`,{d:`m14 20.07c0 1.6-.3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1717907.

```text
((()=>{uYe={"data-glyph":`arrow-line-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fYe(e,t){return k(),f(`svg`,pYe,[...t[0]||=[p(`path`,{d:`m3 12c0-5.77 4.73-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1718470.

```text
(()=>{pYe={"data-glyph":`arrow-spin-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function hYe(e,t){return k(),f(`svg`,gYe,[...t[0]||=[p(`path`,{d:`m13 22.47c-3.63 0-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1719089.

```text
(()=>{gYe={"data-glyph":`arrow-spin-undo`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function vYe(e,t){return k(),f(`svg`,yYe,[...t[0]||=[p(`path`,{d:`m10 3.93c0-1.6.33-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1719630.

```text
"data-glyph":`arrow-triangle-edge-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xYe(e,t){return k(),f(`svg`,SYe,[...t[0]||=[p(`path`,{d:`m8.9 13 9.47-9.43 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1720283.

```text
ta-glyph":`arrow-triangle-exit-right-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wYe(e,t){return k(),f(`svg`,TYe,[...t[0]||=[p(`path`,{d:`m18 8.13c0-1.6-.53
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1721001.

```text
ata-glyph":`arrow-triangle-flip-vertical`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function DYe(e,t){return k(),f(`svg`,OYe,[...t[0]||=[p(`path`,{d:`m3.57 9.53h13.27v5
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1721423.

```text
"data-glyph":`arrow-triangle-point-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function AYe(e,t){return k(),f(`svg`,jYe,[...t[0]||=[p(`path`,{d:`m10.5 3.43c0-1.03.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1722052.

```text
ta-glyph":`arrow-triangle-tray-in-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NYe(e,t){return k(),f(`svg`,PYe,[...t[0]||=[p(`path`,{d:`m15.57 14.93-.02-.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1722967.

```text
((()=>{PYe={"data-glyph":`board-analysis`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IYe(e,t){return k(),f(`svg`,LYe,[...t[0]||=[p(`path`,{d:`m15.33 22h-10.67c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1723526.

```text
={"data-glyph":`board-arrow-diagonal-out`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zYe(e,t){return k(),f(`svg`,BYe,[...t[0]||=[p(`path`,{d:`m6 8h-4v4h4zm0 0h4
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1724281.

```text
()=>{BYe={"data-glyph":`board-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HYe(e,t){return k(),f(`svg`,UYe,[...t[0]||=[p(`path`,{d:`m6 8h-4v4h4zm0 0h4
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1725019.

```text
>{UYe={"data-glyph":`board-badge-warning`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GYe(e,t){return k(),f(`svg`,KYe,[...t[0]||=[p(`path`,{d:`m2 20h4v-4h-4zm4-4
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1725676.

```text
r((()=>{KYe={"data-glyph":`board-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JYe(e,t){return k(),f(`svg`,YYe,[...t[0]||=[p(`path`,{d:`m19.33 22h-14.67c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1726124.

```text
>{YYe={"data-glyph":`board-simple-expand`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ZYe(e,t){return k(),f(`svg`,QYe,[...t[0]||=[p(`path`,{d:`m2 20h7.06c.43.75.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1726733.

```text
{QYe={"data-glyph":`board-simple-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eXe(e,t){return k(),f(`svg`,tXe,[...t[0]||=[p(`path`,{d:`m2 20h5v-5h-5zm-2-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1727580.

```text
e={"data-glyph":`board-simple-stack-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rXe(e,t){return k(),f(`svg`,iXe,[...t[0]||=[p(`path`,{d:`m19.33 16h-1.33v-7
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1728067.

```text
=>{iXe={"data-glyph":`board-simple-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oXe(e,t){return k(),f(`svg`,sXe,[...t[0]||=[p(`path`,{d:`m2 20h2.63c.54.69 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1728695.

```text
=>{sXe={"data-glyph":`board-simple-watch`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eW(e,t){return k(),f(`svg`,lXe,[...t[0]||=[p(`path`,{d:`m19.33 22h-14.67c-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1729147.

```text
lXe,uXe=r((()=>{lXe={"data-glyph":`board`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function dXe(e,t){return k(),f(`svg`,fXe,[...t[0]||=[p(`path`,{d:`m4.73 17.86 13.17-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1729591.

```text
=r((()=>{fXe={"data-glyph":`circle-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function mXe(e,t){return k(),f(`svg`,hXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1730072.

```text
)=>{hXe={"data-glyph":`circle-fill-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _Xe(e,t){return k(),f(`svg`,vXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1730680.

```text
)=>{vXe={"data-glyph":`circle-fill-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function bXe(e,t){return k(),f(`svg`,xXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1731233.

```text
e={"data-glyph":`circle-fill-exclamation`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function CXe(e,t){return k(),f(`svg`,wXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1731774.

```text
()=>{wXe={"data-glyph":`circle-fill-info`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function EXe(e,t){return k(),f(`svg`,DXe,[...t[0]||=[p(`path`,{d:`m12 1.5c5.8 0 10.5
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1732427.

```text
{DXe={"data-glyph":`circle-fill-question`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kXe(e,t){return k(),f(`svg`,AXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1732942.

```text
()=>{AXe={"data-glyph":`circle-fill-star`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),MXe=r((()=>{}));function NXe(e,t){return k(),f(`svg`,PXe,[...t[0]||=[p(`path`,{d:`m1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1733361.

```text
>{PXe={"data-glyph":`circle-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IXe(e,t){return k(),f(`svg`,LXe,[...t[0]||=[p(`path`,{d:`m11 22.5c-5.77 0-1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1734238.

```text
Xe={"data-glyph":`circle-target-practice`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zXe(e,t){return k(),f(`svg`,BXe,[...t[0]||=[p(`path`,{d:`m14.57 20h-5.13c-1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1734705.

```text
()=>{BXe={"data-glyph":`device-bulb-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HXe(e,t){return k(),f(`svg`,UXe,[...t[0]||=[p(`path`,{d:`m12 3c-.83 0-1.5-.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1735559.

```text
()=>{UXe={"data-glyph":`device-bulb-glow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GXe(e,t){return k(),f(`svg`,KXe,[...t[0]||=[p(`path`,{d:`m8 22c-.67 0-1-.33
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1736483.

```text
=>{KXe={"data-glyph":`device-chip-exclam`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JXe(e,t){return k(),f(`svg`,YXe,[...t[0]||=[p(`path`,{d:`m9.07 20h5.9l-.13-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1737036.

```text
={"data-glyph":`device-computer-analysis`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ZXe(e,t){return k(),f(`svg`,QXe,[...t[0]||=[p(`path`,{d:`m1.97 16h.03v-11.3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1737580.

```text
{QXe={"data-glyph":`device-computer-chip`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eZe(e,t){return k(),f(`svg`,tZe,[...t[0]||=[p(`path`,{d:`m17.33 22h-10.67c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1738040.

```text
=r((()=>{tZe={"data-glyph":`device-phone`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rZe(e,t){return k(),f(`svg`,iZe,[...t[0]||=[p(`path`,{d:`m4.67 22c-2 0-2.67
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1738530.

```text
r((()=>{iZe={"data-glyph":`document-blog`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oZe(e,t){return k(),f(`svg`,sZe,[...t[0]||=[p(`path`,{d:`m6 23.67c-1.03.73-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1738880.

```text
={"data-glyph":`document-book-mark-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lZe(e,t){return k(),f(`svg`,uZe,[...t[0]||=[p(`path`,{d:`m5.34 21.81 6.66-4
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1739383.

```text
{"data-glyph":`document-book-mark-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tW(e,t){return k(),f(`svg`,fZe,[...t[0]||=[p(`path`,{d:`m18.57 22h-13.9c-2 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1739836.

```text
=>{fZe={"data-glyph":`document-book-mark`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),mZe=r((()=>{}));function hZe(e,t){return k(),f(`svg`,gZe,[...t[0]||=[p(`path`,{d:`m1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1740860.

```text
>{gZe={"data-glyph":`document-book-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function vZe(e,t){return k(),f(`svg`,yZe,[...t[0]||=[p(`path`,{d:`m2 3.43c0-1.03.4-1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1741476.

```text
yZe={"data-glyph":`document-folder-board`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xZe(e,t){return k(),f(`svg`,SZe,[...t[0]||=[p(`path`,{d:`m16 6.23c-1.27 0-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1742321.

```text
data-glyph":`dots-grid-2x3-round-columns`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wZe(e,t){return k(),f(`svg`,TZe,[...t[0]||=[p(`path`,{d:`m10.5 22h3v-8h2.4c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1742831.

```text
)=>{TZe={"data-glyph":`element-cloud-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function DZe(e,t){return k(),f(`svg`,OZe,[...t[0]||=[p(`path`,{d:`m7.3 21.03c-2.03 1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1743274.

```text
)=>{OZe={"data-glyph":`element-star-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function AZe(e,t){return k(),f(`svg`,jZe,[...t[0]||=[p(`path`,{d:`m12 18.17c2 0 3.77
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1743872.

```text
()=>{jZe={"data-glyph":`emote-face-smile`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NZe(e,t){return k(),f(`svg`,PZe,[...t[0]||=[p(`path`,{d:`m18.13 15.83-6.13 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1744284.

```text
()=>{PZe={"data-glyph":`emote-heart-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IZe(e,t){return k(),f(`svg`,LZe,[...t[0]||=[p(`path`,{d:`m18.63 16.67-6.63 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1744879.

```text
=>{LZe={"data-glyph":`emote-heart-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zZe(e,t){return k(),f(`svg`,BZe,[...t[0]||=[p(`path`,{d:`m19 20v2h-14v-2zm-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1745458.

```text
=r((()=>{BZe={"data-glyph":`game-crown-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HZe(e,t){return k(),f(`svg`,UZe,[...t[0]||=[p(`path`,{d:`m5.8 21.8h-.13c-1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1746045.

```text
WZe=r((()=>{UZe={"data-glyph":`game-flag`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GZe(e,t){return k(),f(`svg`,KZe,[...t[0]||=[p(`path`,{d:`m18 19.83c-4.93 3.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1746638.

```text
(()=>{KZe={"data-glyph":`game-lesson-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JZe(e,t){return k(),f(`svg`,YZe,[...t[0]||=[p(`path`,{d:`m3.07 13.53-2.03-1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1747244.

```text
e=r((()=>{YZe={"data-glyph":`game-lesson`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),ZZe=r((()=>{}));function QZe(e,t){return k(),f(`svg`,$Ze,[...t[0]||=[p(`path`,{d:`m5
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1747668.

```text
(()=>{$Ze={"data-glyph":`game-time-blitz`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tQe(e,t){return k(),f(`svg`,nQe,[...t[0]||=[p(`path`,{d:`m7.17 15.3 1.43 1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1748250.

```text
()=>{nQe={"data-glyph":`game-time-bullet`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iQe(e,t){return k(),f(`svg`,aQe,[...t[0]||=[p(`path`,{d:`m7 20h10c0-4.07-3.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1748868.

```text
)=>{aQe={"data-glyph":`game-time-classic`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sQe(e,t){return k(),f(`svg`,cQe,[...t[0]||=[p(`path`,{d:`m.93 11.63c3.3-1.3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1749677.

```text
(()=>{cQe={"data-glyph":`game-time-daily`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uQe(e,t){return k(),f(`svg`,dQe,[...t[0]||=[p(`path`,{d:`m.2 23.8c3.47-4.67
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1750411.

```text
(()=>{dQe={"data-glyph":`game-time-hyper`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pQe(e,t){return k(),f(`svg`,mQe,[...t[0]||=[p(`path`,{d:`m11.97 14.63c-.9 0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1750943.

```text
(()=>{mQe={"data-glyph":`game-time-rapid`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gQe(e,t){return k(),f(`svg`,_Qe,[...t[0]||=[p(`path`,{d:`m.93 11.63c3.3-1.3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1751963.

```text
>{_Qe={"data-glyph":`game-type-960-daily`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yQe(e,t){return k(),f(`svg`,bQe,[...t[0]||=[p(`path`,{d:`m15.5 2h-2v1.62c4.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1752840.

```text
=>{bQe={"data-glyph":`game-type-960-live`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),SQe=r((()=>{}));function CQe(e,t){return k(),f(`svg`,wQe,[...t[0]||=[p(`path`,{d:`m3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1754464.

```text
=>{wQe={"data-glyph":`game-type-bughouse`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function EQe(e,t){return k(),f(`svg`,DQe,[...t[0]||=[p(`path`,{d:`m22 4.67v7.03l-7.3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1754913.

```text
>{DQe={"data-glyph":`game-type-classroom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kQe(e,t){return k(),f(`svg`,AQe,[...t[0]||=[p(`path`,{d:`m10.03 20.17v-2.17
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1755821.

```text
=>{AQe={"data-glyph":`game-type-computer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function MQe(e,t){return k(),f(`svg`,NQe,[...t[0]||=[p(`path`,{d:`m11.73 18.67c3.07 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1756496.

```text
{NQe={"data-glyph":`game-type-crazyhouse`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function FQe(e,t){return k(),f(`svg`,IQe,[...t[0]||=[p(`path`,{d:`m16.1 3.13-3.2 4.1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1757138.

```text
{IQe={"data-glyph":`game-type-fourplayer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RQe(e,t){return k(),f(`svg`,zQe,[...t[0]||=[p(`path`,{d:`m21.17 22h-18.33c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1757663.

```text
((()=>{zQe={"data-glyph":`game-type-hill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VQe(e,t){return k(),f(`svg`,HQe,[...t[0]||=[p(`path`,{d:`m5.53 20.53c-1.5 0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1758612.

```text
HQe={"data-glyph":`game-type-three-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WQe(e,t){return k(),f(`svg`,GQe,[...t[0]||=[p(`path`,{d:`m21.77 18.7-8.5 4.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1760346.

```text
=>{GQe={"data-glyph":`game-type-variants`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qQe(e,t){return k(),f(`svg`,JQe,[...t[0]||=[p(`path`,{d:`m19.6 22h-.53c-2 0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1760882.

```text
>{JQe={"data-glyph":`graph-bars-hollow-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function XQe(e,t){return k(),f(`svg`,ZQe,[...t[0]||=[p(`path`,{d:`m20.57 22h-1.33c-.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1761482.

```text
ZQe={"data-glyph":`graph-bars-statistics`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function $Qe(e,t){return k(),f(`svg`,e$e,[...t[0]||=[p(`path`,{d:`m19 8.5c-2 0-3.5-1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1761994.

```text
)=>{e$e={"data-glyph":`graph-nodes-share`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function n$e(e,t){return k(),f(`svg`,r$e,[...t[0]||=[p(`path`,{d:`m4.43 17.07c-.6-1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1762571.

```text
$e=r((()=>{r$e={"data-glyph":`hand-loser`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function a$e(e,t){return k(),f(`svg`,o$e,[...t[0]||=[p(`path`,{d:`m10.97 19.13c.83.5
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1763381.

```text
s$e=r((()=>{o$e={"data-glyph":`hand-pawn`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),c$e=r((()=>{}));function l$e(e,t){return k(),f(`svg`,u$e,[...t[0]||=[p(`path`,{d:`m4
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1764334.

```text
)=>{u$e={"data-glyph":`layout-list-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function f$e(e,t){return k(),f(`svg`,p$e,[...t[0]||=[p(`path`,{d:`m19.33 22h-14.67c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1764785.

```text
ata-glyph":`layout-table-cell-properties`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function h$e(e,t){return k(),f(`svg`,g$e,[...t[0]||=[p(`path`,{d:`m11 21v-18h2v18zm8
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1765258.

```text
$e={"data-glyph":`layout-table-columns-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function v$e(e,t){return k(),f(`svg`,y$e,[...t[0]||=[p(`path`,{d:`m4.93 16.37-4.47-3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1766074.

```text
{y$e={"data-glyph":`local-door-left-exit`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function x$e(e,t){return k(),f(`svg`,S$e,[...t[0]||=[p(`path`,{d:`m9.67 11.57c.4-.97
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1766560.

```text
((()=>{S$e={"data-glyph":`local-explorer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function w$e(e,t){return k(),f(`svg`,T$e,[...t[0]||=[p(`path`,{d:`m20.87 10h-17.73c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1767090.

```text
r((()=>{T$e={"data-glyph":`local-library`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function D$e(e,t){return k(),f(`svg`,O$e,[...t[0]||=[p(`path`,{d:`m8.43 23c-1.7-.03-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1767683.

```text
$e=r((()=>{O$e={"data-glyph":`logo-apple`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function nW(e,t){return k(),f(`svg`,A$e,[...t[0]||=[p(`path`,{d:`m21.2 7.97-11.33 11
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1768079.

```text
$e=r((()=>{A$e={"data-glyph":`mark-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rW(e,t){return k(),f(`svg`,M$e,[...t[0]||=[p(`path`,{d:`m6.1 20.77c-1.13 1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1768609.

```text
$e=r((()=>{M$e={"data-glyph":`mark-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function P$e(e,t){return k(),f(`svg`,F$e,[...t[0]||=[p(`path`,{d:`m20 14.5c-1.34 0-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1769088.

```text
={"data-glyph":`mark-ellipsis-horizontal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function L$e(e,t){return k(),f(`svg`,R$e,[...t[0]||=[p(`path`,{d:`m20.07 14h-16.13c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1769435.

```text
$e=r((()=>{R$e={"data-glyph":`mark-minus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function B$e(e,t){return k(),f(`svg`,V$e,[...t[0]||=[p(`path`,{d:`m12.07 22h-.13c-1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1769920.

```text
H$e=r((()=>{V$e={"data-glyph":`mark-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function U$e(e,t){return k(),f(`svg`,W$e,[...t[0]||=[p(`path`,{d:`m18 1.5v3.07l3.97-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1770532.

```text
={"data-glyph":`media-audio-speaker-mute`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function K$e(e,t){return k(),f(`svg`,q$e,[...t[0]||=[p(`path`,{d:`m17.33 17c-.4.43-.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1771387.

```text
{"data-glyph":`media-audio-speaker-noise`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Y$e(e,t){return k(),f(`svg`,X$e,[...t[0]||=[p(`path`,{d:`m20.33 22h-16.67c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1771927.

```text
=>{X$e={"data-glyph":`media-camera-photo`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Q$e(e,t){return k(),f(`svg`,$$e,[...t[0]||=[p(`path`,{d:`m17.33 22h-.67c-2 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1772397.

```text
>{$$e={"data-glyph":`media-control-pause`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function t1e(e,t){return k(),f(`svg`,n1e,[...t[0]||=[p(`path`,{d:`m20.5 12.8-12.73 8
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1772728.

```text
=>{n1e={"data-glyph":`media-control-play`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function i1e(e,t){return k(),f(`svg`,a1e,[...t[0]||=[p(`path`,{d:`m12 20.3c-1.22 0-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1773521.

```text
r((()=>{a1e={"data-glyph":`media-eye-off`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function s1e(e,t){return k(),f(`svg`,c1e,[...t[0]||=[p(`path`,{d:`m12 20.3c-5 0-9.13
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1773972.

```text
((()=>{c1e={"data-glyph":`media-eye-seen`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iW(e,t){return k(),f(`svg`,u1e,[...t[0]||=[p(`path`,{d:`m17.43 7.5-.38.5c-.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1774728.

```text
yph":`membership-tier-diamond-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function f1e(e,t){return k(),f(`svg`,p1e,[...t[0]||=[p(`path`,{d:`m22.57 8.87-9.7 12
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1775132.

```text
e={"data-glyph":`membership-tier-diamond`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function h1e(e,t){return k(),f(`svg`,g1e,[...t[0]||=[p(`path`,{d:`m2.47 10.57c-1.9-1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1775576.

```text
{g1e={"data-glyph":`membership-tier-gold`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function v1e(e,t){return k(),f(`svg`,y1e,[...t[0]||=[p(`path`,{d:`m12.03 22.33c-7.23
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1775987.

```text
={"data-glyph":`membership-tier-platinum`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function x1e(e,t){return k(),f(`svg`,S1e,[...t[0]||=[p(`path`,{d:`m4.83 21.9-3.13 1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1776608.

```text
{"data-glyph":`message-bubble-fill-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function w1e(e,t){return k(),f(`svg`,T1e,[...t[0]||=[p(`path`,{d:`m4.83 21.9-3.13 1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1777348.

```text
{"data-glyph":`message-bubble-fill-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function D1e(e,t){return k(),f(`svg`,O1e,[...t[0]||=[p(`path`,{d:`m22.2 23.13-2.2-1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1778201.

```text
={"data-glyph":`message-bubble-fill-pair`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function A1e(e,t){return k(),f(`svg`,j1e,[...t[0]||=[p(`path`,{d:`m19.33 21h-14.67c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1778663.

```text
j1e={"data-glyph":`message-envelope-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function N1e(e,t){return k(),f(`svg`,P1e,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1779178.

```text
()=>{P1e={"data-glyph":`move-circle-best`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),I1e=r((()=>{}));function L1e(e,t){return k(),f(`svg`,R1e,[...t[0]||=[p(`path`,{d:`m2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1780333.

```text
)=>{R1e={"data-glyph":`piece-knight-fork`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function B1e(e,t){return k(),f(`svg`,V1e,[...t[0]||=[p(`path`,{d:`m14.3 10.5c.23 7.2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1780825.

```text
=>{V1e={"data-glyph":`piece-pawn-brand-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function U1e(e,t){return k(),f(`svg`,W1e,[...t[0]||=[p(`path`,{d:`m15.53 22h-15.07c0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1781713.

```text
)=>{W1e={"data-glyph":`piece-pawn-signal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function K1e(e,t){return k(),f(`svg`,q1e,[...t[0]||=[p(`path`,{d:`m16.63 18.73h-9.3c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1782458.

```text
)=>{q1e={"data-glyph":`piece-simple-king`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Y1e(e,t){return k(),f(`svg`,X1e,[...t[0]||=[p(`path`,{d:`m16.93 22c-.01-1.2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1783561.

```text
1e=r((()=>{X1e={"data-glyph":`pieces-all`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Q1e(e,t){return k(),f(`svg`,$1e,[...t[0]||=[p(`path`,{d:`m11.33 22h-8.67c-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1784045.

```text
{$1e={"data-glyph":`rectangle-fill-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),t0e=r((()=>{}));function n0e(e,t){return k(),f(`svg`,r0e,[...t[0]||=[p(`path`,{d:`m1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1784592.

```text
>{r0e={"data-glyph":`square-fill-checked`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function a0e(e,t){return k(),f(`svg`,o0e,[...t[0]||=[p(`path`,{d:`m17.03 22h-10.07c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1785204.

```text
)=>{o0e={"data-glyph":`square-fill-equal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function c0e(e,t){return k(),f(`svg`,l0e,[...t[0]||=[p(`path`,{d:`m17.03 22h-10.07c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1785699.

```text
)=>{l0e={"data-glyph":`square-fill-minus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function d0e(e,t){return k(),f(`svg`,f0e,[...t[0]||=[p(`path`,{d:`m17.03 22h-10.07c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1786325.

```text
()=>{f0e={"data-glyph":`square-fill-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function m0e(e,t){return k(),f(`svg`,h0e,[...t[0]||=[p(`path`,{d:`m19.33 16h-8.67c-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1786808.

```text
e={"data-glyph":`square-fill-stack-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _0e(e,t){return k(),f(`svg`,aW,[...t[0]||=[p(`path`,{d:`m17.03 19c1.97 0 1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1787293.

```text
=>{aW={"data-glyph":`square-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function y0e(e,t){return k(),f(`svg`,b0e,[...t[0]||=[p(`path`,{d:`m6.07 8.5h-.13c-1.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1789134.

```text
e={"data-glyph":`time-calendar-fill-week`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function S0e(e,t){return k(),f(`svg`,C0e,[...t[0]||=[p(`path`,{d:`m13 22.47c-3.83 0-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1789857.

```text
={"data-glyph":`time-clock-hollow-rewind`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function T0e(e,t){return k(),f(`svg`,E0e,[...t[0]||=[p(`path`,{d:`m15.97 15.3-3.7-2c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1790369.

```text
)=>{E0e={"data-glyph":`time-clock-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function O0e(e,t){return k(),f(`svg`,k0e,[...t[0]||=[p(`path`,{d:`m7.03 20h9.97c0-2.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1790976.

```text
()=>{k0e={"data-glyph":`time-hourglass-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function j0e(e,t){return k(),f(`svg`,M0e,[...t[0]||=[p(`path`,{d:`m5.5 22c-3.03 0-5.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1791763.

```text
(()=>{M0e={"data-glyph":`tool-binoculars`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function P0e(e,t){return k(),f(`svg`,F0e,[...t[0]||=[p(`path`,{d:`m13.8 22.3c-1.77 1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1792441.

```text
r((()=>{F0e={"data-glyph":`tool-dumbbell`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function L0e(e,t){return k(),f(`svg`,R0e,[...t[0]||=[p(`path`,{d:`m8.5 11.87-6.03-8.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1792808.

```text
e=r((()=>{R0e={"data-glyph":`tool-filter`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function B0e(e,t){return k(),f(`svg`,V0e,[...t[0]||=[p(`path`,{d:`m17.33 22h-10.77c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1793261.

```text
(()=>{V0e={"data-glyph":`tool-lock-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function U0e(e,t){return k(),f(`svg`,W0e,[...t[0]||=[p(`path`,{d:`m17.33 22h-10.77c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1793827.

```text
()=>{W0e={"data-glyph":`tool-lock-closed`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function K0e(e,t){return k(),f(`svg`,q0e,[...t[0]||=[p(`path`,{d:`m17.03 8.67c.9 0 1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1794353.

```text
r((()=>{q0e={"data-glyph":`tool-lock-key`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Y0e(e,t){return k(),f(`svg`,X0e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1794937.

```text
{X0e={"data-glyph":`tool-magnifier-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Q0e(e,t){return k(),f(`svg`,$0e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1795587.

```text
={"data-glyph":`tool-magnifier-checker-1`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function t2e(e,t){return k(),f(`svg`,n2e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1796239.

```text
={"data-glyph":`tool-magnifier-checker-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function i2e(e,t){return k(),f(`svg`,a2e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1797010.

```text
>{a2e={"data-glyph":`tool-magnifier-star`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function s2e(e,t){return k(),f(`svg`,c2e,[...t[0]||=[p(`path`,{d:`m7.47 20.53-4.57 1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1797515.

```text
()=>{c2e={"data-glyph":`tool-pencil-line`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function u2e(e,t){return k(),f(`svg`,d2e,[...t[0]||=[p(`path`,{d:`m3.43 6h17.13c1.03
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1797853.

```text
data-glyph":`triangle-fill-medium-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function p2e(e,t){return k(),f(`svg`,m2e,[...t[0]||=[p(`path`,{d:`m20.57 18h-17.13c-
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1798191.

```text
={"data-glyph":`triangle-fill-medium-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function g2e(e,t){return k(),f(`svg`,_2e,[...t[0]||=[p(`path`,{d:`m4.93 8h14.13c1.03
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1798518.

```text
"data-glyph":`triangle-fill-small-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),y2e=r((()=>{}));function b2e(e,t){return k(),f(`svg`,x2e,[...t[0]||=[p(`path`,{d:`m0
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1799320.

```text
2e={"data-glyph":`user-badge-arrow-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function C2e(e,t){return k(),f(`svg`,w2e,[...t[0]||=[p(`path`,{d:`m0 20.03c0-2 .63-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1800096.

```text
(()=>{w2e={"data-glyph":`user-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function E2e(e,t){return k(),f(`svg`,D2e,[...t[0]||=[p(`path`,{d:`m0 20.03c0-2 .63-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1800729.

```text
2e=r((()=>{D2e={"data-glyph":`user-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function k2e(e,t){return k(),f(`svg`,A2e,[...t[0]||=[p(`path`,{d:`m2 20.03c0-2 .63-2
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1801174.

```text
 A2e,j2e=r((()=>{A2e={"data-glyph":`user`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function M2e(e,t){return k(),f(`svg`,N2e,[...t[0]||=[p(`path`,{d:`m8 18v-1.87c0-1.83
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1801973.

```text
N2e,P2e=r((()=>{N2e={"data-glyph":`users`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function F2e(e,t){return k(),f(`svg`,I2e,[...t[0]||=[p(`path`,{d:`m9.57 20.53-1.17 1
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1803040.

```text
()=>{I2e={"data-glyph":`utility-cogwheel`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function R2e(e,t){return k(),f(`svg`,z2e,[...t[0]||=[p(`path`,{d:`m13.3 23.63c-.93.4
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1803491.

```text
{z2e={"data-glyph":`utility-shield-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function V2e(e,t){return k(),f(`svg`,H2e,[...t[0]||=[p(`path`,{d:`m6.5 22h11c2.57 0 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1804132.

```text
(()=>{H2e={"data-glyph":`utility-toggles`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function W2e(e,t){return k(),f(`svg`,G2e,[...t[0]||=[p(`path`,{d:`m21.07 6h-18.13c-.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1804706.

```text
()=>{G2e={"data-glyph":`utility-trashbin`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),oW=r((()=>{LJe(),BJe(),UJe(),KJe(),JJe(),ZJe(),eYe(),rYe(),oYe(),cYe(),dYe(),mYe(),_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2940180.

```text
46,7.46,0,0,1,17.07,13Z`},null,-1)]])}var xNt,SNt,CNt,wNt=r((()=>{je(),xNt={},SNt={xmlns:`http://www.w3.org/2000/svg`,width:`20`,height:`20`,viewBox:`0 0 20 20`},CNt=Ae(xNt,[[`render`,bNt]])})),TNt,ENt=r(((
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 38089.

```text
ze-24 cc-button-icon "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="mark-menu" aria-hidden="true"><path d="m20.07 6h-16.13c-1.6 0-1.93-.33-1.93-
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 39092.

```text
ze-24 cc-button-icon "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="mark-cross" aria-hidden="true"><path d="m6.1 20.77c-1.13 1.13-1.6 1.13-2.73 
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 60832.

```text
20 sidebar-glyph-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="tool-magnifier-blank" aria-hidden="true"><path d="m11 18.33c4.15 0 7.33-3.19
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 61888.

```text
20 sidebar-glyph-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="tool-magnifier-blank" aria-hidden="true"><path d="m11 18.33c4.15 0 7.33-3.19
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 63225.

```text
con sidebar-auth-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="user-badge-plus" aria-hidden="true"><path d="m0 20.03c0-2 .63-2.9 2.47-3.63l
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 64651.

```text
con sidebar-auth-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrow-triangle-enter-right" aria-hidden="true"><path d="m13.33 7.67 3.87 3.8
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 65891.

```text
ebar-footer-link-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="square-fill-question" aria-hidden="true"><path d="m17.03 22h-10.07c-3.67 0-4
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 67152.

```text
ebar-footer-link-icon"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="layout-text-languages" aria-hidden="true"><path d="m11.63 24h-.43c-1.03 0-1.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 69735.

```text
lyph cc-icon-size-16 "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="utility-cogwheel" aria-hidden="true"><path d="m9.57 20.53-1.17 1.27c-.37.4-.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 71011.

```text
lyph cc-icon-size-16 "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrow-triangle-flip-vertical" aria-hidden="true"><path d="m18 8.13c0-1.6-.53
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 71950.

```text
lyph cc-icon-size-16 "
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="emote-face-smile-badge-plus" aria-hidden="true"><path d="m7 11.33c1.07 0 2-.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 73077.

```text
rd-layout-icon resize"
            >

                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-glyph="arrows-stroke-expand-diagonal-b" aria-hidden="true"><path d="m2 9.07v-5.63c0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 150629.

```text
  `}function un(e){if(e===void 0)return{width:0,height:0};let t=document.createElementNS(`http://www.w3.org/2000/svg`,`svg`);t.innerHTML=e,document.body.appendChild(t);let n=t.getBBox();return document.body
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 164005.

```text
w),!1}var Bee=r((()=>{})),mr,Vee=r((()=>{mr=`
<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <image x="7.5" y="7.5" width="25" height="25" />
</svg>
`}));function Hee(e){let{from
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 217646.

```text
ng`,path:`vintage`},wood:{format:`png`,path:`wood`}}})),aie,oie=r((()=>{aie=`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <path opacity="0.2" d="M29.0815 15.8433C30.0895 13.11
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 226264.

```text
)}var la=r((()=>{})),Lie,Rie=r((()=>{Lie=`
<svg viewBox="0 0 40 40" fill="#ffa704" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="12.5" width="30" height="15" rx="3" fill="inherit" />
  <text fill="#6
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 231491.

```text
 Sa({className:e=``,path:t=``,size:n=`24`,viewBox:r=`0 0 18 19`}){return`
    <svg xmlns="http://www.w3.org/2000/svg" class="${e}" width="${n}" height="${n}" viewBox="${r}">
      ${t}
    </svg>
  `}var Ca
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 233499.

```text
e)}var Tae=r((()=>{})),Eae,Dae=r((()=>{Eae=`
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 19">
  <defs>
    <style>
      .cls-1 {
        opacity: 0.3;
      }


```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 383257.

```text
`,`summary`,`title`,`value`,`style`,`xmlns`]),Pe=`http://www.w3.org/1998/Math/MathML`,Fe=`http://www.w3.org/2000/svg`,Ie=`http://www.w3.org/1999/xhtml`,Le=Ie,Re=!1,N=null,ze=Vh({},[Pe,Fe,Ie],tg),Be=Vh({},[`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1713157.

```text
{IJe={"data-glyph":`arrow-caret-vertical`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RJe(e,t){return k(),f(`svg`,zJe,[...t[0]||=[p(`path`,{d:`m21.13 7.07.07.07c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1713579.

```text
{zJe={"data-glyph":`arrow-chevron-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VJe(e,t){return k(),f(`svg`,HJe,[...t[0]||=[p(`path`,{d:`m17.93 2h.13c1.6 0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1714129.

```text
)=>{HJe={"data-glyph":`arrow-chevron-end`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WJe(e,t){return k(),f(`svg`,GJe,[...t[0]||=[p(`path`,{d:`m16.27 21.13-.07.0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1714550.

```text
=>{GJe={"data-glyph":`arrow-chevron-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QU(e,t){return k(),f(`svg`,qJe,[...t[0]||=[p(`path`,{d:`m7.73 2.87.07-.07c1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1714971.

```text
>{qJe={"data-glyph":`arrow-chevron-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function YJe(e,t){return k(),f(`svg`,XJe,[...t[0]||=[p(`path`,{d:`m6.07 22h-.13c-1.6
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1715521.

```text
>{XJe={"data-glyph":`arrow-chevron-start`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function QJe(e,t){return k(),f(`svg`,$Je,[...t[0]||=[p(`path`,{d:`m2.87 16.93-.07-.0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1715942.

```text
)=>{$Je={"data-glyph":`arrow-chevron-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tYe(e,t){return k(),f(`svg`,nYe,[...t[0]||=[p(`path`,{d:`m10 3.93c0-1.6.33-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1716431.

```text
)=>{nYe={"data-glyph":`arrow-line-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iYe(e,t){return k(),f(`svg`,aYe,[...t[0]||=[p(`path`,{d:`m20.07 10c1.6 0 1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1716922.

```text
(()=>{aYe={"data-glyph":`arrow-line-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function $U(e,t){return k(),f(`svg`,sYe,[...t[0]||=[p(`path`,{d:`m3.93 14c-1.6 0-1.9
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1717413.

```text
()=>{sYe={"data-glyph":`arrow-line-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lYe(e,t){return k(),f(`svg`,uYe,[...t[0]||=[p(`path`,{d:`m14 20.07c0 1.6-.3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1717907.

```text
((()=>{uYe={"data-glyph":`arrow-line-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function fYe(e,t){return k(),f(`svg`,pYe,[...t[0]||=[p(`path`,{d:`m3 12c0-5.77 4.73-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1718470.

```text
(()=>{pYe={"data-glyph":`arrow-spin-left`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function hYe(e,t){return k(),f(`svg`,gYe,[...t[0]||=[p(`path`,{d:`m13 22.47c-3.63 0-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1719089.

```text
(()=>{gYe={"data-glyph":`arrow-spin-undo`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function vYe(e,t){return k(),f(`svg`,yYe,[...t[0]||=[p(`path`,{d:`m10 3.93c0-1.6.33-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1719630.

```text
"data-glyph":`arrow-triangle-edge-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xYe(e,t){return k(),f(`svg`,SYe,[...t[0]||=[p(`path`,{d:`m8.9 13 9.47-9.43 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1720283.

```text
ta-glyph":`arrow-triangle-exit-right-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wYe(e,t){return k(),f(`svg`,TYe,[...t[0]||=[p(`path`,{d:`m18 8.13c0-1.6-.53
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1721001.

```text
ata-glyph":`arrow-triangle-flip-vertical`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function DYe(e,t){return k(),f(`svg`,OYe,[...t[0]||=[p(`path`,{d:`m3.57 9.53h13.27v5
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1721423.

```text
"data-glyph":`arrow-triangle-point-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function AYe(e,t){return k(),f(`svg`,jYe,[...t[0]||=[p(`path`,{d:`m10.5 3.43c0-1.03.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1722052.

```text
ta-glyph":`arrow-triangle-tray-in-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NYe(e,t){return k(),f(`svg`,PYe,[...t[0]||=[p(`path`,{d:`m15.57 14.93-.02-.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1722967.

```text
((()=>{PYe={"data-glyph":`board-analysis`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IYe(e,t){return k(),f(`svg`,LYe,[...t[0]||=[p(`path`,{d:`m15.33 22h-10.67c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1723526.

```text
={"data-glyph":`board-arrow-diagonal-out`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zYe(e,t){return k(),f(`svg`,BYe,[...t[0]||=[p(`path`,{d:`m6 8h-4v4h4zm0 0h4
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1724281.

```text
()=>{BYe={"data-glyph":`board-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HYe(e,t){return k(),f(`svg`,UYe,[...t[0]||=[p(`path`,{d:`m6 8h-4v4h4zm0 0h4
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1725019.

```text
>{UYe={"data-glyph":`board-badge-warning`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GYe(e,t){return k(),f(`svg`,KYe,[...t[0]||=[p(`path`,{d:`m2 20h4v-4h-4zm4-4
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1725676.

```text
r((()=>{KYe={"data-glyph":`board-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JYe(e,t){return k(),f(`svg`,YYe,[...t[0]||=[p(`path`,{d:`m19.33 22h-14.67c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1726124.

```text
>{YYe={"data-glyph":`board-simple-expand`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ZYe(e,t){return k(),f(`svg`,QYe,[...t[0]||=[p(`path`,{d:`m2 20h7.06c.43.75.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1726733.

```text
{QYe={"data-glyph":`board-simple-magnify`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eXe(e,t){return k(),f(`svg`,tXe,[...t[0]||=[p(`path`,{d:`m2 20h5v-5h-5zm-2-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1727580.

```text
e={"data-glyph":`board-simple-stack-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rXe(e,t){return k(),f(`svg`,iXe,[...t[0]||=[p(`path`,{d:`m19.33 16h-1.33v-7
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1728067.

```text
=>{iXe={"data-glyph":`board-simple-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oXe(e,t){return k(),f(`svg`,sXe,[...t[0]||=[p(`path`,{d:`m2 20h2.63c.54.69 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1728695.

```text
=>{sXe={"data-glyph":`board-simple-watch`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eW(e,t){return k(),f(`svg`,lXe,[...t[0]||=[p(`path`,{d:`m19.33 22h-14.67c-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1729147.

```text
lXe,uXe=r((()=>{lXe={"data-glyph":`board`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function dXe(e,t){return k(),f(`svg`,fXe,[...t[0]||=[p(`path`,{d:`m4.73 17.86 13.17-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1729591.

```text
=r((()=>{fXe={"data-glyph":`circle-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function mXe(e,t){return k(),f(`svg`,hXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1730072.

```text
)=>{hXe={"data-glyph":`circle-fill-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _Xe(e,t){return k(),f(`svg`,vXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1730680.

```text
)=>{vXe={"data-glyph":`circle-fill-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function bXe(e,t){return k(),f(`svg`,xXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1731233.

```text
e={"data-glyph":`circle-fill-exclamation`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function CXe(e,t){return k(),f(`svg`,wXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1731774.

```text
()=>{wXe={"data-glyph":`circle-fill-info`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function EXe(e,t){return k(),f(`svg`,DXe,[...t[0]||=[p(`path`,{d:`m12 1.5c5.8 0 10.5
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1732427.

```text
{DXe={"data-glyph":`circle-fill-question`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kXe(e,t){return k(),f(`svg`,AXe,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1732942.

```text
()=>{AXe={"data-glyph":`circle-fill-star`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),MXe=r((()=>{}));function NXe(e,t){return k(),f(`svg`,PXe,[...t[0]||=[p(`path`,{d:`m1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1733361.

```text
>{PXe={"data-glyph":`circle-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IXe(e,t){return k(),f(`svg`,LXe,[...t[0]||=[p(`path`,{d:`m11 22.5c-5.77 0-1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1734238.

```text
Xe={"data-glyph":`circle-target-practice`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zXe(e,t){return k(),f(`svg`,BXe,[...t[0]||=[p(`path`,{d:`m14.57 20h-5.13c-1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1734705.

```text
()=>{BXe={"data-glyph":`device-bulb-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HXe(e,t){return k(),f(`svg`,UXe,[...t[0]||=[p(`path`,{d:`m12 3c-.83 0-1.5-.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1735559.

```text
()=>{UXe={"data-glyph":`device-bulb-glow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GXe(e,t){return k(),f(`svg`,KXe,[...t[0]||=[p(`path`,{d:`m8 22c-.67 0-1-.33
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1736483.

```text
=>{KXe={"data-glyph":`device-chip-exclam`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JXe(e,t){return k(),f(`svg`,YXe,[...t[0]||=[p(`path`,{d:`m9.07 20h5.9l-.13-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1737036.

```text
={"data-glyph":`device-computer-analysis`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function ZXe(e,t){return k(),f(`svg`,QXe,[...t[0]||=[p(`path`,{d:`m1.97 16h.03v-11.3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1737580.

```text
{QXe={"data-glyph":`device-computer-chip`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function eZe(e,t){return k(),f(`svg`,tZe,[...t[0]||=[p(`path`,{d:`m17.33 22h-10.67c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1738040.

```text
=r((()=>{tZe={"data-glyph":`device-phone`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rZe(e,t){return k(),f(`svg`,iZe,[...t[0]||=[p(`path`,{d:`m4.67 22c-2 0-2.67
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1738530.

```text
r((()=>{iZe={"data-glyph":`document-blog`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function oZe(e,t){return k(),f(`svg`,sZe,[...t[0]||=[p(`path`,{d:`m6 23.67c-1.03.73-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1738880.

```text
={"data-glyph":`document-book-mark-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function lZe(e,t){return k(),f(`svg`,uZe,[...t[0]||=[p(`path`,{d:`m5.34 21.81 6.66-4
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1739383.

```text
{"data-glyph":`document-book-mark-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tW(e,t){return k(),f(`svg`,fZe,[...t[0]||=[p(`path`,{d:`m18.57 22h-13.9c-2 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1739836.

```text
=>{fZe={"data-glyph":`document-book-mark`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),mZe=r((()=>{}));function hZe(e,t){return k(),f(`svg`,gZe,[...t[0]||=[p(`path`,{d:`m1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1740860.

```text
>{gZe={"data-glyph":`document-book-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function vZe(e,t){return k(),f(`svg`,yZe,[...t[0]||=[p(`path`,{d:`m2 3.43c0-1.03.4-1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1741476.

```text
yZe={"data-glyph":`document-folder-board`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function xZe(e,t){return k(),f(`svg`,SZe,[...t[0]||=[p(`path`,{d:`m16 6.23c-1.27 0-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1742321.

```text
data-glyph":`dots-grid-2x3-round-columns`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function wZe(e,t){return k(),f(`svg`,TZe,[...t[0]||=[p(`path`,{d:`m10.5 22h3v-8h2.4c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1742831.

```text
)=>{TZe={"data-glyph":`element-cloud-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function DZe(e,t){return k(),f(`svg`,OZe,[...t[0]||=[p(`path`,{d:`m7.3 21.03c-2.03 1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1743274.

```text
)=>{OZe={"data-glyph":`element-star-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function AZe(e,t){return k(),f(`svg`,jZe,[...t[0]||=[p(`path`,{d:`m12 18.17c2 0 3.77
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1743872.

```text
()=>{jZe={"data-glyph":`emote-face-smile`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function NZe(e,t){return k(),f(`svg`,PZe,[...t[0]||=[p(`path`,{d:`m18.13 15.83-6.13 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1744284.

```text
()=>{PZe={"data-glyph":`emote-heart-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function IZe(e,t){return k(),f(`svg`,LZe,[...t[0]||=[p(`path`,{d:`m18.63 16.67-6.63 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1744879.

```text
=>{LZe={"data-glyph":`emote-heart-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function zZe(e,t){return k(),f(`svg`,BZe,[...t[0]||=[p(`path`,{d:`m19 20v2h-14v-2zm-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1745458.

```text
=r((()=>{BZe={"data-glyph":`game-crown-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function HZe(e,t){return k(),f(`svg`,UZe,[...t[0]||=[p(`path`,{d:`m5.8 21.8h-.13c-1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1746045.

```text
WZe=r((()=>{UZe={"data-glyph":`game-flag`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function GZe(e,t){return k(),f(`svg`,KZe,[...t[0]||=[p(`path`,{d:`m18 19.83c-4.93 3.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1746638.

```text
(()=>{KZe={"data-glyph":`game-lesson-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function JZe(e,t){return k(),f(`svg`,YZe,[...t[0]||=[p(`path`,{d:`m3.07 13.53-2.03-1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1747244.

```text
e=r((()=>{YZe={"data-glyph":`game-lesson`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),ZZe=r((()=>{}));function QZe(e,t){return k(),f(`svg`,$Ze,[...t[0]||=[p(`path`,{d:`m5
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1747668.

```text
(()=>{$Ze={"data-glyph":`game-time-blitz`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function tQe(e,t){return k(),f(`svg`,nQe,[...t[0]||=[p(`path`,{d:`m7.17 15.3 1.43 1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1748250.

```text
()=>{nQe={"data-glyph":`game-time-bullet`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iQe(e,t){return k(),f(`svg`,aQe,[...t[0]||=[p(`path`,{d:`m7 20h10c0-4.07-3.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1748868.

```text
)=>{aQe={"data-glyph":`game-time-classic`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function sQe(e,t){return k(),f(`svg`,cQe,[...t[0]||=[p(`path`,{d:`m.93 11.63c3.3-1.3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1749677.

```text
(()=>{cQe={"data-glyph":`game-time-daily`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function uQe(e,t){return k(),f(`svg`,dQe,[...t[0]||=[p(`path`,{d:`m.2 23.8c3.47-4.67
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1750411.

```text
(()=>{dQe={"data-glyph":`game-time-hyper`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function pQe(e,t){return k(),f(`svg`,mQe,[...t[0]||=[p(`path`,{d:`m11.97 14.63c-.9 0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1750943.

```text
(()=>{mQe={"data-glyph":`game-time-rapid`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function gQe(e,t){return k(),f(`svg`,_Qe,[...t[0]||=[p(`path`,{d:`m.93 11.63c3.3-1.3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1751963.

```text
>{_Qe={"data-glyph":`game-type-960-daily`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function yQe(e,t){return k(),f(`svg`,bQe,[...t[0]||=[p(`path`,{d:`m15.5 2h-2v1.62c4.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1752840.

```text
=>{bQe={"data-glyph":`game-type-960-live`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),SQe=r((()=>{}));function CQe(e,t){return k(),f(`svg`,wQe,[...t[0]||=[p(`path`,{d:`m3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1754464.

```text
=>{wQe={"data-glyph":`game-type-bughouse`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function EQe(e,t){return k(),f(`svg`,DQe,[...t[0]||=[p(`path`,{d:`m22 4.67v7.03l-7.3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1754913.

```text
>{DQe={"data-glyph":`game-type-classroom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function kQe(e,t){return k(),f(`svg`,AQe,[...t[0]||=[p(`path`,{d:`m10.03 20.17v-2.17
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1755821.

```text
=>{AQe={"data-glyph":`game-type-computer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function MQe(e,t){return k(),f(`svg`,NQe,[...t[0]||=[p(`path`,{d:`m11.73 18.67c3.07 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1756496.

```text
{NQe={"data-glyph":`game-type-crazyhouse`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function FQe(e,t){return k(),f(`svg`,IQe,[...t[0]||=[p(`path`,{d:`m16.1 3.13-3.2 4.1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1757138.

```text
{IQe={"data-glyph":`game-type-fourplayer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function RQe(e,t){return k(),f(`svg`,zQe,[...t[0]||=[p(`path`,{d:`m21.17 22h-18.33c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1757663.

```text
((()=>{zQe={"data-glyph":`game-type-hill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function VQe(e,t){return k(),f(`svg`,HQe,[...t[0]||=[p(`path`,{d:`m5.53 20.53c-1.5 0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1758612.

```text
HQe={"data-glyph":`game-type-three-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function WQe(e,t){return k(),f(`svg`,GQe,[...t[0]||=[p(`path`,{d:`m21.77 18.7-8.5 4.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1760346.

```text
=>{GQe={"data-glyph":`game-type-variants`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function qQe(e,t){return k(),f(`svg`,JQe,[...t[0]||=[p(`path`,{d:`m19.6 22h-.53c-2 0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1760882.

```text
>{JQe={"data-glyph":`graph-bars-hollow-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function XQe(e,t){return k(),f(`svg`,ZQe,[...t[0]||=[p(`path`,{d:`m20.57 22h-1.33c-.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1761482.

```text
ZQe={"data-glyph":`graph-bars-statistics`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function $Qe(e,t){return k(),f(`svg`,e$e,[...t[0]||=[p(`path`,{d:`m19 8.5c-2 0-3.5-1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1761994.

```text
)=>{e$e={"data-glyph":`graph-nodes-share`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function n$e(e,t){return k(),f(`svg`,r$e,[...t[0]||=[p(`path`,{d:`m4.43 17.07c-.6-1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1762571.

```text
$e=r((()=>{r$e={"data-glyph":`hand-loser`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function a$e(e,t){return k(),f(`svg`,o$e,[...t[0]||=[p(`path`,{d:`m10.97 19.13c.83.5
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1763381.

```text
s$e=r((()=>{o$e={"data-glyph":`hand-pawn`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),c$e=r((()=>{}));function l$e(e,t){return k(),f(`svg`,u$e,[...t[0]||=[p(`path`,{d:`m4
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1764334.

```text
)=>{u$e={"data-glyph":`layout-list-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function f$e(e,t){return k(),f(`svg`,p$e,[...t[0]||=[p(`path`,{d:`m19.33 22h-14.67c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1764785.

```text
ata-glyph":`layout-table-cell-properties`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function h$e(e,t){return k(),f(`svg`,g$e,[...t[0]||=[p(`path`,{d:`m11 21v-18h2v18zm8
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1765258.

```text
$e={"data-glyph":`layout-table-columns-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function v$e(e,t){return k(),f(`svg`,y$e,[...t[0]||=[p(`path`,{d:`m4.93 16.37-4.47-3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1766074.

```text
{y$e={"data-glyph":`local-door-left-exit`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function x$e(e,t){return k(),f(`svg`,S$e,[...t[0]||=[p(`path`,{d:`m9.67 11.57c.4-.97
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1766560.

```text
((()=>{S$e={"data-glyph":`local-explorer`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function w$e(e,t){return k(),f(`svg`,T$e,[...t[0]||=[p(`path`,{d:`m20.87 10h-17.73c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1767090.

```text
r((()=>{T$e={"data-glyph":`local-library`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function D$e(e,t){return k(),f(`svg`,O$e,[...t[0]||=[p(`path`,{d:`m8.43 23c-1.7-.03-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1767683.

```text
$e=r((()=>{O$e={"data-glyph":`logo-apple`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function nW(e,t){return k(),f(`svg`,A$e,[...t[0]||=[p(`path`,{d:`m21.2 7.97-11.33 11
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1768079.

```text
$e=r((()=>{A$e={"data-glyph":`mark-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function rW(e,t){return k(),f(`svg`,M$e,[...t[0]||=[p(`path`,{d:`m6.1 20.77c-1.13 1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1768609.

```text
$e=r((()=>{M$e={"data-glyph":`mark-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function P$e(e,t){return k(),f(`svg`,F$e,[...t[0]||=[p(`path`,{d:`m20 14.5c-1.34 0-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1769088.

```text
={"data-glyph":`mark-ellipsis-horizontal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function L$e(e,t){return k(),f(`svg`,R$e,[...t[0]||=[p(`path`,{d:`m20.07 14h-16.13c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1769435.

```text
$e=r((()=>{R$e={"data-glyph":`mark-minus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function B$e(e,t){return k(),f(`svg`,V$e,[...t[0]||=[p(`path`,{d:`m12.07 22h-.13c-1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1769920.

```text
H$e=r((()=>{V$e={"data-glyph":`mark-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function U$e(e,t){return k(),f(`svg`,W$e,[...t[0]||=[p(`path`,{d:`m18 1.5v3.07l3.97-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1770532.

```text
={"data-glyph":`media-audio-speaker-mute`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function K$e(e,t){return k(),f(`svg`,q$e,[...t[0]||=[p(`path`,{d:`m17.33 17c-.4.43-.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1771387.

```text
{"data-glyph":`media-audio-speaker-noise`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Y$e(e,t){return k(),f(`svg`,X$e,[...t[0]||=[p(`path`,{d:`m20.33 22h-16.67c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1771927.

```text
=>{X$e={"data-glyph":`media-camera-photo`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Q$e(e,t){return k(),f(`svg`,$$e,[...t[0]||=[p(`path`,{d:`m17.33 22h-.67c-2 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1772397.

```text
>{$$e={"data-glyph":`media-control-pause`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function t1e(e,t){return k(),f(`svg`,n1e,[...t[0]||=[p(`path`,{d:`m20.5 12.8-12.73 8
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1772728.

```text
=>{n1e={"data-glyph":`media-control-play`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function i1e(e,t){return k(),f(`svg`,a1e,[...t[0]||=[p(`path`,{d:`m12 20.3c-1.22 0-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1773521.

```text
r((()=>{a1e={"data-glyph":`media-eye-off`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function s1e(e,t){return k(),f(`svg`,c1e,[...t[0]||=[p(`path`,{d:`m12 20.3c-5 0-9.13
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1773972.

```text
((()=>{c1e={"data-glyph":`media-eye-seen`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function iW(e,t){return k(),f(`svg`,u1e,[...t[0]||=[p(`path`,{d:`m17.43 7.5-.38.5c-.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1774728.

```text
yph":`membership-tier-diamond-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function f1e(e,t){return k(),f(`svg`,p1e,[...t[0]||=[p(`path`,{d:`m22.57 8.87-9.7 12
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1775132.

```text
e={"data-glyph":`membership-tier-diamond`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function h1e(e,t){return k(),f(`svg`,g1e,[...t[0]||=[p(`path`,{d:`m2.47 10.57c-1.9-1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1775576.

```text
{g1e={"data-glyph":`membership-tier-gold`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function v1e(e,t){return k(),f(`svg`,y1e,[...t[0]||=[p(`path`,{d:`m12.03 22.33c-7.23
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1775987.

```text
={"data-glyph":`membership-tier-platinum`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function x1e(e,t){return k(),f(`svg`,S1e,[...t[0]||=[p(`path`,{d:`m4.83 21.9-3.13 1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1776608.

```text
{"data-glyph":`message-bubble-fill-check`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function w1e(e,t){return k(),f(`svg`,T1e,[...t[0]||=[p(`path`,{d:`m4.83 21.9-3.13 1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1777348.

```text
{"data-glyph":`message-bubble-fill-cross`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function D1e(e,t){return k(),f(`svg`,O1e,[...t[0]||=[p(`path`,{d:`m22.2 23.13-2.2-1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1778201.

```text
={"data-glyph":`message-bubble-fill-pair`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function A1e(e,t){return k(),f(`svg`,j1e,[...t[0]||=[p(`path`,{d:`m19.33 21h-14.67c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1778663.

```text
j1e={"data-glyph":`message-envelope-fill`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function N1e(e,t){return k(),f(`svg`,P1e,[...t[0]||=[p(`path`,{d:`m12 22.5c-5.8 0-10
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1779178.

```text
()=>{P1e={"data-glyph":`move-circle-best`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),I1e=r((()=>{}));function L1e(e,t){return k(),f(`svg`,R1e,[...t[0]||=[p(`path`,{d:`m2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1780333.

```text
)=>{R1e={"data-glyph":`piece-knight-fork`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function B1e(e,t){return k(),f(`svg`,V1e,[...t[0]||=[p(`path`,{d:`m14.3 10.5c.23 7.2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1780825.

```text
=>{V1e={"data-glyph":`piece-pawn-brand-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function U1e(e,t){return k(),f(`svg`,W1e,[...t[0]||=[p(`path`,{d:`m15.53 22h-15.07c0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1781713.

```text
)=>{W1e={"data-glyph":`piece-pawn-signal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function K1e(e,t){return k(),f(`svg`,q1e,[...t[0]||=[p(`path`,{d:`m16.63 18.73h-9.3c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1782458.

```text
)=>{q1e={"data-glyph":`piece-simple-king`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Y1e(e,t){return k(),f(`svg`,X1e,[...t[0]||=[p(`path`,{d:`m16.93 22c-.01-1.2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1783561.

```text
1e=r((()=>{X1e={"data-glyph":`pieces-all`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Q1e(e,t){return k(),f(`svg`,$1e,[...t[0]||=[p(`path`,{d:`m11.33 22h-8.67c-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1784045.

```text
{$1e={"data-glyph":`rectangle-fill-stack`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),t0e=r((()=>{}));function n0e(e,t){return k(),f(`svg`,r0e,[...t[0]||=[p(`path`,{d:`m1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1784592.

```text
>{r0e={"data-glyph":`square-fill-checked`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function a0e(e,t){return k(),f(`svg`,o0e,[...t[0]||=[p(`path`,{d:`m17.03 22h-10.07c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1785204.

```text
)=>{o0e={"data-glyph":`square-fill-equal`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function c0e(e,t){return k(),f(`svg`,l0e,[...t[0]||=[p(`path`,{d:`m17.03 22h-10.07c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1785699.

```text
)=>{l0e={"data-glyph":`square-fill-minus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function d0e(e,t){return k(),f(`svg`,f0e,[...t[0]||=[p(`path`,{d:`m17.03 22h-10.07c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1786325.

```text
()=>{f0e={"data-glyph":`square-fill-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function m0e(e,t){return k(),f(`svg`,h0e,[...t[0]||=[p(`path`,{d:`m19.33 16h-8.67c-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1786808.

```text
e={"data-glyph":`square-fill-stack-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function _0e(e,t){return k(),f(`svg`,aW,[...t[0]||=[p(`path`,{d:`m17.03 19c1.97 0 1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1787293.

```text
=>{aW={"data-glyph":`square-hollow-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function y0e(e,t){return k(),f(`svg`,b0e,[...t[0]||=[p(`path`,{d:`m6.07 8.5h-.13c-1.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1789134.

```text
e={"data-glyph":`time-calendar-fill-week`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function S0e(e,t){return k(),f(`svg`,C0e,[...t[0]||=[p(`path`,{d:`m13 22.47c-3.83 0-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1789857.

```text
={"data-glyph":`time-clock-hollow-rewind`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function T0e(e,t){return k(),f(`svg`,E0e,[...t[0]||=[p(`path`,{d:`m15.97 15.3-3.7-2c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1790369.

```text
)=>{E0e={"data-glyph":`time-clock-hollow`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function O0e(e,t){return k(),f(`svg`,k0e,[...t[0]||=[p(`path`,{d:`m7.03 20h9.97c0-2.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1790976.

```text
()=>{k0e={"data-glyph":`time-hourglass-3`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function j0e(e,t){return k(),f(`svg`,M0e,[...t[0]||=[p(`path`,{d:`m5.5 22c-3.03 0-5.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1791763.

```text
(()=>{M0e={"data-glyph":`tool-binoculars`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function P0e(e,t){return k(),f(`svg`,F0e,[...t[0]||=[p(`path`,{d:`m13.8 22.3c-1.77 1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1792441.

```text
r((()=>{F0e={"data-glyph":`tool-dumbbell`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function L0e(e,t){return k(),f(`svg`,R0e,[...t[0]||=[p(`path`,{d:`m8.5 11.87-6.03-8.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1792808.

```text
e=r((()=>{R0e={"data-glyph":`tool-filter`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function B0e(e,t){return k(),f(`svg`,V0e,[...t[0]||=[p(`path`,{d:`m17.33 22h-10.77c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1793261.

```text
(()=>{V0e={"data-glyph":`tool-lock-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function U0e(e,t){return k(),f(`svg`,W0e,[...t[0]||=[p(`path`,{d:`m17.33 22h-10.77c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1793827.

```text
()=>{W0e={"data-glyph":`tool-lock-closed`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function K0e(e,t){return k(),f(`svg`,q0e,[...t[0]||=[p(`path`,{d:`m17.03 8.67c.9 0 1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1794353.

```text
r((()=>{q0e={"data-glyph":`tool-lock-key`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Y0e(e,t){return k(),f(`svg`,X0e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1794937.

```text
{X0e={"data-glyph":`tool-magnifier-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function Q0e(e,t){return k(),f(`svg`,$0e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1795587.

```text
={"data-glyph":`tool-magnifier-checker-1`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function t2e(e,t){return k(),f(`svg`,n2e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1796239.

```text
={"data-glyph":`tool-magnifier-checker-2`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function i2e(e,t){return k(),f(`svg`,a2e,[...t[0]||=[p(`path`,{d:`m11 18.33c4.15 0 7
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1797010.

```text
>{a2e={"data-glyph":`tool-magnifier-star`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function s2e(e,t){return k(),f(`svg`,c2e,[...t[0]||=[p(`path`,{d:`m7.47 20.53-4.57 1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1797515.

```text
()=>{c2e={"data-glyph":`tool-pencil-line`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function u2e(e,t){return k(),f(`svg`,d2e,[...t[0]||=[p(`path`,{d:`m3.43 6h17.13c1.03
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1797853.

```text
data-glyph":`triangle-fill-medium-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function p2e(e,t){return k(),f(`svg`,m2e,[...t[0]||=[p(`path`,{d:`m20.57 18h-17.13c-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1798191.

```text
={"data-glyph":`triangle-fill-medium-top`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function g2e(e,t){return k(),f(`svg`,_2e,[...t[0]||=[p(`path`,{d:`m4.93 8h14.13c1.03
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1798518.

```text
"data-glyph":`triangle-fill-small-bottom`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),y2e=r((()=>{}));function b2e(e,t){return k(),f(`svg`,x2e,[...t[0]||=[p(`path`,{d:`m0
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1799320.

```text
2e={"data-glyph":`user-badge-arrow-right`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function C2e(e,t){return k(),f(`svg`,w2e,[...t[0]||=[p(`path`,{d:`m0 20.03c0-2 .63-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1800096.

```text
(()=>{w2e={"data-glyph":`user-badge-plus`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function E2e(e,t){return k(),f(`svg`,D2e,[...t[0]||=[p(`path`,{d:`m0 20.03c0-2 .63-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1800729.

```text
2e=r((()=>{D2e={"data-glyph":`user-block`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function k2e(e,t){return k(),f(`svg`,A2e,[...t[0]||=[p(`path`,{d:`m2 20.03c0-2 .63-2
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1801174.

```text
 A2e,j2e=r((()=>{A2e={"data-glyph":`user`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function M2e(e,t){return k(),f(`svg`,N2e,[...t[0]||=[p(`path`,{d:`m8 18v-1.87c0-1.83
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1801973.

```text
N2e,P2e=r((()=>{N2e={"data-glyph":`users`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function F2e(e,t){return k(),f(`svg`,I2e,[...t[0]||=[p(`path`,{d:`m9.57 20.53-1.17 1
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1803040.

```text
()=>{I2e={"data-glyph":`utility-cogwheel`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function R2e(e,t){return k(),f(`svg`,z2e,[...t[0]||=[p(`path`,{d:`m13.3 23.63c-.93.4
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1803491.

```text
{z2e={"data-glyph":`utility-shield-blank`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function V2e(e,t){return k(),f(`svg`,H2e,[...t[0]||=[p(`path`,{d:`m6.5 22h11c2.57 0 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1804132.

```text
(()=>{H2e={"data-glyph":`utility-toggles`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}}));function W2e(e,t){return k(),f(`svg`,G2e,[...t[0]||=[p(`path`,{d:`m21.07 6h-18.13c-.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1804706.

```text
()=>{G2e={"data-glyph":`utility-trashbin`,"aria-hidden":`true`,viewBox:`0 0 24 24`,xmlns:`http://www.w3.org/2000/svg`}})),oW=r((()=>{LJe(),BJe(),UJe(),KJe(),JJe(),ZJe(),eYe(),rYe(),oYe(),cYe(),dYe(),mYe(),_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2940180.

```text
46,7.46,0,0,1,17.07,13Z`},null,-1)]])}var xNt,SNt,CNt,wNt=r((()=>{je(),xNt={},SNt={xmlns:`http://www.w3.org/2000/svg`,width:`20`,height:`20`,viewBox:`0 0 20 20`},CNt=Ae(xNt,[[`render`,bNt]])})),TNt,ENt=r(((
```

**Source references:** SRC-0065, SRC-0090, SRC-0751, SRC-0777, SRC-0781, SRC-1137, SRC-1150, SRC-1165  
**URL references:** <http://www.w3.org/2000/svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18117, FND-18118

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20642"></a>
## FND-20642: https://${window.Config[

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://${window.Config[",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01511"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1996773.

```text
return Am()||cf()||window.chesscom.features.includes(`web_api_domain_rpc_derived`)?rpt():`https://${window.Config[`domain.api`]}`}var apt=r((()=>{Pm(),lf(),the()}));function opt(e){return e!=null&&typeof 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2351021.

```text
return eh()||Rf()||window.chesscom.features.includes(`web_api_domain_rpc_derived`)?jrt():`https://${window.Config[`domain.api`]}`}var Nrt=r((()=>{ih(),zf(),Vf()}));function Prt(){return window.chesscom?.f
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2351021.

```text
return eh()||Rf()||window.chesscom.features.includes(`web_api_domain_rpc_derived`)?jrt():`https://${window.Config[`domain.api`]}`}var Nrt=r((()=>{ih(),zf(),Vf()}));function Prt(){return window.chesscom?.f
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://${window.Config[>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20643"></a>
## FND-20643: https://*.chess.com/*

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://*.chess.com/*",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0005",
    "SRC-0009",
    "SRC-0018",
    "SRC-0022",
    "SRC-0050"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01512"
}

### Evidence

- **SRC-0005** `chess-local-review-v0.1.6-quota-fix.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/ce0c37dc972e1378b9f9a23efac8d0139906db99a83efa11936d24496ad2ee3e.json)
  Character offset 554.

```text
orker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "bridge.js"
      ],
      "run_at": "document_start",
  
```
- **SRC-0005** `chess-local-review-v0.1.6-quota-fix.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/ce0c37dc972e1378b9f9a23efac8d0139906db99a83efa11936d24496ad2ee3e.json)
  Character offset 762.

```text
l_frames": true,
      "match_about_blank": true
    },
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "page-hook.js"
      ],
      "run_at": "document_start",
```
- **SRC-0005** `chess-local-review-v0.1.6-quota-fix.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/ce0c37dc972e1378b9f9a23efac8d0139906db99a83efa11936d24496ad2ee3e.json)
  Character offset 1083.

```text
": [
    {
      "resources": [
        "engines/**"
      ],
      "matches": [
        "https://*.chess.com/*"
      ]
    }
  ]
}

```
- **SRC-0009** `chess-local-review-v0.1.7-cee-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/a1719a80102a08c8e6dcb65127cc9d1cbf676da03fe99416caef011849794088.json)
  Character offset 554.

```text
orker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "bridge.js"
      ],
      "run_at": "document_start",
  
```
- **SRC-0009** `chess-local-review-v0.1.7-cee-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/a1719a80102a08c8e6dcb65127cc9d1cbf676da03fe99416caef011849794088.json)
  Character offset 762.

```text
l_frames": true,
      "match_about_blank": true
    },
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "page-hook.js"
      ],
      "run_at": "document_start",
```
- **SRC-0009** `chess-local-review-v0.1.7-cee-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/a1719a80102a08c8e6dcb65127cc9d1cbf676da03fe99416caef011849794088.json)
  Character offset 1083.

```text
": [
    {
      "resources": [
        "engines/**"
      ],
      "matches": [
        "https://*.chess.com/*"
      ]
    }
  ]
}

```
- **SRC-0018** `chess-local-review-v0.1.8-hide-debug-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/e7e210faed1cda736135f87d36064c9a2303078ce438bcbfe25f6151ec5a0be7.json)
  Character offset 554.

```text
orker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "bridge.js"
      ],
      "run_at": "document_start",
  
```
- **SRC-0018** `chess-local-review-v0.1.8-hide-debug-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/e7e210faed1cda736135f87d36064c9a2303078ce438bcbfe25f6151ec5a0be7.json)
  Character offset 762.

```text
l_frames": true,
      "match_about_blank": true
    },
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "page-hook.js"
      ],
      "run_at": "document_start",
```
- **SRC-0018** `chess-local-review-v0.1.8-hide-debug-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/e7e210faed1cda736135f87d36064c9a2303078ce438bcbfe25f6151ec5a0be7.json)
  Character offset 1083.

```text
": [
    {
      "resources": [
        "engines/**"
      ],
      "matches": [
        "https://*.chess.com/*"
      ]
    }
  ]
}

```
- **SRC-0022** `chess-local-review-v0.1.9-measured-progress-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 554.

```text
orker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "bridge.js"
      ],
      "run_at": "document_start",
  
```
- **SRC-0022** `chess-local-review-v0.1.9-measured-progress-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 762.

```text
l_frames": true,
      "match_about_blank": true
    },
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "page-hook.js"
      ],
      "run_at": "document_start",
```
- **SRC-0022** `chess-local-review-v0.1.9-measured-progress-update.zip!/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 1083.

```text
": [
    {
      "resources": [
        "engines/**"
      ],
      "matches": [
        "https://*.chess.com/*"
      ]
    }
  ]
}

```
- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 554.

```text
orker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "bridge.js"
      ],
      "run_at": "document_start",
  
```
- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 762.

```text
l_frames": true,
      "match_about_blank": true
    },
    {
      "matches": [
        "https://*.chess.com/*"
      ],
      "js": [
        "page-hook.js"
      ],
      "run_at": "document_start",
```
- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
  Character offset 1083.

```text
": [
    {
      "resources": [
        "engines/**"
      ],
      "matches": [
        "https://*.chess.com/*"
      ]
    }
  ]
}

```

**Source references:** SRC-0005, SRC-0009, SRC-0018, SRC-0022, SRC-0050  
**URL references:** <https://*.chess.com/*>  
**Related findings:** None assigned

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20644"></a>
## FND-20644: https://aimchess.com/try

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://aimchess.com/try",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01513"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16954.

```text
r"},"sub":[],"badge":null},{"id":"train.aimchess","type":"link","label":"Aimchess","url":"https:\/\/aimchess.com\/try","icon":{"name":"logo-aimchess","variant":"color"},"sub":[],"badge":null}],"badge":null},
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 11918.

```text
r"},"sub":[],"badge":null},{"id":"train.aimchess","type":"link","label":"Aimchess","url":"https:\/\/aimchess.com\/try","icon":{"name":"logo-aimchess","variant":"color"},"sub":[],"badge":null}],"badge":null},
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16954.

```text
r"},"sub":[],"badge":null},{"id":"train.aimchess","type":"link","label":"Aimchess","url":"https:\/\/aimchess.com\/try","icon":{"name":"logo-aimchess","variant":"color"},"sub":[],"badge":null}],"badge":null},
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://aimchess.com/try>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20645"></a>
## FND-20645: https://api.chess.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://api.chess.com",
  "type": "api_or_websocket_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01514"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 1254.

```text
 <link rel="preconnect" href="//images.chesscomfiles.com">
  <link rel="preconnect" href="https://api.chess.com" crossorigin>

  
  
    
<link
  as="font"
  crossorigin="crossorigin"
  href="/bundles/
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 1294.

```text
 <link rel="preconnect" href="//images.chesscomfiles.com">
  <link rel="preconnect" href="https://api.chess.com" crossorigin>

  
  
    
<link
  as="font"
  crossorigin="crossorigin"
  href="/bundles/
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 1254.

```text
 <link rel="preconnect" href="//images.chesscomfiles.com">
  <link rel="preconnect" href="https://api.chess.com" crossorigin>

  
  
    
<link
  as="font"
  crossorigin="crossorigin"
  href="/bundles/
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://api.chess.com>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20646"></a>
## FND-20646: https://api.chess.com/cast/game/${t}.pgn

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://api.chess.com/cast/game/${t}.pgn",
  "type": "api_or_websocket_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0187"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01515"
}

### Evidence

- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 13219.

```text
ops:{message:g(`Stream started at <a href="%href%" target="_blank">%href%</a>`,{"%href%":`https://api.chess.com/cast/game/${t}.pgn`})}})}var lt=e((()=>{v(),j()}));function ut(e,t){let n=g(`Stream started at <a href="%hre
```
- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 13392.

```text
t(e,t){let n=g(`Stream started at <a href="%href%" target="_blank">%href%</a>`,{"%href%":`https://api.chess.com/cast/game/${t}.pgn`});S({keys:[R.StreamStarted,e.id],unique:!0,notification:{behavior:{ignoreShowPopupsSetti
```

**Source references:** SRC-0187  
**URL references:** <https://api.chess.com/cast/game/${t}.pgn>  
**Related findings:** FND-18200, FND-18201, FND-19434

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20647"></a>
## FND-20647: https://assets-bots.chess.com/books/latest/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-bots.chess.com/books/latest/",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01516"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2717032.

```text
p/js/vendor/jschessengine/books/personalities/${e}.bin`,!1)}var Fxt,Ixt=r((()=>{BN(),Fxt=`https://assets-bots.chess.com/books/latest/`}));function Lxt(){return h4}function Rxt(e=`balanced`,t){f4()?.quit(),h4.clear();let n=w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2717032.

```text
p/js/vendor/jschessengine/books/personalities/${e}.bin`,!1)}var Fxt,Ixt=r((()=>{BN(),Fxt=`https://assets-bots.chess.com/books/latest/`}));function Lxt(){return h4}function Rxt(e=`balanced`,t){f4()?.quit(),h4.clear();let n=w
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-bots.chess.com/books/latest/>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20648"></a>
## FND-20648: https://assets-ds.chess.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01517"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 125118.

```text
data-glyph`],Mo=x(u({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,r=n(()=>t.c
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 125118.

```text
data-glyph`],Mo=x(u({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,r=n(()=>t.c
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1791532.

```text
ata-glyph`],eK=Za(y({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,n=l(()=>t.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2940932.

```text
ata-glyph`],g5=Ga(_({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,n=c(()=>t.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2940932.

```text
ata-glyph`],g5=Ga(_({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,n=c(()=>t.c
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com>  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20649"></a>
## FND-20649: https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01518"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 58596.

```text
24 cc-button-icon sidebar-link-icon TEMPLATE#icon-class"
      height="24"
      data-src=https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg
            width="24"
      data-icon-img="true" style="display:none;"  />
  
  

      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 59757.

```text
24 cc-button-icon sidebar-link-icon TEMPLATE#icon-class"
      height="24"
      data-src=https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg
            width="24"
      data-icon-img="true" style="display:none;"  />
  
  

      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 53760.

```text
24 cc-button-icon sidebar-link-icon TEMPLATE#icon-class"
      height="24"
      data-src=https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg
            width="24"
      data-icon-img="true" style="display:none;"  />
  
  

      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 54921.

```text
24 cc-button-icon sidebar-link-icon TEMPLATE#icon-class"
      height="24"
      data-src=https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg
            width="24"
      data-icon-img="true" style="display:none;"  />
  
  

      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 58596.

```text
24 cc-button-icon sidebar-link-icon TEMPLATE#icon-class"
      height="24"
      data-src=https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg
            width="24"
      data-icon-img="true" style="display:none;"  />
  
  

      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 59757.

```text
24 cc-button-icon sidebar-link-icon TEMPLATE#icon-class"
      height="24"
      data-src=https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg
            width="24"
      data-icon-img="true" style="display:none;"  />
  
  

      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/TEMPLATE#icon-name.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20650"></a>
## FND-20650: https://assets-ds.chess.com/color-icons/binoculars.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/binoculars.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01519"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 51900.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/binoculars.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 52993.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/binoculars.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 47064.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/binoculars.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 48157.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/binoculars.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 51900.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/binoculars.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 52993.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/binoculars.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/binoculars.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20651"></a>
## FND-20651: https://assets-ds.chess.com/color-icons/ellipsis.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/ellipsis.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01520"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 56290.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/ellipsis.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 57379.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/ellipsis.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 51454.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/ellipsis.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 52543.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/ellipsis.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 56290.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/ellipsis.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 57379.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/ellipsis.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/ellipsis.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20652"></a>
## FND-20652: https://assets-ds.chess.com/color-icons/friends.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/friends.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01521"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 54097.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/friends.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 55196.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/friends.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 49261.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/friends.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 50360.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/friends.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 54097.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/friends.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 55196.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/friends.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/friends.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20653"></a>
## FND-20653: https://assets-ds.chess.com/color-icons/lessons.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/lessons.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01522"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 47402.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/lessons.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 48489.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/lessons.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 42566.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/lessons.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 43653.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/lessons.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 47402.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/lessons.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 48489.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/lessons.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/lessons.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20654"></a>
## FND-20654: https://assets-ds.chess.com/color-icons/play-white.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/play-white.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01523"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 42466.

```text
n-size-24 cc-button-icon sidebar-link-icon sidebar-play-icon"
      height="24"
      src=https://assets-ds.chess.com/color-icons/play-white.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 43841.

```text
n-size-24 cc-button-icon sidebar-link-icon sidebar-play-icon"
      height="24"
      src=https://assets-ds.chess.com/color-icons/play-white.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 37630.

```text
n-size-24 cc-button-icon sidebar-link-icon sidebar-play-icon"
      height="24"
      src=https://assets-ds.chess.com/color-icons/play-white.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 39005.

```text
n-size-24 cc-button-icon sidebar-link-icon sidebar-play-icon"
      height="24"
      src=https://assets-ds.chess.com/color-icons/play-white.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 42466.

```text
n-size-24 cc-button-icon sidebar-link-icon sidebar-play-icon"
      height="24"
      src=https://assets-ds.chess.com/color-icons/play-white.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 43841.

```text
n-size-24 cc-button-icon sidebar-link-icon sidebar-play-icon"
      height="24"
      src=https://assets-ds.chess.com/color-icons/play-white.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/play-white.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20655"></a>
## FND-20655: https://assets-ds.chess.com/color-icons/puzzle-piece.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/puzzle-piece.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01524"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 45207.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/puzzle-piece.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 46310.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/puzzle-piece.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 40371.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/puzzle-piece.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 41474.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/puzzle-piece.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 45207.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/puzzle-piece.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 46310.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/puzzle-piece.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/puzzle-piece.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20656"></a>
## FND-20656: https://assets-ds.chess.com/color-icons/training.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/color-icons/training.svg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01525"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 49718.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/training.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 50807.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/training.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 44882.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/training.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 45971.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/training.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 49718.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/training.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 50807.

```text
c-icon-img cc-icon-size-24 cc-button-icon sidebar-link-icon "
      height="24"
      src=https://assets-ds.chess.com/color-icons/training.svg
            width="24"
      data-icon-img="true" style=""  />
  
  

        <img
      
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://assets-ds.chess.com/color-icons/training.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20657"></a>
## FND-20657: https://assets-ds.chess.com/sounds/arena/arena-end-cc7a0c2.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/arena/arena-end-cc7a0c2.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01526"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230250.

```text
e,rle,ile,ale,ole,sle,cle,lle,ule,dle,fle,ple,mle,hle,gle,_le,vle,eo,yle,ble=r((()=>{Jce=`https://assets-ds.chess.com/sounds/arena/arena-end-cc7a0c2.mp3`,Yce=`https://assets-ds.chess.com/sounds/arena/arena-start-13ef57f.mp3`,Xce=`https://asse
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/arena/arena-end-cc7a0c2.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20658"></a>
## FND-20658: https://assets-ds.chess.com/sounds/arena/arena-start-13ef57f.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/arena/arena-start-13ef57f.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01527"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230319.

```text
yle,ble=r((()=>{Jce=`https://assets-ds.chess.com/sounds/arena/arena-end-cc7a0c2.mp3`,Yce=`https://assets-ds.chess.com/sounds/arena/arena-start-13ef57f.mp3`,Xce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/bishop-3c446dc.mp3`,Zce=
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/arena/arena-start-13ef57f.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20659"></a>
## FND-20659: https://assets-ds.chess.com/sounds/bughouse-voice-commands/bishop-3c446dc.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/bishop-3c446dc.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01528"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230390.

```text
-cc7a0c2.mp3`,Yce=`https://assets-ds.chess.com/sounds/arena/arena-start-13ef57f.mp3`,Xce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/bishop-3c446dc.mp3`,Zce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/diagonals-0364470.mp3`,Q
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/bishop-3c446dc.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20660"></a>
## FND-20660: https://assets-ds.chess.com/sounds/bughouse-voice-commands/diagonals-0364470.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/diagonals-0364470.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01529"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230474.

```text
,Xce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/bishop-3c446dc.mp3`,Zce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/diagonals-0364470.mp3`,Qce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/dont-trade-f703679.mp3`,
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/diagonals-0364470.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20661"></a>
## FND-20661: https://assets-ds.chess.com/sounds/bughouse-voice-commands/dont-trade-f703679.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/dont-trade-f703679.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01530"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230561.

```text
e=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/diagonals-0364470.mp3`,Qce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/dont-trade-f703679.mp3`,$ce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/i-have-mate-e6585d5.mp3`
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/dont-trade-f703679.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20662"></a>
## FND-20662: https://assets-ds.chess.com/sounds/bughouse-voice-commands/i-have-mate-e6585d5.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/i-have-mate-e6585d5.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01531"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230649.

```text
=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/dont-trade-f703679.mp3`,$ce=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/i-have-mate-e6585d5.mp3`,ele=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/knight-a33273c.mp3`,tle=
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/i-have-mate-e6585d5.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20663"></a>
## FND-20663: https://assets-ds.chess.com/sounds/bughouse-voice-commands/knight-a33273c.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/knight-a33273c.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01532"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230738.

```text
`https://assets-ds.chess.com/sounds/bughouse-voice-commands/i-have-mate-e6585d5.mp3`,ele=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/knight-a33273c.mp3`,tle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-bishop-7f2e592.mp3`,n
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/knight-a33273c.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20664"></a>
## FND-20664: https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-bishop-7f2e592.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-bishop-7f2e592.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01533"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230822.

```text
,ele=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/knight-a33273c.mp3`,tle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-bishop-7f2e592.mp3`,nle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-diagonals-72fef77.mp3
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-bishop-7f2e592.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20665"></a>
## FND-20665: https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-diagonals-72fef77.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-diagonals-72fef77.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01534"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230909.

```text
e=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-bishop-7f2e592.mp3`,nle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-diagonals-72fef77.mp3`,rle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-knight-4b68667.mp3`,i
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-diagonals-72fef77.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20666"></a>
## FND-20666: https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-knight-4b68667.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-knight-4b68667.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01535"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 230999.

```text
https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-diagonals-72fef77.mp3`,rle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-knight-4b68667.mp3`,ile=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-pawn-5ddd563.mp3`,ale
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-knight-4b68667.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20667"></a>
## FND-20667: https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-pawn-5ddd563.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-pawn-5ddd563.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01536"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231086.

```text
e=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-knight-4b68667.mp3`,ile=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-pawn-5ddd563.mp3`,ale=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-queen-a4e5b21.mp3`,ol
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-pawn-5ddd563.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20668"></a>
## FND-20668: https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-queen-a4e5b21.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-queen-a4e5b21.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01537"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231171.

```text
ile=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-pawn-5ddd563.mp3`,ale=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-queen-a4e5b21.mp3`,ole=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-rook-dfb96f0.mp3`,sle
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-queen-a4e5b21.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20669"></a>
## FND-20669: https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-rook-dfb96f0.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-rook-dfb96f0.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01538"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231257.

```text
le=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-queen-a4e5b21.mp3`,ole=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-rook-dfb96f0.mp3`,sle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/pawn-bb3aa28.mp3`,cle=`h
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-rook-dfb96f0.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20670"></a>
## FND-20670: https://assets-ds.chess.com/sounds/bughouse-voice-commands/pawn-bb3aa28.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/pawn-bb3aa28.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01539"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231342.

```text
ole=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/no-rook-dfb96f0.mp3`,sle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/pawn-bb3aa28.mp3`,cle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/queen-c990134.mp3`,lle=`
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/pawn-bb3aa28.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20671"></a>
## FND-20671: https://assets-ds.chess.com/sounds/bughouse-voice-commands/queen-c990134.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/queen-c990134.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01540"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231424.

```text
3`,sle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/pawn-bb3aa28.mp3`,cle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/queen-c990134.mp3`,lle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/rook-edd49a1.mp3`,ule=`h
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/queen-c990134.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20672"></a>
## FND-20672: https://assets-ds.chess.com/sounds/bughouse-voice-commands/rook-edd49a1.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/rook-edd49a1.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01541"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231507.

```text
`,cle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/queen-c990134.mp3`,lle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/rook-edd49a1.mp3`,ule=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/stall-2df555f.mp3`,dle=`
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/rook-edd49a1.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20673"></a>
## FND-20673: https://assets-ds.chess.com/sounds/bughouse-voice-commands/stall-2df555f.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/stall-2df555f.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01542"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231589.

```text
3`,lle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/rook-edd49a1.mp3`,ule=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/stall-2df555f.mp3`,dle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/trades-are-good-cfe316b.
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/stall-2df555f.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20674"></a>
## FND-20674: https://assets-ds.chess.com/sounds/bughouse-voice-commands/trades-are-good-cfe316b.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/trades-are-good-cfe316b.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01543"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231672.

```text
`,ule=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/stall-2df555f.mp3`,dle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/trades-are-good-cfe316b.mp3`,fle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/watch-the-clock-67f7326.
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/trades-are-good-cfe316b.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20675"></a>
## FND-20675: https://assets-ds.chess.com/sounds/bughouse-voice-commands/watch-the-clock-67f7326.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/bughouse-voice-commands/watch-the-clock-67f7326.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01544"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231765.

```text
ps://assets-ds.chess.com/sounds/bughouse-voice-commands/trades-are-good-cfe316b.mp3`,fle=`https://assets-ds.chess.com/sounds/bughouse-voice-commands/watch-the-clock-67f7326.mp3`,ple=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.m
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/bughouse-voice-commands/watch-the-clock-67f7326.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20676"></a>
## FND-20676: https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01545"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231858.

```text
ps://assets-ds.chess.com/sounds/bughouse-voice-commands/watch-the-clock-67f7326.mp3`,ple=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3`,mle=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.m
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 241809.

```text
wse,Tse,Ese,Dse,Ose,kse,Ase,jse,Ya,Xa,Za,Mse,Nse,Pse,Fse,Ise,Lse,Rse,zse,Bse=r((()=>{Goe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3`,Koe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.m
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 241809.

```text
wse,Tse,Ese,Dse,Ose,kse,Ase,jse,Ya,Xa,Za,Mse,Nse,Pse,Fse,Ise,Lse,Rse,zse,Bse=r((()=>{Goe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3`,Koe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.m
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20677"></a>
## FND-20677: https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01546"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 231950.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3`,mle=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3`,hle=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.m
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 241901.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3`,Koe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3`,qoe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.m
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 241901.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-1-8c866a0.mp3`,Koe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3`,qoe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.m
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20678"></a>
## FND-20678: https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01547"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232042.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3`,hle=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3`,gle=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.m
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 241993.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3`,qoe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3`,Joe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.m
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 241993.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-2-2a88de0.mp3`,qoe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3`,Joe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.m
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20679"></a>
## FND-20679: https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01548"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232134.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3`,gle=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3`,_le=`https://assets-ds.chess.com/sounds/game-events/game-end-f4caf6e.mp3`,vle=`https://a
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242085.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3`,Joe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3`,Yoe=`https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3`,Xo
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242085.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-3-2702709.mp3`,Joe=`https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3`,Yoe=`https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3`,Xo
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20680"></a>
## FND-20680: https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01549"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242177.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3`,Yoe=`https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3`,Xoe=`https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3`,Zoe=`https://asse
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242177.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3`,Yoe=`https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3`,Xoe=`https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3`,Zoe=`https://asse
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20681"></a>
## FND-20681: https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01550"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242263.

```text
oe=`https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3`,Xoe=`https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3`,Zoe=`https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3`,Qoe=`https:/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242263.

```text
oe=`https://assets-ds.chess.com/sounds/daily-puzzle/heartbeat-synthetic-318b903.mp3`,Xoe=`https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3`,Zoe=`https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3`,Qoe=`https:/
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20682"></a>
## FND-20682: https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01551"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242334.

```text
-318b903.mp3`,Xoe=`https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3`,Zoe=`https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3`,Qoe=`https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3`,$oe=`https
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242334.

```text
-318b903.mp3`,Xoe=`https://assets-ds.chess.com/sounds/delight/brilliant-b847134.mp3`,Zoe=`https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3`,Qoe=`https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3`,$oe=`https
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20683"></a>
## FND-20683: https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01552"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242410.

```text
134.mp3`,Zoe=`https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3`,Qoe=`https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3`,$oe=`https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3`,ese=`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242410.

```text
134.mp3`,Zoe=`https://assets-ds.chess.com/sounds/game-actions/move-self-618f465.mp3`,Qoe=`https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3`,$oe=`https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3`,ese=`https://
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20684"></a>
## FND-20684: https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01553"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242488.

```text
5.mp3`,Qoe=`https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3`,$oe=`https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3`,ese=`https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3`,tse=`htt
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242488.

```text
5.mp3`,Qoe=`https://assets-ds.chess.com/sounds/game-actions/opp-correct-2859790.mp3`,$oe=`https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3`,ese=`https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3`,tse=`htt
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20685"></a>
## FND-20685: https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01554"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242563.

```text
9790.mp3`,$oe=`https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3`,ese=`https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3`,tse=`https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3`,nse=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242563.

```text
9790.mp3`,$oe=`https://assets-ds.chess.com/sounds/game-actions/opp-fail-4fa5424.mp3`,ese=`https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3`,tse=`https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3`,nse=
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20686"></a>
## FND-20686: https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01555"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242643.

```text
mp3`,ese=`https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3`,tse=`https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3`,nse=`https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3`,Ja=`https
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242643.

```text
mp3`,ese=`https://assets-ds.chess.com/sounds/game-actions/opp-incorrect-39db01f.mp3`,tse=`https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3`,nse=`https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3`,Ja=`https
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20687"></a>
## FND-20687: https://assets-ds.chess.com/sounds/game-events/game-end-f4caf6e.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-events/game-end-f4caf6e.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01556"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232226.

```text
tps://assets-ds.chess.com/sounds/chessboard-extras/boxing-glove-punch-4-0548361.mp3`,_le=`https://assets-ds.chess.com/sounds/game-events/game-end-f4caf6e.mp3`,vle=`https://assets-ds.chess.com/sounds/game-events/game-start-fb67faa.mp3`,eo=`https://
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/game-events/game-end-f4caf6e.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20688"></a>
## FND-20688: https://assets-ds.chess.com/sounds/game-events/game-start-fb67faa.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-events/game-start-fb67faa.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01557"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232300.

```text
48361.mp3`,_le=`https://assets-ds.chess.com/sounds/game-events/game-end-f4caf6e.mp3`,vle=`https://assets-ds.chess.com/sounds/game-events/game-start-fb67faa.mp3`,eo=`https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3`,yle=`https://asse
```

**Source references:** SRC-0781  
**URL references:** <https://assets-ds.chess.com/sounds/game-events/game-start-fb67faa.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20689"></a>
## FND-20689: https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-0782"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01558"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232375.

```text
af6e.mp3`,vle=`https://assets-ds.chess.com/sounds/game-events/game-start-fb67faa.mp3`,eo=`https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3`,yle=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),x
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10576.

```text
o":`^2.7.0`},oo={name:Nle,version:Ple,description:Fle,repository:Ile

1.130.254
.mp3`,eo=`https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3`,yle=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),x
```

**Source references:** SRC-0781, SRC-0782  
**URL references:** <https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-19886, FND-20489

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20690"></a>
## FND-20690: https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01559"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242727.

```text
,tse=`https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3`,nse=`https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3`,Ja=`https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3`,rse=`https://assets-
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242727.

```text
,tse=`https://assets-ds.chess.com/sounds/game-actions/takeaway-navigate-4f46772.mp3`,nse=`https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3`,Ja=`https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3`,rse=`https://assets-
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20691"></a>
## FND-20691: https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01560"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242805.

```text
2.mp3`,nse=`https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3`,Ja=`https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3`,rse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3`,ise
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242805.

```text
2.mp3`,nse=`https://assets-ds.chess.com/sounds/puzzle-countdown/3-2-1-go-ff8b415.mp3`,Ja=`https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3`,rse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3`,ise
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20692"></a>
## FND-20692: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01561"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242874.

```text
-go-ff8b415.mp3`,Ja=`https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3`,rse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3`,ise=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3`,ase=`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242874.

```text
-go-ff8b415.mp3`,Ja=`https://assets-ds.chess.com/sounds/puzzles/correct-c1411f4.mp3`,rse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3`,ise=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3`,ase=`
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20693"></a>
## FND-20693: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01562"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242959.

```text
rse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3`,ise=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3`,ase=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3`,ose=`h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 242959.

```text
rse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-champion-b26e5a6.mp3`,ise=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3`,ase=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3`,ose=`h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20694"></a>
## FND-20694: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01563"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243042.

```text
`,ise=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3`,ase=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3`,ose=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3`,sse=`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243042.

```text
`,ise=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-legend-689451c.mp3`,ase=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3`,ose=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3`,sse=`
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20695"></a>
## FND-20695: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01564"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243124.

```text
3`,ase=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3`,ose=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3`,sse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3`,cse=`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243124.

```text
3`,ase=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l1-stone-25dd39c.mp3`,ose=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3`,sse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3`,cse=`
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20696"></a>
## FND-20696: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01565"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243207.

```text
`,ose=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3`,sse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3`,cse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3`,lse=`ht
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243207.

```text
`,ose=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/l2-silver-8cb5735.mp3`,sse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3`,cse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3`,lse=`ht
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20697"></a>
## FND-20697: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01566"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243290.

```text
`,sse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3`,cse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3`,lse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3`,use=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243290.

```text
`,sse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-bronze-77b405f.mp3`,cse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3`,lse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3`,use=
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20698"></a>
## FND-20698: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01567"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243371.

```text
p3`,cse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3`,lse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3`,use=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3`,dse=`h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243371.

```text
p3`,cse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r1-wood-c0b8a1a.mp3`,lse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3`,use=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3`,dse=`h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20699"></a>
## FND-20699: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01568"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243455.

```text
,lse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3`,use=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3`,dse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3`,fse=`h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243455.

```text
,lse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-crystal-f266499.mp3`,use=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3`,dse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3`,fse=`h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20700"></a>
## FND-20700: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01569"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243537.

```text
3`,use=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3`,dse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3`,fse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3`,pse=`ht
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243537.

```text
3`,use=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-elite-a796708.mp3`,dse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3`,fse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3`,pse=`ht
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20701"></a>
## FND-20701: https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01570"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243619.

```text
3`,dse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3`,fse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3`,pse=`https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3`,mse=`https://asse
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243619.

```text
3`,dse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-stone-15965e9.mp3`,fse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3`,pse=`https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3`,mse=`https://asse
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20702"></a>
## FND-20702: https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01571"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243700.

```text
p3`,fse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3`,pse=`https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3`,mse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3`,hse=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243700.

```text
p3`,fse=`https://assets-ds.chess.com/sounds/puzzles/easter-eggs/r2-wood-2dbbeff.mp3`,pse=`https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3`,mse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3`,hse=
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20703"></a>
## FND-20703: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01572"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243771.

```text
-2dbbeff.mp3`,pse=`https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3`,mse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3`,hse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3`,gse=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243771.

```text
-2dbbeff.mp3`,pse=`https://assets-ds.chess.com/sounds/puzzles/incorrect-0443f30.mp3`,mse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3`,hse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3`,gse=
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20704"></a>
## FND-20704: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01573"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243855.

```text
,mse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3`,hse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3`,gse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3`,_se=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243855.

```text
,mse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-1-74cfc61.mp3`,hse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3`,gse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3`,_se=
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20705"></a>
## FND-20705: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01574"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243939.

```text
,hse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3`,gse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3`,_se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 243939.

```text
,hse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-2-f74d9f9.mp3`,gse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3`,_se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3`
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20706"></a>
## FND-20706: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01575"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244023.

```text
,gse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3`,_se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3`,vse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce409
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244023.

```text
,gse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/coin-hit-3-9be5cb4.mp3`,_se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3`,vse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce409
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20707"></a>
## FND-20707: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01576"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244112.

```text
`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3`,vse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3`,yse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3`,bs
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244112.

```text
`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/daily-bonus-123-daba95a.mp3`,vse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3`,yse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3`,bs
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20708"></a>
## FND-20708: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01577"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244208.

```text
//assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3`,yse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3`,bse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3`,xse=`h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244208.

```text
//assets-ds.chess.com/sounds/puzzles/puzzle-path/disappear-pan-reappear-ce4099f.mp3`,yse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3`,bse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3`,xse=`h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20709"></a>
## FND-20709: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01578"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244294.

```text
se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3`,bse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3`,xse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244294.

```text
se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/fail-blip-hi-2b78df0.mp3`,bse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3`,xse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20710"></a>
## FND-20710: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01579"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244376.

```text
3`,bse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3`,xse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3`,Sse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3`,Cs
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244376.

```text
3`,bse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-f4ec656.mp3`,xse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3`,Sse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3`,Cs
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20711"></a>
## FND-20711: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01580"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244469.

```text
ps://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3`,Sse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3`,Cse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3`,w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244469.

```text
ps://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-land-sunglasses-ccfd423.mp3`,Sse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3`,Cse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3`,w
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20712"></a>
## FND-20712: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01581"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244555.

```text
se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3`,Cse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3`,wse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3`,
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244555.

```text
se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/hop-prestige-c7b5a3b.mp3`,Cse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3`,wse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3`,
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20713"></a>
## FND-20713: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01582"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244642.

```text
e=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3`,wse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3`,Tse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244642.

```text
e=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/land-prestige-734a27d.mp3`,wse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3`,Tse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20714"></a>
## FND-20714: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01583"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244730.

```text
=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3`,Tse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3`,Ese=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.m
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244730.

```text
=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/level-up-award-8218152.mp3`,Tse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3`,Ese=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.m
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20715"></a>
## FND-20715: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01584"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244825.

```text
://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3`,Ese=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3`,Dse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244825.

```text
://assets-ds.chess.com/sounds/puzzles/puzzle-path/long-travel-to-podium-da2e6a0.mp3`,Ese=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3`,Dse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28a
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20716"></a>
## FND-20716: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01585"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244917.

```text
tps://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3`,Dse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3`,Ose=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3`,k
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 244917.

```text
tps://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-completed-9469182.mp3`,Dse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3`,Ose=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3`,k
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20717"></a>
## FND-20717: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01586"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245015.

```text
assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3`,Ose=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3`,kse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.m
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245015.

```text
assets-ds.chess.com/sounds/puzzles/puzzle-path/prestige-screen-pulldown-28aaea8.mp3`,Ose=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3`,kse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.m
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20718"></a>
## FND-20718: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01587"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245102.

```text
e=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3`,kse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3`,Ase=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3`,jse
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245102.

```text
e=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/puzzle-solved-fee614d.mp3`,kse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3`,Ase=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3`,jse
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20719"></a>
## FND-20719: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01588"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245194.

```text
tps://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3`,Ase=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3`,jse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3`,Y
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245194.

```text
tps://assets-ds.chess.com/sounds/puzzles/puzzle-path/reward-points-coin-8a84fdd.mp3`,Ase=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3`,jse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3`,Y
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20720"></a>
## FND-20720: https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01589"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245279.

```text
Ase=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3`,jse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3`,Ya=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245279.

```text
Ase=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/screen-drop-5465aea.mp3`,jse=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3`,Ya=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20721"></a>
## FND-20721: https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01590"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245365.

```text
se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3`,Ya=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3`,Xa=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245365.

```text
se=`https://assets-ds.chess.com/sounds/puzzles/puzzle-path/tier-up-award-8f0e78e.mp3`,Ya=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3`,Xa=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20722"></a>
## FND-20722: https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01591"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245458.

```text
ps://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3`,Xa=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3`,Za=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.m
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245458.

```text
ps://assets-ds.chess.com/sounds/results-and-feedback/training-result-bad-f0b2ec2.mp3`,Xa=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3`,Za=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.m
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20723"></a>
## FND-20723: https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01592"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245552.

```text
s://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3`,Za=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3`,Mse=`https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3`,Nse=`https:/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245552.

```text
s://assets-ds.chess.com/sounds/results-and-feedback/training-result-good-1437d1d.mp3`,Za=`https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3`,Mse=`https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3`,Nse=`https:/
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20724"></a>
## FND-20724: https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01593"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245645.

```text
ps://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3`,Mse=`https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3`,Nse=`https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3`,Pse=`https://a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245645.

```text
ps://assets-ds.chess.com/sounds/results-and-feedback/training-result-ok-72ffaa5.mp3`,Mse=`https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3`,Nse=`https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3`,Pse=`https://a
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20725"></a>
## FND-20725: https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01594"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245721.

```text
aa5.mp3`,Mse=`https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3`,Nse=`https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3`,Pse=`https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3`,Fse=`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245721.

```text
aa5.mp3`,Mse=`https://assets-ds.chess.com/sounds/skills/skill-highlight-0feb65b.mp3`,Nse=`https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3`,Pse=`https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3`,Fse=`https://
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20726"></a>
## FND-20726: https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01595"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245795.

```text
eb65b.mp3`,Nse=`https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3`,Pse=`https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3`,Fse=`https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3`,Ise=`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245795.

```text
eb65b.mp3`,Nse=`https://assets-ds.chess.com/sounds/skills/skill-mastery-5235b3a.mp3`,Pse=`https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3`,Fse=`https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3`,Ise=`https://
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20727"></a>
## FND-20727: https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01596"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245870.

```text
5b3a.mp3`,Pse=`https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3`,Fse=`https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3`,Ise=`https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3`,Lse=`http
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245870.

```text
5b3a.mp3`,Pse=`https://assets-ds.chess.com/sounds/skills/skill-progress-ed0134d.mp3`,Fse=`https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3`,Ise=`https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3`,Lse=`http
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20728"></a>
## FND-20728: https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01597"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245945.

```text
134d.mp3`,Fse=`https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3`,Ise=`https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3`,Lse=`https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3`,Rse
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 245945.

```text
134d.mp3`,Fse=`https://assets-ds.chess.com/sounds/skills/skill-unlocked-92da641.mp3`,Ise=`https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3`,Lse=`https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3`,Rse
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20729"></a>
## FND-20729: https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01598"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246024.

```text
.mp3`,Ise=`https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3`,Lse=`https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3`,Rse=`https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3`,zse=`https:/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246024.

```text
.mp3`,Ise=`https://assets-ds.chess.com/sounds/special-effects/explosion-1a21832.mp3`,Lse=`https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3`,Rse=`https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3`,zse=`https:/
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20730"></a>
## FND-20730: https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01599"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246109.

```text
Lse=`https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3`,Rse=`https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3`,zse=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),V
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246109.

```text
Lse=`https://assets-ds.chess.com/sounds/timer-and-countdown/countdown-1-615a6d6.mp3`,Rse=`https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3`,zse=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),V
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20731"></a>
## FND-20731: https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-0782",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01600"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232447.

```text
-fb67faa.mp3`,eo=`https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3`,yle=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),xle,Sle,Cle,wle,Tle,Ele,Dle,Ole,kle,Ale,jle,Mle=r((()=>{xle=`@chesscom/explanation-en
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10648.

```text
130.254
.mp3`,eo=`https://assets-ds.chess.com/sounds/game-events/notify-2850486.mp3`,yle=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),xle,Sle,Cle,wle,Tle,Ele,Dle,Ole,kle,Ale,jle,Mle=r((()=>{xle=`@chesscom/explanation-en
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246185.

```text
6d6.mp3`,Rse=`https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3`,zse=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),Vse,Hse,Use,Wse,Gse,Kse,qse,Jse,Yse,Xse,Zse,Qse=r((()=>{Vse=`@chesscom/explanation-en
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246185.

```text
6d6.mp3`,Rse=`https://assets-ds.chess.com/sounds/timer-and-countdown/go-372eb70.mp3`,zse=`https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3`})),Vse,Hse,Use,Wse,Gse,Kse,qse,Jse,Yse,Xse,Zse,Qse=r((()=>{Vse=`@chesscom/explanation-en
```

**Source references:** SRC-0781, SRC-0782, SRC-1137, SRC-1165  
**URL references:** <https://assets-ds.chess.com/sounds/timer-and-countdown/tenseconds-4c5781a.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-19886, FND-20489

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.
