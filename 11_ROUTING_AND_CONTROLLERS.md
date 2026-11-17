# Routing and controller boundaries

[Master index](00_MASTER_INDEX.md)

Each saved route record preserves its name,pattern,declaredmethods,rawdefaults,requirements and sources. Path parameters are not database keys simply because they have similar names.

New observed public mappings:

| URL | Method/status | Matched route header | Controller/handler source |
|---|---|---|---|
| https://www.chess.com/ | GET200 | web_index | Unknown |
| https://www.chess.com/jobs | GET200 | web_jobs | Unknown |

For other declared routes,no live status/auth/response/redirect is assigned unless an old preserved probe explicitly records it. Numeric method lists and optional path segments remain in the exact registry. No route-to-PHPmethodname,validationrule,service or SQLquerywasinvented.

[Complete route definitions](history/prior-audit/registries/routes.json) · [Public response evidence](audit-metadata/public-request-log.json)

