# routes — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18206"></a>
## FND-18206: Declared route i18n_web_league_division

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0101",
  "route_name": "i18n_web_league_division",
  "url_pattern": "/{_locale}/leagues/{league}/{division}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_league_division",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0201",
    "SRC-0780",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 2978,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[\\\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\\\w+`,`league`,!0],[`text`,`/leagues`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{league:`\\\\w+`,division:`[\\\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0201** `research/play.js` — [preserved redacted evidence](../evidence/text/7b48978996e293cd2e02e9853ab5ba84a3684afe8a7e4c5bd40f8e89a1a85571.js)
  Character offset 2195.

```text
hesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG
```
- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)
  Character offset 2247.

```text
hesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 109027.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 58055.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 58055.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG
```

**Source references:** SRC-0201, SRC-0780, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18139, FND-18142, FND-18205

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18207"></a>
## FND-18207: Declared route web_analysis_ceac

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0102",
  "route_name": "web_analysis_ceac",
  "url_pattern": "/analysis/game/{type}/{gameId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_ceac",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 142.

```text
.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_analysis_ceac:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 28658.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 28658.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+
```

**Source references:** SRC-0754, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18208"></a>
## FND-18208: Declared route i18n_web_analysis_ceac

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0103",
  "route_name": "i18n_web_analysis_ceac",
  "url_pattern": "/{_locale}/analysis/game/{type}/{gameId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_ceac",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 965,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 142.

```text
.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_analysis_ceac:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 28658.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 28658.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+
```

**Source references:** SRC-0754, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18209"></a>
## FND-18209: Declared route web_analysis_game_callback_user_allowed_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0104",
  "route_name": "web_analysis_game_callback_user_allowed_view",
  "url_pattern": "/callback/analysis/user/allowed",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_game_callback_user_allowed_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754"
  ],
  "character_offset": 1892,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/analysis/user/allowed`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 1937.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_game_callback_user_allowed_view:{tokens:[[`text`,`/callback/analysis/user/allowed`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl
```

**Source references:** SRC-0754  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18210"></a>
## FND-18210: Declared route web_play_computer_chess960

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0105",
  "route_name": "web_play_computer_chess960",
  "url_pattern": "/play/computer/chess960",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_computer_chess960",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754"
  ],
  "character_offset": 2634,
  "raw_route_declaration": "{tokens:[[`text`,`/play/computer/chess960`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 2661.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_play_computer_chess960:{tokens:[[`text`,`/play/computer/chess960`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```

**Source references:** SRC-0754  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18211"></a>
## FND-18211: Declared route i18n_web_play_computer_chess960

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0106",
  "route_name": "i18n_web_play_computer_chess960",
  "url_pattern": "/{_locale}/play/computer/chess960",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_computer_chess960",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754"
  ],
  "character_offset": 4038,
  "raw_route_declaration": "{tokens:[[`text`,`/play/computer/chess960`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 4070.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_computer_chess960:{tokens:[[`text`,`/play/computer/chess960`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```

**Source references:** SRC-0754  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18212"></a>
## FND-18212: Declared route web_chess_variants

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0107",
  "route_name": "web_chess_variants",
  "url_pattern": "/variants/{variant}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_chess_variants",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754",
    "SRC-0781"
  ],
  "character_offset": 7074,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 7093.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 94729.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```

**Source references:** SRC-0754, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18213"></a>
## FND-18213: Declared route i18n_web_chess_variants

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0108",
  "route_name": "i18n_web_chess_variants",
  "url_pattern": "/{_locale}/variants/{variant}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_chess_variants",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0754",
    "SRC-0781"
  ],
  "character_offset": 7829,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{variant:null,host:`www.chess-dev.com`,_locale:``},requirements:{variant:`.+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 7853.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{variant:null,host:`www.che
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 95489.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_chess_variants:{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{variant:null,host:`www.che
```

**Source references:** SRC-0754, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18126, FND-18132, FND-18166, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18214"></a>
## FND-18214: Declared route web_membership_gift

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0109",
  "route_name": "web_membership_gift",
  "url_pattern": "/membership/gift/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_membership_gift",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0776"
  ],
  "character_offset": 319,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/membership/gift`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0776** `research/refinement/live-chunks/shared.f34807a8.B2SFDOzRcN.chunk.js` — [preserved redacted evidence](../evidence/text/f36ce88b583e90e1599d8c42cd5d956ed4bbd7f73390e464434f985ee62ec857.js)
  Character offset 339.

```text
hesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_membership_gift:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/membership/gift`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```

**Source references:** SRC-0776  
**URL references:** None independently associated  
**Related findings:** FND-18215, FND-19407

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18215"></a>
## FND-18215: Declared route i18n_web_membership_gift

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0110",
  "route_name": "i18n_web_membership_gift",
  "url_pattern": "/{_locale}/membership/gift/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_membership_gift",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0776"
  ],
  "character_offset": 1070,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/membership/gift`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0776** `research/refinement/live-chunks/shared.f34807a8.B2SFDOzRcN.chunk.js` — [preserved redacted evidence](../evidence/text/f36ce88b583e90e1599d8c42cd5d956ed4bbd7f73390e464434f985ee62ec857.js)
  Character offset 1095.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership_gift:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/membership/gift`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,
```

**Source references:** SRC-0776  
**URL references:** None independently associated  
**Related findings:** FND-18214, FND-19407

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18216"></a>
## FND-18216: Declared route web_classroom

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0111",
  "route_name": "web_classroom",
  "url_pattern": "/classroom",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_classroom",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0779",
    "SRC-0781"
  ],
  "character_offset": 497,
  "raw_route_declaration": "{tokens:[[`text`,`/classroom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0779** `research/refinement/live-game-tab.js` — [preserved redacted evidence](../evidence/text/0b689d683d4503896e5fb984c9f0a0c23dd6000d700d6baab70c0df82a62ec72.js)
  Character offset 511.

