# url_references — findings 1601–1700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-20732"></a>
## FND-20732: https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0066",
    "SRC-0201",
    "SRC-0780",
    "SRC-1151"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01601"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 275394.

```text
XLSbIOC9TYzBeY`;function r(){let r=document.createElement(`script`);Object.assign(r,{src:`https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js`,type:`text/javascript`}),r.onerror=t,r.onload=e,document.body.appendChild(r)}function i(
```
- **SRC-0201** `research/play.js` — [preserved redacted evidence](../evidence/text/7b48978996e293cd2e02e9853ab5ba84a3684afe8a7e4c5bd40f8e89a1a85571.js)
  Character offset 76235.

```text
XLSbIOC9TYzBeY`;function r(){let r=document.createElement(`script`);Object.assign(r,{src:`https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js`,type:`text/javascript`}),r.onerror=t,r.onload=e,document.body.appendChild(r)}function i(
```
- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)
  Character offset 76613.

```text
XLSbIOC9TYzBeY`;function r(){let r=document.createElement(`script`);Object.assign(r,{src:`https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js`,type:`text/javascript`}),r.onerror=t,r.onload=e,document.body.appendChild(r)}function i(
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 275394.

```text
XLSbIOC9TYzBeY`;function r(){let r=document.createElement(`script`);Object.assign(r,{src:`https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js`,type:`text/javascript`}),r.onerror=t,r.onload=e,document.body.appendChild(r)}function i(
```

**Source references:** SRC-0066, SRC-0201, SRC-0780, SRC-1151  
**URL references:** <https://cdn.confiant-integrations.net/${n}/gpt_and_prebid/config.js>  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18139, FND-18142

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20733"></a>
## FND-20733: https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-0778",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01602"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 112019.

```text
    
        
    
  
        <script
      defer
      type="text/javascript"
      src="https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js"
      crossorigin="anonymous">
    </script>
  
  <script
    defer
    type="text/javas
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 101894.

```text
>
  
        
    
  
        <script
      defer
      type="text/javascript"
      src="https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js"
      crossorigin="anonymous">
    </script>
  
  <script
    defer
    type="text/javas
```
- **SRC-0778** `research/refinement/live-game-scripts.json` — [preserved redacted evidence](../evidence/text/f5f92fc3259c8e0c3d58eef99649e1afcd7a53d69db0782d80aae4b5f3aa4cbe.json)
  Character offset 588.

```text
.11.4/play.js",
  "/r2/client-packages/navigation/2026.11.5/navigation-logged-out.js",
  "https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js",
  "https://cdn.cookielaw.org/scripttemplates/otSDKStub.js",
  "/bundles/app/vite/ui-fra
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 112019.

```text
    
        
    
  
        <script
      defer
      type="text/javascript"
      src="https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js"
      crossorigin="anonymous">
    </script>
  
  <script
    defer
    type="text/javas
```

**Source references:** SRC-0065, SRC-0777, SRC-0778, SRC-1150  
**URL references:** <https://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20734"></a>
## FND-20734: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://cdn.cookielaw.org/scripttemplates/otSDKStub.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-0778",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01603"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 112210.

```text
gin="anonymous">
    </script>
  
  <script
    defer
    type="text/javascript"
    src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"
    charset="UTF-8"
    data-document-language="true"
    data-domain-script="018fe808-5
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 102085.

```text
gin="anonymous">
    </script>
  
  <script
    defer
    type="text/javascript"
    src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"
    charset="UTF-8"
    data-document-language="true"
    data-domain-script="018fe808-5
```
- **SRC-0778** `research/refinement/live-game-scripts.json` — [preserved redacted evidence](../evidence/text/f5f92fc3259c8e0c3d58eef99649e1afcd7a53d69db0782d80aae4b5f3aa4cbe.json)
  Character offset 679.

```text
ttps://cdn.cookielaw.org/consent/018fe808-534b-7764-9c67-c3def682a1ab/OtAutoBlock.js",
  "https://cdn.cookielaw.org/scripttemplates/otSDKStub.js",
  "/bundles/app/vite/ui-fragments.98kQRL8LIY.js"
]
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 112210.

```text
gin="anonymous">
    </script>
  
  <script
    defer
    type="text/javascript"
    src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"
    charset="UTF-8"
    data-document-language="true"
    data-domain-script="018fe808-5
```

**Source references:** SRC-0065, SRC-0777, SRC-0778, SRC-1150  
**URL references:** <https://cdn.cookielaw.org/scripttemplates/otSDKStub.js>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20735"></a>
## FND-20735: https://cdn.jsdelivr.net/npm/${i.name}@${i.version}/rive_fallback.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://cdn.jsdelivr.net/npm/${i.name}@${i.version}/rive_fallback.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01604"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3040609.

```text
ueue=[],e.wasmURL=`https://unpkg.com/${i.name}@${i.version}/rive.wasm`,e.wasmFallbackURL=`https://cdn.jsdelivr.net/npm/${i.name}@${i.version}/rive_fallback.wasm`,e.wasmBinary=null,e.errorCallbackQueue=[],e.enablePerfMarks=!1,e}()}),((e,t,n)=>{n.r(t),
```

**Source references:** SRC-0781  
**URL references:** <https://cdn.jsdelivr.net/npm/${i.name}@${i.version}/rive_fallback.wasm>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20736"></a>
## FND-20736: https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.wasm",
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
  "id": "URL-01605"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3152043.

```text
ueue=[],e.wasmURL=`https://unpkg.com/${o.name}@${o.version}/rive.wasm`,e.wasmFallbackURL=`https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.wasm`,e.wasmBinary=null,e.wasmThreadsURL=typeof a()==`function`?`https://unpkg.com/${o.name}@$
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3152043.

```text
ueue=[],e.wasmURL=`https://unpkg.com/${o.name}@${o.version}/rive.wasm`,e.wasmFallbackURL=`https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.wasm`,e.wasmBinary=null,e.wasmThreadsURL=typeof a()==`function`?`https://unpkg.com/${o.name}@$
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.wasm>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20737"></a>
## FND-20737: https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback",
  "type": "api_or_websocket_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-0778",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01606"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 90164.

```text
pe="module" src="/bundles/app/vite/turnstile.CBslv1dJqM.js" defer></script>

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback" crossorigin async defer></script>

          
<script type="text/javascript">
    docume
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 89521.

```text
pe="module" src="/bundles/app/vite/turnstile.Bt-bkXiSFU.js" defer></script>

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback" crossorigin async defer></script>


        <script>(()=>{var a=(e=>(e.CPRA="usca",e.CCP
```
- **SRC-0778** `research/refinement/live-game-scripts.json` — [preserved redacted evidence](../evidence/text/f5f92fc3259c8e0c3d58eef99649e1afcd7a53d69db0782d80aae4b5f3aa4cbe.json)
  Character offset 278.

```text
bundles/app/vite/sentry.sGzKJdPHz-.js",
  "/bundles/app/vite/turnstile.Bt-bkXiSFU.js",
  "https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback",
  "/bundles/app/vite/chessboard-layout.CKkjF8P48L.js",
  "/bundles/app/vite/comments.Dm
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 90164.

```text
pe="module" src="/bundles/app/vite/turnstile.CBslv1dJqM.js" defer></script>

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback" crossorigin async defer></script>

          
<script type="text/javascript">
    docume
```

**Source references:** SRC-0065, SRC-0777, SRC-0778, SRC-1150  
**URL references:** <https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20738"></a>
## FND-20738: https://checkoutshopper-live.cdn.adyen.com/checkoutshopper/sdk/6.48.0/adyen.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://checkoutshopper-live.cdn.adyen.com/checkoutshopper/sdk/6.48.0/adyen.js",
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
  "id": "URL-01607"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 83486.

```text
80210853.aHR0cHM6Ly93d3cuY2hlc3MuY29t.g3hcnpsxbNsbEo3XJP_laQJwLDCkoYfA1YmHG6Kns8g","sdk":"https:\/\/checkoutshopper-live.cdn.adyen.com\/checkoutshopper\/sdk\/6.48.0\/adyen.js","integrity":"sha384-58vuSmL0mIz82u9RSqte3f\/NTu5nSZLUSXcFHtF+mp47Hd4FNn3d0clzGVj9aS8x"},
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 82712.

```text
80210853.aHR0cHM6Ly93d3cuY2hlc3MuY29t.g3hcnpsxbNsbEo3XJP_laQJwLDCkoYfA1YmHG6Kns8g","sdk":"https:\/\/checkoutshopper-live.cdn.adyen.com\/checkoutshopper\/sdk\/6.48.0\/adyen.js","integrity":"sha384-58vuSmL0mIz82u9RSqte3f\/NTu5nSZLUSXcFHtF+mp47Hd4FNn3d0clzGVj9aS8x"},
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 83486.

```text
80210853.aHR0cHM6Ly93d3cuY2hlc3MuY29t.g3hcnpsxbNsbEo3XJP_laQJwLDCkoYfA1YmHG6Kns8g","sdk":"https:\/\/checkoutshopper-live.cdn.adyen.com\/checkoutshopper\/sdk\/6.48.0\/adyen.js","integrity":"sha384-58vuSmL0mIz82u9RSqte3f\/NTu5nSZLUSXcFHtF+mp47Hd4FNn3d0clzGVj9aS8x"},
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://checkoutshopper-live.cdn.adyen.com/checkoutshopper/sdk/6.48.0/adyen.js>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20739"></a>
## FND-20739: https://chesscom.slack.com/archives/CP1C1D5TP

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://chesscom.slack.com/archives/CP1C1D5TP",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01608"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344826.

```text
,registryUrl:`https://github.com/ChessCom/client-packages/pkgs/npm/play-client`,slackUrl:`https://chesscom.slack.com/archives/CP1C1D5TP`,owners:[`@yneves`],pagesUsedOn:[`/play/arena/*`,`/play/tournament/*`,`/play/match/*`,`/p
```

**Source references:** SRC-0781  
**URL references:** <https://chesscom.slack.com/archives/CP1C1D5TP>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20740"></a>
## FND-20740: https://client-metrics-cf.chess.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://client-metrics-cf.chess.com",
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
  "id": "URL-01609"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 75853.

```text
      window.chesscom = window.chesscom || {};
    window.chesscom.clientMetricsDomain = 'https://client-metrics-cf.chess.com';

        window.chesscom.showAds = Boolean();
  </script>
  <script type="text/javascri
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 106306.

```text
ions = { canCreatePublicCollections: false };

    window.chesscom.clientMetricsDomain = 'https://client-metrics-cf.chess.com';
    window.chesscom.openings = ["Alapin Sicilian Variation","Alekhine","Benko Gambit","
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 75106.

```text
      window.chesscom = window.chesscom || {};
    window.chesscom.clientMetricsDomain = 'https://client-metrics-cf.chess.com';

        window.chesscom.showAds = Boolean(1);
  </script>
  <script type="text/javascr
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 100009.

```text
D\u007D')
    );
  </script>


<script>
      
    window.chesscom.clientMetricsDomain = 'https://client-metrics-cf.chess.com';
    window.chesscom.playMetricsUrl = 'https://client-metrics-cf.chess.com/play';
    wi
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 75853.

```text
      window.chesscom = window.chesscom || {};
    window.chesscom.clientMetricsDomain = 'https://client-metrics-cf.chess.com';

        window.chesscom.showAds = Boolean();
  </script>
  <script type="text/javascri
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 106306.

```text
ions = { canCreatePublicCollections: false };

    window.chesscom.clientMetricsDomain = 'https://client-metrics-cf.chess.com';
    window.chesscom.openings = ["Alapin Sicilian Variation","Alekhine","Benko Gambit","
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://client-metrics-cf.chess.com>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20741"></a>
## FND-20741: https://client-metrics-cf.chess.com/play

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://client-metrics-cf.chess.com/play",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01610"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 100085.

```text
ricsDomain = 'https://client-metrics-cf.chess.com';
    window.chesscom.playMetricsUrl = 'https://client-metrics-cf.chess.com/play';
    window.chesscom.playMetricsCheckRequiredGamesUrl = 'https://client-metrics-cf.chess
```

**Source references:** SRC-0777  
**URL references:** <https://client-metrics-cf.chess.com/play>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20742"></a>
## FND-20742: https://client-metrics-cf.chess.com/play/check-required-games

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://client-metrics-cf.chess.com/play/check-required-games",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01611"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 100184.

```text
lient-metrics-cf.chess.com/play';
    window.chesscom.playMetricsCheckRequiredGamesUrl = 'https://client-metrics-cf.chess.com/play/check-required-games';
  </script>

  <script>
    window.chesscom.showAds = Boolean(1);
    window.chesscom.s
```

**Source references:** SRC-0777  
**URL references:** <https://client-metrics-cf.chess.com/play/check-required-games>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20743"></a>
## FND-20743: https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0066",
    "SRC-0201",
    "SRC-0780",
    "SRC-1151"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01612"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 276148.

```text
mise:()=>new Promise((e,t)=>{let n=document.createElement(`script`);Object.assign(n,{src:`https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js`,async:!0,type:`text/javascript`}),n.onerror=t,n.onload=e,document.body.appendChild(n)})}
```
- **SRC-0201** `research/play.js` — [preserved redacted evidence](../evidence/text/7b48978996e293cd2e02e9853ab5ba84a3684afe8a7e4c5bd40f8e89a1a85571.js)
  Character offset 76989.

```text
mise:()=>new Promise((e,t)=>{let n=document.createElement(`script`);Object.assign(n,{src:`https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js`,async:!0,type:`text/javascript`}),n.onerror=t,n.onload=e,document.body.appendChild(n)})}
```
- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)
  Character offset 77367.

```text
mise:()=>new Promise((e,t)=>{let n=document.createElement(`script`);Object.assign(n,{src:`https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js`,async:!0,type:`text/javascript`}),n.onerror=t,n.onload=e,document.body.appendChild(n)})}
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 276148.

