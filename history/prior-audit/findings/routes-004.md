# routes — findings 301–321

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18406"></a>
## FND-18406: Declared route web_user_callback_follow_suggestions

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0301",
  "route_name": "web_user_callback_follow_suggestions",
  "url_pattern": "/callback/user/follow_suggestions",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_follow_suggestions",
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
  "character_offset": 94146,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/follow_suggestions`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 94183.

```text
s:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]},web_user_callback_follow_suggestions:{tokens:[[`text`,`/callback/user/follow_suggestions`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 94183.

```text
s:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]},web_user_callback_follow_suggestions:{tokens:[[`text`,`/callback/user/follow_suggestions`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18407"></a>
## FND-18407: Declared route web_user_callback_recent_opponents

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0302",
  "route_name": "web_user_callback_recent_opponents",
  "url_pattern": "/callback/recent/opponents",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_recent_opponents",
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
  "character_offset": 94877,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/recent/opponents`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 94912.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_recent_opponents:{tokens:[[`text`,`/callback/recent/opponents`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 94912.

```text
achy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_callback_recent_opponents:{tokens:[[`text`,`/callback/recent/opponents`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|h
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18408"></a>
## FND-18408: Declared route web_guest_update_skill_level

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0303",
  "route_name": "web_guest_update_skill_level",
  "url_pattern": "/guest/update-skill-level",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_guest_update_skill_level",
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
  "character_offset": 96322,
  "raw_route_declaration": "{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 96351.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_guest_update_skill_level:{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 96351.

```text
ken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_guest_update_skill_level:{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18409"></a>
## FND-18409: Declared route web_user_callback_set_archive_view

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0304",
  "route_name": "web_user_callback_set_archive_view",
  "url_pattern": "/callback/user/archive-view",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_set_archive_view",
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
  "character_offset": 97043,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/archive-view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 97078.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_archive_view:{tokens:[[`text`,`/callback/user/archive-view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 97078.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_archive_view:{tokens:[[`text`,`/callback/user/archive-view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18410"></a>
## FND-18410: Declared route web_user_callback_set_fair_play_agree

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0305",
  "route_name": "web_user_callback_set_fair_play_agree",
  "url_pattern": "/callback/user/set-fair-play-agree/{fairPlayAgree}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_set_fair_play_agree",
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
  "character_offset": 97772,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`1|0`,`fairPlayAgree`,!0],[`text`,`/callback/user/set-fair-play-agree`]],defaults:{host:`www.chess-dev.com`},requirements:{fairPlayAgree:`1|0`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 97810.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_fair_play_agree:{tokens:[[`variable`,`/`,`1|0`,`fairPlayAgree`,!0],[`text`,`/callback/user/set-fair-play-agree`]],defaults:{host:`www.chess-dev.com`},requirements:{fairPlayAgree:`1|0`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_D
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 97810.

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_fair_play_agree:{tokens:[[`variable`,`/`,`1|0`,`fairPlayAgree`,!0],[`text`,`/callback/user/set-fair-play-agree`]],defaults:{host:`www.chess-dev.com`},requirements:{fairPlayAgree:`1|0`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_D
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18411"></a>
## FND-18411: Declared route web_user_callback_set_home_recent_content_type

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0306",
  "route_name": "web_user_callback_set_home_recent_content_type",
  "url_pattern": "/callback/user/home-recent-content-type",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_user_callback_set_home_recent_content_type",
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
  "character_offset": 98573,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/user/home-recent-content-type`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 98620.

```text
s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_home_recent_content_type:{tokens:[[`text`,`/callback/user/home-recent-content-type`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 98620.

```text
s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_callback_set_home_recent_content_type:{tokens:[[`text`,`/callback/user/home-recent-content-type`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18412"></a>
## FND-18412: Declared route web_member_callback_track_member

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0307",
  "route_name": "web_member_callback_track_member",
  "url_pattern": "/callback/member/track/{username}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_callback_track_member",
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
  "character_offset": 99326,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/track`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 99359.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_member_callback_track_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/track`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 99359.

```text
)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_member_callback_track_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/track`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18413"></a>
## FND-18413: Declared route web_member_callback_unblock_member

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0308",
  "route_name": "web_member_callback_unblock_member",
  "url_pattern": "/callback/member/unblock/{username}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_callback_unblock_member",
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
  "character_offset": 100088,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/unblock`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 100123.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_member_callback_unblock_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/unblock`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 100123.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_member_callback_unblock_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/unblock`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18414"></a>
## FND-18414: Declared route web_member_callback_untrack_member

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0309",
  "route_name": "web_member_callback_untrack_member",
  "url_pattern": "/callback/member/untrack/{username}",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_member_callback_untrack_member",
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
  "character_offset": 100854,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/untrack`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 100889.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_member_callback_untrack_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/untrack`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 100889.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_member_callback_untrack_member:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/untrack`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18415"></a>
## FND-18415: Declared route web_simple_delegated_authentication

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0310",
  "route_name": "web_simple_delegated_authentication",
  "url_pattern": "/callback/auth/{realm}/{codeName}",
  "http_methods": [
    "GET",
    "OPTIONS"
  ],
  "title": "not observed",
  "purpose": "declared route web_simple_delegated_authentication",
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
  "character_offset": 102435,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`\\\\w+`,`codeName`,!0],[`variable`,`/`,`\\\\w+`,`realm`,!0],[`text`,`/callback/auth`]],defaults:{host:`www.chess-dev.com`},requirements:{realm:`\\\\w+`,codeName:`\\\\w+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`,`OPTIONS`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 102471.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_simple_delegated_authentication:{tokens:[[`variable`,`/`,`\\w+`,`codeName`,!0],[`variable`,`/`,`\\w+`,`realm`,!0],[`text`,`/callback/auth`]],defaults:{host:`www.chess-dev.com`},requirements:{realm:`\\w+`,codeName:`\\w+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 102471.

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_simple_delegated_authentication:{tokens:[[`variable`,`/`,`\\w+`,`codeName`,!0],[`variable`,`/`,`\\w+`,`realm`,!0],[`text`,`/callback/auth`]],defaults:{host:`www.chess-dev.com`},requirements:{realm:`\\w+`,codeName:`\\w+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18416"></a>
## FND-18416: Declared route web_master_games_callback_search

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0311",
  "route_name": "web_master_games_callback_search",
  "url_pattern": "/callback/games/search",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_master_games_callback_search",
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
  "character_offset": 103263,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 103296.

```text
?[^\\s]+`,`host`,!0]],methods:[`GET`,`OPTIONS`],schemes:[`https`]},web_master_games_callback_search:{tokens:[[`text`,`/callback/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 103296.

```text
?[^\\s]+`,`host`,!0]],methods:[`GET`,`OPTIONS`],schemes:[`https`]},web_master_games_callback_search:{tokens:[[`text`,`/callback/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18417"></a>
## FND-18417: Declared route web_classroom_callback_get_countries

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0312",
  "route_name": "web_classroom_callback_get_countries",
  "url_pattern": "/callback/classroom/get-countries",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_classroom_callback_get_countries",
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
  "character_offset": 119920,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/classroom/get-countries`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 119957.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_classroom_callback_get_countries:{tokens:[[`text`,`/callback/classroom/get-countries`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 119957.

```text
hy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_classroom_callback_get_countries:{tokens:[[`text`,`/callback/classroom/get-countries`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18418"></a>
## FND-18418: Declared route i18n_web_classroom_callback_get_countries

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0313",
  "route_name": "i18n_web_classroom_callback_get_countries",
  "url_pattern": "/{_locale}/callback/classroom/get-countries",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_classroom_callback_get_countries",
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
  "character_offset": 120656,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/classroom/get-countries`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 120698.

```text
)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_classroom_callback_get_countries:{tokens:[[`text`,`/callback/classroom/get-countries`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 120698.

```text
)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_classroom_callback_get_countries:{tokens:[[`text`,`/callback/classroom/get-countries`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18419"></a>
## FND-18419: Declared route web_content_gifs

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0314",
  "route_name": "web_content_gifs",
  "url_pattern": "/gifs",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_content_gifs",
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
  "character_offset": 126094,
  "raw_route_declaration": "{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 126111.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_content_gifs:{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 126111.

```text
hi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_content_gifs:{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_H
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18420"></a>
## FND-18420: Declared route i18n_web_content_gifs

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0315",
  "route_name": "i18n_web_content_gifs",
  "url_pattern": "/{_locale}/gifs",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_content_gifs",
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
  "character_offset": 126777,
  "raw_route_declaration": "{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 126799.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_content_gifs:{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 126799.

```text
kk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_content_gifs:{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18421"></a>
## FND-18421: Declared route web_game_get_gif_url

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0316",
  "route_name": "web_game_get_gif_url",
  "url_pattern": "/callback/game/gif/{type}/{id}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_get_gif_url",
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
  "character_offset": 127546,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`variable`,`/`,`daily|live`,`type`,!0],[`text`,`/callback/game/gif`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 127567.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_get_gif_url:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`variable`,`/`,`daily|live`,`type`,!0],[`text`,`/callback/game/gif`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 127567.

```text
akk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_get_gif_url:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`variable`,`/`,`daily|live`,`type`,!0],[`text`,`/callback/game/gif`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18422"></a>
## FND-18422: Declared route web_game_callback_create_dyn_gif_url

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0317",
  "route_name": "web_game_callback_create_dyn_gif_url",
  "url_pattern": "/callback/game/dyn-gif",
  "http_methods": [
    "POST"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_callback_create_dyn_gif_url",
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
  "character_offset": 128343,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/game/dyn-gif`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 128380.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_game_callback_create_dyn_gif_url:{tokens:[[`text`,`/callback/game/dyn-gif`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 128380.

```text
?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]},web_game_callback_create_dyn_gif_url:{tokens:[[`text`,`/callback/game/dyn-gif`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18423"></a>
## FND-18423: Declared route web_game_archive_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0318",
  "route_name": "web_game_archive_callback",
  "url_pattern": "/callback/games/archive",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_game_archive_callback",
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
  "character_offset": 133467,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/games/archive`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 133493.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_archive_callback:{tokens:[[`text`,`/callback/games/archive`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 133493.

```text
chaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_game_archive_callback:{tokens:[[`text`,`/callback/games/archive`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_I
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18424"></a>
## FND-18424: Declared route web_friend_registration_invite_link_callback

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0319",
  "route_name": "web_friend_registration_invite_link_callback",
  "url_pattern": "/callback/friend/registration-invite-link",
  "http_methods": [
    "not established; empty/missing route constraint"
  ],
  "title": "not observed",
  "purpose": "declared route web_friend_registration_invite_link_callback",
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
  "character_offset": 136718,
  "raw_route_declaration": "{tokens:[[`text`,`/callback/friend/registration-invite-link`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 136763.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_friend_registration_invite_link_callback:{tokens:[[`text`,`/callback/friend/registration-invite-link`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_P
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 136763.

```text
\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_friend_registration_invite_link_callback:{tokens:[[`text`,`/callback/friend/registration-invite-link`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_P
```

**Source references:** SRC-1137, SRC-1165  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18425"></a>
## FND-18425: Declared route web_profile_view_stats

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0320",
  "route_name": "web_profile_view_stats",
  "url_pattern": "/member/{username}/stats/{statType}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route web_profile_view_stats",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1143",
    "SRC-1170"
  ],
  "character_offset": 554,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{statType:null,host:`www.chess-dev.com`},requirements:{statType:`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1143** `research/tab-review.88a71be6.GEFrxdGEBZ.chunk.js` — [preserved redacted evidence](../evidence/text/cb5b4c9902ca6e5c9e7bedde339a657ca9c1d2108c2daad54cc258185dc6f30c.js)
  Character offset 577.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_profile_view_stats:{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{statType:null,host:`www.chess-dev.com`},requiremen
```
- **SRC-1170** `research.zip!/research/tab-review.88a71be6.GEFrxdGEBZ.chunk.js` — [preserved redacted evidence](../evidence/text/cb5b4c9902ca6e5c9e7bedde339a657ca9c1d2108c2daad54cc258185dc6f30c.js)
  Character offset 577.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_profile_view_stats:{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{statType:null,host:`www.chess-dev.com`},requiremen
```

**Source references:** SRC-1143, SRC-1170  
**URL references:** None independently associated  
**Related findings:** FND-18426, FND-19336

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.

<a id="FND-18426"></a>
## FND-18426: Declared route i18n_web_profile_view_stats

**Category:** routes  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "id": "RTE-0321",
  "route_name": "i18n_web_profile_view_stats",
  "url_pattern": "/{_locale}/member/{username}/stats/{statType}",
  "http_methods": [
    "GET"
  ],
  "title": "not observed",
  "purpose": "declared route i18n_web_profile_view_stats",
  "accessibility": "not established by route declaration",
  "authentication": "not established",
  "roles": "not established",
  "forms": "not established",
  "response": "not observed",
  "redirects": "not observed",
  "source_ids": [
    "SRC-1143",
    "SRC-1170"
  ],
  "character_offset": 1646,
  "raw_route_declaration": "{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{statType:null,host:`www.chess-dev.com`,_locale:``},requirements:{statType:`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\\\.)?[^\\\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\\\.)?[^\\\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}",
  "discovery": "static generated route table; NOT a successful request"
}

### Evidence

- **SRC-1143** `research/tab-review.88a71be6.GEFrxdGEBZ.chunk.js` — [preserved redacted evidence](../evidence/text/cb5b4c9902ca6e5c9e7bedde339a657ca9c1d2108c2daad54cc258185dc6f30c.js)
  Character offset 577.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_profile_view_stats:{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{statType:null,host:`www.chess-dev.com`},requiremen
```
- **SRC-1170** `research.zip!/research/tab-review.88a71be6.GEFrxdGEBZ.chunk.js` — [preserved redacted evidence](../evidence/text/cb5b4c9902ca6e5c9e7bedde339a657ca9c1d2108c2daad54cc258185dc6f30c.js)
  Character offset 577.

```text
scom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_profile_view_stats:{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{statType:null,host:`www.chess-dev.com`},requiremen
```

**Source references:** SRC-1143, SRC-1170  
**URL references:** None independently associated  
**Related findings:** FND-18425, FND-19336

**Additional notes:** Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.
