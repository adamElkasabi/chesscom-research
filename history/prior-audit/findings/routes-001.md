# routes — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18106"></a>
## FND-18106: Declared route web_tinymce_get_chessdiagram

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0001",
  "route_name": "web_tinymce_get_chessdiagram",
  "url_pattern": "/tinymce/api/get_diagram",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tinymce_get_chessdiagram",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 1891,
  "raw_route_declaration": "{tokens:[[`text`,`/tinymce/api/get_diagram`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www|admin)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?:www|admin)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 1920.

```text
outes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_tinymce_get_chessdiagram:{tokens:[[`text`,`/tinymce/api/get_diagram`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www|admin)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_G
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 1920.

```text
outes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_tinymce_get_chessdiagram:{tokens:[[`text`,`/tinymce/api/get_diagram`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www|admin)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_G
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18107"></a>
## FND-18107: Declared route web_game_fens_callback_by_user

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0002",
  "route_name": "web_game_fens_callback_by_user",
  "url_pattern": "/callback/game/fens",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_fens_callback_by_user",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 2495,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/game/fens`]],defaults:{host:`www.chess-dev.com`},requirements:{userId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 2526.

```text
ww|admin)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_fens_callback_by_user:{tokens:[[`text`,`/callback/game/fens`]],defaults:{host:`www.chess-dev.com`},requirements:{userId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 2526.

```text
ww|admin)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_fens_callback_by_user:{tokens:[[`text`,`/callback/game/fens`]],defaults:{host:`www.chess-dev.com`},requirements:{userId:`[REDACTED_LITERAL]`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18108"></a>
## FND-18108: Declared route web_eco_callback_search_opening_stats_color_specific

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0003",
  "route_name": "web_eco_callback_search_opening_stats_color_specific",
  "url_pattern": "/callback/eco/search/{cleanUrl}/{username}/{colorAsNumber}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_eco_callback_search_opening_stats_color_specific",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 3240,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`colorAsNumber`,!0],[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 3293.

```text
host`,!0]],methods:[`POST`],schemes:[`https`]},web_eco_callback_search_opening_stats_color_specific:{tokens:[[`variable`,`/`,`[^/]++`,`colorAsNumber`,!0],[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 15095.

```text
`host`,!0]],methods:[`GET`],schemes:[`https`]},web_eco_callback_search_opening_stats_color_specific:{tokens:[[`variable`,`/`,`[^/]++`,`colorAsNumber`,!0],[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 3293.

```text
host`,!0]],methods:[`POST`],schemes:[`https`]},web_eco_callback_search_opening_stats_color_specific:{tokens:[[`variable`,`/`,`[^/]++`,`colorAsNumber`,!0],[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 15095.

```text
`host`,!0]],methods:[`GET`],schemes:[`https`]},web_eco_callback_search_opening_stats_color_specific:{tokens:[[`variable`,`/`,`[^/]++`,`colorAsNumber`,!0],[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/callback/eco/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18109"></a>
## FND-18109: Declared route web_lesson_callback_translations

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0004",
  "route_name": "web_lesson_callback_translations",
  "url_pattern": "/callback/lessons/translated",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_lesson_callback_translations",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 4104,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/lessons/translated`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 4137.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_callback_translations:{tokens:[[`text`,`/callback/lessons/translated`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 12126.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_callback_translations:{tokens:[[`text`,`/callback/lessons/translated`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 4137.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_callback_translations:{tokens:[[`text`,`/callback/lessons/translated`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 12126.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_callback_translations:{tokens:[[`text`,`/callback/lessons/translated`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18110"></a>
## FND-18110: Declared route web_lesson_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0005",
  "route_name": "web_lesson_view",
  "url_pattern": "/lessons/{course}/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_lesson_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 4831,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`variable`,`/`,`[^/]++`,`course`,!0],[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 4847.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`variable`,`/`,`[^/]++`,`course`,!0],[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|e
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 4847.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`variable`,`/`,`[^/]++`,`course`,!0],[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|e
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18111"></a>
## FND-18111: Declared route web_tactic_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0006",
  "route_name": "web_tactic_index",
  "url_pattern": "/puzzles",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tactic_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1151",
    "SRC-1155"
  ],
  "character_offset": 5589,
  "raw_route_declaration": "{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 5606.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tactic_index:{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 2545.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tactic_index:{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 2545.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tactic_index:{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 2545.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tactic_index:{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 5606.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tactic_index:{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 2545.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tactic_index:{tokens:[[`text`,`/puzzles`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```

**Source references:** SRC-0066, SRC-0094, SRC-0102, SRC-0144, SRC-1151, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18112"></a>
## FND-18112: Declared route web_insights

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0007",
  "route_name": "web_insights",
  "url_pattern": "/insights/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_insights",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 6275,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 6288.

```text
cacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 6288.

```text
cacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18113"></a>
## FND-18113: Declared route i18n_web_lesson_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0008",
  "route_name": "i18n_web_lesson_view",
  "url_pattern": "/{_locale}/lessons/{course}/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_lesson_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 7012,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`variable`,`/`,`[^/]++`,`course`,!0],[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 4847.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`variable`,`/`,`[^/]++`,`course`,!0],[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|e
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 4847.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_lesson_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`variable`,`/`,`[^/]++`,`course`,!0],[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|e
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18114"></a>
## FND-18114: Declared route i18n_web_tactic_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0009",
  "route_name": "i18n_web_tactic_index",
  "url_pattern": "/{_locale}/puzzles",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tactic_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1151",
    "SRC-1155"
  ],
  "character_offset": 7856,
  "raw_route_declaration": "{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 7878.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tactic_index:{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 9330.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tactic_index:{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 9330.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tactic_index:{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 9330.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tactic_index:{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 7878.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tactic_index:{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 9330.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tactic_index:{tokens:[[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```

**Source references:** SRC-0066, SRC-0094, SRC-0102, SRC-0144, SRC-1151, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18111, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18115"></a>
## FND-18115: Declared route i18n_web_insights

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0010",
  "route_name": "i18n_web_insights",
  "url_pattern": "/{_locale}/insights/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_insights",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 8628,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 8646.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`w
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 8646.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`w
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18116"></a>
## FND-18116: Declared route web_practice_custom

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0011",
  "route_name": "web_practice_custom",
  "url_pattern": "/practice/custom",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_practice_custom",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 9451,
  "raw_route_declaration": "{tokens:[[`text`,`/practice/custom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 9471.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_practice_custom:{tokens:[[`text`,`/practice/custom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 9471.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_practice_custom:{tokens:[[`text`,`/practice/custom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18117"></a>
## FND-18117: Declared route web_membership

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0012",
  "route_name": "web_membership",
  "url_pattern": "/membership",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_membership",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 10148,
  "raw_route_declaration": "{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 10163.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 1737.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 1737.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2255.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2368.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 10163.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2368.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```

**Source references:** SRC-0066, SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18118"></a>
## FND-18118: Declared route i18n_web_membership

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0013",
  "route_name": "i18n_web_membership",
  "url_pattern": "/{_locale}/membership",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_membership",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 10835,
  "raw_route_declaration": "{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 10855.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 4687.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 4687.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 5205.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 5318.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 10855.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 5318.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership:{tokens:[[`text`,`/membership`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```

**Source references:** SRC-0066, SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18117, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18119"></a>
## FND-18119: Declared route web_archive_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0014",
  "route_name": "web_archive_index",
  "url_pattern": "/games/archive/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_archive_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 11608,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 11626.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 11626.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18120"></a>
## FND-18120: Declared route web_analysis_board_editor_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0015",
  "route_name": "web_analysis_board_editor_tab",
  "url_pattern": "/analysis/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_board_editor_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0761",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 12355,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 12385.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-0761** `research/refinement/live-chunks/shared.a12b57fa.DJ75_leN-v.chunk.js` — [preserved redacted evidence](../evidence/text/0cf5194fbc79b2008d5101b9f5928dce5f965b56bad2c3069f9602f3a3667c39.js)
  Character offset 154.

```text
utes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 12385.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-0066, SRC-0761, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18128, FND-18133

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18121"></a>
## FND-18121: Declared route explorer_callback_move

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0016",
  "route_name": "explorer_callback_move",
  "url_pattern": "/callback/explorer/move",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route explorer_callback_move",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 13227,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/explorer/move`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?:www)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 13250.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},explorer_callback_move:{tokens:[[`text`,`/callback/explorer/move`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 10000.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},explorer_callback_move:{tokens:[[`text`,`/callback/explorer/move`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 13250.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},explorer_callback_move:{tokens:[[`text`,`/callback/explorer/move`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 10000.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},explorer_callback_move:{tokens:[[`text`,`/callback/explorer/move`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18122"></a>
## FND-18122: Declared route explorer_callback_get_suggested_moves

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0017",
  "route_name": "explorer_callback_get_suggested_moves",
  "url_pattern": "/callback/explorer/get-suggested-moves",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route explorer_callback_get_suggested_moves",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 13818,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/explorer/get-suggested-moves`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?:www)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 13856.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},explorer_callback_get_suggested_moves:{tokens:[[`text`,`/callback/explorer/get-suggested-moves`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 104022.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},explorer_callback_get_suggested_moves:{tokens:[[`text`,`/callback/explorer/get-suggested-moves`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 13856.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},explorer_callback_get_suggested_moves:{tokens:[[`text`,`/callback/explorer/get-suggested-moves`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 104022.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},explorer_callback_get_suggested_moves:{tokens:[[`text`,`/callback/explorer/get-suggested-moves`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(www)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18123"></a>
## FND-18123: Declared route web_master_games_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0018",
  "route_name": "web_master_games_search",
  "url_pattern": "/games/search",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_master_games_search",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1136",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 14439,
  "raw_route_declaration": "{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 14463.

```text
`,`(?:www)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-1136** `research/shared.533ee0c1.chunk.js` — [preserved redacted evidence](../evidence/text/b524fbc66b2962944ac6242d90d120d6f2942c40f17da95033d795e34b2a0e42.js)
  Character offset 2771.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 18154.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 14463.

```text
`,`(?:www)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 18154.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```

**Source references:** SRC-0066, SRC-1136, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18129, FND-18326

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18124"></a>
## FND-18124: Declared route web_analysis_board_editor

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0019",
  "route_name": "web_analysis_board_editor",
  "url_pattern": "/analysis",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_board_editor",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 15142,
  "raw_route_declaration": "{tokens:[[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 15168.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_board_editor:{tokens:[[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 7715.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},web_analysis_board_editor:{tokens:[[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 15168.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_analysis_board_editor:{tokens:[[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 7715.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},web_analysis_board_editor:{tokens:[[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18125"></a>
## FND-18125: Declared route web_security_register

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0020",
  "route_name": "web_security_register",
  "url_pattern": "/register",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_security_register",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0781",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 15838,
  "raw_route_declaration": "{tokens:[[`text`,`/register`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 15860.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_register:{tokens:[[`text`,`/register`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 53247.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_register:{tokens:[[`text`,`/register`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 48364.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_register:{tokens:[[`text`,`/register`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 15860.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_register:{tokens:[[`text`,`/register`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 48364.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_register:{tokens:[[`text`,`/register`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```

**Source references:** SRC-0066, SRC-0781, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18126"></a>
## FND-18126: Declared route web_play_computer

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0021",
  "route_name": "web_play_computer",
  "url_pattern": "/play/computer",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_computer",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0754",
    "SRC-0781",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 16535,
  "raw_route_declaration": "{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 16553.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_play_computer:{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|h
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 3363.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_computer:{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|h
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 100746.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_computer:{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|h
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 129087.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_play_computer:{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|h
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 16553.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_play_computer:{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 129087.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_play_computer:{tokens:[[`text`,`/play/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|h
```

**Source references:** SRC-0066, SRC-0754, SRC-0781, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18132, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18127"></a>
## FND-18127: Declared route i18n_web_archive_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0022",
  "route_name": "i18n_web_archive_index",
  "url_pattern": "/{_locale}/games/archive/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_archive_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1151"
  ],
  "character_offset": 17228,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 17251.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,ho
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 17251.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,ho
```

**Source references:** SRC-0066, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18128"></a>
## FND-18128: Declared route i18n_web_analysis_board_editor_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0023",
  "route_name": "i18n_web_analysis_board_editor_tab",
  "url_pattern": "/{_locale}/analysis/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_board_editor_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0761",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 18061,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 12385.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-0761** `research/refinement/live-chunks/shared.a12b57fa.DJ75_leN-v.chunk.js` — [preserved redacted evidence](../evidence/text/0cf5194fbc79b2008d5101b9f5928dce5f965b56bad2c3069f9602f3a3667c39.js)
  Character offset 154.

```text
utes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 12385.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-0066, SRC-0761, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18120, FND-18133

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18129"></a>
## FND-18129: Declared route i18n_web_master_games_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0024",
  "route_name": "i18n_web_master_games_search",
  "url_pattern": "/{_locale}/games/search",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_master_games_search",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1136",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 19019,
  "raw_route_declaration": "{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 19048.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-1136** `research/shared.533ee0c1.chunk.js` — [preserved redacted evidence](../evidence/text/b524fbc66b2962944ac6242d90d120d6f2942c40f17da95033d795e34b2a0e42.js)
  Character offset 3479.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 24535.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 19048.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 24535.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```

**Source references:** SRC-0066, SRC-1136, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18123, FND-18326

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18130"></a>
## FND-18130: Declared route i18n_web_analysis_board_editor

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0025",
  "route_name": "i18n_web_analysis_board_editor",
  "url_pattern": "/{_locale}/analysis",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_board_editor",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 19808,
  "raw_route_declaration": "{tokens:[[`text`,`/analysis`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 19839.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_analysis_board_editor:{tokens:[[`text`,`/analysis`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 20401.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_board_editor:{tokens:[[`text`,`/analysis`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 19839.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_analysis_board_editor:{tokens:[[`text`,`/analysis`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 20401.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_analysis_board_editor:{tokens:[[`text`,`/analysis`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18131"></a>
## FND-18131: Declared route i18n_web_security_register

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0026",
  "route_name": "i18n_web_security_register",
  "url_pattern": "/{_locale}/register",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_security_register",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0781",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 20590,
  "raw_route_declaration": "{tokens:[[`text`,`/register`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 20617.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_register:{tokens:[[`text`,`/register`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 55328.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_register:{tokens:[[`text`,`/register`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 50445.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_register:{tokens:[[`text`,`/register`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 20617.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_register:{tokens:[[`text`,`/register`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 50445.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_register:{tokens:[[`text`,`/register`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```

**Source references:** SRC-0066, SRC-0781, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18132"></a>
## FND-18132: Declared route i18n_web_play_computer

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0027",
  "route_name": "i18n_web_play_computer",
  "url_pattern": "/{_locale}/play/computer",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_computer",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0754",
    "SRC-0781",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 21373,
  "raw_route_declaration": "{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 21396.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_play_computer:{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 4858.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_computer:{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 102217.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_computer:{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 131162.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_computer:{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 21396.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_play_computer:{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 131162.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_computer:{tokens:[[`text`,`/play/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:
```

**Source references:** SRC-0066, SRC-0754, SRC-0781, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18126, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18133"></a>
## FND-18133: Declared route web_openings_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0028",
  "route_name": "web_openings_view",
  "url_pattern": "/openings/{cleanUrl}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_openings_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0761",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 22152,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 22170.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```
- **SRC-0761** `research/refinement/live-chunks/shared.a12b57fa.DJ75_leN-v.chunk.js` — [preserved redacted evidence](../evidence/text/0cf5194fbc79b2008d5101b9f5928dce5f965b56bad2c3069f9602f3a3667c39.js)
  Character offset 1014.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 13528.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 22170.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 13528.

```text
i|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_
```

**Source references:** SRC-0066, SRC-0761, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18120, FND-18128

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18134"></a>
## FND-18134: Declared route i18n_web_openings_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0029",
  "route_name": "i18n_web_openings_view",
  "url_pattern": "/{_locale}/openings/{cleanUrl}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_openings_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0761",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "character_offset": 22880,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 22903.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.c
```
- **SRC-0761** `research/refinement/live-chunks/shared.a12b57fa.DJ75_leN-v.chunk.js` — [preserved redacted evidence](../evidence/text/0cf5194fbc79b2008d5101b9f5928dce5f965b56bad2c3069f9602f3a3667c39.js)
  Character offset 2705.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 23715.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.c
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 22903.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 23715.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_openings_view:{tokens:[[`variable`,`/`,`[^/]++`,`cleanUrl`,!0],[`text`,`/openings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.c
```

**Source references:** SRC-0066, SRC-0761, SRC-1137, SRC-1151, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18120, FND-18128

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18135"></a>
## FND-18135: Declared route web_membership_no_ads

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0030",
  "route_name": "web_membership_no_ads",
  "url_pattern": "/no-ads",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_membership_no_ads",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0781",
    "SRC-1151"
  ],
  "character_offset": 23694,
  "raw_route_declaration": "{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 23716.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 84745.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 23716.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```

**Source references:** SRC-0066, SRC-0781, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18136"></a>
## FND-18136: Declared route i18n_web_membership_no_ads

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0031",
  "route_name": "i18n_web_membership_no_ads",
  "url_pattern": "/{_locale}/no-ads",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_membership_no_ads",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0066",
    "SRC-0781",
    "SRC-1151"
  ],
  "character_offset": 24384,
  "raw_route_declaration": "{tokens:[[`text`,`/no-ads`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 24411.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership_no_ads:{tokens:[[`text`,`/no-ads`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 85440.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership_no_ads:{tokens:[[`text`,`/no-ads`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 24411.

```text
haken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership_no_ads:{tokens:[[`text`,`/no-ads`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```

**Source references:** SRC-0066, SRC-0781, SRC-1151  
**URL references:** None independently associated  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18137"></a>
## FND-18137: Declared route web_about

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0032",
  "route_name": "web_about",
  "url_pattern": "/about",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_about",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 319,
  "raw_route_declaration": "{tokens:[[`text`,`/about`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 329.

```text
},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_about:{tokens:[[`text`,`/about`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 329.

```text
},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_about:{tokens:[[`text`,`/about`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 847.

```text
},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_about:{tokens:[[`text`,`/about`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 960.

```text
},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_about:{tokens:[[`text`,`/about`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 960.

```text
},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_about:{tokens:[[`text`,`/about`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18138"></a>
## FND-18138: Declared route web_article_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0033",
  "route_name": "web_article_view",
  "url_pattern": "/article/view/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_article_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 996,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 1013.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_F
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 1013.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_F
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1531.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_F
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1644.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_F
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1644.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_F
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18139"></a>
## FND-18139: Declared route web_member_titled_players

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0034",
  "route_name": "web_member_titled_players",
  "url_pattern": "/members/titled-players",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_titled_players",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0201",
    "SRC-0751",
    "SRC-0780",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 2409,
  "raw_route_declaration": "{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 2435.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-0201** `research/play.js` — [preserved redacted evidence](../evidence/text/7b48978996e293cd2e02e9853ab5ba84a3684afe8a7e4c5bd40f8e89a1a85571.js)
  Character offset 3893.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 2435.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)
  Character offset 3945.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 2953.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3066.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3066.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```

**Source references:** SRC-0090, SRC-0201, SRC-0751, SRC-0780, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137, FND-18142, FND-18205

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18140"></a>
## FND-18140: Declared route web_member_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0035",
  "route_name": "web_member_view",
  "url_pattern": "/member/{username}",
  "http_methods": [
    "GET",
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 3119,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 3135.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 3135.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 3653.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3766.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 3766.

```text
chi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18141"></a>
## FND-18141: Declared route i18n_web_article_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0036",
  "route_name": "i18n_web_article_view",
  "url_pattern": "/{_locale}/article/view/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_article_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 3855,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 3877.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},i18n_web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 3877.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},i18n_web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 4395.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},i18n_web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 4508.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},i18n_web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 4508.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},i18n_web_article_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/article/view`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18142"></a>
## FND-18142: Declared route i18n_web_member_titled_players

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0037",
  "route_name": "i18n_web_member_titled_players",
  "url_pattern": "/{_locale}/members/titled-players",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_member_titled_players",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0201",
    "SRC-0751",
    "SRC-0780",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 5440,
  "raw_route_declaration": "{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 5471.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```
- **SRC-0201** `research/play.js` — [preserved redacted evidence](../evidence/text/7b48978996e293cd2e02e9853ab5ba84a3684afe8a7e4c5bd40f8e89a1a85571.js)
  Character offset 4608.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 5471.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```
- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)
  Character offset 4660.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 5989.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 6102.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 6102.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_titled_players:{tokens:[[`text`,`/members/titled-players`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requiremen
```

**Source references:** SRC-0090, SRC-0201, SRC-0751, SRC-0780, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137, FND-18139, FND-18205

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18143"></a>
## FND-18143: Declared route i18n_web_member_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0038",
  "route_name": "i18n_web_member_view",
  "url_pattern": "/{_locale}/member/{username}",
  "http_methods": [
    "GET",
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_member_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 6236,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 6257.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 6257.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 6775.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 6888.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 6888.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_member_view:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18144"></a>
## FND-18144: Declared route web_2fa_login

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0039",
  "route_name": "web_2fa_login",
  "url_pattern": "/2fa",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_2fa_login",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 7058,
  "raw_route_declaration": "{tokens:[[`text`,`/2fa`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 7072.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},web_2fa_login:{tokens:[[`text`,`/2fa`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 7072.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`POST`],schemes:[`https`]},web_2fa_login:{tokens:[[`text`,`/2fa`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 68730.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_2fa_login:{tokens:[[`text`,`/2fa`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 46912.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_2fa_login:{tokens:[[`text`,`/2fa`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 46912.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_2fa_login:{tokens:[[`text`,`/2fa`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18145"></a>
## FND-18145: Declared route i18n_web_2fa_login

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0040",
  "route_name": "i18n_web_2fa_login",
  "url_pattern": "/{_locale}/2fa",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_2fa_login",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 7737,
  "raw_route_declaration": "{tokens:[[`text`,`/2fa`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 7756.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_2fa_login:{tokens:[[`text`,`/2fa`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 7756.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_2fa_login:{tokens:[[`text`,`/2fa`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 69414.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_2fa_login:{tokens:[[`text`,`/2fa`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 47596.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_2fa_login:{tokens:[[`text`,`/2fa`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 47596.

```text
|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_2fa_login:{tokens:[[`text`,`/2fa`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18146"></a>
## FND-18146: Declared route web_article_callback_list_authors

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0041",
  "route_name": "web_article_callback_list_authors",
  "url_pattern": "/callback/articles/authors",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_article_callback_list_authors",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 8502,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 8536.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_list_authors:{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 8536.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_list_authors:{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 71772.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_list_authors:{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 104639.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_article_callback_list_authors:{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 104639.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_article_callback_list_authors:{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18147"></a>
## FND-18147: Declared route web_article_callback_lock_coments

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0042",
  "route_name": "web_article_callback_lock_coments",
  "url_pattern": "/callback/articles/lock-comments/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_article_callback_lock_coments",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 9223,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 9257.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 9257.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 72493.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 105360.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 105360.

```text
zachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_article_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18148"></a>
## FND-18148: Declared route web_blog_callback_lock_coments

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0043",
  "route_name": "web_blog_callback_lock_coments",
  "url_pattern": "/callback/blog/lock-comments/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_blog_callback_lock_coments",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 9990,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 10021.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_blog_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 10021.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_blog_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 73257.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_blog_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 106124.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_blog_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 106124.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_blog_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18149"></a>
## FND-18149: Declared route web_news_callback_lock_coments

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0044",
  "route_name": "web_news_callback_lock_coments",
  "url_pattern": "/callback/news/lock-comments/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_news_callback_lock_coments",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 10750,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 10781.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_news_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 10781.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_news_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 74017.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_news_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 106884.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_news_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 106884.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_news_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18150"></a>
## FND-18150: Declared route web_video_callback_lock_coments

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0045",
  "route_name": "web_video_callback_lock_coments",
  "url_pattern": "/callback/video/lock-comments/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_video_callback_lock_coments",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 11510,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 11542.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_video_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 11542.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_video_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 74778.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_video_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 107645.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_video_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 107645.

```text
y)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_video_callback_lock_coments:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|e
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18151"></a>
## FND-18151: Declared route web_content_callback_feature_article

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0046",
  "route_name": "web_content_callback_feature_article",
  "url_pattern": "/callback/content/feature/article/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_content_callback_feature_article",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 12272,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 12309.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_article:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 12309.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_article:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 75545.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_article:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 108412.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_article:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 108412.

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_article:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18152"></a>
## FND-18152: Declared route web_content_callback_feature_blog

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0047",
  "route_name": "web_content_callback_feature_blog",
  "url_pattern": "/callback/content/feature/blog/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_content_callback_feature_blog",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 13043,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 13077.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_blog:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 13077.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_blog:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 76313.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_blog:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 109180.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_blog:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 109180.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_blog:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18153"></a>
## FND-18153: Declared route web_content_callback_feature_lesson_course

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0048",
  "route_name": "web_content_callback_feature_lesson_course",
  "url_pattern": "/callback/content/feature/lesson_course/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_content_callback_feature_lesson_course",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 13808,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 13851.

```text
[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_lesson_course:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 13851.

```text
[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_lesson_course:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 77087.

```text
[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_lesson_course:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 109954.

```text
[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_lesson_course:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 109954.

```text
[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_lesson_course:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18154"></a>
## FND-18154: Declared route web_content_callback_feature_news

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0049",
  "route_name": "web_content_callback_feature_news",
  "url_pattern": "/callback/content/feature/news/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_content_callback_feature_news",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 14591,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 14625.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_news:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 14625.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_news:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 77861.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_news:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 110728.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_news:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 110728.

```text
?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_news:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18155"></a>
## FND-18155: Declared route web_content_callback_feature_chess_video

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0050",
  "route_name": "web_content_callback_feature_chess_video",
  "url_pattern": "/callback/content/feature/chess_video/{id}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_content_callback_feature_chess_video",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 15356,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 15397.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_chess_video:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 15397.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_chess_video:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 78633.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_chess_video:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 111500.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_chess_video:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 111500.

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_content_callback_feature_chess_video:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18156"></a>
## FND-18156: Declared route web_user_callback_set_content_language

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0051",
  "route_name": "web_user_callback_set_content_language",
  "url_pattern": "/callback/user/content-language/set",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_set_content_language",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 16135,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 16174.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_content_language:{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_F
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 16174.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_content_language:{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_F
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 79410.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_content_language:{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_F
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 112277.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_content_language:{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_F
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 112277.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_content_language:{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_F
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18157"></a>
## FND-18157: Declared route web_security_login_and_go

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0052",
  "route_name": "web_security_login_and_go",
  "url_pattern": "/login_and_go",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_security_login_and_go",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 16876,
  "raw_route_declaration": "{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 16902.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_security_login_and_go:{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 16902.

```text
|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_security_login_and_go:{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 53948.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_security_login_and_go:{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 49065.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_security_login_and_go:{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 49065.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_security_login_and_go:{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18158"></a>
## FND-18158: Declared route web_survey_callback_vote

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0053",
  "route_name": "web_survey_callback_vote",
  "url_pattern": "/callback/survey/{id}/vote/{optionId}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_survey_callback_vote",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 17576,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,optionId:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 17601.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,optionId:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_B
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 17601.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,optionId:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_B
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 80137.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,optionId:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_B
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 113004.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,optionId:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_B
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 113004.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_survey_callback_vote:{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,optionId:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_B
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18159"></a>
## FND-18159: Declared route web_team_match_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0054",
  "route_name": "web_team_match_view",
  "url_pattern": "/club/matches/{match}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_team_match_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 18397,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 18417.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 18417.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 61640.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 113820.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 113820.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18160"></a>
## FND-18160: Declared route web_tournament_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0055",
  "route_name": "web_tournament_view",
  "url_pattern": "/tournament/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tournament_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 19139,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 19159.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 19159.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 63870.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 114562.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 114562.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18161"></a>
## FND-18161: Declared route i18n_web_security_login_and_go

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0056",
  "route_name": "i18n_web_security_login_and_go",
  "url_pattern": "/{_locale}/login_and_go",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_security_login_and_go",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 19866,
  "raw_route_declaration": "{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 19897.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_login_and_go:{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 19897.

```text
n|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_security_login_and_go:{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 56115.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_security_login_and_go:{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 51232.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_security_login_and_go:{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 51232.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_security_login_and_go:{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18162"></a>
## FND-18162: Declared route i18n_web_team_match_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0057",
  "route_name": "i18n_web_team_match_view",
  "url_pattern": "/{_locale}/club/matches/{match}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_team_match_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 20652,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{match:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 20677.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 20677.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 65440.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 115294.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 115294.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.co
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18163"></a>
## FND-18163: Declared route i18n_web_tournament_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0058",
  "route_name": "i18n_web_tournament_view",
  "url_pattern": "/{_locale}/tournament/{url}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tournament_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 21480,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 21505.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 21505.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 67928.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 116122.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 116122.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournament_view:{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18164"></a>
## FND-18164: Declared route web_stats

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0059",
  "route_name": "web_stats",
  "url_pattern": "/stats/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_stats",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 22293,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 22303.

```text
r|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 22303.

```text
r|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 83185.

```text
r|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 116920.

```text
r|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 116920.

```text
r|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18165"></a>
## FND-18165: Declared route i18n_web_stats

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0060",
  "route_name": "i18n_web_stats",
  "url_pattern": "/{_locale}/stats/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_stats",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0090",
    "SRC-0751",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 23024,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0090** `research/checkmate.js` — [preserved redacted evidence](../evidence/text/caa3496678e183116e22739f14faf528b0418713a9b1843df07f0ae9b3af256b.js)
  Character offset 23039.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.
```
- **SRC-0751** `research/refinement/live-checkmate.js` — [preserved redacted evidence](../evidence/text/e581b04c3023dcefec26c827938c4b372ed86840d6dd55cebf2650d5e33045e2.js)
  Character offset 23039.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 83921.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 117656.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 117656.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_stats:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.
```

**Source references:** SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18117, FND-18118, FND-18137

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18166"></a>
## FND-18166: Declared route web_play_coach

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0061",
  "route_name": "web_play_coach",
  "url_pattern": "/play/coach",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_play_coach",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-0754",
    "SRC-0781",
    "SRC-1137",
    "SRC-1155",
    "SRC-1165"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 139.

```text
dow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 139.

```text
dow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 139.

```text
dow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 5629.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 100056.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 129777.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 139.

```text
dow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 129777.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_play_coach:{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-0754, SRC-0781, SRC-1137, SRC-1155, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18167"></a>
## FND-18167: Declared route web_user_settings_coach

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0062",
  "route_name": "web_user_settings_coach",
  "url_pattern": "/settings/coach",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_settings_coach",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 811,
  "raw_route_declaration": "{tokens:[[`text`,`/settings/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 835.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_settings_coach:{tokens:[[`text`,`/settings/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 835.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_settings_coach:{tokens:[[`text`,`/settings/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 835.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_settings_coach:{tokens:[[`text`,`/settings/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 835.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_settings_coach:{tokens:[[`text`,`/settings/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18168"></a>
## FND-18168: Declared route web_analysis_ceac_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0063",
  "route_name": "web_analysis_ceac_tab",
  "url_pattern": "/analysis/game/{type}/{gameId}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_analysis_ceac_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1137",
    "SRC-1155",
    "SRC-1165"
  ],
  "character_offset": 1511,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1137, SRC-1155, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18169"></a>
## FND-18169: Declared route web_puzzles_mode

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0064",
  "route_name": "web_puzzles_mode",
  "url_pattern": "/puzzles/{mode}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_puzzles_mode",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 3214,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`]],defaults:{mode:``,host:`www.chess-dev.com`},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 3231.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`]],defaults:{mode:``,host:`www.chess-dev.com`},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 3231.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`]],defaults:{mode:``,host:`www.chess-dev.com`},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 3231.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`]],defaults:{mode:``,host:`www.chess-dev.com`},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 3231.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`]],defaults:{mode:``,host:`www.chess-dev.com`},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18170"></a>
## FND-18170: Declared route web_daily_chess_puzzle

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0065",
  "route_name": "web_daily_chess_puzzle",
  "url_pattern": "/daily",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_daily_chess_puzzle",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 3998,
  "raw_route_declaration": "{tokens:[[`text`,`/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 4021.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_chess_puzzle:{tokens:[[`text`,`/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 4021.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_chess_puzzle:{tokens:[[`text`,`/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 4021.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_chess_puzzle:{tokens:[[`text`,`/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 4021.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_daily_chess_puzzle:{tokens:[[`text`,`/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18171"></a>
## FND-18171: Declared route web_lesson_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0066",
  "route_name": "web_lesson_index",
  "url_pattern": "/lessons",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_lesson_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 4688,
  "raw_route_declaration": "{tokens:[[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 4705.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_lesson_index:{tokens:[[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 4705.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_lesson_index:{tokens:[[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 4705.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_lesson_index:{tokens:[[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 4705.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_lesson_index:{tokens:[[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|h
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18172"></a>
## FND-18172: Declared route web_page_learn

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0067",
  "route_name": "web_page_learn",
  "url_pattern": "/learn",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_page_learn",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 5374,
  "raw_route_declaration": "{tokens:[[`text`,`/learn`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 5389.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_page_learn:{tokens:[[`text`,`/learn`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 5389.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_page_learn:{tokens:[[`text`,`/learn`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 5389.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_page_learn:{tokens:[[`text`,`/learn`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 5389.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_page_learn:{tokens:[[`text`,`/learn`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18173"></a>
## FND-18173: Declared route web_user_home

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0068",
  "route_name": "web_user_home",
  "url_pattern": "/home",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_home",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-0781",
    "SRC-1137",
    "SRC-1155",
    "SRC-1165"
  ],
  "character_offset": 6056,
  "raw_route_declaration": "{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 6070.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 6070.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 6070.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 103786.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 137479.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 6070.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 137479.

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-0781, SRC-1137, SRC-1155, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18174"></a>
## FND-18174: Declared route web_security_onboarding

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0069",
  "route_name": "web_security_onboarding",
  "url_pattern": "/onboarding",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_security_onboarding",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 6736,
  "raw_route_declaration": "{tokens:[[`text`,`/onboarding`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 6760.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_onboarding:{tokens:[[`text`,`/onboarding`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 6760.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_onboarding:{tokens:[[`text`,`/onboarding`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 6760.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_onboarding:{tokens:[[`text`,`/onboarding`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 6760.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_security_onboarding:{tokens:[[`text`,`/onboarding`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_H
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18175"></a>
## FND-18175: Declared route i18n_web_play_coach

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0070",
  "route_name": "i18n_web_play_coach",
  "url_pattern": "/{_locale}/play/coach",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_play_coach",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-0754",
    "SRC-0781",
    "SRC-1137",
    "SRC-1155",
    "SRC-1165"
  ],
  "character_offset": 7432,
  "raw_route_declaration": "{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 7452.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 7452.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 7452.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0754** `research/refinement/live-chunks/shared.0ca1ef1f.BLOIc94Fsf.chunk.js` — [preserved redacted evidence](../evidence/text/ed85af2c7ba46fc7d2fe3855a1a4757e92297cd255c864c06f9e515f33db8e3c.js)
  Character offset 6321.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 101441.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 131938.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 7452.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 131938.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_play_coach:{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-0754, SRC-0781, SRC-1137, SRC-1155, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18176"></a>
## FND-18176: Declared route i18n_web_analysis_ceac_tab

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0071",
  "route_name": "i18n_web_analysis_ceac_tab",
  "url_pattern": "/{_locale}/analysis/game/{type}/{gameId}/{tab}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_analysis_ceac_tab",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1137",
    "SRC-1155",
    "SRC-1165"
  ],
  "character_offset": 8205,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{type:`daily|live|master|pgn|computer|coach`,tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 1533.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_ceac_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|compu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 9135.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_analysis_board_editor_tab:{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`text`,`/analysis`]],defaults:{host:`www.chess-dev.com`},requirements:{tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|sz
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1137, SRC-1155, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18177"></a>
## FND-18177: Declared route i18n_web_puzzles_mode

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0072",
  "route_name": "i18n_web_puzzles_mode",
  "url_pattern": "/{_locale}/puzzles/{mode}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_puzzles_mode",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 10080,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{mode:``,host:`www.chess-dev.com`,_locale:``},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 10102.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{mode:`
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 10102.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{mode:`
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 10102.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{mode:`
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 10102.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_puzzles_mode:{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{mode:`
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18178"></a>
## FND-18178: Declared route i18n_web_daily_chess_puzzle

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0073",
  "route_name": "i18n_web_daily_chess_puzzle",
  "url_pattern": "/{_locale}/daily",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_daily_chess_puzzle",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 10950,
  "raw_route_declaration": "{tokens:[[`text`,`/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 10978.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_daily_chess_puzzle:{tokens:[[`text`,`/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 10978.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_daily_chess_puzzle:{tokens:[[`text`,`/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 10978.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_daily_chess_puzzle:{tokens:[[`text`,`/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 10978.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_daily_chess_puzzle:{tokens:[[`text`,`/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18179"></a>
## FND-18179: Declared route i18n_web_lesson_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0074",
  "route_name": "i18n_web_lesson_index",
  "url_pattern": "/{_locale}/lessons",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_lesson_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 11726,
  "raw_route_declaration": "{tokens:[[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 11748.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_lesson_index:{tokens:[[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 11748.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_lesson_index:{tokens:[[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 11748.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_lesson_index:{tokens:[[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 11748.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_lesson_index:{tokens:[[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!ad
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18180"></a>
## FND-18180: Declared route i18n_web_page_learn

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0075",
  "route_name": "i18n_web_page_learn",
  "url_pattern": "/{_locale}/learn",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_page_learn",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0094",
    "SRC-0102",
    "SRC-0144",
    "SRC-1155"
  ],
  "character_offset": 12498,
  "raw_route_declaration": "{tokens:[[`text`,`/learn`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0094** `research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 12518.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_page_learn:{tokens:[[`text`,`/learn`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```
- **SRC-0102** `research/client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 12518.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_page_learn:{tokens:[[`text`,`/learn`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```
- **SRC-0144** `research/play-chunks/client.411a4358.Dcbgz_LFZX.chunk.js` — [preserved redacted evidence](../evidence/text/ee5ae9f7e71fa636976470dc3fafbfbef36527135350e21228d0894bce68aa32.js)
  Character offset 12518.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_page_learn:{tokens:[[`text`,`/learn`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```
- **SRC-1155** `research.zip!/research/chunk_client.411a4358.wFtSs_EYP_.chunk.js` — [preserved redacted evidence](../evidence/text/017fc1eb8148a9d74bef6c4a2b593c02b65ab144a53e2def57d92e11723afb0a.js)
  Character offset 12518.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_page_learn:{tokens:[[`text`,`/learn`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admi
```

**Source references:** SRC-0094, SRC-0102, SRC-0144, SRC-1155  
**URL references:** None independently associated  
**Related findings:** FND-18111, FND-18114, FND-18166

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18181"></a>
## FND-18181: Declared route web_league_callback_league_info

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0076",
  "route_name": "web_league_callback_league_info",
  "url_pattern": "/callback/leagues/league-info",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_league_callback_league_info",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0134"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/leagues/league-info`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0134** `research/play-chunks/client.136c7de7.Ciflqgar3A.chunk.js` — [preserved redacted evidence](../evidence/text/d2a7cd07972bdf80e9898478f7baf4267b4c7375f89205e19ca6daa9207c25c6.js)
  Character offset 156.

```text
es=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_league_callback_league_info:{tokens:[[`text`,`/callback/leagues/league-info`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_E
```

**Source references:** SRC-0134  
**URL references:** None independently associated  
**Related findings:** FND-18182, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18182"></a>
## FND-18182: Declared route i18n_web_league_callback_league_info

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0077",
  "route_name": "i18n_web_league_callback_league_info",
  "url_pattern": "/{_locale}/callback/leagues/league-info",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_league_callback_league_info",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0134"
  ],
  "character_offset": 846,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/leagues/league-info`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0134** `research/play-chunks/client.136c7de7.Ciflqgar3A.chunk.js` — [preserved redacted evidence](../evidence/text/d2a7cd07972bdf80e9898478f7baf4267b4c7375f89205e19ca6daa9207c25c6.js)
  Character offset 883.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_league_callback_league_info:{tokens:[[`text`,`/callback/leagues/league-info`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requ
```

**Source references:** SRC-0134  
**URL references:** None independently associated  
**Related findings:** FND-18181, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18183"></a>
## FND-18183: Declared route web_policies_community

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0078",
  "route_name": "web_policies_community",
  "url_pattern": "/legal/community",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_policies_community",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0136",
    "SRC-0146",
    "SRC-0163",
    "SRC-0175",
    "SRC-0177",
    "SRC-0179",
    "SRC-0191",
    "SRC-0192"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0136** `research/play-chunks/client.1ceb0e95.CvC4o8ajEV.chunk.js` — [preserved redacted evidence](../evidence/text/15443a966a65b77a795130c8ddf49f4e50d6c148222e22fe9a7b822847e02f9e.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0146** `research/play-chunks/client.4a9e3c32.B86Cut1SJs.chunk.js` — [preserved redacted evidence](../evidence/text/91bb388e5a35c735e8c40d774316eb09f860a1467032f305625fd81728ef63ac.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0163** `research/play-chunks/client.8377e444.3SCIMnf7Uj.chunk.js` — [preserved redacted evidence](../evidence/text/685f81519b86972486f4b8f3d0873f386d10db5aef6aa8d044dad3138a7e87f4.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0175** `research/play-chunks/client.a70e00bc.DVI1ix4lyU.chunk.js` — [preserved redacted evidence](../evidence/text/4be0ac1c4252308e1be3493430420dfd11fc1f009ff2b2e249ed6a97434c4e7b.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0179** `research/play-chunks/client.b7294ae3.D2dmAF_rN0.chunk.js` — [preserved redacted evidence](../evidence/text/05f2ba7ea7e678abd94864230e25d6bbe34873396d323b5186ce32d028f4ffb0.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```
- **SRC-0192** `research/play-chunks/client.d9b5e4c3.B1bZhM72oL.chunk.js` — [preserved redacted evidence](../evidence/text/ddf32fa4e9cfc1c9cdca0b30ed2e49781b407a3683c5792e9f17a58d3ed1eefe.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_policies_community:{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN
```

**Source references:** SRC-0136, SRC-0146, SRC-0163, SRC-0175, SRC-0177, SRC-0179, SRC-0191, SRC-0192  
**URL references:** None independently associated  
**Related findings:** FND-18184, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18184"></a>
## FND-18184: Declared route i18n_web_policies_community

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0079",
  "route_name": "i18n_web_policies_community",
  "url_pattern": "/{_locale}/legal/community",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_policies_community",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0136",
    "SRC-0146",
    "SRC-0163",
    "SRC-0175",
    "SRC-0177",
    "SRC-0179",
    "SRC-0191",
    "SRC-0192"
  ],
  "character_offset": 824,
  "raw_route_declaration": "{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0136** `research/play-chunks/client.1ceb0e95.CvC4o8ajEV.chunk.js` — [preserved redacted evidence](../evidence/text/15443a966a65b77a795130c8ddf49f4e50d6c148222e22fe9a7b822847e02f9e.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0146** `research/play-chunks/client.4a9e3c32.B86Cut1SJs.chunk.js` — [preserved redacted evidence](../evidence/text/91bb388e5a35c735e8c40d774316eb09f860a1467032f305625fd81728ef63ac.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0163** `research/play-chunks/client.8377e444.3SCIMnf7Uj.chunk.js` — [preserved redacted evidence](../evidence/text/685f81519b86972486f4b8f3d0873f386d10db5aef6aa8d044dad3138a7e87f4.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0175** `research/play-chunks/client.a70e00bc.DVI1ix4lyU.chunk.js` — [preserved redacted evidence](../evidence/text/4be0ac1c4252308e1be3493430420dfd11fc1f009ff2b2e249ed6a97434c4e7b.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 1545.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0179** `research/play-chunks/client.b7294ae3.D2dmAF_rN0.chunk.js` — [preserved redacted evidence](../evidence/text/05f2ba7ea7e678abd94864230e25d6bbe34873396d323b5186ce32d028f4ffb0.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```
- **SRC-0192** `research/play-chunks/client.d9b5e4c3.B1bZhM72oL.chunk.js` — [preserved redacted evidence](../evidence/text/ddf32fa4e9cfc1c9cdca0b30ed2e49781b407a3683c5792e9f17a58d3ed1eefe.js)
  Character offset 852.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_policies_community:{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{hos
```

**Source references:** SRC-0136, SRC-0146, SRC-0163, SRC-0175, SRC-0177, SRC-0179, SRC-0191, SRC-0192  
**URL references:** None independently associated  
**Related findings:** FND-18183, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18185"></a>
## FND-18185: Declared route web_oauth_certificates

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0080",
  "route_name": "web_oauth_certificates",
  "url_pattern": "/certs",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_oauth_certificates",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0141"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/certs`]],defaults:{host:`oauth.chess-dev.com`},requirements:{host:`(oauth)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?:oauth)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0141** `research/play-chunks/client.32a69dc3.AQ-Pk-x73V.chunk.js` — [preserved redacted evidence](../evidence/text/893674ce7b93f14f5f55ba654a2a6ed7e5333678598089715caf263a0e77f800.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_oauth_certificates:{tokens:[[`text`,`/certs`]],defaults:{host:`oauth.chess-dev.com`},requirements:{host:`(oauth)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|
```

**Source references:** SRC-0141  
**URL references:** None independently associated  
**Related findings:** FND-19434, FND-19456

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18186"></a>
## FND-18186: Declared route web_club_callback_team_match_seek_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0081",
  "route_name": "web_club_callback_team_match_seek_view",
  "url_pattern": "/callback/club/{id}/daily/match-seek/get",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_club_callback_team_match_seek_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/daily/match-seek/get`],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 163.

```text
ow.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_club_callback_team_match_seek_view:{tokens:[[`text`,`/daily/match-seek/get`],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|e
```

**Source references:** SRC-0145  
**URL references:** None independently associated  
**Related findings:** FND-18187, FND-18188

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18187"></a>
## FND-18187: Declared route web_votechess_get_group_seek_data

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0082",
  "route_name": "web_votechess_get_group_seek_data",
  "url_pattern": "/votechess/seek/data/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_votechess_get_group_seek_data",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145"
  ],
  "character_offset": 910,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 944.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_votechess_get_group_seek_data:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_I
```

**Source references:** SRC-0145  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18188

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18188"></a>
## FND-18188: Declared route web_tournaments_live_arena_redirect

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0083",
  "route_name": "web_tournaments_live_arena_redirect",
  "url_pattern": "/tournament/live/arena/redirect-to/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tournaments_live_arena_redirect",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145"
  ],
  "character_offset": 1659,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/tournament/live/arena/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 1695.

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournaments_live_arena_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/arena/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|
```

**Source references:** SRC-0145  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18187

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18189"></a>
## FND-18189: Declared route web_team_match_live_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0084",
  "route_name": "web_team_match_live_view",
  "url_pattern": "/club/matches/live/{match}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_team_match_live_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145",
    "SRC-0781"
  ],
  "character_offset": 2432,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`match`,!0],[`text`,`/club/matches/live`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 2457.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_team_match_live_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches/live`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 60893.

```text
schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_team_match_live_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches/live`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_E
```

**Source references:** SRC-0145, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18187, FND-18188, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18190"></a>
## FND-18190: Declared route web_tournaments_live_redirect

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0085",
  "route_name": "web_tournaments_live_redirect",
  "url_pattern": "/tournament/live/redirect-to/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_tournaments_live_redirect",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145"
  ],
  "character_offset": 3184,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 3214.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|
```

**Source references:** SRC-0145  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18187, FND-18188

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18191"></a>
## FND-18191: Declared route i18n_web_tournaments_live_arena_redirect

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0086",
  "route_name": "i18n_web_tournaments_live_arena_redirect",
  "url_pattern": "/{_locale}/tournament/live/arena/redirect-to/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tournaments_live_arena_redirect",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145"
  ],
  "character_offset": 3945,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/tournament/live/arena/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 3986.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournaments_live_arena_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/arena/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host
```

**Source references:** SRC-0145  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18187, FND-18188

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18192"></a>
## FND-18192: Declared route i18n_web_team_match_live_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0087",
  "route_name": "i18n_web_team_match_live_view",
  "url_pattern": "/{_locale}/club/matches/live/{match}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_team_match_live_view",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145",
    "SRC-0781"
  ],
  "character_offset": 4804,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`match`,!0],[`text`,`/club/matches/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{match:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 4834.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_live_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-d
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 64607.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_team_match_live_view:{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-d
```

**Source references:** SRC-0145, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18187, FND-18188, FND-18117, FND-18118

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18193"></a>
## FND-18193: Declared route i18n_web_tournaments_live_redirect

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0088",
  "route_name": "i18n_web_tournaments_live_redirect",
  "url_pattern": "/{_locale}/tournament/live/redirect-to/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_tournaments_live_redirect",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0145"
  ],
  "character_offset": 5642,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0145** `research/play-chunks/client.4789876b.OIw87FW1Ur.chunk.js` — [preserved redacted evidence](../evidence/text/a0907399add239c3c896b4ce70ae4dde35c8d3e83e50ad055a5eb74fb2bb989d.js)
  Character offset 5677.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_tournaments_live_redirect:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.
```

**Source references:** SRC-0145  
**URL references:** None independently associated  
**Related findings:** FND-18186, FND-18187, FND-18188

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18194"></a>
## FND-18194: Declared route web_game_seek_callback_get

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0089",
  "route_name": "web_game_seek_callback_get",
  "url_pattern": "/callback/game_seek/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_seek_callback_get",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0157"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0157** `research/play-chunks/client.7270d63d.kMserZAQjC.chunk.js` — [preserved redacted evidence](../evidence/text/ff1b9e85da2ef2bbd05c4a93024ab05c428f3535f57496a161ad579696344c4b.js)
  Character offset 151.

```text
.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_game_seek_callback_get:{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_
```

**Source references:** SRC-0157  
**URL references:** None independently associated  
**Related findings:** FND-18195, FND-18196

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18195"></a>
## FND-18195: Declared route web_user_callback_popup

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0090",
  "route_name": "web_user_callback_popup",
  "url_pattern": "/callback/user/popup/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_popup",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0157",
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "character_offset": 873,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/popup`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0157** `research/play-chunks/client.7270d63d.kMserZAQjC.chunk.js` — [preserved redacted evidence](../evidence/text/ff1b9e85da2ef2bbd05c4a93024ab05c428f3535f57496a161ad579696344c4b.js)
  Character offset 897.

```text
|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_popup:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/popup`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 99320.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_popup:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/popup`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 55745.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_popup:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/popup`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 55745.

```text
en|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_popup:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/popup`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_E
```

**Source references:** SRC-0157, SRC-0781, SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18194, FND-18196, FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18196"></a>
## FND-18196: Declared route pubapi_player_stats

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0091",
  "route_name": "pubapi_player_stats",
  "url_pattern": "/pub/player/{username}/stats",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route pubapi_player_stats",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0157"
  ],
  "character_offset": 1618,
  "raw_route_declaration": "{tokens:[[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0157** `research/play-chunks/client.7270d63d.kMserZAQjC.chunk.js` — [preserved redacted evidence](../evidence/text/ff1b9e85da2ef2bbd05c4a93024ab05c428f3535f57496a161ad579696344c4b.js)
  Character offset 1638.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},pubapi_player_stats:{tokens:[[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]}});try{(function(){var e=typeof window<`u`?window:typeof global<`u`?global:typeof globalThis<`u`?globalThis:typeof self<`u`?self:{},t
```

**Source references:** SRC-0157  
**URL references:** None independently associated  
**Related findings:** FND-18194, FND-18195

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18197"></a>
## FND-18197: Declared route web_member_callback_count_games_vs_opponent

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0092",
  "route_name": "web_member_callback_count_games_vs_opponent",
  "url_pattern": "/callback/member/count/{location}/{username}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_callback_count_games_vs_opponent",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0159"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`live|daily`,`location`,!0],[`text`,`/callback/member/count`]],defaults:{host:`www.chess-dev.com`},requirements:{location:`live|daily`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0159** `research/play-chunks/client.7588617e.DH7NV2kvmd.chunk.js` — [preserved redacted evidence](../evidence/text/0fff931cb946efaf8538b8006fb0a84f10f54722e6a8f638eb4cf738fe806f5c.js)
  Character offset 168.

```text
esscom.routes||{},Object.assign(window.chesscom.routes,{web_member_callback_count_games_vs_opponent:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`live|daily`,`location`,!0],[`text`,`/callback/member/count`]],defaults:{host:`www.chess-dev.com`},requirements:{location:`live|daily`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY
```

**Source references:** SRC-0159  
**URL references:** None independently associated  
**Related findings:** FND-19434, FND-19518

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18198"></a>
## FND-18198: Declared route web_verification_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0093",
  "route_name": "web_verification_index",
  "url_pattern": "/verified",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_verification_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0177",
    "SRC-0178",
    "SRC-0191"
  ],
  "character_offset": 824,
  "raw_route_declaration": "{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 847.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-0178** `research/play-chunks/client.b63508a8.TV1r5gKe8m.chunk.js` — [preserved redacted evidence](../evidence/text/058cb22094e269d06d05dba21718fcedcfb7af95d49e1777e4e763e7ae7bb9ab.js)
  Character offset 147.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 1633.

```text
k|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_verification_index:{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|
```

**Source references:** SRC-0177, SRC-0178, SRC-0191  
**URL references:** None independently associated  
**Related findings:** FND-18183, FND-18184, FND-18199, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18199"></a>
## FND-18199: Declared route i18n_web_verification_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0094",
  "route_name": "i18n_web_verification_index",
  "url_pattern": "/{_locale}/verified",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_verification_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0177",
    "SRC-0178",
    "SRC-0191"
  ],
  "character_offset": 2303,
  "raw_route_declaration": "{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0177** `research/play-chunks/client.b575bf8d.DglgoUFndd.chunk.js` — [preserved redacted evidence](../evidence/text/0028d9058d0a86d257d71c627e62d7f6714be854b986a82e9a1bf1c4a6cabb74.js)
  Character offset 2331.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-0178** `research/play-chunks/client.b63508a8.TV1r5gKe8m.chunk.js` — [preserved redacted evidence](../evidence/text/058cb22094e269d06d05dba21718fcedcfb7af95d49e1777e4e763e7ae7bb9ab.js)
  Character offset 845.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```
- **SRC-0191** `research/play-chunks/client.d976f756.ExiAKnE9rz.chunk.js` — [preserved redacted evidence](../evidence/text/960d6d244581e2c6cf8a346836cfdcfc3dd1eee17f5687caba27eea271e04f5d.js)
  Character offset 2331.

```text
aken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_verification_index:{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!a
```

**Source references:** SRC-0177, SRC-0178, SRC-0191  
**URL references:** None independently associated  
**Related findings:** FND-18183, FND-18184, FND-18198, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18200"></a>
## FND-18200: Declared route web_event_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0095",
  "route_name": "web_event_index",
  "url_pattern": "/events",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_event_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0183",
    "SRC-0187"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0183** `research/play-chunks/client.c7f33bdc.CZI5g1X-MW.chunk.js` — [preserved redacted evidence](../evidence/text/9e0b2cc2b609701c265b68cd697a0f0fcb0dcfed1fc0ea8daddf1e4e26eaaec5.js)
  Character offset 140.

```text
ow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_event_index:{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```
- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 140.

```text
ow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_event_index:{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu
```

**Source references:** SRC-0183, SRC-0187  
**URL references:** None independently associated  
**Related findings:** FND-18201, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18201"></a>
## FND-18201: Declared route i18n_web_event_index

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0096",
  "route_name": "i18n_web_event_index",
  "url_pattern": "/{_locale}/events",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_event_index",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0183",
    "SRC-0187"
  ],
  "character_offset": 808,
  "raw_route_declaration": "{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0183** `research/play-chunks/client.c7f33bdc.CZI5g1X-MW.chunk.js` — [preserved redacted evidence](../evidence/text/9e0b2cc2b609701c265b68cd697a0f0fcb0dcfed1fc0ea8daddf1e4e26eaaec5.js)
  Character offset 829.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_event_index:{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```
- **SRC-0187** `research/play-chunks/client.cc96dfb7.C5YLkh3jZT.chunk.js` — [preserved redacted evidence](../evidence/text/b56fb7107bc84ab8fd248841e29159a59243f0a1a67d82391e250268a8050376.js)
  Character offset 829.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_event_index:{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!adm
```

**Source references:** SRC-0183, SRC-0187  
**URL references:** None independently associated  
**Related findings:** FND-18200, FND-19434

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18202"></a>
## FND-18202: Declared route web_game_daily

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0097",
  "route_name": "web_game_daily",
  "url_pattern": "/game/daily/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_daily",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0185",
    "SRC-0781"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0185** `research/play-chunks/client.c99e9053.T-v1At4smI.chunk.js` — [preserved redacted evidence](../evidence/text/2ea3d95c3779cb2a143435df4b4a5edd0b51fb00a67d1cf3d966eaea70d1f09a.js)
  Character offset 139.

```text
dow.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|f
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 12638.

```text
cchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|f
```

**Source references:** SRC-0185, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18203, FND-19434, FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18203"></a>
## FND-18203: Declared route i18n_web_game_daily

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0098",
  "route_name": "i18n_web_game_daily",
  "url_pattern": "/{_locale}/game/daily/{id}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_game_daily",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0185",
    "SRC-0781"
  ],
  "character_offset": 845,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0185** `research/play-chunks/client.c99e9053.T-v1At4smI.chunk.js` — [preserved redacted evidence](../evidence/text/2ea3d95c3779cb2a143435df4b4a5edd0b51fb00a67d1cf3d966eaea70d1f09a.js)
  Character offset 865.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 35556.

```text
sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,
```

**Source references:** SRC-0185, SRC-0781  
**URL references:** None independently associated  
**Related findings:** FND-18202, FND-19434, FND-18117, FND-18118, FND-18125

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18204"></a>
## FND-18204: Declared route web_move_condition_callback_save

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0099",
  "route_name": "web_move_condition_callback_save",
  "url_pattern": "/callback/move-condition/game/{id}/save",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_move_condition_callback_save",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-0196"
  ],
  "character_offset": 124,
  "raw_route_declaration": "{tokens:[[`text`,`/save`],[`variable`,`/`,`\\\\d+`,`id`,!0],[`text`,`/callback/move-condition/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-0196** `research/play-chunks/client.e40aa74c.B791Jm9PEx.chunk.js` — [preserved redacted evidence](../evidence/text/02189c9a5a423c14fc9f58a1a95059099ef5f122b3d2db97c4c16e6281437c69.js)
  Character offset 157.

```text
s=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_move_condition_callback_save:{tokens:[[`text`,`/save`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/move-condition/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|
```

**Source references:** SRC-0196  
**URL references:** None independently associated  
**Related findings:** FND-19434, FND-19450

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18205"></a>
## FND-18205: Declared route web_league_division

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0100",
  "route_name": "web_league_division",
  "url_pattern": "/leagues/{league}/{division}",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_league_division",
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
  "character_offset": 2175,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[\\\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\\\w+`,division:`[\\\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
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
**Related findings:** FND-18139, FND-18142

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.