```text
mise:()=>new Promise((e,t)=>{let n=document.createElement(`script`);Object.assign(n,{src:`https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js`,async:!0,type:`text/javascript`}),n.onerror=t,n.onload=e,document.body.appendChild(n)})}
```

**Source references:** SRC-0066, SRC-0201, SRC-0780, SRC-1151  
**URL references:** <https://dn0qt3r0xannq.cloudfront.net/chess-RXC9HVsKRD/chess-default/prebid-load.js>  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18139, FND-18142

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20744"></a>
## FND-20744: https://empty.invalid

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://empty.invalid",
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
  "id": "URL-01613"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 508065.

```text
=`function`,r=typeof globalThis.Request==`function`;if(n&&r)try{t=new globalThis.Request(`https://empty.invalid`,{body:new globalThis.ReadableStream,method:`POST`,get duplex(){return e=!0,`half`}}).hea
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1341779.

```text
=`function`,r=typeof globalThis.Request==`function`;if(n&&r)try{t=new globalThis.Request(`https://empty.invalid`,{body:new globalThis.ReadableStream,method:`POST`,get duplex(){return e=!0,`half`}}).hea
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1341779.

```text
=`function`,r=typeof globalThis.Request==`function`;if(n&&r)try{t=new globalThis.Request(`https://empty.invalid`,{body:new globalThis.ReadableStream,method:`POST`,get duplex(){return e=!0,`half`}}).hea
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://empty.invalid>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20745"></a>
## FND-20745: https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0036",
    "SRC-1138",
    "SRC-1140",
    "SRC-1141",
    "SRC-1146",
    "SRC-1166",
    "SRC-1168",
    "SRC-1169",
    "SRC-1173"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01614"
}

### Evidence

- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 1657.

```text
1)},i.print=i.printErr=function(e){if("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"!==e){if(0===W.length)return console.log(e);for(var t of W)t(e)}},i.terminate=function(){
```
- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 12856.

