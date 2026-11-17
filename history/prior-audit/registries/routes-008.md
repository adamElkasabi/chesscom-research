# Declared page and route inventory

[Master index](../00_MASTER_INDEX.md)

## RTE-0281 — web_library_collection_upload_thumbnail

- URL pattern (derived): `/callback/library/collections/{uuid}/actions/upload-thumbnail`
- Methods: POST
- Purpose: declared route web_library_collection_upload_thumbnail
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18386](../findings/routes-003.md#FND-18386)

```javascript
{tokens:[[`text`,`/actions/upload-thumbnail`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0282 — web_library_collection_update_participant

- URL pattern (derived): `/callback/library/collections/{uuid}/participants/{userId}`
- Methods: PUT
- Purpose: declared route web_library_collection_update_participant
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18387](../findings/routes-003.md#FND-18387)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`userId`,!0],[`text`,`/participants`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]}
```

## RTE-0283 — web_library_callback_create_collection

- URL pattern (derived): `/callback/library/collections`
- Methods: POST
- Purpose: declared route web_library_callback_create_collection
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18388](../findings/routes-003.md#FND-18388)

```javascript
{tokens:[[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0284 — web_library_collection_update_collection

- URL pattern (derived): `/library/collections/{uuid}/actions/update`
- Methods: POST
- Purpose: declared route web_library_collection_update_collection
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18389](../findings/routes-003.md#FND-18389)

```javascript
{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0285 — web_library_create_collection

- URL pattern (derived): `/library/collections`
- Methods: POST
- Purpose: declared route web_library_create_collection
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18390](../findings/routes-003.md#FND-18390)

```javascript
{tokens:[[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0286 — web_library_collection_update_collection_json

- URL pattern (derived): `/library/collections/{uuid}/actions/update`
- Methods: PUT
- Purpose: declared route web_library_collection_update_collection_json
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18391](../findings/routes-003.md#FND-18391)

```javascript
{tokens:[[`text`,`/actions/update`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]}
```

## RTE-0287 — web_library_home

- URL pattern (derived): `/library`
- Methods: GET
- Purpose: declared route web_library_home
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18392](../findings/routes-003.md#FND-18392)

```javascript
{tokens:[[`text`,`/library`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0288 — web_library_callback_collection_privacy

- URL pattern (derived): `/callback/library/collections/{uuid}/actions/privacy`
- Methods: POST
- Purpose: declared route web_library_callback_collection_privacy
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18393](../findings/routes-003.md#FND-18393)

```javascript
{tokens:[[`text`,`/actions/privacy`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/collections`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0289 — i18n_web_library_home

- URL pattern (derived): `/{_locale}/library`
- Methods: GET
- Purpose: declared route i18n_web_library_home
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18394](../findings/routes-003.md#FND-18394)

```javascript
{tokens:[[`text`,`/library`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0290 — web_friend_request_callback

- URL pattern (derived): `/callback/friend/request/{user}`
- Methods: POST
- Purpose: declared route web_friend_request_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18395](../findings/routes-003.md#FND-18395)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0291 — web_friend_accept_request_callback

- URL pattern (derived): `/callback/friend/accept/{user}`
- Methods: PUT
- Purpose: declared route web_friend_accept_request_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18396](../findings/routes-003.md#FND-18396)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/accept`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`PUT`],schemes:[`https`]}
```

## RTE-0292 — web_member_callback_block_member

- URL pattern (derived): `/callback/member/block/{username}`
- Methods: POST
- Purpose: declared route web_member_callback_block_member
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18397](../findings/routes-003.md#FND-18397)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/block`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0293 — web_friend_cancel_request_callback

- URL pattern (derived): `/callback/friend/cancel/request/{user}`
- Methods: POST
- Purpose: declared route web_friend_cancel_request_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18398](../findings/routes-003.md#FND-18398)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/cancel/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0294 — web_user_callback_valid_username

- URL pattern (derived): `/callback/user/valid`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_callback_valid_username
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18399](../findings/routes-003.md#FND-18399)

```javascript
{tokens:[[`text`,`/callback/user/valid`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0295 — i18n_web_user_callback_valid_username

- URL pattern (derived): `/{_locale}/callback/user/valid`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_user_callback_valid_username
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18400](../findings/routes-003.md#FND-18400)

```javascript
{tokens:[[`text`,`/callback/user/valid`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0296 — web_friend_decline_request_callback

- URL pattern (derived): `/callback/friend/decline/request/{user}`
- Methods: DELETE
- Purpose: declared route web_friend_decline_request_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18401](../findings/routes-003.md#FND-18401)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/decline/request`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}
```

## RTE-0297 — web_friend_delete_callback

- URL pattern (derived): `/callback/friend/delete/{user}`
- Methods: DELETE
- Purpose: declared route web_friend_delete_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18402](../findings/routes-003.md#FND-18402)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`user`,!0],[`text`,`/callback/friend/delete`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`DELETE`],schemes:[`https`]}
```

## RTE-0298 — web_user_callback_dismiss_follow_suggestion

- URL pattern (derived): `/callback/user/dismiss_follow/{username}`
- Methods: POST
- Purpose: declared route web_user_callback_dismiss_follow_suggestion
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18403](../findings/routes-003.md#FND-18403)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/dismiss_follow`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0299 — web_user_callback_report_reasons

- URL pattern (derived): `/callback/report-user`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_callback_report_reasons
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18404](../findings/routes-003.md#FND-18404)

```javascript
{tokens:[[`text`,`/callback/report-user`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0300 — pubapi_player_profile

- URL pattern (derived): `/pub/player/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route pubapi_player_profile
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18405](../findings/routes-003.md#FND-18405)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]}
```

## RTE-0301 — web_user_callback_follow_suggestions

- URL pattern (derived): `/callback/user/follow_suggestions`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_callback_follow_suggestions
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18406](../findings/routes-004.md#FND-18406)

```javascript
{tokens:[[`text`,`/callback/user/follow_suggestions`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0302 — web_user_callback_recent_opponents

- URL pattern (derived): `/callback/recent/opponents`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_callback_recent_opponents
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18407](../findings/routes-004.md#FND-18407)

```javascript
{tokens:[[`text`,`/callback/recent/opponents`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0303 — web_guest_update_skill_level

- URL pattern (derived): `/guest/update-skill-level`
- Methods: POST
- Purpose: declared route web_guest_update_skill_level
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18408](../findings/routes-004.md#FND-18408)

```javascript
{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0304 — web_user_callback_set_archive_view

- URL pattern (derived): `/callback/user/archive-view`
- Methods: POST
- Purpose: declared route web_user_callback_set_archive_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18409](../findings/routes-004.md#FND-18409)

```javascript
{tokens:[[`text`,`/callback/user/archive-view`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0305 — web_user_callback_set_fair_play_agree

- URL pattern (derived): `/callback/user/set-fair-play-agree/{fairPlayAgree}`
- Methods: POST
- Purpose: declared route web_user_callback_set_fair_play_agree
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18410](../findings/routes-004.md#FND-18410)

```javascript
{tokens:[[`variable`,`/`,`1|0`,`fairPlayAgree`,!0],[`text`,`/callback/user/set-fair-play-agree`]],defaults:{host:`www.chess-dev.com`},requirements:{fairPlayAgree:`1|0`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0306 — web_user_callback_set_home_recent_content_type

- URL pattern (derived): `/callback/user/home-recent-content-type`
- Methods: POST
- Purpose: declared route web_user_callback_set_home_recent_content_type
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18411](../findings/routes-004.md#FND-18411)

```javascript
{tokens:[[`text`,`/callback/user/home-recent-content-type`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0307 — web_member_callback_track_member

- URL pattern (derived): `/callback/member/track/{username}`
- Methods: POST
- Purpose: declared route web_member_callback_track_member
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18412](../findings/routes-004.md#FND-18412)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/track`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0308 — web_member_callback_unblock_member

- URL pattern (derived): `/callback/member/unblock/{username}`
- Methods: POST
- Purpose: declared route web_member_callback_unblock_member
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18413](../findings/routes-004.md#FND-18413)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/unblock`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0309 — web_member_callback_untrack_member

- URL pattern (derived): `/callback/member/untrack/{username}`
- Methods: POST
- Purpose: declared route web_member_callback_untrack_member
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18414](../findings/routes-004.md#FND-18414)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/member/untrack`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0310 — web_simple_delegated_authentication

- URL pattern (derived): `/callback/auth/{realm}/{codeName}`
- Methods: GET, OPTIONS
- Purpose: declared route web_simple_delegated_authentication
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18415](../findings/routes-004.md#FND-18415)

```javascript
{tokens:[[`variable`,`/`,`\\w+`,`codeName`,!0],[`variable`,`/`,`\\w+`,`realm`,!0],[`text`,`/callback/auth`]],defaults:{host:`www.chess-dev.com`},requirements:{realm:`\\w+`,codeName:`\\w+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`,`OPTIONS`],schemes:[`https`]}
```

## RTE-0311 — web_master_games_callback_search

- URL pattern (derived): `/callback/games/search`
- Methods: GET
- Purpose: declared route web_master_games_callback_search
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18416](../findings/routes-004.md#FND-18416)

```javascript
{tokens:[[`text`,`/callback/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0312 — web_classroom_callback_get_countries

- URL pattern (derived): `/callback/classroom/get-countries`
- Methods: GET
- Purpose: declared route web_classroom_callback_get_countries
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18417](../findings/routes-004.md#FND-18417)

```javascript
{tokens:[[`text`,`/callback/classroom/get-countries`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0313 — i18n_web_classroom_callback_get_countries

- URL pattern (derived): `/{_locale}/callback/classroom/get-countries`
- Methods: GET
- Purpose: declared route i18n_web_classroom_callback_get_countries
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18418](../findings/routes-004.md#FND-18418)

```javascript
{tokens:[[`text`,`/callback/classroom/get-countries`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0314 — web_content_gifs

- URL pattern (derived): `/gifs`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_content_gifs
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18419](../findings/routes-004.md#FND-18419)

```javascript
{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0315 — i18n_web_content_gifs

- URL pattern (derived): `/{_locale}/gifs`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_content_gifs
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18420](../findings/routes-004.md#FND-18420)

```javascript
{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0316 — web_game_get_gif_url

- URL pattern (derived): `/callback/game/gif/{type}/{id}`
- Methods: GET
- Purpose: declared route web_game_get_gif_url
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18421](../findings/routes-004.md#FND-18421)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`variable`,`/`,`daily|live`,`type`,!0],[`text`,`/callback/game/gif`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0317 — web_game_callback_create_dyn_gif_url

- URL pattern (derived): `/callback/game/dyn-gif`
- Methods: POST
- Purpose: declared route web_game_callback_create_dyn_gif_url
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18422](../findings/routes-004.md#FND-18422)

```javascript
{tokens:[[`text`,`/callback/game/dyn-gif`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0318 — web_game_archive_callback

- URL pattern (derived): `/callback/games/archive`
- Methods: GET
- Purpose: declared route web_game_archive_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18423](../findings/routes-004.md#FND-18423)

```javascript
{tokens:[[`text`,`/callback/games/archive`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0319 — web_friend_registration_invite_link_callback

- URL pattern (derived): `/callback/friend/registration-invite-link`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_friend_registration_invite_link_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1137, SRC-1165
- Detailed finding: [FND-18424](../findings/routes-004.md#FND-18424)

```javascript
{tokens:[[`text`,`/callback/friend/registration-invite-link`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0320 — web_profile_view_stats

- URL pattern (derived): `/member/{username}/stats/{statType}`
- Methods: GET
- Purpose: declared route web_profile_view_stats
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1143, SRC-1170
- Detailed finding: [FND-18425](../findings/routes-004.md#FND-18425)

```javascript
{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`]],defaults:{statType:null,host:`www.chess-dev.com`},requirements:{statType:`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```
