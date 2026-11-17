# URL and reference inventory

[Master index](../00_MASTER_INDEX.md)

## URL-01201

`/tournament/live/redirect-to`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20332](../findings/url_references-013.md#FND-20332).

### SRC-0145 at character 3264

```text
[`https`]},web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|
```

### SRC-0145 at character 5727

```text
ps`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0145 at character 16088

```text
[`https`]},web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|
```

### SRC-0145 at character 18551

```text
ps`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0145 at character 19668

```text
om.routes,{web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|
```

### SRC-0145 at character 21207

```text
ps`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01202

`/v2/game-review`

- Type: api_or_websocket_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20333](../findings/url_references-013.md#FND-20333).

### SRC-0006 at character 9298

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```

### SRC-0010 at character 9298

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```

### SRC-0019 at character 9395

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```

### SRC-0023 at character 9395

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```

### SRC-0053 at character 9395

```text
 return null; }
    const path = (u.pathname || '').replace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostn
```

## URL-01203

`/v2/run-search`

- Type: api_or_websocket_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20334](../findings/url_references-013.md#FND-20334).

### SRC-0006 at character 9351

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```

### SRC-0010 at character 9351

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```

### SRC-0019 at character 9448

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```

### SRC-0023 at character 9448

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```

### SRC-0053 at character 9448

```text
eplace(/\/+$/, '');
    if (path === '/v2/game-review') return 'review';
    if (path === '/v2/run-search') return 'run-search';
    if (u.hostname.startsWith('analysis.')) return 'analysis-other'
```

## URL-01204

`/variants`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20335](../findings/url_references-013.md#FND-20335).

### SRC-0754 at character 7146

```text
schemes:[`https`]},web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```

### SRC-0754 at character 7906

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0754 at character 21628

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```

### SRC-0754 at character 22388

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 94782

```text
schemes:[`https`]},web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```

### SRC-0781 at character 95542

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 2170526

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```

### SRC-0781 at character 2171286

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 2593449

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```

### SRC-0781 at character 2595589

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 2933191

```text
w.chesscom.routes,{web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!ad
```

### SRC-0781 at character 2934636

```text
es:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01205

`/verified`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20336](../findings/url_references-013.md#FND-20336).

### SRC-0177 at character 865

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0177 at character 2349

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0177 at character 10519

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0177 at character 12003

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0178 at character 165

```text
.routes||{},Object.assign(window.chesscom.routes,{web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0178 at character 863

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0178 at character 3480

```text
.routes||{},Object.assign(window.chesscom.routes,{web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0178 at character 4178

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0191 at character 1651

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0191 at character 2349

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0191 at character 10211

```text
^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0191 at character 11695

```text
+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01206

`/vite/${e}`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20337](../findings/url_references-013.md#FND-20337).

### SRC-0781 at character 310533

```text
e(e)||``}var zd=r((()=>{}));function Nme(e){let t=document.querySelector(`link[data-href*="/vite/${e}"]`);if(t)return t.setAttribute(`href`,t.getAttribute(`data-href`)),t.removeAttribute(`data
```

### SRC-1137 at character 314620

```text
e(e)||``}var Xd=r((()=>{}));function ude(e){let t=document.querySelector(`link[data-href*="/vite/${e}"]`);if(t)return t.setAttribute(`href`,t.getAttribute(`data-href`)),t.removeAttribute(`data
```

### SRC-1165 at character 314620

```text
e(e)||``}var Xd=r((()=>{}));function ude(e){let t=document.querySelector(`link[data-href*="/vite/${e}"]`);if(t)return t.setAttribute(`href`,t.getAttribute(`data-href`)),t.removeAttribute(`data
```

## URL-01207

`/vote`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20338](../findings/url_references-013.md#FND-20338).

### SRC-0090 at character 17657

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-0090 at character 148969

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-0751 at character 17657

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-0751 at character 148969

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-0781 at character 80193

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-0781 at character 978882

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-1137 at character 113174

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-1137 at character 2700313

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-1165 at character 113174

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

### SRC-1165 at character 2700313

```text
`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-d
```

## URL-01208

`/votechess/seek`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20339](../findings/url_references-013.md#FND-20339).

### SRC-0781 at character 28535

```text
https`]},web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 474630

```text
https`]},web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 2966434