```text
lue "+e}function Ie(){s||o||(J=J||{})["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 13000.

```text
king-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,l("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 13144.

```text
king-on-the-main-browser-thread"]=1,l("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"))}i.establishStackSpace=function(e,t){Nt(e,t),qt(e)},i.invokeEntryPoint=function(e,t){re
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 1657.

```text
1)},i.print=i.printErr=function(e){if("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"!==e){if(0===W.length)return console.log(e);for(var t of W)t(e)}},i.terminate=function(){
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 12856.

```text
lue "+e}function Ie(){s||o||(J=J||{})["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 13000.

```text
king-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,l("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 13144.

```text
king-on-the-main-browser-thread"]=1,l("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"))}i.establishStackSpace=function(e,t){Nt(e,t),qt(e)},i.invokeEntryPoint=function(e,t){re
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 12504.

```text
lue "+e}function Te(){s||o||(J=J||{})["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 12648.

```text
king-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,d("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 12792.

```text
king-on-the-main-browser-thread"]=1,d("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"))}i.establishStackSpace=function(e,t){Wt(e,t),Bt(e)},i.invokeEntryPoint=function(e,t){re
```
- **SRC-1141** `research/stockfish.js` — [preserved redacted evidence](../evidence/text/2a9661e708b82108c4f17405a8a29093c99bebf5b50ace7fb0d244a22bedb8ec.js)
  Character offset 30409.

```text
ENVIRONMENT_IS_WORKER)return;warnOnce("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread")}function _emscripten_conditional_set_current_thread_status(expectedStatus,newStatus){ex
```
- **SRC-1146** `research/torch-lite.js` — [preserved redacted evidence](../evidence/text/baaed8e88d4c05d47de70808692ad41ae1e4b6d3bdc5b8274d6b49ec83c333b4.js)
  Character offset 12783.

```text
a}function db(){x||u||(la||(la={}),la["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(la["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/po
```
- **SRC-1146** `research/torch-lite.js` — [preserved redacted evidence](../evidence/text/baaed8e88d4c05d47de70808692ad41ae1e4b6d3bdc5b8274d6b49ec83c333b4.js)
  Character offset 12928.

```text
ing-on-the-main-browser-thread"]||(la["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,H("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1146** `research/torch-lite.js` — [preserved redacted evidence](../evidence/text/baaed8e88d4c05d47de70808692ad41ae1e4b6d3bdc5b8274d6b49ec83c333b4.js)
  Character offset 13072.

```text
king-on-the-main-browser-thread"]=1,H("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread")))}function eb(a,b){if(!a)return H("pthread_join attempted on a null thread pointer!"),7
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 1657.

```text
1)},i.print=i.printErr=function(e){if("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"!==e){if(0===W.length)return console.log(e);for(var t of W)t(e)}},i.terminate=function(){
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 12856.

```text
lue "+e}function Ie(){s||o||(J=J||{})["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 13000.

```text
king-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,l("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 13144.

```text
king-on-the-main-browser-thread"]=1,l("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"))}i.establishStackSpace=function(e,t){Nt(e,t),qt(e)},i.invokeEntryPoint=function(e,t){re
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 12504.

```text
lue "+e}function Te(){s||o||(J=J||{})["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 12648.

```text
king-on-the-main-browser-thread"]||(J["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,d("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 12792.

```text
king-on-the-main-browser-thread"]=1,d("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"))}i.establishStackSpace=function(e,t){Wt(e,t),Bt(e)},i.invokeEntryPoint=function(e,t){re
```
- **SRC-1169** `research.zip!/research/stockfish.js` — [preserved redacted evidence](../evidence/text/2a9661e708b82108c4f17405a8a29093c99bebf5b50ace7fb0d244a22bedb8ec.js)
  Character offset 30409.

```text
ENVIRONMENT_IS_WORKER)return;warnOnce("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread")}function _emscripten_conditional_set_current_thread_status(expectedStatus,newStatus){ex
```
- **SRC-1173** `research.zip!/research/torch-lite.js` — [preserved redacted evidence](../evidence/text/baaed8e88d4c05d47de70808692ad41ae1e4b6d3bdc5b8274d6b49ec83c333b4.js)
  Character offset 12783.

```text
a}function db(){x||u||(la||(la={}),la["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]||(la["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/po
```
- **SRC-1173** `research.zip!/research/torch-lite.js` — [preserved redacted evidence](../evidence/text/baaed8e88d4c05d47de70808692ad41ae1e4b6d3bdc5b8274d6b49ec83c333b4.js)
  Character offset 12928.

```text
ing-on-the-main-browser-thread"]||(la["Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread"]=1,H("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/por
```
- **SRC-1173** `research.zip!/research/torch-lite.js` — [preserved redacted evidence](../evidence/text/baaed8e88d4c05d47de70808692ad41ae1e4b6d3bdc5b8274d6b49ec83c333b4.js)
  Character offset 13072.

```text
king-on-the-main-browser-thread"]=1,H("Blocking on the main thread is very dangerous, see https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread")))}function eb(a,b){if(!a)return H("pthread_join attempted on a null thread pointer!"),7
```

**Source references:** SRC-0036, SRC-1138, SRC-1140, SRC-1141, SRC-1146, SRC-1166, SRC-1168, SRC-1169, SRC-1173  
**URL references:** <https://emscripten.org/docs/porting/pthreads.html#blocking-on-the-main-browser-thread>  
**Related findings:** FND-19887, FND-20179

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20746"></a>
## FND-20746: https://en.wikipedia.org/wiki/Chess.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://en.wikipedia.org/wiki/Chess.com",
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
  "id": "URL-01615"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11699.

```text
     "https://www.tiktok.com/@chess",
          "https://www.twitch.tv/chess",
          "https://en.wikipedia.org/wiki/Chess.com",
          "https://www.wikidata.org/wiki/Q16829376",
          "https://www.crunchbase.
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6663.

```text
     "https://www.tiktok.com/@chess",
          "https://www.twitch.tv/chess",
          "https://en.wikipedia.org/wiki/Chess.com",
          "https://www.wikidata.org/wiki/Q16829376",
          "https://www.crunchbase.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11699.

```text
     "https://www.tiktok.com/@chess",
          "https://www.twitch.tv/chess",
          "https://en.wikipedia.org/wiki/Chess.com",
          "https://www.wikidata.org/wiki/Q16829376",
          "https://www.crunchbase.
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://en.wikipedia.org/wiki/Chess.com>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20747"></a>
## FND-20747: https://github.com/ChessCom/chess/blob/develop/client/web/play/release-history.md

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/ChessCom/chess/blob/develop/client/web/play/release-history.md",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01616"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344628.

```text
rceCodeUrl:`https://github.com/ChessCom/chess/tree/develop/client/web/play`,changelogUrl:`https://github.com/ChessCom/chess/blob/develop/client/web/play/release-history.md`,description:`Play client`,registryUrl:`https://github.com/ChessCom/client-packages/pkgs/
```

**Source references:** SRC-0781  
**URL references:** <https://github.com/ChessCom/chess/blob/develop/client/web/play/release-history.md>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20748"></a>
## FND-20748: https://github.com/ChessCom/chess/tree/develop/client/web/play

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/ChessCom/chess/tree/develop/client/web/play",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01617"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344550.

```text
com/play/online`}],featureFlags:[{name:`client_play_beta`,channel:`beta`}],sourceCodeUrl:`https://github.com/ChessCom/chess/tree/develop/client/web/play`,changelogUrl:`https://github.com/ChessCom/chess/blob/develop/client/web/play/release-his
```

**Source references:** SRC-0781  
**URL references:** <https://github.com/ChessCom/chess/tree/develop/client/web/play>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20749"></a>
## FND-20749: https://github.com/ChessCom/client-packages/pkgs/npm/play-client

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/ChessCom/client-packages/pkgs/npm/play-client",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01618"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344750.

```text
s/blob/develop/client/web/play/release-history.md`,description:`Play client`,registryUrl:`https://github.com/ChessCom/client-packages/pkgs/npm/play-client`,slackUrl:`https://chesscom.slack.com/archives/CP1C1D5TP`,owners:[`@yneves`],pagesUsedOn:
```

**Source references:** SRC-0781  
**URL references:** <https://github.com/ChessCom/client-packages/pkgs/npm/play-client>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20750"></a>
## FND-20750: https://github.com/ChessCom/explanation-engine#readme

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/ChessCom/explanation-engine#readme",
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
  "id": "URL-01619"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232826.

```text
/client-packages.git`},Tle={registry:`https://npm.pkg.github.com/`},Ele=`UNLICENSED`,Dle=`https://github.com/ChessCom/explanation-engine#readme`,Ole=[`explanation-engine.js`,`explanation-engine.wasm`],kle={protoc:`./third_party/proto
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 233610.

```text
om/client-packages.git`},Lle={registry:`https://npm.pkg.github.com/`},to=`UNLICENSED`,no=`https://github.com/ChessCom/explanation-engine#readme`,ro=[`explanation-engine.js`,`explanation-engine.wasm`],io={protoc:`./third_party/protobu
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10153.

```text
om/client-packages.git`},Lle={registry:`https://npm.pkg.github.com/`},to=`UNLICENSED`,no=`https://github.com/ChessCom/explanation-engine#readme`,ro=[`explanation-engine.js`,`explanation-engine.wasm`],io={protoc:`./third_party/protobu
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 11027.

```text
/client-packages.git`},Tle={registry:`https://npm.pkg.github.com/`},Ele=`UNLICENSED`,Dle=`https://github.com/ChessCom/explanation-engine#readme`,Ole=[`explanation-engine.js`,`explanation-engine.wasm`],kle={protoc:`./third_party/proto
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246564.

```text
/client-packages.git`},Gse={registry:`https://npm.pkg.github.com/`},Kse=`UNLICENSED`,qse=`https://github.com/ChessCom/explanation-engine#readme`,Jse=[`explanation-engine.js`,`explanation-engine.wasm`],Yse={protoc:`./third_party/proto
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 247356.

```text
/client-packages.git`},rce={registry:`https://npm.pkg.github.com/`},ice=`UNLICENSED`,ace=`https://github.com/ChessCom/explanation-engine#readme`,oce=[`explanation-engine.js`,`explanation-engine.wasm`],sce={protoc:`./third_party/proto
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246564.

```text
/client-packages.git`},Gse={registry:`https://npm.pkg.github.com/`},Kse=`UNLICENSED`,qse=`https://github.com/ChessCom/explanation-engine#readme`,Jse=[`explanation-engine.js`,`explanation-engine.wasm`],Yse={protoc:`./third_party/proto
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 247356.

```text
/client-packages.git`},rce={registry:`https://npm.pkg.github.com/`},ice=`UNLICENSED`,ace=`https://github.com/ChessCom/explanation-engine#readme`,oce=[`explanation-engine.js`,`explanation-engine.wasm`],sce={protoc:`./third_party/proto
```

**Source references:** SRC-0781, SRC-0782, SRC-1137, SRC-1165  
**URL references:** <https://github.com/ChessCom/explanation-engine#readme>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-19886, FND-20489

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20751"></a>
## FND-20751: https://github.com/glinscott/nnue-pytorch

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/glinscott/nnue-pytorch",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0035"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01620"
}

### Evidence

- **SRC-0035** `extension/engines/stockfish/nn-5af11540bbfe.nnue` — [preserved redacted evidence](../evidence/binary-strings/5af11540bbfefcb54e38c5dd000cab4b469dfa7599a1d55be5d2722c20a8929b.txt)
  Character offset 25.

```text
Network trained with the https://github.com/glinscott/nnue-pytorch trainer.
d#wg#D.h
,x_^j`".h
\yy.\t.h
x1zJ"d.h
.9><i5P.h
ZBI+S|.h
Lz&~{t.h
/8><i4P.h
```

**Source references:** SRC-0035  
**URL references:** <https://github.com/glinscott/nnue-pytorch>  
**Related findings:** None assigned

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20752"></a>
## FND-20752: https://github.com/hi-ogawa/Stockfish

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/hi-ogawa/Stockfish",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0036",
    "SRC-0038",
    "SRC-1138",
    "SRC-1139",
    "SRC-1140",
    "SRC-1166",
    "SRC-1167",
    "SRC-1168"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01621"
}

### Evidence

- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 279.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-0038** `extension/engines/stockfish/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 282.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 279.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-1139** `research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 282.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 279.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 279.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-1167** `research.zip!/research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 282.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 279.

```text

 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other co
```

**Source references:** SRC-0036, SRC-0038, SRC-1138, SRC-1139, SRC-1140, SRC-1166, SRC-1167, SRC-1168  
**URL references:** <https://github.com/hi-ogawa/Stockfish>  
**Related findings:** FND-19887, FND-20179, FND-20745

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20753"></a>
## FND-20753: https://github.com/llvm/llvm-project

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/llvm/llvm-project",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0037",
    "SRC-0039"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01622"
}

### Evidence

- **SRC-0037** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.wasm` — [preserved redacted evidence](../evidence/binary-strings/064234cfc56dc28a18ced0b35630bc8f2dc1a7c689073fb1e2b78ede7c2a6b35.txt)
  Character offset 152.

```text
tion name UCI_Chess960 value false
UCI_AnalyseMode
UCI_ShowWDL
UCI_Chess960
Clang 13.0.0 (https://github.com/llvm/llvm-project 31e75512174e1bdaa242ee5c7f30fe56e68c3748)
the Universal Chess Interface (UCI) protocol to
```
- **SRC-0039** `extension/engines/stockfish/stockfish-nnue-16-single.wasm` — [preserved redacted evidence](../evidence/binary-strings/198c952007aa12b24aa649525f049f9508178fbfd5a3298810d7e87d91229a04.txt)
  Character offset 152.

```text
tion name UCI_Chess960 value false
UCI_AnalyseMode
UCI_ShowWDL
UCI_Chess960
Clang 14.0.0 (https://github.com/llvm/llvm-project 78e87970af888bbbd5652c31f3a8454e8e9dd5b8)
```

**Source references:** SRC-0037, SRC-0039  
**URL references:** <https://github.com/llvm/llvm-project>  
**Related findings:** FND-20757

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20754"></a>
## FND-20754: https://github.com/niklasf/stockfish.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/niklasf/stockfish.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0036",
    "SRC-0038",
    "SRC-1138",
    "SRC-1139",
    "SRC-1140",
    "SRC-1166",
    "SRC-1167",
    "SRC-1168"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01623"
}

### Evidence

- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 234.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-0038** `extension/engines/stockfish/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 237.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 234.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-1139** `research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 237.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 234.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 234.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-1167** `research.zip!/research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 237.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 234.

```text
klas Fiekas <[REDACTED_EMAIL]>
 * Hiroshi Ogawa <[REDACTED_EMAIL]>
 * https://github.com/niklasf/stockfish.wasm
 * https://github.com/hi-ogawa/Stockfish
 *
 * Based on Stockfish (c) T. Romstad, M. Cost
```

**Source references:** SRC-0036, SRC-0038, SRC-1138, SRC-1139, SRC-1140, SRC-1166, SRC-1167, SRC-1168  
**URL references:** <https://github.com/niklasf/stockfish.wasm>  
**Related findings:** FND-19887, FND-20179, FND-20745, FND-20752

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20755"></a>
## FND-20755: https://github.com/nmrugg/stockfish.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/nmrugg/stockfish.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0036",
    "SRC-0038",
    "SRC-1138",
    "SRC-1139",
    "SRC-1140",
    "SRC-1166",
    "SRC-1167",
    "SRC-1168"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01624"
}

### Evidence

- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 48.

```text
/*!
 * Stockfish.js (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-0038** `extension/engines/stockfish/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 51.

```text
/*!
 * Stockfish.js 16 (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 48.

```text
/*!
 * Stockfish.js (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-1139** `research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 51.

```text
/*!
 * Stockfish.js 16 (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 48.

```text
/*!
 * Stockfish.js (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 48.

```text
/*!
 * Stockfish.js (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-1167** `research.zip!/research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 51.

```text
/*!
 * Stockfish.js 16 (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 48.

```text
/*!
 * Stockfish.js (c) 2023, Chess.com, LLC
 * https://github.com/nmrugg/stockfish.js
 * License: GPLv3
 *
 * Based on stockfish.wasm (c)
 * Niklas Fiekas <niklas.fiekas@backs
```

**Source references:** SRC-0036, SRC-0038, SRC-1138, SRC-1139, SRC-1140, SRC-1166, SRC-1167, SRC-1168  
**URL references:** <https://github.com/nmrugg/stockfish.js>  
**Related findings:** FND-19887, FND-20179, FND-20745, FND-20752

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20756"></a>
## FND-20756: https://github.com/official-stockfish/Stockfish

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/official-stockfish/Stockfish",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0036",
    "SRC-0038",
    "SRC-1138",
    "SRC-1139",
    "SRC-1140",
    "SRC-1166",
    "SRC-1167",
    "SRC-1168"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01625"
}

### Evidence

- **SRC-0036** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 421.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var $t,e,n,t,r,a;function i(){function e(S){var i,k,T,t,n;S=S||{},(i=i||(v
```
- **SRC-0038** `extension/engines/stockfish/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 424.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(vo
```
- **SRC-1138** `research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 421.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var $t,e,n,t,r,a;function i(){function e(S){var i,k,T,t,n;S=S||{},(i=i||(v
```
- **SRC-1139** `research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 424.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(vo
```
- **SRC-1140** `research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 421.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var e,n,t,r,a;function i(){function e(e){var i,S,k,T,B;e=e||{},(i=i||(void
```
- **SRC-1166** `research.zip!/research/stockfish-nnue-16-no-Worker.js` — [preserved redacted evidence](../evidence/text/b2cacb67453e6be099d6e76e717b40e8d8e8b93716ec8320011c14fda62fd317.js)
  Character offset 421.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var $t,e,n,t,r,a;function i(){function e(S){var i,k,T,t,n;S=S||{},(i=i||(v
```
- **SRC-1167** `research.zip!/research/stockfish-nnue-16-single.js` — [preserved redacted evidence](../evidence/text/b49d13f972f148f6797d968fcfc31462cb775deb2580be74f285b8fc9a8b27ef.js)
  Character offset 424.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var t,n,r,e,o,a;function i(){function e(e){var i,D,I,n,t;e=e||{},(i=i||(vo
```
- **SRC-1168** `research.zip!/research/stockfish-nnue-16.js` — [preserved redacted evidence](../evidence/text/65d4cd6f066439236eb1153f545c867aeb6a9346bc6d0693d6b643fedba134f2.js)
  Character offset 421.

```text
 Stockfish (c) T. Romstad, M. Costalba, J. Kiiski, G. Linscott and other contributors.
 * https://github.com/official-stockfish/Stockfish
 */!function(){var e,n,t,r,a;function i(){function e(e){var i,S,k,T,B;e=e||{},(i=i||(void
```

**Source references:** SRC-0036, SRC-0038, SRC-1138, SRC-1139, SRC-1140, SRC-1166, SRC-1167, SRC-1168  
**URL references:** <https://github.com/official-stockfish/Stockfish>  
**Related findings:** FND-19887, FND-20179, FND-20745, FND-20752

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20757"></a>
## FND-20757: https://github.com/official-stockfish/Stockfish#readme

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/official-stockfish/Stockfish#readme",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0037"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01626"
}

### Evidence

- **SRC-0037** `extension/engines/stockfish/stockfish-nnue-16-no-Worker.wasm` — [preserved redacted evidence](../evidence/binary-strings/064234cfc56dc28a18ced0b35630bc8f2dc1a7c689073fb1e2b78ede7c2a6b35.txt)
  Character offset 351.

```text
(UCI) protocol to communicate with a GUI, an API, etc.
For any further information, visit https://github.com/official-stockfish/Stockfish#readme
```

**Source references:** SRC-0037  
**URL references:** <https://github.com/official-stockfish/Stockfish#readme>  
**Related findings:** FND-20753

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20758"></a>
## FND-20758: https://github.com/rive-app/rive-wasm/tree/master/js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/rive-app/rive-wasm/tree/master/js",
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
  "id": "URL-01627"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3112812.

```text
eb api.","main":"rive.js","homepage":"https://rive.app","repository":{"type":"git","url":"https://github.com/rive-app/rive-wasm/tree/master/js"},"keywords":["rive","animation"],"author":"Rive","contributors":["Luigi Rosso <luigi@riv
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323381.

```text
eb api.","main":"rive.js","homepage":"https://rive.app","repository":{"type":"git","url":"https://github.com/rive-app/rive-wasm/tree/master/js"},"keywords":["rive","animation"],"author":"Rive","contributors":["Luigi Rosso <luigi@riv
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323381.

```text
eb api.","main":"rive.js","homepage":"https://rive.app","repository":{"type":"git","url":"https://github.com/rive-app/rive-wasm/tree/master/js"},"keywords":["rive","animation"],"author":"Rive","contributors":["Luigi Rosso <luigi@riv
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://github.com/rive-app/rive-wasm/tree/master/js>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20759"></a>
## FND-20759: https://github.com/sindresorhus/ky#baseurl

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/sindresorhus/ky#baseurl",
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
  "id": "URL-01628"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 522995.

```text
 See also the new `baseUrl` option for improved flexibility with standard URL resolution: https://github.com/sindresorhus/ky#baseurl",Uv=Symbol(`timedOutResponseData`),uTe=e=>{let t=/;\s*charset\s*=\s*(?:"([^"]+)"|([^;,\s]
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1356746.

```text
 See also the new `baseUrl` option for improved flexibility with standard URL resolution: https://github.com/sindresorhus/ky#baseurl",dI=Symbol(`timedOutResponseData`),fI=e=>{let t=/;\s*charset\s*=\s*(?:"([^"]+)"|([^;,\s]+
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1356746.

```text
 See also the new `baseUrl` option for improved flexibility with standard URL resolution: https://github.com/sindresorhus/ky#baseurl",dI=Symbol(`timedOutResponseData`),fI=e=>{let t=/;\s*charset\s*=\s*(?:"([^"]+)"|([^;,\s]+
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://github.com/sindresorhus/ky#baseurl>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20760"></a>
## FND-20760: https://github.com/uuidjs/uuid#getrandomvalues-not-supported

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/uuidjs/uuid#getrandomvalues-not-supported",
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
  "id": "URL-01629"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 543347.

```text
etRandomValues.bind(crypto),!Cy))throw Error(`crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported`);return Cy(wEe)}var Cy,wEe,TEe=r((()=>{wEe=new Uint8Array(16)}));function EEe(e){return 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1680307.

```text
etRandomValues.bind(crypto),!MH))throw Error(`crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported`);return MH(qGe)}var MH,qGe,JGe=r((()=>{qGe=new Uint8Array(16)}));function YGe(e,t=0){ret
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1680307.

```text
etRandomValues.bind(crypto),!MH))throw Error(`crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported`);return MH(qGe)}var MH,qGe,JGe=r((()=>{qGe=new Uint8Array(16)}));function YGe(e,t=0){ret
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://github.com/uuidjs/uuid#getrandomvalues-not-supported>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20761"></a>
## FND-20761: https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat",
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
  "id": "URL-01630"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 74816.

```text
essageFormat" is required to use ICU MessageFormat but it has not been found. Please read https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat`);return new e.IntlMessageFormat(o,void 0,void 0,{ignoreTag:!0}).format(n||{})}return l(o
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 74816.

```text
essageFormat" is required to use ICU MessageFormat but it has not been found. Please read https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat`);return new e.IntlMessageFormat(o,void 0,void 0,{ignoreTag:!0}).format(n||{})}return l(o
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 387472.

```text
essageFormat" is required to use ICU MessageFormat but it has not been found. Please read https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat`);return new e.IntlMessageFormat(o,void 0,void 0,{ignoreTag:!0}).format(n||{})}return l(o
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 376629.

```text
essageFormat" is required to use ICU MessageFormat but it has not been found. Please read https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat`);return new e.IntlMessageFormat(o,void 0,void 0,{ignoreTag:!0}).format(n||{})}return l(o
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 376629.

```text
essageFormat" is required to use ICU MessageFormat but it has not been found. Please read https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat`);return new e.IntlMessageFormat(o,void 0,void 0,{ignoreTag:!0}).format(n||{})}return l(o
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://github.com/willdurand/BazingaJsTranslationBundle/blob/master/Resources/doc/index.md#using-icu-messageformat>  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20762"></a>
## FND-20762: https://images.chesscomfiles.com/chess-themes/boards/green/150.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/boards/green/150.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01631"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 64363.

```text
 visibility: hidden;
                background: var(--theme-board-style-image, url(&quot;https://images.chesscomfiles.com/chess-themes/boards/green/150.png&quot;)) 0 0 / cover no-repeat;
                ">
    <div
            style="
                  
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/boards/green/150.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20763"></a>
## FND-20763: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01632"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65061.

```text
n.png&quot;)) 14.29% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bb, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png&quot;)) 28.57% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bq, url(&quot;https://image
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65517.

```text
k.png&quot;)) 57.14% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bb, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png&quot;)) 71.43% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bn, url(&quot;https://image
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bb.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20764"></a>
## FND-20764: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01633"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65365.

```text
q.png&quot;)) 42.86% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bk, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png&quot;)) 57.14% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bb, url(&quot;https://image
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bk.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20765"></a>
## FND-20765: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01634"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 64909.

```text
150/br.png&quot;)) 0 0 / 12.5% no-repeat,
            var(--theme-piece-set-bn, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png&quot;)) 14.29% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bb, url(&quot;https://image
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65669.

```text
b.png&quot;)) 71.43% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bn, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png&quot;)) 85.71% 0 / 12.5% no-repeat,
            var(--theme-piece-set-br, url(&quot;https://image
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bn.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20766"></a>
## FND-20766: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01635"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65972.

```text
br.png&quot;)) 100% 0 / 12.5% no-repeat,

            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 0 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://image
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 66124.

```text
p.png&quot;)) 0 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 14.29% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 66281.

