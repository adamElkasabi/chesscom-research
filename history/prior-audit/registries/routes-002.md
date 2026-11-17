# Declared page and route inventory

[Master index](../00_MASTER_INDEX.md)

## RTE-0041 — web_article_callback_list_authors

- URL pattern (derived): `/callback/articles/authors`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_article_callback_list_authors
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18146](../findings/routes-001.md#FND-18146)

```javascript
{tokens:[[`text`,`/callback/articles/authors`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0042 — web_article_callback_lock_coments

- URL pattern (derived): `/callback/articles/lock-comments/{id}`
- Methods: POST
- Purpose: declared route web_article_callback_lock_coments
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18147](../findings/routes-001.md#FND-18147)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/articles/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0043 — web_blog_callback_lock_coments

- URL pattern (derived): `/callback/blog/lock-comments/{id}`
- Methods: POST
- Purpose: declared route web_blog_callback_lock_coments
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18148](../findings/routes-001.md#FND-18148)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/blog/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0044 — web_news_callback_lock_coments

- URL pattern (derived): `/callback/news/lock-comments/{id}`
- Methods: POST
- Purpose: declared route web_news_callback_lock_coments
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18149](../findings/routes-001.md#FND-18149)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/news/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0045 — web_video_callback_lock_coments

- URL pattern (derived): `/callback/video/lock-comments/{id}`
- Methods: POST
- Purpose: declared route web_video_callback_lock_coments
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18150](../findings/routes-001.md#FND-18150)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/video/lock-comments`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0046 — web_content_callback_feature_article

- URL pattern (derived): `/callback/content/feature/article/{id}`
- Methods: POST
- Purpose: declared route web_content_callback_feature_article
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18151](../findings/routes-001.md#FND-18151)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/article`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0047 — web_content_callback_feature_blog

- URL pattern (derived): `/callback/content/feature/blog/{id}`
- Methods: POST
- Purpose: declared route web_content_callback_feature_blog
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18152](../findings/routes-001.md#FND-18152)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/blog`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0048 — web_content_callback_feature_lesson_course

- URL pattern (derived): `/callback/content/feature/lesson_course/{id}`
- Methods: POST
- Purpose: declared route web_content_callback_feature_lesson_course
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18153](../findings/routes-001.md#FND-18153)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/lesson_course`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0049 — web_content_callback_feature_news

- URL pattern (derived): `/callback/content/feature/news/{id}`
- Methods: POST
- Purpose: declared route web_content_callback_feature_news
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18154](../findings/routes-001.md#FND-18154)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/news`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0050 — web_content_callback_feature_chess_video

- URL pattern (derived): `/callback/content/feature/chess_video/{id}`
- Methods: POST
- Purpose: declared route web_content_callback_feature_chess_video
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18155](../findings/routes-001.md#FND-18155)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/content/feature/chess_video`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0051 — web_user_callback_set_content_language

- URL pattern (derived): `/callback/user/content-language/set`
- Methods: POST
- Purpose: declared route web_user_callback_set_content_language
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18156](../findings/routes-001.md#FND-18156)

```javascript
{tokens:[[`text`,`/callback/user/content-language/set`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0052 — web_security_login_and_go

- URL pattern (derived): `/login_and_go`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_security_login_and_go
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18157](../findings/routes-001.md#FND-18157)

```javascript
{tokens:[[`text`,`/login_and_go`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0053 — web_survey_callback_vote

- URL pattern (derived): `/callback/survey/{id}/vote/{optionId}`
- Methods: POST
- Purpose: declared route web_survey_callback_vote
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18158](../findings/routes-001.md#FND-18158)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`optionId`,!0],[`text`,`/vote`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/survey`]],defaults:{host:`www.chess-dev.com`},requirements:{id:`\\d+`,optionId:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]}
```

## RTE-0054 — web_team_match_view

- URL pattern (derived): `/club/matches/{match}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_team_match_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18159](../findings/routes-001.md#FND-18159)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`]],defaults:{host:`www.chess-dev.com`},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0055 — web_tournament_view

- URL pattern (derived): `/tournament/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_tournament_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18160](../findings/routes-001.md#FND-18160)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0056 — i18n_web_security_login_and_go

- URL pattern (derived): `/{_locale}/login_and_go`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_security_login_and_go
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18161](../findings/routes-001.md#FND-18161)

```javascript
{tokens:[[`text`,`/login_and_go`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0057 — i18n_web_team_match_view

- URL pattern (derived): `/{_locale}/club/matches/{match}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_team_match_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18162](../findings/routes-001.md#FND-18162)

```javascript
{tokens:[[`variable`,`/`,`\\d+`,`match`,!0],[`text`,`/club/matches`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{match:`\\d+`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0058 — i18n_web_tournament_view

- URL pattern (derived): `/{_locale}/tournament/{url}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_tournament_view
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18163](../findings/routes-001.md#FND-18163)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`url`,!0],[`text`,`/tournament`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0059 — web_stats

- URL pattern (derived): `/stats/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_stats
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18164](../findings/routes-001.md#FND-18164)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0060 — i18n_web_stats

- URL pattern (derived): `/{_locale}/stats/{username}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_stats
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0090, SRC-0751, SRC-0781, SRC-1137, SRC-1165
- Detailed finding: [FND-18165](../findings/routes-001.md#FND-18165)

```javascript
{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/stats`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{username:null,host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0061 — web_play_coach

- URL pattern (derived): `/play/coach`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_play_coach
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-0754, SRC-0781, SRC-1137, SRC-1155, SRC-1165
- Detailed finding: [FND-18166](../findings/routes-001.md#FND-18166)

```javascript
{tokens:[[`text`,`/play/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0062 — web_user_settings_coach

- URL pattern (derived): `/settings/coach`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_settings_coach
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18167](../findings/routes-001.md#FND-18167)

```javascript
{tokens:[[`text`,`/settings/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0063 — web_analysis_ceac_tab

- URL pattern (derived): `/analysis/game/{type}/{gameId}/{tab}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_analysis_ceac_tab
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1137, SRC-1155, SRC-1165
- Detailed finding: [FND-18168](../findings/routes-001.md#FND-18168)

```javascript
{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`]],defaults:{host:`www.chess-dev.com`},requirements:{type:`daily|live|master|pgn|computer|coach`,tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0064 — web_puzzles_mode

- URL pattern (derived): `/puzzles/{mode}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_puzzles_mode
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18169](../findings/routes-001.md#FND-18169)

```javascript
{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`]],defaults:{mode:``,host:`www.chess-dev.com`},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0065 — web_daily_chess_puzzle

- URL pattern (derived): `/daily`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_daily_chess_puzzle
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18170](../findings/routes-001.md#FND-18170)

```javascript
{tokens:[[`text`,`/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0066 — web_lesson_index

- URL pattern (derived): `/lessons`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_lesson_index
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18171](../findings/routes-001.md#FND-18171)

```javascript
{tokens:[[`text`,`/lessons`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0067 — web_page_learn

- URL pattern (derived): `/learn`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_page_learn
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18172](../findings/routes-001.md#FND-18172)

```javascript
{tokens:[[`text`,`/learn`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0068 — web_user_home

- URL pattern (derived): `/home`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_user_home
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-0781, SRC-1137, SRC-1155, SRC-1165
- Detailed finding: [FND-18173](../findings/routes-001.md#FND-18173)

```javascript
{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0069 — web_security_onboarding

- URL pattern (derived): `/onboarding`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_security_onboarding
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18174](../findings/routes-001.md#FND-18174)

```javascript
{tokens:[[`text`,`/onboarding`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0070 — i18n_web_play_coach

- URL pattern (derived): `/{_locale}/play/coach`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_play_coach
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-0754, SRC-0781, SRC-1137, SRC-1155, SRC-1165
- Detailed finding: [FND-18175](../findings/routes-001.md#FND-18175)

```javascript
{tokens:[[`text`,`/play/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0071 — i18n_web_analysis_ceac_tab

- URL pattern (derived): `/{_locale}/analysis/game/{type}/{gameId}/{tab}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_analysis_ceac_tab
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1137, SRC-1155, SRC-1165
- Detailed finding: [FND-18176](../findings/routes-001.md#FND-18176)

```javascript
{tokens:[[`variable`,`/`,`analysis|review|games|explorer|tablebase|collection-settings|members`,`tab`,!0],[`variable`,`/`,`[^/]++`,`gameId`,!0],[`variable`,`/`,`daily|live|master|pgn|computer|coach`,`type`,!0],[`text`,`/analysis/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{type:`daily|live|master|pgn|computer|coach`,tab:`analysis|review|games|explorer|tablebase|collection-settings|members`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0072 — i18n_web_puzzles_mode

- URL pattern (derived): `/{_locale}/puzzles/{mode}`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_puzzles_mode
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18177](../findings/routes-001.md#FND-18177)

```javascript
{tokens:[[`variable`,`/`,`rush|rated|learning|battle`,`mode`,!0],[`text`,`/puzzles`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{mode:``,host:`www.chess-dev.com`,_locale:``},requirements:{mode:`rush|rated|learning|battle`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0073 — i18n_web_daily_chess_puzzle

- URL pattern (derived): `/{_locale}/daily`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_daily_chess_puzzle
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18178](../findings/routes-001.md#FND-18178)

```javascript
{tokens:[[`text`,`/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0074 — i18n_web_lesson_index

- URL pattern (derived): `/{_locale}/lessons`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_lesson_index
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18179](../findings/routes-001.md#FND-18179)

```javascript
{tokens:[[`text`,`/lessons`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0075 — i18n_web_page_learn

- URL pattern (derived): `/{_locale}/learn`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_page_learn
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0094, SRC-0102, SRC-0144, SRC-1155
- Detailed finding: [FND-18180](../findings/routes-001.md#FND-18180)

```javascript
{tokens:[[`text`,`/learn`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0076 — web_league_callback_league_info

- URL pattern (derived): `/callback/leagues/league-info`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_league_callback_league_info
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0134
- Detailed finding: [FND-18181](../findings/routes-001.md#FND-18181)

```javascript
{tokens:[[`text`,`/callback/leagues/league-info`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0077 — i18n_web_league_callback_league_info

- URL pattern (derived): `/{_locale}/callback/leagues/league-info`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_league_callback_league_info
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0134
- Detailed finding: [FND-18182](../findings/routes-001.md#FND-18182)

```javascript
{tokens:[[`text`,`/callback/leagues/league-info`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0078 — web_policies_community

- URL pattern (derived): `/legal/community`
- Methods: not established; empty/missing route constraint
- Purpose: declared route web_policies_community
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0136, SRC-0146, SRC-0163, SRC-0175, SRC-0177, SRC-0179, SRC-0191, SRC-0192
- Detailed finding: [FND-18183](../findings/routes-001.md#FND-18183)

```javascript
{tokens:[[`text`,`/legal/community`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0079 — i18n_web_policies_community

- URL pattern (derived): `/{_locale}/legal/community`
- Methods: not established; empty/missing route constraint
- Purpose: declared route i18n_web_policies_community
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0136, SRC-0146, SRC-0163, SRC-0175, SRC-0177, SRC-0179, SRC-0191, SRC-0192
- Detailed finding: [FND-18184](../findings/routes-001.md#FND-18184)

```javascript
{tokens:[[`text`,`/legal/community`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{host:`www.chess-dev.com`,_locale:``},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}
```

## RTE-0080 — web_oauth_certificates

- URL pattern (derived): `/certs`
- Methods: GET
- Purpose: declared route web_oauth_certificates
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-0141
- Detailed finding: [FND-18185](../findings/routes-001.md#FND-18185)

```javascript
{tokens:[[`text`,`/certs`]],defaults:{host:`oauth.chess-dev.com`},requirements:{host:`(oauth)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?:oauth)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```