```text
.routes,{web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

## URL-01209

`/votechess/seek/data`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20340](../findings/url_references-013.md#FND-20340).

### SRC-0145 at character 996

```text
s`]},web_votechess_get_group_seek_data:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0145 at character 11634

```text
tes,{web_votechess_get_group_seek_data:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

## URL-01210

`bundles/app/js/engine/`

- Type: external_or_documentation; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20341](../findings/url_references-013.md#FND-20341).

### SRC-2048 at character 13420

```text
co.json`
unless the `analysis_engine_skip_book` feature flag is set.

Files shipped under `bundles/app/js/engine/`: `stockfish-nnue-15.1{,-no-Worker,-no-simd}.{js,wasm}`,
`stockfish-nnue-16{,-no-Worker,-n
```

## URL-01211

`bundles/app/js/engine/book-small.json`

- Type: external_or_documentation; form: relative_literal.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20342](../findings/url_references-013.md#FND-20342).

### SRC-0064 at character 2334

```text
-5af11540bbfe.nnue' "$D/stockfish/nn-5af11540bbfe.nnue" &
wait
# --- opening book ---
get 'bundles/app/js/engine/book-small.json' "$D/book/book-small.json" &
wait
echo "=== done ==="

```

### SRC-0781 at character 277837

```text
on Od(e){return e.filter((e,t,n)=>n.indexOf(e)===t)}var kd=r((()=>{})),Ad,pme=r((()=>{Ad={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bun
```

### SRC-0781 at character 277877

```text
xOf(e)===t)}var kd=r((()=>{})),Ad,pme=r((()=>{Ad={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`
```

### SRC-0781 at character 1914938

```text
res?.includes(`analysis_engine_skip_book`)?void 0:yN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),QJ={[KJ.STOCKFISH_NNUE]:{name:qJ?.full?.name||
```

### SRC-1137 at character 282742

```text
()=>{})),Ad,jd=r((()=>{Ad=(e,t)=>[...e].sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bun
```

### SRC-1137 at character 282782

```text
sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`
```

### SRC-1137 at character 1330340

```text
res?.includes(`analysis_engine_skip_book`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||
```

### SRC-1165 at character 282742

```text
()=>{})),Ad,jd=r((()=>{Ad=(e,t)=>[...e].sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bun
```

### SRC-1165 at character 282782

```text
sort((e,n)=>e[t]>n[t]?1:-1)})),Md,ode=r((()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`
```

### SRC-1165 at character 1330340

```text
res?.includes(`analysis_engine_skip_book`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||
```

## URL-01212

`bundles/app/js/engine/books/${e}.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20343](../findings/url_references-013.md#FND-20343).

### SRC-1137 at character 2716893

```text
`${Fxt}${encodeURIComponent(e)}`:zN(t?.includes(`book_binaries_from_npm_data_eco_webapp`)?`bundles/app/js/engine/books/${e}.bin`:`bundles/app/js/vendor/jschessengine/books/personalities/${e}.bin`,!1)}var Fxt,Ixt=r((()=
```

### SRC-1165 at character 2716893

```text
`${Fxt}${encodeURIComponent(e)}`:zN(t?.includes(`book_binaries_from_npm_data_eco_webapp`)?`bundles/app/js/engine/books/${e}.bin`:`bundles/app/js/vendor/jschessengine/books/personalities/${e}.bin`,!1)}var Fxt,Ixt=r((()=
```

## URL-01213

`bundles/app/js/engine/books/aggressive.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20344](../findings/url_references-013.md#FND-20344).

### SRC-0781 at character 277917

```text
(()=>{Ad={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstei
```

### SRC-0781 at character 277962

```text
son":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rub
```

### SRC-1137 at character 282822

```text
(()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstei
```

### SRC-1137 at character 282867

```text
son":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rub
```

### SRC-1165 at character 282822

```text
(()=>{Md={"bundles/app/js/engine/book-small.json":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstei
```

### SRC-1165 at character 282867

```text
son":`bundles/app/js/engine/book-small.json`,"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rub
```

## URL-01214

`bundles/app/js/engine/books/akiba_rubinstein.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20345](../findings/url_references-013.md#FND-20345).

### SRC-0781 at character 278007

```text
"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.
```

### SRC-0781 at character 278058

```text
es/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bu
```

### SRC-1137 at character 282912

```text
"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.
```

### SRC-1137 at character 282963

```text
es/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bu
```

### SRC-1165 at character 282912

```text
"bundles/app/js/engine/books/aggressive.bin":`bundles/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.
```

### SRC-1165 at character 282963

```text
es/app/js/engine/books/aggressive.bin`,"bundles/app/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bu
```

## URL-01215

`bundles/app/js/engine/books/alekhine.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20346](../findings/url_references-013.md#FND-20346).

### SRC-0781 at character 278109

```text
/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.b
```

### SRC-0781 at character 278152

```text
dles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_
```

### SRC-1137 at character 283014

```text
/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.b
```

### SRC-1137 at character 283057

```text
dles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_
```

### SRC-1165 at character 283014

```text
/js/engine/books/akiba_rubinstein.bin":`bundles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.b
```

### SRC-1165 at character 283057

```text
dles/app/js/engine/books/akiba_rubinstein.bin`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_
```

## URL-01216

`bundles/app/js/engine/books/alexandra_botez.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20347](../findings/url_references-013.md#FND-20347).

### SRC-0781 at character 278195

```text
in`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_
```

### SRC-0781 at character 278245

```text
ndles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexan
```

### SRC-1137 at character 283100

```text
in`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_
```

### SRC-1137 at character 283150

```text
ndles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexan
```

### SRC-1165 at character 283100

```text
in`,"bundles/app/js/engine/books/alekhine.bin":`bundles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_
```

### SRC-1165 at character 283150

```text
ndles/app/js/engine/books/alekhine.bin`,"bundles/app/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexan
```

## URL-01217

`bundles/app/js/engine/books/alexandra_kosteniuk.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20348](../findings/url_references-013.md#FND-20348).

### SRC-0781 at character 278295

```text
pp/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_h
```

### SRC-0781 at character 278349

```text
s/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hamble
```

### SRC-1137 at character 283200

```text
pp/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_h
```

### SRC-1137 at character 283254

```text
s/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hamble
```

### SRC-1165 at character 283200

```text
pp/js/engine/books/alexandra_botez.bin":`bundles/app/js/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_h
```

### SRC-1165 at character 283254

```text
s/engine/books/alexandra_botez.bin`,"bundles/app/js/engine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hamble
```

## URL-01218

`bundles/app/js/engine/books/aman_hambleton.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20349](../findings/url_references-013.md#FND-20349).

### SRC-0781 at character 278403

```text
gine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_bote
```

### SRC-0781 at character 278452

```text
js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.
```

### SRC-1137 at character 283308

```text
gine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_bote
```

### SRC-1137 at character 283357

```text
js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.
```

### SRC-1165 at character 283308

```text
gine/books/alexandra_kosteniuk.bin":`bundles/app/js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_bote
```

### SRC-1165 at character 283357

```text
js/engine/books/alexandra_kosteniuk.bin`,"bundles/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.
```

## URL-01219

`bundles/app/js/engine/books/andrea_botez.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20350](../findings/url_references-013.md#FND-20350).

### SRC-0781 at character 278501

```text
/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bi
```

### SRC-0781 at character 278548

```text
es/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`
```

### SRC-1137 at character 283406

```text
/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bi
```

### SRC-1137 at character 283453

```text
es/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`
```

### SRC-1165 at character 283406

```text
/app/js/engine/books/aman_hambleton.bin":`bundles/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bi
```

### SRC-1165 at character 283453

```text
es/app/js/engine/books/aman_hambleton.bin`,"bundles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`
```

## URL-01220

`bundles/app/js/engine/books/anish_giri.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20351](../findings/url_references-013.md#FND-20351).

### SRC-0781 at character 278595

```text
dles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.b
```

### SRC-0781 at character 278640

```text
undles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramlin
```

### SRC-1137 at character 283500

```text
dles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.b
```

### SRC-1137 at character 283545

```text
undles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramlin
```

### SRC-1165 at character 283500

```text
dles/app/js/engine/books/andrea_botez.bin":`bundles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.b
```

### SRC-1165 at character 283545

```text
undles/app/js/engine/books/andrea_botez.bin`,"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramlin
```

## URL-01221

`bundles/app/js/engine/books/anna_cramling.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20352](../findings/url_references-013.md#FND-20352).

### SRC-0781 at character 278685

```text
"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychu
```

### SRC-0781 at character 278733

```text
ndles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychu
```

### SRC-1137 at character 283590

```text
"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychu
```

### SRC-1137 at character 283638

```text
ndles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychu
```

### SRC-1165 at character 283590

```text
"bundles/app/js/engine/books/anish_giri.bin":`bundles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychu
```

### SRC-1165 at character 283638

```text
ndles/app/js/engine/books/anish_giri.bin`,"bundles/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychu
```

## URL-01222

`bundles/app/js/engine/books/anna_muzychuk.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20353](../findings/url_references-013.md#FND-20353).

### SRC-0781 at character 278781

```text
es/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.
```

### SRC-0781 at character 278829

```text
es/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bi
```

### SRC-1137 at character 283686

```text
es/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.
```

### SRC-1137 at character 283734

```text
es/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bi
```

### SRC-1165 at character 283686

```text
es/app/js/engine/books/anna_cramling.bin":`bundles/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.
```

### SRC-1165 at character 283734

```text
es/app/js/engine/books/anna_cramling.bin`,"bundles/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bi
```

## URL-01223

`bundles/app/js/engine/books/anna_rudolf.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20354](../findings/url_references-013.md#FND-20354).

### SRC-0781 at character 278877

```text
es/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.
```

### SRC-0781 at character 278923

```text
dles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levi
```

### SRC-1137 at character 283782

```text
es/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.
```

### SRC-1137 at character 283828

```text
dles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levi
```

### SRC-1165 at character 283782

```text
es/app/js/engine/books/anna_muzychuk.bin":`bundles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.
```

### SRC-1165 at character 283828

```text
dles/app/js/engine/books/anna_muzychuk.bin`,"bundles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levi
```

## URL-01224

`bundles/app/js/engine/books/anthony_levin.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20355](../findings/url_references-013.md#FND-20355).

### SRC-0781 at character 278969

```text
undles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_mile
```

### SRC-0781 at character 279017

```text
dles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_mile
```

### SRC-1137 at character 283874

```text
undles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_mile
```

### SRC-1137 at character 283922

```text
dles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_mile
```

### SRC-1165 at character 283874

```text
undles/app/js/engine/books/anna_rudolf.bin":`bundles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_mile
```

### SRC-1165 at character 283922

```text
dles/app/js/engine/books/anna_rudolf.bin`,"bundles/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_mile
```

## URL-01225

`bundles/app/js/engine/books/anthony_miles.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20356](../findings/url_references-013.md#FND-20356).

### SRC-0781 at character 279065

```text
es/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowi
```

### SRC-0781 at character 279113

```text
es/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimz
```

### SRC-1137 at character 283970

```text
es/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowi
```

### SRC-1137 at character 284018

```text
es/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimz
```

### SRC-1165 at character 283970

```text
es/app/js/engine/books/anthony_levin.bin":`bundles/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowi
```

### SRC-1165 at character 284018

```text
es/app/js/engine/books/anthony_levin.bin`,"bundles/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimz
```

## URL-01226

`bundles/app/js/engine/books/aron_nimzowitsch.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20357](../findings/url_references-013.md#FND-20357).

### SRC-0781 at character 279161

```text
es/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_r
```

### SRC-0781 at character 279212

```text
app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_
```

### SRC-1137 at character 284066

```text
es/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_r
```

### SRC-1137 at character 284117

```text
app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_
```

### SRC-1165 at character 284066

```text
es/app/js/engine/books/anthony_miles.bin":`bundles/app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_r
```

### SRC-1165 at character 284117

```text
app/js/engine/books/anthony_miles.bin`,"bundles/app/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_
```

## URL-01227

`bundles/app/js/engine/books/avigail_rosenthal.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20358](../findings/url_references-013.md#FND-20358).

### SRC-0781 at character 279263

```text
/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced
```

### SRC-0781 at character 279315

```text
js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bu
```

### SRC-1137 at character 284168

```text
/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced
```

### SRC-1137 at character 284220

```text
js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bu
```

### SRC-1165 at character 284168

```text
/js/engine/books/aron_nimzowitsch.bin":`bundles/app/js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced
```

### SRC-1165 at character 284220

```text
js/engine/books/aron_nimzowitsch.bin`,"bundles/app/js/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bu
```

## URL-01228

`bundles/app/js/engine/books/balanced.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20359](../findings/url_references-013.md#FND-20359).

### SRC-0781 at character 279367

```text
s/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bu
```

### SRC-0781 at character 279410

```text
les/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bu
```

### SRC-1137 at character 284272

```text
s/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bu
```

### SRC-1137 at character 284315

```text
les/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bu
```

### SRC-1165 at character 284272

```text
s/engine/books/avigail_rosenthal.bin":`bundles/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bu
```

### SRC-1165 at character 284315

```text
les/app/js/engine/books/avigail_rosenthal.bin`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bu
```

## URL-01229

`bundles/app/js/engine/books/beginner.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20360](../findings/url_references-013.md#FND-20360).

### SRC-0781 at character 279453

```text
in`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin"
```

### SRC-0781 at character 279496

```text
in":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.
```

### SRC-1137 at character 284358

```text
in`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin"
```

### SRC-1137 at character 284401

```text
in":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.
```

### SRC-1165 at character 284358

```text
in`,"bundles/app/js/engine/books/balanced.bin":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin"
```

### SRC-1165 at character 284401

```text
in":`bundles/app/js/engine/books/balanced.bin`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.
```

## URL-01230

`bundles/app/js/engine/books/benjamin_bok.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20361](../findings/url_references-013.md#FND-20361).

### SRC-0781 at character 279539

```text
in`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_fine
```

### SRC-0781 at character 279586

```text
`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin
```

### SRC-1137 at character 284444

```text
in`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_fine
```

### SRC-1137 at character 284491

```text
`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin
```

### SRC-1165 at character 284444

```text
in`,"bundles/app/js/engine/books/beginner.bin":`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_fine
```

### SRC-1165 at character 284491

```text
`bundles/app/js/engine/books/beginner.bin`,"bundles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin
```

## URL-01231

`bundles/app/js/engine/books/benjamin_finegold.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20362](../findings/url_references-013.md#FND-20362).

### SRC-0781 at character 279633

```text
dles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_lar
```

### SRC-0781 at character 279685

```text
app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bi
```

### SRC-1137 at character 284538

```text
dles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_lar
```

### SRC-1137 at character 284590

```text
app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bi
```

### SRC-1165 at character 284538

```text
dles/app/js/engine/books/benjamin_bok.bin":`bundles/app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_lar
```

### SRC-1165 at character 284590

```text
app/js/engine/books/benjamin_bok.bin`,"bundles/app/js/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bi
```

## URL-01232

`bundles/app/js/engine/books/bent_larsen.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20363](../findings/url_references-013.md#FND-20363).

### SRC-0781 at character 279737

```text
s/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter
```

### SRC-0781 at character 279783

```text
/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wou
```

### SRC-1137 at character 284642

```text
s/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter
```

### SRC-1137 at character 284688

```text
/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wou
```

### SRC-1165 at character 284642

```text
s/engine/books/benjamin_finegold.bin":`bundles/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter
```

### SRC-1165 at character 284688

```text
/app/js/engine/books/benjamin_finegold.bin`,"bundles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wou
```

## URL-01233

`bundles/app/js/engine/books/bikfoot_wouter.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20364](../findings/url_references-013.md#FND-20364).

### SRC-0781 at character 279829

```text
undles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`
```

### SRC-0781 at character 279878

```text
les/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/ap
```

### SRC-1137 at character 284734

```text
undles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`
```

### SRC-1137 at character 284783

```text
les/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/ap
```

### SRC-1165 at character 284734

```text
undles/app/js/engine/books/bent_larsen.bin":`bundles/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`
```

### SRC-1165 at character 284783

```text
les/app/js/engine/books/bent_larsen.bin`,"bundles/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/ap
```

## URL-01234

`bundles/app/js/engine/books/book.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20365](../findings/url_references-013.md#FND-20365).

### SRC-0781 at character 279927

```text
/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundl
```

### SRC-0781 at character 279966

```text
":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"
```

### SRC-1137 at character 284832

```text
/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundl
```

### SRC-1137 at character 284871

```text
":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"
```

### SRC-1165 at character 284832

```text
/app/js/engine/books/bikfoot_wouter.bin":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundl
```

### SRC-1165 at character 284871

```text
":`bundles/app/js/engine/books/bikfoot_wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"
```

## URL-01235

`bundles/app/js/engine/books/botvinnik.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20366](../findings/url_references-013.md#FND-20366).

### SRC-0781 at character 280005

```text
wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":
```

### SRC-0781 at character 280049

```text
k.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`
```

### SRC-1137 at character 284910

```text
wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":
```

### SRC-1137 at character 284954

```text
k.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`
```

### SRC-1165 at character 284910

```text
wouter.bin`,"bundles/app/js/engine/books/book.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":
```

### SRC-1165 at character 284954

```text
k.bin":`bundles/app/js/engine/books/book.bin`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`
```

## URL-01236

`bundles/app/js/engine/books/capablanca.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20367](../findings/url_references-013.md#FND-20367).

### SRC-0781 at character 280093

```text
`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.b
```

### SRC-0781 at character 280138

```text
:`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evan
```

### SRC-1137 at character 284998

```text
`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.b
```

### SRC-1137 at character 285043

```text
:`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evan
```

### SRC-1165 at character 284998

```text
`,"bundles/app/js/engine/books/botvinnik.bin":`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.b
```

### SRC-1165 at character 285043

```text
:`bundles/app/js/engine/books/botvinnik.bin`,"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evan
```

## URL-01237

`bundles/app/js/engine/books/captain_evans.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20368](../findings/url_references-013.md#FND-20368).

### SRC-0781 at character 280183

```text
"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin"
```

### SRC-0781 at character 280231

```text
ndles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bund
```

### SRC-1137 at character 285088

```text
"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin"
```

### SRC-1137 at character 285136

```text
ndles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bund
```

### SRC-1165 at character 285088

```text
"bundles/app/js/engine/books/capablanca.bin":`bundles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin"
```

### SRC-1165 at character 285136

```text
ndles/app/js/engine/books/capablanca.bin`,"bundles/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bund
```

## URL-01238

`bundles/app/js/engine/books/carlsen.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20369](../findings/url_references-013.md#FND-20369).

### SRC-0781 at character 280279

```text
es/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`
```

### SRC-0781 at character 280321

```text
`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bi
```

### SRC-1137 at character 285184

```text
es/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`
```

### SRC-1137 at character 285226

```text
`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bi
```

### SRC-1165 at character 285184

```text
es/app/js/engine/books/captain_evans.bin":`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`
```

### SRC-1165 at character 285226

```text
`bundles/app/js/engine/books/captain_evans.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bi
```

## URL-01239

`bundles/app/js/engine/books/cccopenings.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20370](../findings/url_references-013.md#FND-20370).

### SRC-0781 at character 280363

```text
.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_puli
```

### SRC-0781 at character 280409

```text
":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christia
```

### SRC-1137 at character 285268

```text
.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_puli
```

### SRC-1137 at character 285314

```text
":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christia
```

### SRC-1165 at character 285268

```text
.bin`,"bundles/app/js/engine/books/carlsen.bin":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_puli
```

### SRC-1165 at character 285314

```text
":`bundles/app/js/engine/books/carlsen.bin`,"bundles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christia
```

## URL-01240

`bundles/app/js/engine/books/christian_pulisic.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20371](../findings/url_references-013.md#FND-20371).

### SRC-0781 at character 280455

```text
undles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classica
```

### SRC-0781 at character 280507

```text
/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"
```

### SRC-1137 at character 285360

```text
undles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classica
```

### SRC-1137 at character 285412

```text
/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"
```

### SRC-1165 at character 285360

```text
undles/app/js/engine/books/cccopenings.bin":`bundles/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classica
```

### SRC-1165 at character 285412

```text
/app/js/engine/books/cccopenings.bin`,"bundles/app/js/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"
```

## URL-01241

`bundles/app/js/engine/books/classical.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20372](../findings/url_references-013.md#FND-20372).

### SRC-0781 at character 280559

```text
s/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin
```

### SRC-0781 at character 280603

```text
es/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.
```

### SRC-1137 at character 285464

```text
s/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin
```

### SRC-1137 at character 285508

```text
es/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.
```

### SRC-1165 at character 285464

```text
s/engine/books/christian_pulisic.bin":`bundles/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin
```

### SRC-1165 at character 285508

```text
es/app/js/engine/books/christian_pulisic.bin`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.
```

## URL-01242

`bundles/app/js/engine/books/dan_rozovsky.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20373](../findings/url_references-013.md#FND-20373).

### SRC-0781 at character 280647

```text
`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_narodi
```

### SRC-0781 at character 280694

```text
bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_n
```

### SRC-1137 at character 285552

```text
`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_narodi
```

### SRC-1137 at character 285599

```text
bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_n
```

### SRC-1165 at character 285552

```text
`,"bundles/app/js/engine/books/classical.bin":`bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_narodi
```

### SRC-1165 at character 285599

```text
bundles/app/js/engine/books/classical.bin`,"bundles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_n
```

## URL-01243

`bundles/app/js/engine/books/daniel_naroditsky.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20374](../findings/url_references-013.md#FND-20374).

### SRC-0781 at character 280741

```text
dles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_mo
```

### SRC-0781 at character 280793

```text
app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bi
```

### SRC-1137 at character 285646

```text
dles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_mo
```

### SRC-1137 at character 285698

```text
app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bi
```

### SRC-1165 at character 285646

```text
dles/app/js/engine/books/dan_rozovsky.bin":`bundles/app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_mo
```

### SRC-1165 at character 285698

```text
app/js/engine/books/dan_rozovsky.bin`,"bundles/app/js/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bi
```

## URL-01244

`bundles/app/js/engine/books/daryl_morey.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20375](../findings/url_references-013.md#FND-20375).

### SRC-0781 at character 280845

```text
s/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.b
```

### SRC-0781 at character 280891

```text
/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.
```

### SRC-1137 at character 285750

```text
s/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.b
```

### SRC-1137 at character 285796

```text
/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.
```

### SRC-1165 at character 285750

```text
s/engine/books/daniel_naroditsky.bin":`bundles/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.b
```

### SRC-1165 at character 285796

```text
/app/js/engine/books/daniel_naroditsky.bin`,"bundles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.
```

## URL-01245

`bundles/app/js/engine/books/david_howell.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20376](../findings/url_references-013.md#FND-20376).

### SRC-0781 at character 280937

```text
undles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.b
```

### SRC-0781 at character 280984

```text
ndles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bi
```

### SRC-1137 at character 285842

```text
undles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.b
```

### SRC-1137 at character 285889

```text
ndles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bi
```

### SRC-1165 at character 285842

```text
undles/app/js/engine/books/daryl_morey.bin":`bundles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.b
```

### SRC-1165 at character 285889

```text
ndles/app/js/engine/books/daryl_morey.bin`,"bundles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bi
```

## URL-01246

`bundles/app/js/engine/books/dawid_czerw.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20377](../findings/url_references-013.md#FND-20377).

### SRC-0781 at character 281031

```text
dles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bun
```

### SRC-0781 at character 281077

```text
ndles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/ap
```

### SRC-1137 at character 285936

```text
dles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bun
```

### SRC-1137 at character 285982

```text
ndles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/ap
```

### SRC-1165 at character 285936

```text
dles/app/js/engine/books/david_howell.bin":`bundles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bun
```

### SRC-1165 at character 285982

```text
ndles/app/js/engine/books/david_howell.bin`,"bundles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/ap
```

## URL-01247

`bundles/app/js/engine/books/ding.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20378](../findings/url_references-013.md#FND-20378).

### SRC-0781 at character 281123

```text
undles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bu
```

### SRC-0781 at character 281162

```text
bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.
```

### SRC-1137 at character 286028

```text
undles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bu
```

### SRC-1137 at character 286067

```text
bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.
```

### SRC-1165 at character 286028

```text
undles/app/js/engine/books/dawid_czerw.bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bu
```

### SRC-1165 at character 286067

```text
bin":`bundles/app/js/engine/books/dawid_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.
```

## URL-01248

`bundles/app/js/engine/books/dodge_coates.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20379](../findings/url_references-013.md#FND-20379).

### SRC-0781 at character 281201

```text
_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman
```

### SRC-0781 at character 281248

```text
in":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittma
```

### SRC-1137 at character 286106

```text
_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman
```

### SRC-1137 at character 286153

```text
in":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittma
```

### SRC-1165 at character 286106

```text
_czerw.bin`,"bundles/app/js/engine/books/ding.bin":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman
```

### SRC-1165 at character 286153

```text
in":`bundles/app/js/engine/books/ding.bin`,"bundles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittma
```

## URL-01249

`bundles/app/js/engine/books/dylan_rittman.bin`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20380](../findings/url_references-013.md#FND-20380).

### SRC-0781 at character 281295

```text
dles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`b
```

### SRC-0781 at character 281343

```text
les/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/ap
```

### SRC-1137 at character 286200

```text
dles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`b
```

### SRC-1137 at character 286248

```text
les/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/ap
```

### SRC-1165 at character 286200

```text
dles/app/js/engine/books/dodge_coates.bin":`bundles/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`b
```

### SRC-1165 at character 286248

```text
les/app/js/engine/books/dodge_coates.bin`,"bundles/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/ap
```

## URL-01250

`bundles/app/js/engine/books/eco.json`

- Type: external_or_documentation; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20381](../findings/url_references-013.md#FND-20381).

### SRC-0781 at character 281391

```text
es/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bun
```

### SRC-0781 at character 281430

```text
n":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bi
```

### SRC-0781 at character 1914978

```text
`)?void 0:yN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),QJ={[KJ.STOCKFISH_NNUE]:{name:qJ?.full?.name||`Stockfish 16.1`,description:L(`%filesi
```

### SRC-1137 at character 286296

```text
es/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bun
```

### SRC-1137 at character 286335

```text
n":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bi
```

### SRC-1137 at character 1330380

```text
`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||`Stockfish 16.1`,description:z(`%filesi
```

### SRC-1137 at character 2686118

```text
unction Xbt(){let e=window.context?.environment===`test`?`bundles/app/js/engine/eco.json`:`bundles/app/js/engine/books/eco.json`;return`${self.location.origin}${zN(e,!1)}`}var Zbt=r((()=>{BN()}));function Qbt(e=U2.game
```

### SRC-1165 at character 286296

```text
es/app/js/engine/books/dylan_rittman.bin":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bun
```

### SRC-1165 at character 286335

```text
n":`bundles/app/js/engine/books/dylan_rittman.bin`,"bundles/app/js/engine/books/eco.json":`bundles/app/js/engine/books/eco.json`,"bundles/app/js/engine/books/eric_hansen.bin":`bundles/app/js/engine/books/eric_hansen.bi
```

### SRC-1165 at character 1330380

```text
`)?void 0:zN(window.context?.environment===`test`?`bundles/app/js/engine/book-small.json`:`bundles/app/js/engine/books/eco.json`,!1),iP={[QN.STOCKFISH_NNUE]:{name:$N?.full?.name||`Stockfish 16.1`,description:z(`%filesi
```

### SRC-1165 at character 2686118

```text
unction Xbt(){let e=window.context?.environment===`test`?`bundles/app/js/engine/eco.json`:`bundles/app/js/engine/books/eco.json`;return`${self.location.origin}${zN(e,!1)}`}var Zbt=r((()=>{BN()}));function Qbt(e=U2.game
```

### SRC-2048 at character 13300

```text
display name `Stockfish 16.1`, `66MB`,
`paths.settings: { Threads: '1' }`, `pathToBook` = `bundles/app/js/engine/books/eco.json`
unless the `analysis_engine_skip_book` feature flag is set.

Files shipped under `bundles
```