```text
&quot;)) 14.29% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 28.57% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 66438.

```text
&quot;)) 28.57% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 42.86% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 66595.

```text
&quot;)) 42.86% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 57.14% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 66752.

```text
&quot;)) 57.14% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 71.43% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 66909.

```text
&quot;)) 71.43% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 85.71% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67066.

```text
&quot;)) 85.71% 14.29% / 12.5% no-repeat,
            var(--theme-piece-set-bp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;)) 100% 14.29% / 12.5% no-repeat,

            var(--theme-piece-set-wr, url(&quot;https://i
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bp.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20767"></a>
## FND-20767: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01636"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65213.

```text
b.png&quot;)) 28.57% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bq, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png&quot;)) 42.86% 0 / 12.5% no-repeat,
            var(--theme-piece-set-bk, url(&quot;https://image
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/bq.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20768"></a>
## FND-20768: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01637"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 64762.

```text
r: black;
                    background:
            var(--theme-piece-set-br, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png&quot;)) 0 0 / 12.5% no-repeat,
            var(--theme-piece-set-bn, url(&quot;https://images.che
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 65821.

```text
n.png&quot;)) 85.71% 0 / 12.5% no-repeat,
            var(--theme-piece-set-br, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png&quot;)) 100% 0 / 12.5% no-repeat,

            var(--theme-piece-set-bp, url(&quot;https://images
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/br.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20769"></a>
## FND-20769: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01638"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67527.

```text
ng&quot;)) 14.29% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wb, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png&quot;)) 28.57% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wq, url(&quot;https://im
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67992.

```text
ng&quot;)) 57.14% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wb, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png&quot;)) 71.43% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wn, url(&quot;https://im
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wb.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20770"></a>
## FND-20770: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01639"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67837.

```text
ng&quot;)) 42.86% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wk, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png&quot;)) 57.14% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wb, url(&quot;https://im
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wk.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20771"></a>
## FND-20771: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01640"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67372.

```text
/wr.png&quot;)) 0 100% / 12.5% no-repeat,
            var(--theme-piece-set-wn, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png&quot;)) 14.29% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wb, url(&quot;https://im
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 68147.

```text
ng&quot;)) 71.43% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wn, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png&quot;)) 85.71% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wr, url(&quot;https://im
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wn.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20772"></a>
## FND-20772: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01641"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 68456.

```text
png&quot;)) 100% 100% / 12.5% no-repeat,

            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 0 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://image
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 68608.

```text
p.png&quot;)) 0 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 14.29% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 68765.

```text
&quot;)) 14.29% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 28.57% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 68922.

```text
&quot;)) 28.57% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 42.86% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 69079.

```text
&quot;)) 42.86% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 57.14% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 69236.

```text
&quot;)) 57.14% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 71.43% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 69393.

```text
&quot;)) 71.43% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 85.71% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 69550.

```text
&quot;)) 85.71% 85.71% / 12.5% no-repeat,
            var(--theme-piece-set-wp, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;)) 100% 85.71% / 12.5% no-repeat;
                    "></div>

    
            <style>
   
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wp.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20773"></a>
## FND-20773: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01642"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67682.

```text
ng&quot;)) 28.57% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wq, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png&quot;)) 42.86% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wk, url(&quot;https://im
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wq.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20774"></a>
## FND-20774: https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png&quot;))

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png&quot;))",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01643"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 67222.

```text
g&quot;)) 100% 14.29% / 12.5% no-repeat,

            var(--theme-piece-set-wr, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png&quot;)) 0 100% / 12.5% no-repeat,
            var(--theme-piece-set-wn, url(&quot;https://images.
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 68302.

```text
ng&quot;)) 85.71% 100% / 12.5% no-repeat,
            var(--theme-piece-set-wr, url(&quot;https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png&quot;)) 100% 100% / 12.5% no-repeat,

            var(--theme-piece-set-wp, url(&quot;https://ima
```

**Source references:** SRC-0777  
**URL references:** <https://images.chesscomfiles.com/chess-themes/pieces/neo/150/wr.png&quot;))>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20775"></a>
## FND-20775: https://images.chesscomfiles.com/chess-themes/sounds/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://images.chesscomfiles.com/chess-themes/sounds/",
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
  "id": "URL-01644"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 180070.

```text
capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bun
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1248031.

```text
om`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`},pieceAnimationsEngine:iz.PieceAnimationsEngine.JS}}var sz=r((()=>{az(),Gne()})),cz,lz,u
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195727.

```text
capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bun
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 561437.

```text
om`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`},pieceAnimationsEngine:vv.PieceAnimationsEngine.JS}}var xv=r((()=>{yv(),mne()})),Sv,Cv,w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195727.

```text
capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bun
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 561437.

```text
om`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`},pieceAnimationsEngine:vv.PieceAnimationsEngine.JS}}var xv=r((()=>{yv(),mne()})),Sv,Cv,w
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://images.chesscomfiles.com/chess-themes/sounds/>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20776"></a>
## FND-20776: https://next.vuex.vuejs.org/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://next.vuex.vuejs.org/",
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
  "id": "URL-01645"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2828146.

```text
load:t,options:n}}function REt(e,t){TEt({id:`org.vuejs.vuex`,app:e,label:`Vuex`,homepage:`https://next.vuex.vuejs.org/`,logo:`https://vuejs.org/images/icons/favicon-96x96.png`,packageName:`vuex`,componentStat
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2828146.

```text
load:t,options:n}}function REt(e,t){TEt({id:`org.vuejs.vuex`,app:e,label:`Vuex`,homepage:`https://next.vuex.vuejs.org/`,logo:`https://vuejs.org/images/icons/favicon-96x96.png`,packageName:`vuex`,componentStat
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://next.vuex.vuejs.org/>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20777"></a>
## FND-20777: https://npm.pkg.github.com/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://npm.pkg.github.com/",
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
  "id": "URL-01646"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 232774.

```text
wle={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Tle={registry:`https://npm.pkg.github.com/`},Ele=`UNLICENSED`,Dle=`https://github.com/ChessCom/explanation-engine#readme`,Ole=[`expl
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 233560.

```text
Ile={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Lle={registry:`https://npm.pkg.github.com/`},to=`UNLICENSED`,no=`https://github.com/ChessCom/explanation-engine#readme`,ro=[`explana
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344305.

```text
Nye={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Pye={registry:`https://npm.pkg.github.com/`},Fye=[`dist/*`,`release-history.md`],Iye={entries:[`play`],vendorBundleName:`play`,links
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10103.

