# Declared page and route inventory

[Master index](../00_MASTER_INDEX.md)

## RTE-0161 — i18n_web_play_new

- URL pattern (derived): `/{_locale}/play/online/new`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_new
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18266](../findings/routes-002.md#FND-18266)

```javascript
{tokens:[[`text`,`/play/online/new`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0162 — i18n_web_play

- URL pattern (derived): `/{_locale}/play/online`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18267](../findings/routes-002.md#FND-18267)

```javascript
{tokens:[[`text`,`/play/online`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0163 — i18n_web_game_uuid

- URL pattern (derived): `/{_locale}/game/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_game_uuid
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18268](../findings/routes-002.md#FND-18268)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0164 — i18n_web_play_settings

- URL pattern (derived): `/{_locale}/play/online/settings`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_settings
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18269](../findings/routes-002.md#FND-18269)

```javascript
{tokens:[[`text`,`/play/online/settings`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0165 — i18n_web_play_live_team_match

- URL pattern (derived): `/{_locale}/play/match/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_live_team_match
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18270](../findings/routes-002.md#FND-18270)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/play/match`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0166 — i18n_web_play_tournaments

- URL pattern (derived): `/{_locale}/play/online/tournaments`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_tournaments
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18271](../findings/routes-002.md#FND-18271)

```javascript
{tokens:[[`text`,`/play/online/tournaments`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0167 — i18n_web_play_variant_3_check

- URL pattern (derived): `/{_locale}/play/online/3-check`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_variant_3_check
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18272](../findings/routes-002.md#FND-18272)

```javascript
{tokens:[[`text`,`/play/online/3-check`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0168 — i18n_web_play_variant_chess960

- URL pattern (derived): `/{_locale}/play/online/chess960`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_variant_chess960
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18273](../findings/routes-002.md#FND-18273)

```javascript
{tokens:[[`text`,`/play/online/chess960`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0169 — i18n_web_play_variant_crazyhouse

- URL pattern (derived): `/{_locale}/play/online/crazyhouse`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_variant_crazyhouse
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18274](../findings/routes-002.md#FND-18274)

```javascript
{tokens:[[`text`,`/play/online/crazyhouse`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0170 — i18n_web_play_variant_doubles_bughouse

- URL pattern (derived): `/{_locale}/play/online/doubles-bughouse`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_variant_doubles_bughouse
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18275](../findings/routes-002.md#FND-18275)

```javascript
{tokens:[[`text`,`/play/online/doubles-bughouse`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0171 — i18n_web_play_variant_king_of_the_hill

- URL pattern (derived): `/{_locale}/play/online/king-of-the-hill`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_variant_king_of_the_hill
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18276](../findings/routes-002.md#FND-18276)

```javascript
{tokens:[[`text`,`/play/online/king-of-the-hill`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0172 — i18n_web_play_watch

- URL pattern (derived): `/{_locale}/play/online/watch`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_watch
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18277](../findings/routes-002.md#FND-18277)

```javascript
{tokens:[[`text`,`/play/online/watch`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0173 — web_search

- URL pattern (derived): `/search`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_search
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18278](../findings/routes-002.md#FND-18278)

```javascript
{tokens:[[`text`,`/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0174 — i18n_web_search

- URL pattern (derived): `/{_locale}/search`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_search
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18279](../findings/routes-002.md#FND-18279)

```javascript
{tokens:[[`text`,`/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0175 — web_bff_oauth_token

- URL pattern (derived): `/bff-token`
- Methods: POST
- Purpose: declared route web_bff_oauth_token
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18280](../findings/routes-002.md#FND-18280)

```javascript
{tokens:[[`text`,`/bff-token`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0176 — web_computer_callback_load_game

- URL pattern (derived): `/{gameType}/callback/game/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_computer_callback_load_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18281](../findings/routes-002.md#FND-18281)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`],[`variable`,`/`,`computer|coach`,`gameType`,!0]],defaults:{gameType:`computer`,host:`www.chess-dev.com`},requirements:{id:`\\d+`,gameType:`computer|coach`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0177 — web_callback_load_game_live_data

- URL pattern (derived): `/callback/live/game/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_callback_load_game_live_data
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18282](../findings/routes-002.md#FND-18282)

```javascript
{tokens:[[`variable`,`/`,`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,`id`,!0],[`text`,`/callback/live/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`(?:\\d+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12})`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0178 — web_daily_callback_load_game

- URL pattern (derived): `/callback/daily/game/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_daily_callback_load_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18283](../findings/routes-002.md#FND-18283)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0179 — web_tournaments_live_arena_view

- URL pattern (derived): `/tournament/live/arena/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_tournaments_live_arena_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18284](../findings/routes-002.md#FND-18284)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live/arena`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0180 — web_tournaments_live_view

- URL pattern (derived): `/tournament/live/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_tournaments_live_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18285](../findings/routes-002.md#FND-18285)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0181 — i18n_web_tournaments_live_arena_view

- URL pattern (derived): `/{_locale}/tournament/live/arena/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_tournaments_live_arena_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18286](../findings/routes-002.md#FND-18286)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live/arena`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0182 — i18n_web_tournaments_live_view

- URL pattern (derived): `/{_locale}/tournament/live/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_tournaments_live_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18287](../findings/routes-002.md#FND-18287)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0183 — web_puzzles_mode_battle_view

- URL pattern (derived): `/puzzles/battle/{shortUuid}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_puzzles_mode_battle_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18288](../findings/routes-002.md#FND-18288)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0184 — i18n_web_puzzles_mode_battle_view

- URL pattern (derived): `/{_locale}/puzzles/battle/{shortUuid}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_puzzles_mode_battle_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18289](../findings/routes-002.md#FND-18289)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`shortUuid`,!0],[`text`,`/puzzles/battle`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0185 — web_user_callback_id_to_user_data

- URL pattern (derived): `/callback/user/id-to-data`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_callback_id_to_user_data
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18290](../findings/routes-002.md#FND-18290)

```javascript
{tokens:[[`text`,`/callback/user/id-to-data`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0186 — web_club_profile

- URL pattern (derived): `/club/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_club_profile
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18291](../findings/routes-002.md#FND-18291)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/club`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0187 — i18n_web_club_profile

- URL pattern (derived): `/{_locale}/club/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_club_profile
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18292](../findings/routes-002.md#FND-18292)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/club`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0188 — web_play_settings_is_on_vacation_callback

- URL pattern (derived): `/callback/play/settings/is-on-vacation`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_settings_is_on_vacation_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18293](../findings/routes-002.md#FND-18293)

```javascript
{tokens:[[`text`,`/callback/play/settings/is-on-vacation`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0189 — web_play_settings_vacation_time_remaining_callback

- URL pattern (derived): `/callback/play/settings/vacation-time-remaining`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_settings_vacation_time_remaining_callback
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18294](../findings/routes-002.md#FND-18294)

```javascript
{tokens:[[`text`,`/callback/play/settings/vacation-time-remaining`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0190 — web_analysis_game_callback_view_all

- URL pattern (derived): `/callback/analysis/game/{type}/{gameId}/all`
- Methods: GET
- Purpose: declared route web_analysis_game_callback_view_all
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18295](../findings/routes-002.md#FND-18295)

```javascript
{tokens:[[`text`,`/all`],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`[^/]++`,`type`,!0],[`text`,`/callback/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```

## RTE-0191 — web_move_condition_callback_get

- URL pattern (derived): `/callback/move-conditions/game/{id}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_move_condition_callback_get
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18296](../findings/routes-002.md#FND-18296)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/move-conditions/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0192 — web_daily_callback_load_next_game

- URL pattern (derived): `/callback/daily/game/{id}/next`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_daily_callback_load_next_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18297](../findings/routes-002.md#FND-18297)

```javascript
{tokens:[[`text`,`/next`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0193 — web_daily_callback_load_previous_game

- URL pattern (derived): `/callback/daily/game/{id}/previous`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_daily_callback_load_previous_game
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18298](../findings/routes-002.md#FND-18298)

```javascript
{tokens:[[`text`,`/previous`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/daily/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0194 — web_game_callback_submit_move

- URL pattern (derived): `/callback/game/{id}/submit-move`
- Methods: POST
- Purpose: declared route web_game_callback_submit_move
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18299](../findings/routes-002.md#FND-18299)

```javascript
{tokens:[[`text`,`/submit-move`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0195 — web_game_callback_offer_draw

- URL pattern (derived): `/callback/game/{id}/offer-draw`
- Methods: POST
- Purpose: declared route web_game_callback_offer_draw
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18300](../findings/routes-002.md#FND-18300)

```javascript
{tokens:[[`text`,`/offer-draw`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0196 — web_game_callback_decline_draw

- URL pattern (derived): `/callback/game/{id}/decline-draw`
- Methods: POST
- Purpose: declared route web_game_callback_decline_draw
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18301](../findings/routes-002.md#FND-18301)

```javascript
{tokens:[[`text`,`/decline-draw`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0197 — web_game_callback_resign

- URL pattern (derived): `/callback/game/{id}/resign`
- Methods: POST
- Purpose: declared route web_game_callback_resign
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18302](../findings/routes-002.md#FND-18302)

```javascript
{tokens:[[`text`,`/resign`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0198 — web_game_seek_callback_accept_seek

- URL pattern (derived): `/callback/game_seek/{id}/accept-seek`
- Methods: POST
- Purpose: declared route web_game_seek_callback_accept_seek
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781
- Detailed finding: [FND-18303](../findings/routes-002.md#FND-18303)

```javascript
{tokens:[[`text`,`/accept-seek`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0199 — web_bucket

- URL pattern (derived): `/callback/bucket`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_bucket
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18304](../findings/routes-002.md#FND-18304)

```javascript
{tokens:[[`text`,`/callback/bucket`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0200 — i18n_web_bucket

- URL pattern (derived): `/{_locale}/callback/bucket`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_bucket
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18305](../findings/routes-002.md#FND-18305)

```javascript
{tokens:[[`text`,`/callback/bucket`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```
