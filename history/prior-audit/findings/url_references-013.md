# url_references — findings 1201–1300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-20332"></a>
## FND-20332: /tournament/live/redirect-to

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/tournament/live/redirect-to",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0145"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01201"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 3264.

```text
[`https`]},web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|
```
- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 5727.

```text
ps`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 16088.

```text
[`https`]},web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|
```
- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 18551.

```text
ps`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 19668.

```text
om.routes,{web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|
```
- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 21207.

```text
ps`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

**Source references:** SRC-0145  
**URL references:** </tournament/live/redirect-to>  
**Related findings:** FND-18186, FND-18187, FND-18188

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20333"></a>
## FND-20333: /v2/game-review

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/v2/game-review",
  "type": "api_or_websocket_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0006",
    "SRC-0010",
    "SRC-0019",
    "SRC-0023",
    "SRC-0053"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01202"
}

### Evidence

- **SRC-0006** `chess-local-review-v0.1.6-quota-fix.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/a8c3dca7549b332cc78867ba216378165b16b6c3255ac2b2c5822fda511e35b5.js)
  Character offset 9298.

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```
- **SRC-0010** `chess-local-review-v0.1.7-cee-update.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/a8c3dca7549b332cc78867ba216378165b16b6c3255ac2b2c5822fda511e35b5.js)
  Character offset 9298.

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```
- **SRC-0019** `chess-local-review-v0.1.8-hide-debug-update.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 9395.

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```
- **SRC-0023** `chess-local-review-v0.1.9-measured-progress-update.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 9395.

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```
- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 9395.

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```

**Source references:** SRC-0006, SRC-0010, SRC-0019, SRC-0023, SRC-0053  
**URL references:** </v2/game-review>  
**Related findings:** FND-20334

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20334"></a>
## FND-20334: /v2/run-search

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/v2/run-search",
  "type": "api_or_websocket_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0006",
    "SRC-0010",
    "SRC-0019",
    "SRC-0023",
    "SRC-0053"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01203"
}

### Evidence

- **SRC-0006** `chess-local-review-v0.1.6-quota-fix.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/a8c3dca7549b332cc78867ba216378165b16b6c3255ac2b2c5822fda511e35b5.js)
  Character offset 9351.

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```
- **SRC-0010** `chess-local-review-v0.1.7-cee-update.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/a8c3dca7549b332cc78867ba216378165b16b6c3255ac2b2c5822fda511e35b5.js)
  Character offset 9351.

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```
- **SRC-0019** `chess-local-review-v0.1.8-hide-debug-update.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 9448.

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```
- **SRC-0023** `chess-local-review-v0.1.9-measured-progress-update.zip!/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 9448.

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```
- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 9448.

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```

**Source references:** SRC-0006, SRC-0010, SRC-0019, SRC-0023, SRC-0053  
**URL references:** </v2/run-search>  
**Related findings:** FND-20333

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20335"></a>
## FND-20335: /variants

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/variants",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0754",
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01204"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 7146.

```text
schemes:[`https`]},web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 7906.

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 21628.

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 22388.

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 94782.

```text
schemes:[`https`]},web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 95542.

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2170526.

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2171286.

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2593449.

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2595589.

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2933191.

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2934636.

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

**Source references:** SRC-0754, SRC-0781  
**URL references:** </variants>  
**Related findings:** FND-18126, FND-18132, FND-18166, FND-18117, FND-18118

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20336"></a>
## FND-20336: /verified

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/verified",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0177",
    "SRC-0178",
    "SRC-0191"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01205"
}

### Evidence

- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 865.

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 2349.

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 10519.

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 12003.

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0178** `research/play-chunks/client.b63508a8.TV1r5gKe8m.chunk.js` — [preserved redacted evidence](../evidence/text/058cb22094e269d06d05dba21718fcedcfb7af95d49e1777e4e763e7ae7bb9ab.js)
  Character offset 165.

```text
.routes||{},Object.assign(window.chesscom.routes,{web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0178** `research/play-chunks/client.b63508a8.TV1r5gKe8m.chunk.js` — [preserved redacted evidence](../evidence/text/058cb22094e269d06d05dba21718fcedcfb7af95d49e1777e4e763e7ae7bb9ab.js)
  Character offset 863.

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0178** `research/play-chunks/client.b63508a8.TV1r5gKe8m.chunk.js` — [preserved redacted evidence](../evidence/text/058cb22094e269d06d05dba21718fcedcfb7af95d49e1777e4e763e7ae7bb9ab.js)
  Character offset 3480.

```text
.routes||{},Object.assign(window.chesscom.routes,{web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0178** `research/play-chunks/client.b63508a8.TV1r5gKe8m.chunk.js` — [preserved redacted evidence](../evidence/text/058cb22094e269d06d05dba21718fcedcfb7af95d49e1777e4e763e7ae7bb9ab.js)
  Character offset 4178.

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 1651.

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 2349.

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 10211.

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 11695.

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

**Source references:** SRC-0177, SRC-0178, SRC-0191  
**URL references:** </verified>  
**Related findings:** FND-18183, FND-18184, FND-18198, FND-18199, FND-19434

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20337"></a>
## FND-20337: /vite/${e}

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/vite/${e}",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01206"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 310533.

```text
e(e)||``}var zd=r((()=>{}));function Nme(e){let t=document.querySelector(`link[data-href*="/vite/${e}"]`);if(t)return t.setAttribute(`href`,t.getAttribute(`data-href`)),t.removeAttribute(`data
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 314620.

```text
e(e)||``}var Xd=r((()=>{}));function ude(e){let t=document.querySelector(`link[data-href*="/vite/${e}"]`);if(t)return t.setAttribute(`href`,t.getAttribute(`data-href`)),t.removeAttribute(`data
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 314620.

```text
e(e)||``}var Xd=r((()=>{}));function ude(e){let t=document.querySelector(`link[data-href*="/vite/${e}"]`);if(t)return t.setAttribute(`href`,t.getAttribute(`data-href`)),t.removeAttribute(`data
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** </vite/${e}>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20338"></a>
## FND-20338: /vote

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/vote",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
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
  "id": "URL-01207"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 17657.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 148969.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 17657.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 148969.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 80193.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 978882.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 113174.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2700313.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 113174.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2700313.

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** </vote>  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20339"></a>
## FND-20339: /votechess/seek

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/votechess/seek",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01208"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 28535.

```text
https`]},web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 474630.