```text
Ile={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Lle={registry:`https://npm.pkg.github.com/`},to=`UNLICENSED`,no=`https://github.com/ChessCom/explanation-engine#readme`,ro=[`explana
```
- **SRC-0782** `research/refinement/live-source-excerpts.txt` — [preserved redacted evidence](../evidence/text/84fbc8cd25ab45b6f440c3650eb158b97092594a2adef748290c3547be21de2d.txt)
  Character offset 10975.

```text
wle={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Tle={registry:`https://npm.pkg.github.com/`},Ele=`UNLICENSED`,Dle=`https://github.com/ChessCom/explanation-engine#readme`,Ole=[`expl
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246512.

```text
Wse={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Gse={registry:`https://npm.pkg.github.com/`},Kse=`UNLICENSED`,qse=`https://github.com/ChessCom/explanation-engine#readme`,Jse=[`expl
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 247304.

```text
nce={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},rce={registry:`https://npm.pkg.github.com/`},ice=`UNLICENSED`,ace=`https://github.com/ChessCom/explanation-engine#readme`,oce=[`expl
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 246512.

```text
Wse={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},Gse={registry:`https://npm.pkg.github.com/`},Kse=`UNLICENSED`,qse=`https://github.com/ChessCom/explanation-engine#readme`,Jse=[`expl
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 247304.

```text
nce={type:`git`,url:`git+https://github.com/ChessCom/client-packages.git`},rce={registry:`https://npm.pkg.github.com/`},ice=`UNLICENSED`,ace=`https://github.com/ChessCom/explanation-engine#readme`,oce=[`expl
```

**Source references:** SRC-0781, SRC-0782, SRC-1137, SRC-1165  
**URL references:** <https://npm.pkg.github.com/>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-19886, FND-20489

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20778"></a>
## FND-20778: https://rive.app

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app",
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
  "id": "URL-01647"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3112760.

```text
rsion":"2.38.2","description":"Rive's webgl2 based web api.","main":"rive.js","homepage":"https://rive.app","repository":{"type":"git","url":"https://github.com/rive-app/rive-wasm/tree/master/js"}
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323329.

```text
rsion":"2.49.3","description":"Rive's webgl2 based web api.","main":"rive.js","homepage":"https://rive.app","repository":{"type":"git","url":"https://github.com/rive-app/rive-wasm/tree/master/js"}
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323329.

```text
rsion":"2.49.3","description":"Rive's webgl2 based web api.","main":"rive.js","homepage":"https://rive.app","repository":{"type":"git","url":"https://github.com/rive-app/rive-wasm/tree/master/js"}
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://rive.app>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20779"></a>
## FND-20779: https://rive.app)

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app)",
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
  "id": "URL-01648"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3112962.

```text
ords":["rive","animation"],"author":"Rive","contributors":["Luigi Rosso <[REDACTED_EMAIL]> (https://rive.app)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (htt
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3113013.

```text
utors":["Luigi Rosso <[REDACTED_EMAIL]> (https://rive.app)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]>
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3113066.

```text
pp)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]> (https://rive.app)","Matthew Sullivan <matt.j.sulliv
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3113122.

```text
"Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]> (https://rive.app)","Matthew Sullivan <[REDACTED_EMAIL]> (mailto:[REDACTED_EMAIL])","Chris
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3113255.

```text
[REDACTED_EMAIL]> (mailto:[REDACTED_EMAIL])","Chris Dalton <[REDACTED_EMAIL]> (https://rive.app)"],"license":"MIT","files":["rive.js","rive.wasm","rive_fallback.wasm","rive.js.map","rive
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323531.

```text
ords":["rive","animation"],"author":"Rive","contributors":["Luigi Rosso <[REDACTED_EMAIL]> (https://rive.app)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (htt
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323582.

```text
utors":["Luigi Rosso <[REDACTED_EMAIL]> (https://rive.app)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]>
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323635.

```text
pp)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]> (https://rive.app)","Matthew Sullivan <matt.j.sulliv
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323691.

```text
"Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]> (https://rive.app)","Matthew Sullivan <[REDACTED_EMAIL]> (mailto:[REDACTED_EMAIL])","Chris
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323824.

```text
[REDACTED_EMAIL]> (mailto:[REDACTED_EMAIL])","Chris Dalton <[REDACTED_EMAIL]> (https://rive.app)"],"license":"MIT","files":["rive.js","rive.wasm","rive_fallback.wasm","rive.js.map","rive
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323531.

```text
ords":["rive","animation"],"author":"Rive","contributors":["Luigi Rosso <[REDACTED_EMAIL]> (https://rive.app)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (htt
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323582.

```text
utors":["Luigi Rosso <[REDACTED_EMAIL]> (https://rive.app)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]>
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323635.

```text
pp)","Maxwell Talbot <[REDACTED_EMAIL]> (https://rive.app)","Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]> (https://rive.app)","Matthew Sullivan <matt.j.sulliv
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323691.

```text
"Arthur Vivian <[REDACTED_EMAIL]> (https://rive.app)","Umberto Sonnino <[REDACTED_EMAIL]> (https://rive.app)","Matthew Sullivan <[REDACTED_EMAIL]> (mailto:[REDACTED_EMAIL])","Chris
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3323824.

```text
[REDACTED_EMAIL]> (mailto:[REDACTED_EMAIL])","Chris Dalton <[REDACTED_EMAIL]> (https://rive.app)"],"license":"MIT","files":["rive.js","rive.wasm","rive_fallback.wasm","rive.js.map","rive
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://rive.app)>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20780"></a>
## FND-20780: https://rive.app/docs/editor/data-binding/migration-guide

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app/docs/editor/data-binding/migration-guide",
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
  "id": "URL-01649"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3406193.

```text
Use a state machine to control playback and data binding to react to changes instead. See https://rive.app/docs/editor/data-binding/migration-guide for how to migrate.`,te=`Subscribing to state change events at runtime is deprecated and 
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3406193.

```text
Use a state machine to control playback and data binding to react to changes instead. See https://rive.app/docs/editor/data-binding/migration-guide for how to migrate.`,te=`Subscribing to state change events at runtime is deprecated and 
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://rive.app/docs/editor/data-binding/migration-guide>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20781"></a>
## FND-20781: https://rive.app/docs/editor/data-binding/migration-guide#state-machine-inputs

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app/docs/editor/data-binding/migration-guide#state-machine-inputs",
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
  "id": "URL-01650"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3405625.

```text
ill be removed in a future major version: please use data binding properties instead. See https://rive.app/docs/editor/data-binding/migration-guide#state-machine-inputs for how to migrate.`,O=`Text run APIs are deprecated and will be removed in a future majo
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3405625.

```text
ill be removed in a future major version: please use data binding properties instead. See https://rive.app/docs/editor/data-binding/migration-guide#state-machine-inputs for how to migrate.`,O=`Text run APIs are deprecated and will be removed in a future majo
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://rive.app/docs/editor/data-binding/migration-guide#state-machine-inputs>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20782"></a>
## FND-20782: https://rive.app/docs/editor/data-binding/migration-guide#updating-text-runs-at-runtime

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app/docs/editor/data-binding/migration-guide#updating-text-runs-at-runtime",
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
  "id": "URL-01651"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3405841.

```text
cated and will be removed in a future major version: please use data binding instead. See https://rive.app/docs/editor/data-binding/migration-guide#updating-text-runs-at-runtime for how to migrate.`,ee=`Loop events are deprecated and will be removed in a future major
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3405841.

```text
cated and will be removed in a future major version: please use data binding instead. See https://rive.app/docs/editor/data-binding/migration-guide#updating-text-runs-at-runtime for how to migrate.`,ee=`Loop events are deprecated and will be removed in a future major
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://rive.app/docs/editor/data-binding/migration-guide#updating-text-runs-at-runtime>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20783"></a>
## FND-20783: https://rive.app/docs/editor/state-machine/states#actions

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app/docs/editor/state-machine/states#actions",
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
  "id": "URL-01652"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3406508.

```text
ty observers) or state machine actions to react to changes from your graphic instead. See https://rive.app/docs/editor/state-machine/states#actions for how to migrate.`,ne={animationNames:`animation-names`,animationsParam:`animations-par
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3406508.

```text
ty observers) or state machine actions to react to changes from your graphic instead. See https://rive.app/docs/editor/state-machine/states#actions for how to migrate.`,ne={animationNames:`animation-names`,animationsParam:`animations-par
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://rive.app/docs/editor/state-machine/states#actions>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20784"></a>
## FND-20784: https://rive.app/docs/runtimes/web/rive-events

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://rive.app/docs/runtimes/web/rive-events",
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
  "id": "URL-01653"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3405423.

```text
cated and will be removed in a future major version: please use data binding instead. See https://rive.app/docs/runtimes/web/rive-events for how to migrate.`,D=`State machine inputs are deprecated and will be removed in a futu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3405423.

```text
cated and will be removed in a future major version: please use data binding instead. See https://rive.app/docs/runtimes/web/rive-events for how to migrate.`,D=`State machine inputs are deprecated and will be removed in a futu
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://rive.app/docs/runtimes/web/rive-events>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20785"></a>
## FND-20785: https://schema.org

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://schema.org",
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
  "id": "URL-01654"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10586.

```text
e-credentials">

        <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "https://www.chess.com/#organization",

```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 5550.

```text
e-credentials">

        <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "https://www.chess.com/#organization",

```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10586.

```text
e-credentials">

        <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "https://www.chess.com/#organization",

```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://schema.org>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20786"></a>
## FND-20786: https://services.chess-dev.com/service/insights/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://services.chess-dev.com/service/insights/",
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
  "id": "URL-01655"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1089383.

```text
ub:`x-pubsub-port`},ZI={gamelist:`https://services.chess.com/service/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353180.

```text
ub:`x-pubsub-port`},sX={gamelist:`https://services.chess.com/service/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353180.

```text
ub:`x-pubsub-port`},sX={gamelist:`https://services.chess.com/service/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://services.chess-dev.com/service/insights/>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20787"></a>
## FND-20787: https://services.chess-dev.com/service/reactions-service/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://services.chess-dev.com/service/reactions-service/",
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
  "id": "URL-01656"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1089451.

```text
/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://serv
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353248.

```text
/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://serv
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353248.

```text
/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://serv
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://services.chess-dev.com/service/reactions-service/>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20788"></a>
## FND-20788: https://services.chess-dev.com/service/user-properties

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://services.chess-dev.com/service/user-properties",
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
  "id": "URL-01657"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1089586.

```text
ons-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://services.chess-dev.com/service/user-properties`}})),$I,eL=r((()=>{z(),$I=yd()})),ALe,jLe=r((()=>{Ke(),eL(),Sy(),ALe=xy.extend({credentia
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353383.

```text
ons-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://services.chess-dev.com/service/user-properties`}}));function Grt(e){return e!=null&&typeof e!=`function`&&Tle(e.length)}var lX=r((()=>{E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353383.

```text
ons-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://services.chess-dev.com/service/user-properties`}}));function Grt(e){return e!=null&&typeof e!=`function`&&Tle(e.length)}var lX=r((()=>{E
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://services.chess-dev.com/service/user-properties>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20789"></a>
## FND-20789: https://services.chess.com/service/gamelist/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://services.chess.com/service/gamelist/",
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
  "id": "URL-01658"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1089327.

```text
rnative:`x-rsocket-port`,presence:`x-presence-port`,pubsub:`x-pubsub-port`},ZI={gamelist:`https://services.chess.com/service/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://se
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353124.

```text
rnative:`x-rsocket-port`,presence:`x-presence-port`,pubsub:`x-pubsub-port`},sX={gamelist:`https://services.chess.com/service/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://se
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353124.

```text
rnative:`x-rsocket-port`,presence:`x-presence-port`,pubsub:`x-pubsub-port`},sX={gamelist:`https://services.chess.com/service/gamelist/`,insights:`https://services.chess-dev.com/service/insights/`,reactionsService:`https://se
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://services.chess.com/service/gamelist/>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20790"></a>
## FND-20790: https://services.chess.com/service/topplayers/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://services.chess.com/service/topplayers/",
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
  "id": "URL-01659"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1089522.

```text
,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://services.chess-dev.com/service/user-properties`}})),$I,eL=r((()=
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353319.

```text
,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://services.chess-dev.com/service/user-properties`}}));function Grt
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2353319.

```text
,reactionsService:`https://services.chess-dev.com/service/reactions-service/`,topplayers:`https://services.chess.com/service/topplayers/`,userProperties:`https://services.chess-dev.com/service/user-properties`}}));function Grt
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://services.chess.com/service/topplayers/>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20791"></a>
## FND-20791: https://support.chess.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://support.chess.com",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0175",
    "SRC-0177",
    "SRC-0191"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01660"
}

### Evidence

- **SRC-0175** `research/play-chunks/client.a70e00bc.DVI1ix4lyU.chunk.js` — [preserved redacted evidence](../evidence/text/4be0ac1c4252308e1be3493430420dfd11fc1f009ff2b2e249ed6a97434c4e7b.js)
  Character offset 4739.

```text
Support</a></u>.`,{"%guidelinesUrl%":l.generate(`web_policies_community`),"%supportUrl%":`https://support.chess.com`});break;default:n&&(i=n);break}i&&S({notification:{behavior:{dismissTimeout:12e3,ignoreS
```
- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 9511.

```text
Support</a></u>.`,{"%guidelinesUrl%":o.generate(`web_policies_community`),"%supportUrl%":`https://support.chess.com`});break;default:r=n??l(`An unknown error occurred, please try again later`);break}r&&p(r
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 9044.

```text
Support</a></u>.`,{"%guidelinesUrl%":l.generate(`web_policies_community`),"%supportUrl%":`https://support.chess.com`});break;default:r=t??g(`An unknown error occurred, please try again later`);break}r&&C({
```

**Source references:** SRC-0175, SRC-0177, SRC-0191  
**URL references:** <https://support.chess.com>  
**Related findings:** FND-18183, FND-18184, FND-19434, FND-18198

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20792"></a>
## FND-20792: https://support.chess.com/article/670-why-cant-i-challenge-certain-players

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://support.chess.com/article/670-why-cant-i-challenge-certain-players",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0146",
    "SRC-0163"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01661"
}

### Evidence

- **SRC-0146** `research/play-chunks/client.4a9e3c32.B86Cut1SJs.chunk.js` — [preserved redacted evidence](../evidence/text/91bb388e5a35c735e8c40d774316eb09f860a1467032f305625fd81728ef63ac.js)
  Character offset 7314.

```text
er.player_protection_operative`:i&&(n=v(`You are not able to challenge %toUser%. <a href="https://support.chess.com/article/670-why-cant-i-challenge-certain-players" target="_blank">Find out more</a>.`,{"%toUser%":i.getUsername()}));break;case`user.playi
```
- **SRC-0163** `research/play-chunks/client.8377e444.3SCIMnf7Uj.chunk.js` — [preserved redacted evidence](../evidence/text/685f81519b86972486f4b8f3d0873f386d10db5aef6aa8d044dad3138a7e87f4.js)
  Character offset 3590.

```text
rget_user_cannot_be_challenged`:t&&(i=y(`You are not able to challenge %toUser%. <a href="https://support.chess.com/article/670-why-cant-i-challenge-certain-players" target="_blank">Find out more</a>.`,{"%toUser%":t}));break;case`target_user_is_blocked`:
```
- **SRC-0163** `research/play-chunks/client.8377e444.3SCIMnf7Uj.chunk.js` — [preserved redacted evidence](../evidence/text/685f81519b86972486f4b8f3d0873f386d10db5aef6aa8d044dad3138a7e87f4.js)
  Character offset 5084.

```text
eak;case`target_user_protected`:t&&(i=y(`You are not able to challenge %toUser%. <a href="https://support.chess.com/article/670-why-cant-i-challenge-certain-players" target="_blank">Find out more</a>.`,{"%toUser%":t}));break;case`initial_position_invalid
```

**Source references:** SRC-0146, SRC-0163  
**URL references:** <https://support.chess.com/article/670-why-cant-i-challenge-certain-players>  
**Related findings:** FND-18183, FND-18184, FND-19434

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20793"></a>
## FND-20793: https://support.chess.com/articles/8584209-how-do-i-fix-my-disconnect-lag-issues

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://support.chess.com/articles/8584209-how-do-i-fix-my-disconnect-lag-issues",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0153"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01662"
}

### Evidence

- **SRC-0153** `research/play-chunks/client.6c82c33c.YwP1GMJYZB.chunk.js` — [preserved redacted evidence](../evidence/text/e5559f246444b0455ecdbae380ac8312067a4845bac1fb4f9a59d205c306ae12.js)
  Character offset 1782.

```text
age. <a  href="%1$s%" target="_blank">Visit our Help Center</a> to learn more.`,{"%1$s%":`https://support.chess.com/articles/8584209-how-do-i-fix-my-disconnect-lag-issues`});default:return y(`You have been disconnected. Please, refresh the page to reconnect.`)
```

**Source references:** SRC-0153  
**URL references:** <https://support.chess.com/articles/8584209-how-do-i-fix-my-disconnect-lag-issues>  
**Related findings:** FND-19434, FND-19825

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20794"></a>
## FND-20794: https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.mp3",
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
  "id": "URL-01663"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2627195.

```text
referPendingCoach:e})?.voiceId||null}var m0=r((()=>{UH()}));function jvt({hash:e}){return`https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.mp3`}var Mvt=r((()=>{f0(),m0()}));function Nvt({hash:e}){return`https://text-and-audio.chess.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2627195.

```text
referPendingCoach:e})?.voiceId||null}var m0=r((()=>{UH()}));function jvt({hash:e}){return`https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.mp3`}var Mvt=r((()=>{f0(),m0()}));function Nvt({hash:e}){return`https://text-and-audio.chess.
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.mp3>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20795"></a>
## FND-20795: https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.viseme

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.viseme",
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
  "id": "URL-01664"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2627373.

```text
erPendingCoach:!0})}/${e}.mp3`}var Mvt=r((()=>{f0(),m0()}));function Nvt({hash:e}){return`https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.viseme`}var Pvt=r((()=>{f0(),m0()}));function Fvt({preferPendingCoach:e}={preferPendingCoach:!1}
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2627373.

```text
erPendingCoach:!0})}/${e}.mp3`}var Mvt=r((()=>{f0(),m0()}));function Nvt({hash:e}){return`https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.viseme`}var Pvt=r((()=>{f0(),m0()}));function Fvt({preferPendingCoach:e}={preferPendingCoach:!1}
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://text-and-audio.chess.com/prod/released/${p0({preferPendingCoach:!0})}/${d0({preferPendingCoach:!0})}/${e}.viseme>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20796"></a>
## FND-20796: https://text-and-audio.chess.com/text_prod/released/${e}/${t}/cee_asset_v2.json.bzp

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://text-and-audio.chess.com/text_prod/released/${e}/${t}/cee_asset_v2.json.bzp",
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
  "id": "URL-01665"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3024345.

```text
({textId:e,locale:t});if(r){await r.promise?.catch(()=>{});return}let i;try{let r=xy.get(`https://text-and-audio.chess.com/text_prod/released/${e}/${t}/cee_asset_v2.json.bzp`);i=n.speechAssets.add({locale:t,textId:e,promise:r});let{data:a}=await r;i.data=a,P7.emi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2778966.

```text
({textId:e,locale:t});if(r){await r.promise?.catch(()=>{});return}let i;try{let r=bL.get(`https://text-and-audio.chess.com/text_prod/released/${e}/${t}/cee_asset_v2.json.bzp`);i=n.speechAssets.add({locale:t,textId:e,promise:r});let{data:a}=await r;i.data=a,c_.emi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2778966.

```text
({textId:e,locale:t});if(r){await r.promise?.catch(()=>{});return}let i;try{let r=bL.get(`https://text-and-audio.chess.com/text_prod/released/${e}/${t}/cee_asset_v2.json.bzp`);i=n.speechAssets.add({locale:t,textId:e,promise:r});let{data:a}=await r;i.data=a,c_.emi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://text-and-audio.chess.com/text_prod/released/${e}/${t}/cee_asset_v2.json.bzp>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20797"></a>
## FND-20797: https://twitter.com/chesscom

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://twitter.com/chesscom",
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
  "id": "URL-01666"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11421.

```text
  },
        "sameAs": [
          "https://www.youtube.com/user/wwwChesscom",
          "https://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6385.

```text
  },
        "sameAs": [
          "https://www.youtube.com/user/wwwChesscom",
          "https://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11421.

```text
  },
        "sameAs": [
          "https://www.youtube.com/user/wwwChesscom",
          "https://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://twitter.com/chesscom>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20798"></a>
## FND-20798: https://unpkg.com/${i.name}@${i.version}/rive.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://unpkg.com/${i.name}@${i.version}/rive.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01667"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3040538.

```text
etWasmBinary=function(){return e.wasmBinary},e.isLoading=!1,e.callBackQueue=[],e.wasmURL=`https://unpkg.com/${i.name}@${i.version}/rive.wasm`,e.wasmFallbackURL=`https://cdn.jsdelivr.net/npm/${i.name}@${i.version}/rive_fallback.was
```

**Source references:** SRC-0781  
**URL references:** <https://unpkg.com/${i.name}@${i.version}/rive.wasm>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20799"></a>
## FND-20799: https://unpkg.com/${o.name}@${o.version}/rive.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://unpkg.com/${o.name}@${o.version}/rive.wasm",
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
  "id": "URL-01668"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3151972.

```text
etWasmBinary=function(){return e.wasmBinary},e.isLoading=!1,e.callBackQueue=[],e.wasmURL=`https://unpkg.com/${o.name}@${o.version}/rive.wasm`,e.wasmFallbackURL=`https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.was
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3151972.

```text
etWasmBinary=function(){return e.wasmBinary},e.isLoading=!1,e.callBackQueue=[],e.wasmURL=`https://unpkg.com/${o.name}@${o.version}/rive.wasm`,e.wasmFallbackURL=`https://cdn.jsdelivr.net/npm/${o.name}@${o.version}/rive_fallback.was
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://unpkg.com/${o.name}@${o.version}/rive.wasm>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20800"></a>
## FND-20800: https://unpkg.com/${o.name}@${o.version}/rive_threads.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://unpkg.com/${o.name}@${o.version}/rive_threads.wasm",
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
  "id": "URL-01669"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3152174.

```text
o.version}/rive_fallback.wasm`,e.wasmBinary=null,e.wasmThreadsURL=typeof a()==`function`?`https://unpkg.com/${o.name}@${o.version}/rive_threads.wasm`:null,e.triedThreads=!1,e.parallelParts=null,e.replayWorker=!0,e.replayCapsArrived=!1,e.r
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3152174.

```text
o.version}/rive_fallback.wasm`,e.wasmBinary=null,e.wasmThreadsURL=typeof a()==`function`?`https://unpkg.com/${o.name}@${o.version}/rive_threads.wasm`:null,e.triedThreads=!1,e.parallelParts=null,e.replayWorker=!0,e.replayCapsArrived=!1,e.r
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://unpkg.com/${o.name}@${o.version}/rive_threads.wasm>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20801"></a>
## FND-20801: https://verify.${t}

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://verify.${t}",
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
  "id": "URL-01670"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 540031.

```text
1,gy=[]}function $Te(){let e=new URL(window.location.href),t=Xd(),n=e.pathname,r=new URL(`https://verify.${t}`);r.searchParams.set(`redirect`,`referer`),r.searchParams.set(`path`,n),window.location.a
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1373785.

```text
1,sL=[]}function $ze(){let e=new URL(window.location.href),t=wf(),n=e.pathname,r=new URL(`https://verify.${t}`);r.searchParams.set(`redirect`,`referer`),r.searchParams.set(`path`,n),window.location.a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1373785.

```text
1,sL=[]}function $ze(){let e=new URL(window.location.href),t=wf(),n=e.pathname,r=new URL(`https://verify.${t}`);r.searchParams.set(`redirect`,`referer`),r.searchParams.set(`path`,n),window.location.a
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://verify.${t}>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20802"></a>
## FND-20802: https://vuejs.org/images/icons/favicon-96x96.png

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://vuejs.org/images/icons/favicon-96x96.png",
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
  "id": "URL-01671"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2828182.

```text
TEt({id:`org.vuejs.vuex`,app:e,label:`Vuex`,homepage:`https://next.vuex.vuejs.org/`,logo:`https://vuejs.org/images/icons/favicon-96x96.png`,packageName:`vuex`,componentStateTypes:[qEt]},function(n){n.addTimelineLayer({id:r6,labe
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2828182.

```text
TEt({id:`org.vuejs.vuex`,app:e,label:`Vuex`,homepage:`https://next.vuex.vuejs.org/`,logo:`https://vuejs.org/images/icons/favicon-96x96.png`,packageName:`vuex`,componentStateTypes:[qEt]},function(n){n.addTimelineLayer({id:r6,labe
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <https://vuejs.org/images/icons/favicon-96x96.png>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20803"></a>
## FND-20803: https://www.chess.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0064",
    "SRC-0065",
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
  "id": "URL-01672"
}

