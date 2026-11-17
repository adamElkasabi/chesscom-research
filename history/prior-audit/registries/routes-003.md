# Declared page and route inventory

[Master index](../00_MASTER_INDEX.md)

## RTE-0081 — web_club_callback_team_match_seek_view

- URL pattern (derived): `/callback/club/{id}/daily/match-seek/get`
- Methods: GET
- Purpose: declared route web_club_callback_team_match_seek_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145
- Detailed finding: [FND-18186](../findings/routes-001.md#FND-18186)

```javascript
{tokens:[[`text`,`/daily/match-seek/get`],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0082 — web_votechess_get_group_seek_data

- URL pattern (derived): `/votechess/seek/data/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_votechess_get_group_seek_data
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145
- Detailed finding: [FND-18187](../findings/routes-001.md#FND-18187)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/votechess/seek/data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0083 — web_tournaments_live_arena_redirect

- URL pattern (derived): `/tournament/live/arena/redirect-to/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_tournaments_live_arena_redirect
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145
- Detailed finding: [FND-18188](../findings/routes-001.md#FND-18188)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/arena/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0084 — web_team_match_live_view

- URL pattern (derived): `/club/matches/live/{match}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_team_match_live_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145, SRC-0781
- Detailed finding: [FND-18189](../findings/routes-001.md#FND-18189)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches/live`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0085 — web_tournaments_live_redirect

- URL pattern (derived): `/tournament/live/redirect-to/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_tournaments_live_redirect
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145
- Detailed finding: [FND-18190](../findings/routes-001.md#FND-18190)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0086 — i18n_web_tournaments_live_arena_redirect

- URL pattern (derived): `/{_locale}/tournament/live/arena/redirect-to/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_tournaments_live_arena_redirect
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145
- Detailed finding: [FND-18191](../findings/routes-001.md#FND-18191)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/arena/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0087 — i18n_web_team_match_live_view

- URL pattern (derived): `/{_locale}/club/matches/live/{match}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_team_match_live_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145, SRC-0781
- Detailed finding: [FND-18192](../findings/routes-001.md#FND-18192)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0088 — i18n_web_tournaments_live_redirect

- URL pattern (derived): `/{_locale}/tournament/live/redirect-to/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_tournaments_live_redirect
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0145
- Detailed finding: [FND-18193](../findings/routes-001.md#FND-18193)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/tournament/live/redirect-to`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0089 — web_game_seek_callback_get

- URL pattern (derived): `/callback/game_seek/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_game_seek_callback_get
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0157
- Detailed finding: [FND-18194](../findings/routes-001.md#FND-18194)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0090 — web_user_callback_popup

- URL pattern (derived): `/callback/user/popup/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_callback_popup
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0157, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18195](../findings/routes-001.md#FND-18195)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/callback/user/popup`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0091 — pubapi_player_stats

- URL pattern (derived): `/pub/player/{username}/stats`
- Methods: not established; empty/missing route constraint
- Purpose: declared route pubapi_player_stats
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0157
- Detailed finding: [FND-18196](../findings/routes-001.md#FND-18196)

```javascript
{tokens:[[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`],[`text`,`/pub/player`]],defaults:[],requirements:[],hosttokens:[[`text`,`api.chess-dev.com`]],methods:[],schemes:[`https`]}
```

## RTE-0092 — web_member_callback_count_games_vs_opponent

- URL pattern (derived): `/callback/member/count/{location}/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_member_callback_count_games_vs_opponent
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0159
- Detailed finding: [FND-18197](../findings/routes-001.md#FND-18197)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`variable`,`/`,`live|daily`,`location`,!0],[`text`,`/callback/member/count`]],defaults:{host:`www.chess-dev.com`},requirements:{location:`live|daily`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0093 — web_verification_index

- URL pattern (derived): `/verified`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_verification_index
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0177, SRC-0178, SRC-0191
- Detailed finding: [FND-18198](../findings/routes-001.md#FND-18198)

```javascript
{tokens:[[`text`,`/verified`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0094 — i18n_web_verification_index

- URL pattern (derived): `/{_locale}/verified`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_verification_index
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0177, SRC-0178, SRC-0191
- Detailed finding: [FND-18199](../findings/routes-001.md#FND-18199)

```javascript
{tokens:[[`text`,`/verified`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0095 — web_event_index

- URL pattern (derived): `/events`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_event_index
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0183, SRC-0187
- Detailed finding: [FND-18200](../findings/routes-001.md#FND-18200)

```javascript
{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0096 — i18n_web_event_index

- URL pattern (derived): `/{_locale}/events`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_event_index
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0183, SRC-0187
- Detailed finding: [FND-18201](../findings/routes-001.md#FND-18201)

```javascript
{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0097 — web_game_daily

- URL pattern (derived): `/game/daily/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_game_daily
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0185, SRC-0781
- Detailed finding: [FND-18202](../findings/routes-001.md#FND-18202)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0098 — i18n_web_game_daily

- URL pattern (derived): `/{_locale}/game/daily/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_game_daily
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0185, SRC-0781
- Detailed finding: [FND-18203](../findings/routes-001.md#FND-18203)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0099 — web_move_condition_callback_save

- URL pattern (derived): `/callback/move-condition/game/{id}/save`
- Methods: POST
- Purpose: declared route web_move_condition_callback_save
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0196
- Detailed finding: [FND-18204](../findings/routes-001.md#FND-18204)

```javascript
{tokens:[[`text`,`/save`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/move-condition/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0100 — web_league_division

- URL pattern (derived): `/leagues/{league}/{division}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_league_division
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0201, SRC-0780, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18205](../findings/routes-001.md#FND-18205)

```javascript
{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0101 — i18n_web_league_division

- URL pattern (derived): `/{_locale}/leagues/{league}/{division}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_league_division
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0201, SRC-0780, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18206](../findings/routes-002.md#FND-18206)

```javascript
{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0102 — web_analysis_ceac

- URL pattern (derived): `/analysis/game/{type}/{gameId}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_analysis_ceac
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754, SRC-1137, SRC-1165
- Detailed finding: [FND-18207](../findings/routes-002.md#FND-18207)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0103 — i18n_web_analysis_ceac

- URL pattern (derived): `/{_locale}/analysis/game/{type}/{gameId}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_analysis_ceac
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754, SRC-1137, SRC-1165
- Detailed finding: [FND-18208](../findings/routes-002.md#FND-18208)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{type:`daily|live|master|pgn|computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0104 — web_analysis_game_callback_user_allowed_view

- URL pattern (derived): `/callback/analysis/user/allowed`
- Methods: GET
- Purpose: declared route web_analysis_game_callback_user_allowed_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754
- Detailed finding: [FND-18209](../findings/routes-002.md#FND-18209)

```javascript
{tokens:[[`text`,`/callback/analysis/user/allowed`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0105 — web_play_computer_chess960

- URL pattern (derived): `/play/computer/chess960`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_computer_chess960
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754
- Detailed finding: [FND-18210](../findings/routes-002.md#FND-18210)

```javascript
{tokens:[[`text`,`/play/computer/chess960`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0106 — i18n_web_play_computer_chess960

- URL pattern (derived): `/{_locale}/play/computer/chess960`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_computer_chess960
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754
- Detailed finding: [FND-18211](../findings/routes-002.md#FND-18211)

```javascript
{tokens:[[`text`,`/play/computer/chess960`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0107 — web_chess_variants

- URL pattern (derived): `/variants/{variant}`
- Methods: GET
- Purpose: declared route web_chess_variants
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754, SRC-0781
- Detailed finding: [FND-18212](../findings/routes-002.md#FND-18212)

```javascript
{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`]],defaults:{variant:null,host:`www.chess-dev.com`},requirements:{variant:`.+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0108 — i18n_web_chess_variants

- URL pattern (derived): `/{_locale}/variants/{variant}`
- Methods: GET
- Purpose: declared route i18n_web_chess_variants
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0754, SRC-0781
- Detailed finding: [FND-18213](../findings/routes-002.md#FND-18213)

```javascript
{tokens:[[`variable`,`/`,`.+`,`variant`,!0],[`text`,`/variants`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{variant:null,host:`www.chess-dev.com`,_locale:``},requirements:{variant:`.+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0109 — web_membership_gift

- URL pattern (derived): `/membership/gift/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_membership_gift
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0776
- Detailed finding: [FND-18214](../findings/routes-002.md#FND-18214)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/membership/gift`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0110 — i18n_web_membership_gift

- URL pattern (derived): `/{_locale}/membership/gift/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_membership_gift
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0776
- Detailed finding: [FND-18215](../findings/routes-002.md#FND-18215)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/membership/gift`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0111 — web_classroom

- URL pattern (derived): `/classroom`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_classroom
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0779, SRC-0781
- Detailed finding: [FND-18216](../findings/routes-002.md#FND-18216)

```javascript
{tokens:[[`text`,`/classroom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0112 — i18n_web_classroom

- URL pattern (derived): `/{_locale}/classroom`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_classroom
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0779, SRC-0781
- Detailed finding: [FND-18217](../findings/routes-002.md#FND-18217)

```javascript
{tokens:[[`text`,`/classroom`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0113 — web_coach_hide_saved_game

- URL pattern (derived): `/callback/coach/hide-game/{id}`
- Methods: POST
- Purpose: declared route web_coach_hide_saved_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0779
- Detailed finding: [FND-18218](../findings/routes-002.md#FND-18218)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/coach/hide-game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0114 — web_computer_hide_saved_game

- URL pattern (derived): `/callback/computer/hide-game/{id}`
- Methods: POST
- Purpose: declared route web_computer_hide_saved_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0779
- Detailed finding: [FND-18219](../findings/routes-002.md#FND-18219)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/computer/hide-game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0115 — web_live_game

- URL pattern (derived): `/live/game/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_live_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18220](../findings/routes-002.md#FND-18220)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0116 — web_play_club_challenges

- URL pattern (derived): `/play/online/club-challenges`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_club_challenges
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18221](../findings/routes-002.md#FND-18221)

```javascript
{tokens:[[`text`,`/play/online/club-challenges`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0117 — web_game_coach

- URL pattern (derived): `/game/coach/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_game_coach
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18222](../findings/routes-002.md#FND-18222)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0118 — web_game_computer

- URL pattern (derived): `/game/computer/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_game_computer
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18223](../findings/routes-002.md#FND-18223)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0119 — web_play_connected_board

- URL pattern (derived): `/play/online/connected-board`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_connected_board
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18224](../findings/routes-002.md#FND-18224)

```javascript
{tokens:[[`text`,`/play/online/connected-board`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0120 — web_play_create_tournament

- URL pattern (derived): `/play/online/create-tournament/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_create_tournament
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18225](../findings/routes-002.md#FND-18225)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/online/create-tournament`]],defaults:{id:``,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```