```text
https`]},web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2966434.

```text
.routes,{web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

**Source references:** SRC-0781  
**URL references:** </votechess/seek>  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20340"></a>
## FND-20340: /votechess/seek/data

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "/votechess/seek/data",
  "type": "page_or_route_candidate",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0145"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01209"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 996.

```text
s`]},web_votechess_get_group_seek_data:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```
- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 11634.

```text
tes,{web_votechess_get_group_seek_data:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

**Source references:** SRC-0145  
**URL references:** </votechess/seek/data>  
**Related findings:** FND-18186, FND-18187, FND-18188

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20341"></a>
## FND-20341: bundles/app/js/engine/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/",
  "type": "external_or_documentation",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-2048"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01210"
}

### Evidence

- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 13420.

```text
co.json`
unless the `analysis_engine_skip_book` feature flag is set.

Files shipped under `bundles/app/js/engine/`: `stockfish-nnue-15.1{,-no-Worker,-no-simd}.{js,wasm}`,
`stockfish-nnue-16{,-no-Worker,-n
```

**Source references:** SRC-2048  
**URL references:** <bundles/app/js/engine/>  
**Related findings:** FND-00217, FND-00218, FND-00219

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20342"></a>
## FND-20342: bundles/app/js/engine/book-small.json

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/book-small.json",
  "type": "external_or_documentation",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0064",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 200; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01211",
  "historical_http_observations": [
    {
      "target_literal": "bundles/app/js/engine/book-small.json",
      "http_status": 200,
      "size_download": 2140353,
      "content_type_and_optional_elapsed": "application/json",
      "source_id": "SRC-0204",
      "line": 10,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0064** `fetch-assets.sh` — [preserved redacted evidence](../evidence/text/4fd21605ac735ee70e6717867eb17d057b430580a6adf2918d177c00aef42751.sh)
  Character offset 2334.

```text
-5af11540bbfe.nnue' "$D/stockfish/nn-5af11540bbfe.nnue" &
wait
# --- opening book ---
get 'bundles/app/js/engine/book-small.json' "$D/book/book-small.json" &
wait
echo "=== done ==="

```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 277837.

```text
on Od(e){return e.filter((e,t,n)=>n.indexOf(e)===t)}var kd=r((()=>{})),Ad,pme=r((()=>{Ad={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bun
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 277877.

```text
xOf(e)===t)}var kd=r((()=>{})),Ad,pme=r((()=>{Ad={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1914938.

```text
res?.includes(`analysis_engine_skip_book`)?void 0:yN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),QJ={[KJ.STOCKFISH_NNUE]:{name:qJ?.full?.name||
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282742.

```text
()=>{})),Ad,jd=r((()=>{Ad=(e,t)=>[...e].sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bun
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282782.

```text
sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1330340.

```text
res?.includes(`analysis_engine_skip_book`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282742.

```text
()=>{})),Ad,jd=r((()=>{Ad=(e,t)=>[...e].sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bun
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282782.

```text
sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1330340.

```text
res?.includes(`analysis_engine_skip_book`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||
```

**Source references:** SRC-0064, SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/book-small.json>  
**Related findings:** FND-18976, FND-20462, FND-18117, FND-18118, FND-18125

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20343"></a>
## FND-20343: bundles/app/js/engine/books/${e}.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/${e}.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01212"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2716893.

```text
`${Fxt}${encodeURIComponent(e)}`:zN(t?.includes(`book_binaries_from_npm_data_eco_webapp`)?`bundles/app/js/engine/books/${e}.bin`:`bundles/app/js/vendor/jschessengine/books/personalities/${e}.bin`,!1)}var Fxt,Ixt=r((()=
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2716893.

```text
`${Fxt}${encodeURIComponent(e)}`:zN(t?.includes(`book_binaries_from_npm_data_eco_webapp`)?`bundles/app/js/engine/books/${e}.bin`:`bundles/app/js/vendor/jschessengine/books/personalities/${e}.bin`,!1)}var Fxt,Ixt=r((()=
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/${e}.bin>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20344"></a>
## FND-20344: bundles/app/js/engine/books/aggressive.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/aggressive.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01213"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 277917.

```text
(()=>{Ad={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstei
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 277962.

```text
son":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rub
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282822.

```text
(()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstei
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282867.

```text
son":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rub
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282822.

```text
(()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstei
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282867.

```text
son":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rub
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/aggressive.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20345"></a>
## FND-20345: bundles/app/js/engine/books/akiba_rubinstein.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/akiba_rubinstein.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01214"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278007.

```text
"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278058.

```text
es/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282912.

```text
"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282963.

```text
es/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282912.

```text
"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 282963.

```text
es/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/akiba_rubinstein.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20346"></a>
## FND-20346: bundles/app/js/engine/books/alekhine.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/alekhine.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01215"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278109.

```text
/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278152.

```text
dles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283014.

```text
/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283057.

```text
dles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283014.

```text
/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283057.

```text
dles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/alekhine.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20347"></a>
## FND-20347: bundles/app/js/engine/books/alexandra_botez.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/alexandra_botez.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01216"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278195.

```text
in`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278245.

```text
ndles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexan
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283100.

```text
in`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283150.

```text
ndles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexan
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283100.

```text
in`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283150.

```text
ndles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexan
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/alexandra_botez.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20348"></a>
## FND-20348: bundles/app/js/engine/books/alexandra_kosteniuk.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/alexandra_kosteniuk.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01217"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278295.

```text
pp/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_h
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278349.

```text
s/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hamble
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283200.

```text
pp/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_h
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283254.

```text
s/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hamble
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283200.

```text
pp/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283254.

```text
s/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hamble
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/alexandra_kosteniuk.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20349"></a>
## FND-20349: bundles/app/js/engine/books/aman_hambleton.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/aman_hambleton.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01218"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278403.

```text
gine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_bote
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278452.

```text
js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283308.

```text
gine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_bote
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283357.

```text
js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283308.

```text
gine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_bote
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283357.

```text
js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/aman_hambleton.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20350"></a>
## FND-20350: bundles/app/js/engine/books/andrea_botez.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/andrea_botez.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01219"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278501.

```text
/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278548.

```text
es/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283406.

```text
/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283453.

```text
es/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283406.

```text
/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283453.

```text
es/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/andrea_botez.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20351"></a>
## FND-20351: bundles/app/js/engine/books/anish_giri.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/anish_giri.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01220"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278595.

```text
dles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278640.

```text
undles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramlin
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283500.

```text
dles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283545.

```text
undles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramlin
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283500.

```text
dles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283545.

```text
undles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramlin
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/anish_giri.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20352"></a>
## FND-20352: bundles/app/js/engine/books/anna_cramling.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/anna_cramling.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01221"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278685.

```text
"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278733.

```text
ndles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283590.

```text
"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283638.

```text
ndles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283590.

```text
"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283638.

```text
ndles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/anna_cramling.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20353"></a>
## FND-20353: bundles/app/js/engine/books/anna_muzychuk.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/anna_muzychuk.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01222"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278781.

```text
es/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278829.

```text
es/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283686.

```text
es/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283734.

```text
es/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283686.

```text
es/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283734.

```text
es/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/anna_muzychuk.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20354"></a>
## FND-20354: bundles/app/js/engine/books/anna_rudolf.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/anna_rudolf.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01223"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278877.

```text
es/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278923.

```text
dles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283782.

```text
es/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283828.

```text
dles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283782.

```text
es/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283828.

```text
dles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/anna_rudolf.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20355"></a>
## FND-20355: bundles/app/js/engine/books/anthony_levin.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/anthony_levin.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01224"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 278969.

```text
undles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_mile
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279017.

```text
dles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_mile
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283874.

```text
undles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_mile
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283922.

```text
dles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_mile
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283874.

```text
undles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_mile
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283922.

```text
dles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_mile
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/anthony_levin.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20356"></a>
## FND-20356: bundles/app/js/engine/books/anthony_miles.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/anthony_miles.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01225"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279065.

```text
es/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279113.

```text
es/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimz
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283970.

```text
es/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284018.

```text
es/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 283970.

```text
es/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284018.

```text
es/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimz
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/anthony_miles.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20357"></a>
## FND-20357: bundles/app/js/engine/books/aron_nimzowitsch.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/aron_nimzowitsch.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01226"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279161.

```text
es/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_r
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279212.

```text
app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284066.

```text
es/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_r
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284117.

```text
app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284066.

```text
es/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_r
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284117.

```text
app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/aron_nimzowitsch.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20358"></a>
## FND-20358: bundles/app/js/engine/books/avigail_rosenthal.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/avigail_rosenthal.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01227"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279263.

```text
/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279315.

```text
js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284168.

```text
/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284220.

```text
js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284168.

```text
/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284220.

```text
js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/avigail_rosenthal.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20359"></a>
## FND-20359: bundles/app/js/engine/books/balanced.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/balanced.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01228"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279367.

```text
s/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279410.

```text
les/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284272.

```text
s/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284315.

```text
les/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284272.

```text
s/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284315.

```text
les/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/balanced.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20360"></a>
## FND-20360: bundles/app/js/engine/books/beginner.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/beginner.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01229"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279453.

```text
in`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin"
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279496.

```text
in":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284358.

```text
in`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284401.

```text
in":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284358.

```text
in`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284401.

```text
in":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/beginner.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20361"></a>
## FND-20361: bundles/app/js/engine/books/benjamin_bok.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/benjamin_bok.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01230"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279539.

```text
in`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_fine
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279586.

```text
`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284444.

```text
in`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_fine
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284491.

```text
`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284444.

```text
in`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_fine
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284491.

```text
`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/benjamin_bok.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20362"></a>
## FND-20362: bundles/app/js/engine/books/benjamin_finegold.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/benjamin_finegold.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01231"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279633.

```text
dles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_lar
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279685.

```text
app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284538.

```text
dles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_lar
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284590.

```text
app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284538.

```text
dles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_lar
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284590.

```text
app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/benjamin_finegold.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20363"></a>
## FND-20363: bundles/app/js/engine/books/bent_larsen.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/bent_larsen.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01232"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279737.

```text
s/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279783.

```text
/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wou
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284642.

```text
s/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284688.

```text
/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wou
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284642.

```text
s/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284688.

```text
/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wou
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/bent_larsen.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20364"></a>
## FND-20364: bundles/app/js/engine/books/bikfoot_wouter.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/bikfoot_wouter.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01233"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279829.

```text
undles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279878.

```text
les/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/ap
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284734.

```text
undles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284783.

```text
les/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/ap
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284734.

```text
undles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284783.

```text
les/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/ap
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/bikfoot_wouter.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20365"></a>
## FND-20365: bundles/app/js/engine/books/book.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/book.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01234"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279927.

```text
/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundl
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 279966.

```text
":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284832.

```text
/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundl
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284871.

```text
":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284832.

```text
/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundl
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284871.

```text
":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/book.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20366"></a>
## FND-20366: bundles/app/js/engine/books/botvinnik.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/botvinnik.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01235"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280005.

```text
wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280049.

```text
k.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284910.

```text
wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284954.

```text
k.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284910.

```text
wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284954.

```text
k.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/botvinnik.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20367"></a>
## FND-20367: bundles/app/js/engine/books/capablanca.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/capablanca.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01236"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280093.

```text
`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280138.

```text
:`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evan
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284998.

```text
`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285043.

```text
:`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evan
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 284998.

```text
`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285043.

```text
:`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evan
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/capablanca.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20368"></a>
## FND-20368: bundles/app/js/engine/books/captain_evans.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/captain_evans.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01237"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280183.

```text
"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin"
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280231.

```text
ndles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bund
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285088.

```text
"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285136.

```text
ndles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bund
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285088.

```text
"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285136.

```text
ndles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bund
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/captain_evans.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20369"></a>
## FND-20369: bundles/app/js/engine/books/carlsen.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/carlsen.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01238"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280279.

```text
es/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280321.

```text
`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285184.

```text
es/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285226.

```text
`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285184.

```text
es/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285226.

```text
`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/carlsen.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20370"></a>
## FND-20370: bundles/app/js/engine/books/cccopenings.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/cccopenings.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01239"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280363.

```text
.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_puli
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280409.

```text
":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christia
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285268.

```text
.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_puli
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285314.

```text
":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christia
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285268.

```text
.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_puli
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285314.

```text
":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christia
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/cccopenings.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20371"></a>
## FND-20371: bundles/app/js/engine/books/christian_pulisic.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/christian_pulisic.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01240"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280455.

```text
undles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classica
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280507.

```text
/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285360.

```text
undles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classica
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285412.

```text
/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285360.

```text
undles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classica
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285412.

```text
/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/christian_pulisic.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20372"></a>
## FND-20372: bundles/app/js/engine/books/classical.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/classical.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01241"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280559.

```text
s/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280603.

```text
es/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285464.

```text
s/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285508.

```text
es/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285464.

```text
s/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285508.

```text
es/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/classical.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20373"></a>
## FND-20373: bundles/app/js/engine/books/dan_rozovsky.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/dan_rozovsky.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01242"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280647.

```text
`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_narodi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280694.

```text
bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_n
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285552.

```text
`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_narodi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285599.

```text
bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_n
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285552.

```text
`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_narodi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285599.

```text
bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_n
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/dan_rozovsky.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20374"></a>
## FND-20374: bundles/app/js/engine/books/daniel_naroditsky.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/daniel_naroditsky.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01243"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280741.

```text
dles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_mo
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280793.

```text
app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285646.

```text
dles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_mo
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285698.

```text
app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285646.

```text
dles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_mo
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285698.

```text
app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/daniel_naroditsky.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20375"></a>
## FND-20375: bundles/app/js/engine/books/daryl_morey.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/daryl_morey.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01244"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280845.

```text
s/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280891.

```text
/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285750.

```text
s/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285796.

```text
/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285750.

```text
s/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285796.

```text
/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/daryl_morey.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20376"></a>
## FND-20376: bundles/app/js/engine/books/david_howell.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/david_howell.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01245"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280937.

```text
undles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 280984.

```text
ndles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285842.

```text
undles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285889.

```text
ndles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285842.

```text
undles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285889.

```text
ndles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/david_howell.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20377"></a>
## FND-20377: bundles/app/js/engine/books/dawid_czerw.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/dawid_czerw.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01246"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281031.

```text
dles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bun
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281077.

```text
ndles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/ap
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285936.

```text
dles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bun
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285982.

```text
ndles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/ap
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285936.

```text
dles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bun
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 285982.

```text
ndles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/ap
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/dawid_czerw.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20378"></a>
## FND-20378: bundles/app/js/engine/books/ding.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/ding.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01247"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281123.

```text
undles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281162.

```text
bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286028.

```text
undles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286067.

```text
bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286028.

```text
undles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286067.

```text
bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/ding.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20379"></a>
## FND-20379: bundles/app/js/engine/books/dodge_coates.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/dodge_coates.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01248"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281201.

```text
_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281248.

```text
in":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittma
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286106.

```text
_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286153.

```text
in":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittma
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286106.

```text
_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286153.

```text
in":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittma
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/dodge_coates.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20380"></a>
## FND-20380: bundles/app/js/engine/books/dylan_rittman.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/dylan_rittman.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01249"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281295.

```text
dles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281343.

```text
les/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/ap
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286200.

```text
dles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286248.

```text
les/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/ap
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286200.

```text
dles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286248.

```text
les/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/ap
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/dylan_rittman.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20381"></a>
## FND-20381: bundles/app/js/engine/books/eco.json

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/eco.json",
  "type": "external_or_documentation",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165",
    "SRC-2048"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01250"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281391.

```text
es/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bun
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281430.

```text
n":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1914978.

```text
`)?void 0:yN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),QJ={[KJ.STOCKFISH_NNUE]:{name:qJ?.full?.name||`Stockfish 16.1`,description:L(`%filesi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286296.

```text
es/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bun
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286335.

```text
n":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1330380.

```text
`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||`Stockfish 16.1`,description:z(`%filesi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2686118.

```text
unction Xbt(){let e=window.context?.environment===`test`?`bundles/app/js/engine/eco.json`:`bundles/app/js/engine/books/eco.json`;return`${self.location.origin}${zN(e,!1)}`}var Zbt=r((()=>{BN()}));function Qbt(e=U2.game
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286296.

```text
es/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bun
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286335.

```text
n":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1330380.

```text
`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||`Stockfish 16.1`,description:z(`%filesi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2686118.

```text
unction Xbt(){let e=window.context?.environment===`test`?`bundles/app/js/engine/eco.json`:`bundles/app/js/engine/books/eco.json`;return`${self.location.origin}${zN(e,!1)}`}var Zbt=r((()=>{BN()}));function Qbt(e=U2.game
```
- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
  Character offset 13300.

```text
display name `Stockfish 16.1`, `66MB`,
`paths.settings: { Threads: '1' }`, `pathToBook` = `bundles/app/js/engine/books/eco.json`
unless the `analysis_engine_skip_book` feature flag is set.

Files shipped under `bundles
```

**Source references:** SRC-0781, SRC-1137, SRC-1165, SRC-2048  
**URL references:** <bundles/app/js/engine/books/eco.json>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20382"></a>
## FND-20382: bundles/app/js/engine/books/eric_hansen.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/eric_hansen.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01251"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281469.

```text
ittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281515.

```text
son":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebes
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286374.

```text
ittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286420.

```text
son":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebes
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286374.

```text
ittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286420.

```text
son":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebes
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/eric_hansen.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20383"></a>
## FND-20383: bundles/app/js/engine/books/erik_allebest.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/erik_allebest.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01252"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281561.

```text
undles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzge
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281609.

```text
dles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzge
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286466.

```text
undles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzge
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286514.

```text
dles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzge
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286466.

```text
undles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzge
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286514.

```text
dles/app/js/engine/books/eric_hansen.bin`,"bundles/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzge
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/erik_allebest.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20384"></a>
## FND-20384: bundles/app/js/engine/books/ethan_metzger.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/ethan_metzger.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01253"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281657.

```text
es/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281705.

```text
es/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/ap
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286562.

```text
es/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286610.

```text
es/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/ap
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286562.

```text
es/app/js/engine/books/erik_allebest.bin":`bundles/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286610.

```text
es/app/js/engine/books/erik_allebest.bin`,"bundles/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/ap
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/ethan_metzger.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20385"></a>
## FND-20385: bundles/app/js/engine/books/euwe.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/euwe.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01254"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281753.

```text
es/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundle
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281792.

```text
n":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286658.

```text
es/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundle
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286697.

```text
n":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286658.

```text
es/app/js/engine/books/ethan_metzger.bin":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundle
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286697.

```text
n":`bundles/app/js/engine/books/ethan_metzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/euwe.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20386"></a>
## FND-20386: bundles/app/js/engine/books/f-pawner.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/f-pawner.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01255"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281831.

```text
etzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281874.

```text
we.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_ca
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286736.

```text
etzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286779.

```text
we.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_ca
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286736.

```text
etzger.bin`,"bundles/app/js/engine/books/euwe.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286779.

```text
we.bin":`bundles/app/js/engine/books/euwe.bin`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_ca
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/f-pawner.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20387"></a>
## FND-20387: bundles/app/js/engine/books/fabiano_caruana.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/fabiano_caruana.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01256"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281917.

```text
in`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 281967.

```text
ndles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bund
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286822.

```text
in`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286872.

```text
ndles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bund
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286822.

```text
in`,"bundles/app/js/engine/books/f-pawner.bin":`bundles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286872.

```text
ndles/app/js/engine/books/f-pawner.bin`,"bundles/app/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bund
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/fabiano_caruana.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20388"></a>
## FND-20388: bundles/app/js/engine/books/fischer.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/fischer.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01257"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282017.

```text
pp/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundl
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282059.

```text
undles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundle
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286922.

```text
pp/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundl
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286964.

```text
undles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundle
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286922.

```text
pp/js/engine/books/fabiano_caruana.bin":`bundles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundl
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 286964.

```text
undles/app/js/engine/books/fabiano_caruana.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundle
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/fischer.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20389"></a>
## FND-20389: bundles/app/js/engine/books/gambit.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/gambit.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01258"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282101.

```text
.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bun
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282142.

```text
r.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287006.

```text
.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bun
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287047.

```text
r.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287006.

```text
.bin`,"bundles/app/js/engine/books/fischer.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bun
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287047.

```text
r.bin":`bundles/app/js/engine/books/fischer.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/gambit.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20390"></a>
## FND-20390: bundles/app/js/engine/books/hou_yifan.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/hou_yifan.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01259"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282183.

```text
er.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_bur
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282227.

```text
bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunte
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287088.

```text
er.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_bur
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287132.

```text
bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunte
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287088.

```text
er.bin`,"bundles/app/js/engine/books/gambit.bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_bur
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287132.

```text
bin":`bundles/app/js/engine/books/gambit.bin`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunte
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/hou_yifan.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20391"></a>
## FND-20391: bundles/app/js/engine/books/hunter_klotz_burwell.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/hunter_klotz_burwell.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01260"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282271.

```text
`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_n
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282326.

```text
app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nep
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287176.

```text
`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_n
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287231.

```text
app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nep
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287176.

```text
`,"bundles/app/js/engine/books/hou_yifan.bin":`bundles/app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_n
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287231.

```text
app/js/engine/books/hou_yifan.bin`,"bundles/app/js/engine/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nep
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/hunter_klotz_burwell.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20392"></a>
## FND-20392: bundles/app/js/engine/books/ian_nepomniachtchi.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/ian_nepomniachtchi.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01261"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282381.

```text
ne/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282434.

```text
gine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundle
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287286.

```text
ne/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287339.

```text
gine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundle
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287286.

```text
ne/books/hunter_klotz_burwell.bin":`bundles/app/js/engine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287339.

```text
gine/books/hunter_klotz_burwell.bin`,"bundles/app/js/engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundle
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/ian_nepomniachtchi.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20393"></a>
## FND-20393: bundles/app/js/engine/books/indian.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/indian.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01262"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282487.

```text
engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282528.

```text
dles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287392.

```text
engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287433.

```text
dles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287392.

```text
engine/books/ian_nepomniachtchi.bin":`bundles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287433.

```text
dles/app/js/engine/books/ian_nepomniachtchi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/indian.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20394"></a>
## FND-20394: bundles/app/js/engine/books/irina_krush.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/irina_krush.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01263"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282569.

```text
hi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282615.

```text
n":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287474.

```text
hi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287520.

```text
n":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287474.

```text
hi.bin`,"bundles/app/js/engine/books/indian.bin":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287520.

```text
n":`bundles/app/js/engine/books/indian.bin`,"bundles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/irina_krush.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20395"></a>
## FND-20395: bundles/app/js/engine/books/james_canty.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/james_canty.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01264"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282661.

```text
undles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282707.

```text
undles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287566.

```text
undles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287612.

```text
undles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287566.

```text
undles/app/js/engine/books/irina_krush.bin":`bundles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287612.

```text
undles/app/js/engine/books/irina_krush.bin`,"bundles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/james_canty.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20396"></a>
## FND-20396: bundles/app/js/engine/books/jay_severson.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/jay_severson.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01265"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282753.

```text
undles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282800.

```text
ndles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287658.

```text
undles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287705.

```text
ndles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287658.

```text
undles/app/js/engine/books/james_canty.bin":`bundles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287705.

```text
ndles/app/js/engine/books/james_canty.bin`,"bundles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/jay_severson.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20397"></a>
## FND-20397: bundles/app/js/engine/books/jeremy_kane.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/jeremy_kane.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01266"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282847.

```text
dles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_canno
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282893.

```text
ndles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287752.

```text
dles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_canno
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287798.

```text
ndles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287752.

```text
dles/app/js/engine/books/jay_severson.bin":`bundles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_canno
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287798.

```text
ndles/app/js/engine/books/jay_severson.bin`,"bundles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/jeremy_kane.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20398"></a>
## FND-20398: bundles/app/js/engine/books/jonathan_cannon.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/jonathan_cannon.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01267"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282939.

```text
undles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_vot
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 282989.

```text
es/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287844.

```text
undles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_vot
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287894.

```text
es/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287844.

```text
undles/app/js/engine/books/jeremy_kane.bin":`bundles/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_vot
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287894.

```text
es/app/js/engine/books/jeremy_kane.bin`,"bundles/app/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/jonathan_cannon.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20399"></a>
## FND-20399: bundles/app/js/engine/books/joseph_votto.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/joseph_votto.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01268"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283039.

```text
pp/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283086.

```text
s/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287944.

```text
pp/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287991.

```text
s/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287944.

```text
pp/js/engine/books/jonathan_cannon.bin":`bundles/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 287991.

```text
s/app/js/engine/books/jonathan_cannon.bin`,"bundles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/joseph_votto.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20400"></a>
## FND-20400: bundles/app/js/engine/books/judit_polgar.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/judit_polgar.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01269"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283133.

```text
dles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283180.

```text
dles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288038.

```text
dles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288085.

```text
dles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288038.

```text
dles/app/js/engine/books/joseph_votto.bin":`bundles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288085.

```text
dles/app/js/engine/books/joseph_votto.bin`,"bundles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/judit_polgar.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20401"></a>
## FND-20401: bundles/app/js/engine/books/julien_song.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/julien_song.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01270"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283227.

```text
dles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283273.

```text
ndles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundle
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288132.

```text
dles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288178.

```text
ndles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundle
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288132.

```text
dles/app/js/engine/books/judit_polgar.bin":`bundles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288178.

```text
ndles/app/js/engine/books/judit_polgar.bin`,"bundles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundle
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/julien_song.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20402"></a>
## FND-20402: bundles/app/js/engine/books/karpov.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/karpov.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01271"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283319.

```text
undles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bund
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283360.

```text
n":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288224.

```text
undles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bund
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288265.

```text
n":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288224.

```text
undles/app/js/engine/books/julien_song.bin":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bund
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288265.

```text
n":`bundles/app/js/engine/books/julien_song.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/karpov.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20403"></a>
## FND-20403: bundles/app/js/engine/books/kasparov.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/kasparov.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01272"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283401.

```text
ng.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin"
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283444.

```text
.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288306.

```text
ng.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288349.

```text
.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288306.

```text
ng.bin`,"bundles/app/js/engine/books/karpov.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288349.

```text
.bin":`bundles/app/js/engine/books/karpov.bin`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/kasparov.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20404"></a>
## FND-20404: bundles/app/js/engine/books/kassa_korley.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/kassa_korley.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01273"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283487.

```text
in`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilbe
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283534.

```text
`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wil
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288392.

```text
in`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilbe
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288439.

```text
`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wil
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288392.

```text
in`,"bundles/app/js/engine/books/kasparov.bin":`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilbe
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288439.

```text
`bundles/app/js/engine/books/kasparov.bin`,"bundles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wil
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/kassa_korley.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20405"></a>
## FND-20405: bundles/app/js/engine/books/kenneth_wilber.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/kenneth_wilber.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01274"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283581.

```text
dles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283630.

```text
es/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288486.

```text
dles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288535.

```text
es/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288486.

```text
dles/app/js/engine/books/kassa_korley.bin":`bundles/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288535.

```text
es/app/js/engine/books/kassa_korley.bin`,"bundles/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/kenneth_wilber.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20406"></a>
## FND-20406: bundles/app/js/engine/books/kevin_bordi.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/kevin_bordi.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01275"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283679.

```text
/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283725.

```text
les/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundle
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288584.

```text
/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288630.

```text
les/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundle
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288584.

```text
/app/js/engine/books/kenneth_wilber.bin":`bundles/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288630.

```text
les/app/js/engine/books/kenneth_wilber.bin`,"bundles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundle
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/kevin_bordi.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20407"></a>
## FND-20407: bundles/app/js/engine/books/komodo.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/komodo.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01276"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283771.

```text
undles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bund
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283812.

```text
n":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288676.

```text
undles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bund
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288717.

```text
n":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288676.

```text
undles/app/js/engine/books/kevin_bordi.bin":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bund
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288717.

```text
n":`bundles/app/js/engine/books/kevin_bordi.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/komodo.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20408"></a>
## FND-20408: bundles/app/js/engine/books/korchnoi.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/korchnoi.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01277"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283853.

```text
di.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitaria
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283896.

```text
.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288758.

```text
di.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitaria
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288801.

```text
.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288758.

```text
di.bin`,"bundles/app/js/engine/books/komodo.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitaria
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288801.

```text
.bin":`bundles/app/js/engine/books/komodo.bin`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/korchnoi.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20409"></a>
## FND-20409: bundles/app/js/engine/books/krikor_mekhitarian.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/krikor_mekhitarian.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01278"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283939.

```text
in`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 283992.

```text
es/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundle
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288844.

```text
in`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288897.

```text
es/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundle
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288844.

```text
in`,"bundles/app/js/engine/books/korchnoi.bin":`bundles/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288897.

```text
es/app/js/engine/books/korchnoi.bin`,"bundles/app/js/engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundle
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/krikor_mekhitarian.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20410"></a>
## FND-20410: bundles/app/js/engine/books/lasker.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/lasker.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01279"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284045.

```text
engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284086.

```text
dles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288950.

```text
engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288991.

```text
dles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288950.

```text
engine/books/krikor_mekhitarian.bin":`bundles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 288991.

```text
dles/app/js/engine/books/krikor_mekhitarian.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/lasker.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20411"></a>
## FND-20411: bundles/app/js/engine/books/leo_stokes.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/leo_stokes.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01280"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284127.

```text
an.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284172.

```text
in":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronia
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289032.

```text
an.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289077.

```text
in":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronia
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289032.

```text
an.bin`,"bundles/app/js/engine/books/lasker.bin":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289077.

```text
in":`bundles/app/js/engine/books/lasker.bin`,"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronia
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/leo_stokes.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20412"></a>
## FND-20412: bundles/app/js/engine/books/levon_aronian.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/levon_aronian.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01281"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284217.

```text
"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284265.

```text
ndles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289122.

```text
"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289170.

```text
ndles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289122.

```text
"bundles/app/js/engine/books/leo_stokes.bin":`bundles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289170.

```text
ndles/app/js/engine/books/leo_stokes.bin`,"bundles/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/levon_aronian.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20413"></a>
## FND-20413: bundles/app/js/engine/books/levy_rozman.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/levy_rozman.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01282"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284313.

```text
es/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284359.

```text
dles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289218.

```text
es/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289264.

```text
dles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289218.

```text
es/app/js/engine/books/levon_aronian.bin":`bundles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289264.

```text
dles/app/js/engine/books/levon_aronian.bin`,"bundles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/levy_rozman.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20414"></a>
## FND-20414: bundles/app/js/engine/books/luis_fernandez_siles.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/luis_fernandez_siles.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01283"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284405.

```text
undles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/marti
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284460.

```text
p/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289310.

```text
undles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/marti
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289365.

```text
p/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289310.

```text
undles/app/js/engine/books/levy_rozman.bin":`bundles/app/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/marti
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289365.

```text
p/js/engine/books/levy_rozman.bin`,"bundles/app/js/engine/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/luis_fernandez_siles.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20415"></a>
## FND-20415: bundles/app/js/engine/books/martin_enev.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/martin_enev.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01284"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284515.

```text
ne/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284561.

```text
p/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289420.

```text
ne/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289466.

```text
p/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289420.

```text
ne/books/luis_fernandez_siles.bin":`bundles/app/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289466.

```text
p/js/engine/books/luis_fernandez_siles.bin`,"bundles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/martin_enev.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20416"></a>
## FND-20416: bundles/app/js/engine/books/matt_turner.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/matt_turner.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01285"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284607.

```text
undles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284653.

```text
undles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ash
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289512.

```text
undles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289558.

```text
undles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ash
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289512.

```text
undles/app/js/engine/books/martin_enev.bin":`bundles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289558.

```text
undles/app/js/engine/books/martin_enev.bin`,"bundles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ash
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/matt_turner.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20417"></a>
## FND-20417: bundles/app/js/engine/books/maurice_ashley.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/maurice_ashley.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01286"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284699.

```text
undles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_gre
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284748.

```text
les/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_gre
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289604.

```text
undles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_gre
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289653.

```text
les/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_gre
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289604.

```text
undles/app/js/engine/books/matt_turner.bin":`bundles/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_gre
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289653.

```text
les/app/js/engine/books/matt_turner.bin`,"bundles/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_gre
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/maurice_ashley.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20418"></a>
## FND-20418: bundles/app/js/engine/books/michael_greene.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/michael_greene.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01287"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284797.

```text
/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284846.

```text
/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289702.

```text
/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289751.

```text
/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289702.

```text
/app/js/engine/books/maurice_ashley.bin":`bundles/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289751.

```text
/app/js/engine/books/maurice_ashley.bin`,"bundles/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/michael_greene.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20419"></a>
## FND-20419: bundles/app/js/engine/books/mike_klein.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/mike_klein.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01288"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284895.

```text
/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284940.

```text
dles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289800.

```text
/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289845.

```text
dles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289800.

```text
/app/js/engine/books/michael_greene.bin":`bundles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289845.

```text
dles/app/js/engine/books/michael_greene.bin`,"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/mike_klein.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20420"></a>
## FND-20420: bundles/app/js/engine/books/nakamura.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/nakamura.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01289"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 284985.

```text
"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285028.

```text
":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289890.

```text
"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289933.

```text
":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289890.

```text
"bundles/app/js/engine/books/mike_klein.bin":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289933.

```text
":`bundles/app/js/engine/books/mike_klein.bin`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/nakamura.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20421"></a>
## FND-20421: bundles/app/js/engine/books/nakamura_classic.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/nakamura_classic.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01290"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285071.

```text
in`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.b
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285122.

```text
dles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bund
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289976.

```text
in`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.b
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290027.

```text
dles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bund
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 289976.

```text
in`,"bundles/app/js/engine/books/nakamura.bin":`bundles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.b
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290027.

```text
dles/app/js/engine/books/nakamura.bin`,"bundles/app/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bund
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/nakamura_classic.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20422"></a>
## FND-20422: bundles/app/js/engine/books/naritav.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/naritav.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01291"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285173.

```text
/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285215.

```text
ndles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gur
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290078.

```text
/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290120.

```text
ndles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gur
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290078.

```text
/js/engine/books/nakamura_classic.bin":`bundles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290120.

```text
ndles/app/js/engine/books/nakamura_classic.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gur
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/naritav.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20423"></a>
## FND-20423: bundles/app/js/engine/books/naycir_gurpinar.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/naycir_gurpinar.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01292"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285257.

```text
.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285307.

```text
undles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bund
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290162.

```text
.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290212.

```text
undles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bund
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290162.

```text
.bin`,"bundles/app/js/engine/books/naritav.bin":`bundles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290212.

```text
undles/app/js/engine/books/naritav.bin`,"bundles/app/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bund
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/naycir_gurpinar.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20424"></a>
## FND-20424: bundles/app/js/engine/books/offbeat.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/offbeat.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01293"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285357.

```text
pp/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285399.

```text
undles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksand
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290262.

```text
pp/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290304.

```text
undles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksand
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290262.

```text
pp/js/engine/books/naycir_gurpinar.bin":`bundles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290304.

```text
undles/app/js/engine/books/naycir_gurpinar.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksand
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/offbeat.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20425"></a>
## FND-20425: bundles/app/js/engine/books/oleksandr_bortnyk.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/oleksandr_bortnyk.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01294"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285441.

```text
.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_mor
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285493.

```text
dles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290346.

```text
.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_mor
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290398.

```text
dles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290346.

```text
.bin`,"bundles/app/js/engine/books/offbeat.bin":`bundles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_mor
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290398.

```text
dles/app/js/engine/books/offbeat.bin`,"bundles/app/js/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/oleksandr_bortnyk.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20426"></a>
## FND-20426: bundles/app/js/engine/books/paul_morphy.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/paul_morphy.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01295"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285545.

```text
s/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285591.

```text
/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290450.

```text
s/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290496.

```text
/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290450.

```text
s/engine/books/oleksandr_bortnyk.bin":`bundles/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290496.

```text
/app/js/engine/books/oleksandr_bortnyk.bin`,"bundles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/paul_morphy.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20427"></a>
## FND-20427: bundles/app/js/engine/books/pepecuenca.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/pepecuenca.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01296"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285637.

```text
undles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285682.

```text
bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290542.

```text
undles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290587.

```text
bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290542.

```text
undles/app/js/engine/books/paul_morphy.bin":`bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290587.

```text
bundles/app/js/engine/books/paul_morphy.bin`,"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/pepecuenca.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20428"></a>
## FND-20428: bundles/app/js/engine/books/petrosian.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/petrosian.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01297"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285727.

```text
"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285771.

```text
:`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutes
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290632.

```text
"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290676.

```text
:`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutes
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290632.

```text
"bundles/app/js/engine/books/pepecuenca.bin":`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290676.

```text
:`bundles/app/js/engine/books/pepecuenca.bin`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutes
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/petrosian.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20429"></a>
## FND-20429: bundles/app/js/engine/books/phiona_mutesi.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/phiona_mutesi.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01298"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285815.

```text
`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285863.

```text
undles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290720.

```text
`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290768.

```text
undles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290720.

```text
`,"bundles/app/js/engine/books/petrosian.bin":`bundles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290768.

```text
undles/app/js/engine/books/petrosian.bin`,"bundles/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/phiona_mutesi.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20430"></a>
## FND-20430: bundles/app/js/engine/books/pia_cramling.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/pia_cramling.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01299"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285911.

```text
es/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bi
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 285958.

```text
les/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290816.

```text
es/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290863.

```text
les/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290816.

```text
es/app/js/engine/books/phiona_mutesi.bin":`bundles/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290863.

```text
les/app/js/engine/books/phiona_mutesi.bin`,"bundles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/pia_cramling.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20431"></a>
## FND-20431: bundles/app/js/engine/books/positional.bin

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "bundles/app/js/engine/books/positional.bin",
  "type": "asset",
  "reference_form": "relative_literal",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01300"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 286005.

```text
dles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`,"bundles/app/js/engine/books/qiyu_zhou.bin":
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 286050.

```text
undles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`,"bundles/app/js/engine/books/qiyu_zhou.bin":`bundles/app/js/engine/books/qiyu_zhou.bin`,"
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290910.

```text
dles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`,"bundles/app/js/engine/books/qiyu_zhou.bin":
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290955.

```text
undles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`,"bundles/app/js/engine/books/qiyu_zhou.bin":`bundles/app/js/engine/books/qiyu_zhou.bin`,"
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290910.

```text
dles/app/js/engine/books/pia_cramling.bin":`bundles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`,"bundles/app/js/engine/books/qiyu_zhou.bin":
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 290955.

```text
undles/app/js/engine/books/pia_cramling.bin`,"bundles/app/js/engine/books/positional.bin":`bundles/app/js/engine/books/positional.bin`,"bundles/app/js/engine/books/qiyu_zhou.bin":`bundles/app/js/engine/books/qiyu_zhou.bin`,"
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <bundles/app/js/engine/books/positional.bin>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.
