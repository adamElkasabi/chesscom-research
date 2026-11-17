# routes — findings 201–300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18306"></a>
## FND-18306: Declared route web_game_callback_daily_chess_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0201",
  "route_name": "web_game_callback_daily_chess_challenge",
  "url_pattern": "/callback/game/daily/challenge/{opponent}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_daily_chess_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 97768,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`opponent`,!0],[`text`,`/callback/game/daily/challenge`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 97808.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_callback_daily_chess_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`opponent`,!0],[`text`,`/callback/game/daily/challenge`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18307"></a>
## FND-18307: Declared route web_game_callback_random_daily_chess_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0202",
  "route_name": "web_game_callback_random_daily_chess_challenge",
  "url_pattern": "/callback/game/random/daily/challenge",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_random_daily_chess_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 98545,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/game/random/daily/challenge`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 98592.

```text
s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_game_callback_random_daily_chess_challenge:{tokens:[[`text`,`/callback/game/random/daily/challenge`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18308"></a>
## FND-18308: Declared route web_game_seek_callback_decline_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0203",
  "route_name": "web_game_seek_callback_decline_challenge",
  "url_pattern": "/callback/game_seek/{id}/decline-challenge",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_seek_callback_decline_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 102973,
  "raw_route_declaration": "{tokens:[[`text`,`/decline-challenge`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 103014.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_seek_callback_decline_challenge:{tokens:[[`text`,`/decline-challenge`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18309"></a>
## FND-18309: Declared route web_user_callback_notices

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0204",
  "route_name": "web_user_callback_notices",
  "url_pattern": "/callback/user/notices",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_notices",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 104452,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/notices`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 104478.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_notices:{tokens:[[`text`,`/callback/user/notices`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18310"></a>
## FND-18310: Declared route web_user_callback_report_user

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0205",
  "route_name": "web_user_callback_report_user",
  "url_pattern": "/callback/report-user",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_report_user",
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
  "character_offset": 105166,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 105196.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_user_callback_report_user:{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 53479.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_user:{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 53479.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_user:{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18311"></a>
## FND-18311: Declared route web_user_callback_report_content

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0206",
  "route_name": "web_user_callback_report_content",
  "url_pattern": "/callback/report-forum-topic/{uuid}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_report_content",
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
  "character_offset": 105884,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/report-forum-topic`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 105917.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_content:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/report-forum-topic`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 54200.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_content:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/report-forum-topic`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 54200.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_content:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/report-forum-topic`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18312"></a>
## FND-18312: Declared route web_tv_callback_report

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0207",
  "route_name": "web_tv_callback_report",
  "url_pattern": "/chess-tv/callback/report/{reason}/{video}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_tv_callback_report",
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
  "character_offset": 106648,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`video`,!0],[`variable`,`/`,`[^/]++`,`reason`,!0],[`text`,`/chess-tv/callback/report`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 106671.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_tv_callback_report:{tokens:[[`variable`,`/`,`[^/]++`,`video`,!0],[`variable`,`/`,`[^/]++`,`reason`,!0],[`text`,`/chess-tv/callback/report`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 54954.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_tv_callback_report:{tokens:[[`variable`,`/`,`[^/]++`,`video`,!0],[`variable`,`/`,`[^/]++`,`reason`,!0],[`text`,`/chess-tv/callback/report`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 54954.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_tv_callback_report:{tokens:[[`variable`,`/`,`[^/]++`,`video`,!0],[`variable`,`/`,`[^/]++`,`reason`,!0],[`text`,`/chess-tv/callback/report`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18313"></a>
## FND-18313: Declared route web_user_callback_lifetime_score

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0208",
  "route_name": "web_user_callback_lifetime_score",
  "url_pattern": "/callback/user/lifetime-score/{user}/{opponent}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_lifetime_score",
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
  "character_offset": 107438,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`opponent`,!0],[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/user/lifetime-score`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 107471.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_lifetime_score:{tokens:[[`variable`,`/`,`[^/]++`,`opponent`,!0],[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/user/lifetime-score`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 56499.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_lifetime_score:{tokens:[[`variable`,`/`,`[^/]++`,`opponent`,!0],[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/user/lifetime-score`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 56499.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_lifetime_score:{tokens:[[`variable`,`/`,`[^/]++`,`opponent`,!0],[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/user/lifetime-score`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18314"></a>
## FND-18314: Declared route web_user_callback_username_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0209",
  "route_name": "web_user_callback_username_search",
  "url_pattern": "/callback/user/search/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_username_search",
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
  "character_offset": 108237,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/search`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 108271.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_username_search:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/search`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|e
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 57299.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_username_search:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/search`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|e
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 57299.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_username_search:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/search`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|e
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18315"></a>
## FND-18315: Declared route web_club_callback_get_data

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0210",
  "route_name": "web_club_callback_get_data",
  "url_pattern": "/callback/club/data/{id}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_club_callback_get_data",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 112155,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 112182.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_club_callback_get_data:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18316"></a>
## FND-18316: Declared route web_club_callback_user_admin_clubs

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0211",
  "route_name": "web_club_callback_user_admin_clubs",
  "url_pattern": "/callback/clubs/user/admin",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_club_callback_user_admin_clubs",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 112901,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/clubs/user/admin`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 112936.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_club_callback_user_admin_clubs:{tokens:[[`text`,`/callback/clubs/user/admin`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18317"></a>
## FND-18317: Declared route web_club_callback_user_member_clubs

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0212",
  "route_name": "web_club_callback_user_member_clubs",
  "url_pattern": "/callback/clubs/user/member",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_club_callback_user_member_clubs",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 113628,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/clubs/user/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 113664.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_club_callback_user_member_clubs:{tokens:[[`text`,`/callback/clubs/user/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18318"></a>
## FND-18318: Declared route web_security_callback_user_roles

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0213",
  "route_name": "web_security_callback_user_roles",
  "url_pattern": "/callback/security/user/roles",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_security_callback_user_roles",
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
  "character_offset": 114357,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/security/user/roles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 114390.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_security_callback_user_roles:{tokens:[[`text`,`/callback/security/user/roles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 95632.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_callback_user_roles:{tokens:[[`text`,`/callback/security/user/roles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 95632.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_callback_user_roles:{tokens:[[`text`,`/callback/security/user/roles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18319"></a>
## FND-18319: Declared route web_alert_callback_alerts

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0214",
  "route_name": "web_alert_callback_alerts",
  "url_pattern": "/callback/alert/alerts",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_alert_callback_alerts",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 115080,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/alert/alerts`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 115106.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_alert_callback_alerts:{tokens:[[`text`,`/callback/alert/alerts`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18320"></a>
## FND-18320: Declared route web_game_seek_callback_user_seeks

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0215",
  "route_name": "web_game_seek_callback_user_seeks",
  "url_pattern": "/callback/game_seek/user-seeks",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_seek_callback_user_seeks",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 115789,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/game_seek/user-seeks`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 115823.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_seek_callback_user_seeks:{tokens:[[`text`,`/callback/game_seek/user-seeks`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18321"></a>
## FND-18321: Declared route web_tv_callback_schedule

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0216",
  "route_name": "web_tv_callback_schedule",
  "url_pattern": "/chess-tv/callback/schedule/{locale}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tv_callback_schedule",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 116514,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`locale`,!0],[`text`,`/chess-tv/callback/schedule`]],defaults:{locale:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 116539.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tv_callback_schedule:{tokens:[[`variable`,`/`,`[^/]++`,`locale`,!0],[`text`,`/chess-tv/callback/schedule`]],defaults:{locale:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18322"></a>
## FND-18322: Declared route i18n_web_tv_callback_schedule

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0217",
  "route_name": "i18n_web_tv_callback_schedule",
  "url_pattern": "/{_locale}/chess-tv/callback/schedule/{locale}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tv_callback_schedule",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 117277,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`locale`,!0],[`text`,`/chess-tv/callback/schedule`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{locale:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 117307.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tv_callback_schedule:{tokens:[[`variable`,`/`,`[^/]++`,`locale`,!0],[`text`,`/chess-tv/callback/schedule`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{local
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18323"></a>
## FND-18323: Declared route web_live_recent_time_control

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0218",
  "route_name": "web_live_recent_time_control",
  "url_pattern": "/live/recent-time-control",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_live_recent_time_control",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 118126,
  "raw_route_declaration": "{tokens:[[`text`,`/live/recent-time-control`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 118155.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_live_recent_time_control:{tokens:[[`text`,`/live/recent-time-control`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18324"></a>
## FND-18324: Declared route i18n_web_live_recent_time_control

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0219",
  "route_name": "i18n_web_live_recent_time_control",
  "url_pattern": "/{_locale}/live/recent-time-control",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_live_recent_time_control",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 118841,
  "raw_route_declaration": "{tokens:[[`text`,`/live/recent-time-control`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 118875.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_live_recent_time_control:{tokens:[[`text`,`/live/recent-time-control`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirem
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18325"></a>
## FND-18325: Declared route web_game_seek_callback_delete_challenge

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0220",
  "route_name": "web_game_seek_callback_delete_challenge",
  "url_pattern": "/callback/game_seek/{id}/delete-challenge",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_seek_callback_delete_challenge",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0781"
  ],
  "character_offset": 119642,
  "raw_route_declaration": "{tokens:[[`text`,`/delete-challenge`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 119682.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_seek_callback_delete_challenge:{tokens:[[`text`,`/delete-challenge`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_D
```

**Source references:** SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18326"></a>
## FND-18326: Declared route web_master_games_callback_player

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0221",
  "route_name": "web_master_games_callback_player",
  "url_pattern": "/callback/games/player",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_master_games_callback_player",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1136"
  ],
  "character_offset": 560,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/games/player`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1136** `research/shared.533ee0c1.chunk.js` — [preserved redacted evidence](../evidence/text/b524fbc66b2962944ac6242d90d120d6f2942c40f17da95033d795e34b2a0e42.js)
  Character offset 593.

```text
s=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_master_games_callback_player:{tokens:[[`text`,`/callback/games/player`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```

**Source references:** SRC-1136  
**URL references:** None independently associated  
**Related findings:** FND-18123, FND-18129

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18327"></a>
## FND-18327: Declared route web_courses_shop

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0222",
  "route_name": "web_courses_shop",
  "url_pattern": "/courses/all",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_courses_shop",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1136"
  ],
  "character_offset": 1281,
  "raw_route_declaration": "{tokens:[[`text`,`/courses/all`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1136** `research/shared.533ee0c1.chunk.js` — [preserved redacted evidence](../evidence/text/b524fbc66b2962944ac6242d90d120d6f2942c40f17da95033d795e34b2a0e42.js)
  Character offset 1298.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_courses_shop:{tokens:[[`text`,`/courses/all`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_
```

**Source references:** SRC-1136  
**URL references:** None independently associated  
**Related findings:** FND-18123, FND-18129, FND-18326

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18328"></a>
## FND-18328: Declared route i18n_web_courses_shop

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0223",
  "route_name": "i18n_web_courses_shop",
  "url_pattern": "/{_locale}/courses/all",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_courses_shop",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1136"
  ],
  "character_offset": 1971,
  "raw_route_declaration": "{tokens:[[`text`,`/courses/all`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1136** `research/shared.533ee0c1.chunk.js` — [preserved redacted evidence](../evidence/text/b524fbc66b2962944ac6242d90d120d6f2942c40f17da95033d795e34b2a0e42.js)
  Character offset 1993.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_courses_shop:{tokens:[[`text`,`/courses/all`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(
```

**Source references:** SRC-1136  
**URL references:** None independently associated  
**Related findings:** FND-18123, FND-18129, FND-18326

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18329"></a>
## FND-18329: Declared route web_analysis_board_editor_collections

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0224",
  "route_name": "web_analysis_board_editor_collections",
  "url_pattern": "/analysis/collections",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_board_editor_collections",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 8385,
  "raw_route_declaration": "{tokens:[[`text`,`/analysis/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 8423.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_collections:{tokens:[[`text`,`/analysis/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 8423.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_collections:{tokens:[[`text`,`/analysis/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18330"></a>
## FND-18330: Declared route web_eco_callback_stats_fen_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0225",
  "route_name": "web_eco_callback_stats_fen_search",
  "url_pattern": "/callback/eco/search/fen",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_eco_callback_stats_fen_search",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 10568,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/eco/search/fen`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 10602.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_eco_callback_stats_fen_search:{tokens:[[`text`,`/callback/eco/search/fen`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 10602.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_eco_callback_stats_fen_search:{tokens:[[`text`,`/callback/eco/search/fen`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18331"></a>
## FND-18331: Declared route web_analysis_game_callback_game_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0226",
  "route_name": "web_analysis_game_callback_game_view",
  "url_pattern": "/callback/analysis/game/{type}/{gameId}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_game_callback_game_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 11293,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 11330.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_game_callback_game_view:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 11330.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_game_callback_game_view:{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18332"></a>
## FND-18332: Declared route web_page_new_train

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0227",
  "route_name": "web_page_new_train",
  "url_pattern": "/new-train",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_page_new_train",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 12820,
  "raw_route_declaration": "{tokens:[[`text`,`/new-train`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 12839.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_page_new_train:{tokens:[[`text`,`/new-train`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 12839.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_page_new_train:{tokens:[[`text`,`/new-train`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18333"></a>
## FND-18333: Declared route web_eco_callback_search_opening_stats

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0228",
  "route_name": "web_eco_callback_search_opening_stats",
  "url_pattern": "/callback/eco/search/{cleanUrl}/{username}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_eco_callback_search_opening_stats",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 14238,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 14276.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_eco_callback_search_opening_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 14276.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_eco_callback_search_opening_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18334"></a>
## FND-18334: Declared route web_analysis_game_callback_retry_attempt

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0229",
  "route_name": "web_analysis_game_callback_retry_attempt",
  "url_pattern": "/callback/analysis/retry",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_game_callback_retry_attempt",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 15906,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/analysis/retry`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 15947.

```text
.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_game_callback_retry_attempt:{tokens:[[`text`,`/callback/analysis/retry`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 15947.

```text
.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_game_callback_retry_attempt:{tokens:[[`text`,`/callback/analysis/retry`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18335"></a>
## FND-18335: Declared route web_analysis_game_callback_self_analysis_create

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0230",
  "route_name": "web_analysis_game_callback_self_analysis_create",
  "url_pattern": "/callback/analysis/self",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_game_callback_self_analysis_create",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 16638,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/analysis/self`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 16686.

```text
]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_game_callback_self_analysis_create:{tokens:[[`text`,`/callback/analysis/self`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 16686.

```text
]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_game_callback_self_analysis_create:{tokens:[[`text`,`/callback/analysis/self`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18336"></a>
## FND-18336: Declared route web_analysis_library_game_callback_self_analysis_create

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0231",
  "route_name": "web_analysis_library_game_callback_self_analysis_create",
  "url_pattern": "/callback/analysis/library/self",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_game_callback_self_analysis_create",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 17376,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/analysis/library/self`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 17432.

```text
t`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_library_game_callback_self_analysis_create:{tokens:[[`text`,`/callback/analysis/library/self`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 17432.

```text
t`,!0]],methods:[`POST`],schemes:[`https`]},web_analysis_library_game_callback_self_analysis_create:{tokens:[[`text`,`/callback/analysis/library/self`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18337"></a>
## FND-18337: Declared route web_analysis_shared_board

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0232",
  "route_name": "web_analysis_shared_board",
  "url_pattern": "/analysis/room/{sessionId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_shared_board",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 18833,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}`,`sessionId`,!0],[`text`,`/analysis/room`]],defaults:{host:`www.chess-dev.com`},requirements:{sessionId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 18859.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_shared_board:{tokens:[[`variable`,`/`,`[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}`,`sessionId`,!0],[`text`,`/analysis/room`]],defaults:{host:`www.chess-dev.com`},requirements:{sessionId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_loca
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 18859.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_shared_board:{tokens:[[`variable`,`/`,`[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}`,`sessionId`,!0],[`text`,`/analysis/room`]],defaults:{host:`www.chess-dev.com`},requirements:{sessionId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_loca
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18338"></a>
## FND-18338: Declared route web_analysis_saved

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0233",
  "route_name": "web_analysis_saved",
  "url_pattern": "/analysis/saved",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_saved",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 19675,
  "raw_route_declaration": "{tokens:[[`text`,`/analysis/saved`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 19694.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_saved:{tokens:[[`text`,`/analysis/saved`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 19694.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_saved:{tokens:[[`text`,`/analysis/saved`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18339"></a>
## FND-18339: Declared route i18n_web_analysis_board_editor_collections

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0234",
  "route_name": "i18n_web_analysis_board_editor_collections",
  "url_pattern": "/{_locale}/analysis/collections",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_board_editor_collections",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 21152,
  "raw_route_declaration": "{tokens:[[`text`,`/analysis/collections`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 21195.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_board_editor_collections:{tokens:[[`text`,`/analysis/collections`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 21195.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_board_editor_collections:{tokens:[[`text`,`/analysis/collections`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18340"></a>
## FND-18340: Declared route i18n_web_page_new_train

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0235",
  "route_name": "i18n_web_page_new_train",
  "url_pattern": "/{_locale}/new-train",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_page_new_train",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 22916,
  "raw_route_declaration": "{tokens:[[`text`,`/new-train`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 22940.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_page_new_train:{tokens:[[`text`,`/new-train`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 22940.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_page_new_train:{tokens:[[`text`,`/new-train`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18341"></a>
## FND-18341: Declared route i18n_web_analysis_shared_board

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0236",
  "route_name": "i18n_web_analysis_shared_board",
  "url_pattern": "/{_locale}/analysis/room/{sessionId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_shared_board",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 25295,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}`,`sessionId`,!0],[`text`,`/analysis/room`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{sessionId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 18859.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_shared_board:{tokens:[[`variable`,`/`,`[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}`,`sessionId`,!0],[`text`,`/analysis/room`]],defaults:{host:`www.chess-dev.com`},requirements:{sessionId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_loca
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 18859.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_shared_board:{tokens:[[`variable`,`/`,`[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}`,`sessionId`,!0],[`text`,`/analysis/room`]],defaults:{host:`www.chess-dev.com`},requirements:{sessionId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_loca
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18342"></a>
## FND-18342: Declared route i18n_web_analysis_saved

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0237",
  "route_name": "i18n_web_analysis_saved",
  "url_pattern": "/{_locale}/analysis/saved",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_saved",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 26223,
  "raw_route_declaration": "{tokens:[[`text`,`/analysis/saved`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 26247.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_saved:{tokens:[[`text`,`/analysis/saved`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 26247.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_saved:{tokens:[[`text`,`/analysis/saved`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18343"></a>
## FND-18343: Declared route web_shared_analysis_board_editor

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0238",
  "route_name": "web_shared_analysis_board_editor",
  "url_pattern": "/a/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_shared_analysis_board_editor",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 27004,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 27037.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_shared_analysis_board_editor:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 27037.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_shared_analysis_board_editor:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18344"></a>
## FND-18344: Declared route web_shared_analysis_board_editor_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0239",
  "route_name": "web_shared_analysis_board_editor_tab",
  "url_pattern": "/a/{id}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_shared_analysis_board_editor_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 27734,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18345"></a>
## FND-18345: Declared route web_analysis_library_user_collection_game_legacy

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0240",
  "route_name": "web_analysis_library_user_collection_game_legacy",
  "url_pattern": "/analysis/library/{libraryUserCollectionGameId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_user_collection_game_legacy",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 30498,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 30547.

```text
[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection_game_legacy:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 30547.

```text
[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection_game_legacy:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18346"></a>
## FND-18346: Declared route web_analysis_library_user_collection_game_legacy_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0241",
  "route_name": "web_analysis_library_user_collection_game_legacy_tab",
  "url_pattern": "/analysis/library/{libraryUserCollectionGameId}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_user_collection_game_legacy_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 31284,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18347"></a>
## FND-18347: Declared route web_analysis_library_user_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0242",
  "route_name": "web_analysis_library_user_collection",
  "url_pattern": "/analysis/collection/{collectionSlug}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_user_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 32246,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 32283.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection:{tokens:[[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 32283.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection:{tokens:[[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18348"></a>
## FND-18348: Declared route web_analysis_library_user_collection_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0243",
  "route_name": "web_analysis_library_user_collection_tab",
  "url_pattern": "/analysis/collection/{collectionSlug}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_user_collection_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 33010,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18349"></a>
## FND-18349: Declared route web_analysis_library_user_collection_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0244",
  "route_name": "web_analysis_library_user_collection_game",
  "url_pattern": "/analysis/collection/{collectionSlug}/{libraryUserCollectionGameId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_user_collection_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 33950,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 33992.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection_game:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 33992.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection_game:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18350"></a>
## FND-18350: Declared route web_analysis_library_user_collection_game_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0245",
  "route_name": "web_analysis_library_user_collection_game_tab",
  "url_pattern": "/analysis/collection/{collectionSlug}/{libraryUserCollectionGameId}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_user_collection_game_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 34778,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18351"></a>
## FND-18351: Declared route web_analysis_calculator

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0246",
  "route_name": "web_analysis_calculator",
  "url_pattern": "/calculator",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_calculator",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 35782,
  "raw_route_declaration": "{tokens:[[`text`,`/calculator`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 35806.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_calculator:{tokens:[[`text`,`/calculator`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 35806.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_calculator:{tokens:[[`text`,`/calculator`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18352"></a>
## FND-18352: Declared route i18n_web_shared_analysis_board_editor

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0247",
  "route_name": "i18n_web_shared_analysis_board_editor",
  "url_pattern": "/{_locale}/a/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_shared_analysis_board_editor",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 36478,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 36516.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_shared_analysis_board_editor:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 36516.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_shared_analysis_board_editor:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:`
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18353"></a>
## FND-18353: Declared route i18n_web_shared_analysis_board_editor_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0248",
  "route_name": "i18n_web_shared_analysis_board_editor_tab",
  "url_pattern": "/{_locale}/a/{id}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_shared_analysis_board_editor_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 37294,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/a`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18354"></a>
## FND-18354: Declared route i18n_web_analysis_library_user_collection_game_legacy

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0249",
  "route_name": "i18n_web_analysis_library_user_collection_game_legacy",
  "url_pattern": "/{_locale}/analysis/library/{libraryUserCollectionGameId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_library_user_collection_game_legacy",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 40316,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 40370.

```text
]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_library_user_collection_game_legacy:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defa
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 40370.

```text
]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_library_user_collection_game_legacy:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defa
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18355"></a>
## FND-18355: Declared route i18n_web_analysis_library_user_collection_game_legacy_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0250",
  "route_name": "i18n_web_analysis_library_user_collection_game_legacy_tab",
  "url_pattern": "/{_locale}/analysis/library/{libraryUserCollectionGameId}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_library_user_collection_game_legacy_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 41188,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`text`,`/analysis/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18356"></a>
## FND-18356: Declared route i18n_web_analysis_library_user_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0251",
  "route_name": "i18n_web_analysis_library_user_collection",
  "url_pattern": "/{_locale}/analysis/collection/{collectionSlug}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_library_user_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 42236,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 42278.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_library_user_collection:{tokens:[[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 42278.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_library_user_collection:{tokens:[[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18357"></a>
## FND-18357: Declared route i18n_web_analysis_library_user_collection_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0252",
  "route_name": "i18n_web_analysis_library_user_collection_tab",
  "url_pattern": "/{_locale}/analysis/collection/{collectionSlug}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_library_user_collection_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 43086,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18358"></a>
## FND-18358: Declared route i18n_web_analysis_library_user_collection_game

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0253",
  "route_name": "i18n_web_analysis_library_user_collection_game",
  "url_pattern": "/{_locale}/analysis/collection/{collectionSlug}/{libraryUserCollectionGameId}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_library_user_collection_game",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 44112,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 33992.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection_game:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 33992.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_user_collection_game:{tokens:[[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18359"></a>
## FND-18359: Declared route i18n_web_analysis_library_user_collection_game_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0254",
  "route_name": "i18n_web_analysis_library_user_collection_game_tab",
  "url_pattern": "/{_locale}/analysis/collection/{collectionSlug}/{libraryUserCollectionGameId}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_library_user_collection_game_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 45026,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`libraryUserCollectionGameId`,!0],[`variable`,`/`,`[^/]++`,`collectionSlug`,!0],[`text`,`/analysis/collection`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18360"></a>
## FND-18360: Declared route i18n_web_analysis_calculator

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0255",
  "route_name": "i18n_web_analysis_calculator",
  "url_pattern": "/{_locale}/calculator",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_calculator",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 46116,
  "raw_route_declaration": "{tokens:[[`text`,`/calculator`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 46145.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_calculator:{tokens:[[`text`,`/calculator`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 46145.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_calculator:{tokens:[[`text`,`/calculator`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18361"></a>
## FND-18361: Declared route web_analysis_library_game_callback_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0256",
  "route_name": "web_analysis_library_game_callback_view",
  "url_pattern": "/callback/analysis/library/{lucgId}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_library_game_callback_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 59727,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`lucgId`,!0],[`text`,`/callback/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 59767.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_game_callback_view:{tokens:[[`variable`,`/`,`[^/]++`,`lucgId`,!0],[`text`,`/callback/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 59767.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_library_game_callback_view:{tokens:[[`variable`,`/`,`[^/]++`,`lucgId`,!0],[`text`,`/callback/analysis/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18362"></a>
## FND-18362: Declared route web_library_collection_add_bookmark

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0257",
  "route_name": "web_library_collection_add_bookmark",
  "url_pattern": "/callback/library/collections/{uuid}/bookmarks",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_add_bookmark",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 60497,
  "raw_route_declaration": "{tokens:[[`text`,`/bookmarks`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 60533.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_collection_add_bookmark:{tokens:[[`text`,`/bookmarks`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|e
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 60533.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_collection_add_bookmark:{tokens:[[`text`,`/bookmarks`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|e
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18363"></a>
## FND-18363: Declared route web_library_collection_add_lookup

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0258",
  "route_name": "web_library_collection_add_lookup",
  "url_pattern": "/callback/library/collections/{uuid}/lookups",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_add_lookup",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 61287,
  "raw_route_declaration": "{tokens:[[`text`,`/lookups`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 61321.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_add_lookup:{tokens:[[`text`,`/lookups`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 61321.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_add_lookup:{tokens:[[`text`,`/lookups`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18364"></a>
## FND-18364: Declared route web_library_collection_add_participant

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0259",
  "route_name": "web_library_collection_add_participant",
  "url_pattern": "/callback/library/collections/{uuid}/participants",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_add_participant",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 62073,
  "raw_route_declaration": "{tokens:[[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 62112.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_add_participant:{tokens:[[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_D
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 62112.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_add_participant:{tokens:[[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_D
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18365"></a>
## FND-18365: Declared route web_library_callback_add_from_pgn_to_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0260",
  "route_name": "web_library_callback_add_from_pgn_to_collection",
  "url_pattern": "/callback/library/collections/{uuid}/actions/add-from-pgn",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_add_from_pgn_to_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 62869,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/add-from-pgn`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 62917.

```text
]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_add_from_pgn_to_collection:{tokens:[[`text`,`/actions/add-from-pgn`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 62917.

```text
]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_add_from_pgn_to_collection:{tokens:[[`text`,`/actions/add-from-pgn`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18366"></a>
## FND-18366: Declared route web_library_collection_add_items

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0261",
  "route_name": "web_library_collection_add_items",
  "url_pattern": "/callback/library/collections/{uuid}/items-bulk",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_add_items",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 63682,
  "raw_route_declaration": "{tokens:[[`text`,`/items-bulk`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 63715.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_add_items:{tokens:[[`text`,`/items-bulk`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 63715.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_add_items:{tokens:[[`text`,`/items-bulk`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18367"></a>
## FND-18367: Declared route web_library_callback_add_from_url_to_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0262",
  "route_name": "web_library_callback_add_from_url_to_collection",
  "url_pattern": "/callback/library/collections/{uuid}/actions/add-from-url",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_add_from_url_to_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 64470,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/add-from-url`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 64518.

```text
]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_add_from_url_to_collection:{tokens:[[`text`,`/actions/add-from-url`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 64518.

```text
]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_add_from_url_to_collection:{tokens:[[`text`,`/actions/add-from-url`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18368"></a>
## FND-18368: Declared route web_library_collection_download_games

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0263",
  "route_name": "web_library_collection_download_games",
  "url_pattern": "/callback/library/collections/{uuid}/actions/download-pgn",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_download_games",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 65283,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/download-pgn`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 65321.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_download_games:{tokens:[[`text`,`/actions/download-pgn`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 65321.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_download_games:{tokens:[[`text`,`/actions/download-pgn`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18369"></a>
## FND-18369: Declared route web_library_callback_collection_items

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0264",
  "route_name": "web_library_callback_collection_items",
  "url_pattern": "/callback/library/collections/{uuid}/items",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_collection_items",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 66086,
  "raw_route_declaration": "{tokens:[[`text`,`/items`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 66124.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_collection_items:{tokens:[[`text`,`/items`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 66124.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_collection_items:{tokens:[[`text`,`/items`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18370"></a>
## FND-18370: Declared route web_library_community_collections

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0265",
  "route_name": "web_library_community_collections",
  "url_pattern": "/callback/library/community/collections",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_community_collections",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 66873,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/library/community/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 66907.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_community_collections:{tokens:[[`text`,`/callback/library/community/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 66907.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_community_collections:{tokens:[[`text`,`/callback/library/community/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18371"></a>
## FND-18371: Declared route web_library_callback_copy_into_new_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0266",
  "route_name": "web_library_callback_copy_into_new_collection",
  "url_pattern": "/callback/library/collections/{uuid}/actions/copy-into-new",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_copy_into_new_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 67612,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/copy-into-new`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 67658.

```text
\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_copy_into_new_collection:{tokens:[[`text`,`/actions/copy-into-new`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|d
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 67658.

```text
\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_copy_into_new_collection:{tokens:[[`text`,`/actions/copy-into-new`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|d
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18372"></a>
## FND-18372: Declared route web_library_callback_delete_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0267",
  "route_name": "web_library_callback_delete_collection",
  "url_pattern": "/callback/library/collections/{uuid}",
  "http_methods": [
    "DELETE"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_delete_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 68424,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 68463.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_delete_collection:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 68463.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_delete_collection:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18373"></a>
## FND-18373: Declared route web_library_bookmarks

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0268",
  "route_name": "web_library_bookmarks",
  "url_pattern": "/callback/library/bookmarks",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_bookmarks",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 69197,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/library/bookmarks`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 69219.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_library_bookmarks:{tokens:[[`text`,`/callback/library/bookmarks`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 69219.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_library_bookmarks:{tokens:[[`text`,`/callback/library/bookmarks`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18374"></a>
## FND-18374: Declared route web_library_collections

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0269",
  "route_name": "web_library_collections",
  "url_pattern": "/callback/library/collections",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collections",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 69912,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 69936.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_collections:{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 69936.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_collections:{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18375"></a>
## FND-18375: Declared route web_library_callback_publish_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0270",
  "route_name": "web_library_callback_publish_collection",
  "url_pattern": "/callback/library/collections/{uuid}/actions/publish",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_publish_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 70631,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/publish`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 70671.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_publish_collection:{tokens:[[`text`,`/actions/publish`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|d
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 70671.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_publish_collection:{tokens:[[`text`,`/actions/publish`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|d
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18376"></a>
## FND-18376: Declared route web_library_collection_remove_root_bookmark

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0271",
  "route_name": "web_library_collection_remove_root_bookmark",
  "url_pattern": "/callback/library/collections/{uuid}/actions/remove-root-bookmark",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_remove_root_bookmark",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 71431,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/remove-root-bookmark`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 71475.

```text
^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_remove_root_bookmark:{tokens:[[`text`,`/actions/remove-root-bookmark`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 71475.

```text
^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_remove_root_bookmark:{tokens:[[`text`,`/actions/remove-root-bookmark`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18377"></a>
## FND-18377: Declared route web_library_collection_remove_items

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0272",
  "route_name": "web_library_collection_remove_items",
  "url_pattern": "/callback/library/collections/{uuid}/actions/remove-items",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_remove_items",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 72248,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/remove-items`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 72284.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_remove_items:{tokens:[[`text`,`/actions/remove-items`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 72284.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_remove_items:{tokens:[[`text`,`/actions/remove-items`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18378"></a>
## FND-18378: Declared route web_library_collection_remove_lookup

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0273",
  "route_name": "web_library_collection_remove_lookup",
  "url_pattern": "/callback/library/collections/{uuid}/lookups/{lookup}",
  "http_methods": [
    "DELETE"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_remove_lookup",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 73049,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`lookup`,!0],[`text`,`/lookups`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 73086.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_remove_lookup:{tokens:[[`variable`,`/`,`[^/]++`,`lookup`,!0],[`text`,`/lookups`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_B
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 73086.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_remove_lookup:{tokens:[[`variable`,`/`,`[^/]++`,`lookup`,!0],[`text`,`/lookups`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_B
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18379"></a>
## FND-18379: Declared route web_library_collection_remove_participant

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0274",
  "route_name": "web_library_collection_remove_participant",
  "url_pattern": "/callback/library/collections/{uuid}/participants/{userId}",
  "http_methods": [
    "DELETE"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_remove_participant",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 73878,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 73920.

```text
^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_library_collection_remove_participant:{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 73920.

```text
^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_library_collection_remove_participant:{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18380"></a>
## FND-18380: Declared route web_library_callback_single_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0275",
  "route_name": "web_library_callback_single_collection",
  "url_pattern": "/callback/library/collections/{uuid}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_single_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 74717,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 68463.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_delete_collection:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 68463.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_delete_collection:{tokens:[[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18381"></a>
## FND-18381: Declared route web_library_shared_collections

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0276",
  "route_name": "web_library_shared_collections",
  "url_pattern": "/callback/library/shared",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_shared_collections",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 75487,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/library/shared`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 75518.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_shared_collections:{tokens:[[`text`,`/callback/library/shared`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 75518.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_shared_collections:{tokens:[[`text`,`/callback/library/shared`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18382"></a>
## FND-18382: Declared route web_library_callback_unpublish_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0277",
  "route_name": "web_library_callback_unpublish_collection",
  "url_pattern": "/callback/library/collections/{uuid}/actions/unpublish",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_unpublish_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 76208,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/unpublish`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 76250.

```text
)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_unpublish_collection:{tokens:[[`text`,`/actions/unpublish`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 76250.

```text
)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_unpublish_collection:{tokens:[[`text`,`/actions/unpublish`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18383"></a>
## FND-18383: Declared route web_library_callback_update_lucg_details

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0278",
  "route_name": "web_library_callback_update_lucg_details",
  "url_pattern": "/callback/library/lucgs/{uuid}/details",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_update_lucg_details",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 77012,
  "raw_route_declaration": "{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 77053.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_update_lucg_details:{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 77053.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_update_lucg_details:{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18384"></a>
## FND-18384: Declared route web_library_callback_update_collection_privacy_settings

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0279",
  "route_name": "web_library_callback_update_collection_privacy_settings",
  "url_pattern": "/callback/library/collections/{uuid}/privacy-settings",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_update_collection_privacy_settings",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 77799,
  "raw_route_declaration": "{tokens:[[`text`,`/privacy-settings`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 77855.

```text
t`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_update_collection_privacy_settings:{tokens:[[`text`,`/privacy-settings`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 77855.

```text
t`,!0]],methods:[`POST`],schemes:[`https`]},web_library_callback_update_collection_privacy_settings:{tokens:[[`text`,`/privacy-settings`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18385"></a>
## FND-18385: Declared route web_library_collection_update_thumbnail

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0280",
  "route_name": "web_library_collection_update_thumbnail",
  "url_pattern": "/callback/library/collections/{uuid}/thumbnail",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_update_thumbnail",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 78616,
  "raw_route_declaration": "{tokens:[[`text`,`/thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 78656.

```text
.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_update_thumbnail:{tokens:[[`text`,`/thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|e
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 78656.

```text
.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_update_thumbnail:{tokens:[[`text`,`/thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|e
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18386"></a>
## FND-18386: Declared route web_library_collection_upload_thumbnail

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0281",
  "route_name": "web_library_collection_upload_thumbnail",
  "url_pattern": "/callback/library/collections/{uuid}/actions/upload-thumbnail",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_upload_thumbnail",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 79410,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/upload-thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 79450.

```text
.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_upload_thumbnail:{tokens:[[`text`,`/actions/upload-thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_C
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 79450.

```text
.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_upload_thumbnail:{tokens:[[`text`,`/actions/upload-thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_C
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18387"></a>
## FND-18387: Declared route web_library_collection_update_participant

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0282",
  "route_name": "web_library_collection_update_participant",
  "url_pattern": "/callback/library/collections/{uuid}/participants/{userId}",
  "http_methods": [
    "PUT"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_update_participant",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 80219,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 73920.

```text
^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_library_collection_remove_participant:{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 73920.

```text
^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_library_collection_remove_participant:{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18388"></a>
## FND-18388: Declared route web_library_callback_create_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0283",
  "route_name": "web_library_callback_create_collection",
  "url_pattern": "/callback/library/collections",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_create_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 81055,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 69936.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_collections:{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 69936.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_collections:{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18389"></a>
## FND-18389: Declared route web_library_collection_update_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0284",
  "route_name": "web_library_collection_update_collection",
  "url_pattern": "/library/collections/{uuid}/actions/update",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_update_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 81790,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 81831.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_update_collection:{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 81831.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_update_collection:{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18390"></a>
## FND-18390: Declared route web_library_create_collection

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0285",
  "route_name": "web_library_create_collection",
  "url_pattern": "/library/collections",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_create_collection",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 82581,
  "raw_route_declaration": "{tokens:[[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 82611.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_create_collection:{tokens:[[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 82611.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_create_collection:{tokens:[[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18391"></a>
## FND-18391: Declared route web_library_collection_update_collection_json

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0286",
  "route_name": "web_library_collection_update_collection_json",
  "url_pattern": "/library/collections/{uuid}/actions/update",
  "http_methods": [
    "PUT"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_collection_update_collection_json",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 83298,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 81831.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_update_collection:{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 81831.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_library_collection_update_collection:{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18392"></a>
## FND-18392: Declared route web_library_home

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0287",
  "route_name": "web_library_home",
  "url_pattern": "/library",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_home",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 84093,
  "raw_route_declaration": "{tokens:[[`text`,`/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 84110.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]},web_library_home:{tokens:[[`text`,`/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 84110.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]},web_library_home:{tokens:[[`text`,`/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18393"></a>
## FND-18393: Declared route web_library_callback_collection_privacy

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0288",
  "route_name": "web_library_callback_collection_privacy",
  "url_pattern": "/callback/library/collections/{uuid}/actions/privacy",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_library_callback_collection_privacy",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 84784,
  "raw_route_declaration": "{tokens:[[`text`,`/actions/privacy`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 84824.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_collection_privacy:{tokens:[[`text`,`/actions/privacy`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|d
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 84824.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_library_callback_collection_privacy:{tokens:[[`text`,`/actions/privacy`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|d
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18394"></a>
## FND-18394: Declared route i18n_web_library_home

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0289",
  "route_name": "i18n_web_library_home",
  "url_pattern": "/{_locale}/library",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_library_home",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 85584,
  "raw_route_declaration": "{tokens:[[`text`,`/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 85606.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},i18n_web_library_home:{tokens:[[`text`,`/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 85606.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},i18n_web_library_home:{tokens:[[`text`,`/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18395"></a>
## FND-18395: Declared route web_friend_request_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0290",
  "route_name": "web_friend_request_callback",
  "url_pattern": "/callback/friend/request/{user}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_friend_request_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 86361,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 86389.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_friend_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 86389.

```text
szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_friend_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18396"></a>
## FND-18396: Declared route web_friend_accept_request_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0291",
  "route_name": "web_friend_accept_request_callback",
  "url_pattern": "/callback/friend/accept/{user}",
  "http_methods": [
    "PUT"
  ],
  "title": "not observed",
  "purpose": "declared route web_friend_accept_request_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 87116,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/accept`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 87151.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_friend_accept_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/accept`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 87151.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_friend_accept_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/accept`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18397"></a>
## FND-18397: Declared route web_member_callback_block_member

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0292",
  "route_name": "web_member_callback_block_member",
  "url_pattern": "/callback/member/block/{username}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_callback_block_member",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 87876,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/block`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 87909.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]},web_member_callback_block_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/block`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 87909.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]},web_member_callback_block_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/block`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18398"></a>
## FND-18398: Declared route web_friend_cancel_request_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0293",
  "route_name": "web_friend_cancel_request_callback",
  "url_pattern": "/callback/friend/cancel/request/{user}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_friend_cancel_request_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 88638,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/cancel/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 88673.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_friend_cancel_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/cancel/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 88673.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_friend_cancel_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/cancel/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18399"></a>
## FND-18399: Declared route web_user_callback_valid_username

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0294",
  "route_name": "web_user_callback_valid_username",
  "url_pattern": "/callback/user/valid",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_valid_username",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 89407,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/valid`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 89440.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_valid_username:{tokens:[[`text`,`/callback/user/valid`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 89440.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_valid_username:{tokens:[[`text`,`/callback/user/valid`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18400"></a>
## FND-18400: Declared route i18n_web_user_callback_valid_username

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0295",
  "route_name": "i18n_web_user_callback_valid_username",
  "url_pattern": "/{_locale}/callback/user/valid",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_user_callback_valid_username",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 90121,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/valid`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 90159.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_user_callback_valid_username:{tokens:[[`text`,`/callback/user/valid`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 90159.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_user_callback_valid_username:{tokens:[[`text`,`/callback/user/valid`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18401"></a>
## FND-18401: Declared route web_friend_decline_request_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0296",
  "route_name": "web_friend_decline_request_callback",
  "url_pattern": "/callback/friend/decline/request/{user}",
  "http_methods": [
    "DELETE"
  ],
  "title": "not observed",
  "purpose": "declared route web_friend_decline_request_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 90921,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/decline/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 90957.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_friend_decline_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/decline/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 90957.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_friend_decline_request_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/decline/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18402"></a>
## FND-18402: Declared route web_friend_delete_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0297",
  "route_name": "web_friend_delete_callback",
  "url_pattern": "/callback/friend/delete/{user}",
  "http_methods": [
    "DELETE"
  ],
  "title": "not observed",
  "purpose": "declared route web_friend_delete_callback",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 91694,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/delete`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 91721.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_friend_delete_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/delete`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 91721.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_friend_delete_callback:{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/delete`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18403"></a>
## FND-18403: Declared route web_user_callback_dismiss_follow_suggestion

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0298",
  "route_name": "web_user_callback_dismiss_follow_suggestion",
  "url_pattern": "/callback/user/dismiss_follow/{username}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_dismiss_follow_suggestion",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 92449,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/dismiss_follow`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 92493.

```text
\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_user_callback_dismiss_follow_suggestion:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/dismiss_follow`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 92493.

```text
\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]},web_user_callback_dismiss_follow_suggestion:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/dismiss_follow`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18404"></a>
## FND-18404: Declared route web_user_callback_report_reasons

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0299",
  "route_name": "web_user_callback_report_reasons",
  "url_pattern": "/callback/report-user",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_report_reasons",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 93239,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 53479.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_user:{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 53479.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_report_user:{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18405"></a>
## FND-18405: Declared route pubapi_player_profile

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0300",
  "route_name": "pubapi_player_profile",
  "url_pattern": "/pub/player/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route pubapi_player_profile",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 93954,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 93976.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},pubapi_player_profile:{tokens:[[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]},web_user_callback_follow_suggestions:{tokens:[[`text`,`/callback/user/follow_suggestions`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 93976.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},pubapi_player_profile:{tokens:[[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]},web_user_callback_follow_suggestions:{tokens:[[`text`,`/callback/user/follow_suggestions`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.
