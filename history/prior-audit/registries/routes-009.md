# Declared page and route inventory

[Master index](../00_MASTER_INDEX.md)

## RTE-0321 — i18n_web_profile_view_stats

- URL pattern (derived): `/{_locale}/member/{username}/stats/{statType}`
- Methods: GET
- Purpose: declared route i18n_web_profile_view_stats
- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.
- Sources: SRC-1143, SRC-1170
- Detailed finding: [FND-18426](../findings/routes-004.md#FND-18426)

```javascript
{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,`statType`,!0],[`text`,`/stats`],[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/member`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`,`_locale`,!0]],defaults:{statType:null,host:`www.chess-dev.com`,_locale:``},requirements:{statType:`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-moves`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk|sl|tr|uk|af|ar|az|be|bs|et|fa|gl|he|hi|id|is|ka|lv|ms|pt-BR|sq|sr|vi|zh-HK|zh-TW|fil|nl-BE|bn|tk|ca|ur|--locale--`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[`GET`],schemes:[`https`]}
```