```text
ndow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_classroom:{tokens:[[`text`,`/classroom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 110713.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_classroom:{tokens:[[`text`,`/classroom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```

**Source references:** SRC-0779, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18217, FND-18218, FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18217"></a>
## FND-18217: Declared route i18n_web_classroom

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0112",
  "route_name": "i18n_web_classroom",
  "url_pattern": "/{_locale}/classroom",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_classroom",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0779",
    "SRC-0781"
  ],
  "character_offset": 1182,
  "raw_route_declaration": "{tokens:[[`text`,`/classroom`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0779** `research/refinement/live-game-tab.js` — [preserved redacted evidence](../evidence/text/0b689d683d4503896e5fb984c9f0a0c23dd6000d700d6baab70c0df82a62ec72.js)
  Character offset 1201.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_classroom:{tokens:[[`text`,`/classroom`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 111403.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_classroom:{tokens:[[`text`,`/classroom`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!
```

**Source references:** SRC-0779, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18216, FND-18218, FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18218"></a>
## FND-18218: Declared route web_coach_hide_saved_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0113",
  "route_name": "web_coach_hide_saved_game",
  "url_pattern": "/callback/coach/hide-game/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_coach_hide_saved_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0779"
  ],
  "character_offset": 1953,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/coach/hide-game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0779** `research/refinement/live-game-tab.js` — [preserved redacted evidence](../evidence/text/0b689d683d4503896e5fb984c9f0a0c23dd6000d700d6baab70c0df82a62ec72.js)
  Character offset 1979.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_coach_hide_saved_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/coach/hide-game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```

**Source references:** SRC-0779  
**URL references:** None independently associated  
**Related findings:** FND-18216, FND-18217

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18219"></a>
## FND-18219: Declared route web_computer_hide_saved_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0114",
  "route_name": "web_computer_hide_saved_game",
  "url_pattern": "/callback/computer/hide-game/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_computer_hide_saved_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0779"
  ],
  "character_offset": 2713,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/computer/hide-game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0779** `research/refinement/live-game-tab.js` — [preserved redacted evidence](../evidence/text/0b689d683d4503896e5fb984c9f0a0c23dd6000d700d6baab70c0df82a62ec72.js)
  Character offset 2742.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_computer_hide_saved_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/computer/hide-game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```

**Source references:** SRC-0779  
**URL references:** None independently associated  
**Related findings:** FND-18216, FND-18217, FND-18218

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18220"></a>
## FND-18220: Declared route web_live_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0115",
  "route_name": "web_live_game",
  "url_pattern": "/live/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_live_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 7576,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 7590.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},web_live_game:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18221"></a>
## FND-18221: Declared route web_play_club_challenges

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0116",
  "route_name": "web_play_club_challenges",
  "url_pattern": "/play/online/club-challenges",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_club_challenges",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 8295,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/club-challenges`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 8320.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_club_challenges:{tokens:[[`text`,`/play/online/club-challenges`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18222"></a>
## FND-18222: Declared route web_game_coach

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0117",
  "route_name": "web_game_coach",
  "url_pattern": "/game/coach/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_coach",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 9009,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 9024.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_coach:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18223"></a>
## FND-18223: Declared route web_game_computer

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0118",
  "route_name": "web_game_computer",
  "url_pattern": "/game/computer/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_computer",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 9730,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 9748.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_computer:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_F
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18224"></a>
## FND-18224: Declared route web_play_connected_board

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0119",
  "route_name": "web_play_connected_board",
  "url_pattern": "/play/online/connected-board",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_connected_board",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 10457,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/connected-board`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 10482.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_connected_board:{tokens:[[`text`,`/play/online/connected-board`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18225"></a>
## FND-18225: Declared route web_play_create_tournament

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0120",
  "route_name": "web_play_create_tournament",
  "url_pattern": "/play/online/create-tournament/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_create_tournament",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 11171,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/online/create-tournament`]],defaults:{id:``,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 11198.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_create_tournament:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/online/create-tournament`]],defaults:{id:``,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18226"></a>
## FND-18226: Declared route web_play_daily

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0121",
  "route_name": "web_play_daily",
  "url_pattern": "/play/online/daily",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_daily",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 11929,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 11944.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_daily:{tokens:[[`text`,`/play/online/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18227"></a>
## FND-18227: Declared route web_daily_seek

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0122",
  "route_name": "web_daily_seek",
  "url_pattern": "/daily-chess/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_daily_seek",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 13344,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-chess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 13359.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-chess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18228"></a>
## FND-18228: Declared route web_play_daily_team_match_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0123",
  "route_name": "web_play_daily_team_match_challenge",
  "url_pattern": "/daily-team/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_daily_team_match_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 14071,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 14107.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18229"></a>
## FND-18229: Declared route web_play_friend

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0124",
  "route_name": "web_play_friend",
  "url_pattern": "/play/online/friend",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_friend",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 14818,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/friend`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 14834.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_friend:{tokens:[[`text`,`/play/online/friend`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18230"></a>
## FND-18230: Declared route web_play_live_arena

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0125",
  "route_name": "web_play_live_arena",
  "url_pattern": "/play/arena/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_live_arena",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 15514,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/arena`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 15534.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_live_arena:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/arena`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18231"></a>
## FND-18231: Declared route web_play_live_arena_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0126",
  "route_name": "web_play_live_arena_challenge",
  "url_pattern": "/live-arena/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_live_arena_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 16240,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-arena/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 16270.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_live_arena_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-arena/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18232"></a>
## FND-18232: Declared route web_play_arena_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0127",
  "route_name": "web_play_arena_challenge",
  "url_pattern": "/arena/invite/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_arena_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 16981,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/arena/invite`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 17006.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_arena_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/arena/invite`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18233"></a>
## FND-18233: Declared route web_game_live

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0128",
  "route_name": "web_game_live",
  "url_pattern": "/game/live/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_live",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 17714,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 17728.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fi
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 121492.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fi
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 121492.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fi
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18234"></a>
## FND-18234: Declared route web_play_live_team_match_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0129",
  "route_name": "web_play_live_team_match_challenge",
  "url_pattern": "/live-team/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_live_team_match_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 18433,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 18468.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_live_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18235"></a>
## FND-18235: Declared route web_play_rcn_team_match_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0130",
  "route_name": "web_play_rcn_team_match_challenge",
  "url_pattern": "/match/invite/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_rcn_team_match_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 19178,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/match/invite`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 19212.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_rcn_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/match/invite`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18236"></a>
## FND-18236: Declared route web_play_live_tournament

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0131",
  "route_name": "web_play_live_tournament",
  "url_pattern": "/play/tournament/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_live_tournament",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 19920,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 19945.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_live_tournament:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18237"></a>
## FND-18237: Declared route web_play_new

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0132",
  "route_name": "web_play_new",
  "url_pattern": "/play/online/new",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_new",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 20656,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/new`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 20669.

```text
cacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_new:{tokens:[[`text`,`/play/online/new`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 130462.

```text
cacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_new:{tokens:[[`text`,`/play/online/new`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 130462.

```text
cacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_new:{tokens:[[`text`,`/play/online/new`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18238"></a>
## FND-18238: Declared route web_play

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0133",
  "route_name": "web_play",
  "url_pattern": "/play/online",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 21346,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 21355.

```text
fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play:{tokens:[[`text`,`/play/online`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18239"></a>
## FND-18239: Declared route web_game_uuid

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0134",
  "route_name": "web_game_uuid",
  "url_pattern": "/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_uuid",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 22028,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 22042.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 122211.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 122211.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18240"></a>
## FND-18240: Declared route web_play_settings

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0135",
  "route_name": "web_play_settings",
  "url_pattern": "/play/online/settings",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_settings",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 22742,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/settings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 22760.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_settings:{tokens:[[`text`,`/play/online/settings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18241"></a>
## FND-18241: Declared route web_play_live_team_match

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0136",
  "route_name": "web_play_live_team_match",
  "url_pattern": "/play/match/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_live_team_match",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 23442,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/match`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 23467.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_live_team_match:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/match`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18242"></a>
## FND-18242: Declared route web_play_tournaments

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0137",
  "route_name": "web_play_tournaments",
  "url_pattern": "/play/online/tournaments",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_tournaments",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 24173,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/tournaments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 24194.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_tournaments:{tokens:[[`text`,`/play/online/tournaments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18243"></a>
## FND-18243: Declared route web_play_variant_3_check

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0138",
  "route_name": "web_play_variant_3_check",
  "url_pattern": "/play/online/3-check",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_variant_3_check",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 24879,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/3-check`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 24904.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_variant_3_check:{tokens:[[`text`,`/play/online/3-check`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|h
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18244"></a>
## FND-18244: Declared route web_play_variant_chess960

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0139",
  "route_name": "web_play_variant_chess960",
  "url_pattern": "/play/online/chess960",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_variant_chess960",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 25585,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/chess960`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 25611.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_variant_chess960:{tokens:[[`text`,`/play/online/chess960`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18245"></a>
## FND-18245: Declared route web_play_variant_crazyhouse

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0140",
  "route_name": "web_play_variant_crazyhouse",
  "url_pattern": "/play/online/crazyhouse",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_variant_crazyhouse",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 26293,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/crazyhouse`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 26321.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_variant_crazyhouse:{tokens:[[`text`,`/play/online/crazyhouse`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18246"></a>
## FND-18246: Declared route web_play_variant_doubles_bughouse

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0141",
  "route_name": "web_play_variant_doubles_bughouse",
  "url_pattern": "/play/online/doubles-bughouse",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_variant_doubles_bughouse",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 27005,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/doubles-bughouse`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 27039.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_variant_doubles_bughouse:{tokens:[[`text`,`/play/online/doubles-bughouse`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18247"></a>
## FND-18247: Declared route web_play_variant_king_of_the_hill

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0142",
  "route_name": "web_play_variant_king_of_the_hill",
  "url_pattern": "/play/online/king-of-the-hill",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_variant_king_of_the_hill",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 27729,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/king-of-the-hill`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 27763.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_variant_king_of_the_hill:{tokens:[[`text`,`/play/online/king-of-the-hill`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18248"></a>
## FND-18248: Declared route web_votechess_view_group_seek

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0143",
  "route_name": "web_votechess_view_group_seek",
  "url_pattern": "/votechess/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_votechess_view_group_seek",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 28453,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 28483.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_votechess_view_group_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18249"></a>
## FND-18249: Declared route web_play_watch

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0144",
  "route_name": "web_play_watch",
  "url_pattern": "/play/online/watch",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_watch",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 29193,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/watch`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 29208.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_watch:{tokens:[[`text`,`/play/online/watch`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18250"></a>
## FND-18250: Declared route i18n_web_live_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0145",
  "route_name": "i18n_web_live_game",
  "url_pattern": "/{_locale}/live/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_live_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 29887,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 29906.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_live_game:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18251"></a>
## FND-18251: Declared route i18n_web_play_club_challenges

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0146",
  "route_name": "i18n_web_play_club_challenges",
  "url_pattern": "/{_locale}/play/online/club-challenges",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_club_challenges",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 30692,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/club-challenges`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 30722.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_club_challenges:{tokens:[[`text`,`/play/online/club-challenges`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18252"></a>
## FND-18252: Declared route i18n_web_game_coach

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0147",
  "route_name": "i18n_web_game_coach",
  "url_pattern": "/{_locale}/game/coach/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_game_coach",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 31492,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 31512.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_coach:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18253"></a>
## FND-18253: Declared route i18n_web_game_computer

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0148",
  "route_name": "i18n_web_game_computer",
  "url_pattern": "/{_locale}/game/computer/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_game_computer",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 32299,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 32322.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_computer:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18254"></a>
## FND-18254: Declared route i18n_web_play_connected_board

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0149",
  "route_name": "i18n_web_play_connected_board",
  "url_pattern": "/{_locale}/play/online/connected-board",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_connected_board",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 33112,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/connected-board`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 33142.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_connected_board:{tokens:[[`text`,`/play/online/connected-board`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requi
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18255"></a>
## FND-18255: Declared route i18n_web_play_create_tournament

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0150",
  "route_name": "i18n_web_play_create_tournament",
  "url_pattern": "/{_locale}/play/online/create-tournament/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_create_tournament",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 33912,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/online/create-tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{id:``,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 33944.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_create_tournament:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/online/create-tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{id:``,
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18256"></a>
## FND-18256: Declared route i18n_web_play_daily

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0151",
  "route_name": "i18n_web_play_daily",
  "url_pattern": "/{_locale}/play/online/daily",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_daily",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 34756,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 34776.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_daily:{tokens:[[`text`,`/play/online/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{h
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18257"></a>
## FND-18257: Declared route i18n_web_play_daily_team_match_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0152",
  "route_name": "i18n_web_play_daily_team_match_challenge",
  "url_pattern": "/{_locale}/daily-team/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_daily_team_match_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 36343,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 36384.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18258"></a>
## FND-18258: Declared route i18n_web_play_friend

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0153",
  "route_name": "i18n_web_play_friend",
  "url_pattern": "/{_locale}/play/online/friend",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_friend",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 37176,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/friend`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 37197.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_friend:{tokens:[[`text`,`/play/online/friend`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18259"></a>
## FND-18259: Declared route i18n_web_play_live_arena

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0154",
  "route_name": "i18n_web_play_live_arena",
  "url_pattern": "/{_locale}/play/arena/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_live_arena",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 37958,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/arena`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 37983.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_live_arena:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/arena`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18260"></a>
## FND-18260: Declared route i18n_web_play_live_arena_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0155",
  "route_name": "i18n_web_play_live_arena_challenge",
  "url_pattern": "/{_locale}/live-arena/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_live_arena_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 38770,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-arena/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 38805.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_live_arena_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-arena/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18261"></a>
## FND-18261: Declared route i18n_web_play_arena_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0156",
  "route_name": "i18n_web_play_arena_challenge",
  "url_pattern": "/{_locale}/arena/invite/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_arena_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 39597,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/arena/invite`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 39627.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_arena_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/arena/invite`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18262"></a>
## FND-18262: Declared route i18n_web_game_live

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0157",
  "route_name": "i18n_web_game_live",
  "url_pattern": "/{_locale}/game/live/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_game_live",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 40416,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 40435.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 123676.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 123676.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18263"></a>
## FND-18263: Declared route i18n_web_play_live_team_match_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0158",
  "route_name": "i18n_web_play_live_team_match_challenge",
  "url_pattern": "/{_locale}/live-team/seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_live_team_match_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 41221,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 41261.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_live_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.c
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18264"></a>
## FND-18264: Declared route i18n_web_play_rcn_team_match_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0159",
  "route_name": "i18n_web_play_rcn_team_match_challenge",
  "url_pattern": "/{_locale}/match/invite/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_rcn_team_match_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 42052,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/match/invite`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 42091.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_rcn_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/match/invite`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18265"></a>
## FND-18265: Declared route i18n_web_play_live_tournament

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0160",
  "route_name": "i18n_web_play_live_tournament",
  "url_pattern": "/{_locale}/play/tournament/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_live_tournament",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 42880,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 42910.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_live_tournament:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18266"></a>
## FND-18266: Declared route i18n_web_play_new

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0161",
  "route_name": "i18n_web_play_new",
  "url_pattern": "/{_locale}/play/online/new",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_new",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 43702,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/new`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 43720.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_new:{tokens:[[`text`,`/play/online/new`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 132709.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_new:{tokens:[[`text`,`/play/online/new`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 132709.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_new:{tokens:[[`text`,`/play/online/new`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18267"></a>
## FND-18267: Declared route i18n_web_play

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0162",
  "route_name": "i18n_web_play",
  "url_pattern": "/{_locale}/play/online",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 44478,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 44492.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play:{tokens:[[`text`,`/play/online`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18268"></a>
## FND-18268: Declared route i18n_web_game_uuid

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0163",
  "route_name": "i18n_web_game_uuid",
  "url_pattern": "/{_locale}/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_game_uuid",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 45246,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 45265.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_local
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 124481.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_local
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 124481.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_local
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18269"></a>
## FND-18269: Declared route i18n_web_play_settings

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0164",
  "route_name": "i18n_web_play_settings",
  "url_pattern": "/{_locale}/play/online/settings",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_settings",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 46046,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/settings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 46069.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_settings:{tokens:[[`text`,`/play/online/settings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18270"></a>
## FND-18270: Declared route i18n_web_play_live_team_match

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0165",
  "route_name": "i18n_web_play_live_team_match",
  "url_pattern": "/{_locale}/play/match/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_live_team_match",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 46832,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/match`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 46862.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_live_team_match:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/match`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18271"></a>
## FND-18271: Declared route i18n_web_play_tournaments

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0166",
  "route_name": "i18n_web_play_tournaments",
  "url_pattern": "/{_locale}/play/online/tournaments",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_tournaments",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 47649,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/tournaments`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 47675.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_tournaments:{tokens:[[`text`,`/play/online/tournaments`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requireme
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18272"></a>
## FND-18272: Declared route i18n_web_play_variant_3_check

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0167",
  "route_name": "i18n_web_play_variant_3_check",
  "url_pattern": "/{_locale}/play/online/3-check",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_variant_3_check",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 48441,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/3-check`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 48471.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_variant_3_check:{tokens:[[`text`,`/play/online/3-check`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18273"></a>
## FND-18273: Declared route i18n_web_play_variant_chess960

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0168",
  "route_name": "i18n_web_play_variant_chess960",
  "url_pattern": "/{_locale}/play/online/chess960",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_variant_chess960",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 49233,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/chess960`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 49264.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_variant_chess960:{tokens:[[`text`,`/play/online/chess960`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18274"></a>
## FND-18274: Declared route i18n_web_play_variant_crazyhouse

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0169",
  "route_name": "i18n_web_play_variant_crazyhouse",
  "url_pattern": "/{_locale}/play/online/crazyhouse",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_variant_crazyhouse",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 50027,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/crazyhouse`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 50060.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_variant_crazyhouse:{tokens:[[`text`,`/play/online/crazyhouse`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18275"></a>
## FND-18275: Declared route i18n_web_play_variant_doubles_bughouse

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0170",
  "route_name": "i18n_web_play_variant_doubles_bughouse",
  "url_pattern": "/{_locale}/play/online/doubles-bughouse",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_variant_doubles_bughouse",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 50825,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/doubles-bughouse`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 50864.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_variant_doubles_bughouse:{tokens:[[`text`,`/play/online/doubles-bughouse`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requ
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18276"></a>
## FND-18276: Declared route i18n_web_play_variant_king_of_the_hill

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0171",
  "route_name": "i18n_web_play_variant_king_of_the_hill",
  "url_pattern": "/{_locale}/play/online/king-of-the-hill",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_variant_king_of_the_hill",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 51635,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/king-of-the-hill`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 51674.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_variant_king_of_the_hill:{tokens:[[`text`,`/play/online/king-of-the-hill`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requ
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18277"></a>
## FND-18277: Declared route i18n_web_play_watch

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0172",
  "route_name": "i18n_web_play_watch",
  "url_pattern": "/{_locale}/play/online/watch",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_watch",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 52445,
  "raw_route_declaration": "{tokens:[[`text`,`/play/online/watch`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 52465.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_watch:{tokens:[[`text`,`/play/online/watch`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{h
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18278"></a>
## FND-18278: Declared route web_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0173",
  "route_name": "web_search",
  "url_pattern": "/search",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_search",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 54622,
  "raw_route_declaration": "{tokens:[[`text`,`/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 54633.

```text
|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_search:{tokens:[[`text`,`/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 49750.

```text
|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_search:{tokens:[[`text`,`/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 49750.

```text
|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_search:{tokens:[[`text`,`/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18279"></a>
## FND-18279: Declared route i18n_web_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0174",
  "route_name": "i18n_web_search",
  "url_pattern": "/{_locale}/search",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_search",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 56870,
  "raw_route_declaration": "{tokens:[[`text`,`/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 56886.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_search:{tokens:[[`text`,`/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 52003.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_search:{tokens:[[`text`,`/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 52003.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_search:{tokens:[[`text`,`/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18280"></a>
## FND-18280: Declared route web_bff_oauth_token

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0175",
  "route_name": "web_bff_oauth_token",
  "url_pattern": "/bff-token",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_bff_oauth_token",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 57635,
  "raw_route_declaration": "{tokens:[[`text`,`/bff-token`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 57655.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_bff_oauth_token:{tokens:[[`text`,`/bff-token`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 52772.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_bff_oauth_token:{tokens:[[`text`,`/bff-token`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 52772.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_bff_oauth_token:{tokens:[[`text`,`/bff-token`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18281"></a>
## FND-18281: Declared route web_computer_callback_load_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0176",
  "route_name": "web_computer_callback_load_game",
  "url_pattern": "/{gameType}/callback/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_computer_callback_load_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 58332,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game`],[`variable`,`/`,`computer|coach`,`gameType`,!0]],defaults:{gameType:`computer`,host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,gameType:`computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 58364.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_computer_callback_load_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`],[`variable`,`/`,`computer|coach`,`gameType`,!0]],defaults:{gameType:`computer`,host:`www.chess-dev.com`},requirements:{id:`\\d+`,gameType:`computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`a
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 135155.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_computer_callback_load_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`],[`variable`,`/`,`computer|coach`,`gameType`,!0]],defaults:{gameType:`computer`,host:`www.chess-dev.com`},requirements:{id:`\\d+`,gameType:`computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 135155.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_computer_callback_load_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`],[`variable`,`/`,`computer|coach`,`gameType`,!0]],defaults:{gameType:`computer`,host:`www.chess-dev.com`},requirements:{id:`\\d+`,gameType:`computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`a
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18282"></a>
## FND-18282: Declared route web_callback_load_game_live_data

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0177",
  "route_name": "web_callback_load_game_live_data",
  "url_pattern": "/callback/live/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_callback_load_game_live_data",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 59175,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`(?:\\\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,`id`,!0],[`text`,`/callback/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`(?:\\\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 59208.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_callback_load_game_live_data:{tokens:[[`variable`,`/`,`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,`id`,!0],[`text`,`/callback/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,h
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 134215.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_callback_load_game_live_data:{tokens:[[`variable`,`/`,`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,`id`,!0],[`text`,`/callback/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 134215.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_callback_load_game_live_data:{tokens:[[`variable`,`/`,`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,`id`,!0],[`text`,`/callback/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,h
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18283"></a>
## FND-18283: Declared route web_daily_callback_load_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0178",
  "route_name": "web_daily_callback_load_game",
  "url_pattern": "/callback/daily/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_daily_callback_load_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 60116,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 60145.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_callback_load_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 135995.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_callback_load_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 135995.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_callback_load_game:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18284"></a>
## FND-18284: Declared route web_tournaments_live_arena_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0179",
  "route_name": "web_tournaments_live_arena_view",
  "url_pattern": "/tournament/live/arena/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tournaments_live_arena_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 62362,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live/arena`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 62394.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournaments_live_arena_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live/arena`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18285"></a>
## FND-18285: Declared route web_tournaments_live_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0180",
  "route_name": "web_tournaments_live_view",
  "url_pattern": "/tournament/live/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tournaments_live_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 63112,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 63138.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournaments_live_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18286"></a>
## FND-18286: Declared route i18n_web_tournaments_live_arena_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0181",
  "route_name": "i18n_web_tournaments_live_arena_view",
  "url_pattern": "/{_locale}/tournament/live/arena/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tournaments_live_arena_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 66243,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live/arena`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 66280.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournaments_live_arena_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live/arena`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.che
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18287"></a>
## FND-18287: Declared route i18n_web_tournaments_live_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0182",
  "route_name": "i18n_web_tournaments_live_view",
  "url_pattern": "/{_locale}/tournament/live/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tournaments_live_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 67079,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 67110.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournaments_live_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18288"></a>
## FND-18288: Declared route web_puzzles_mode_battle_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0183",
  "route_name": "web_puzzles_mode_battle_view",
  "url_pattern": "/puzzles/battle/{shortUuid}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_puzzles_mode_battle_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 70160,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 70189.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode_battle_view:{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 122940.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode_battle_view:{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 122940.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode_battle_view:{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18289"></a>
## FND-18289: Declared route i18n_web_puzzles_mode_battle_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0184",
  "route_name": "i18n_web_puzzles_mode_battle_view",
  "url_pattern": "/{_locale}/puzzles/battle/{shortUuid}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_puzzles_mode_battle_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 70906,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 70940.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode_battle_view:{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.ches
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 125296.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode_battle_view:{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.ches
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 125296.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode_battle_view:{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.ches
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18290"></a>
## FND-18290: Declared route web_user_callback_id_to_user_data

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0185",
  "route_name": "web_user_callback_id_to_user_data",
  "url_pattern": "/callback/user/id-to-data",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_id_to_user_data",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 80933,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/id-to-data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 80967.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_id_to_user_data:{tokens:[[`text`,`/callback/user/id-to-data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18291"></a>
## FND-18291: Declared route web_club_profile

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0186",
  "route_name": "web_club_profile",
  "url_pattern": "/club/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_club_profile",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 81653,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/club`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 81670.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_club_profile:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/club`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18292"></a>
## FND-18292: Declared route i18n_web_club_profile

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0187",
  "route_name": "i18n_web_club_profile",
  "url_pattern": "/{_locale}/club/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_club_profile",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 82371,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/club`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 82393.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_club_profile:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/club`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_loca
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18293"></a>
## FND-18293: Declared route web_play_settings_is_on_vacation_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0188",
  "route_name": "web_play_settings_is_on_vacation_callback",
  "url_pattern": "/callback/play/settings/is-on-vacation",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_settings_is_on_vacation_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 86189,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/play/settings/is-on-vacation`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 86231.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_settings_is_on_vacation_callback:{tokens:[[`text`,`/callback/play/settings/is-on-vacation`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|f
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18294"></a>
## FND-18294: Declared route web_play_settings_vacation_time_remaining_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0189",
  "route_name": "web_play_settings_vacation_time_remaining_callback",
  "url_pattern": "/callback/play/settings/vacation-time-remaining",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_settings_vacation_time_remaining_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 86930,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/play/settings/vacation-time-remaining`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 86981.

```text
\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_settings_vacation_time_remaining_callback:{tokens:[[`text`,`/callback/play/settings/vacation-time-remaining`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18295"></a>
## FND-18295: Declared route web_analysis_game_callback_view_all

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0190",
  "route_name": "web_analysis_game_callback_view_all",
  "url_pattern": "/callback/analysis/game/{type}/{gameId}/all",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_game_callback_view_all",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 87689,
  "raw_route_declaration": "{tokens:[[`text`,`/all`],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 87725.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_game_callback_view_all:{tokens:[[`text`,`/all`],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 101656.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_game_callback_view_all:{tokens:[[`text`,`/all`],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 101656.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_game_callback_view_all:{tokens:[[`text`,`/all`],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18296"></a>
## FND-18296: Declared route web_move_condition_callback_get

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0191",
  "route_name": "web_move_condition_callback_get",
  "url_pattern": "/callback/move-conditions/game/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_move_condition_callback_get",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 88504,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/move-conditions/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 88536.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_move_condition_callback_get:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/move-conditions/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_E
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18297"></a>
## FND-18297: Declared route web_daily_callback_load_next_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0192",
  "route_name": "web_daily_callback_load_next_game",
  "url_pattern": "/callback/daily/game/{id}/next",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_daily_callback_load_next_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 89269,
  "raw_route_declaration": "{tokens:[[`text`,`/next`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 89303.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_callback_load_next_game:{tokens:[[`text`,`/next`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18298"></a>
## FND-18298: Declared route web_daily_callback_load_previous_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0193",
  "route_name": "web_daily_callback_load_previous_game",
  "url_pattern": "/callback/daily/game/{id}/previous",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_daily_callback_load_previous_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 90043,
  "raw_route_declaration": "{tokens:[[`text`,`/previous`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 90081.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_callback_load_previous_game:{tokens:[[`text`,`/previous`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18299"></a>
## FND-18299: Declared route web_game_callback_submit_move

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0194",
  "route_name": "web_game_callback_submit_move",
  "url_pattern": "/callback/game/{id}/submit-move",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_submit_move",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 90825,
  "raw_route_declaration": "{tokens:[[`text`,`/submit-move`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 90855.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_callback_submit_move:{tokens:[[`text`,`/submit-move`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18300"></a>
## FND-18300: Declared route web_game_callback_offer_draw

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0195",
  "route_name": "web_game_callback_offer_draw",
  "url_pattern": "/callback/game/{id}/offer-draw",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_offer_draw",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 91602,
  "raw_route_declaration": "{tokens:[[`text`,`/offer-draw`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 91631.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_game_callback_offer_draw:{tokens:[[`text`,`/offer-draw`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18301"></a>
## FND-18301: Declared route web_game_callback_decline_draw

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0196",
  "route_name": "web_game_callback_decline_draw",
  "url_pattern": "/callback/game/{id}/decline-draw",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_decline_draw",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 92377,
  "raw_route_declaration": "{tokens:[[`text`,`/decline-draw`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 92408.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_game_callback_decline_draw:{tokens:[[`text`,`/decline-draw`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|e
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18302"></a>
## FND-18302: Declared route web_game_callback_resign

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0197",
  "route_name": "web_game_callback_resign",
  "url_pattern": "/callback/game/{id}/resign",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_resign",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 93156,
  "raw_route_declaration": "{tokens:[[`text`,`/resign`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 93181.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_game_callback_resign:{tokens:[[`text`,`/resign`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|e
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18303"></a>
## FND-18303: Declared route web_game_seek_callback_accept_seek

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0198",
  "route_name": "web_game_seek_callback_accept_seek",
  "url_pattern": "/callback/game_seek/{id}/accept-seek",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_seek_callback_accept_seek",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 93923,
  "raw_route_declaration": "{tokens:[[`text`,`/accept-seek`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 93958.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_game_seek_callback_accept_seek:{tokens:[[`text`,`/accept-seek`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18304"></a>
## FND-18304: Declared route web_bucket

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0199",
  "route_name": "web_bucket",
  "url_pattern": "/callback/bucket",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_bucket",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 96306,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/bucket`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 96317.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_bucket:{tokens:[[`text`,`/callback/bucket`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 118469.

```text
|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_bucket:{tokens:[[`text`,`/callback/bucket`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 118469.

```text
|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_bucket:{tokens:[[`text`,`/callback/bucket`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18305"></a>
## FND-18305: Declared route i18n_web_bucket

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0200",
  "route_name": "i18n_web_bucket",
  "url_pattern": "/{_locale}/callback/bucket",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_bucket",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 96994,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/bucket`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 97010.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_bucket:{tokens:[[`text`,`/callback/bucket`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 119162.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_bucket:{tokens:[[`text`,`/callback/bucket`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 119162.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_bucket:{tokens:[[`text`,`/callback/bucket`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.