### Evidence

- **SRC-0064** `fetch-assets.sh` — [preserved redacted evidence](../evidence/text/4fd21605ac735ee70e6717867eb17d057b430580a6adf2918d177c00aef42751.sh)
  Character offset 140.

```text
inux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
ROOT='https://www.chess.com'
D='extension/engines'
get() { # get <relative-url> <dest>
  local u="$ROOT/$1" dst="$2"

```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10739.

```text
@id": "https://www.chess.com/#organization",
        "name": "Chess.com",
        "url": "https://www.chess.com",
        "logo": {
          "@type": "ImageObject",
                    "url": "https:/
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 5703.

```text
@id": "https://www.chess.com/#organization",
        "name": "Chess.com",
        "url": "https://www.chess.com",
        "logo": {
          "@type": "ImageObject",
                    "url": "https:/
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 138142.

```text
 Number(n.toFixed(1))}var yee=r((()=>{}));function Qn(e){return e?.assetPaths?.basePath||`https://www.chess.com`}var $n=r((()=>{})),er,tr=r((()=>{er={AddAnnotation:`AddAnnotation`,AddComment:`AddCommen
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1247922.

```text
,threatSquareOpacity:.8,useSharedStyleTag:!1,disableRookCastling:!1,assetPaths:{basePath:`https://www.chess.com`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`ht
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2999603.

```text
()=>{rq(),$Vt=g7(),pI(),Vf()})),tHt,nHt,rHt=r((()=>{ZF(),UZ(),ZZ(),df(),uf()&&(tHt=BZ(KZ(`https://www.chess.com`))),nHt=qZ(kIe,tHt)})),v7,y7=r((()=>{z(),Sq(),v7=dg(`play.modules.tournament-list`,()=>fe
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 155645.

```text
 Number(n.toFixed(1))}var aee=r((()=>{}));function Vn(e){return e?.assetPaths?.basePath||`https://www.chess.com`}var Hn=r((()=>{})),Un,Wn=r((()=>{Un={AddAnnotation:`AddAnnotation`,AddComment:`AddCommen
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262354.

```text
Ss,Rle=r((()=>{bs={mockServer:{port:3005},service:{prefix:`/service/courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},xs={mockServer:{por
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262421.

```text
/courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},xs={mockServer:{port:3005},service:{prefix:`/service/opening-courses/rpc`,baseURL:`htt
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262529.

```text
com`}},xs={mockServer:{port:3005},service:{prefix:`/service/opening-courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},Ss=[{prefixes:[`/co
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262596.

```text
-courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},Ss=[{prefixes:[`/courses`,`/course`],overrideKey:`courses`,config:bs},{prefixes:[`/ope
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 561328.

```text
,threatSquareOpacity:.8,useSharedStyleTag:!1,disableRookCastling:!1,assetPaths:{basePath:`https://www.chess.com`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`ht
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10739.

```text
@id": "https://www.chess.com/#organization",
        "name": "Chess.com",
        "url": "https://www.chess.com",
        "logo": {
          "@type": "ImageObject",
                    "url": "https:/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 155645.

```text
 Number(n.toFixed(1))}var aee=r((()=>{}));function Vn(e){return e?.assetPaths?.basePath||`https://www.chess.com`}var Hn=r((()=>{})),Un,Wn=r((()=>{Un={AddAnnotation:`AddAnnotation`,AddComment:`AddCommen
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262354.

```text
Ss,Rle=r((()=>{bs={mockServer:{port:3005},service:{prefix:`/service/courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},xs={mockServer:{por
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262421.

```text
/courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},xs={mockServer:{port:3005},service:{prefix:`/service/opening-courses/rpc`,baseURL:`htt
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262529.

```text
com`}},xs={mockServer:{port:3005},service:{prefix:`/service/opening-courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},Ss=[{prefixes:[`/co
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 262596.

```text
-courses/rpc`,baseURL:`https://www.chess.com`,headers:{}},authentication:{callbackDomain:`https://www.chess.com`}},Ss=[{prefixes:[`/courses`,`/course`],overrideKey:`courses`,config:bs},{prefixes:[`/ope
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 561328.

```text
,threatSquareOpacity:.8,useSharedStyleTag:!1,disableRookCastling:!1,assetPaths:{basePath:`https://www.chess.com`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`ht
```

**Source references:** SRC-0064, SRC-0065, SRC-0777, SRC-0781, SRC-1137, SRC-1150, SRC-1165  
**URL references:** <https://www.chess.com>  
**Related findings:** FND-18976, FND-20342, FND-20462, FND-18977, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20804"></a>
## FND-20804: https://www.chess.com/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/",
  "type": "page_or_route_candidate",
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
  "id": "URL-01673"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 39733.

```text
lass="mobile-toolbar-logo-wrapper"
        data-interaction="mobile-header"
        href="https://www.chess.com/"
        target="_self">
        <img
          class="mobile-toolbar-logo"
          alt
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 41616.

```text
n"
    data-interaction="header"
    aria-label="Chess.com - Play Chess Online"
    href="https://www.chess.com/"
    target="_self">
        <div class="sidebar-logo-image"></div>
  </a>

  <div class=
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 34869.

```text
lass="mobile-toolbar-logo-wrapper"
        data-interaction="mobile-header"
        href="https://www.chess.com/"
        target="_self">
        <img
          class="mobile-toolbar-logo"
          alt
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 36780.

```text
n"
    data-interaction="header"
    aria-label="Chess.com - Play Chess Online"
    href="https://www.chess.com/"
    target="_self">
        <div class="sidebar-logo-image"></div>
  </a>

  <div class=
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 39733.

```text
lass="mobile-toolbar-logo-wrapper"
        data-interaction="mobile-header"
        href="https://www.chess.com/"
        target="_self">
        <img
          class="mobile-toolbar-logo"
          alt
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 41616.

```text
n"
    data-interaction="header"
    aria-label="Chess.com - Play Chess Online"
    href="https://www.chess.com/"
    target="_self">
        <div class="sidebar-logo-image"></div>
  </a>

  <div class=
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20805"></a>
## FND-20805: https://www.chess.com/#organization

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/#organization",
  "type": "page_or_route_candidate",
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
  "id": "URL-01674"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10656.

```text
       "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "https://www.chess.com/#organization",
        "name": "Chess.com",
        "url": "https://www.chess.com",
        "logo": {

```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 5620.

```text
       "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "https://www.chess.com/#organization",
        "name": "Chess.com",
        "url": "https://www.chess.com",
        "logo": {

```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10656.

```text
       "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "https://www.chess.com/#organization",
        "name": "Chess.com",
        "url": "https://www.chess.com",
        "logo": {

```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/#organization>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20806"></a>
## FND-20806: https://www.chess.com/**

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/**",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0055"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01675"
}

### Evidence

- **SRC-0055** `extension/test/browser-cee-test.mjs` — [preserved redacted evidence](../evidence/text/2adbf9d468b472e760f439ff8ee05ccc58423d88253d757a79218c5524970bd3.mjs)
  Character offset 3163.

```text
creen document via bridge -> service worker.
  await page.close();
  await context.route('https://www.chess.com/**', route => route.fulfill({
    status: 200, contentType: 'text/html',
    body: '<!doctyp
```

**Source references:** SRC-0055  
**URL references:** <https://www.chess.com/**>  
**Related findings:** FND-19399, FND-19400, FND-20215

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20807"></a>
## FND-20807: https://www.chess.com/af/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/af/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01676"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7799.

```text
s://www.chess.com/uk/analysis" hreflang="uk" />
              <link rel="alternate" href="https://www.chess.com/af/analysis" hreflang="af" />
              <link rel="alternate" href="https://www.chess.com/ar/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7799.

```text
s://www.chess.com/uk/analysis" hreflang="uk" />
              <link rel="alternate" href="https://www.chess.com/af/analysis" hreflang="af" />
              <link rel="alternate" href="https://www.chess.com/ar/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/af/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20808"></a>
## FND-20808: https://www.chess.com/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0202",
    "SRC-0777",
    "SRC-1147",
    "SRC-1150",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 200; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01677",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/analysis",
      "http_status": 200,
      "size_download": 113132,
      "content_type_and_optional_elapsed": "text/html; charset=UTF-8 0.252476",
      "source_id": "SRC-0202",
      "line": 24,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 3971.

```text
lysis Board, Game Review &amp; PGN Editor" />

          <meta property="og:url" content="https://www.chess.com/analysis" />

          <meta property="fb:app_id" content="2427617054" />

          <meta proper
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5156.

```text
-analysis-board.4b839d53.png" />

  
  
        
  
          <link rel="alternate" href="https://www.chess.com/analysis" hreflang="en" />

            
              <link rel="alternate" href="https://www.che
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10373.

```text
ess.com/ur/analysis" hreflang="ur" />
          
    
        <link rel="canonical" href="https://www.chess.com/analysis">
  
    
              
    
    <link rel="manifest" href="/manifest.json" crossorigin=
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16097.

```text
r"},"sub":[],"badge":null},{"id":"train.analysis","type":"link","label":"Analysis","url":"https:\/\/www.chess.com\/analysis","icon":{"name":"magnifier-analysis","variant":"color"},"sub":[],"badge":null},{"id":"tra
```
- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3195.

```text
engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analysis                                                                       200 113132 text/htm
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 11061.

```text
r"},"sub":[],"badge":null},{"id":"train.analysis","type":"link","label":"Analysis","url":"https:\/\/www.chess.com\/analysis","icon":{"name":"magnifier-analysis","variant":"color"},"sub":[],"badge":null},{"id":"tra
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1710.

```text
ine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 3971.

```text
lysis Board, Game Review &amp; PGN Editor" />

          <meta property="og:url" content="https://www.chess.com/analysis" />

          <meta property="fb:app_id" content="2427617054" />

          <meta proper
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5156.

```text
-analysis-board.4b839d53.png" />

  
  
        
  
          <link rel="alternate" href="https://www.chess.com/analysis" hreflang="en" />

            
              <link rel="alternate" href="https://www.che
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10373.

```text
ess.com/ur/analysis" hreflang="ur" />
          
    
        <link rel="canonical" href="https://www.chess.com/analysis">
  
    
              
    
    <link rel="manifest" href="/manifest.json" crossorigin=
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16097.

```text
r"},"sub":[],"badge":null},{"id":"train.analysis","type":"link","label":"Analysis","url":"https:\/\/www.chess.com\/analysis","icon":{"name":"magnifier-analysis","variant":"color"},"sub":[],"badge":null},{"id":"tra
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3195.

```text
engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analysis                                                                       200 113132 text/htm
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1710.

```text
ine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```

**Source references:** SRC-0065, SRC-0202, SRC-0777, SRC-1147, SRC-1150, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18975, FND-18976

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20809"></a>
## FND-20809: https://www.chess.com/analysis/collections

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/analysis/collections",
  "type": "page_or_route_candidate",
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
  "id": "URL-01678"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20611.

```text
variant":"color"},"sub":[{"id":"other.library","type":"link","label":"Collections","url":"https:\/\/www.chess.com\/analysis\/collections","icon":{"name":"board-stack-green","variant":"color"},"sub":[],"badge":null},{"id":"othe
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 15575.

```text
variant":"color"},"sub":[{"id":"other.library","type":"link","label":"Collections","url":"https:\/\/www.chess.com\/analysis\/collections","icon":{"name":"board-stack-green","variant":"color"},"sub":[],"badge":null},{"id":"othe
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20611.

```text
variant":"color"},"sub":[{"id":"other.library","type":"link","label":"Collections","url":"https:\/\/www.chess.com\/analysis\/collections","icon":{"name":"board-stack-green","variant":"color"},"sub":[],"badge":null},{"id":"othe
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/analysis/collections>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20810"></a>
## FND-20810: https://www.chess.com/analysis/game/live/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/analysis/game/live/",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-2047"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01679"
}

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 30482.

```text
ine, your own account)

1. Open DevTools → Network → WS, tick **Preserve log**.
2. Go to `https://www.chess.com/analysis/game/live/<your-game-id>` and press
   **Game Review**.
3. Click the `wss://analysis.chess.com/443/v
```

**Source references:** SRC-2047  
**URL references:** <https://www.chess.com/analysis/game/live/>  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20811"></a>
## FND-20811: https://www.chess.com/analysis/game/live/186934806892/review

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/analysis/game/live/186934806892/review",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0055"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01680"
}

### Evidence

- **SRC-0055** `extension/test/browser-cee-test.mjs` — [preserved redacted evidence](../evidence/text/2adbf9d468b472e760f439ff8ee05ccc58423d88253d757a79218c5524970bd3.mjs)
  Character offset 4100.

```text
l-review/.test(message.text())) statuses.push(message.text()); });
  await gamePage.goto('https://www.chess.com/analysis/game/live/186934806892/review');
  const requestBytes = encodeMessage('.chesscom.ceac.v2.GameReviewRequest', {
    newG
```

**Source references:** SRC-0055  
**URL references:** <https://www.chess.com/analysis/game/live/186934806892/review>  
**Related findings:** FND-19399, FND-19400, FND-20215

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20812"></a>
## FND-20812: https://www.chess.com/analysis/game/live/186934806892/review?move=0

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/analysis/game/live/186934806892/review?move=0",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0125",
    "SRC-0786",
    "SRC-0787",
    "SRC-0788",
    "SRC-2044",
    "SRC-2049"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01681"
}

### Evidence

- **SRC-0125** `research/fixtures/doting-prospect.pgn` — [preserved redacted evidence](../evidence/text/88562cf522f5be8a600f5e9d352e605f4b34239c990954ef76134a7f0c6ce794.pgn)
  Character offset 372.

```text
 by checkmate"]
[StartTime "18:58:21"]
[EndDate "2026.11.10"]
[EndTime "18:59:55"]
[Link "https://www.chess.com/analysis/game/live/186934806892/review?move=0"]

1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+
8. Kf1 
```
- **SRC-0786** `research/refinement/probe-human-decoded-log.txt` — [preserved redacted evidence](../evidence/text/b60812946f93d0fec18aa67a30bb831542870aa7c7aaf338ce6ae3cfb449fa1e.txt)
  Character offset 372.

```text
 by checkmate"]
[StartTime "18:58:21"]
[EndDate "2026.11.10"]
[EndTime "18:59:55"]
[Link "https://www.chess.com/analysis/game/live/186934806892/review?move=0"]

1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+
8. Kf1 
```
- **SRC-0787** `research/refinement/probe-human-no-maia-decoded-log.txt` — [preserved redacted evidence](../evidence/text/cee84f6e0fcf886152acd6ad0a88e0d970be0ea3f1fd331e48767d612cbc6f2a.txt)
  Character offset 372.

```text
 by checkmate"]
[StartTime "18:58:21"]
[EndDate "2026.11.10"]
[EndTime "18:59:55"]
[Link "https://www.chess.com/analysis/game/live/186934806892/review?move=0"]

1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+
8. Kf1 
```
- **SRC-0788** `research/refinement/probe-normal-decoded-log.txt` — [preserved redacted evidence](../evidence/text/fc6a30e936c2a0c6f15a458fdc52a1a744fe2294c8e5b3501cd3d9c4b252dbd1.txt)
  Character offset 372.

```text
 by checkmate"]
[StartTime "18:58:21"]
[EndDate "2026.11.10"]
[EndTime "18:59:55"]
[Link "https://www.chess.com/analysis/game/live/186934806892/review?move=0"]

1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+
8. Kf1 
```
- **SRC-2044** `torch-refinement-research.zip!/research/fixtures/doting-prospect.pgn` — [preserved redacted evidence](../evidence/text/88562cf522f5be8a600f5e9d352e605f4b34239c990954ef76134a7f0c6ce794.pgn)
  Character offset 372.

```text
 by checkmate"]
[StartTime "18:58:21"]
[EndDate "2026.11.10"]
[EndTime "18:59:55"]
[Link "https://www.chess.com/analysis/game/live/186934806892/review?move=0"]

1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+
8. Kf1 
```
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 1545.

```text
e-parameter comparison against their original 20-ply reference.
- Original reference URL: https://www.chess.com/analysis/game/live/186934806892/review?move=0 ; 20 plies, result0-1, White Elo100/Black333, 600-second control. Reference accuracy71.7/
```

**Source references:** SRC-0125, SRC-0786, SRC-0787, SRC-0788, SRC-2044, SRC-2049  
**URL references:** <https://www.chess.com/analysis/game/live/186934806892/review?move=0>  
**Related findings:** FND-18935

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20813"></a>
## FND-20813: https://www.chess.com/analysis/game/live/187140546024/review?flip=true&move=0

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/analysis/game/live/187140546024/review?flip=true&move=0",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0127",
    "SRC-2045"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01682"
}

### Evidence

- **SRC-0127** `research/fixtures/human-game.pgn` — [preserved redacted evidence](../evidence/text/ce5eada5268e6670178f0cdb8a776408d483455467c98a4d5c2b5be4fb5ae174.pgn)
  Character offset 611.

```text
 by checkmate"]
[StartTime "17:44:46"]
[EndDate "2026.11.13"]
[EndTime "17:53:29"]
[Link "https://www.chess.com/analysis/game/live/187140546024/review?flip=true&move=0"]
[WhiteCountry "123"]
[WhiteTitle ""]
[BlackCountry "45"]
[BlackTitle ""]

1. d4 d5 2. c
```
- **SRC-2045** `torch-refinement-research.zip!/research/fixtures/human-game.pgn` — [preserved redacted evidence](../evidence/text/ce5eada5268e6670178f0cdb8a776408d483455467c98a4d5c2b5be4fb5ae174.pgn)
  Character offset 611.

```text
 by checkmate"]
[StartTime "17:44:46"]
[EndDate "2026.11.13"]
[EndTime "17:53:29"]
[Link "https://www.chess.com/analysis/game/live/187140546024/review?flip=true&move=0"]
[WhiteCountry "123"]
[WhiteTitle ""]
[BlackCountry "45"]
[BlackTitle ""]

1. d4 d5 2. c
```

**Source references:** SRC-0127, SRC-2045  
**URL references:** <https://www.chess.com/analysis/game/live/187140546024/review?flip=true&move=0>  
**Related findings:** FND-20911, FND-21011

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20814"></a>
## FND-20814: https://www.chess.com/ar/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ar/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01683"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7893.

```text
s://www.chess.com/af/analysis" hreflang="af" />
              <link rel="alternate" href="https://www.chess.com/ar/analysis" hreflang="ar" />
              <link rel="alternate" href="https://www.chess.com/az/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7893.

```text
s://www.chess.com/af/analysis" hreflang="af" />
              <link rel="alternate" href="https://www.chess.com/ar/analysis" hreflang="ar" />
              <link rel="alternate" href="https://www.chess.com/az/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ar/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20815"></a>
## FND-20815: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#agreement

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#agreement",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01684"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 813961.

```text
 timeout vs insufficient material`),[yE.UNTERMINATED]:L(`unterminated`)},EE={[yE.AGREED]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#agreement`,[yE.CHECKMATED]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-expla
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#agreement>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20816"></a>
## FND-20816: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#checkmate

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#checkmate",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01685"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814065.

```text
ess.com/article/view/how-chess-games-can-end-8-ways-explained#agreement`,[yE.CHECKMATED]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#checkmate`,[yE.FIFTY_MOVE]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-expla
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#checkmate>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20817"></a>
## FND-20817: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#insufficient-material

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#insufficient-material",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01686"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814275.

```text
s.com/article/view/how-chess-games-can-end-8-ways-explained#move-rule`,[yE.INSUFFICIENT]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#insufficient-material`,[yE.REPETITION]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-expla
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814810.

```text
m/article/view/how-chess-games-can-end-8-ways-explained#timeout`,[yE.TIMEVSINSUFFICIENT]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#insufficient-material`},DE={HALF_HALF:`1/2-1/2`,HALF_HALF_ENTITY:`&frac12;-&frac12;`,ONE_ZERO:`1-0`,ZERO_ONE:`0
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#insufficient-material>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20818"></a>
## FND-20818: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#move-rule

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#move-rule",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01687"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814169.

```text
ess.com/article/view/how-chess-games-can-end-8-ways-explained#checkmate`,[yE.FIFTY_MOVE]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#move-rule`,[yE.INSUFFICIENT]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-exp
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#move-rule>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20819"></a>
## FND-20819: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#repetition

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#repetition",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01688"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814391.

```text
cle/view/how-chess-games-can-end-8-ways-explained#insufficient-material`,[yE.REPETITION]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#repetition`,[yE.RESIGNED]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explain
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#repetition>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20820"></a>
## FND-20820: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#resignation

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#resignation",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01689"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814494.

```text
hess.com/article/view/how-chess-games-can-end-8-ways-explained#repetition`,[yE.RESIGNED]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#resignation`,[yE.STALEMATE]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explai
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#resignation>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20821"></a>
## FND-20821: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#stalemate

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#stalemate",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01690"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814599.

```text
ss.com/article/view/how-chess-games-can-end-8-ways-explained#resignation`,[yE.STALEMATE]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#stalemate`,[yE.TIMEOUT]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explaine
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#stalemate>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20822"></a>
## FND-20822: https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#timeout

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#timeout",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01691"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 814700.

```text
.chess.com/article/view/how-chess-games-can-end-8-ways-explained#stalemate`,[yE.TIMEOUT]:`https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#timeout`,[yE.TIMEVSINSUFFICIENT]:`https://www.chess.com/article/view/how-chess-games-can-end-8-wa
```

**Source references:** SRC-0781  
**URL references:** <https://www.chess.com/article/view/how-chess-games-can-end-8-ways-explained#timeout>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20823"></a>
## FND-20823: https://www.chess.com/article/view/how-to-be-a-good-sport-in-online-chess#StartingGames

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-to-be-a-good-sport-in-online-chess#StartingGames",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0187"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01692"
}

### Evidence

- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 8469.

```text
it takes to find an opponent. <a href="%href%" target="_blank">Learn More</a>`,{"%href%":`https://www.chess.com/article/view/how-to-be-a-good-sport-in-online-chess#StartingGames`});case`opponent_incident_logged`:return g(`Your opponent has been warned for abandoning 
```
- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 8793.

```text
ly playing other Poor Sports. <a href="%href%" target="_blank">Learn More</a>`,{"%href%":`https://www.chess.com/article/view/how-to-be-a-good-sport-in-online-chess#StartingGames`});case`game.rage_quit_detected`:return g(`Your opponent quit without resigning in a losi
```
- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 9133.

```text
d according to our <a href="%href%" target="_blank">Sportsmanship Policy</a>.`,{"%href%":`https://www.chess.com/article/view/how-to-be-a-good-sport-in-online-chess#StartingGames`});default:return}}var Z=e((()=>{v()}));function Ye(e){let t=X(e);t&&M(e,{component:`Cons
```

**Source references:** SRC-0187  
**URL references:** <https://www.chess.com/article/view/how-to-be-a-good-sport-in-online-chess#StartingGames>  
**Related findings:** FND-18200, FND-18201, FND-19434

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20824"></a>
## FND-20824: https://www.chess.com/article/view/how-to-capture-en-passant

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/article/view/how-to-capture-en-passant",
  "type": "page_or_route_candidate",
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
  "id": "URL-01693"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 179938.

```text
(e,t){e.element.remove(),t.delete(e.key)}var $te=r((()=>{})),ni,ri=r((()=>{ni={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.che
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1247956.

```text
tyleTag:!1,disableRookCastling:!1,assetPaths:{basePath:`https://www.chess.com`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`},pieceAnimationsEngi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195595.

```text
e,t){e.element.remove(),t.delete(e.key)}var Pte=r((()=>{})),Or,Fte=r((()=>{Or={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.che
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 561362.

```text
tyleTag:!1,disableRookCastling:!1,assetPaths:{basePath:`https://www.chess.com`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`},pieceAnimationsEngi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195595.

```text
e,t){e.element.remove(),t.delete(e.key)}var Pte=r((()=>{})),Or,Fte=r((()=>{Or={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.che
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 561362.

```text
tyleTag:!1,disableRookCastling:!1,assetPaths:{basePath:`https://www.chess.com`,enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`},pieceAnimationsEngi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/article/view/how-to-capture-en-passant>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20825"></a>
## FND-20825: https://www.chess.com/articles

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/articles",
  "type": "page_or_route_candidate",
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
  "id": "URL-01694"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19932.

```text
"sub":[],"badge":null},{"id":"community.articles","type":"link","label":"Articles","url":"https:\/\/www.chess.com\/articles","icon":{"name":"page-article","variant":"color"},"sub":[],"badge":null},{"id":"community
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 14896.

```text
"sub":[],"badge":null},{"id":"community.articles","type":"link","label":"Articles","url":"https:\/\/www.chess.com\/articles","icon":{"name":"page-article","variant":"color"},"sub":[],"badge":null},{"id":"community
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19932.

```text
"sub":[],"badge":null},{"id":"community.articles","type":"link","label":"Articles","url":"https:\/\/www.chess.com\/articles","icon":{"name":"page-article","variant":"color"},"sub":[],"badge":null},{"id":"community
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/articles>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20826"></a>
## FND-20826: https://www.chess.com/az/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/az/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01695"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7987.

```text
s://www.chess.com/ar/analysis" hreflang="ar" />
              <link rel="alternate" href="https://www.chess.com/az/analysis" hreflang="az" />
              <link rel="alternate" href="https://www.chess.com/be/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7987.

```text
s://www.chess.com/ar/analysis" hreflang="ar" />
              <link rel="alternate" href="https://www.chess.com/az/analysis" hreflang="az" />
              <link rel="alternate" href="https://www.chess.com/be/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/az/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20827"></a>
## FND-20827: https://www.chess.com/be/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/be/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01696"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8081.

```text
s://www.chess.com/az/analysis" hreflang="az" />
              <link rel="alternate" href="https://www.chess.com/be/analysis" hreflang="be" />
              <link rel="alternate" href="https://www.chess.com/bs/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8081.

```text
s://www.chess.com/az/analysis" hreflang="az" />
              <link rel="alternate" href="https://www.chess.com/be/analysis" hreflang="be" />
              <link rel="alternate" href="https://www.chess.com/bs/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/be/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20828"></a>
## FND-20828: https://www.chess.com/bg/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bg/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01697"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6577.

```text
s://www.chess.com/hy/analysis" hreflang="hy" />
              <link rel="alternate" href="https://www.chess.com/bg/analysis" hreflang="bg" />
              <link rel="alternate" href="https://www.chess.com/hr/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6577.

```text
s://www.chess.com/hy/analysis" hreflang="hy" />
              <link rel="alternate" href="https://www.chess.com/bg/analysis" hreflang="bg" />
              <link rel="alternate" href="https://www.chess.com/hr/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/bg/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20829"></a>
## FND-20829: https://www.chess.com/blogs

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/blogs",
  "type": "page_or_route_candidate",
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
  "id": "URL-01698"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20100.

```text
lor"},"sub":[],"badge":null},{"id":"community.blogs","type":"link","label":"Blogs","url":"https:\/\/www.chess.com\/blogs","icon":{"name":"page-blog","variant":"color"},"sub":[],"badge":null},{"id":"community.fo
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 15064.

```text
lor"},"sub":[],"badge":null},{"id":"community.blogs","type":"link","label":"Blogs","url":"https:\/\/www.chess.com\/blogs","icon":{"name":"page-blog","variant":"color"},"sub":[],"badge":null},{"id":"community.fo
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20100.

```text
lor"},"sub":[],"badge":null},{"id":"community.blogs","type":"link","label":"Blogs","url":"https:\/\/www.chess.com\/blogs","icon":{"name":"page-blog","variant":"color"},"sub":[],"badge":null},{"id":"community.fo
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/blogs>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20830"></a>
## FND-20830: https://www.chess.com/bn/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bn/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01699"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9987.

```text
w.chess.com/nl-BE/analysis" hreflang="nl-BE" />
              <link rel="alternate" href="https://www.chess.com/bn/analysis" hreflang="bn" />
              <link rel="alternate" href="https://www.chess.com/tk/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9987.

```text
w.chess.com/nl-BE/analysis" hreflang="nl-BE" />
              <link rel="alternate" href="https://www.chess.com/bn/analysis" hreflang="bn" />
              <link rel="alternate" href="https://www.chess.com/tk/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/bn/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20831"></a>
## FND-20831: https://www.chess.com/bs/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bs/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01700"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8175.

```text
s://www.chess.com/be/analysis" hreflang="be" />
              <link rel="alternate" href="https://www.chess.com/bs/analysis" hreflang="bs" />
              <link rel="alternate" href="https://www.chess.com/et/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8175.

```text
s://www.chess.com/be/analysis" hreflang="be" />
              <link rel="alternate" href="https://www.chess.com/bs/analysis" hreflang="bs" />
              <link rel="alternate" href="https://www.chess.com/et/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/bs/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.
