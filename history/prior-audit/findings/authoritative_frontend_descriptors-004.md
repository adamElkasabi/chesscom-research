# authoritative_frontend_descriptors — findings 301–400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17838"></a>
## FND-17838: Full frontend descriptor: chesscom/user_properties/v1/properties_navbar.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_navbar.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "NavbarProperty",
      "field": [
        {
          "name": "pins",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "favorites",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1039,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.NavbarPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "NavbarPropertyDefinition",
      "value": [
        {
          "name": "NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "NAVBAR_PROPERTY_DEFINITION_PINS",
          "number": 1,
          "options": {}
        },
        {
          "name": "NAVBAR_PROPERTY_DEFINITION_FAVORITES",
          "number": 2,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 539721.

```text
EFHEAUaMcI+LhooVGhlIHNlY29uZCBjaGFuY2UgdGFnIGFzc2lnbmVkIHRvIGEgdXNlciAAQAAaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_navbar.proto":"CjNjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19uYXZiYXIucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSK7AQoOTmF2YmFyUHJvcGVydHkSEQoEcGlucxgBIAMoCUID+EABEhYKCWZhdm9yaXRlcxgCIAMoCUID+EACMnUKCmRlZmluaXRpb24SHS5nb29nbGUucHJvdG9idWYuRmllbGRPcHRpb25zGI8IIAEoDjI1Lm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17839"></a>
## FND-17839: Full frontend descriptor: chesscom/user_properties/v1/properties_widgets.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_widgets.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "WidgetsProperty",
      "field": [
        {
          "name": "current_widgets",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "used_widgets",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1040,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.WidgetsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "WidgetsPropertyDefinition",
      "value": [
        {
          "name": "WIDGETS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CURRENT_WIDGETS",
          "number": 1,
          "options": {}
        },
        {
          "name": "USED_WIDGETS",
          "number": 2,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 540525.

```text
5hdmJhcl9mYXZvcml0ZXMaJEEgbGlzdCBvZiBmYXZvcml0ZSBuYXZpZ2F0aW9uIGl0ZW1zLiAAGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_widgets.proto":"CjRjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc193aWRnZXRzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEiywEKD1dpZGdldHNQcm9wZXJ0eRIcCg9jdXJyZW50X3dpZGdldHMYASADKAlCA4BBARIZCgx1c2VkX3dpZGdldHMYAiADKAlCA4BBAjJ2CgpkZWZpbml0aW9uEh0uZ29vZ2xlLnByb3RvYnVmLkZpZWxkT
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17840"></a>
## FND-17840: Full frontend descriptor: chesscom/user_properties/v1/properties_league.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_league.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "LeagueProperty",
      "field": [
        {
          "name": "league_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "league_image_url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "league_is_in_the_promotion_zone",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "promotion_league_name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "promotion_league_image_url",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "leagues_definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1041,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.LeaguePropertyDefinition",
          "json_name": "leaguesDefinition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_league_name"
        },
        {
          "name": "_league_image_url"
        },
        {
          "name": "_league_is_in_the_promotion_zone"
        },
        {
          "name": "_promotion_league_name"
        },
        {
          "name": "_promotion_league_image_url"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "LeaguePropertyDefinition",
      "value": [
        {
          "name": "LEAGUE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LEAGUE_NAME",
          "number": 1,
          "options": {}
        },
        {
          "name": "LEAGUE_IMAGE_URL",
          "number": 2,
          "options": {}
        },
        {
          "name": "LEAGUE_IS_IN_THE_PROMOTION_ZONE",
          "number": 3,
          "options": {}
        },
        {
          "name": "PROMOTION_LEAGUE_NAME",
          "number": 4,
          "options": {}
        },
        {
          "name": "PROMOTION_LEAGUE_IMAGE_URL",
          "number": 5,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 541357.

```text
XQgdHlwZXMgdXNlciBoYWQgaW5zdGFsbGVkIGF0IGFueSBwb2ludCBpbiB0aGUgcGFzdCAASAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_league.proto":"CjNjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19sZWFndWUucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLvAwoOTGVhZ3VlUHJvcGVydHkSHQoLbGVhZ3VlX25hbWUYASABKAlCA4hBAUgAiAEBEiIKEGxlYWd1ZV9pbWFnZV91cmwYAiABKAlCA4hBAkgBiAEBEjEKH2xlYWd1ZV9pc19pbl90aGVfcHJvbW90aW9uX3
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17841"></a>
## FND-17841: Full frontend descriptor: chesscom/user_properties/v1/properties_puzzle_rush.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_puzzle_rush.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PuzzleRushProperty",
      "field": [
        {
          "name": "number_of_puzzle_rush_games",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "best_puzzle_rush_score",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_puzzle_rush_event_date",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1042,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PuzzleRushPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_number_of_puzzle_rush_games"
        },
        {
          "name": "_best_puzzle_rush_score"
        },
        {
          "name": "_last_puzzle_rush_event_date"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PuzzleRushPropertyDefinition",
      "value": [
        {
          "name": "PUZZLE_RUSH_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES",
          "number": 1,
          "options": {}
        },
        {
          "name": "PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE",
          "number": 2,
          "options": {}
        },
        {
          "name": "PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE",
          "number": 3,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 542784.

```text
2YgdGhlIGxlYWd1ZSB3aGVyZSB0aGUgcGxheWVyIHdvdWxkIGJlIHByb21vdGVkIGltYWdlIAAaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_puzzle_rush.proto":"CjhjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19wdXp6bGVfcnVzaC5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIpcDChJQdXp6bGVSdXNoUHJvcGVydHkSLQobbnVtYmVyX29mX3B1enpsZV9ydXNoX2dhbWVzGAEgASgFQgOQQQFIAIgBARIoChZiZXN0X3B1enpsZV9ydXNoX3Njb3JlGAIgASgFQgOQQQJIA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17842"></a>
## FND-17842: Full frontend descriptor: chesscom/user_properties/v1/properties_monthly_bot_event.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_monthly_bot_event.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "MonthlyBotEventProperty",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "points",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "milestones_achieved",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "last_progression_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1043,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_key"
        },
        {
          "name": "_points"
        },
        {
          "name": "_milestones_achieved"
        },
        {
          "name": "_last_progression_at"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "MonthlyBotEventPropertyDefinition",
      "value": [
        {
          "name": "MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY",
          "number": 1,
          "options": {}
        },
        {
          "name": "MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS",
          "number": 2,
          "options": {}
        },
        {
          "name": "MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED",
          "number": 3,
          "options": {}
        },
        {
          "name": "MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT",
          "number": 4,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 544017.

```text
BQdXp6bGUgUnVzaCAoZm9yIGFjdGl2YXRpb24gLyBoaXN0b3JpYyBkYXRhIGV4aXN0cykgAEgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_monthly_bot_event.proto":"Cj5jaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19tb250aGx5X2JvdF9ldmVudC5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIoADChdNb250aGx5Qm90RXZlbnRQcm9wZXJ0eRIVCgNrZXkYASABKAlCA5hBAUgAiAEBEhgKBnBvaW50cxgCIAEoBUIDmEECSAGIAQESJQoTbWlsZXN0b25lc19hY2hpZXZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17843"></a>
## FND-17843: Full frontend descriptor: chesscom/user_properties/v1/properties_predictive.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_predictive.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PredictiveProperty",
      "field": [
        {
          "name": "churn_risk_30d",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "predictive_scores_updated_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "churn_risk_30d_generated_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "churn_risk_30d_model_version",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "activation_7d",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "puzzle_slump_7d",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "lessons_progression_7d",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "review_upsell_30d",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "return_7d",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "trial_start_7d",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "trial_conversion_30d",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "subscription_conversion_30d",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "annual_renewal_365d",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "nurr_7d",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "curr_14d",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "lesson_adoption_30d",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "reactivation_7d",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "trial_propensity_score",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1008,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PredictivePropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_churn_risk_30d"
        },
        {
          "name": "_predictive_scores_updated_at"
        },
        {
          "name": "_churn_risk_30d_generated_at"
        },
        {
          "name": "_churn_risk_30d_model_version"
        },
        {
          "name": "_activation_7d"
        },
        {
          "name": "_puzzle_slump_7d"
        },
        {
          "name": "_lessons_progression_7d"
        },
        {
          "name": "_review_upsell_30d"
        },
        {
          "name": "_return_7d"
        },
        {
          "name": "_trial_start_7d"
        },
        {
          "name": "_trial_conversion_30d"
        },
        {
          "name": "_subscription_conversion_30d"
        },
        {
          "name": "_annual_renewal_365d"
        },
        {
          "name": "_nurr_7d"
        },
        {
          "name": "_curr_14d"
        },
        {
          "name": "_lesson_adoption_30d"
        },
        {
          "name": "_reactivation_7d"
        },
        {
          "name": "_trial_propensity_score"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PredictivePropertyDefinition",
      "value": [
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D",
          "number": 1,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT",
          "number": 2,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT",
          "number": 3,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION",
          "number": 4,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D",
          "number": 5,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D",
          "number": 6,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D",
          "number": 7,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D",
          "number": 8,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D",
          "number": 9,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D",
          "number": 10,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D",
          "number": 11,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D",
          "number": 12,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D",
          "number": 13,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_NURR_7D",
          "number": 14,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_CURR_14D",
          "number": 15,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D",
          "number": 16,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D",
          "number": 17,
          "options": {}
        },
        {
          "name": "PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE",
          "number": 18,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 545947.

```text
HByb2dyZXNzaW9uIHVwZGF0ZSBpbiB0aGUgY3VycmVudCBNb250aGx5IEJvdCBFdmVudCAASAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_predictive.proto":"CjdjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19wcmVkaWN0aXZlLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEimgoKElByZWRpY3RpdmVQcm9wZXJ0eRIgCg5jaHVybl9yaXNrXzMwZBgBIAEoAUIDgD8BSACIAQESSgoccHJlZGljdGl2ZV9zY29yZXNfdXBkYXRlZF9hdBgCIAEoCzIaLmdvb2dsZS5wcm90b2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17844"></a>
## FND-17844: Full frontend descriptor: chesscom/user_properties/v1/properties_growth.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_growth.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "GrowthProperty",
      "field": [
        {
          "name": "momentum_state",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "momentum_prior_state",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "momentum_computed_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1009,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.GrowthPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_momentum_state"
        },
        {
          "name": "_momentum_prior_state"
        },
        {
          "name": "_momentum_computed_at"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "GrowthPropertyDefinition",
      "value": [
        {
          "name": "GROWTH_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE",
          "number": 1,
          "options": {}
        },
        {
          "name": "GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE",
          "number": 2,
          "options": {}
        },
        {
          "name": "GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT",
          "number": 3,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 551903.

```text
FseXRpY3MudHBfdjVfdXNlcl9zY29yZXNfbGF0ZXN0LiBTb3VyY2U6IERBVEEtMzk3OS4gAEgBGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_growth.proto":"CjNjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19ncm93dGgucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLjAgoOR3Jvd3RoUHJvcGVydHkSIAoObW9tZW50dW1fc3RhdGUYASABKAlCA4g/AUgAiAEBEiYKFG1vbWVudHVtX3ByaW9yX3N0YXRlGAIgASgJQgOIPwJIAYgBARJCChRtb21lbnR1bV9jb21wdXRlZF9hdB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17845"></a>
## FND-17845: Full frontend descriptor: chesscom/user_properties/v1/properties_skills.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_skills.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "SkillsProperty",
      "field": [
        {
          "name": "unlocked_skills",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "mastered_skills",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1044,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SkillsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "SkillsPropertyDefinition",
      "value": [
        {
          "name": "SKILLS_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS",
          "number": 1,
          "options": {}
        },
        {
          "name": "SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS",
          "number": 2,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 553242.

```text
29tcHV0ZWRfYXQaKVRpbWVzdGFtcCB3aGVuIG1vbWVudHVtIHdhcyBsYXN0IGNvbXB1dGVkSAEaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_skills.proto":"CjNjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19za2lsbHMucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLMAQoOU2tpbGxzUHJvcGVydHkSHAoPdW5sb2NrZWRfc2tpbGxzGAEgAygJQgOgQQESHAoPbWFzdGVyZWRfc2tpbGxzGAIgAygJQgOgQQIydQoKZGVmaW5pdGlvbhIdLmdvb2dsZS5wcm90b2J1Zi5GaWVsZE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17846"></a>
## FND-17846: Full frontend descriptor: chesscom/user_properties/v1/properties_opening_courses.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_opening_courses.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "OpeningCoursesProperty",
      "field": [
        {
          "name": "first_opening_courses_session_date",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_opening_courses_session_date",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_opening_courses_study_date",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_variations_learned",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_variations_reviewed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_reviews_pending",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_started",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_completed",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_feature_limit_hits",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "number_of_opening_courses_previews_claimed",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1045,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.OpeningCoursesPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_first_opening_courses_session_date"
        },
        {
          "name": "_last_opening_courses_session_date"
        },
        {
          "name": "_last_opening_courses_study_date"
        },
        {
          "name": "_number_of_opening_courses_variations_learned"
        },
        {
          "name": "_number_of_opening_courses_variations_reviewed"
        },
        {
          "name": "_number_of_opening_courses_reviews_pending"
        },
        {
          "name": "_number_of_opening_courses_started"
        },
        {
          "name": "_number_of_opening_courses_completed"
        },
        {
          "name": "_number_of_opening_courses_feature_limit_hits"
        },
        {
          "name": "_number_of_opening_courses_previews_claimed"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "OpeningCoursesPropertyDefinition",
      "value": [
        {
          "name": "OPENING_COURSES_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FIRST_OPENING_COURSES_SESSION_DATE",
          "number": 1,
          "options": {}
        },
        {
          "name": "LAST_OPENING_COURSES_SESSION_DATE",
          "number": 2,
          "options": {}
        },
        {
          "name": "LAST_OPENING_COURSES_STUDY_DATE",
          "number": 3,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED",
          "number": 4,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED",
          "number": 5,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING",
          "number": 6,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_STARTED",
          "number": 7,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_COMPLETED",
          "number": 8,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS",
          "number": 9,
          "options": {}
        },
        {
          "name": "NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED",
          "number": 10,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 554135.

```text
scxowTnVtZXJpYyBTa2lsbCBlbnVtIGNvZGVzIHRoZSBwbGF5ZXIgaGFzIG1hc3RlcmVkIABIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_opening_courses.proto":"CjxjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19vcGVuaW5nX2NvdXJzZXMucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLqCQoWT3BlbmluZ0NvdXJzZXNQcm9wZXJ0eRJQCiJmaXJzdF9vcGVuaW5nX2NvdXJzZXNfc2Vzc2lvbl9kYXRlGAEgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEIDq
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17847"></a>
## FND-17847: Full frontend descriptor: chesscom/settings/v1/settings_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_metadata.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "SettingMetadata",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.settings.v1.SettingMetadata.Type"
        },
        {
          "name": "default_value",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue"
        },
        {
          "name": "allowed_values",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue"
        },
        {
          "name": "validators",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingMetadata.Validator"
        },
        {
          "name": "allow_null_values",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "nested_type": [
        {
          "name": "Validator",
          "field": [
            {
              "name": "range",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingMetadata.Validator.RangeValidator",
              "oneof_index": 0
            },
            {
              "name": "not_blank",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator",
              "oneof_index": 0
            },
            {
              "name": "length",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingMetadata.Validator.LengthValidator",
              "oneof_index": 0
            },
            {
              "name": "regex",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingMetadata.Validator.RegexValidator",
              "oneof_index": 0
            }
          ],
          "nested_type": [
            {
              "name": "RangeValidator",
              "field": [
                {
                  "name": "min",
                  "number": 1,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_INT32",
                  "oneof_index": 0,
                  "proto3_optional": true
                },
                {
                  "name": "max",
                  "number": 2,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_INT32",
                  "oneof_index": 1,
                  "proto3_optional": true
                }
              ],
              "oneof_decl": [
                {
                  "name": "_min"
                },
                {
                  "name": "_max"
                }
              ]
            },
            {
              "name": "NotBlankValidator"
            },
            {
              "name": "LengthValidator",
              "field": [
                {
                  "name": "min",
                  "number": 1,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_INT32",
                  "oneof_index": 0,
                  "proto3_optional": true
                },
                {
                  "name": "max",
                  "number": 2,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_INT32",
                  "oneof_index": 1,
                  "proto3_optional": true
                }
              ],
              "oneof_decl": [
                {
                  "name": "_min"
                },
                {
                  "name": "_max"
                }
              ]
            },
            {
              "name": "RegexValidator",
              "field": [
                {
                  "name": "pattern",
                  "number": 1,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ]
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        }
      ],
      "enum_type": [
        {
          "name": "Type",
          "value": [
            {
              "name": "TYPE_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "TYPE_BOOLEAN",
              "number": 1
            },
            {
              "name": "TYPE_STRING",
              "number": 2
            },
            {
              "name": "TYPE_INTEGER",
              "number": 3
            },
            {
              "name": "TYPE_LONG",
              "number": 4
            },
            {
              "name": "TYPE_DOUBLE",
              "number": 5
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_allow_null_values"
        }
      ]
    },
    {
      "name": "SettingValue",
      "field": [
        {
          "name": "boolean",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "oneof_index": 0
        },
        {
          "name": "string",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "oneof_index": 0
        },
        {
          "name": "integer",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Integer",
          "oneof_index": 0
        },
        {
          "name": "long",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Long",
          "oneof_index": 0
        },
        {
          "name": "double",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Double",
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "Boolean",
          "field": [
            {
              "name": "value",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL",
              "oneof_index": 0
            },
            {
              "name": "null",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Empty",
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "wrapped_value"
            }
          ]
        },
        {
          "name": "String",
          "field": [
            {
              "name": "value",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING",
              "oneof_index": 0
            },
            {
              "name": "null",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Empty",
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "wrapped_value"
            }
          ]
        },
        {
          "name": "Integer",
          "field": [
            {
              "name": "value",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32",
              "oneof_index": 0
            },
            {
              "name": "null",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Empty",
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "wrapped_value"
            }
          ]
        },
        {
          "name": "Long",
          "field": [
            {
              "name": "value",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT64",
              "oneof_index": 0
            },
            {
              "name": "null",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Empty",
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "wrapped_value"
            }
          ]
        },
        {
          "name": "Double",
          "field": [
            {
              "name": "value",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_DOUBLE",
              "oneof_index": 0
            },
            {
              "name": "null",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Empty",
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "wrapped_value"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "setting_metadata",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 1100,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.settings.v1.SettingMetadata",
      "json_name": "settingMetadata"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 557671.

```text
iBvZiBvcGVuaW5nIGNvdXJzZXMgdGhlIHVzZXIgaGFzIGluIGEgcHJldmlldyBzdGF0ZSAASAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/settings/v1/settings_metadata.proto":"CixjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19tZXRhZGF0YS5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEikQgKD1NldHRpbmdNZXRhZGF0YRIKCgJpZBgBIAEoCRIMCgRuYW1lGAIgASgJEhMKC2Rlc2NyaXB0aW9uGAMgASgJEjgKBHR5cGUYBCABKA4yKi5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nTWV0YWRhdGEuVHlwZRI5Cg1kZWZhdWx0X
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17848"></a>
## FND-17848: Full frontend descriptor: chesscom/settings/v1/settings_board.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_board.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "BoardSetting",
      "field": [
        {
          "name": "coordinates",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "move_list_style",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "animation_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "win_celebration",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "move_method",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "highlight_moves",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "white_always_on_bottom",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_sounds",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_legal_moves",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_animations",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "board_style",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "pieces_style",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "sound_theme",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "castling_type",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "move_classification_style",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "game_result_animations",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "game_over_screen",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 560380.

```text
5zGMwIIAEoCzIlLmNoZXNzY29tLnNldHRpbmdzLnYxLlNldHRpbmdNZXRhZGF0YVIPc2V0dGluZ01ldGFkYXRhYgZwcm90bzM","chesscom/settings/v1/settings_board.proto":"CiljaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19ib2FyZC5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEiliIKDEJvYXJkU2V0dGluZxLYAQoLY29vcmRpbmF0ZXMYASABKAsyKS5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nVmFsdWUuU3RyaW5nQpUB4kSRAQoRYm9hcmQuY29vcmRpbmF0ZXMSEUJvYXJkIENvb3JkaW5hdGVzGihXaGV0aGVyIGFuZCB3
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17849"></a>
## FND-17849: Full frontend descriptor: chesscom/settings/v1/settings_gameplay.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_gameplay.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "GameplaySetting",
      "field": [
        {
          "name": "confirm_resign",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "focus_mode",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "auto_analysis",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_challenges_from",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_game_chat_with",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "challenge_min_rating",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Integer",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "challenge_max_rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Integer",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "seek_min_rating",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Integer",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "seek_max_rating",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Integer",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "seek_game_type",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_timestamps",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "friends_can_challenge_me_no_matter_what",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_streaks",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_membership_badges",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "live",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.GameplaySetting.GameplayLiveSetting",
          "oneof_index": 0
        },
        {
          "name": "daily",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.GameplaySetting.GameplayDailySetting",
          "oneof_index": 0
        },
        {
          "name": "analysis",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting",
          "oneof_index": 0
        },
        {
          "name": "show_my_membership_badge",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_player_flair",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "seek_time_class",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "voice_move",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "auto_save_bot_games",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "GameplayLiveSetting",
          "field": [
            {
              "name": "premoves",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "auto_promote_queen",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "play_multiple_games",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "auto_switch_game",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "auto_watch_top_game",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "low_time_warning",
              "number": 6,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "engine_evaluation",
              "number": 7,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "evaluation_bar",
              "number": 8,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "allow_offline_challenges",
              "number": 9,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "allow_chat_requests_from",
              "number": 10,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.String",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "challenge_alerts",
              "number": 11,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.String",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "friends_alerts",
              "number": 12,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.String",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "event_announcements",
              "number": 13,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.String",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "right_button_arrows",
              "number": 14,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_is_rated",
              "number": 15,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_base_time_chess",
              "number": 16,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_increment_chess",
              "number": 17,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_base_time_variants",
              "number": 18,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_increment_variants",
              "number": 19,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_filter_hide_variants",
              "number": 20,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_filter_premium_only",
              "number": 21,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_filter_rated_only",
              "number": 22,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "hide_ratings_during_the_game",
              "number": 23,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_time_class",
              "number": 24,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.String",
              "options": {
                "deprecated": true
              },
              "oneof_index": 0
            },
            {
              "name": "confirm_move",
              "number": 25,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        },
        {
          "name": "GameplayDailySetting",
          "field": [
            {
              "name": "after_moving",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.String",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "confirm_move",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "auto_win_on_time",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "max_game_count",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "min_days_per_move",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "max_days_per_move",
              "number": 6,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "seek_days_per_move",
              "number": 7,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Integer",
              "options": {},
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        },
        {
          "name": "GameplayAnalysisSetting",
          "field": [
            {
              "name": "evaluation_bar_mode",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode",
              "oneof_index": 0
            }
          ],
          "nested_type": [
            {
              "name": "EvaluationBarMode",
              "field": [
                {
                  "name": "wdl_for_openings",
                  "number": 1,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_MESSAGE",
                  "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
                  "options": {},
                  "oneof_index": 0
                },
                {
                  "name": "tablebase_in_endgame",
                  "number": 2,
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_MESSAGE",
                  "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
                  "options": {},
                  "oneof_index": 0
                }
              ],
              "oneof_decl": [
                {
                  "name": "value"
                }
              ]
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 566361.

```text
g0KC2Z1bGxfc2NyZWVuMg8SDQoLZnVsbF9zY3JlZW4yCxIJCgdjbGFzc2ljSAA6B4KmHQMKAQFCBwoFdmFsdWViBnByb3RvMw","chesscom/settings/v1/settings_gameplay.proto":"CixjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19nYW1lcGxheS5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEislgKD0dhbWVwbGF5U2V0dGluZxKTAQoOY29uZmlybV9yZXNpZ24YASABKAsyKi5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nVmFsdWUuQm9vbGVhbkJN4kRKChdnYW1lcGxheS5jb25maXJtX3Jlc2lnbhIXR2FtZXBsYXkgQ29uZmlyb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17850"></a>
## FND-17850: Full frontend descriptor: chesscom/settings/v1/settings_home.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_home.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "HomeSetting",
      "field": [
        {
          "name": "recommended_games",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_recommended_activities",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_chess_tv",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_daily_puzzle",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "default_tab",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 581602.

```text
FibGViYXNlIGluIGVuZGdhbWUgASoECgIIAUgAQgcKBXZhbHVlQgcKBXZhbHVlOgeCph0DCgEBQgcKBXZhbHVlYgZwcm90bzM","chesscom/settings/v1/settings_home.proto":"CihjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19ob21lLnByb3RvEhRjaGVzc2NvbS5zZXR0aW5ncy52MSLvBgoLSG9tZVNldHRpbmcSoAEKEXJlY29tbWVuZGVkX2dhbWVzGAEgASgLMiouY2hlc3Njb20uc2V0dGluZ3MudjEuU2V0dGluZ1ZhbHVlLkJvb2xlYW5CV+JEVAoWaG9tZS5yZWNvbW1lbmRlZF9nYW1lcxIYU2hvdyBSZWNvbW1lbmRlZCBNYXRjaGVzG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17851"></a>
## FND-17851: Full frontend descriptor: chesscom/settings/v1/settings_learn.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_learn.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "LearnSetting",
      "field": [
        {
          "name": "coach",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "coach_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "coach_nudge",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "enable_coach_voice",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "coach_voice_speed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Double",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "enable_coach",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "enable_motivational",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_coach_avatar_game_review",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "lesson_view",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "auto_save_coach_games",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "skills_enabled",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "coach_evaluation_bar",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "coach_suggestion_arrows",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "coach_threat_arrows",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "teach_legal_moves",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 582920.

```text
pdHlfZmVlZDIREg8KDWFjdGl2aXR5X2ZlZWQyEBIOCgxnYW1lX2hpc3RvcnlIADoHgqYdAwoBAUIHCgV2YWx1ZWIGcHJvdG8z","chesscom/settings/v1/settings_learn.proto":"CiljaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19sZWFybi5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEijhcKDExlYXJuU2V0dGluZxKpAgoFY29hY2gYASABKAsyKS5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nVmFsdWUuU3RyaW5nQuwBGAHiROYBCgtsZWFybi5jb2FjaBILTGVhcm4gQ29hY2gaZE5hbWUgb2YgdGhlIGNvYWNoIHRvIGJlIHVzZWQg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17852"></a>
## FND-17852: Full frontend descriptor: chesscom/settings/v1/settings_notification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_notification.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "NotificationSetting",
      "field": [
        {
          "name": "auto_track_content",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "web",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.NotificationSetting.NotificationWebSetting",
          "oneof_index": 0
        },
        {
          "name": "mobile",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.NotificationSetting.NotificationMobileSetting",
          "oneof_index": 0
        },
        {
          "name": "email",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.NotificationSetting.NotificationEmailSetting",
          "oneof_index": 0
        },
        {
          "name": "show_internal_ads",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "NotificationWebSetting",
          "field": [
            {
              "name": "my_turn_to_move",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "game_event",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_message",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_friend_request",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_social_trophy",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_user_comment",
              "number": 6,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_content",
              "number": 7,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_comment",
              "number": 8,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "hero_playing",
              "number": 9,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "chess_tv",
              "number": 10,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "lesson_quota",
              "number": 11,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "vote_chess",
              "number": 12,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "news_and_announcements",
              "number": 13,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "lesson_and_practice",
              "number": 14,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "friend_activity_updates",
              "number": 15,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "streaks_reminders",
              "number": 16,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "leagues_reminders",
              "number": 17,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "contact_match",
              "number": 18,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "puzzle_reminders",
              "number": 19,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "game_review_reminders",
              "number": 20,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "coach_reminders",
              "number": 21,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "special_offers",
              "number": 23,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "courses_reminders",
              "number": 24,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "community_updates",
              "number": 25,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        },
        {
          "name": "NotificationMobileSetting",
          "field": [
            {
              "name": "my_turn_to_move",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "game_event",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_message",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_friend_request",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_social_trophy",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_user_comment",
              "number": 6,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_content",
              "number": 7,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_comment",
              "number": 8,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "hero_playing",
              "number": 9,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "chess_tv",
              "number": 10,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "lesson_quota",
              "number": 11,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "vote_chess",
              "number": 12,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "news_and_announcements",
              "number": 13,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "lesson_and_practice",
              "number": 14,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "friend_activity_updates",
              "number": 15,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "recommended_match",
              "number": 16,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "puzzle_reminder",
              "number": 17,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "streaks_reminders",
              "number": 18,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "leagues_reminders",
              "number": 19,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "contact_match",
              "number": 20,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "game_review_reminders",
              "number": 21,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "coach_reminders",
              "number": 22,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "special_offers",
              "number": 23,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "courses_reminders",
              "number": 24,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "community_updates",
              "number": 25,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        },
        {
          "name": "NotificationEmailSetting",
          "field": [
            {
              "name": "my_turn_to_move",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "game_event",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_message",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_friend_request",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_social_trophy",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_user_comment",
              "number": 6,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_content",
              "number": 7,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "new_comment",
              "number": 8,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "hero_playing",
              "number": 9,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "chess_tv",
              "number": 10,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "lesson_quota",
              "number": 11,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "vote_chess",
              "number": 12,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "news_and_announcements",
              "number": 13,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "lesson_and_practice",
              "number": 14,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "friend_activity_updates",
              "number": 15,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "puzzle_reminder",
              "number": 16,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "streaks_reminders",
              "number": 17,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "leagues_reminders",
              "number": 18,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "contact_match",
              "number": 19,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "game_review_reminders",
              "number": 21,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "coach_reminders",
              "number": 22,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "special_offers",
              "number": 23,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "courses_reminders",
              "number": 24,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            },
            {
              "name": "community_updates",
              "number": 25,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
              "options": {},
              "oneof_index": 0
            }
          ],
          "oneof_decl": [
            {
              "name": "value"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 587013.

```text
yB3aHkgYW4gYXR0ZW1wdGVkIG1vdmUgaXMgaWxsZWdhbC4gASoECgISAEABSAA6B4KmHQMKAQFCBwoFdmFsdWViBnByb3RvMw","chesscom/settings/v1/settings_notification.proto":"CjBjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19ub3RpZmljYXRpb24ucHJvdG8SFGNoZXNzY29tLnNldHRpbmdzLnYxIr51ChNOb3RpZmljYXRpb25TZXR0aW5nEtQBChJhdXRvX3RyYWNrX2NvbnRlbnQYASABKAsyKi5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nVmFsdWUuQm9vbGVhbkKJAeJEhQEKH25vdGlmaWNhdGlvbi5hdXRvX3RyYWNrX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17853"></a>
## FND-17853: Full frontend descriptor: chesscom/settings/v1/settings_privacy.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_privacy.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "PrivacySetting",
      "field": [
        {
          "name": "allow_global_chat_requests_from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "messages_privacy",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "notes_privacy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "blog_privacy",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "friends_list_privacy",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "insights_privacy",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_friend_requests",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_club_invitations",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_tournament_invitations",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "safe_mode",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_contact_matching",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "suspicious_login_protection_otvc",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "allow_classroom_invitations",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 607229.

```text
xoZQ29tbXVuaXR5IFVwZGF0ZXMgKGVtYWlsKSABKgQKAggBSABCBwoFdmFsdWU6B4KmHQMKAQFCBwoFdmFsdWViBnByb3RvMw","chesscom/settings/v1/settings_privacy.proto":"CitjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19wcml2YWN5LnByb3RvEhRjaGVzc2NvbS5zZXR0aW5ncy52MSLpFgoOUHJpdmFjeVNldHRpbmcSwQIKH2FsbG93X2dsb2JhbF9jaGF0X3JlcXVlc3RzX2Zyb20YASABKAsyKS5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nVmFsdWUuU3RyaW5nQuoB4kTmAQoncHJpdmFjeS5hbGxvd19nbG9iYWxfY2hhdF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17854"></a>
## FND-17854: Full frontend descriptor: chesscom/settings/v1/settings_puzzle.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_puzzle.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "PuzzleSetting",
      "field": [
        {
          "name": "show_details",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_timer",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_classic_mode",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_chat_hints",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_mistake_feedback",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_puzzle_goals",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "collect_puzzle_points",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "always_show_rating",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "difficulty_mode",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_hints_automatically",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "daily_puzzle_hard_mode",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 611277.

```text
5hYmxlIC8gZGlzYWJsZSBjbGFzc3Jvb20gaW52aXRhdGlvbnMgASoECgIIAUgAOgeCph0DCgEBQgcKBXZhbHVlYgZwcm90bzM","chesscom/settings/v1/settings_puzzle.proto":"CipjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19wdXp6bGUucHJvdG8SFGNoZXNzY29tLnNldHRpbmdzLnYxItYPCg1QdXp6bGVTZXR0aW5nEswBCgxzaG93X2RldGFpbHMYASABKAsyKS5jaGVzc2NvbS5zZXR0aW5ncy52MS5TZXR0aW5nVmFsdWUuU3RyaW5nQogB4kSEAQoUcHV6emxlcy5zaG93X2RldGFpbHMSFFB1enpsZXMgU2hvdyBEZXRhaWxzGiZXaGV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17855"></a>
## FND-17855: Full frontend descriptor: chesscom/settings/v1/settings_toaster_center.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_toaster_center.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "ToasterCenterSetting",
      "field": [
        {
          "name": "show_club_request_toasters",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_friend_request_toasters",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "automatically_expand_toasters",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "show_tournament_reminder_toasters",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_move_made_toasters",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "show_toasters",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 614103.

```text
RoiUGxheSB0aGUgRGFpbHkgUHV6emxlIGluIGhhcmQgbW9kZSABKgQKAggASAA6B4KmHQMKAQFCBwoFdmFsdWViBnByb3RvMw","chesscom/settings/v1/settings_toaster_center.proto":"CjJjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc190b2FzdGVyX2NlbnRlci5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEiqQoKFFRvYXN0ZXJDZW50ZXJTZXR0aW5nEs8BChpzaG93X2NsdWJfcmVxdWVzdF90b2FzdGVycxgBIAEoCzIqLmNoZXNzY29tLnNldHRpbmdzLnYxLlNldHRpbmdWYWx1ZS5Cb29sZWFuQn3iRHoKKXRvYXN0ZXJfY2VudGV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17856"></a>
## FND-17856: Full frontend descriptor: chesscom/settings/v1/settings_ui.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_ui.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "UiSetting",
      "field": [
        {
          "name": "mode",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.String",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "enable_special_theme_forcing",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 616034.

```text
N0ZXJzGh5TaG93IGFsbCB0b2FzdGVyIG5vdGlmaWNhdGlvbnMgASoECgIIAUgAOgeCph0DCgEBQgcKBXZhbHVlYgZwcm90bzM","chesscom/settings/v1/settings_ui.proto":"CiZjaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc191aS5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEirwMKCVVpU2V0dGluZxKtAQoEbW9kZRgBIAEoCzIpLmNoZXNzY29tLnNldHRpbmdzLnYxLlNldHRpbmdWYWx1ZS5TdHJpbmdCcuJEbwoHdWkubW9kZRIHVWkgTW9kZRo6VUkgbW9kZSB1c2VkIGluIHRoZSBlbnRpcmUgc3lzdGVtLCBmb3IgZGlzcGxheWluZyB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17857"></a>
## FND-17857: Full frontend descriptor: chesscom/settings/v1/settings_watch.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_watch.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "WatchSetting",
      "field": [
        {
          "name": "advanced_engine_settings",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "player_names_above_and_below",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.SettingValue.Boolean",
          "options": {},
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 616750.

```text
0aGVtZXMgYXNzb2NpYXRlZCB3aXRoIHNwZWNpYWwgZXZlbnRzIAEqBAoCCAFIADoHgqYdAwoBAUIHCgV2YWx1ZWIGcHJvdG8z","chesscom/settings/v1/settings_watch.proto":"CiljaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc193YXRjaC5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEi3QMKDFdhdGNoU2V0dGluZxLHAQoYYWR2YW5jZWRfZW5naW5lX3NldHRpbmdzGAEgASgLMiouY2hlc3Njb20uc2V0dGluZ3MudjEuU2V0dGluZ1ZhbHVlLkJvb2xlYW5Cd+JEdAoed2F0Y2guYWR2YW5jZWRfZW5naW5lX3NldHRpbmdzEh5XYXRjaCBB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17858"></a>
## FND-17858: Full frontend descriptor: chesscom/settings/v1/settings_model.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/settings/v1/settings_model.proto",
  "package": "chesscom.settings.v1",
  "message_type": [
    {
      "name": "Setting",
      "field": [
        {
          "name": "gameplay",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.GameplaySetting",
          "oneof_index": 0
        },
        {
          "name": "notification",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.NotificationSetting",
          "oneof_index": 0
        },
        {
          "name": "privacy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.PrivacySetting",
          "oneof_index": 0
        },
        {
          "name": "board",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.BoardSetting",
          "oneof_index": 0
        },
        {
          "name": "puzzle",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.PuzzleSetting",
          "oneof_index": 0
        },
        {
          "name": "learn",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.LearnSetting",
          "oneof_index": 0
        },
        {
          "name": "ui",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.UiSetting",
          "oneof_index": 0
        },
        {
          "name": "toaster_center",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.ToasterCenterSetting",
          "oneof_index": 0
        },
        {
          "name": "home",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.HomeSetting",
          "oneof_index": 0
        },
        {
          "name": "watch",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.WatchSetting",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 617535.

```text
G93IGJvYXJkIGluIC9ldmVudHMgc2luZ2xlIGdhbWUgdmlldyABKgQKAggASAA6B4KmHQMKAQFCBwoFdmFsdWViBnByb3RvMw","chesscom/settings/v1/settings_model.proto":"CiljaGVzc2NvbS9zZXR0aW5ncy92MS9zZXR0aW5nc19tb2RlbC5wcm90bxIUY2hlc3Njb20uc2V0dGluZ3MudjEi0AQKB1NldHRpbmcSOQoIZ2FtZXBsYXkYASABKAsyJS5jaGVzc2NvbS5zZXR0aW5ncy52MS5HYW1lcGxheVNldHRpbmdIABJBCgxub3RpZmljYXRpb24YAiABKAsyKS5jaGVzc2NvbS5zZXR0aW5ncy52MS5Ob3RpZmljYXRpb25TZXR0aW5nSAASNwoH
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17859"></a>
## FND-17859: Full frontend descriptor: chesscom/user_properties/v1/properties.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PropertiesByUser",
      "field": [
        {
          "name": "user",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "properties",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.Properties"
        },
        {
          "name": "time_windows_properties",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TimeWindowsPropertiesData",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_time_windows_properties"
        }
      ]
    },
    {
      "name": "Properties",
      "field": [
        {
          "name": "core",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.CoreProperty",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "pii",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PIIProperty",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "user_details",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.UserDetailsProperty",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "roles",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.RolesProperty",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "activity",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.ActivityProperty",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "subscription",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.SubscriptionProperty",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "attribution_signup_initial",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AttributionProperty",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "attribution_signup_last",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AttributionProperty",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "attribution_trial_initial",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AttributionProperty",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "attribution_trial_last",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AttributionProperty",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "ratings",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.RatingsProperty",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "wdl",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.WDLProperty",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "analysis",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AnalysisProperty",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "settings_daily_chess",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.SettingsDailyChessProperty",
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "settings_live_chess",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.SettingsLiveChessProperty",
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "stats_daily_chess",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsDailyProperty",
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "stats_daily_chess960",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsDailyChess960Property",
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "stats_live_chess_bullet",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "stats_live_chess_blitz",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "stats_live_chess_rapid",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "stats_live_chess960_bullet",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "stats_live_chess960_blitz",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "stats_live_chess960_rapid",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "stats_live_bughouse",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.StatsLiveProperty",
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "user_settings",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.UserSettingsProperty",
          "options": {
            "deprecated": true
          },
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "puzzles_attempted",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PuzzlesAttemptedProperty",
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "clubs",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.ClubsProperty",
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "puzzle_battle",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PuzzleBattleProperty",
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "audiences",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AudiencesProperty",
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "user_abuse",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.UserAbuseProperty",
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "settings",
          "number": 31,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.Setting"
        },
        {
          "name": "daily_puzzles_solved",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.DailyPuzzlesSolvedProperty",
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_chess",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_chess960",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_bughouse",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_threecheck",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_crazyhouse",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_kingofthehill",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "play_bullet_oddschess",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_chess",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_chess960",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_bughouse",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_threecheck",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_crazyhouse",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_kingofthehill",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 43,
          "proto3_optional": true
        },
        {
          "name": "play_blitz_oddschess",
          "number": 46,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 44,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_chess",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 45,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_chess960",
          "number": 48,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 46,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_bughouse",
          "number": 49,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 47,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_threecheck",
          "number": 50,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 48,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_crazyhouse",
          "number": 51,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 49,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_kingofthehill",
          "number": 52,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 50,
          "proto3_optional": true
        },
        {
          "name": "play_rapid_oddschess",
          "number": 53,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 51,
          "proto3_optional": true
        },
        {
          "name": "play_daily_chess",
          "number": 54,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 52,
          "proto3_optional": true
        },
        {
          "name": "play_daily_chess960",
          "number": 55,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 53,
          "proto3_optional": true
        },
        {
          "name": "play_daily_oddschess",
          "number": 56,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PlayStatsProperty",
          "oneof_index": 54,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_chess",
          "number": 57,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 55,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_chess960",
          "number": 58,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 56,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_bughouse",
          "number": 59,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 57,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_threecheck",
          "number": 60,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 58,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_crazyhouse",
          "number": 61,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 59,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_kingofthehill",
          "number": 62,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 60,
          "proto3_optional": true
        },
        {
          "name": "tournament_bullet_oddschess",
          "number": 63,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 61,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_chess",
          "number": 64,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 62,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_chess960",
          "number": 65,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 63,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_bughouse",
          "number": 66,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 64,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_threecheck",
          "number": 67,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 65,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_crazyhouse",
          "number": 68,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 66,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_kingofthehill",
          "number": 69,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 67,
          "proto3_optional": true
        },
        {
          "name": "tournament_blitz_oddschess",
          "number": 70,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 68,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_chess",
          "number": 71,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 69,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_chess960",
          "number": 72,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 70,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_bughouse",
          "number": 73,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 71,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_threecheck",
          "number": 74,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 72,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_crazyhouse",
          "number": 75,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 73,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_kingofthehill",
          "number": 76,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 74,
          "proto3_optional": true
        },
        {
          "name": "tournament_rapid_oddschess",
          "number": 77,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 75,
          "proto3_optional": true
        },
        {
          "name": "tournament_daily_chess",
          "number": 78,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 76,
          "proto3_optional": true
        },
        {
          "name": "tournament_daily_chess960",
          "number": 79,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 77,
          "proto3_optional": true
        },
        {
          "name": "tournament_daily_oddschess",
          "number": 80,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsProperty",
          "oneof_index": 78,
          "proto3_optional": true
        },
        {
          "name": "user_engagement",
          "number": 81,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.UserEngagementProperty",
          "oneof_index": 79,
          "proto3_optional": true
        },
        {
          "name": "coaches",
          "number": 82,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.CoachesProperty",
          "oneof_index": 80,
          "proto3_optional": true
        },
        {
          "name": "themes",
          "number": 83,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.ThemesProperty",
          "oneof_index": 81,
          "proto3_optional": true
        },
        {
          "name": "ipqs",
          "number": 84,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.IpqsProperty",
          "oneof_index": 82,
          "proto3_optional": true
        },
        {
          "name": "puzzle_stats",
          "number": 85,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.UserPuzzleStatsProperty",
          "oneof_index": 83,
          "proto3_optional": true
        },
        {
          "name": "courses",
          "number": 86,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.CoursesProperty",
          "oneof_index": 84,
          "proto3_optional": true
        },
        {
          "name": "survey",
          "number": 87,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.SurveyProperty",
          "oneof_index": 85,
          "proto3_optional": true
        },
        {
          "name": "attribution_subscription_upgrade_initial",
          "number": 88,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AttributionProperty",
          "oneof_index": 86,
          "proto3_optional": true
        },
        {
          "name": "attribution_subscription_upgrade_last",
          "number": 89,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AttributionProperty",
          "oneof_index": 87,
          "proto3_optional": true
        },
        {
          "name": "product_activity_rankings",
          "number": 90,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.ProductActivityRankingsProperty",
          "oneof_index": 88,
          "proto3_optional": true
        },
        {
          "name": "turnstile",
          "number": 91,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TurnstileProperty",
          "oneof_index": 89,
          "proto3_optional": true
        },
        {
          "name": "user_streak_v2",
          "number": 92,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.UserStreakV2Property",
          "oneof_index": 90,
          "proto3_optional": true
        },
        {
          "name": "fair_play",
          "number": 93,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.FairPlayProperty",
          "oneof_index": 91,
          "proto3_optional": true
        },
        {
          "name": "navbar",
          "number": 94,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.NavbarProperty",
          "oneof_index": 92,
          "proto3_optional": true
        },
        {
          "name": "themes_ios",
          "number": 95,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.ThemesProperty",
          "oneof_index": 93,
          "proto3_optional": true
        },
        {
          "name": "themes_android",
          "number": 96,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.ThemesProperty",
          "oneof_index": 94,
          "proto3_optional": true
        },
        {
          "name": "widgets_ios",
          "number": 97,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.WidgetsProperty",
          "oneof_index": 95,
          "proto3_optional": true
        },
        {
          "name": "widgets_android",
          "number": 98,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.WidgetsProperty",
          "oneof_index": 96,
          "proto3_optional": true
        },
        {
          "name": "league",
          "number": 99,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.LeagueProperty",
          "oneof_index": 97,
          "proto3_optional": true
        },
        {
          "name": "puzzle_rush",
          "number": 100,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PuzzleRushProperty",
          "oneof_index": 98,
          "proto3_optional": true
        },
        {
          "name": "monthly_bot_event",
          "number": 101,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.MonthlyBotEventProperty",
          "oneof_index": 99,
          "proto3_optional": true
        },
        {
          "name": "predictive",
          "number": 102,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PredictiveProperty",
          "oneof_index": 100,
          "proto3_optional": true
        },
        {
          "name": "growth",
          "number": 103,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.GrowthProperty",
          "oneof_index": 101,
          "proto3_optional": true
        },
        {
          "name": "skills",
          "number": 104,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.SkillsProperty",
          "oneof_index": 102,
          "proto3_optional": true
        },
        {
          "name": "opening_courses",
          "number": 105,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.OpeningCoursesProperty",
          "oneof_index": 103,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_core"
        },
        {
          "name": "_pii"
        },
        {
          "name": "_user_details"
        },
        {
          "name": "_roles"
        },
        {
          "name": "_activity"
        },
        {
          "name": "_subscription"
        },
        {
          "name": "_attribution_signup_initial"
        },
        {
          "name": "_attribution_signup_last"
        },
        {
          "name": "_attribution_trial_initial"
        },
        {
          "name": "_attribution_trial_last"
        },
        {
          "name": "_ratings"
        },
        {
          "name": "_wdl"
        },
        {
          "name": "_analysis"
        },
        {
          "name": "_settings_daily_chess"
        },
        {
          "name": "_settings_live_chess"
        },
        {
          "name": "_stats_daily_chess"
        },
        {
          "name": "_stats_daily_chess960"
        },
        {
          "name": "_stats_live_chess_bullet"
        },
        {
          "name": "_stats_live_chess_blitz"
        },
        {
          "name": "_stats_live_chess_rapid"
        },
        {
          "name": "_stats_live_chess960_bullet"
        },
        {
          "name": "_stats_live_chess960_blitz"
        },
        {
          "name": "_stats_live_chess960_rapid"
        },
        {
          "name": "_stats_live_bughouse"
        },
        {
          "name": "_user_settings"
        },
        {
          "name": "_puzzles_attempted"
        },
        {
          "name": "_clubs"
        },
        {
          "name": "_puzzle_battle"
        },
        {
          "name": "_audiences"
        },
        {
          "name": "_user_abuse"
        },
        {
          "name": "_daily_puzzles_solved"
        },
        {
          "name": "_play_bullet_chess"
        },
        {
          "name": "_play_bullet_chess960"
        },
        {
          "name": "_play_bullet_bughouse"
        },
        {
          "name": "_play_bullet_threecheck"
        },
        {
          "name": "_play_bullet_crazyhouse"
        },
        {
          "name": "_play_bullet_kingofthehill"
        },
        {
          "name": "_play_bullet_oddschess"
        },
        {
          "name": "_play_blitz_chess"
        },
        {
          "name": "_play_blitz_chess960"
        },
        {
          "name": "_play_blitz_bughouse"
        },
        {
          "name": "_play_blitz_threecheck"
        },
        {
          "name": "_play_blitz_crazyhouse"
        },
        {
          "name": "_play_blitz_kingofthehill"
        },
        {
          "name": "_play_blitz_oddschess"
        },
        {
          "name": "_play_rapid_chess"
        },
        {
          "name": "_play_rapid_chess960"
        },
        {
          "name": "_play_rapid_bughouse"
        },
        {
          "name": "_play_rapid_threecheck"
        },
        {
          "name": "_play_rapid_crazyhouse"
        },
        {
          "name": "_play_rapid_kingofthehill"
        },
        {
          "name": "_play_rapid_oddschess"
        },
        {
          "name": "_play_daily_chess"
        },
        {
          "name": "_play_daily_chess960"
        },
        {
          "name": "_play_daily_oddschess"
        },
        {
          "name": "_tournament_bullet_chess"
        },
        {
          "name": "_tournament_bullet_chess960"
        },
        {
          "name": "_tournament_bullet_bughouse"
        },
        {
          "name": "_tournament_bullet_threecheck"
        },
        {
          "name": "_tournament_bullet_crazyhouse"
        },
        {
          "name": "_tournament_bullet_kingofthehill"
        },
        {
          "name": "_tournament_bullet_oddschess"
        },
        {
          "name": "_tournament_blitz_chess"
        },
        {
          "name": "_tournament_blitz_chess960"
        },
        {
          "name": "_tournament_blitz_bughouse"
        },
        {
          "name": "_tournament_blitz_threecheck"
        },
        {
          "name": "_tournament_blitz_crazyhouse"
        },
        {
          "name": "_tournament_blitz_kingofthehill"
        },
        {
          "name": "_tournament_blitz_oddschess"
        },
        {
          "name": "_tournament_rapid_chess"
        },
        {
          "name": "_tournament_rapid_chess960"
        },
        {
          "name": "_tournament_rapid_bughouse"
        },
        {
          "name": "_tournament_rapid_threecheck"
        },
        {
          "name": "_tournament_rapid_crazyhouse"
        },
        {
          "name": "_tournament_rapid_kingofthehill"
        },
        {
          "name": "_tournament_rapid_oddschess"
        },
        {
          "name": "_tournament_daily_chess"
        },
        {
          "name": "_tournament_daily_chess960"
        },
        {
          "name": "_tournament_daily_oddschess"
        },
        {
          "name": "_user_engagement"
        },
        {
          "name": "_coaches"
        },
        {
          "name": "_themes"
        },
        {
          "name": "_ipqs"
        },
        {
          "name": "_puzzle_stats"
        },
        {
          "name": "_courses"
        },
        {
          "name": "_survey"
        },
        {
          "name": "_attribution_subscription_upgrade_initial"
        },
        {
          "name": "_attribution_subscription_upgrade_last"
        },
        {
          "name": "_product_activity_rankings"
        },
        {
          "name": "_turnstile"
        },
        {
          "name": "_user_streak_v2"
        },
        {
          "name": "_fair_play"
        },
        {
          "name": "_navbar"
        },
        {
          "name": "_themes_ios"
        },
        {
          "name": "_themes_android"
        },
        {
          "name": "_widgets_ios"
        },
        {
          "name": "_widgets_android"
        },
        {
          "name": "_league"
        },
        {
          "name": "_puzzle_rush"
        },
        {
          "name": "_monthly_bot_event"
        },
        {
          "name": "_predictive"
        },
        {
          "name": "_growth"
        },
        {
          "name": "_skills"
        },
        {
          "name": "_opening_courses"
        }
      ]
    },
    {
      "name": "Definitions",
      "field": [
        {
          "name": "core",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.CorePropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "pii",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PIIPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "user_details",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserDetailsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "roles",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.RolesPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "activity",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ActivityPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "subscription",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SubscriptionPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "attribution_signup_initial",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "attribution_signup_last",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "attribution_trial_initial",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "attribution_trial_last",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "ratings",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.RatingsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "wdl",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.WDLPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "analysis",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AnalysisPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "settings_daily_chess",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "settings_live_chess",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "stats_daily_chess",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsDailyPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_daily_chess960",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_chess_bullet",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_chess_blitz",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_chess_rapid",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_chess960_bullet",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_chess960_blitz",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_chess960_rapid",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "stats_live_bughouse",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "user_settings",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserSettingsPropertyDefinition",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "puzzles_attempted",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "clubs",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ClubsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "puzzle_battle",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PuzzleBattlePropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "audiences",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AudiencesPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "user_abuse",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserAbusePropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "setting",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.settings.v1.Setting",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "daily_puzzles_solved",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "play_bullet_chess",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_bullet_chess960",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_bullet_bughouse",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_bullet_threecheck",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_bullet_crazyhouse",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_bullet_kingofthehill",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_bullet_oddschess",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_chess",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_chess960",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_bughouse",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_threecheck",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_crazyhouse",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_kingofthehill",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_blitz_oddschess",
          "number": 46,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_chess",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_chess960",
          "number": 48,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_bughouse",
          "number": 49,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_threecheck",
          "number": 50,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_crazyhouse",
          "number": 51,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_kingofthehill",
          "number": 52,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_rapid_oddschess",
          "number": 53,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_daily_chess",
          "number": 54,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_daily_chess960",
          "number": 55,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "play_daily_oddschess",
          "number": 56,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_chess",
          "number": 57,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_chess960",
          "number": 58,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_bughouse",
          "number": 59,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_threecheck",
          "number": 60,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_crazyhouse",
          "number": 61,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_kingofthehill",
          "number": 62,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_bullet_oddschess",
          "number": 63,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_chess",
          "number": 64,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_chess960",
          "number": 65,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_bughouse",
          "number": 66,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_threecheck",
          "number": 67,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_crazyhouse",
          "number": 68,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_kingofthehill",
          "number": 69,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_blitz_oddschess",
          "number": 70,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_chess",
          "number": 71,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_chess960",
          "number": 72,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_bughouse",
          "number": 73,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_threecheck",
          "number": 74,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_crazyhouse",
          "number": 75,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_kingofthehill",
          "number": 76,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_rapid_oddschess",
          "number": 77,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_daily_chess",
          "number": 78,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_daily_chess960",
          "number": 79,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "tournament_daily_oddschess",
          "number": 80,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "user_engagement",
          "number": 81,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserEngagementPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "coaches",
          "number": 82,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.CoachesPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "themes",
          "number": 83,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ThemesPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "ipqs",
          "number": 84,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.IpqsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "puzzle_stats",
          "number": 85,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "courses",
          "number": 86,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.CoursesPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "survey",
          "number": 87,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SurveyPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "attribution_subscription_upgrade_initial",
          "number": 88,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "attribution_subscription_upgrade_last",
          "number": 89,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "product_activity_rankings",
          "number": 90,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "turnstile",
          "number": 91,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TurnstilePropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "user_streak_v2",
          "number": 92,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserStreakV2PropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "fair_play",
          "number": 93,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.FairPlayPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "navbar",
          "number": 94,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.NavbarPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "themes_ios",
          "number": 95,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ThemesPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "themes_android",
          "number": 96,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ThemesPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "widgets_ios",
          "number": 97,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.WidgetsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "widgets_android",
          "number": 98,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.WidgetsPropertyDefinition",
          "options": {},
          "oneof_index": 0
        },
        {
          "name": "league",
          "number": 99,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.LeaguePropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "puzzle_rush",
          "number": 100,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PuzzleRushPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "monthly_bot_event",
          "number": 101,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "predictive",
          "number": 102,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PredictivePropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "growth",
          "number": 103,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.GrowthPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "skills",
          "number": 104,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SkillsPropertyDefinition",
          "oneof_index": 0
        },
        {
          "name": "opening_courses",
          "number": 105,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.OpeningCoursesPropertyDefinition",
          "oneof_index": 0
        }
      ],
      "extension": [
        {
          "name": "property_name_prefix",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1999,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "json_name": "propertyNamePrefix",
          "proto3_optional": true
        },
        {
          "name": "deprecation_date",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 2001,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "json_name": "deprecationDate",
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "definition"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 618473.

```text
RjaBgKIAEoCzIiLmNoZXNzY29tLnNldHRpbmdzLnYxLldhdGNoU2V0dGluZ0gAOgeCph0DCgEBQgcKBXZhbHVlYgZwcm90bzM","chesscom/user_properties/v1/properties.proto":"CixjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllcy5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIuQBChBQcm9wZXJ0aWVzQnlVc2VyEgwKBHVzZXIYASABKAkSOwoKcHJvcGVydGllcxgCIAEoCzInLmNoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MS5Qcm9wZXJ0aWVzEmAKF3RpbWVfd2luZG93c19wcm9wZXJ0aWVzGAMgASgLM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17860"></a>
## FND-17860: Full frontend descriptor: chesscom/user_properties/v1/authenticated_properties_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/authenticated_properties_service.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "GetPropertiesForAuthenticatedUserRequest",
      "field": [
        {
          "name": "properties",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.Definitions"
        }
      ],
      "options": {}
    },
    {
      "name": "GetPropertiesForAuthenticatedUserResponse",
      "field": [
        {
          "name": "user_properties",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PropertiesByUser"
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "AuthenticatedPropertiesService",
      "method": [
        {
          "name": "GetPropertiesForAuthenticatedUser",
          "input_type": ".chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserRequest",
          "output_type": ".chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserResponse",
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 649239.

```text
nbGUucHJvdG9idWYuVGltZXN0YW1wUg9kZXByZWNhdGlvbkRhdGWIAQE6B4KmHQMKAQFCDAoKZGVmaW5pdGlvbmIGcHJvdG8z","chesscom/user_properties/v1/authenticated_properties_service.proto":"CkJjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvYXV0aGVudGljYXRlZF9wcm9wZXJ0aWVzX3NlcnZpY2UucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSJxCihHZXRQcm9wZXJ0aWVzRm9yQXV0aGVudGljYXRlZFVzZXJSZXF1ZXN0EjwKCnByb3BlcnRpZXMYASADKAsyKC5jaGVzc2NvbS51c2VyX3Byb3BlcnRpZXM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17862"></a>
## FND-17862: Full frontend descriptor: chesscom/user_gateway/v1/user_gateway.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_gateway/v1/user_gateway.proto",
  "package": "chesscom.user_gateway.v1",
  "message_type": [
    {
      "name": "GatewayUserView",
      "field": [
        {
          "name": "user",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        },
        {
          "name": "user_properties",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PropertiesByUser",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "presence",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.presence.v1.UserPresence",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "ratings",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ratings.v2.VariantTimeClassRatingGroup"
        },
        {
          "name": "relationships",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_relationships.v2.ListableUserRelationship"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_properties"
        },
        {
          "name": "_presence"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 650237.

```text
m0uY29tEhpzdGFnaW5nLmNoZXNzLXBsYXRmb3JtLmNvbRIXcHJvZC5jaGVzcy1wbGF0Zm9ybS5jb20aACICCAFiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway.proto":"CitjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5LnByb3RvEhhjaGVzc2NvbS51c2VyX2dhdGV3YXkudjEigQMKD0dhdGV3YXlVc2VyVmlldxIoCgR1c2VyGAEgASgLMhouY2hlc3Njb20udXNlci52MS5Vc2VyVmlldxJLCg91c2VyX3Byb3BlcnRpZXMYAiABKAsyLS5jaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEuUHJvcGVydGllc0J5VXNlck
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17863"></a>
## FND-17863: Full frontend descriptor: chesscom/user_gateway/v1/user_gateway_service_envelopes.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_gateway/v1/user_gateway_service_envelopes.proto",
  "package": "chesscom.user_gateway.v1",
  "message_type": [
    {
      "name": "RelationshipWriteSuccess",
      "field": [
        {
          "name": "completed_at",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ],
      "options": {}
    },
    {
      "name": "SendFriendRequestFailure",
      "field": [
        {
          "name": "already_friends",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.AlreadyFriends",
          "oneof_index": 0
        },
        {
          "name": "user_blocked",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserBlocked",
          "oneof_index": 0
        },
        {
          "name": "self_relationship_not_allowed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.SelfRelationshipNotAllowed",
          "oneof_index": 0
        },
        {
          "name": "friendship_limit_reached",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.FriendshipLimitReached",
          "oneof_index": 0
        },
        {
          "name": "target_friend_cap_reached",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetFriendCapReached",
          "oneof_index": 0
        },
        {
          "name": "outgoing_friend_request_cap_reached",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.OutgoingFriendRequestCapReached",
          "oneof_index": 0
        },
        {
          "name": "trust_level_denied",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TrustLevelDenied",
          "oneof_index": 0
        },
        {
          "name": "rate_limit_exceeded",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RateLimitExceeded",
          "oneof_index": 0
        },
        {
          "name": "target_not_accepting_friend_requests",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests",
          "oneof_index": 0
        },
        {
          "name": "target_unavailable",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUnavailable",
          "oneof_index": 0
        },
        {
          "name": "sender_not_allowed",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.SenderNotAllowed",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        },
        {
          "name": "target_user_not_found",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "AcceptFriendRequestFailure",
      "field": [
        {
          "name": "not_found",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipNotFound",
          "oneof_index": 0
        },
        {
          "name": "friend_request_not_pending",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.FriendRequestNotPending",
          "oneof_index": 0
        },
        {
          "name": "friendship_limit_reached",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.FriendshipLimitReached",
          "oneof_index": 0
        },
        {
          "name": "user_blocked",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserBlocked",
          "oneof_index": 0
        },
        {
          "name": "rate_limit_exceeded",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RateLimitExceeded",
          "oneof_index": 0
        },
        {
          "name": "target_user_not_found",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "DeclineFriendRequestFailure",
      "field": [
        {
          "name": "rate_limit_exceeded",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RateLimitExceeded",
          "oneof_index": 0
        },
        {
          "name": "target_user_not_found",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "CancelFriendRequestFailure",
      "field": [
        {
          "name": "rate_limit_exceeded",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RateLimitExceeded",
          "oneof_index": 0
        },
        {
          "name": "target_user_not_found",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "RemoveFriendFailure",
      "field": [
        {
          "name": "target_user_not_found",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "BlockUserFailure",
      "field": [
        {
          "name": "target_immune",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetImmune",
          "oneof_index": 0
        },
        {
          "name": "block_limit_reached",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.BlockLimitReached",
          "oneof_index": 0
        },
        {
          "name": "self_relationship_not_allowed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.SelfRelationshipNotAllowed",
          "oneof_index": 0
        },
        {
          "name": "target_user_not_found",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "UnblockUserFailure",
      "field": [
        {
          "name": "target_user_not_found",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.TargetUserNotFound",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "AcceptFriendLinkSuccess",
      "field": [
        {
          "name": "friend_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "friend_username",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "AcceptFriendLinkFailure",
      "field": [
        {
          "name": "friend_link_invalid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.FriendLinkInvalid",
          "oneof_index": 0
        },
        {
          "name": "friend_link_not_found",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.FriendLinkNotFound",
          "oneof_index": 0
        },
        {
          "name": "self_relationship_not_allowed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.SelfRelationshipNotAllowed",
          "oneof_index": 0
        },
        {
          "name": "user_blocked",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserBlocked",
          "oneof_index": 0
        },
        {
          "name": "friendship_limit_reached",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.FriendshipLimitReached",
          "oneof_index": 0
        },
        {
          "name": "rate_limit_exceeded",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RateLimitExceeded",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.InvalidRequest",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    },
    {
      "name": "AlreadyFriends",
      "options": {}
    },
    {
      "name": "TargetFriendCapReached",
      "options": {}
    },
    {
      "name": "OutgoingFriendRequestCapReached",
      "options": {}
    },
    {
      "name": "TrustLevelDenied",
      "field": [
        {
          "name": "reason",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_reason"
        }
      ]
    },
    {
      "name": "TargetNotAcceptingFriendRequests",
      "options": {}
    },
    {
      "name": "TargetUnavailable",
      "options": {}
    },
    {
      "name": "SenderNotAllowed",
      "options": {}
    },
    {
      "name": "TargetUserNotFound",
      "options": {}
    },
    {
      "name": "RelationshipNotFound",
      "options": {}
    },
    {
      "name": "FriendRequestNotPending",
      "options": {}
    },
    {
      "name": "FriendLinkInvalid",
      "options": {}
    },
    {
      "name": "FriendLinkNotFound",
      "options": {}
    },
    {
      "name": "SelfRelationshipNotAllowed",
      "options": {}
    },
    {
      "name": "UserBlocked",
      "options": {}
    },
    {
      "name": "TargetImmune",
      "options": {}
    },
    {
      "name": "BlockLimitReached",
      "field": [
        {
          "name": "max_blocked_users",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendshipLimitReached",
      "field": [
        {
          "name": "max_friends",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "RateLimitExceeded",
      "field": [
        {
          "name": "retry_after_seconds",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "InvalidRequest",
      "field": [
        {
          "name": "message",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_message"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 650909.

```text
lzdGFibGVVc2VyUmVsYXRpb25zaGlwOgeCph0DCgEBQhIKEF91c2VyX3Byb3BlcnRpZXNCCwoJX3ByZXNlbmNlYgZwcm90bzM","chesscom/user_gateway/v1/user_gateway_service_envelopes.proto":"Cj1jaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2VfZW52ZWxvcGVzLnByb3RvEhhjaGVzc2NvbS51c2VyX2dhdGV3YXkudjEiVgoYUmVsYXRpb25zaGlwV3JpdGVTdWNjZXNzEjAKDGNvbXBsZXRlZF9hdBgBIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXA6CIKmHQQKAgECItIIChhTZW5kRnJpZW5k
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17864"></a>
## FND-17864: Full frontend descriptor: chesscom/user_gateway/v1/user_identifier.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_gateway/v1/user_identifier.proto",
  "package": "chesscom.user_gateway.v1",
  "message_type": [
    {
      "name": "UserIdentifier",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "username",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657210.

```text
gECIjwKDkludmFsaWRSZXF1ZXN0EhQKB21lc3NhZ2UYASABKAlIAIgBAToIgqYdBAoCAQJCCgoIX21lc3NhZ2ViBnByb3RvMw","chesscom/user_gateway/v1/user_identifier.proto":"Ci5jaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9pZGVudGlmaWVyLnByb3RvEhhjaGVzc2NvbS51c2VyX2dhdGV3YXkudjEiSQoOVXNlcklkZW50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17865"></a>
## FND-17865: Full frontend descriptor: chesscom/user_gateway/v1/user_gateway_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_gateway/v1/user_gateway_service.proto",
  "package": "chesscom.user_gateway.v1",
  "message_type": [
    {
      "name": "GetUserDataRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "other_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_relationships",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipRequestCriteria"
        },
        {
          "name": "field_mask",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataResponse",
      "field": [
        {
          "name": "user_data",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.GatewayUserView"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataByUsernameRequest",
      "field": [
        {
          "name": "username",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "other_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_relationships",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipRequestCriteria"
        },
        {
          "name": "field_mask",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        },
        {
          "name": "include_disabled",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataByUsernameResponse",
      "field": [
        {
          "name": "user_data",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.GatewayUserView"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataManyRequest",
      "field": [
        {
          "name": "user_uuids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "other_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_relationships",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipRequestCriteria"
        },
        {
          "name": "field_mask",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataManyResponse",
      "field": [
        {
          "name": "user_data",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.GatewayUserView"
        }
      ],
      "options": {}
    },
    {
      "name": "ListRelatedUsersDataRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "other_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_relationships",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipRequestCriteria"
        },
        {
          "name": "field_mask",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        }
      ],
      "options": {}
    },
    {
      "name": "ListRelatedUsersDataResponse",
      "field": [
        {
          "name": "user_data",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.GatewayUserView"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataWithOtherUsernamesRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "other_usernames",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_relationships",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipRequestCriteria"
        },
        {
          "name": "field_mask",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        },
        {
          "name": "include_disabled",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUserDataWithOtherUsernamesResponse",
      "field": [
        {
          "name": "user_data",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.GatewayUserView"
        }
      ],
      "options": {}
    },
    {
      "name": "ListUsersRequest",
      "field": [
        {
          "name": "pagination",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "criteria",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.Criterion"
        },
        {
          "name": "field_mask",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_pagination"
        }
      ]
    },
    {
      "name": "ListUsersResponse",
      "field": [
        {
          "name": "user_data",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.GatewayUserView"
        },
        {
          "name": "pagination",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.ResponsePagination"
        }
      ],
      "options": {}
    },
    {
      "name": "SendFriendRequestRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        },
        {
          "name": "source",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "method",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_source"
        },
        {
          "name": "_method"
        }
      ]
    },
    {
      "name": "SendFriendRequestResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.SendFriendRequestFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "AcceptFriendRequestRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        }
      ],
      "options": {}
    },
    {
      "name": "AcceptFriendRequestResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.AcceptFriendRequestFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "DeclineFriendRequestRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        }
      ],
      "options": {}
    },
    {
      "name": "DeclineFriendRequestResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.DeclineFriendRequestFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "CancelFriendRequestRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        }
      ],
      "options": {}
    },
    {
      "name": "CancelFriendRequestResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.CancelFriendRequestFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "RemoveFriendRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        }
      ],
      "options": {}
    },
    {
      "name": "RemoveFriendResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RemoveFriendFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "BlockUserRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        }
      ],
      "options": {}
    },
    {
      "name": "BlockUserResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.BlockUserFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "UnblockUserRequest",
      "field": [
        {
          "name": "user_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UserIdentifier"
        }
      ],
      "options": {}
    },
    {
      "name": "UnblockUserResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.RelationshipWriteSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.UnblockUserFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "AcceptFriendLinkRequest",
      "field": [
        {
          "name": "friend_link_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "AcceptFriendLinkResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.AcceptFriendLinkSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_gateway.v1.AcceptFriendLinkFailure",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "UserGatewayService",
      "method": [
        {
          "name": "GetUserData",
          "input_type": ".chesscom.user_gateway.v1.GetUserDataRequest",
          "output_type": ".chesscom.user_gateway.v1.GetUserDataResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "GetUserDataByUsername",
          "input_type": ".chesscom.user_gateway.v1.GetUserDataByUsernameRequest",
          "output_type": ".chesscom.user_gateway.v1.GetUserDataByUsernameResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "GetUserDataMany",
          "input_type": ".chesscom.user_gateway.v1.GetUserDataManyRequest",
          "output_type": ".chesscom.user_gateway.v1.GetUserDataManyResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListRelatedUsersData",
          "input_type": ".chesscom.user_gateway.v1.ListRelatedUsersDataRequest",
          "output_type": ".chesscom.user_gateway.v1.ListRelatedUsersDataResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "GetUserDataWithOtherUsernames",
          "input_type": ".chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest",
          "output_type": ".chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListUsers",
          "input_type": ".chesscom.user_gateway.v1.ListUsersRequest",
          "output_type": ".chesscom.user_gateway.v1.ListUsersResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "SendFriendRequest",
          "input_type": ".chesscom.user_gateway.v1.SendFriendRequestRequest",
          "output_type": ".chesscom.user_gateway.v1.SendFriendRequestResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "AcceptFriendRequest",
          "input_type": ".chesscom.user_gateway.v1.AcceptFriendRequestRequest",
          "output_type": ".chesscom.user_gateway.v1.AcceptFriendRequestResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "DeclineFriendRequest",
          "input_type": ".chesscom.user_gateway.v1.DeclineFriendRequestRequest",
          "output_type": ".chesscom.user_gateway.v1.DeclineFriendRequestResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "CancelFriendRequest",
          "input_type": ".chesscom.user_gateway.v1.CancelFriendRequestRequest",
          "output_type": ".chesscom.user_gateway.v1.CancelFriendRequestResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "RemoveFriend",
          "input_type": ".chesscom.user_gateway.v1.RemoveFriendRequest",
          "output_type": ".chesscom.user_gateway.v1.RemoveFriendResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "BlockUser",
          "input_type": ".chesscom.user_gateway.v1.BlockUserRequest",
          "output_type": ".chesscom.user_gateway.v1.BlockUserResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "UnblockUser",
          "input_type": ".chesscom.user_gateway.v1.UnblockUserRequest",
          "output_type": ".chesscom.user_gateway.v1.UnblockUserResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "AcceptFriendLink",
          "input_type": ".chesscom.user_gateway.v1.AcceptFriendLinkRequest",
          "output_type": ".chesscom.user_gateway.v1.AcceptFriendLinkResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        }
      ],
      "options": {}
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17880"></a>
## FND-17880: Full frontend descriptor: chesscom/friends_search/v1/friends_search.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/friends_search/v1/friends_search.proto",
  "package": "chesscom.friends_search.v1",
  "message_type": [
    {
      "name": "FriendsSearchRootQuery",
      "field": [
        {
          "name": "order_by",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchOrderBy"
        },
        {
          "name": "query",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchQuery"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchQuery",
      "field": [
        {
          "name": "statement",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchStatement"
        },
        {
          "name": "or",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchQuery",
          "oneof_index": 0
        },
        {
          "name": "and",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchQuery",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "operator"
        }
      ]
    },
    {
      "name": "FriendsSearchStatement",
      "field": [
        {
          "name": "field_value",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchFieldValueCriteria",
          "oneof_index": 0
        },
        {
          "name": "rating_range",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRatingRangeCriteria",
          "oneof_index": 0
        },
        {
          "name": "all_fields_text",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchTextCriteria",
          "oneof_index": 0
        },
        {
          "name": "last_login_date",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchLastLoginDateCriteria",
          "oneof_index": 0
        },
        {
          "name": "is_online",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchIsOnlineCriteria",
          "oneof_index": 0
        },
        {
          "name": "all_fields_text_except_email",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchTextCriteria",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "criteria"
        }
      ]
    },
    {
      "name": "FriendsSearchFieldValueCriteria",
      "field": [
        {
          "name": "searchable_field",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchSearchableField"
        },
        {
          "name": "field_value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchTextCriteria",
      "field": [
        {
          "name": "text_to_search",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "exact_username_first",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "boost_username",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_exact_username_first"
        },
        {
          "name": "_boost_username"
        }
      ]
    },
    {
      "name": "FriendsSearchRatingRangeCriteria",
      "field": [
        {
          "name": "variant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.Variant"
        },
        {
          "name": "timeclass",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.TimeClass"
        },
        {
          "name": "min_inclusive",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "max_inclusive",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchLastLoginDateCriteria",
      "field": [
        {
          "name": "last_login_date",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchIsOnlineCriteria",
      "field": [
        {
          "name": "is_online",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchFriend",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_view",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        },
        {
          "name": "friend_since",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_login_date",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_staff",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "presence",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchPresenceStatus"
        },
        {
          "name": "best_rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "is_requestor_friend",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "country",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Country"
        },
        {
          "name": "requestor_friend_request_direction",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendRequestDirection",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "ratings",
          "number": 90,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRatingItem"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_friend_since"
        },
        {
          "name": "_last_login_date"
        },
        {
          "name": "_requestor_friend_request_direction"
        }
      ]
    },
    {
      "name": "FriendsSearchRecommendation",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_view",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        },
        {
          "name": "country",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Country"
        },
        {
          "name": "best_rating",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "ratings",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRatingItem"
        },
        {
          "name": "presence",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchPresenceStatus"
        },
        {
          "name": "is_staff",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "rank",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "score",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "reason",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "SocialFriendsSearchFriend",
      "field": [
        {
          "name": "friend",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchFriend"
        },
        {
          "name": "allows_challenges",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "allows_messages",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "full_presence",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.presence.v1.UserPresence"
        }
      ],
      "options": {}
    },
    {
      "name": "PendingFriendsSearchFriend",
      "field": [
        {
          "name": "friend",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.SocialFriendsSearchFriend"
        },
        {
          "name": "is_incoming_request",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchFriendship",
      "field": [
        {
          "name": "created_at",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "friend_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "FriendsSearchRatingItem",
      "field": [
        {
          "name": "variant_timeclass",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchVariantTimeclass"
        },
        {
          "name": "rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchOrderBy",
      "field": [
        {
          "name": "field",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchSearchableField"
        },
        {
          "name": "order",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchOrder",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_order"
        }
      ]
    },
    {
      "name": "FriendsSearchCursorToken",
      "field": [
        {
          "name": "page_number",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "page_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "how_many_pages",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "total_elements",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_how_many_pages"
        },
        {
          "name": "_total_elements"
        }
      ]
    },
    {
      "name": "BlockedUsers",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "legacy_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "username",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "extra_fields",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchExtraFieldResponse"
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchExtraFieldResponse",
      "field": [
        {
          "name": "field",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRetrievableField"
        },
        {
          "name": "string_value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "long_value",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 0
        },
        {
          "name": "integer_value",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "float_value",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 0
        },
        {
          "name": "double_value",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "oneof_index": 0
        },
        {
          "name": "bool_value",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "value"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "FriendsSearchPresenceStatus",
      "value": [
        {
          "name": "FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE",
          "number": 1
        },
        {
          "name": "FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE",
          "number": 2
        },
        {
          "name": "FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "FriendRequestDirection",
      "value": [
        {
          "name": "FRIEND_REQUEST_DIRECTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FRIEND_REQUEST_DIRECTION_OUTGOING",
          "number": 1
        },
        {
          "name": "FRIEND_REQUEST_DIRECTION_INCOMING",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchOrder",
      "value": [
        {
          "name": "FRIENDS_SEARCH_ORDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FRIENDS_SEARCH_ORDER_ASC",
          "number": 1
        },
        {
          "name": "FRIENDS_SEARCH_ORDER_DESC",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchSearchableField",
      "value": [
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME",
          "number": 1
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME",
          "number": 2
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL",
          "number": 3
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_COUNTRY",
          "number": 4
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_LOGIN_DATE",
          "number": 6
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_IS_ONLINE",
          "number": 7
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_ALL",
          "number": 8
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_ALL_EXCEPT_EMAIL",
          "number": 9
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_CREATED_DATE",
          "number": 10
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME_PREFIX",
          "number": 11
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME_UNIQUE",
          "number": 12
        },
        {
          "name": "FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_FEED_ACTIVITY",
          "number": 13
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchVariantTimeclass",
      "value": [
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS_BLITZ",
          "number": 1
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS_BULLET",
          "number": 2
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS_DAILY",
          "number": 3
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS_RAPID",
          "number": 4
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS960_BLITZ",
          "number": 5
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS960_BULLET",
          "number": 6
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS960_DAILY",
          "number": 7
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS960_RAPID",
          "number": 8
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CRAZYHOUSE_BLITZ",
          "number": 9
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_BUGHOUSE_BLITZ",
          "number": 10
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_KINGOFTHEHILL_BLITZ",
          "number": 11
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_ODDSCHESS_BLITZ",
          "number": 12
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_THREECHECK_BLITZ",
          "number": 13
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CRAZYHOUSE_BULLET",
          "number": 14
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_BUGHOUSE_BULLET",
          "number": 15
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_KINGOFTHEHILL_BULLET",
          "number": 16
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_ODDSCHESS_BULLET",
          "number": 17
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_THREECHECK_BULLET",
          "number": 18
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CRAZYHOUSE_DAILY",
          "number": 19
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_BUGHOUSE_DAILY",
          "number": 20
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_KINGOFTHEHILL_DAILY",
          "number": 21
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_ODDSCHESS_DAILY",
          "number": 22
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_THREECHECK_DAILY",
          "number": 23
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CRAZYHOUSE_RAPID",
          "number": 24
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_BUGHOUSE_RAPID",
          "number": 25
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_KINGOFTHEHILL_RAPID",
          "number": 26
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_ODDSCHESS_RAPID",
          "number": 27
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_THREECHECK_RAPID",
          "number": 28
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CHESS960",
          "number": 29
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_ODDSCHESS",
          "number": 30
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_THREECHECK",
          "number": 31
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_CRAZYHOUSE",
          "number": 32
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_BUGHOUSE",
          "number": 33
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_KINGOFTHEHILL",
          "number": 34
        },
        {
          "name": "FRIENDS_SEARCH_VARIANT_TIMECLASS_UNRATED",
          "number": 35
        }
      ],
      "options": {}
    },
    {
      "name": "FriendsSearchRetrievableField",
      "value": [
        {
          "name": "FRIENDS_SEARCH_RETRIEVABLE_FIELD_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FRIENDS_SEARCH_RETRIEVABLE_FIELD_AVATAR",
          "number": 1
        },
        {
          "name": "FRIENDS_SEARCH_RETRIEVABLE_FIELD_COUNTRY_CODE",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 666200.

```text
9kLmNoZXNzLXBsYXRmb3JtLmNvbRojEgtiZWFyZXJfYXV0aBIJcGhwc2Vzc2lkEgl4LWFwaS1rZXkiAggBKgFkYgZwcm90bzM","chesscom/friends_search/v1/friends_search.proto":"Ci9jaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaC5wcm90bxIaY2hlc3Njb20uZnJpZW5kc19zZWFyY2gudjEipAEKFkZyaWVuZHNTZWFyY2hSb290UXVlcnkSQgoIb3JkZXJfYnkYASADKAsyMC5jaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MS5GcmllbmRzU2VhcmNoT3JkZXJCeRI9CgVxdWVyeRgCIAEoCzIuLmNoZXNzY29tLmZyaW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17881"></a>
## FND-17881: Full frontend descriptor: chesscom/friends_search/v1/friends_navigation_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/friends_search/v1/friends_navigation_service.proto",
  "package": "chesscom.friends_search.v1",
  "message_type": [
    {
      "name": "ListRecentFriendsRequest",
      "options": {}
    },
    {
      "name": "ListRecentFriendsResponse",
      "field": [
        {
          "name": "friends",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.SocialFriendsSearchFriend"
        }
      ],
      "options": {}
    },
    {
      "name": "ListRecentPendingFriendsRequest",
      "field": [
        {
          "name": "pagination",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "direction",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendRequestDirection",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_pagination"
        },
        {
          "name": "_direction"
        }
      ]
    },
    {
      "name": "ListRecentPendingFriendsResponse",
      "field": [
        {
          "name": "pending_friends",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.PendingFriendsSearchFriend"
        },
        {
          "name": "pagination",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.ResponsePagination"
        }
      ],
      "options": {}
    },
    {
      "name": "SocialAutocompleteRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "prefix",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "include_friends",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "include_suggestions",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "friends_limit",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "suggestions_limit",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "exact_username_first",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "boost_username",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_include_friends"
        },
        {
          "name": "_include_suggestions"
        },
        {
          "name": "_friends_limit"
        },
        {
          "name": "_suggestions_limit"
        },
        {
          "name": "_exact_username_first"
        },
        {
          "name": "_boost_username"
        }
      ]
    },
    {
      "name": "SocialAutocompleteResponse",
      "field": [
        {
          "name": "friends",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.SocialFriendsSearchFriend"
        },
        {
          "name": "suggestions",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.SocialFriendsSearchFriend"
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "FriendsNavigationService",
      "method": [
        {
          "name": "ListRecentFriends",
          "input_type": ".chesscom.friends_search.v1.ListRecentFriendsRequest",
          "output_type": ".chesscom.friends_search.v1.ListRecentFriendsResponse"
        },
        {
          "name": "ListRecentPendingFriends",
          "input_type": ".chesscom.friends_search.v1.ListRecentPendingFriendsRequest",
          "output_type": ".chesscom.friends_search.v1.ListRecentPendingFriendsResponse"
        },
        {
          "name": "SocialAutocomplete",
          "input_type": ".chesscom.friends_search.v1.SocialAutocompleteRequest",
          "output_type": ".chesscom.friends_search.v1.SocialAutocompleteResponse",
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 676259.

```text
EFSEAESMQotRlJJRU5EU19TRUFSQ0hfUkVUUklFVkFCTEVfRklFTERfQ09VTlRSWV9DT0RFEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/friends_search/v1/friends_navigation_service.proto":"CjtjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX25hdmlnYXRpb25fc2VydmljZS5wcm90bxIaY2hlc3Njb20uZnJpZW5kc19zZWFyY2gudjEiIwoYTGlzdFJlY2VudEZyaWVuZHNSZXF1ZXN0OgeCph0DCgEBImwKGUxpc3RSZWNlbnRGcmllbmRzUmVzcG9uc2USRgoHZnJpZW5kcxgBIAMoCzI1LmNoZXNzY29tLmZyaWVuZHNfc2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17885"></a>
## FND-17885: Full frontend descriptor: chesscom/friends_search/v1/friends_search_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/friends_search/v1/friends_search_service.proto",
  "package": "chesscom.friends_search.v1",
  "message_type": [
    {
      "name": "QueryFriendsRequest",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "include_presence_status",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "pagination",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "query",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRootQuery"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_uuid"
        },
        {
          "name": "_include_presence_status"
        },
        {
          "name": "_pagination"
        }
      ]
    },
    {
      "name": "QueryFriendsResponse",
      "field": [
        {
          "name": "pagination",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.ResponsePagination"
        },
        {
          "name": "friends",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchFriend"
        }
      ],
      "options": {}
    },
    {
      "name": "AutocompleteRequest",
      "field": [
        {
          "name": "prefix",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "include_friends",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "include_suggestions",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "friends_limit",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "suggestions_limit",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "exact_username_first",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "boost_username",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_include_friends"
        },
        {
          "name": "_include_suggestions"
        },
        {
          "name": "_friends_limit"
        },
        {
          "name": "_suggestions_limit"
        },
        {
          "name": "_exact_username_first"
        },
        {
          "name": "_boost_username"
        }
      ]
    },
    {
      "name": "AutocompleteResponse",
      "field": [
        {
          "name": "friends",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchFriend"
        },
        {
          "name": "suggestions",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchFriend"
        }
      ],
      "options": {}
    },
    {
      "name": "GetBlockersOfRequest",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "pagination",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "extra_fields",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRetrievableField"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_pagination"
        }
      ]
    },
    {
      "name": "GetBlockersOfResponse",
      "field": [
        {
          "name": "pagination",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.ResponsePagination"
        },
        {
          "name": "blocked_users",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.BlockedUsers"
        }
      ],
      "options": {}
    },
    {
      "name": "GetUsersBlockedByRequest",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "last_login_date",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "extra_fields",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.friends_search.v1.FriendsSearchRetrievableField"
        },
        {
          "name": "pagination",
          "number": 99,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_login_date"
        },
        {
          "name": "_pagination"
        }
      ]
    },
    {
      "name": "GetUsersBlockedByResponse",
      "field": [
        {
          "name": "pagination",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.ResponsePagination"
        },
        {
          "name": "blocked_users",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.friends_search.v1.BlockedUsers"
        }
      ],
      "options": {}
    },
    {
      "name": "GetFriendsCountRequest",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GetFriendsCountResponse",
      "field": [
        {
          "name": "friend_count",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "FriendsSearchService",
      "method": [
        {
          "name": "QueryFriends",
          "input_type": ".chesscom.friends_search.v1.QueryFriendsRequest",
          "output_type": ".chesscom.friends_search.v1.QueryFriendsResponse",
          "options": {}
        },
        {
          "name": "Autocomplete",
          "input_type": ".chesscom.friends_search.v1.AutocompleteRequest",
          "output_type": ".chesscom.friends_search.v1.AutocompleteResponse",
          "options": {}
        },
        {
          "name": "GetBlockersOf",
          "input_type": ".chesscom.friends_search.v1.GetBlockersOfRequest",
          "output_type": ".chesscom.friends_search.v1.GetBlockersOfResponse",
          "options": {}
        },
        {
          "name": "GetUsersBlockedBy",
          "input_type": ".chesscom.friends_search.v1.GetUsersBlockedByRequest",
          "output_type": ".chesscom.friends_search.v1.GetUsersBlockedByResponse",
          "options": {}
        },
        {
          "name": "GetFriendsCount",
          "input_type": ".chesscom.friends_search.v1.GetFriendsCountRequest",
          "output_type": ".chesscom.friends_search.v1.GetFriendsCountResponse",
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 678739.

```text
dpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoLEglwaHBzZXNzaWQiAggBYgZwcm90bzM","chesscom/friends_search/v1/friends_search_service.proto":"CjdjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaF9zZXJ2aWNlLnByb3RvEhpjaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MSKLAgoTUXVlcnlGcmllbmRzUmVxdWVzdBIRCgR1dWlkGAEgASgJSACIAQESJAoXaW5jbHVkZV9wcmVzZW5jZV9zdGF0dXMYAiABKAhIAYgBARI7CgpwYWdpbmF0aW9uGAMgASgLMiIuY2hlc3Njb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17891"></a>
## FND-17891: Full frontend descriptor: chesscom/ceac/v1/game_analysis.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v1/game_analysis.proto",
  "package": "chesscom.ceac.v1",
  "enum_type": [
    {
      "name": "GameAnalysisGameType",
      "value": [
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_DAILY",
          "number": 1
        },
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_LIVE",
          "number": 2
        },
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_MASTER",
          "number": 3
        },
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_PGN",
          "number": 4
        },
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER",
          "number": 5
        },
        {
          "name": "GAME_ANALYSIS_GAME_TYPE_VS_COACH",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 682458.

```text
m0uY29tEhpzdGFnaW5nLmNoZXNzLXBsYXRmb3JtLmNvbRIXcHJvZC5jaGVzcy1wbGF0Zm9ybS5jb20aACICCAFiBnByb3RvMw","chesscom/ceac/v1/game_analysis.proto":"CiRjaGVzc2NvbS9jZWFjL3YxL2dhbWVfYW5hbHlzaXMucHJvdG8SEGNoZXNzY29tLmNlYWMudjEqoQIKFEdhbWVBbmFseXNpc0dhbWVUeXBlEicKI0dBTUVfQU5BTFlTSVNfR0FNRV9UWVBFX1VOU1BFQ0lGSUVEEAASIQodR0FNRV9BTkFMWVNJU19HQU1FX1RZUEVfREFJTFkQARIgChxHQU1FX0FOQUxZU0lTX0dBTUVfVFlQRV9MSVZFEAISIgoeR0FNRV9BTkFMWVNJU19HQ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17892"></a>
## FND-17892: Full frontend descriptor: chesscom/courses/v1/course_recommendation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_recommendation.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseRecommendation",
      "field": [
        {
          "name": "coach_text",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "variation_preview_url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_url",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "cover_image_url",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "review_count",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "short_description",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "CourseSummary",
      "field": [
        {
          "name": "variation_preview_url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "num_reviews",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "thumbnail_url",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RecommendationReason",
      "value": [
        {
          "name": "RECOMMENDATION_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RECOMMENDATION_REASON_LAST_BOOK_MOVE",
          "number": 1
        },
        {
          "name": "RECOMMENDATION_REASON_FIRST_MISTAKE",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 682975.

```text
RZUEVfVlNfQ09NUFVURVIQBRIkCiBHQU1FX0FOQUxZU0lTX0dBTUVfVFlQRV9WU19DT0FDSBAGGgeKph0DCgEBYgZwcm90bzM","chesscom/courses/v1/course_recommendation.proto":"Ci9jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9yZWNvbW1lbmRhdGlvbi5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSL0AQoUQ291cnNlUmVjb21tZW5kYXRpb24SEgoKY29hY2hfdGV4dBgBIAEoCRIdChV2YXJpYXRpb25fcHJldmlld191cmwYAiABKAkSEwoLY291cnNlX25hbWUYAyABKAkSEwoLYXV0aG9yX25hbWUYBCABKAkSEQoJY291cnNlX2lkGA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17893"></a>
## FND-17893: Full frontend descriptor: chesscom/game_review/v2/user_activity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_review/v2/user_activity.proto",
  "package": "chesscom.game_review.v2",
  "message_type": [
    {
      "name": "GameReviewStart",
      "field": [
        {
          "name": "game_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.ceac.v1.GameAnalysisGameType"
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "source",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewStartSource"
        },
        {
          "name": "funnel",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel"
        },
        {
          "name": "game_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        },
        {
          "name": "_game_id"
        }
      ]
    },
    {
      "name": "GameReviewPremiumModalOpened",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "trigger",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewPremiumModalTrigger",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "category",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        },
        {
          "name": "_trigger"
        },
        {
          "name": "_category"
        }
      ]
    },
    {
      "name": "GameReviewPremiumModalClosed",
      "field": [
        {
          "name": "button_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewPremiumModalButton",
          "options": {}
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "trigger",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewPremiumModalTrigger",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        },
        {
          "name": "_trigger"
        }
      ]
    },
    {
      "name": "GameReviewPremiumModalUpgradeClicked",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "trigger",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewPremiumModalTrigger",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        },
        {
          "name": "_trigger"
        }
      ]
    },
    {
      "name": "GameReviewStartReviewClicked",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewOverviewScreenContinueReviewClicked",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewSelfAnalysisClicked",
      "field": [
        {
          "name": "game_review_screen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewScreen",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_review_screen"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewOverviewScreenEvalGraphClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewClassificationsExpandClicked",
      "field": [
        {
          "name": "is_expanded",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMoveClassificationClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewStartGameClicked",
      "field": [
        {
          "name": "time_class",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "game_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.ceac.v1.GameAnalysisGameType"
        },
        {
          "name": "game_review_screen",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewScreen",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_review_screen"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMoveFeedbackButtonClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "button_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewMoveFeedbackButton",
          "options": {}
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMovesMoveNodeClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMoveChangedClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "move_navigation_method",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewMoveNavigationMethod"
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMoveChangedArrowKeyPressed",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "move_navigation_method",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewMoveNavigationMethod"
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewBackButtonClicked",
      "field": [
        {
          "name": "button_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewBackButtonWeb",
          "options": {}
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMovesEvalGraphClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewMovesMovesPlaybackToggled",
      "field": [
        {
          "name": "moves_playback_enabled",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewCoachAudioToggleMuteClicked",
      "field": [
        {
          "name": "coach_speech_muted",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "coach_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "game_review_screen",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewScreen",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        },
        {
          "name": "_game_review_screen"
        }
      ]
    },
    {
      "name": "GameReviewShowMovesToggleClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "button_state",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.ShowMovesButtonState"
        },
        {
          "name": "user_or_opponent_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewCoachVisualization",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewCeacResponse",
      "field": [
        {
          "name": "is_user_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "game_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.ceac.v1.GameAnalysisGameType"
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "source",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewStartSource"
        },
        {
          "name": "ceac_response_result",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewCoachTextFeedback",
      "field": [
        {
          "name": "celebrity_coach_text",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_feedback",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "game_link",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_number",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "selected_coach_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "selected_coach_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_classification",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "cee_version",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "engine_strength",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_feedback"
        }
      ]
    },
    {
      "name": "GameReviewCourseRecommendationViewed",
      "field": [
        {
          "name": "course_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewCourseRecommendationType"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseRecommendationClicked",
      "field": [
        {
          "name": "course_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewCourseRecommendationType"
        },
        {
          "name": "opening_name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "fen",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "variation_preview_url",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_id",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_url",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "cover_image_url",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "review_count",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "short_description",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_color",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseRecommendationDecision",
      "field": [
        {
          "name": "rec_eligible",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "course_matched",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "reason",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason"
        },
        {
          "name": "recommendation_reason",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.RecommendationReason"
        },
        {
          "name": "fen",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_rating"
        }
      ]
    },
    {
      "name": "GameReviewCourseRecommendationSuppressed",
      "field": [
        {
          "name": "reason",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewCourseRecommendationType",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "fen",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "opening",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_type"
        },
        {
          "name": "_rating"
        },
        {
          "name": "_fen"
        },
        {
          "name": "_opening"
        }
      ]
    },
    {
      "name": "GameReviewCourseDeviationViewed",
      "field": [
        {
          "name": "course_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseDeviationClicked",
      "field": [
        {
          "name": "course_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseDeviationShowMovesClicked",
      "field": [
        {
          "name": "course_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewUserMoveMade",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewTakeawaysViewed",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "paywall_shown",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "train_cta_destination",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "train_item_type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainItemType",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_train_cta_destination"
        },
        {
          "name": "_train_item_type"
        }
      ]
    },
    {
      "name": "GameReviewTakeawaysUpgradeClicked",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewTakeawaysTrainCtaClicked",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "destination",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination"
        },
        {
          "name": "game_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "train_item_type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainItemType",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_id"
        },
        {
          "name": "_train_item_type"
        }
      ]
    },
    {
      "name": "GameReviewTakeawaysNextClicked",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "train_cta_shown",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "train_item_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainItemType",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_train_item_type"
        }
      ]
    },
    {
      "name": "GameReviewMoveContextExtension",
      "field": [
        {
          "name": "move_number",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "move_classification",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "is_key_move",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        }
      ]
    },
    {
      "name": "GameReviewContextExtension",
      "field": [
        {
          "name": "specific_move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "nested_type": [
        {
          "name": "GameReviewMove",
          "field": [
            {
              "name": "move_number",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "user_or_opponent_move",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
              "oneof_index": 0,
              "proto3_optional": true
            },
            {
              "name": "move_classification",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
            },
            {
              "name": "is_key_move",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL"
            }
          ],
          "oneof_decl": [
            {
              "name": "_user_or_opponent_move"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_specific_move"
        }
      ]
    },
    {
      "name": "GameReviewExplainButtonClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewExplainButtonClosed",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewExplainMoveNavClicked",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "user_or_opponent_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.UserOrOpponentMove",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "percent_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "line_ply",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "move_navigation_method",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewMoveNavigationMethod"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_or_opponent_move"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewShareButtonClicked",
      "field": [
        {
          "name": "game_review_screen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewScreen",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "placement",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewSharePlacement",
          "options": {}
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_review_screen"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewShareCompleted",
      "field": [
        {
          "name": "game_review_screen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewScreen",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "placement",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewSharePlacement",
          "options": {}
        },
        {
          "name": "destination",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_review_screen"
        },
        {
          "name": "_destination"
        },
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "GameReviewSettingsClicked",
      "field": [
        {
          "name": "game_review_screen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewScreen",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_review.v2.GameReviewResult",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_review_screen"
        },
        {
          "name": "_result"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "GameReviewScreen",
      "value": [
        {
          "name": "GAME_REVIEW_SCREEN_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_SCREEN_OVERVIEW",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_SCREEN_MOVES",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "ShowMovesButtonState",
      "value": [
        {
          "name": "SHOW_MOVES_BUTTON_STATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHOW_MOVES_BUTTON_STATE_SHOW",
          "number": 1
        },
        {
          "name": "SHOW_MOVES_BUTTON_STATE_HIDE",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "UserOrOpponentMove",
      "value": [
        {
          "name": "USER_OR_OPPONENT_MOVE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_OR_OPPONENT_MOVE_USER",
          "number": 1
        },
        {
          "name": "USER_OR_OPPONENT_MOVE_OPPONENT",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewMoveNavigationMethod",
      "value": [
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD",
          "number": 3
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED",
          "number": 4
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD",
          "number": 5
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED",
          "number": 6
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG",
          "number": 7
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED",
          "number": 8
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED",
          "number": 9
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT",
          "number": 10
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT",
          "number": 11
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP",
          "number": 12
        },
        {
          "name": "GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN",
          "number": 13
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewBackButtonWeb",
      "value": [
        {
          "name": "GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewMoveFeedbackButton",
      "value": [
        {
          "name": "GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE",
          "number": 3
        },
        {
          "name": "GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE",
          "number": 4
        },
        {
          "name": "GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewPremiumModalButton",
      "value": [
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewStartSource",
      "value": [
        {
          "name": "GAME_REVIEW_START_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_HOME",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_GAME_ARCHIVE",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_PROFILE",
          "number": 3
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_GAME_END",
          "number": 4
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_ANALYSIS",
          "number": 5
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_COACH_NUDGE",
          "number": 6
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_DEEPLINK",
          "number": 7
        },
        {
          "name": "GAME_REVIEW_START_SOURCE_STATS",
          "number": 8
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewResult",
      "value": [
        {
          "name": "GAME_REVIEW_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_RESULT_USER_WON",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_RESULT_USER_LOST",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_RESULT_USER_DRAW",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseRecommendationType",
      "value": [
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseRecommendationDecisionReason",
      "value": [
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING",
          "number": 3
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewCourseRecommendationSuppressionReason",
      "value": [
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY",
          "number": 3
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG",
          "number": 4
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT",
          "number": 5
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN",
          "number": 6
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN",
          "number": 7
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR",
          "number": 8
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION",
          "number": 9
        },
        {
          "name": "GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR",
          "number": 10
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewSharePlacement",
      "value": [
        {
          "name": "GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME",
          "number": 2
        },
        {
          "name": "GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER",
          "number": 3
        },
        {
          "name": "GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR",
          "number": 4
        },
        {
          "name": "GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewTakeawaysTrainCtaDestination",
      "value": [
        {
          "name": "GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewPremiumModalTrigger",
      "value": [
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT",
          "number": 1
        },
        {
          "name": "GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 683871.

```text
FTVF9CT09LX01PVkUQARInCiNSRUNPTU1FTkRBVElPTl9SRUFTT05fRklSU1RfTUlTVEFLRRACGgeKph0DCgEBYgZwcm90bzM","chesscom/game_review/v2/user_activity.proto":"CitjaGVzc2NvbS9nYW1lX3Jldmlldy92Mi91c2VyX2FjdGl2aXR5LnByb3RvEhdjaGVzc2NvbS5nYW1lX3Jldmlldy52MiLcAgoPR2FtZVJldmlld1N0YXJ0EjkKCWdhbWVfdHlwZRgBIAEoDjImLmNoZXNzY29tLmNlYWMudjEuR2FtZUFuYWx5c2lzR2FtZVR5cGUSPgoGcmVzdWx0GAIgASgOMikuY2hlc3Njb20uZ2FtZV9yZXZpZXcudjIuR2FtZVJldmlld1Jlc3
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17894"></a>
## FND-17894: Full frontend descriptor: chesscom/courses/v1/user_access_grant.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/user_access_grant.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "UserAccessGrant",
      "value": [
        {
          "name": "USER_ACCESS_GRANT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_ACCESS_GRANT_FULL",
          "number": 1
        },
        {
          "name": "USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE",
          "number": 2
        },
        {
          "name": "USER_ACCESS_GRANT_PREVIEW",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 706896.

```text
SNQoxR0FNRV9SRVZJRVdfUFJFTUlVTV9NT0RBTF9UUklHR0VSX1RBS0VBV0FZU19UUkFJThACGgiKph0ECgIBAmIGcHJvdG8z","chesscom/courses/v1/user_access_grant.proto":"CitjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfYWNjZXNzX2dyYW50LnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxKqEBCg9Vc2VyQWNjZXNzR3JhbnQSIQodVVNFUl9BQ0NFU1NfR1JBTlRfVU5TUEVDSUZJRUQQABIaChZVU0VSX0FDQ0VTU19HUkFOVF9GVUxMEAESJwojVVNFUl9BQ0NFU1NfR1JBTlRfRElBTU9ORF9FWENMVVNJVkUQAhIdChlVU0VSX0FDQ0VTU1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17895"></a>
## FND-17895: Full frontend descriptor: chesscom/courses_common/v1/course_price.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_price.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CoursePrice",
      "field": [
        {
          "name": "original",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "discounted",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "diamond",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_discounted"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 707263.

```text
1JBTlRfRElBTU9ORF9FWENMVVNJVkUQAhIdChlVU0VSX0FDQ0VTU19HUkFOVF9QUkVWSUVXEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/courses_common/v1/course_price.proto":"Ci1jaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfcHJpY2UucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxIqkBCgtDb3Vyc2VQcmljZRIoCghvcmlnaW5hbBgCIAEoCzIWLmNoZXNzY29tLmFwaS52MS5Nb25leRIvCgpkaXNjb3VudGVkGAMgASgLMhYuY2hlc3Njb20uYXBpLnYxLk1vbmV5SACIAQESJwoHZGlhbW9uZBgEIAEoCzIWLmNo
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17896"></a>
## FND-17896: Full frontend descriptor: chesscom/courses_common/v1/course_game_aspect.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_game_aspect.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseGameAspect",
      "field": [
        {
          "name": "main_game_aspect",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseGameAspectType"
        },
        {
          "name": "secondary_game_aspect",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseGameAspectType",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_secondary_game_aspect"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CourseGameAspectType",
      "value": [
        {
          "name": "COURSE_GAME_ASPECT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_GAME_ASPECT_TYPE_OPENING",
          "number": 1
        },
        {
          "name": "COURSE_GAME_ASPECT_TYPE_TACTICS",
          "number": 2
        },
        {
          "name": "COURSE_GAME_ASPECT_TYPE_STRATEGY",
          "number": 3
        },
        {
          "name": "COURSE_GAME_ASPECT_TYPE_ENDGAME",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 707654.

```text
SJwoHZGlhbW9uZBgEIAEoCzIWLmNoZXNzY29tLmFwaS52MS5Nb25leToHgqYdAwoBAUINCgtfZGlzY291bnRlZGIGcHJvdG8z","chesscom/courses_common/v1/course_game_aspect.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfZ2FtZV9hc3BlY3QucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxItcBChBDb3Vyc2VHYW1lQXNwZWN0EkoKEG1haW5fZ2FtZV9hc3BlY3QYASABKA4yMC5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Db3Vyc2VHYW1lQXNwZWN0VHlwZRJUChVzZWNvbmRhcnlfZ2FtZV9hc3
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17897"></a>
## FND-17897: Full frontend descriptor: chesscom/courses_common/v1/picture.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/picture.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "Picture",
      "field": [
        {
          "name": "url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "preview_url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_preview_url"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 708419.

```text
FQ1RfVFlQRV9TVFJBVEVHWRADEiMKH0NPVVJTRV9HQU1FX0FTUEVDVF9UWVBFX0VOREdBTUUQBBoHiqYdAwoBAWIGcHJvdG8z","chesscom/courses_common/v1/picture.proto":"CihjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9waWN0dXJlLnByb3RvEhpjaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MSJJCgdQaWN0dXJlEgsKA3VybBgBIAEoCRIYCgtwcmV2aWV3X3VybBgCIAEoCUgAiAEBOgeCph0DCgEBQg4KDF9wcmV2aWV3X3VybGIGcHJvdG8z","chesscom/courses_common/v1/range.proto":"CiZjaGVzc2NvbS9jb3Vyc2VzX2Nvb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17898"></a>
## FND-17898: Full frontend descriptor: chesscom/courses_common/v1/range.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/range.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "Range",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 708669.

```text
lEgsKA3VybBgBIAEoCRIYCgtwcmV2aWV3X3VybBgCIAEoCUgAiAEBOgeCph0DCgEBQg4KDF9wcmV2aWV3X3VybGIGcHJvdG8z","chesscom/courses_common/v1/range.proto":"CiZjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9yYW5nZS5wcm90bxIaY2hlc3Njb20uY291cnNlc19jb21tb24udjEiKgoFUmFuZ2USDAoEZnJvbRgBIAEoBRIKCgJ0bxgCIAEoBToHgqYdAwoBAWIGcHJvdG8z","chesscom/courses_common/v1/course_rating.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfcmF0aW5nLnByb3RvEhp
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17899"></a>
## FND-17899: Full frontend descriptor: chesscom/courses_common/v1/course_rating.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_rating.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseRating",
      "field": [
        {
          "name": "average",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "amount",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 708873.

```text
jb20uY291cnNlc19jb21tb24udjEiKgoFUmFuZ2USDAoEZnJvbRgBIAEoBRIKCgJ0bxgCIAEoBToHgqYdAwoBAWIGcHJvdG8z","chesscom/courses_common/v1/course_rating.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfcmF0aW5nLnByb3RvEhpjaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MSI4CgxDb3Vyc2VSYXRpbmcSDwoHYXZlcmFnZRgBIAEoAhIOCgZhbW91bnQYAiABKAU6B4KmHQMKAQFiBnByb3RvMw","chesscom/courses_common/v1/course_video.proto":"Ci1jaGVzc2NvbS9jb3Vyc2VzX2NvbW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17900"></a>
## FND-17900: Full frontend descriptor: chesscom/courses_common/v1/course_video.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_video.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseVideo",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "provider",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseVideoProvider"
        },
        {
          "name": "provider_video_identifier",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "thumbnail",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "duration_seconds",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_id"
        },
        {
          "name": "_thumbnail"
        },
        {
          "name": "_duration_seconds"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CourseVideoProvider",
      "value": [
        {
          "name": "COURSE_VIDEO_PROVIDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_VIDEO_PROVIDER_WISTIA",
          "number": 1
        },
        {
          "name": "COURSE_VIDEO_PROVIDER_YOUTUBE",
          "number": 2
        },
        {
          "name": "COURSE_VIDEO_PROVIDER_VIMEO",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 709115.

```text
W1vbi52MSI4CgxDb3Vyc2VSYXRpbmcSDwoHYXZlcmFnZRgBIAEoAhIOCgZhbW91bnQYAiABKAU6B4KmHQMKAQFiBnByb3RvMw","chesscom/courses_common/v1/course_video.proto":"Ci1jaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfdmlkZW8ucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxIqECCgtDb3Vyc2VWaWRlbxIPCgJpZBgBIAEoCUgAiAEBEgwKBG5hbWUYAiABKAkSQQoIcHJvdmlkZXIYAyABKA4yLy5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Db3Vyc2VWaWRlb1Byb3ZpZGVyEiEKGXByb3ZpZGVyX3Zp
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17901"></a>
## FND-17901: Full frontend descriptor: chesscom/courses_common/v1/course_source.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_source.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseSource",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.SourceType"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "SourceType",
      "value": [
        {
          "name": "SOURCE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SOURCE_TYPE_CHESSABLE",
          "number": 1
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 709898.

```text
JREVPX1BST1ZJREVSX1lPVVRVQkUQAhIfChtDT1VSU0VfVklERU9fUFJPVklERVJfVklNRU8QAxoHiqYdAwoBAWIGcHJvdG8z","chesscom/courses_common/v1/course_source.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2Vfc291cmNlLnByb3RvEhpjaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MSJZCgxDb3Vyc2VTb3VyY2USCgoCaWQYASABKAkSNAoEdHlwZRgCIAEoDjImLmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxLlNvdXJjZVR5cGU6B4KmHQMKAQEqTQoKU291cmNlVHlwZRIbChdTT1VSQ0VfVFlQRV9VTlNQRUN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17902"></a>
## FND-17902: Full frontend descriptor: chesscom/courses_common/v1/course_board_preview.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_board_preview.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseBoardPreview",
      "field": [
        {
          "name": "start_square",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "crop_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_crop_size"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 710289.

```text
IbChdTT1VSQ0VfVFlQRV9VTlNQRUNJRklFRBAAEhkKFVNPVVJDRV9UWVBFX0NIRVNTQUJMRRABGgeKph0DCgEBYgZwcm90bzM","chesscom/courses_common/v1/course_board_preview.proto":"CjVjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfYm9hcmRfcHJldmlldy5wcm90bxIaY2hlc3Njb20uY291cnNlc19jb21tb24udjEidAoSQ291cnNlQm9hcmRQcmV2aWV3Ei8KDHN0YXJ0X3NxdWFyZRgBIAEoDjIZLmNoZXNzY29tLmNoZXNzLnYxLlNxdWFyZRIWCgljcm9wX3NpemUYAiABKAVIAIgBAToHgqYdAwoBAUIMCgpfY3JvcF9z
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17903"></a>
## FND-17903: Full frontend descriptor: chesscom/courses_common/v1/course_target_level.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_target_level.proto",
  "package": "chesscom.courses_common.v1",
  "enum_type": [
    {
      "name": "CourseTargetLevel",
      "value": [
        {
          "name": "COURSE_TARGET_LEVEL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_TARGET_LEVEL_NOVICE",
          "number": 1
        },
        {
          "name": "COURSE_TARGET_LEVEL_BEGINNER",
          "number": 2
        },
        {
          "name": "COURSE_TARGET_LEVEL_INTERMEDIATE",
          "number": 3
        },
        {
          "name": "COURSE_TARGET_LEVEL_ADVANCED",
          "number": 4
        },
        {
          "name": "COURSE_TARGET_LEVEL_MASTER",
          "number": 5
        },
        {
          "name": "COURSE_TARGET_LEVEL_EXPERT",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 710627.

```text
9tLmNoZXNzLnYxLlNxdWFyZRIWCgljcm9wX3NpemUYAiABKAVIAIgBAToHgqYdAwoBAUIMCgpfY3JvcF9zaXplYgZwcm90bzM","chesscom/courses_common/v1/course_target_level.proto":"CjRjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfdGFyZ2V0X2xldmVsLnByb3RvEhpjaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MSqLAgoRQ291cnNlVGFyZ2V0TGV2ZWwSIwofQ09VUlNFX1RBUkdFVF9MRVZFTF9VTlNQRUNJRklFRBAAEh4KGkNPVVJTRV9UQVJHRVRfTEVWRUxfTk9WSUNFEAESIAocQ09VUlNFX1RBUkdFVF9MRVZFTF9CR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17904"></a>
## FND-17904: Full frontend descriptor: chesscom/courses_common/v1/course_variation_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_variation_type.proto",
  "package": "chesscom.courses_common.v1",
  "enum_type": [
    {
      "name": "CourseVariationType",
      "value": [
        {
          "name": "COURSE_VARIATION_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_VARIATION_TYPE_INFORMATIONAL",
          "number": 1
        },
        {
          "name": "COURSE_VARIATION_TYPE_ALTERNATIVE",
          "number": 2
        },
        {
          "name": "COURSE_VARIATION_TYPE_REFERENCE",
          "number": 3
        },
        {
          "name": "COURSE_VARIATION_TYPE_PUZZLE",
          "number": 4
        },
        {
          "name": "COURSE_VARIATION_TYPE_LESSON",
          "number": 5
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 711165.

```text
TRV9UQVJHRVRfTEVWRUxfTUFTVEVSEAUSHgoaQ09VUlNFX1RBUkdFVF9MRVZFTF9FWFBFUlQQBhoHiqYdAwoBAWIGcHJvdG8z","chesscom/courses_common/v1/course_variation_type.proto":"CjZjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfdmFyaWF0aW9uX3R5cGUucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxKvUBChNDb3Vyc2VWYXJpYXRpb25UeXBlEiUKIUNPVVJTRV9WQVJJQVRJT05fVFlQRV9VTlNQRUNJRklFRBAAEicKI0NPVVJTRV9WQVJJQVRJT05fVFlQRV9JTkZPUk1BVElPTkFMEAESJQohQ09VUlN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17905"></a>
## FND-17905: Full frontend descriptor: chesscom/courses_common/v1/course_drawings.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_drawings.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseDrawingArrow",
      "field": [
        {
          "name": "square_from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "square_to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseDrawingArrowType"
        }
      ]
    },
    {
      "name": "CourseDrawingSquare",
      "field": [
        {
          "name": "square",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseDrawingSquareType"
        }
      ]
    },
    {
      "name": "CourseSubvariationDrawing",
      "field": [
        {
          "name": "branch_fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "branch_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "position_fen",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "drawing_squares",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseDrawingSquare"
        },
        {
          "name": "drawing_arrows",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseDrawingArrow"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CourseDrawingArrowType",
      "value": [
        {
          "name": "COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_DRAWING_ARROW_TYPE_PRIMARY",
          "number": 1
        },
        {
          "name": "COURSE_DRAWING_ARROW_TYPE_SECONDARY",
          "number": 2
        },
        {
          "name": "COURSE_DRAWING_ARROW_TYPE_TERTIARY",
          "number": 3
        },
        {
          "name": "COURSE_DRAWING_ARROW_TYPE_QUATERNARY",
          "number": 4
        }
      ]
    },
    {
      "name": "CourseDrawingSquareType",
      "value": [
        {
          "name": "COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_DRAWING_SQUARE_TYPE_PRIMARY",
          "number": 1
        },
        {
          "name": "COURSE_DRAWING_SQUARE_TYPE_SECONDARY",
          "number": 2
        },
        {
          "name": "COURSE_DRAWING_SQUARE_TYPE_TERTIARY",
          "number": 3
        },
        {
          "name": "COURSE_DRAWING_SQUARE_TYPE_QUATERNARY",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 711679.

```text
ENPVVJTRV9WQVJJQVRJT05fVFlQRV9QVVpaTEUQBBIgChxDT1VSU0VfVkFSSUFUSU9OX1RZUEVfTEVTU09OEAViBnByb3RvMw","chesscom/courses_common/v1/course_drawings.proto":"CjBjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfZHJhd2luZ3MucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxIrQBChJDb3Vyc2VEcmF3aW5nQXJyb3cSLgoLc3F1YXJlX2Zyb20YASABKA4yGS5jaGVzc2NvbS5jaGVzcy52MS5TcXVhcmUSLAoJc3F1YXJlX3RvGAIgASgOMhkuY2hlc3Njb20uY2hlc3MudjEuU3F1YXJlEkAKBHR5c
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17906"></a>
## FND-17906: Full frontend descriptor: chesscom/courses_common/v1/course_review_author.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_review_author.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseReviewAuthor",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.UserSource"
        },
        {
          "name": "display_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "avatar",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture"
        }
      ]
    },
    {
      "name": "UserSource",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.UserSourceType"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserSourceType",
      "value": [
        {
          "name": "USER_SOURCE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_SOURCE_TYPE_CHESSCOM",
          "number": 1
        },
        {
          "name": "USER_SOURCE_TYPE_CHESSABLE",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 713216.

```text
NRVUFSRV9UWVBFX1RFUlRJQVJZEAMSKQolQ09VUlNFX0RSQVdJTkdfU1FVQVJFX1RZUEVfUVVBVEVSTkFSWRAEYgZwcm90bzM","chesscom/courses_common/v1/course_review_author.proto":"CjVjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfcmV2aWV3X2F1dGhvci5wcm90bxIaY2hlc3Njb20uY291cnNlc19jb21tb24udjEilwEKEkNvdXJzZVJldmlld0F1dGhvchI2CgZzb3VyY2UYASABKAsyJi5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Vc2VyU291cmNlEhQKDGRpc3BsYXlfbmFtZRgCIAEoCRIzCgZhdmF0YXIYAyAB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17907"></a>
## FND-17907: Full frontend descriptor: chesscom/courses_common/v1/course_product_review.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_product_review.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseProductReview",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "title",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "text",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseReviewAuthor"
        },
        {
          "name": "published_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 713867.

```text
QABIdChlVU0VSX1NPVVJDRV9UWVBFX0NIRVNTQ09NEAESHgoaVVNFUl9TT1VSQ0VfVFlQRV9DSEVTU0FCTEUQAmIGcHJvdG8z","chesscom/courses_common/v1/course_product_review.proto":"CjZjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfcHJvZHVjdF9yZXZpZXcucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxIr4BChNDb3Vyc2VQcm9kdWN0UmV2aWV3EgoKAmlkGAEgASgJEg4KBnJhdGluZxgCIAEoAhINCgV0aXRsZRgDIAEoCRIMCgR0ZXh0GAQgASgJEjwKBHVzZXIYBSABKAsyLi5jaGVzc2NvbS5jb3Vyc2V
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17908"></a>
## FND-17908: Full frontend descriptor: chesscom/courses_common/v1/course_coach_avatar.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_coach_avatar.proto",
  "package": "chesscom.courses_common.v1",
  "enum_type": [
    {
      "name": "CourseCoachAvatar",
      "value": [
        {
          "name": "COURSE_COACH_AVATAR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_COACH_AVATAR_DAVID",
          "number": 1
        },
        {
          "name": "COURSE_COACH_AVATAR_MAE",
          "number": 2
        },
        {
          "name": "COURSE_COACH_AVATAR_DANTE",
          "number": 3
        },
        {
          "name": "COURSE_COACH_AVATAR_NADIA",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 714307.

```text
yc2VSZXZpZXdBdXRob3ISMAoMcHVibGlzaGVkX2F0GAYgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses_common/v1/course_coach_avatar.proto":"CjRjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfY29hY2hfYXZhdGFyLnByb3RvEhpjaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MSq7AQoRQ291cnNlQ29hY2hBdmF0YXISIwofQ09VUlNFX0NPQUNIX0FWQVRBUl9VTlNQRUNJRklFRBAAEh0KGUNPVVJTRV9DT0FDSF9BVkFUQVJfREFWSUQQARIbChdDT1VSU0VfQ09BQ0hfQVZBVEFSX01BR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17909"></a>
## FND-17909: Full frontend descriptor: chesscom/courses_common/v1/course_variation_alternative_move.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_variation_alternative_move.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseVariationAlternativeMove",
      "field": [
        {
          "name": "san",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 714739.

```text
VJTRV9DT0FDSF9BVkFUQVJfREFOVEUQAxIdChlDT1VSU0VfQ09BQ0hfQVZBVEFSX05BRElBEAQaB4qmHQMKAQFiBnByb3RvMw","chesscom/courses_common/v1/course_variation_alternative_move.proto":"CkJjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfdmFyaWF0aW9uX2FsdGVybmF0aXZlX21vdmUucHJvdG8SGmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxIjoKHkNvdXJzZVZhcmlhdGlvbkFsdGVybmF0aXZlTW92ZRILCgNzYW4YASABKAkSCwoDZmVuGAIgASgJYgZwcm90bzM","chesscom/courses_common/v1/co
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17910"></a>
## FND-17910: Full frontend descriptor: chesscom/courses_common/v1/course_chapter_stats.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses_common/v1/course_chapter_stats.proto",
  "package": "chesscom.courses_common.v1",
  "message_type": [
    {
      "name": "CourseChapterStats",
      "field": [
        {
          "name": "trainable_variations",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "informational_variations",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "quickstarter_variations",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "alternative_variations",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "puzzles",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "average_training_depth",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "paid_video_minutes",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 715030.

```text
9uLnYxIjoKHkNvdXJzZVZhcmlhdGlvbkFsdGVybmF0aXZlTW92ZRILCgNzYW4YASABKAkSCwoDZmVuGAIgASgJYgZwcm90bzM","chesscom/courses_common/v1/course_chapter_stats.proto":"CjVjaGVzc2NvbS9jb3Vyc2VzX2NvbW1vbi92MS9jb3Vyc2VfY2hhcHRlcl9zdGF0cy5wcm90bxIaY2hlc3Njb20uY291cnNlc19jb21tb24udjEi4gEKEkNvdXJzZUNoYXB0ZXJTdGF0cxIcChR0cmFpbmFibGVfdmFyaWF0aW9ucxgBIAEoBRIgChhpbmZvcm1hdGlvbmFsX3ZhcmlhdGlvbnMYAiABKAUSHwoXcXVpY2tzdGFydGVyX3ZhcmlhdGlvbnMY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17911"></a>
## FND-17911: Full frontend descriptor: chesscom/courses/v1/course_author.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_author.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseAuthor",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "chess_title",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "picture",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseAuthorType"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_chess_title"
        },
        {
          "name": "_picture"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CourseAuthorType",
      "value": [
        {
          "name": "COURSE_AUTHOR_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_AUTHOR_TYPE_MAIN",
          "number": 1
        },
        {
          "name": "COURSE_AUTHOR_TYPE_COAUTHOR",
          "number": 2
        },
        {
          "name": "COURSE_AUTHOR_TYPE_ENDORSER",
          "number": 3
        },
        {
          "name": "COURSE_AUTHOR_TYPE_PRESENTER",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 715516.

```text
UgASgFEh4KFmF2ZXJhZ2VfdHJhaW5pbmdfZGVwdGgYBiABKAISGgoScGFpZF92aWRlb19taW51dGVzGAcgASgFYgZwcm90bzM","chesscom/courses/v1/course_author.proto":"CidjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9hdXRob3IucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiywEKDENvdXJzZUF1dGhvchIMCgRuYW1lGAEgASgJEhgKC2NoZXNzX3RpdGxlGAIgASgJSACIAQESOQoHcGljdHVyZRgDIAEoCzIjLmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxLlBpY3R1cmVIAYgBARIzCgR0eXBlGAQgASgOMiUuY2hlc3Njb20uY291cn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17912"></a>
## FND-17912: Full frontend descriptor: chesscom/courses/v1/course_canonical_line.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_canonical_line.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseCanonicalLine",
      "field": [
        {
          "name": "moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 716189.

```text
BVVRIT1JfVFlQRV9FTkRPUlNFUhADEiAKHENPVVJTRV9BVVRIT1JfVFlQRV9QUkVTRU5URVIQBBoHiqYdAwoBAWIGcHJvdG8z","chesscom/courses/v1/course_canonical_line.proto":"Ci9jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jYW5vbmljYWxfbGluZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSItChNDb3Vyc2VDYW5vbmljYWxMaW5lEg0KBW1vdmVzGAEgAygJOgeCph0DCgEBYgZwcm90bzM","chesscom/courses/v1/course_coach_speech.proto":"Ci1jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jb2FjaF9zcGVl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17913"></a>
## FND-17913: Full frontend descriptor: chesscom/courses/v1/course_coach_speech.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_coach_speech.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseCoachSpeech",
      "field": [
        {
          "name": "intro",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoachSpeechItem",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "main",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoachSpeechItem",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "subvariation_items",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoachSpeechItem"
        }
      ],
      "oneof_decl": [
        {
          "name": "_intro"
        },
        {
          "name": "_main"
        }
      ]
    },
    {
      "name": "CourseCoachSpeechItem",
      "field": [
        {
          "name": "text_item_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "audio_url_hash",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "san",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_san"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 716409.

```text
hlc3Njb20uY291cnNlcy52MSItChNDb3Vyc2VDYW5vbmljYWxMaW5lEg0KBW1vdmVzGAEgAygJOgeCph0DCgEBYgZwcm90bzM","chesscom/courses/v1/course_coach_speech.proto":"Ci1jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jb2FjaF9zcGVlY2gucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEi7QEKEUNvdXJzZUNvYWNoU3BlZWNoEj4KBWludHJvGAEgASgLMiouY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VDb2FjaFNwZWVjaEl0ZW1IAIgBARI9CgRtYWluGAIgASgLMiouY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VDb2FjaFNw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17914"></a>
## FND-17914: Full frontend descriptor: chesscom/courses/v1/course_coach_comment.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_coach_comment.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseCoachComment",
      "field": [
        {
          "name": "text",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "speech",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoachSpeechItem",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_speech"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 717023.

```text
gBIAEoCRIWCg5hdWRpb191cmxfaGFzaBgCIAEoCRIQCgNzYW4YAyABKAlIAIgBAToHgqYdAwoBAUIGCgRfc2FuYgZwcm90bzM","chesscom/courses/v1/course_coach_comment.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jb2FjaF9jb21tZW50LnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIncKEkNvdXJzZUNvYWNoQ29tbWVudBIMCgR0ZXh0GAEgASgJEj8KBnNwZWVjaBgCIAEoCzIqLmNoZXNzY29tLmNvdXJzZXMudjEuQ291cnNlQ29hY2hTcGVlY2hJdGVtSACIAQE6B4KmHQMKAQFCCQoHX3NwZWVjaGIGcHJvdG8z","ches
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17915"></a>
## FND-17915: Full frontend descriptor: chesscom/courses/v1/course_custom_tag.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_custom_tag.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseCustomTag",
      "field": [
        {
          "name": "value",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 717339.

```text
oZXNzY29tLmNvdXJzZXMudjEuQ291cnNlQ29hY2hTcGVlY2hJdGVtSACIAQE6B4KmHQMKAQFCCQoHX3NwZWVjaGIGcHJvdG8z","chesscom/courses/v1/course_custom_tag.proto":"CitjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jdXN0b21fdGFnLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIikKD0NvdXJzZUN1c3RvbVRhZxINCgV2YWx1ZRgBIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/courses/v1/course_product.proto":"CihjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0LnByb3RvEhNjaGVzc2NvbS5j
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17916"></a>
## FND-17916: Full frontend descriptor: chesscom/courses/v1/course_product.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_product.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseProduct",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "short_description",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "square_picture",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture"
        },
        {
          "name": "rectangular_picture",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture"
        },
        {
          "name": "rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseRating"
        },
        {
          "name": "recommended_level_range",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Range"
        },
        {
          "name": "game_aspect",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseGameAspect"
        },
        {
          "name": "color",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "release_date",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "authors",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseAuthor"
        },
        {
          "name": "video",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseVideo",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "slug",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_trainer_sku",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "video_sku",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "move_trainer_price",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CoursePrice",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "video_price",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CoursePrice",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "move_trainer_purchase_date",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "video_purchase_date",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "move_trainer_ids",
          "number": 21,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "variation_count",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "video_hours_count",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "is_diamond_exclusive",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "language",
          "number": 25,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Language"
        },
        {
          "name": "is_deleted",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "free_video_minutes",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "course_source",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseSource"
        },
        {
          "name": "user_access_grant",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.UserAccessGrant",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "best_for",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseTargetLevel",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "course_custom_tags",
          "number": 31,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCustomTag"
        },
        {
          "name": "canonical_line",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCanonicalLine",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "is_recommended",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "first_coach_comment",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoachComment",
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "board_preview",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseBoardPreview",
          "oneof_index": 14,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_video"
        },
        {
          "name": "_move_trainer_sku"
        },
        {
          "name": "_video_sku"
        },
        {
          "name": "_move_trainer_price"
        },
        {
          "name": "_video_price"
        },
        {
          "name": "_move_trainer_purchase_date"
        },
        {
          "name": "_video_purchase_date"
        },
        {
          "name": "_video_hours_count"
        },
        {
          "name": "_is_deleted"
        },
        {
          "name": "_free_video_minutes"
        },
        {
          "name": "_user_access_grant"
        },
        {
          "name": "_best_for"
        },
        {
          "name": "_canonical_line"
        },
        {
          "name": "_first_coach_comment"
        },
        {
          "name": "_board_preview"
        }
      ]
    },
    {
      "name": "CourseProductList",
      "field": [
        {
          "name": "course_list",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 717544.

```text
vEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIikKD0NvdXJzZUN1c3RvbVRhZxINCgV2YWx1ZRgBIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/courses/v1/course_product.proto":"CihjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0LnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIssPCg1Db3Vyc2VQcm9kdWN0EgoKAmlkGAEgASgJEgwKBG5hbWUYAiABKAkSEwoLZGVzY3JpcHRpb24YAyABKAkSGQoRc2hvcnRfZGVzY3JpcHRpb24YBCABKAkSOwoOc3F1YXJlX3BpY3R1cmUYBSABKAsyIy5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52M
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17917"></a>
## FND-17917: Full frontend descriptor: chesscom/courses/v1/user_course_recommendation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/user_course_recommendation.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "RecommendedCourse",
      "field": [
        {
          "name": "product",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct"
        },
        {
          "name": "rank",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "primary_signal",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.RecommendationSignal"
        },
        {
          "name": "eco_family",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.EcoFamily",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_eco_family"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RecommendationTouchpoint",
      "value": [
        {
          "name": "RECOMMENDATION_TOUCHPOINT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RECOMMENDATION_TOUCHPOINT_DASHBOARD",
          "number": 1
        },
        {
          "name": "RECOMMENDATION_TOUCHPOINT_SHOP",
          "number": 2
        },
        {
          "name": "RECOMMENDATION_TOUCHPOINT_APP",
          "number": 3
        }
      ]
    },
    {
      "name": "RecommendationSignal",
      "value": [
        {
          "name": "RECOMMENDATION_SIGNAL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RECOMMENDATION_SIGNAL_OPENING_MATCH",
          "number": 1
        },
        {
          "name": "RECOMMENDATION_SIGNAL_WEAKNESS_MATCH",
          "number": 2
        },
        {
          "name": "RECOMMENDATION_SIGNAL_ACTIVITY",
          "number": 3
        },
        {
          "name": "RECOMMENDATION_SIGNAL_QUALITY",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 720453.

```text
R1Y3RMaXN0EjcKC2NvdXJzZV9saXN0GAEgAygLMiIuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VQcm9kdWN0YgZwcm90bzM","chesscom/courses/v1/user_course_recommendation.proto":"CjRjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfY291cnNlX3JlY29tbWVuZGF0aW9uLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIt8BChFSZWNvbW1lbmRlZENvdXJzZRIzCgdwcm9kdWN0GAEgASgLMiIuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VQcm9kdWN0EgwKBHJhbmsYAiABKAUSQQoOcHJpbWFyeV9zaWduYWwYAyABKA4yKS5jaGVzc2Nvb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17918"></a>
## FND-17918: Full frontend descriptor: chesscom/courses/v1/course_recommendation_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_recommendation_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetCourseRecommendationForPositionRequest",
      "field": [
        {
          "name": "rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "color",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "fen",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "reason",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.RecommendationReason"
        },
        {
          "name": "user_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "eco_code",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_rating"
        },
        {
          "name": "_color"
        },
        {
          "name": "_eco_code"
        }
      ]
    },
    {
      "name": "GetCourseRecommendationForPositionResponse",
      "field": [
        {
          "name": "course",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseRecommendation",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_course"
        }
      ]
    },
    {
      "name": "GetCoursesForPositionRequest",
      "field": [
        {
          "name": "fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "color",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_color"
        }
      ]
    },
    {
      "name": "GetCoursesForPositionResponse",
      "field": [
        {
          "name": "courses",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseSummary"
        }
      ]
    },
    {
      "name": "GetUserCourseRecommendationsRequest",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "touchpoint",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.RecommendationTouchpoint"
        },
        {
          "name": "limit",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_limit"
        }
      ]
    },
    {
      "name": "GetUserCourseRecommendationsResponse",
      "field": [
        {
          "name": "set_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "courses",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.RecommendedCourse"
        },
        {
          "name": "is_fallback",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "oneof_decl": [
        {
          "name": "_set_id"
        }
      ]
    },
    {
      "name": "ReportRecommendationImpressionRequest",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "set_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "course_ids",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "touchpoint",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.RecommendationTouchpoint"
        },
        {
          "name": "is_fallback",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_set_id"
        },
        {
          "name": "_is_fallback"
        }
      ]
    },
    {
      "name": "ReportRecommendationImpressionResponse"
    }
  ],
  "service": [
    {
      "name": "CourseRecommendationService",
      "method": [
        {
          "name": "GetCourseRecommendationForPosition",
          "input_type": ".chesscom.courses.v1.GetCourseRecommendationForPositionRequest",
          "output_type": ".chesscom.courses.v1.GetCourseRecommendationForPositionResponse",
          "options": {}
        },
        {
          "name": "GetCoursesForPosition",
          "input_type": ".chesscom.courses.v1.GetCoursesForPositionRequest",
          "output_type": ".chesscom.courses.v1.GetCoursesForPositionResponse",
          "options": {}
        },
        {
          "name": "GetUserCourseRecommendations",
          "input_type": ".chesscom.courses.v1.GetUserCourseRecommendationsRequest",
          "output_type": ".chesscom.courses.v1.GetUserCourseRecommendationsResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "ReportRecommendationImpression",
          "input_type": ".chesscom.courses.v1.ReportRecommendationImpressionRequest",
          "output_type": ".chesscom.courses.v1.ReportRecommendationImpressionResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 721459.

```text
DT01NRU5EQVRJT05fU0lHTkFMX0FDVElWSVRZEAMSIQodUkVDT01NRU5EQVRJT05fU0lHTkFMX1FVQUxJVFkQBGIGcHJvdG8z","chesscom/courses/v1/course_recommendation_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9yZWNvbW1lbmRhdGlvbl9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIoACCilHZXRDb3Vyc2VSZWNvbW1lbmRhdGlvbkZvclBvc2l0aW9uUmVxdWVzdBITCgZyYXRpbmcYASABKAVIAIgBARIsCgVjb2xvchgCIAEoDjIYLmNoZXNzY29tLmNoZXNzLnYxLkNvbG9ySAGIAQESCwoDZm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17923"></a>
## FND-17923: Full frontend descriptor: chesscom/courses/v1/goal_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/goal_type.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "GoalType",
      "value": [
        {
          "name": "GOAL_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GOAL_TYPE_FTUE_CHECKLIST",
          "number": 1
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 724099.

```text
Npb25SZXNwb25zZSIDkAICQi7KtywqCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGg0SC2JlYXJlcl9hdXRoYgZwcm90bzM","chesscom/courses/v1/goal_type.proto":"CiNjaGVzc2NvbS9jb3Vyc2VzL3YxL2dvYWxfdHlwZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSpDCghHb2FsVHlwZRIZChVHT0FMX1RZUEVfVU5TUEVDSUZJRUQQABIcChhHT0FMX1RZUEVfRlRVRV9DSEVDS0xJU1QQAWIGcHJvdG8z","chesscom/courses/v1/reward.proto":"CiBjaGVzc2NvbS9jb3Vyc2VzL3YxL3Jld2FyZC5wcm90bxITY2hlc3Njb20uY291
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17924"></a>
## FND-17924: Full frontend descriptor: chesscom/courses/v1/reward.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/reward.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "Reward",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.RewardType"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_value"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RewardType",
      "value": [
        {
          "name": "REWARD_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "REWARD_TYPE_ANY_DIAMOND_COURSE",
          "number": 1
        },
        {
          "name": "REWARD_TYPE_PAID_COURSE",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 724320.

```text
Hb2FsVHlwZRIZChVHT0FMX1RZUEVfVU5TUEVDSUZJRUQQABIcChhHT0FMX1RZUEVfRlRVRV9DSEVDS0xJU1QQAWIGcHJvdG8z","chesscom/courses/v1/reward.proto":"CiBjaGVzc2NvbS9jb3Vyc2VzL3YxL3Jld2FyZC5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCgZSZXdhcmQSLQoEdHlwZRgBIAEoDjIfLmNoZXNzY29tLmNvdXJzZXMudjEuUmV3YXJkVHlwZRISCgV2YWx1ZRgCIAEoCUgAiAEBQggKBl92YWx1ZSpqCgpSZXdhcmRUeXBlEhsKF1JFV0FSRF9UWVBFX1VOU1BFQ0lGSUVEEAASIgoeUkVXQVJEX1RZUEVfQU5ZX0RJQU1PTkRfQ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17925"></a>
## FND-17925: Full frontend descriptor: chesscom/courses/v1/user_goal_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/user_goal_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "SetUserGoalRequest",
      "field": [
        {
          "name": "goal_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.GoalType"
        }
      ]
    },
    {
      "name": "SetUserGoalResponse"
    },
    {
      "name": "ClaimRewardRequest",
      "field": [
        {
          "name": "goal_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.GoalType"
        },
        {
          "name": "reward",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.Reward"
        }
      ]
    },
    {
      "name": "ClaimRewardResponse"
    }
  ],
  "service": [
    {
      "name": "UserGoalService",
      "method": [
        {
          "name": "SetUserGoal",
          "input_type": ".chesscom.courses.v1.SetUserGoalRequest",
          "output_type": ".chesscom.courses.v1.SetUserGoalResponse"
        },
        {
          "name": "ClaimReward",
          "input_type": ".chesscom.courses.v1.ClaimRewardRequest",
          "output_type": ".chesscom.courses.v1.ClaimRewardResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 724702.

```text
SIgoeUkVXQVJEX1RZUEVfQU5ZX0RJQU1PTkRfQ09VUlNFEAESGwoXUkVXQVJEX1RZUEVfUEFJRF9DT1VSU0UQAmIGcHJvdG8z","chesscom/courses/v1/user_goal_service.proto":"CitjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfZ29hbF9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIkYKElNldFVzZXJHb2FsUmVxdWVzdBIwCglnb2FsX3R5cGUYASABKA4yHS5jaGVzc2NvbS5jb3Vyc2VzLnYxLkdvYWxUeXBlIhUKE1NldFVzZXJHb2FsUmVzcG9uc2UicwoSQ2xhaW1SZXdhcmRSZXF1ZXN0EjAKCWdvYWxfdHlwZRgBIAEoDjIdLm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17928"></a>
## FND-17928: Full frontend descriptor: chesscom/courses/v1/course_user_learning_information.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_user_learning_information.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseUserLearningInformation",
      "field": [
        {
          "name": "learned_variation_amount",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "review_ready_amount",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "last_studied_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "acquired_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "is_paused",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "next_review_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_inactive",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "mastery_level",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "max_mastery_level",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "oneof_decl": [
        {
          "name": "_last_studied_at"
        },
        {
          "name": "_next_review_at"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 725498.

```text
NvdXJzZXMudjEuQ2xhaW1SZXdhcmRSZXNwb25zZUIhyrcsHQoEL3JwYxITEhFjb3Vyc2VzLmNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/courses/v1/course_user_learning_information.proto":"CjpjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV91c2VyX2xlYXJuaW5nX2luZm9ybWF0aW9uLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIoMDCh1Db3Vyc2VVc2VyTGVhcm5pbmdJbmZvcm1hdGlvbhIgChhsZWFybmVkX3ZhcmlhdGlvbl9hbW91bnQYASABKAUSGwoTcmV2aWV3X3JlYWR5X2Ftb3VudBgCIAEoBRI4Cg9sYXN0X3N0dWRpZWR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17929"></a>
## FND-17929: Full frontend descriptor: chesscom/courses/v1/ownership_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/ownership_type.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "OwnershipType",
      "value": [
        {
          "name": "OWNERSHIP_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "OWNERSHIP_TYPE_ACQUIRED",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "OWNERSHIP_TYPE_PREVIEW",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "OWNERSHIP_TYPE_CLAIMED",
          "number": 3
        },
        {
          "name": "OWNERSHIP_TYPE_PURCHASED",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 726201.

```text
kKEW1heF9tYXN0ZXJ5X2xldmVsGAkgASgFQhIKEF9sYXN0X3N0dWRpZWRfYXRCEQoPX25leHRfcmV2aWV3X2F0YgZwcm90bzM","chesscom/courses/v1/ownership_type.proto":"CihjaGVzc2NvbS9jb3Vyc2VzL3YxL293bmVyc2hpcF90eXBlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxKqoBCg1Pd25lcnNoaXBUeXBlEh4KGk9XTkVSU0hJUF9UWVBFX1VOU1BFQ0lGSUVEEAASHwoXT1dORVJTSElQX1RZUEVfQUNRVUlSRUQQARoCCAESHgoWT1dORVJTSElQX1RZUEVfUFJFVklFVxACGgIIARIaChZPV05FUlNISVBfVFlQRV9DTEFJTUVEEAMSH
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17930"></a>
## FND-17930: Full frontend descriptor: chesscom/courses/v1/course.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "Course",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "title",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "picture",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture"
        },
        {
          "name": "user_learning_information",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseUserLearningInformation"
        },
        {
          "name": "authors",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseAuthor"
        },
        {
          "name": "total_variation_amount",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "is_diamond_exclusive",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ownership_type",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.OwnershipType"
        },
        {
          "name": "slug",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_source",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseSource"
        },
        {
          "name": "is_tutorial",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "user_access_grant",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.UserAccessGrant"
        },
        {
          "name": "canonical_line",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCanonicalLine",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_canonical_line"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 726573.

```text
xACGgIIARIaChZPV05FUlNISVBfVFlQRV9DTEFJTUVEEAMSHAoYT1dORVJTSElQX1RZUEVfUFVSQ0hBU0VEEARiBnByb3RvMw","chesscom/courses/v1/course.proto":"CiBjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSLhBAoGQ291cnNlEgoKAmlkGAEgASgJEg0KBXRpdGxlGAIgASgJEjQKB3BpY3R1cmUYAyABKAsyIy5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5QaWN0dXJlElUKGXVzZXJfbGVhcm5pbmdfaW5mb3JtYXRpb24YBCABKAsyMi5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZVVzZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17931"></a>
## FND-17931: Full frontend descriptor: chesscom/courses/v1/tutorial_category.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/tutorial_category.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "TutorialCategory",
      "value": [
        {
          "name": "TUTORIAL_CATEGORY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TUTORIAL_CATEGORY_OPENING",
          "number": 1
        },
        {
          "name": "TUTORIAL_CATEGORY_TACTICS",
          "number": 2
        },
        {
          "name": "TUTORIAL_CATEGORY_STRATEGY",
          "number": 3
        },
        {
          "name": "TUTORIAL_CATEGORY_ENDGAME",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727511.

```text
oLmNoZXNzY29tLmNvdXJzZXMudjEuQ291cnNlQ2Fub25pY2FsTGluZUgAiAEBQhEKD19jYW5vbmljYWxfbGluZWIGcHJvdG8z","chesscom/courses/v1/tutorial_category.proto":"CitjaGVzc2NvbS9jb3Vyc2VzL3YxL3R1dG9yaWFsX2NhdGVnb3J5LnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxKrIBChBUdXRvcmlhbENhdGVnb3J5EiEKHVRVVE9SSUFMX0NBVEVHT1JZX1VOU1BFQ0lGSUVEEAASHQoZVFVUT1JJQUxfQ0FURUdPUllfT1BFTklORxABEh0KGVRVVE9SSUFMX0NBVEVHT1JZX1RBQ1RJQ1MQAhIeChpUVVRPUklBTF9DQVRFR09SWV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17932"></a>
## FND-17932: Full frontend descriptor: chesscom/courses/v1/courses_dashboard_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_dashboard_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetCourseListRequest"
    },
    {
      "name": "GetCourseListResponse",
      "field": [
        {
          "name": "course_list",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.Course"
        }
      ]
    },
    {
      "name": "SetCourseInactiveRequest",
      "field": [
        {
          "name": "course_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetCourseInactiveResponse"
    },
    {
      "name": "SetCoursePausedRequest",
      "field": [
        {
          "name": "course_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetCoursePausedResponse"
    },
    {
      "name": "SetCourseUnpausedRequest",
      "field": [
        {
          "name": "course_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetCourseUnpausedResponse"
    },
    {
      "name": "AssignTutorialRequest",
      "field": [
        {
          "name": "user_rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "tutorial_category",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.TutorialCategory",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "course_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "oneof_decl": [
        {
          "name": "_tutorial_category"
        }
      ]
    },
    {
      "name": "AssignTutorialResponse",
      "field": [
        {
          "name": "default_move_trainer_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetAvailableTutorialsRequest",
      "field": [
        {
          "name": "user_rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    },
    {
      "name": "GetAvailableTutorialsResponse",
      "field": [
        {
          "name": "course_list",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "course_list_by_category",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry"
        }
      ],
      "nested_type": [
        {
          "name": "CourseListByCategoryEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.courses.v1.CourseProductList"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ]
    }
  ],
  "service": [
    {
      "name": "CoursesDashboardService",
      "method": [
        {
          "name": "GetCourseList",
          "input_type": ".chesscom.courses.v1.GetCourseListRequest",
          "output_type": ".chesscom.courses.v1.GetCourseListResponse"
        },
        {
          "name": "SetCourseInactive",
          "input_type": ".chesscom.courses.v1.SetCourseInactiveRequest",
          "output_type": ".chesscom.courses.v1.SetCourseInactiveResponse"
        },
        {
          "name": "SetCoursePaused",
          "input_type": ".chesscom.courses.v1.SetCoursePausedRequest",
          "output_type": ".chesscom.courses.v1.SetCoursePausedResponse"
        },
        {
          "name": "SetCourseUnpaused",
          "input_type": ".chesscom.courses.v1.SetCourseUnpausedRequest",
          "output_type": ".chesscom.courses.v1.SetCourseUnpausedResponse"
        },
        {
          "name": "AssignTutorial",
          "input_type": ".chesscom.courses.v1.AssignTutorialRequest",
          "output_type": ".chesscom.courses.v1.AssignTutorialResponse"
        },
        {
          "name": "GetAvailableTutorials",
          "input_type": ".chesscom.courses.v1.GetAvailableTutorialsRequest",
          "output_type": ".chesscom.courses.v1.GetAvailableTutorialsResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17939"></a>
## FND-17939: Full frontend descriptor: chesscom/courses/v1/course_chapter_details.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_chapter_details.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseChapterDetails",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "stats",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseChapterStats"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 730271.

```text
kdldEF2YWlsYWJsZVR1dG9yaWFsc1Jlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/course_chapter_details.proto":"CjBjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jaGFwdGVyX2RldGFpbHMucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEibwoUQ291cnNlQ2hhcHRlckRldGFpbHMSCgoCaWQYASABKAkSDAoEbmFtZRgCIAEoCRI9CgVzdGF0cxgDIAEoCzIuLmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxLkNvdXJzZUNoYXB0ZXJTdGF0c2IGcHJvdG8z","chesscom/c
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17940"></a>
## FND-17940: Full frontend descriptor: chesscom/courses/v1/course_product_details.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_product_details.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseProductDetails",
      "field": [
        {
          "name": "product",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct"
        },
        {
          "name": "chapters",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseChapterDetails"
        },
        {
          "name": "reviews",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseProductReview"
        },
        {
          "name": "default_move_trainer_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 730581.

```text
oCRI9CgVzdGF0cxgDIAEoCzIuLmNoZXNzY29tLmNvdXJzZXNfY29tbW9uLnYxLkNvdXJzZUNoYXB0ZXJTdGF0c2IGcHJvdG8z","chesscom/courses/v1/course_product_details.proto":"CjBjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2RldGFpbHMucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEi6wEKFENvdXJzZVByb2R1Y3REZXRhaWxzEjMKB3Byb2R1Y3QYASABKAsyIi5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZVByb2R1Y3QSOwoIY2hhcHRlcnMYAiADKAsyKS5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZUNoYXB0Z
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17941"></a>
## FND-17941: Full frontend descriptor: chesscom/courses/v1/course_product_details_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_product_details_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetCourseProductBySlugRequest",
      "field": [
        {
          "name": "slug",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "country_code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseProductBySlugResponse",
      "field": [
        {
          "name": "details",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProductDetails"
        }
      ]
    },
    {
      "name": "ClaimCourseProductRequest",
      "field": [
        {
          "name": "product_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ClaimCourseProductResponse",
      "field": [
        {
          "name": "default_move_trainer_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        }
      ]
    },
    {
      "name": "GetDefaultMoveTrainerIdByProductIdRequest",
      "field": [
        {
          "name": "product_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetDefaultMoveTrainerIdByProductIdResponse",
      "field": [
        {
          "name": "default_move_trainer_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_course_owned",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_video_owned",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "SetCourseActiveRequest",
      "field": [
        {
          "name": "course_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetCourseActiveResponse"
    }
  ],
  "service": [
    {
      "name": "CourseProductDetailsService",
      "method": [
        {
          "name": "GetCourseProductBySlug",
          "input_type": ".chesscom.courses.v1.GetCourseProductBySlugRequest",
          "output_type": ".chesscom.courses.v1.GetCourseProductBySlugResponse"
        },
        {
          "name": "ClaimCourseProduct",
          "input_type": ".chesscom.courses.v1.ClaimCourseProductRequest",
          "output_type": ".chesscom.courses.v1.ClaimCourseProductResponse"
        },
        {
          "name": "GetDefaultMoveTrainerIdByProductId",
          "input_type": ".chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdRequest",
          "output_type": ".chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdResponse"
        },
        {
          "name": "SetCourseActive",
          "input_type": ".chesscom.courses.v1.SetCourseActiveRequest",
          "output_type": ".chesscom.courses.v1.SetCourseActiveResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 731058.

```text
VzX2NvbW1vbi52MS5Db3Vyc2VQcm9kdWN0UmV2aWV3Eh8KF2RlZmF1bHRfbW92ZV90cmFpbmVyX2lkGAQgASgJYgZwcm90bzM","chesscom/courses/v1/course_product_details_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2RldGFpbHNfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJDCh1HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVxdWVzdBIMCgRzbHVnGAEgASgJEhQKDGNvdW50cnlfY29kZRgCIAEoCSJcCh5HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVzcG9uc2USOgoHZGV0YWlscxgBI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17946"></a>
## FND-17946: Full frontend descriptor: chesscom/courses/v1/course_configuration.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_configuration.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseConfiguration",
      "field": [
        {
          "name": "show_video",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "language",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "learn_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseLearnType",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "review_type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseReviewType",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "repetition_amount",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "depth",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "schedule_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseScheduleType",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "schedule",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.SpacedRepetitionSchedule",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "auto_next",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "quiz_time_limit",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "timer",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "assisted_quiz",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "review_failed_behavior",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseReviewFailedBehavior",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "assisted_quiz_pause_to_read",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "learn_mode",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseConsumptionMode",
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "learn_mode_set_by_user",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 15,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_show_video"
        },
        {
          "name": "_language"
        },
        {
          "name": "_learn_type"
        },
        {
          "name": "_review_type"
        },
        {
          "name": "_repetition_amount"
        },
        {
          "name": "_depth"
        },
        {
          "name": "_schedule_type"
        },
        {
          "name": "_schedule"
        },
        {
          "name": "_auto_next"
        },
        {
          "name": "_quiz_time_limit"
        },
        {
          "name": "_timer"
        },
        {
          "name": "_assisted_quiz"
        },
        {
          "name": "_review_failed_behavior"
        },
        {
          "name": "_assisted_quiz_pause_to_read"
        },
        {
          "name": "_learn_mode"
        },
        {
          "name": "_learn_mode_set_by_user"
        }
      ]
    },
    {
      "name": "SpacedRepetitionSchedule",
      "field": [
        {
          "name": "seconds_amount",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CourseLearnType",
      "value": [
        {
          "name": "COURSE_LEARN_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_LEARN_TYPE_ALL",
          "number": 1
        },
        {
          "name": "COURSE_LEARN_TYPE_KEY",
          "number": 2
        }
      ]
    },
    {
      "name": "CourseConsumptionMode",
      "value": [
        {
          "name": "COURSE_CONSUMPTION_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_CONSUMPTION_MODE_LEARN",
          "number": 1
        },
        {
          "name": "COURSE_CONSUMPTION_MODE_READ",
          "number": 2
        },
        {
          "name": "COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH",
          "number": 3
        }
      ]
    },
    {
      "name": "CourseReviewType",
      "value": [
        {
          "name": "COURSE_REVIEW_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_REVIEW_TYPE_LEARNED_ORDER",
          "number": 1
        },
        {
          "name": "COURSE_REVIEW_TYPE_RANDOM_ORDER",
          "number": 2
        },
        {
          "name": "COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER",
          "number": 3
        }
      ]
    },
    {
      "name": "CourseScheduleType",
      "value": [
        {
          "name": "COURSE_SCHEDULE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_SCHEDULE_TYPE_SPACED_REPETITION",
          "number": 1
        },
        {
          "name": "COURSE_SCHEDULE_TYPE_CYCLICAL",
          "number": 2
        },
        {
          "name": "COURSE_SCHEDULE_TYPE_CUSTOM",
          "number": 3
        }
      ]
    },
    {
      "name": "CourseReviewFailedBehavior",
      "value": [
        {
          "name": "COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE",
          "number": 1
        },
        {
          "name": "COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE",
          "number": 2
        },
        {
          "name": "COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 732756.

```text
zZXMudjEuU2V0Q291cnNlQWN0aXZlUmVzcG9uc2VCIcq3LB0KBC9ycGMSExIRY291cnNlcy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/courses/v1/course_configuration.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jb25maWd1cmF0aW9uLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIvkHChNDb3Vyc2VDb25maWd1cmF0aW9uEhcKCnNob3dfdmlkZW8YASABKAhIAIgBARIVCghsYW5ndWFnZRgCIAEoCUgBiAEBEj0KCmxlYXJuX3R5cGUYAyABKA4yJC5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZUxlYXJuVHlwZUgCiAE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17947"></a>
## FND-17947: Full frontend descriptor: chesscom/courses/v1/course_chapter.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_chapter.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseChapter",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "video",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseVideo",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "user_video_position",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_video"
        },
        {
          "name": "_user_video_position"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 735519.

```text
5UX0NZQ0xFEAISNQoxQ09VUlNFX1JFVklFV19GQUlMRURfQkVIQVZJT1JfQkFDS19UT19GSVJTVF9DWUNMRRADYgZwcm90bzM","chesscom/courses/v1/course_chapter.proto":"CihjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jaGFwdGVyLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIqoBCg1Db3Vyc2VDaGFwdGVyEgoKAmlkGAEgASgJEgwKBG5hbWUYAiABKAkSOwoFdmlkZW8YAyABKAsyJy5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Db3Vyc2VWaWRlb0gAiAEBEiAKE3VzZXJfdmlkZW9fcG9zaXRpb24YBCABKAVIAYgBAUIICgZfd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17948"></a>
## FND-17948: Full frontend descriptor: chesscom/courses/v1/course_coach.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_coach.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseCoach",
      "field": [
        {
          "name": "avatar",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseCoachAvatar"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 735891.

```text
3VzZXJfdmlkZW9fcG9zaXRpb24YBCABKAVIAYgBAUIICgZfdmlkZW9CFgoUX3VzZXJfdmlkZW9fcG9zaXRpb25iBnByb3RvMw","chesscom/courses/v1/course_coach.proto":"CiZjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9jb2FjaC5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCgtDb3Vyc2VDb2FjaBI9CgZhdmF0YXIYASABKA4yLS5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Db3Vyc2VDb2FjaEF2YXRhcjoHgqYdAwoBAWIGcHJvdG8z","chesscom/courses/v1/course_lesson_player.proto":"Ci5jaGVzc2NvbS9jb3V
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17949"></a>
## FND-17949: Full frontend descriptor: chesscom/courses/v1/course_lesson_player.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_lesson_player.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseLessonPlayer",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "picture",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "is_author",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "oneof_decl": [
        {
          "name": "_picture"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 736143.

```text
0YXIYASABKA4yLS5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Db3Vyc2VDb2FjaEF2YXRhcjoHgqYdAwoBAWIGcHJvdG8z","chesscom/courses/v1/course_lesson_player.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9sZXNzb25fcGxheWVyLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxInwKEkNvdXJzZUxlc3NvblBsYXllchIMCgRuYW1lGAEgASgJEjkKB3BpY3R1cmUYAiABKAsyIy5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5QaWN0dXJlSACIAQESEQoJaXNfYXV0aG9yGAMgASgIQgoKCF9waWN0dXJlYgZwcm90bzM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17950"></a>
## FND-17950: Full frontend descriptor: chesscom/courses/v1/course_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_type.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "CourseType",
      "value": [
        {
          "name": "COURSE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_TYPE_FREE",
          "number": 1
        },
        {
          "name": "COURSE_TYPE_DIAMOND_EXCLUSIVE",
          "number": 2
        },
        {
          "name": "COURSE_TYPE_PAID",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 736466.

```text
NvbS5jb3Vyc2VzX2NvbW1vbi52MS5QaWN0dXJlSACIAQESEQoJaXNfYXV0aG9yGAMgASgIQgoKCF9waWN0dXJlYgZwcm90bzM","chesscom/courses/v1/course_type.proto":"CiVjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV90eXBlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxKngKCkNvdXJzZVR5cGUSGwoXQ09VUlNFX1RZUEVfVU5TUEVDSUZJRUQQABIUChBDT1VSU0VfVFlQRV9GUkVFEAESIQodQ09VUlNFX1RZUEVfRElBTU9ORF9FWENMVVNJVkUQAhIUChBDT1VSU0VfVFlQRV9QQUlEEANiBnByb3RvMw","chesscom/courses/v1/mov
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17951"></a>
## FND-17951: Full frontend descriptor: chesscom/courses/v1/move_trainer.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/move_trainer.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "MoveTrainer",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "picture",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture"
        },
        {
          "name": "chapters",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseChapter"
        },
        {
          "name": "authors",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseAuthor"
        },
        {
          "name": "slug",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "access_right_mode",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.AccessRightMode"
        },
        {
          "name": "course_type",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseType"
        },
        {
          "name": "course_source",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseSource"
        },
        {
          "name": "course_game_aspect",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseGameAspect",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "coach",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoach",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "author_player",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLessonPlayer"
        },
        {
          "name": "learner_player",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLessonPlayer",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_course_game_aspect"
        },
        {
          "name": "_coach"
        },
        {
          "name": "_learner_player"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "MoveTrainerTrainingMode",
      "value": [
        {
          "name": "MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MOVE_TRAINER_TRAINING_MODE_LEARN",
          "number": 1
        },
        {
          "name": "MOVE_TRAINER_TRAINING_MODE_REVIEW",
          "number": 2
        }
      ]
    },
    {
      "name": "MoveTrainerTrainingResult",
      "value": [
        {
          "name": "MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MOVE_TRAINER_TRAINING_RESULT_PASS",
          "number": 1
        },
        {
          "name": "MOVE_TRAINER_TRAINING_RESULT_FAILED",
          "number": 2
        }
      ]
    },
    {
      "name": "AccessRightMode",
      "value": [
        {
          "name": "ACCESS_RIGHT_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ACCESS_RIGHT_MODE_FULL",
          "number": 1
        },
        {
          "name": "ACCESS_RIGHT_MODE_PREVIEW",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 736763.

```text
V9GUkVFEAESIQodQ09VUlNFX1RZUEVfRElBTU9ORF9FWENMVVNJVkUQAhIUChBDT1VSU0VfVFlQRV9QQUlEEANiBnByb3RvMw","chesscom/courses/v1/move_trainer.proto":"CiZjaGVzc2NvbS9jb3Vyc2VzL3YxL21vdmVfdHJhaW5lci5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSLMBQoLTW92ZVRyYWluZXISCgoCaWQYASABKAkSDAoEbmFtZRgCIAEoCRI0CgdwaWN0dXJlGAMgASgLMiMuY2hlc3Njb20uY291cnNlc19jb21tb24udjEuUGljdHVyZRI0CghjaGFwdGVycxgEIAMoCzIiLmNoZXNzY29tLmNvdXJzZXMudjEuQ291cnNlQ2hhcHR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17952"></a>
## FND-17952: Full frontend descriptor: chesscom/courses/v1/nag.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/nag.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "Nag",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "nag_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 738415.

```text
GSUVEEAASGgoWQUNDRVNTX1JJR0hUX01PREVfRlVMTBABEh0KGUFDQ0VTU19SSUdIVF9NT0RFX1BSRVZJRVcQAmIGcHJvdG8z","chesscom/courses/v1/nag.proto":"Ch1jaGVzc2NvbS9jb3Vyc2VzL3YxL25hZy5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSIjCgNOYWcSDAoEdHlwZRgBIAEoCRIOCgZuYWdfaWQYAiABKAViBnByb3RvMw","chesscom/courses/v1/course_position.proto":"CiljaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wb3NpdGlvbi5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSLKAQoOQ291cnNlUG9zaXRpb24
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17953"></a>
## FND-17953: Full frontend descriptor: chesscom/courses/v1/course_position.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_position.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CoursePosition",
      "field": [
        {
          "name": "fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "highlights",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseDrawingSquare"
        },
        {
          "name": "arrows",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseDrawingArrow"
        },
        {
          "name": "nags",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.Nag"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 738580.

```text
y5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSIjCgNOYWcSDAoEdHlwZRgBIAEoCRIOCgZuYWdfaWQYAiABKAViBnByb3RvMw","chesscom/courses/v1/course_position.proto":"CiljaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wb3NpdGlvbi5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSLKAQoOQ291cnNlUG9zaXRpb24SCwoDZmVuGAEgASgJEkMKCmhpZ2hsaWdodHMYAiADKAsyLy5jaGVzc2NvbS5jb3Vyc2VzX2NvbW1vbi52MS5Db3Vyc2VEcmF3aW5nU3F1YXJlEj4KBmFycm93cxgDIAMoCzIuLmNoZXNzY29tLmNvdXJzZXNfY29tbW9u
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17954"></a>
## FND-17954: Full frontend descriptor: chesscom/courses/v1/variation_access_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/variation_access_type.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "VariationAccessType",
      "value": [
        {
          "name": "VARIATION_ACCESS_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "VARIATION_ACCESS_TYPE_PREVIEWABLE",
          "number": 1
        },
        {
          "name": "VARIATION_ACCESS_TYPE_LOCKED",
          "number": 2
        },
        {
          "name": "VARIATION_ACCESS_TYPE_FULL_ACCESS",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 738997.

```text
W9uLnYxLkNvdXJzZURyYXdpbmdBcnJvdxImCgRuYWdzGAQgAygLMhguY2hlc3Njb20uY291cnNlcy52MS5OYWdiBnByb3RvMw","chesscom/courses/v1/variation_access_type.proto":"Ci9jaGVzc2NvbS9jb3Vyc2VzL3YxL3ZhcmlhdGlvbl9hY2Nlc3NfdHlwZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSqsAQoTVmFyaWF0aW9uQWNjZXNzVHlwZRIlCiFWQVJJQVRJT05fQUNDRVNTX1RZUEVfVU5TUEVDSUZJRUQQABIlCiFWQVJJQVRJT05fQUNDRVNTX1RZUEVfUFJFVklFV0FCTEUQARIgChxWQVJJQVRJT05fQUNDRVNTX1RZUEVfTE9DS0
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17955"></a>
## FND-17955: Full frontend descriptor: chesscom/courses/v1/course_variation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_variation.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseVariation",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "starting_position",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CoursePosition"
        },
        {
          "name": "move_trainer_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "chapter_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseVariationType"
        },
        {
          "name": "is_learned",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_paused",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "video_start",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "video_end",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "access_type",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.VariationAccessType"
        },
        {
          "name": "learning_level",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "first_learned_at",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "last_reviewed_at",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "next_review_at",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "move_count",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "preview_position",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CoursePosition",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "learner_color",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "slug",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "oneof_decl": [
        {
          "name": "_video_start"
        },
        {
          "name": "_video_end"
        },
        {
          "name": "_learning_level"
        },
        {
          "name": "_first_learned_at"
        },
        {
          "name": "_last_reviewed_at"
        },
        {
          "name": "_next_review_at"
        },
        {
          "name": "_preview_position"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 739388.

```text
VRJT05fQUNDRVNTX1RZUEVfTE9DS0VEEAISJQohVkFSSUFUSU9OX0FDQ0VTU19UWVBFX0ZVTExfQUNDRVNTEANiBnByb3RvMw","chesscom/courses/v1/course_variation.proto":"CipjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV92YXJpYXRpb24ucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEi1QYKD0NvdXJzZVZhcmlhdGlvbhIKCgJpZBgBIAEoCRIMCgRuYW1lGAIgASgJEj4KEXN0YXJ0aW5nX3Bvc2l0aW9uGAMgASgLMiMuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VQb3NpdGlvbhIXCg9tb3ZlX3RyYWluZXJfaWQYBCABKAkSEgoKY2h
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17956"></a>
## FND-17956: Full frontend descriptor: chesscom/courses/v1/course_learning_session.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_learning_session.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseLearningSession",
      "field": [
        {
          "name": "lessons_headers",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVariation"
        },
        {
          "name": "reviews_headers",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVariation"
        },
        {
          "name": "move_trainers",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.MoveTrainer"
        },
        {
          "name": "last_learned_variation_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_last_learned_variation_id"
        }
      ]
    },
    {
      "name": "CourseLearningSessionStats",
      "field": [
        {
          "name": "total_learning_session_variations_amount",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_learning_session_time_seconds",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_learning_session_accuracy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "current_training_variations_amount",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "current_training_time_seconds",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_learning_session_variations_by_type",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVariationTypeCount"
        }
      ]
    },
    {
      "name": "CourseLearningSessionProgress",
      "field": [
        {
          "name": "total_learning_session_variations_by_type",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVariationTypeCount"
        }
      ]
    },
    {
      "name": "CourseVariationTypeCount",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseVariationType"
        },
        {
          "name": "count",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 740675.

```text
RfYXRCEwoRX2xhc3RfcmV2aWV3ZWRfYXRCEQoPX25leHRfcmV2aWV3X2F0QhMKEV9wcmV2aWV3X3Bvc2l0aW9uYgZwcm90bzM","chesscom/courses/v1/course_learning_session.proto":"CjFjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9sZWFybmluZ19zZXNzaW9uLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIpQCChVDb3Vyc2VMZWFybmluZ1Nlc3Npb24SPQoPbGVzc29uc19oZWFkZXJzGAEgAygLMiQuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VWYXJpYXRpb24SPQoPcmV2aWV3c19oZWFkZXJzGAIgAygLMiQuY2hlc3Njb20uY291
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17957"></a>
## FND-17957: Full frontend descriptor: chesscom/courses/v1/course_variation_ply.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_variation_ply.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseVariationPly",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_number",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "san",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "position",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CoursePosition"
        },
        {
          "name": "color",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "is_learnable",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "alternative_moves",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.CourseVariationAlternativeMove"
        },
        {
          "name": "pre_comment",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "post_comment",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "ply_index",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "coach_speech",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCoachSpeech",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_pre_comment"
        },
        {
          "name": "_post_comment"
        },
        {
          "name": "_coach_speech"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 741990.

```text
OMi8uY2hlc3Njb20uY291cnNlc19jb21tb24udjEuQ291cnNlVmFyaWF0aW9uVHlwZRINCgVjb3VudBgCIAEoBWIGcHJvdG8z","chesscom/courses/v1/course_variation_ply.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV92YXJpYXRpb25fcGx5LnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIswDChJDb3Vyc2VWYXJpYXRpb25QbHkSCgoCaWQYASABKAkSEwoLbW92ZV9udW1iZXIYAiABKAUSCwoDc2FuGAMgASgJEjUKCHBvc2l0aW9uGAQgASgLMiMuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2VQb3NpdGlvbhInCgVjb2xvchg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17958"></a>
## FND-17958: Full frontend descriptor: chesscom/courses/v1/course_lesson.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_lesson.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseLesson",
      "field": [
        {
          "name": "variation",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVariation"
        },
        {
          "name": "white_player",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLessonPlayer"
        },
        {
          "name": "black_player",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLessonPlayer"
        },
        {
          "name": "plies",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVariationPly"
        },
        {
          "name": "settings",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseConfiguration"
        },
        {
          "name": "video_section",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Range",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "user_video_position",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "first_learnable_move_color",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "initial_ply_offset",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "oneof_decl": [
        {
          "name": "_video_section"
        },
        {
          "name": "_user_video_position"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 742762.

```text
vYWNoU3BlZWNoSAKIAQFCDgoMX3ByZV9jb21tZW50Qg8KDV9wb3N0X2NvbW1lbnRCDwoNX2NvYWNoX3NwZWVjaGIGcHJvdG8z","chesscom/courses/v1/course_lesson.proto":"CidjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9sZXNzb24ucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiogQKDENvdXJzZUxlc3NvbhI3Cgl2YXJpYXRpb24YASABKAsyJC5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZVZhcmlhdGlvbhI9Cgx3aGl0ZV9wbGF5ZXIYAiABKAsyJy5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZUxlc3NvblBsYXllchI9CgxibGFja1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17959"></a>
## FND-17959: Full frontend descriptor: chesscom/courses/v1/course_video_playback.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_video_playback.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CourseVideoPlayback",
      "field": [
        {
          "name": "hls_url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "files",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVideoPlaybackFile"
        },
        {
          "name": "text_tracks",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVideoTextTrack"
        },
        {
          "name": "thumbnail_url",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "duration_seconds",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_hls_url"
        },
        {
          "name": "_thumbnail_url"
        },
        {
          "name": "_duration_seconds"
        }
      ]
    },
    {
      "name": "CourseVideoPlaybackFile",
      "field": [
        {
          "name": "url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "width",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "height",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "file_size",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_file_size"
        }
      ]
    },
    {
      "name": "CourseVideoTextTrack",
      "field": [
        {
          "name": "language",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "label",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "url",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_label"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 743633.

```text
ml0aWFsX3BseV9vZmZzZXQYCSABKAVCEAoOX3ZpZGVvX3NlY3Rpb25CFgoUX3VzZXJfdmlkZW9fcG9zaXRpb25iBnByb3RvMw","chesscom/courses/v1/course_video_playback.proto":"Ci9jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV92aWRlb19wbGF5YmFjay5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKfAgoTQ291cnNlVmlkZW9QbGF5YmFjaxIUCgdobHNfdXJsGAEgASgJSACIAQESOwoFZmlsZXMYAiADKAsyLC5jaGVzc2NvbS5jb3Vyc2VzLnYxLkNvdXJzZVZpZGVvUGxheWJhY2tGaWxlEj4KC3RleHRfdHJhY2tzGAMgAygLMikuY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17960"></a>
## FND-17960: Full frontend descriptor: chesscom/courses/v1/courses_training_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_training_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetCourseLearningSessionRequest",
      "field": [
        {
          "name": "context_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "learning_session_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "course_slug",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_learning_session_id"
        },
        {
          "name": "_course_slug"
        }
      ]
    },
    {
      "name": "GetCourseLearningSessionResponse",
      "field": [
        {
          "name": "learning_session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLearningSession"
        },
        {
          "name": "learning_session_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "progress",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLearningSessionProgress"
        }
      ]
    },
    {
      "name": "GetCourseTrainingForLearningRequest",
      "field": [
        {
          "name": "variation_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "learning_session_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseTrainingForLearningResponse",
      "field": [
        {
          "name": "lesson",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLesson"
        },
        {
          "name": "training_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseTrainingForReviewingRequest",
      "field": [
        {
          "name": "variation_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "learning_session_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseTrainingForReviewingResponse",
      "field": [
        {
          "name": "lesson",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLesson"
        },
        {
          "name": "training_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "StoreCourseTrainingProgressRequest",
      "field": [
        {
          "name": "ply_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "san",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "training_mode",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.MoveTrainerTrainingMode"
        },
        {
          "name": "learning_session_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "training_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "StoreCourseTrainingProgressResponse"
    },
    {
      "name": "StoreCourseVideoProgressRequest",
      "field": [
        {
          "name": "video_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "learning_session_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "position_in_seconds",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "watched_seconds",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    },
    {
      "name": "StoreCourseVideoProgressResponse"
    },
    {
      "name": "GetCourseVideoPlaybackRequest",
      "field": [
        {
          "name": "video_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseVideoPlaybackResponse",
      "field": [
        {
          "name": "playback",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseVideoPlayback"
        }
      ]
    },
    {
      "name": "FinalizeCourseTrainingRequest",
      "field": [
        {
          "name": "learning_session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "training_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "FinalizeCourseTrainingResponse",
      "field": [
        {
          "name": "stats",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLearningSessionStats"
        }
      ]
    },
    {
      "name": "GetCourseStatsRequest",
      "field": [
        {
          "name": "context_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseStatsResponse",
      "field": [
        {
          "name": "stats",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseLearningSessionStats"
        }
      ]
    },
    {
      "name": "GetCourseConfigurationRequest",
      "field": [
        {
          "name": "context_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_slug",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_course_slug"
        }
      ]
    },
    {
      "name": "GetCourseConfigurationResponse",
      "field": [
        {
          "name": "configuration",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseConfiguration"
        },
        {
          "name": "available_languages",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Language"
        }
      ]
    },
    {
      "name": "StoreCourseConfigurationRequest",
      "field": [
        {
          "name": "context_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "configuration",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseConfiguration"
        }
      ]
    },
    {
      "name": "StoreCourseConfigurationResponse"
    },
    {
      "name": "DeleteCourseProgressRequest",
      "field": [
        {
          "name": "course_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "DeleteCourseProgressResponse"
    },
    {
      "name": "ClaimPreviewRequest",
      "field": [
        {
          "name": "variation_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ClaimPreviewResponse"
    },
    {
      "name": "SetVariationPausedRequest",
      "field": [
        {
          "name": "variation_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetVariationPausedResponse"
    },
    {
      "name": "SetVariationUnpausedRequest",
      "field": [
        {
          "name": "variation_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetVariationUnpausedResponse"
    }
  ],
  "service": [
    {
      "name": "CoursesTrainingService",
      "method": [
        {
          "name": "GetCourseLearningSession",
          "input_type": ".chesscom.courses.v1.GetCourseLearningSessionRequest",
          "output_type": ".chesscom.courses.v1.GetCourseLearningSessionResponse"
        },
        {
          "name": "GetCourseTrainingForLearning",
          "input_type": ".chesscom.courses.v1.GetCourseTrainingForLearningRequest",
          "output_type": ".chesscom.courses.v1.GetCourseTrainingForLearningResponse"
        },
        {
          "name": "GetCourseTrainingForReviewing",
          "input_type": ".chesscom.courses.v1.GetCourseTrainingForReviewingRequest",
          "output_type": ".chesscom.courses.v1.GetCourseTrainingForReviewingResponse"
        },
        {
          "name": "StoreCourseTrainingProgress",
          "input_type": ".chesscom.courses.v1.StoreCourseTrainingProgressRequest",
          "output_type": ".chesscom.courses.v1.StoreCourseTrainingProgressResponse"
        },
        {
          "name": "StoreCourseVideoProgress",
          "input_type": ".chesscom.courses.v1.StoreCourseVideoProgressRequest",
          "output_type": ".chesscom.courses.v1.StoreCourseVideoProgressResponse"
        },
        {
          "name": "GetCourseVideoPlayback",
          "input_type": ".chesscom.courses.v1.GetCourseVideoPlaybackRequest",
          "output_type": ".chesscom.courses.v1.GetCourseVideoPlaybackResponse"
        },
        {
          "name": "FinalizeCourseTraining",
          "input_type": ".chesscom.courses.v1.FinalizeCourseTrainingRequest",
          "output_type": ".chesscom.courses.v1.FinalizeCourseTrainingResponse"
        },
        {
          "name": "GetCourseStats",
          "input_type": ".chesscom.courses.v1.GetCourseStatsRequest",
          "output_type": ".chesscom.courses.v1.GetCourseStatsResponse"
        },
        {
          "name": "GetCourseConfiguration",
          "input_type": ".chesscom.courses.v1.GetCourseConfigurationRequest",
          "output_type": ".chesscom.courses.v1.GetCourseConfigurationResponse"
        },
        {
          "name": "StoreCourseConfiguration",
          "input_type": ".chesscom.courses.v1.StoreCourseConfigurationRequest",
          "output_type": ".chesscom.courses.v1.StoreCourseConfigurationResponse"
        },
        {
          "name": "DeleteCourseProgress",
          "input_type": ".chesscom.courses.v1.DeleteCourseProgressRequest",
          "output_type": ".chesscom.courses.v1.DeleteCourseProgressResponse"
        },
        {
          "name": "ClaimPreview",
          "input_type": ".chesscom.courses.v1.ClaimPreviewRequest",
          "output_type": ".chesscom.courses.v1.ClaimPreviewResponse"
        },
        {
          "name": "SetVariationPaused",
          "input_type": ".chesscom.courses.v1.SetVariationPausedRequest",
          "output_type": ".chesscom.courses.v1.SetVariationPausedResponse"
        },
        {
          "name": "SetVariationUnpaused",
          "input_type": ".chesscom.courses.v1.SetVariationUnpausedRequest",
          "output_type": ".chesscom.courses.v1.SetVariationUnpausedResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17975"></a>
## FND-17975: Full frontend descriptor: chesscom/courses/v1/course_product_by_sku_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_product_by_sku_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetCourseProductBySKURequest",
      "field": [
        {
          "name": "sku",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "locale",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_locale"
        }
      ]
    },
    {
      "name": "GetCourseProductBySKUResponse",
      "field": [
        {
          "name": "product",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "GetCourseProductBySKUService",
      "method": [
        {
          "name": "GetCourseProductBySKU",
          "input_type": ".chesscom.courses.v1.GetCourseProductBySKURequest",
          "output_type": ".chesscom.courses.v1.GetCourseProductBySKUResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 750411.

```text
EuU2V0VmFyaWF0aW9uVW5wYXVzZWRSZXNwb25zZUIhyrcsHQoEL3JwYxITEhFjb3Vyc2VzLmNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/courses/v1/course_product_by_sku_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2J5X3NrdV9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIksKHEdldENvdXJzZVByb2R1Y3RCeVNLVVJlcXVlc3QSCwoDc2t1GAEgASgJEhMKBmxvY2FsZRgCIAEoCUgAiAEBQgkKB19sb2NhbGUiVAodR2V0Q291cnNlUHJvZHVjdEJ5U0tVUmVzcG9uc2USMwoHcHJvZH
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17977"></a>
## FND-17977: Full frontend descriptor: chesscom/courses/v1/user_flag.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/user_flag.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "UserFlag",
      "value": [
        {
          "name": "USER_FLAG_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_FLAG_HAS_EXCLUSIVE_COURSES",
          "number": 1
        },
        {
          "name": "USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT",
          "number": 2
        },
        {
          "name": "USER_FLAG_HAS_UNLIMITED_PREVIEWS",
          "number": 3
        },
        {
          "name": "USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET",
          "number": 4
        },
        {
          "name": "USER_FLAG_HAS_TUTORIAL",
          "number": 5
        },
        {
          "name": "USER_FLAG_HAS_CLOSED_WELCOME_WIDGET",
          "number": 6
        },
        {
          "name": "USER_FLAG_OWNS_A_COURSE",
          "number": 7
        },
        {
          "name": "USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT",
          "number": 8
        },
        {
          "name": "USER_FLAG_HAS_PREVIEW_COURSES",
          "number": 9
        },
        {
          "name": "USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR",
          "number": 10
        },
        {
          "name": "USER_FLAG_COACH_DEFAULT_OFF",
          "number": 11
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 751066.

```text
kdldENvdXJzZVByb2R1Y3RCeVNLVVJlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/user_flag.proto":"CiNjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfZmxhZy5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSrMAwoIVXNlckZsYWcSGQoVVVNFUl9GTEFHX1VOU1BFQ0lGSUVEEAASIwofVVNFUl9GTEFHX0hBU19FWENMVVNJVkVfQ09VUlNFUxABEisKJ1VTRVJfRkxBR19IQVNfR0xPQkFMX1NUQUNLQUJMRV9ESVNDT1VOVBACEiQKIFVTRVJfRkxBR19IQVNfVU5MSU1JVEVEX1BSRV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17978"></a>
## FND-17978: Full frontend descriptor: chesscom/courses/v1/configurable_user_flag_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/configurable_user_flag_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "SetConfigurableUserFlagRequest",
      "field": [
        {
          "name": "user_flag",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.UserFlag"
        }
      ]
    },
    {
      "name": "SetConfigurableUserFlagResponse"
    }
  ],
  "service": [
    {
      "name": "CoursesConfigurableUserFlagService",
      "method": [
        {
          "name": "SetConfigurableUserFlag",
          "input_type": ".chesscom.courses.v1.SetConfigurableUserFlagRequest",
          "output_type": ".chesscom.courses.v1.SetConfigurableUserFlagResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 751813.

```text
kxBR19IQVNfU0tJUFBFRF9GVFVFX1NFTEVDVE9SEAoSHwobVVNFUl9GTEFHX0NPQUNIX0RFRkFVTFRfT0ZGEAtiBnByb3RvMw","chesscom/courses/v1/configurable_user_flag_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvbmZpZ3VyYWJsZV91c2VyX2ZsYWdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJSCh5TZXRDb25maWd1cmFibGVVc2VyRmxhZ1JlcXVlc3QSMAoJdXNlcl9mbGFnGAEgASgOMh0uY2hlc3Njb20uY291cnNlcy52MS5Vc2VyRmxhZyIhCh9TZXRDb25maWd1cmFibGVVc2VyRmxhZ1Jlc3Bvb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17980"></a>
## FND-17980: Full frontend descriptor: chesscom/courses/v1/courses_previews_information_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_previews_information_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetPreviewsInformationRequest"
    },
    {
      "name": "GetPreviewsInformationResponse",
      "field": [
        {
          "name": "used_amount",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_amount",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "variation_resets_in_days_amount",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "period",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "max_previews_per_course",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "oneof_decl": [
        {
          "name": "_total_amount"
        },
        {
          "name": "_variation_resets_in_days_amount"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "CoursesPreviewsInformationService",
      "method": [
        {
          "name": "GetPreviewsInformation",
          "input_type": ".chesscom.courses.v1.GetPreviewsInformationRequest",
          "output_type": ".chesscom.courses.v1.GetPreviewsInformationResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 752429.

```text
XRDb25maWd1cmFibGVVc2VyRmxhZ1Jlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/courses_previews_information_service.proto":"Cj5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfcHJldmlld3NfaW5mb3JtYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSIfCh1HZXRQcmV2aWV3c0luZm9ybWF0aW9uUmVxdWVzdCLkAQoeR2V0UHJldmlld3NJbmZvcm1hdGlvblJlc3BvbnNlEhMKC3VzZWRfYW1vdW50GAEgASgFEhkKDHRvdGFsX2Ftb3VudBg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17982"></a>
## FND-17982: Full frontend descriptor: chesscom/courses/v1/goal_step.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/goal_step.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GoalStep",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "completed_amount",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_amount",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753247.

```text
2V0UHJldmlld3NJbmZvcm1hdGlvblJlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/goal_step.proto":"CiNjaGVzc2NvbS9jb3Vyc2VzL3YxL2dvYWxfc3RlcC5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJICghHb2FsU3RlcBIMCgR0eXBlGAEgASgJEhgKEGNvbXBsZXRlZF9hbW91bnQYAiABKAUSFAoMdG90YWxfYW1vdW50GAMgASgFYgZwcm90bzM","chesscom/courses/v1/user_goal.proto":"CiNjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfZ29hbC5wcm90bxITY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17983"></a>
## FND-17983: Full frontend descriptor: chesscom/courses/v1/user_goal.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/user_goal.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "UserGoal",
      "field": [
        {
          "name": "goal_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.GoalType"
        },
        {
          "name": "steps",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.GoalStep"
        },
        {
          "name": "reward",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.Reward"
        },
        {
          "name": "achieved_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "reward_claimed_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753475.

```text
RlcBIMCgR0eXBlGAEgASgJEhgKEGNvbXBsZXRlZF9hbW91bnQYAiABKAUSFAoMdG90YWxfYW1vdW50GAMgASgFYgZwcm90bzM","chesscom/courses/v1/user_goal.proto":"CiNjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfZ29hbC5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSL/AQoIVXNlckdvYWwSMAoJZ29hbF90eXBlGAEgASgOMh0uY2hlc3Njb20uY291cnNlcy52MS5Hb2FsVHlwZRIsCgVzdGVwcxgCIAMoCzIdLmNoZXNzY29tLmNvdXJzZXMudjEuR29hbFN0ZXASKwoGcmV3YXJkGAMgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5SZXdhcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17984"></a>
## FND-17984: Full frontend descriptor: chesscom/courses/v1/courses_authentication_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_authentication_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "AuthenticateForCoursesWithCookieRequest",
      "field": [
        {
          "name": "provider_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "cookie_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "AuthenticateForCoursesWithCookieResponse",
      "field": [
        {
          "name": "access_token",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "refresh_token",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "expires_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "expires_in_seconds",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        }
      ]
    },
    {
      "name": "GetOAuthURLForCoursesRequest",
      "field": [
        {
          "name": "provider_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "redirect_uri",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetOAuthURLForCoursesResponse",
      "field": [
        {
          "name": "url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "AuthenticateForCoursesRequest",
      "field": [
        {
          "name": "provider_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "redirect_uri",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "state",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "AuthenticateForCoursesResponse",
      "field": [
        {
          "name": "access_token",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "refresh_token",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "expires_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "expires_in_seconds",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        }
      ]
    },
    {
      "name": "RefreshTokenForCoursesRequest",
      "field": [
        {
          "name": "refresh_token",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "RefreshTokenForCoursesResponse",
      "field": [
        {
          "name": "access_token",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "refresh_token",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "expires_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "expires_in_seconds",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        }
      ],
      "oneof_decl": [
        {
          "name": "_refresh_token"
        }
      ]
    },
    {
      "name": "GetUserInfoForCoursesRequest"
    },
    {
      "name": "GetUserInfoForCoursesResponse",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "username",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "picture",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Picture"
        },
        {
          "name": "provider",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "flags",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.UserFlag"
        },
        {
          "name": "user_goal",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.UserGoal"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "CoursesAuthenticationService",
      "method": [
        {
          "name": "AuthenticateForCoursesWithCookie",
          "input_type": ".chesscom.courses.v1.AuthenticateForCoursesWithCookieRequest",
          "output_type": ".chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse"
        },
        {
          "name": "GetOAuthURLForCourses",
          "input_type": ".chesscom.courses.v1.GetOAuthURLForCoursesRequest",
          "output_type": ".chesscom.courses.v1.GetOAuthURLForCoursesResponse"
        },
        {
          "name": "AuthenticateForCourses",
          "input_type": ".chesscom.courses.v1.AuthenticateForCoursesRequest",
          "output_type": ".chesscom.courses.v1.AuthenticateForCoursesResponse"
        },
        {
          "name": "RefreshTokenForCourses",
          "input_type": ".chesscom.courses.v1.RefreshTokenForCoursesRequest",
          "output_type": ".chesscom.courses.v1.RefreshTokenForCoursesResponse"
        },
        {
          "name": "GetUserInfoForCourses",
          "input_type": ".chesscom.courses.v1.GetUserInfoForCoursesRequest",
          "output_type": ".chesscom.courses.v1.GetUserInfoForCoursesResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753948.

```text
uVGltZXN0YW1wEjUKEXJld2FyZF9jbGFpbWVkX2F0GAUgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses/v1/courses_authentication_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfYXV0aGVudGljYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCidBdXRoZW50aWNhdGVGb3JDb3Vyc2VzV2l0aENvb2tpZVJlcXVlc3QSFQoNcHJvdmlkZXJfbmFtZRgBIAEoCRITCgtjb29raWVfbmFtZRgCIAEoCSKjAQooQXV0aGVudGljYXRlRm9yQ291cnNlc1dpd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17990"></a>
## FND-17990: Full frontend descriptor: chesscom/courses/v1/courses_has_user_access_to_sku_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_has_user_access_to_sku_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetHasUserAccessToSkuRequest",
      "field": [
        {
          "name": "chesscom_user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sku",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetHasUserAccessToSkuResponse",
      "field": [
        {
          "name": "has_access",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "GetHasUserAccessToSkuService",
      "method": [
        {
          "name": "GetHasUserAccessToSku",
          "input_type": ".chesscom.courses.v1.GetHasUserAccessToSkuRequest",
          "output_type": ".chesscom.courses.v1.GetHasUserAccessToSkuResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 756644.

```text
kdldFVzZXJJbmZvRm9yQ291cnNlc1Jlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/courses_has_user_access_to_sku_service.proto":"CkBjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfaGFzX3VzZXJfYWNjZXNzX3RvX3NrdV9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIkUKHEdldEhhc1VzZXJBY2Nlc3NUb1NrdVJlcXVlc3QSGAoQY2hlc3Njb21fdXNlcl9pZBgBIAEoCRILCgNza3UYAiABKAkiMwodR2V0SGFzVXNlckFjY2Vzc1RvU2t1UmVzcG9uc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17992"></a>
## FND-17992: Full frontend descriptor: chesscom/courses/v1/courses_shop_pagination.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_shop_pagination.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "CoursesShopPagination",
      "field": [
        {
          "name": "limit",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "offset",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 757268.

```text
kdldEhhc1VzZXJBY2Nlc3NUb1NrdVJlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/courses_shop_pagination.proto":"CjFjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfc2hvcF9wYWdpbmF0aW9uLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIjYKFUNvdXJzZXNTaG9wUGFnaW5hdGlvbhINCgVsaW1pdBgBIAEoBRIOCgZvZmZzZXQYAiABKAViBnByb3RvMw","chesscom/courses/v1/course_tag.proto":"CiRjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV90YWcu
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17993"></a>
## FND-17993: Full frontend descriptor: chesscom/courses/v1/course_tag.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/course_tag.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "CourseTag",
      "value": [
        {
          "name": "COURSE_TAG_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COURSE_TAG_RECOMMENDED",
          "number": 1
        },
        {
          "name": "COURSE_TAG_BEST_SELLER",
          "number": 2
        },
        {
          "name": "COURSE_TAG_ON_SALE",
          "number": 3
        },
        {
          "name": "COURSE_TAG_VIDEO",
          "number": 4
        },
        {
          "name": "COURSE_TAG_DIAMOND_EXCLUSIVE",
          "number": 5
        },
        {
          "name": "COURSE_TAG_FREE",
          "number": 6
        },
        {
          "name": "COURSE_TAG_TOP_PLAYERS",
          "number": 7
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 757505.

```text
3Vyc2VzLnYxIjYKFUNvdXJzZXNTaG9wUGFnaW5hdGlvbhINCgVsaW1pdBgBIAEoBRIOCgZvZmZzZXQYAiABKAViBnByb3RvMw","chesscom/courses/v1/course_tag.proto":"CiRjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV90YWcucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEq4AEKCUNvdXJzZVRhZxIaChZDT1VSU0VfVEFHX1VOU1BFQ0lGSUVEEAASGgoWQ09VUlNFX1RBR19SRUNPTU1FTkRFRBABEhoKFkNPVVJTRV9UQUdfQkVTVF9TRUxMRVIQAhIWChJDT1VSU0VfVEFHX09OX1NBTEUQAxIUChBDT1VSU0VfVEFHX1ZJREVPEAQSIAocQ09VU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17994"></a>
## FND-17994: Full frontend descriptor: chesscom/courses/v1/price_range.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/price_range.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "PriceRange",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "with_video",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 757939.

```text
NT05EX0VYQ0xVU0lWRRAFEhMKD0NPVVJTRV9UQUdfRlJFRRAGEhoKFkNPVVJTRV9UQUdfVE9QX1BMQVlFUlMQB2IGcHJvdG8z","chesscom/courses/v1/price_range.proto":"CiVjaGVzc2NvbS9jb3Vyc2VzL3YxL3ByaWNlX3JhbmdlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIjoKClByaWNlUmFuZ2USDAoEZnJvbRgBIAEoBRIKCgJ0bxgCIAEoBRISCgp3aXRoX3ZpZGVvGAMgASgIYgZwcm90bzM","chesscom/courses/v1/product_list_retrieve_mode.proto":"CjRjaGVzc2NvbS9jb3Vyc2VzL3YxL3Byb2R1Y3RfbGlzdF9yZXR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17995"></a>
## FND-17995: Full frontend descriptor: chesscom/courses/v1/product_list_retrieve_mode.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/product_list_retrieve_mode.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "ProductListRetrieveMode",
      "value": [
        {
          "name": "PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PRODUCT_LIST_RETRIEVE_MODE_ALL",
          "number": 1
        },
        {
          "name": "PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 758153.

```text
VzLnYxIjoKClByaWNlUmFuZ2USDAoEZnJvbRgBIAEoBRIKCgJ0bxgCIAEoBRISCgp3aXRoX3ZpZGVvGAMgASgIYgZwcm90bzM","chesscom/courses/v1/product_list_retrieve_mode.proto":"CjRjaGVzc2NvbS9jb3Vyc2VzL3YxL3Byb2R1Y3RfbGlzdF9yZXRyaWV2ZV9tb2RlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxKpcBChdQcm9kdWN0TGlzdFJldHJpZXZlTW9kZRIqCiZQUk9EVUNUX0xJU1RfUkVUUklFVkVfTU9ERV9VTlNQRUNJRklFRBAAEiIKHlBST0RVQ1RfTElTVF9SRVRSSUVWRV9NT0RFX0FMTBABEiwKKFBST0RVQ1RfTElTV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17996"></a>
## FND-17996: Full frontend descriptor: chesscom/courses/v1/shop_sort_option.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/shop_sort_option.proto",
  "package": "chesscom.courses.v1",
  "enum_type": [
    {
      "name": "ShopSortOption",
      "value": [
        {
          "name": "SHOP_SORT_OPTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHOP_SORT_OPTION_PRICE_ASC",
          "number": 1
        },
        {
          "name": "SHOP_SORT_OPTION_PRICE_DESC",
          "number": 2
        },
        {
          "name": "SHOP_SORT_OPTION_VARIATIONS_DESC",
          "number": 3
        },
        {
          "name": "SHOP_SORT_OPTION_RELEASE_DATE_DESC",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 758527.

```text
SRVRSSUVWRV9NT0RFX0FMTBABEiwKKFBST0RVQ1RfTElTVF9SRVRSSUVWRV9NT0RFX1BST0RVQ1RfQ09VTlQQAmIGcHJvdG8z","chesscom/courses/v1/shop_sort_option.proto":"CipjaGVzc2NvbS9jb3Vyc2VzL3YxL3Nob3Bfc29ydF9vcHRpb24ucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEqwQEKDlNob3BTb3J0T3B0aW9uEiAKHFNIT1BfU09SVF9PUFRJT05fVU5TUEVDSUZJRUQQABIeChpTSE9QX1NPUlRfT1BUSU9OX1BSSUNFX0FTQxABEh8KG1NIT1BfU09SVF9PUFRJT05fUFJJQ0VfREVTQxACEiQKIFNIT1BfU09SVF9PUFRJT05fVkF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17997"></a>
## FND-17997: Full frontend descriptor: chesscom/courses/v1/courses_shop_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1/courses_shop_service.proto",
  "package": "chesscom.courses.v1",
  "message_type": [
    {
      "name": "GetCourseProductListRequest",
      "field": [
        {
          "name": "pagination",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CoursesShopPagination",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "search_query",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "game_aspects",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses_common.v1.CourseGameAspectType"
        },
        {
          "name": "elo_ranges",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Range"
        },
        {
          "name": "color",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "tags",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.CourseTag"
        },
        {
          "name": "country_code",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "price_range_in_cents",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses_common.v1.Range",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "exclude_owned_courses",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "user_rating",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "retrieve_mode",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.ProductListRetrieveMode",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "price_range",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.PriceRange",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "fen",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "course_custom_tags",
          "number": 14,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseCustomTag"
        },
        {
          "name": "sort",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.courses.v1.ShopSortOption",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "include_only_owned_courses",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 10,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_pagination"
        },
        {
          "name": "_search_query"
        },
        {
          "name": "_color"
        },
        {
          "name": "_price_range_in_cents"
        },
        {
          "name": "_exclude_owned_courses"
        },
        {
          "name": "_user_rating"
        },
        {
          "name": "_retrieve_mode"
        },
        {
          "name": "_price_range"
        },
        {
          "name": "_fen"
        },
        {
          "name": "_sort"
        },
        {
          "name": "_include_only_owned_courses"
        }
      ]
    },
    {
      "name": "GetCourseProductListResponse",
      "field": [
        {
          "name": "total",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "product_list",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct"
        }
      ]
    },
    {
      "name": "GetShopMetadataRequest",
      "field": [
        {
          "name": "country_code",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetShopMetadataResponse",
      "field": [
        {
          "name": "number_of_courses_on_sale",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "max_price",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "CoursesShopService",
      "method": [
        {
          "name": "GetCourseProductList",
          "input_type": ".chesscom.courses.v1.GetCourseProductListRequest",
          "output_type": ".chesscom.courses.v1.GetCourseProductListResponse"
        },
        {
          "name": "GetShopMetadata",
          "input_type": ".chesscom.courses.v1.GetShopMetadataRequest",
          "output_type": ".chesscom.courses.v1.GetShopMetadataResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 758934.

```text
9PUFRJT05fVkFSSUFUSU9OU19ERVNDEAMSJgoiU0hPUF9TT1JUX09QVElPTl9SRUxFQVNFX0RBVEVfREVTQxAEYgZwcm90bzM","chesscom/courses/v1/courses_shop_service.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfc2hvcF9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIu8HChtHZXRDb3Vyc2VQcm9kdWN0TGlzdFJlcXVlc3QSQwoKcGFnaW5hdGlvbhgBIAEoCzIqLmNoZXNzY29tLmNvdXJzZXMudjEuQ291cnNlc1Nob3BQYWdpbmF0aW9uSACIAQESGQoMc2VhcmNoX3F1ZXJ5GAIgASgJSAGIAQESRgoMZ2F
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18000"></a>
## FND-18000: Full frontend descriptor: chesscom/courses/v1alpha/course_deviation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1alpha/course_deviation.proto",
  "package": "chesscom.courses.v1alpha",
  "message_type": [
    {
      "name": "CourseDeviation",
      "field": [
        {
          "name": "correct_line",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "correct_line_move_arrow",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Arrow"
        },
        {
          "name": "variation_url",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ply",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "course_url",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "course_name",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "thumbnail_url",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_name",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "fen_in_course",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "fen_deviated",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 761170.

```text
zZXMudjEuR2V0U2hvcE1ldGFkYXRhUmVzcG9uc2VCIcq3LB0KBC9ycGMSExIRY291cnNlcy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/courses/v1alpha/course_deviation.proto":"Ci9jaGVzc2NvbS9jb3Vyc2VzL3YxYWxwaGEvY291cnNlX2RldmlhdGlvbi5wcm90bxIYY2hlc3Njb20uY291cnNlcy52MWFscGhhIogCCg9Db3Vyc2VEZXZpYXRpb24SFAoMY29ycmVjdF9saW5lGAEgAygJEjkKF2NvcnJlY3RfbGluZV9tb3ZlX2Fycm93GAIgASgLMhguY2hlc3Njb20uY2hlc3MudjEuQXJyb3cSFQoNdmFyaWF0aW9uX3VybBgDIAEoCRILCg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18001"></a>
## FND-18001: Full frontend descriptor: chesscom/courses/v1alpha/course_deviations_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/courses/v1alpha/course_deviations_service.proto",
  "package": "chesscom.courses.v1alpha",
  "message_type": [
    {
      "name": "GetCourseDeviationsRequest",
      "field": [
        {
          "name": "color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "fens",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetCourseDeviationsResponse",
      "field": [
        {
          "name": "deviations",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1alpha.CourseDeviation"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "CourseDeviationsService",
      "method": [
        {
          "name": "GetCourseDeviations",
          "input_type": ".chesscom.courses.v1alpha.GetCourseDeviationsRequest",
          "output_type": ".chesscom.courses.v1alpha.GetCourseDeviationsResponse",
          "options": {}
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 761690.

```text
MKC2F1dGhvcl9uYW1lGAggASgJEhUKDWZlbl9pbl9jb3Vyc2UYCSABKAkSFAoMZmVuX2RldmlhdGVkGAogASgJYgZwcm90bzM","chesscom/courses/v1alpha/course_deviations_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxYWxwaGEvY291cnNlX2RldmlhdGlvbnNfc2VydmljZS5wcm90bxIYY2hlc3Njb20uY291cnNlcy52MWFscGhhIlMKGkdldENvdXJzZURldmlhdGlvbnNSZXF1ZXN0EicKBWNvbG9yGAEgASgOMhguY2hlc3Njb20uY2hlc3MudjEuQ29sb3ISDAoEZmVucxgCIAMoCSJcChtHZXRDb3Vyc2VEZXZpYXRpb25zUmVzc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.
