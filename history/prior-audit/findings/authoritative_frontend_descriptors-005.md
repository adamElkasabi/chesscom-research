# authoritative_frontend_descriptors — findings 401–450

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18003"></a>
## FND-18003: Full frontend descriptor: chesscom/skills/v1/skill_category.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/skill_category.proto",
  "package": "chesscom.skills.v1",
  "enum_type": [
    {
      "name": "SkillCategory",
      "value": [
        {
          "name": "SKILL_CATEGORY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILL_CATEGORY_FUNDAMENTALS",
          "number": 1
        },
        {
          "name": "SKILL_CATEGORY_OPENINGS",
          "number": 2
        },
        {
          "name": "SKILL_CATEGORY_TACTICS",
          "number": 3
        },
        {
          "name": "SKILL_CATEGORY_STRATEGY",
          "number": 4
        },
        {
          "name": "SKILL_CATEGORY_ENDGAME",
          "number": 5
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 762395.

```text
lhdGlvbnNSZXNwb25zZSIAQi7KtywqCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGg0SC2JlYXJlcl9hdXRoYgZwcm90bzM","chesscom/skills/v1/skill_category.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxfY2F0ZWdvcnkucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSrLAQoNU2tpbGxDYXRlZ29yeRIeChpTS0lMTF9DQVRFR09SWV9VTlNQRUNJRklFRBAAEh8KG1NLSUxMX0NBVEVHT1JZX0ZVTkRBTUVOVEFMUxABEhsKF1NLSUxMX0NBVEVHT1JZX09QRU5JTkdTEAISGgoWU0tJTExfQ0FURUdPUllfVEFDVElDUxADEhsKF1NLSU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18004"></a>
## FND-18004: Full frontend descriptor: chesscom/skills/v1/eligibility_error.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/eligibility_error.proto",
  "package": "chesscom.skills.v1",
  "message_type": [
    {
      "name": "EligibilityError",
      "field": [
        {
          "name": "reason",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.EligibilityError.Reason"
        }
      ],
      "enum_type": [
        {
          "name": "Reason",
          "value": [
            {
              "name": "REASON_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "REASON_GAME_SKILL_POINTS_EXPIRED",
              "number": 1
            },
            {
              "name": "REASON_NOT_A_GAME_PARTICIPANT",
              "number": 2
            },
            {
              "name": "REASON_PLAYER_DISABLED",
              "number": 3
            },
            {
              "name": "REASON_GAME_NOT_FOUND",
              "number": 4
            }
          ]
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 762807.

```text
sKF1NLSUxMX0NBVEVHT1JZX1NUUkFURUdZEAQSGgoWU0tJTExfQ0FURUdPUllfRU5ER0FNRRAFGgeKph0DCgEBYgZwcm90bzM","chesscom/skills/v1/eligibility_error.proto":"CipjaGVzc2NvbS9za2lsbHMvdjEvZWxpZ2liaWxpdHlfZXJyb3IucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL7AQoQRWxpZ2liaWxpdHlFcnJvchI7CgZyZWFzb24YASABKA4yKy5jaGVzc2NvbS5za2lsbHMudjEuRWxpZ2liaWxpdHlFcnJvci5SZWFzb24ioAEKBlJlYXNvbhIWChJSRUFTT05fVU5TUEVDSUZJRUQQABIkCiBSRUFTT05fR0FNRV9TS0lMTF9QT0l
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18005"></a>
## FND-18005: Full frontend descriptor: chesscom/skills/v1/skill_point_gained.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/skill_point_gained.proto",
  "package": "chesscom.skills.v1",
  "message_type": [
    {
      "name": "SkillPointGained",
      "field": [
        {
          "name": "skill",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        },
        {
          "name": "new_value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "max_value",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 763290.

```text
ISGgoWUkVBU09OX1BMQVlFUl9ESVNBQkxFRBADEhkKFVJFQVNPTl9HQU1FX05PVF9GT1VORBAEOgeCph0DCgEBYgZwcm90bzM","chesscom/skills/v1/skill_point_gained.proto":"CitjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxfcG9pbnRfZ2FpbmVkLnByb3RvEhJjaGVzc2NvbS5za2lsbHMudjEidwoQU2tpbGxQb2ludEdhaW5lZBI0CgVza2lsbBgBIAEoDjIlLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbBIRCgluZXdfdmFsdWUYAiABKA0SEQoJbWF4X3ZhbHVlGAMgASgNOgeCph0DCgEBYgZwcm90bzM","chesscom/ski
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18006"></a>
## FND-18006: Full frontend descriptor: chesscom/skills/v1/skill_view.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/skill_view.proto",
  "package": "chesscom.skills.v1",
  "message_type": [
    {
      "name": "SkillView",
      "field": [
        {
          "name": "skill",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        },
        {
          "name": "category",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillCategory"
        },
        {
          "name": "points_required",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "points_gained",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "is_unlocked",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_mastered",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 763598.

```text
9uX2VuZ2luZS52MS5Ta2lsbBIRCgluZXdfdmFsdWUYAiABKA0SEQoJbWF4X3ZhbHVlGAMgASgNOgeCph0DCgEBYgZwcm90bzM","chesscom/skills/v1/skill_view.proto":"CiNjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxfdmlldy5wcm90bxISY2hlc3Njb20uc2tpbGxzLnYxItkBCglTa2lsbFZpZXcSNAoFc2tpbGwYASABKA4yJS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuU2tpbGwSMwoIY2F0ZWdvcnkYAiABKA4yIS5jaGVzc2NvbS5za2lsbHMudjEuU2tpbGxDYXRlZ29yeRIXCg9wb2ludHNfcmVxdWlyZWQYAyABKA0SFQoNcG9pbn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18007"></a>
## FND-18007: Full frontend descriptor: chesscom/skills/v1/skills_configuration.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/skills_configuration.proto",
  "package": "chesscom.skills.v1",
  "message_type": [
    {
      "name": "SkillConfiguration",
      "field": [
        {
          "name": "skill_items",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.SkillItemConfiguration"
        }
      ],
      "options": {}
    },
    {
      "name": "SkillItemConfiguration",
      "field": [
        {
          "name": "skill",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.Translation"
        },
        {
          "name": "category",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillCategory"
        },
        {
          "name": "points_to_master",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "diagram",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.Translation"
        },
        {
          "name": "unlocked_by_all",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.UnlockedByAll",
          "oneof_index": 0
        },
        {
          "name": "unlocked_by_any",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.UnlockedByAny",
          "oneof_index": 0
        },
        {
          "name": "icon_png",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "icon_svg",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "unlocking_condition"
        }
      ]
    },
    {
      "name": "UnlockedByAll",
      "field": [
        {
          "name": "unlocked_by_all",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        }
      ],
      "options": {}
    },
    {
      "name": "UnlockedByAny",
      "field": [
        {
          "name": "unlocked_by_any",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        }
      ],
      "options": {}
    },
    {
      "name": "SkillCategoryConfiguration",
      "field": [
        {
          "name": "skills_categories",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.SkillCategoryItemConfiguration"
        }
      ],
      "options": {}
    },
    {
      "name": "SkillCategoryItemConfiguration",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillCategory"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.Translation"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 764019.

```text
zX2dhaW5lZBgEIAEoDRITCgtpc191bmxvY2tlZBgFIAEoCBITCgtpc19tYXN0ZXJlZBgGIAEoCDoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_configuration.proto":"Ci1jaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX2NvbmZpZ3VyYXRpb24ucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSJkChJTa2lsbENvbmZpZ3VyYXRpb24SPwoLc2tpbGxfaXRlbXMYASADKAsyKi5jaGVzc2NvbS5za2lsbHMudjEuU2tpbGxJdGVtQ29uZmlndXJhdGlvbjoNgqYdAwoBAcK3LAIIASL/AwoWU2tpbGxJdGVtQ29uZmlndXJhdGlvbhI0CgVza2ls
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18008"></a>
## FND-18008: Full frontend descriptor: chesscom/skills/v1/skills_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/skills_service.proto",
  "package": "chesscom.skills.v1",
  "message_type": [
    {
      "name": "GainSkillPointsRequest",
      "field": [
        {
          "name": "game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "skill_positions",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SkillsPosition"
        },
        {
          "name": "coach_input",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.GainSkillPointsRequest.CoachInput",
          "oneof_index": 0
        },
        {
          "name": "game_review_input",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput",
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "CoachInput",
          "field": [
            {
              "name": "player_color",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.chess.v1.Color"
            }
          ]
        },
        {
          "name": "GameReviewInput"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "input"
        }
      ]
    },
    {
      "name": "GainSkillPointsResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure",
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "GainSkillPointsSuccess",
          "field": [
            {
              "name": "skills_unlocked",
              "number": 1,
              "label": "LABEL_REPEATED",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.explanation_engine.v1.Skill"
            },
            {
              "name": "skill_points_gained",
              "number": 2,
              "label": "LABEL_REPEATED",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.skills.v1.SkillPointGained"
            },
            {
              "name": "skills_mastered",
              "number": 3,
              "label": "LABEL_REPEATED",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.explanation_engine.v1.Skill"
            },
            {
              "name": "has_mastered_all",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL"
            },
            {
              "name": "is_first_ever_skill_point",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL"
            }
          ],
          "options": {}
        },
        {
          "name": "GainSkillPointsFailure",
          "field": [
            {
              "name": "error",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.skills.v1.EligibilityError"
            }
          ],
          "options": {}
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
      "name": "GetSkillsRequest",
      "options": {}
    },
    {
      "name": "GetSkillsResponse",
      "field": [
        {
          "name": "skill_items",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.SkillView"
        },
        {
          "name": "has_mastered_all",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "GetSkillsPositionsRequest",
      "field": [
        {
          "name": "game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "skill_positions",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SkillsPosition"
        }
      ],
      "options": {}
    },
    {
      "name": "GetSkillsPositionsResponse",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure",
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "GetSkillsPositionsSuccess",
          "field": [
            {
              "name": "skill_positions",
              "number": 1,
              "label": "LABEL_REPEATED",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.SkillsPosition"
            }
          ],
          "options": {}
        },
        {
          "name": "GetSkillsPositionsFailure",
          "field": [
            {
              "name": "error",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.skills.v1.EligibilityError"
            }
          ],
          "options": {}
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
      "name": "GetConfigRequest",
      "field": [
        {
          "name": "version",
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
          "name": "_version"
        }
      ]
    },
    {
      "name": "GetConfigResponse",
      "field": [
        {
          "name": "status",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.GetConfigResponse.Status"
        },
        {
          "name": "version",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "skill_configuration",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.SkillConfiguration",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "skill_category_configuration",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.skills.v1.SkillCategoryConfiguration",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "enum_type": [
        {
          "name": "Status",
          "value": [
            {
              "name": "STATUS_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "STATUS_NEW_VERSION_AVAILABLE",
              "number": 1
            },
            {
              "name": "STATUS_UP_TO_DATE",
              "number": 2
            }
          ],
          "options": {}
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_skill_configuration"
        },
        {
          "name": "_skill_category_configuration"
        }
      ]
    },
    {
      "name": "ResetSkillsRequest",
      "options": {}
    },
    {
      "name": "ResetSkillsResponse",
      "options": {}
    }
  ],
  "service": [
    {
      "name": "SkillsService",
      "method": [
        {
          "name": "GainSkillPoints",
          "input_type": ".chesscom.skills.v1.GainSkillPointsRequest",
          "output_type": ".chesscom.skills.v1.GainSkillPointsResponse",
          "options": {}
        },
        {
          "name": "GetSkills",
          "input_type": ".chesscom.skills.v1.GetSkillsRequest",
          "output_type": ".chesscom.skills.v1.GetSkillsResponse",
          "options": {}
        },
        {
          "name": "GetSkillsPositions",
          "input_type": ".chesscom.skills.v1.GetSkillsPositionsRequest",
          "output_type": ".chesscom.skills.v1.GetSkillsPositionsResponse",
          "options": {}
        },
        {
          "name": "GetConfig",
          "input_type": ".chesscom.skills.v1.GetConfigRequest",
          "output_type": ".chesscom.skills.v1.GetConfigResponse",
          "options": {}
        },
        {
          "name": "ResetSkills",
          "input_type": ".chesscom.skills.v1.ResetSkillsRequest",
          "output_type": ".chesscom.skills.v1.ResetSkillsResponse",
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
  Character offset 765586.

```text
pbGxDYXRlZ29yeRIrCgRuYW1lGAIgASgLMh0uY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_service.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL8AgoWR2FpblNraWxsUG9pbnRzUmVxdWVzdBIPCgdnYW1lX2lkGAEgASgJEkcKD3NraWxsX3Bvc2l0aW9ucxgCIAMoCzIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbHNQb3NpdGlvbhJMCgtjb2FjaF9pbnB1dBgDIAEoCzI1LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18014"></a>
## FND-18014: Full frontend descriptor: chesscom/skills/v1/user_activity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/skills/v1/user_activity.proto",
  "package": "chesscom.skills.v1",
  "message_type": [
    {
      "name": "SkillContextExtension",
      "field": [
        {
          "name": "skill_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        },
        {
          "name": "skill_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "skill_category",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillCategory"
        },
        {
          "name": "skill_status",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillStatus"
        },
        {
          "name": "points_current",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "points_needed_to_master",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    },
    {
      "name": "SkillSettingsContextExtension",
      "field": [
        {
          "name": "new_state",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillSettingsNewState"
        },
        {
          "name": "entry_point",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.skills.v1.SkillSettingsEntryPoint"
        }
      ],
      "options": {}
    },
    {
      "name": "SkillPointAnimationViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillPointsIntroScreenViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillsButtonClicked",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillsListViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillCategoryViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillIntroFullScreenViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillRowClicked",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillDefinitionModalViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillMasteryModalViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillUnlockModalViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillMasteryShareButtonClicked",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "AllSkillsMasteredScreenViewed",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "AllSkillsMasteredShareButtonClicked",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_funnel"
        }
      ]
    },
    {
      "name": "SkillsSettingToggleClicked",
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "SkillStatus",
      "value": [
        {
          "name": "SKILL_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILL_STATUS_UNLOCKED",
          "number": 1
        },
        {
          "name": "SKILL_STATUS_LOCKED",
          "number": 2
        },
        {
          "name": "SKILL_STATUS_MASTERED",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "SkillSettingsNewState",
      "value": [
        {
          "name": "SKILL_SETTINGS_NEW_STATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILL_SETTINGS_NEW_STATE_ON",
          "number": 1
        },
        {
          "name": "SKILL_SETTINGS_NEW_STATE_OFF",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "SkillSettingsEntryPoint",
      "value": [
        {
          "name": "SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS",
          "number": 1
        },
        {
          "name": "SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS",
          "number": 2
        },
        {
          "name": "SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS",
          "number": 3
        },
        {
          "name": "SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS",
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
  Character offset 769621.

```text
XNlcnZpY2VzLm5leC52YS1zdGFnaW5nLTAxLmNoZXNzLXBsYXRmb3JtLmNvbRoNEgtiZWFyZXJfYXV0aCICCAFiBnByb3RvMw","chesscom/skills/v1/user_activity.proto":"CiZjaGVzc2NvbS9za2lsbHMvdjEvdXNlcl9hY3Rpdml0eS5wcm90bxISY2hlc3Njb20uc2tpbGxzLnYxIpwCChVTa2lsbENvbnRleHRFeHRlbnNpb24SNwoIc2tpbGxfaWQYASABKA4yJS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuU2tpbGwSEgoKc2tpbGxfbmFtZRgCIAEoCRI5Cg5za2lsbF9jYXRlZ29yeRgDIAEoDjIhLmNoZXNzY29tLnNraWxscy52MS5
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18015"></a>
## FND-18015: Full frontend descriptor: chesscom/interactions/v1/user_activity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/interactions/v1/user_activity.proto",
  "package": "chesscom.interactions.v1",
  "message_type": [
    {
      "name": "Click",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel"
        },
        {
          "name": "interface",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "element",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "tag",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "selection_index",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "selected_item",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "count",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "tags",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_tag"
        },
        {
          "name": "_selection_index"
        },
        {
          "name": "_selected_item"
        },
        {
          "name": "_count"
        }
      ]
    },
    {
      "name": "Impression",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel"
        },
        {
          "name": "interface",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "tag",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "selection_index",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "tags",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "elements",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_tag"
        },
        {
          "name": "_selection_index"
        }
      ]
    },
    {
      "name": "Input",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel"
        },
        {
          "name": "interface",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "element",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "input_text",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "tags",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_input_text"
        }
      ]
    },
    {
      "name": "SharedBoardGifCreated",
      "field": [
        {
          "name": "funnel",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel"
        },
        {
          "name": "interface",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "element",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "tags",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "content",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "website",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "size",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "board",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "pieces",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "has_coordinates",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "board_is_flipped",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 774359.

```text
1MQAxIyCi5TS0lMTF9TRVRUSU5HU19FTlRSWV9QT0lOVF9DT0FDSF9HQU1FX1NFVFRJTkdTEAQaB4qmHQMKAQFiBnByb3RvMw","chesscom/interactions/v1/user_activity.proto":"CixjaGVzc2NvbS9pbnRlcmFjdGlvbnMvdjEvdXNlcl9hY3Rpdml0eS5wcm90bxIYY2hlc3Njb20uaW50ZXJhY3Rpb25zLnYxIrMCCgVDbGljaxI4CgZmdW5uZWwYASABKA4yKC5jaGVzc2NvbS5wcm90b19vcHRpb25zLmV2ZW50cy52MS5GdW5uZWwSFwoJaW50ZXJmYWNlGAIgASgJQgTA8xgBEhUKB2VsZW1lbnQYAyABKAlCBMjzGAESFAoDdGFnGAQgASgJQgIYA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18016"></a>
## FND-18016: Full frontend descriptor: chesscom/payments/v1/enums.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/enums.proto",
  "package": "chesscom.payments.v1",
  "enum_type": [
    {
      "name": "AdditionalDataFieldType",
      "value": [
        {
          "name": "ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ADDITIONAL_DATA_FIELD_TYPE_SELECT",
          "number": 1
        },
        {
          "name": "ADDITIONAL_DATA_FIELD_TYPE_TEXT",
          "number": 2
        },
        {
          "name": "ADDITIONAL_DATA_FIELD_TYPE_EMAIL",
          "number": 3
        },
        {
          "name": "ADDITIONAL_DATA_FIELD_TYPE_TEL",
          "number": 4
        }
      ]
    },
    {
      "name": "CancellationContext",
      "value": [
        {
          "name": "CANCELLATION_CONTEXT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CANCELLATION_CONTEXT_USER_DECISION",
          "number": 1
        },
        {
          "name": "CANCELLATION_CONTEXT_ADMIN_ACTION",
          "number": 2
        },
        {
          "name": "CANCELLATION_CONTEXT_PAYMENT_PROCESSING",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "CancellationEffect",
      "value": [
        {
          "name": "CANCELLATION_EFFECT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CANCELLATION_EFFECT_END_OF_PERIOD",
          "number": 1
        },
        {
          "name": "CANCELLATION_EFFECT_IMMEDIATE",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "CancellationSource",
      "value": [
        {
          "name": "CANCELLATION_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CANCELLATION_SOURCE_VOLUNTARY",
          "number": 1
        },
        {
          "name": "CANCELLATION_SOURCE_INVOLUNTARY",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "IncentiveChargeType",
      "value": [
        {
          "name": "INCENTIVE_CHARGE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "INCENTIVE_CHARGE_TYPE_FIRST_CHARGE",
          "number": 1
        },
        {
          "name": "INCENTIVE_CHARGE_TYPE_ALL_CHARGES",
          "number": 2
        },
        {
          "name": "INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "IncentiveType",
      "value": [
        {
          "name": "INCENTIVE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "INCENTIVE_TYPE_COUPON",
          "number": 1
        },
        {
          "name": "INCENTIVE_TYPE_SPECIAL_OFFER",
          "number": 2
        },
        {
          "name": "INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW",
          "number": 3
        },
        {
          "name": "INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED",
          "number": 4
        },
        {
          "name": "INCENTIVE_TYPE_STUDENT_DISCOUNT",
          "number": 5
        },
        {
          "name": "INCENTIVE_TYPE_REACTIVATION_OFFER",
          "number": 6
        },
        {
          "name": "INCENTIVE_TYPE_FREEVIEW",
          "number": 7
        }
      ],
      "options": {}
    },
    {
      "name": "IncentiveOfferType",
      "value": [
        {
          "name": "INCENTIVE_OFFER_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "INCENTIVE_OFFER_TYPE_FREE_TIME",
          "number": 1
        },
        {
          "name": "INCENTIVE_OFFER_TYPE_DISCOUNT",
          "number": 2
        },
        {
          "name": "INCENTIVE_OFFER_TYPE_FREE_LIFETIME",
          "number": 3
        },
        {
          "name": "INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE",
          "number": 4
        },
        {
          "name": "INCENTIVE_OFFER_TYPE_OPENING_OFFER",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "SubscriptionDurationUnit",
      "value": [
        {
          "name": "SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUBSCRIPTION_DURATION_UNIT_DAY",
          "number": 1
        },
        {
          "name": "SUBSCRIPTION_DURATION_UNIT_WEEK",
          "number": 2
        },
        {
          "name": "SUBSCRIPTION_DURATION_UNIT_MONTH",
          "number": 3
        },
        {
          "name": "SUBSCRIPTION_DURATION_UNIT_YEAR",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "IncentiveTemplate",
      "value": [
        {
          "name": "INCENTIVE_TEMPLATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "INCENTIVE_TEMPLATE_BAU",
          "number": 1
        },
        {
          "name": "INCENTIVE_TEMPLATE_SUMMER_SALE",
          "number": 2
        },
        {
          "name": "INCENTIVE_TEMPLATE_BLACK_FRIDAY",
          "number": 3
        },
        {
          "name": "INCENTIVE_TEMPLATE_CYBER_MONDAY",
          "number": 4
        },
        {
          "name": "INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "INCENTIVE_TEMPLATE_CYBER_MONDAY_2025",
          "number": 6,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "INCENTIVE_TEMPLATE_SPRING_SALE_2026",
          "number": 7,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC",
          "number": 8,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK",
          "number": 9,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026",
          "number": 10
        },
        {
          "name": "INCENTIVE_TEMPLATE_CYBER_MONDAY_2026",
          "number": 11
        },
        {
          "name": "INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND",
          "number": 12
        },
        {
          "name": "INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND",
          "number": 13
        }
      ],
      "options": {}
    },
    {
      "name": "OrderType",
      "value": [
        {
          "name": "ORDER_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ORDER_TYPE_GIFT",
          "number": 1
        },
        {
          "name": "ORDER_TYPE_PRODUCT_CHANGE",
          "number": 2
        },
        {
          "name": "ORDER_TYPE_PURCHASE",
          "number": 3
        },
        {
          "name": "ORDER_TYPE_RENEWAL",
          "number": 4
        },
        {
          "name": "ORDER_TYPE_TRIAL",
          "number": 5
        },
        {
          "name": "ORDER_TYPE_TRIAL_CONVERSION",
          "number": 6
        },
        {
          "name": "ORDER_TYPE_FREE_EXTENSION",
          "number": 7
        },
        {
          "name": "ORDER_TYPE_FREE",
          "number": 8
        }
      ],
      "options": {}
    },
    {
      "name": "PaymentAction",
      "value": [
        {
          "name": "PAYMENT_ACTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PAYMENT_ACTION_AUTHORISE",
          "number": 1
        },
        {
          "name": "PAYMENT_ACTION_PAY",
          "number": 2
        },
        {
          "name": "PAYMENT_ACTION_RENEW",
          "number": 3
        },
        {
          "name": "PAYMENT_ACTION_DONATE",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "PaymentContext",
      "value": [
        {
          "name": "PAYMENT_CONTEXT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PAYMENT_CONTEXT_GIFT_MEMBERSHIP",
          "number": 1
        },
        {
          "name": "PAYMENT_CONTEXT_MEMBERSHIP",
          "number": 2
        },
        {
          "name": "PAYMENT_CONTEXT_DONATION",
          "number": 3
        },
        {
          "name": "PAYMENT_CONTEXT_COURSE",
          "number": 4
        }
      ]
    },
    {
      "name": "PaymentTarget",
      "value": [
        {
          "name": "PAYMENT_TARGET_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PAYMENT_TARGET_SELF",
          "number": 1
        },
        {
          "name": "PAYMENT_TARGET_OTHER",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "PaymentGateway",
      "value": [
        {
          "name": "PAYMENT_GATEWAY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PAYMENT_GATEWAY_AUTHORIZE_NET",
          "number": 1
        },
        {
          "name": "PAYMENT_GATEWAY_PAYPAL",
          "number": 2
        },
        {
          "name": "PAYMENT_GATEWAY_APPLE",
          "number": 3
        },
        {
          "name": "PAYMENT_GATEWAY_LITLE",
          "number": 4
        },
        {
          "name": "PAYMENT_GATEWAY_STRIPE",
          "number": 5
        },
        {
          "name": "PAYMENT_GATEWAY_ADYEN",
          "number": 6
        },
        {
          "name": "PAYMENT_GATEWAY_FACEBOOK",
          "number": 7
        },
        {
          "name": "PAYMENT_GATEWAY_GOOGLE",
          "number": 8
        },
        {
          "name": "PAYMENT_GATEWAY_HUAWEI",
          "number": 9
        },
        {
          "name": "PAYMENT_GATEWAY_CRYPTO",
          "number": 10
        },
        {
          "name": "PAYMENT_GATEWAY_DLOCAL",
          "number": 11
        }
      ],
      "options": {}
    },
    {
      "name": "PaymentMethod",
      "value": [
        {
          "name": "PAYMENT_METHOD_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PAYMENT_METHOD_CREDIT_CARD",
          "number": 1
        },
        {
          "name": "PAYMENT_METHOD_GOOGLE",
          "number": 2
        },
        {
          "name": "PAYMENT_METHOD_APPLE",
          "number": 3
        },
        {
          "name": "PAYMENT_METHOD_PAYPAL",
          "number": 4
        },
        {
          "name": "PAYMENT_METHOD_ADYEN",
          "number": 5
        },
        {
          "name": "PAYMENT_METHOD_IDEAL",
          "number": 6
        },
        {
          "name": "PAYMENT_METHOD_NO_PAYMENT_METHOD",
          "number": 7
        },
        {
          "name": "PAYMENT_METHOD_SOFORT",
          "number": 8
        },
        {
          "name": "PAYMENT_METHOD_CARRIER_BILLING",
          "number": 9
        },
        {
          "name": "PAYMENT_METHOD_GIROPAY",
          "number": 10
        },
        {
          "name": "PAYMENT_METHOD_SEPA_DIRECT_DEBIT",
          "number": 11
        },
        {
          "name": "PAYMENT_METHOD_WORLD_PAY",
          "number": 12
        },
        {
          "name": "PAYMENT_METHOD_HUAWEI_POINTS",
          "number": 13
        },
        {
          "name": "PAYMENT_METHOD_FREE_WEEK",
          "number": 14
        },
        {
          "name": "PAYMENT_METHOD_FACEBOOK",
          "number": 15
        },
        {
          "name": "PAYMENT_METHOD_MONEY_ORDER",
          "number": 16
        },
        {
          "name": "PAYMENT_METHOD_HUAWEI_POINT_CARD",
          "number": 17
        },
        {
          "name": "PAYMENT_METHOD_HUAWEI_WALLET",
          "number": 18
        },
        {
          "name": "PAYMENT_METHOD_ALIPAY",
          "number": 19
        },
        {
          "name": "PAYMENT_METHOD_DEBIT_CARD",
          "number": 20
        },
        {
          "name": "PAYMENT_METHOD_WECHAT_PAY",
          "number": 21
        },
        {
          "name": "PAYMENT_METHOD_GIFT_CARD",
          "number": 22
        },
        {
          "name": "PAYMENT_METHOD_BALANCE",
          "number": 23
        },
        {
          "name": "PAYMENT_METHOD_ANT_CREDIT_PAY",
          "number": 24
        },
        {
          "name": "PAYMENT_METHOD_IPAY88",
          "number": 25
        },
        {
          "name": "PAYMENT_METHOD_M_PESA",
          "number": 26
        },
        {
          "name": "PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE",
          "number": 27
        },
        {
          "name": "PAYMENT_METHOD_CRYPTO",
          "number": 28
        },
        {
          "name": "PAYMENT_METHOD_GOOGLEPAY",
          "number": 29
        },
        {
          "name": "PAYMENT_METHOD_APPLEPAY",
          "number": 30
        },
        {
          "name": "PAYMENT_METHOD_NEQUI",
          "number": 31
        },
        {
          "name": "PAYMENT_METHOD_PIX",
          "number": 32
        }
      ],
      "options": {}
    },
    {
      "name": "PaymentTrigger",
      "value": [
        {
          "name": "PAYMENT_TRIGGER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PAYMENT_TRIGGER_USER_INITIATED",
          "number": 1
        },
        {
          "name": "PAYMENT_TRIGGER_AUTOMATED",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "PlanState",
      "value": [
        {
          "name": "PLAN_STATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAN_STATE_ACTIVE",
          "number": 1
        },
        {
          "name": "PLAN_STATE_PAST_DUE",
          "number": 2
        },
        {
          "name": "PLAN_STATE_CANCELLED_ACTIVE",
          "number": 3
        },
        {
          "name": "PLAN_STATE_CANCELLED_DEACTIVATED",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "ProductType",
      "value": [
        {
          "name": "PRODUCT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PRODUCT_TYPE_MEMBERSHIP",
          "number": 1
        },
        {
          "name": "PRODUCT_TYPE_DONATION",
          "number": 7
        },
        {
          "name": "PRODUCT_TYPE_COURSE",
          "number": 8
        },
        {
          "name": "PRODUCT_TYPE_VERIFIED",
          "number": 9
        },
        {
          "name": "PRODUCT_TYPE_GROUP_MEMBERSHIP",
          "number": 10
        }
      ],
      "options": {}
    },
    {
      "name": "MembershipLevel",
      "value": [
        {
          "name": "MEMBERSHIP_LEVEL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MEMBERSHIP_LEVEL_CHEATER",
          "number": 5
        },
        {
          "name": "MEMBERSHIP_LEVEL_ABUSER",
          "number": 6
        },
        {
          "name": "MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED",
          "number": 7
        },
        {
          "name": "MEMBERSHIP_LEVEL_BASIC",
          "number": 10
        },
        {
          "name": "MEMBERSHIP_LEVEL_NO_ADS",
          "number": 20
        },
        {
          "name": "MEMBERSHIP_LEVEL_GOLD",
          "number": 30
        },
        {
          "name": "MEMBERSHIP_LEVEL_PLATINUM",
          "number": 40
        },
        {
          "name": "MEMBERSHIP_LEVEL_DIAMOND",
          "number": 50
        },
        {
          "name": "MEMBERSHIP_LEVEL_MODERATOR",
          "number": 60
        },
        {
          "name": "MEMBERSHIP_LEVEL_STAFF",
          "number": 70
        }
      ],
      "options": {}
    },
    {
      "name": "PriceGroup",
      "value": [
        {
          "name": "PRICE_GROUP_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PRICE_GROUP_SEPT_2022",
          "number": 1
        },
        {
          "name": "PRICE_GROUP_SEPT_2026_V1",
          "number": 2
        },
        {
          "name": "PRICE_GROUP_SEPT_2026_V2",
          "number": 3
        },
        {
          "name": "PRICE_GROUP_JAN_2027_V2",
          "number": 4
        },
        {
          "name": "PRICE_GROUP_JAN_2027_V3",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "TrialState",
      "value": [
        {
          "name": "TRIAL_STATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRIAL_STATE_ACTIVE",
          "number": 1
        },
        {
          "name": "TRIAL_STATE_ENDED",
          "number": 2
        },
        {
          "name": "TRIAL_STATE_CANCELLED",
          "number": 3
        },
        {
          "name": "TRIAL_STATE_CONVERTED",
          "number": 4
        }
      ]
    },
    {
      "name": "BusinessEntity",
      "value": [
        {
          "name": "BUSINESS_ENTITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BUSINESS_ENTITY_CHESSCOM",
          "number": 1
        },
        {
          "name": "BUSINESS_ENTITY_CHESSABLE",
          "number": 2
        }
      ]
    },
    {
      "name": "StatusCode",
      "value": [
        {
          "name": "STATUS_CODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STATUS_CODE_ADMIN_CANCEL",
          "number": 1
        },
        {
          "name": "STATUS_CODE_CANCEL",
          "number": 2
        },
        {
          "name": "STATUS_CODE_CHARGEBACK",
          "number": 3
        },
        {
          "name": "STATUS_CODE_CHARGEBACK_REVERSED",
          "number": 4
        },
        {
          "name": "STATUS_CODE_DUPLICATE",
          "number": 5
        },
        {
          "name": "STATUS_CODE_ENDED",
          "number": 6
        },
        {
          "name": "STATUS_CODE_FAILED",
          "number": 7
        },
        {
          "name": "STATUS_CODE_NEW",
          "number": 8
        },
        {
          "name": "STATUS_CODE_PAYPAL_AGREEMENT",
          "number": 9
        },
        {
          "name": "STATUS_CODE_PAYPAL_CANCEL",
          "number": 10
        },
        {
          "name": "STATUS_CODE_PENDING",
          "number": 11
        },
        {
          "name": "STATUS_CODE_PLAN_TRANSITION",
          "number": 12
        },
        {
          "name": "STATUS_CODE_PROCESSED",
          "number": 13
        },
        {
          "name": "STATUS_CODE_REACTIVATED",
          "number": 14
        },
        {
          "name": "STATUS_CODE_REFUND",
          "number": 15
        },
        {
          "name": "STATUS_CODE_SHUTOFF",
          "number": 16
        },
        {
          "name": "STATUS_CODE_TRIAL_CANCEL",
          "number": 17
        },
        {
          "name": "STATUS_CODE_TRIAL_ENDED",
          "number": 18
        },
        {
          "name": "STATUS_CODE_INCENTIVE_REDEMPTION",
          "number": 19
        },
        {
          "name": "STATUS_CODE_REFUND_FAILED",
          "number": 20
        },
        {
          "name": "STATUS_CODE_REFUND_PENDING",
          "number": 21
        }
      ],
      "options": {}
    },
    {
      "name": "PlatformCourseAccessChangedAction",
      "value": [
        {
          "name": "PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED",
          "number": 1
        },
        {
          "name": "PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED",
          "number": 2
        }
      ]
    },
    {
      "name": "CancelSurveyReason",
      "value": [
        {
          "name": "CANCEL_SURVEY_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CANCEL_SURVEY_REASON_TOO_EXPENSIVE",
          "number": 1
        },
        {
          "name": "CANCEL_SURVEY_REASON_TECHNICAL_ISSUES",
          "number": 2
        },
        {
          "name": "CANCEL_SURVEY_REASON_USING_OTHER",
          "number": 3
        },
        {
          "name": "CANCEL_SURVEY_REASON_LESS_INTEREST",
          "number": 4
        },
        {
          "name": "CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL",
          "number": 5
        },
        {
          "name": "CANCEL_SURVEY_REASON_OTHER",
          "number": 6
        },
        {
          "name": "CANCEL_SURVEY_REASON_NOT_USING",
          "number": 7
        }
      ],
      "options": {}
    },
    {
      "name": "SubscriptionPaymentStatus",
      "value": [
        {
          "name": "SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING",
          "number": 1
        },
        {
          "name": "SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE",
          "number": 2
        },
        {
          "name": "SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 775925.

```text
YChBib2FyZF9pc19mbGlwcGVkGAsgASgIOibC8xgbChVTaGFyZWRCb2FyZEdpZkNyZWF0ZWQQAhgEgqYdAwoBAWIGcHJvdG8z","chesscom/payments/v1/enums.proto":"CiBjaGVzc2NvbS9wYXltZW50cy92MS9lbnVtcy5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEq2wEKF0FkZGl0aW9uYWxEYXRhRmllbGRUeXBlEioKJkFERElUSU9OQUxfREFUQV9GSUVMRF9UWVBFX1VOU1BFQ0lGSUVEEAASJQohQURESVRJT05BTF9EQVRBX0ZJRUxEX1RZUEVfU0VMRUNUEAESIwofQURESVRJT05BTF9EQVRBX0ZJRUxEX1RZUEVfVEVYVBACEiQKIEFERElUS
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18017"></a>
## FND-18017: Full frontend descriptor: chesscom/payments/v1/subscription.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/subscription.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "Subscription",
      "field": [
        {
          "name": "length",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "unit",
          "number": 2,
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
  Character offset 785633.

```text
VRVU19TT0ZUX0ZBSUxVUkUQAhIsCihTVUJTQ1JJUFRJT05fUEFZTUVOVF9TVEFUVVNfSEFSRF9GQUlMVVJFEANiBnByb3RvMw","chesscom/payments/v1/subscription.proto":"CidjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb24ucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIjUKDFN1YnNjcmlwdGlvbhIOCgZsZW5ndGgYASABKAUSDAoEdW5pdBgCIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/payments/v1/product.proto":"CiJjaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0LnByb3RvEhRjaGVzc2NvbS5wYXltZW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18018"></a>
## FND-18018: Full frontend descriptor: chesscom/payments/v1/product.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/product.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "Product",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sku",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "price_amount",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "subscription",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Subscription",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "description",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "image",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "product_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.ProductType"
        },
        {
          "name": "membership_code",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MembershipLevel",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_subscription"
        },
        {
          "name": "_description"
        },
        {
          "name": "_image"
        },
        {
          "name": "_membership_code"
        }
      ]
    },
    {
      "name": "ProductSummary",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "sku",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "price_amount",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "subscription",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Subscription",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "description",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "image",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "product_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.ProductType",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "membership_code",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MembershipLevel",
          "oneof_index": 6,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_name"
        },
        {
          "name": "_price_amount"
        },
        {
          "name": "_subscription"
        },
        {
          "name": "_description"
        },
        {
          "name": "_image"
        },
        {
          "name": "_product_type"
        },
        {
          "name": "_membership_code"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 785846.

```text
heW1lbnRzLnYxIjUKDFN1YnNjcmlwdGlvbhIOCgZsZW5ndGgYASABKAUSDAoEdW5pdBgCIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/payments/v1/product.proto":"CiJjaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0LnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSKFAwoHUHJvZHVjdBIMCgRuYW1lGAEgASgJEgsKA3NrdRgCIAEoCRIsCgxwcmljZV9hbW91bnQYAyABKAsyFi5jaGVzc2NvbS5hcGkudjEuTW9uZXkSPQoMc3Vic2NyaXB0aW9uGAQgASgLMiIuY2hlc3Njb20ucGF5bWVudHMudjEuU3Vic2NyaXB0aW9uSACIAQESGAoLZGV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18019"></a>
## FND-18019: Full frontend descriptor: chesscom/payments/v1/incentive_external_association.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/incentive_external_association.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "IncentiveExternalAssociation",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "incentive_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "identifier",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 787106.

```text
vbkIOCgxfZGVzY3JpcHRpb25CCAoGX2ltYWdlQg8KDV9wcm9kdWN0X3R5cGVCEgoQX21lbWJlcnNoaXBfY29kZWIGcHJvdG8z","chesscom/payments/v1/incentive_external_association.proto":"CjljaGVzc2NvbS9wYXltZW50cy92MS9pbmNlbnRpdmVfZXh0ZXJuYWxfYXNzb2NpYXRpb24ucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIooBChxJbmNlbnRpdmVFeHRlcm5hbEFzc29jaWF0aW9uEgoKAmlkGAEgASgFEhQKDGluY2VudGl2ZV9pZBgCIAEoCRISCgppZGVudGlmaWVyGAMgASgJEisKCHBsYXRmb3JtGAQgASgOMhkuY2hlc3Nj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18020"></a>
## FND-18020: Full frontend descriptor: chesscom/payments/v1/incentive_offer.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/incentive_offer.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "IncentiveOffer",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "incentive_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.IncentiveOfferType"
        },
        {
          "name": "value",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "period_start",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "period_end",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "duration",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "duration_unit",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionDurationUnit",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "prices",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.IncentiveOfferPrice"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_description"
        },
        {
          "name": "_period_end"
        },
        {
          "name": "_duration"
        },
        {
          "name": "_duration_unit"
        }
      ]
    },
    {
      "name": "IncentiveOfferPrice",
      "field": [
        {
          "name": "price",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "country",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Country",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_country"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 787476.

```text
lmaWVyGAMgASgJEisKCHBsYXRmb3JtGAQgASgOMhkuY2hlc3Njb20uYXBpLnYxLlBsYXRmb3JtOgeCph0DCgEBYgZwcm90bzM","chesscom/payments/v1/incentive_offer.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9pbmNlbnRpdmVfb2ZmZXIucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIqsDCg5JbmNlbnRpdmVPZmZlchIKCgJpZBgBIAEoCRIUCgxpbmNlbnRpdmVfaWQYAiABKAkSGAoLZGVzY3JpcHRpb24YAyABKAlIAIgBARI2CgR0eXBlGAQgASgOMiguY2hlc3Njb20ucGF5bWVudHMudjEuSW5jZW50aXZlT2ZmZXJUeXBlEg0KBXZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18021"></a>
## FND-18021: Full frontend descriptor: chesscom/payments/v1/incentive.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/incentive.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "Incentive",
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
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.IncentiveType"
        },
        {
          "name": "free_time",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "discount_percentage",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "discount_amount",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "discount_charge_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.IncentiveChargeType",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "discount_recurring_limit",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "incentive_offers",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.IncentiveOffer"
        },
        {
          "name": "is_payment_information_required",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "incentive_external_associations",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.IncentiveExternalAssociation"
        },
        {
          "name": "expires_at",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "starts_at",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "product",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "code",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "campaign_id",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "template",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.IncentiveTemplate",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "app_store_subscription_group_id",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 12,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_free_time"
        },
        {
          "name": "_discount_percentage"
        },
        {
          "name": "_discount_amount"
        },
        {
          "name": "_discount_charge_type"
        },
        {
          "name": "_discount_recurring_limit"
        },
        {
          "name": "_is_payment_information_required"
        },
        {
          "name": "_expires_at"
        },
        {
          "name": "_starts_at"
        },
        {
          "name": "_product"
        },
        {
          "name": "_code"
        },
        {
          "name": "_campaign_id"
        },
        {
          "name": "_template"
        },
        {
          "name": "_app_store_subscription_group_id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 788372.

```text
jb3VudHJ5GAIgASgLMhguY2hlc3Njb20uYXBpLnYxLkNvdW50cnlIAIgBAToHgqYdAwoBAUIKCghfY291bnRyeWIGcHJvdG8z","chesscom/payments/v1/incentive.proto":"CiRjaGVzc2NvbS9wYXltZW50cy92MS9pbmNlbnRpdmUucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIrIICglJbmNlbnRpdmUSCgoCaWQYASABKAkSDAoEbmFtZRgCIAEoCRIxCgR0eXBlGAMgASgOMiMuY2hlc3Njb20ucGF5bWVudHMudjEuSW5jZW50aXZlVHlwZRIWCglmcmVlX3RpbWUYBCABKAVIAIgBARIgChNkaXNjb3VudF9wZXJjZW50YWdlGAUgASgCSAGIAQESN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18022"></a>
## FND-18022: Full frontend descriptor: chesscom/payments/v1/discount.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/discount.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "Discount",
      "field": [
        {
          "name": "discount_amount",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "discount_amount_with_taxes",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "incentive_offer_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "offer_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_incentive_offer_id"
        },
        {
          "name": "_offer_id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 789941.

```text
IOCgxfY2FtcGFpZ25faWRCCwoJX3RlbXBsYXRlQiIKIF9hcHBfc3RvcmVfc3Vic2NyaXB0aW9uX2dyb3VwX2lkYgZwcm90bzM","chesscom/payments/v1/discount.proto":"CiNjaGVzc2NvbS9wYXltZW50cy92MS9kaXNjb3VudC5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi4AEKCERpc2NvdW50Ei8KD2Rpc2NvdW50X2Ftb3VudBgBIAEoCzIWLmNoZXNzY29tLmFwaS52MS5Nb25leRI6ChpkaXNjb3VudF9hbW91bnRfd2l0aF90YXhlcxgCIAEoCzIWLmNoZXNzY29tLmFwaS52MS5Nb25leRIjChJpbmNlbnRpdmVfb2ZmZXJfaWQYAyABKAVCAh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18023"></a>
## FND-18023: Full frontend descriptor: chesscom/permissions/v1/premium_features.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/permissions/v1/premium_features.proto",
  "package": "chesscom.permissions.v1",
  "enum_type": [
    {
      "name": "PremiumFeature",
      "value": [
        {
          "name": "PREMIUM_FEATURE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLES_RATED",
          "number": 1
        },
        {
          "name": "PREMIUM_FEATURE_NO_ADS",
          "number": 2
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLE_RUSH",
          "number": 3
        },
        {
          "name": "PREMIUM_FEATURE_LESSONS",
          "number": 4
        },
        {
          "name": "PREMIUM_FEATURE_ANALYSIS",
          "number": 5
        },
        {
          "name": "PREMIUM_FEATURE_VIDEOS",
          "number": 6
        },
        {
          "name": "PREMIUM_FEATURE_ENDGAMES_TRAINER",
          "number": 7
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLES_UNRATED",
          "number": 8
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLE_BATTLE",
          "number": 9
        },
        {
          "name": "PREMIUM_FEATURE_INSIGHTS",
          "number": 10
        },
        {
          "name": "PREMIUM_FEATURE_EXPLORER",
          "number": 11
        },
        {
          "name": "PREMIUM_FEATURE_FLAIR_PREMIUM",
          "number": 12
        },
        {
          "name": "PREMIUM_FEATURE_FLAIR_STAR",
          "number": 13
        },
        {
          "name": "PREMIUM_FEATURE_FLAIR_CROWN",
          "number": 14
        },
        {
          "name": "PREMIUM_FEATURE_FLAIR_DIAMOND",
          "number": 15
        },
        {
          "name": "PREMIUM_FEATURE_BOTS",
          "number": 16
        },
        {
          "name": "PREMIUM_FEATURE_PLAY_VS_COACH",
          "number": 17
        },
        {
          "name": "PREMIUM_FEATURE_COURSES_SPECIAL_PRICE",
          "number": 18
        },
        {
          "name": "PREMIUM_FEATURE_EXCLUSIVE_COURSE",
          "number": 19
        },
        {
          "name": "PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS",
          "number": 20
        },
        {
          "name": "PREMIUM_FEATURE_MOVE_EXPLANATIONS",
          "number": 21
        },
        {
          "name": "PREMIUM_FEATURE_ADVANCED_STATS",
          "number": 22
        },
        {
          "name": "PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS",
          "number": 23
        },
        {
          "name": "PREMIUM_FEATURE_DRILLS",
          "number": 24
        },
        {
          "name": "PREMIUM_FEATURE_TIME_OUT_PROTECTION",
          "number": 25
        },
        {
          "name": "PREMIUM_FEATURE_PREMIUM_TOURNAMENTS",
          "number": 26
        },
        {
          "name": "PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES",
          "number": 27
        },
        {
          "name": "PREMIUM_FEATURE_PREMIUM_MATCHMAKING",
          "number": 28
        },
        {
          "name": "PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY",
          "number": 29
        },
        {
          "name": "PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING",
          "number": 33
        },
        {
          "name": "PREMIUM_FEATURE_BRILLIANT_MOVES",
          "number": 34
        },
        {
          "name": "PREMIUM_FEATURE_BOT_EVENT_MONETIZATION",
          "number": 35
        },
        {
          "name": "PREMIUM_FEATURE_OPENING_COURSES",
          "number": 36
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 790374.

```text
Ib2ZmZXJfaWQYBCABKAlIAYgBAToHgqYdAwoBAUIVChNfaW5jZW50aXZlX29mZmVyX2lkQgsKCV9vZmZlcl9pZGIGcHJvdG8z","chesscom/permissions/v1/premium_features.proto":"Ci5jaGVzc2NvbS9wZXJtaXNzaW9ucy92MS9wcmVtaXVtX2ZlYXR1cmVzLnByb3RvEhdjaGVzc2NvbS5wZXJtaXNzaW9ucy52MSrqCQoOUHJlbWl1bUZlYXR1cmUSHwobUFJFTUlVTV9GRUFUVVJFX1VOU1BFQ0lGSUVEEAASIQodUFJFTUlVTV9GRUFUVVJFX1BVWlpMRVNfUkFURUQQARIaChZQUkVNSVVNX0ZFQVRVUkVfTk9fQURTEAISHwobUFJFTUlVTV9GRUF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18024"></a>
## FND-18024: Full frontend descriptor: chesscom/premium_access/v1/enums.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/premium_access/v1/enums.proto",
  "package": "chesscom.premium_access.v1",
  "enum_type": [
    {
      "name": "PremiumFeature",
      "value": [
        {
          "name": "PREMIUM_FEATURE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLES_RATED",
          "number": 1
        },
        {
          "name": "PREMIUM_FEATURE_NO_ADS",
          "number": 2
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLE_RUSH",
          "number": 3
        },
        {
          "name": "PREMIUM_FEATURE_LESSONS",
          "number": 4
        },
        {
          "name": "PREMIUM_FEATURE_ANALYSIS",
          "number": 5
        },
        {
          "name": "PREMIUM_FEATURE_VIDEOS",
          "number": 6
        },
        {
          "name": "PREMIUM_FEATURE_ENDGAMES_TRAINER",
          "number": 7
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLES_UNRATED",
          "number": 8
        },
        {
          "name": "PREMIUM_FEATURE_PUZZLE_BATTLE",
          "number": 9
        },
        {
          "name": "PREMIUM_FEATURE_INSIGHTS",
          "number": 10
        },
        {
          "name": "PREMIUM_FEATURE_EXPLORER",
          "number": 11
        },
        {
          "name": "PREMIUM_FEATURE_BOTS",
          "number": 16
        },
        {
          "name": "PREMIUM_FEATURE_PLAY_VS_COACH",
          "number": 17
        },
        {
          "name": "PREMIUM_FEATURE_COURSES_SPECIAL_PRICE",
          "number": 18
        },
        {
          "name": "PREMIUM_FEATURE_EXCLUSIVE_COURSE",
          "number": 19
        },
        {
          "name": "PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS",
          "number": 20
        },
        {
          "name": "PREMIUM_FEATURE_MOVE_EXPLANATIONS",
          "number": 21
        },
        {
          "name": "PREMIUM_FEATURE_ADVANCED_STATS",
          "number": 22
        },
        {
          "name": "PREMIUM_FEATURE_OFFLINE_PUZZLES",
          "number": 23
        },
        {
          "name": "PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS",
          "number": 24
        },
        {
          "name": "PREMIUM_FEATURE_DRILLS",
          "number": 25
        },
        {
          "name": "PREMIUM_FEATURE_TIME_OUT_PROTECTION",
          "number": 26
        },
        {
          "name": "PREMIUM_FEATURE_PREMIUM_TOURNAMENTS",
          "number": 27
        },
        {
          "name": "PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES",
          "number": 28
        },
        {
          "name": "PREMIUM_FEATURE_PREMIUM_MATCHMAKING",
          "number": 29
        },
        {
          "name": "PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY",
          "number": 30
        },
        {
          "name": "PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING",
          "number": 33
        },
        {
          "name": "PREMIUM_FEATURE_BRILLIANT_MOVES",
          "number": 34
        },
        {
          "name": "PREMIUM_FEATURE_BOT_EVENT_MONETIZATION",
          "number": 35
        },
        {
          "name": "PREMIUM_FEATURE_TRAIN",
          "number": 36
        },
        {
          "name": "PREMIUM_FEATURE_OPENING_COURSES",
          "number": 37
        },
        {
          "name": "PREMIUM_FEATURE_CLUB_CREATION",
          "number": 38
        },
        {
          "name": "PREMIUM_FEATURE_CLASSROOM_UNLIMITED",
          "number": 39
        },
        {
          "name": "PREMIUM_FEATURE_CHAT",
          "number": 40
        },
        {
          "name": "PREMIUM_FEATURE_WEEKLY_COACH_REPORT",
          "number": 41
        },
        {
          "name": "PREMIUM_FEATURE_COURSES_CATALOG",
          "number": 42
        }
      ],
      "options": {},
      "reserved_range": [
        {
          "start": 12,
          "end": 15
        },
        {
          "start": 31,
          "end": 31
        },
        {
          "start": 32,
          "end": 32
        }
      ]
    },
    {
      "name": "Action",
      "value": [
        {
          "name": "ACTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ACTION_CREATE",
          "number": 1
        },
        {
          "name": "ACTION_VIEW",
          "number": 2
        },
        {
          "name": "ACTION_RETRY",
          "number": 3
        },
        {
          "name": "ACTION_COMMENTARY",
          "number": 4
        },
        {
          "name": "ACTION_BOOKMARK",
          "number": 5
        },
        {
          "name": "ACTION_PLAY",
          "number": 6
        },
        {
          "name": "ACTION_ATTEMPT_SUCCESS",
          "number": 7
        },
        {
          "name": "ACTION_ATTEMPT_FAILURE",
          "number": 8
        }
      ]
    },
    {
      "name": "Period",
      "value": [
        {
          "name": "PERIOD_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PERIOD_DAY",
          "number": 1
        },
        {
          "name": "PERIOD_WEEK",
          "number": 2
        },
        {
          "name": "PERIOD_MONTH",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 792216.

```text
kVOVF9NT05FVElaQVRJT04QIxIjCh9QUkVNSVVNX0ZFQVRVUkVfT1BFTklOR19DT1VSU0VTECQaB4qmHQMKAQFiBnByb3RvMw","chesscom/premium_access/v1/enums.proto":"CiZjaGVzc2NvbS9wcmVtaXVtX2FjY2Vzcy92MS9lbnVtcy5wcm90bxIaY2hlc3Njb20ucHJlbWl1bV9hY2Nlc3MudjEq6QoKDlByZW1pdW1GZWF0dXJlEh8KG1BSRU1JVU1fRkVBVFVSRV9VTlNQRUNJRklFRBAAEiEKHVBSRU1JVU1fRkVBVFVSRV9QVVpaTEVTX1JBVEVEEAESGgoWUFJFTUlVTV9GRUFUVVJFX05PX0FEUxACEh8KG1BSRU1JVU1fRkVBVFVSRV9QVVpaTEV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18025"></a>
## FND-18025: Full frontend descriptor: chesscom/payments/v1/membership_product_details.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/membership_product_details.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "MembershipProductDetails",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "image_url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "level",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "short_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "max_applicable_accounts",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "displayed_premium_features",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.permissions.v1.PremiumFeature"
        },
        {
          "name": "displayed_premium_features_v2",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.premium_access.v1.PremiumFeature"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 794600.

```text
fVU5TUEVDSUZJRUQQABIOCgpQRVJJT0RfREFZEAESDwoLUEVSSU9EX1dFRUsQAhIQCgxQRVJJT0RfTU9OVEgQA2IGcHJvdG8z","chesscom/payments/v1/membership_product_details.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJzaGlwX3Byb2R1Y3RfZGV0YWlscy5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEitgIKGE1lbWJlcnNoaXBQcm9kdWN0RGV0YWlscxIMCgRuYW1lGAEgASgJEhEKCWltYWdlX3VybBgCIAEoCRIMCgRjb2RlGAMgASgJEg0KBWxldmVsGAQgASgFEhIKCnNob3J0X25hbWUYBSABKAkSHwoXbWF4X2Fw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18026"></a>
## FND-18026: Full frontend descriptor: chesscom/payments/v1/checkout_total.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/checkout_total.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "CheckoutTotal",
      "field": [
        {
          "name": "product",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Product"
        },
        {
          "name": "original_amount",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "original_amount_with_taxes",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "discount_amount",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "discount_amount_with_taxes",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "subtotal_amount",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "subtotal_amount_with_taxes",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "credit_amount",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "credit_amount_with_taxes",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "total_amount",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "tax_amount",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "total_amount_with_taxes",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "incentive",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Incentive",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "tax_lines",
          "number": 14,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.TaxLine"
        },
        {
          "name": "usd_fx_rate",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "course_product_details",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.courses.v1.CourseProduct",
          "oneof_index": 0
        },
        {
          "name": "membership_product_details",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.MembershipProductDetails",
          "oneof_index": 0
        },
        {
          "name": "discount_amount_breakdown",
          "number": 18,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Discount"
        },
        {
          "name": "subtotal_amount_in_months",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "subtotal_amount_with_taxes_in_months",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "product_details"
        },
        {
          "name": "_incentive"
        },
        {
          "name": "_subtotal_amount_in_months"
        },
        {
          "name": "_subtotal_amount_with_taxes_in_months"
        }
      ]
    },
    {
      "name": "TaxLine",
      "field": [
        {
          "name": "description",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rate",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "amount",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        }
      ],
      "options": {}
    },
    {
      "name": "TotalBreakdown",
      "field": [
        {
          "name": "original_amount",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "original_amount_with_taxes",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "discount_amount",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "discount_amount_with_taxes",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "subtotal_amount",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "subtotal_amount_with_taxes",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "credit_amount",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "credit_amount_with_taxes",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "total_amount",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "tax_amount",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "total_amount_with_taxes",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        }
      ],
      "options": {}
    },
    {
      "name": "CheckoutTotalSummary",
      "field": [
        {
          "name": "product",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.ProductSummary"
        },
        {
          "name": "total_breakdown",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.TotalBreakdown",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "incentive",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Incentive",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "tax_lines",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.TaxLine"
        },
        {
          "name": "usd_fx_rate",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "discount_amount_breakdown",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Discount"
        },
        {
          "name": "country",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Country",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_total_breakdown"
        },
        {
          "name": "_incentive"
        },
        {
          "name": "_usd_fx_rate"
        },
        {
          "name": "_country"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 795190.

```text
Jlc192MhgIIAMoDjIqLmNoZXNzY29tLnByZW1pdW1fYWNjZXNzLnYxLlByZW1pdW1GZWF0dXJlOgeCph0DCgEBYgZwcm90bzM","chesscom/payments/v1/checkout_total.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9jaGVja291dF90b3RhbC5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi3QkKDUNoZWNrb3V0VG90YWwSLgoHcHJvZHVjdBgBIAEoCzIdLmNoZXNzY29tLnBheW1lbnRzLnYxLlByb2R1Y3QSLwoPb3JpZ2luYWxfYW1vdW50GAIgASgLMhYuY2hlc3Njb20uYXBpLnYxLk1vbmV5EjoKGm9yaWdpbmFsX2Ftb3VudF93aXRoX3Rh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18027"></a>
## FND-18027: Full frontend descriptor: chesscom/payments/v1/request_location.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/request_location.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "RequestLocation",
      "field": [
        {
          "name": "zip_code",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "region",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_zip_code"
        },
        {
          "name": "_region"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 798557.

```text
KAQFCEgoQX3RvdGFsX2JyZWFrZG93bkIMCgpfaW5jZW50aXZlQg4KDF91c2RfZnhfcmF0ZUIKCghfY291bnRyeWIGcHJvdG8z","chesscom/payments/v1/request_location.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9yZXF1ZXN0X2xvY2F0aW9uLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSJVCg9SZXF1ZXN0TG9jYXRpb24SFQoIemlwX2NvZGUYASABKAlIAIgBARITCgZyZWdpb24YAiABKAlIAYgBAUILCglfemlwX2NvZGVCCQoHX3JlZ2lvbmIGcHJvdG8z","chesscom/payments/v1/country_price.proto":"CihjaGVzc2Nv
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18028"></a>
## FND-18028: Full frontend descriptor: chesscom/payments/v1/country_price.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/country_price.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "CountryPrice",
      "field": [
        {
          "name": "country_code",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "original_price",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "current_price",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "special_price",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 798822.

```text
IemlwX2NvZGUYASABKAlIAIgBARITCgZyZWdpb24YAiABKAlIAYgBAUILCglfemlwX2NvZGVCCQoHX3JlZ2lvbmIGcHJvdG8z","chesscom/payments/v1/country_price.proto":"CihjaGVzc2NvbS9wYXltZW50cy92MS9jb3VudHJ5X3ByaWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSKyAQoMQ291bnRyeVByaWNlEhQKDGNvdW50cnlfY29kZRgBIAEoCRIuCg5vcmlnaW5hbF9wcmljZRgCIAEoCzIWLmNoZXNzY29tLmFwaS52MS5Nb25leRItCg1jdXJyZW50X3ByaWNlGAMgASgLMhYuY2hlc3Njb20uYXBpLnYxLk1vbmV5Ei0KDXNwZWNpY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18029"></a>
## FND-18029: Full frontend descriptor: chesscom/payments/v1/product_prices.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/product_prices.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "ProductPrices",
      "field": [
        {
          "name": "sku",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "country_prices",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.CountryPrice"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 799206.

```text
3Njb20uYXBpLnYxLk1vbmV5Ei0KDXNwZWNpYWxfcHJpY2UYBCABKAsyFi5jaGVzc2NvbS5hcGkudjEuTW9uZXliBnByb3RvMw","chesscom/payments/v1/product_prices.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0X3ByaWNlcy5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEiWAoNUHJvZHVjdFByaWNlcxILCgNza3UYASABKAkSOgoOY291bnRyeV9wcmljZXMYAiADKAsyIi5jaGVzc2NvbS5wYXltZW50cy52MS5Db3VudHJ5UHJpY2ViBnByb3RvMw","chesscom/payments/v1/charge.proto":"CiFjaGVzc2NvbS9wYXl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18030"></a>
## FND-18030: Full frontend descriptor: chesscom/payments/v1/charge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/charge.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "Charge",
      "field": [
        {
          "name": "charge_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "amount_cents",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "currency",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "charged_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "gateway",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "payment_method",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.ChargePlatform"
        },
        {
          "name": "refunded_cents",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "is_trial",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "plan",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "subscription_id",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "auto_refund_eligible",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "ineligibility_reason",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.support.v1.RefundIneligibilityReason"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ChargePlatform",
      "value": [
        {
          "name": "CHARGE_PLATFORM_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CHARGE_PLATFORM_WEB",
          "number": 1
        },
        {
          "name": "CHARGE_PLATFORM_APPLE",
          "number": 2
        },
        {
          "name": "CHARGE_PLATFORM_GOOGLE",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 799471.

```text
SABKAkSOgoOY291bnRyeV9wcmljZXMYAiADKAsyIi5jaGVzc2NvbS5wYXltZW50cy52MS5Db3VudHJ5UHJpY2ViBnByb3RvMw","chesscom/payments/v1/charge.proto":"CiFjaGVzc2NvbS9wYXltZW50cy92MS9jaGFyZ2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIpEDCgZDaGFyZ2USEQoJY2hhcmdlX2lkGAEgASgJEhQKDGFtb3VudF9jZW50cxgCIAEoBRIQCghjdXJyZW5jeRgDIAEoCRIuCgpjaGFyZ2VkX2F0GAQgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcBIPCgdnYXRld2F5GAUgASgJEhYKDnBheW1lbnRfbWV0aG9kGAYg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18031"></a>
## FND-18031: Full frontend descriptor: chesscom/payments/v1/found_charge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/found_charge.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "FoundCharge",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "charge",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Charge"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 800312.

```text
k9STV9XRUIQARIZChVDSEFSR0VfUExBVEZPUk1fQVBQTEUQAhIaChZDSEFSR0VfUExBVEZPUk1fR09PR0xFEANiBnByb3RvMw","chesscom/payments/v1/found_charge.proto":"CidjaGVzc2NvbS9wYXltZW50cy92MS9mb3VuZF9jaGFyZ2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIk4KC0ZvdW5kQ2hhcmdlEhEKCXVzZXJfdXVpZBgBIAEoCRIsCgZjaGFyZ2UYAiABKAsyHC5jaGVzc2NvbS5wYXltZW50cy52MS5DaGFyZ2ViBnByb3RvMw","chesscom/payments/v1/invoice_bill_to.proto":"CipjaGVzc2NvbS9wYXltZW50cy92
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18032"></a>
## FND-18032: Full frontend descriptor: chesscom/payments/v1/invoice_bill_to.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/invoice_bill_to.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "InvoiceBillTo",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "address_lines",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "country_code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "tax_id",
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
  Character offset 800559.

```text
hEKCXVzZXJfdXVpZBgBIAEoCRIsCgZjaGFyZ2UYAiABKAsyHC5jaGVzc2NvbS5wYXltZW50cy52MS5DaGFyZ2ViBnByb3RvMw","chesscom/payments/v1/invoice_bill_to.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9pbnZvaWNlX2JpbGxfdG8ucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIloKDUludm9pY2VCaWxsVG8SDAoEbmFtZRgBIAEoCRIVCg1hZGRyZXNzX2xpbmVzGAIgAygJEhQKDGNvdW50cnlfY29kZRgDIAEoCRIOCgZ0YXhfaWQYBCABKAliBnByb3RvMw","chesscom/payments/v1/subscription_admin.proto":"Ci
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18033"></a>
## FND-18033: Full frontend descriptor: chesscom/payments/v1/subscription_admin.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/subscription_admin.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "PaidOrderBasis",
      "field": [
        {
          "name": "charge_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "PartnerMembershipBasis",
      "field": [
        {
          "name": "partner",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MembershipPartner"
        },
        {
          "name": "charge_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "revolut_code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "reference"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CancelSubscriptionResult",
      "value": [
        {
          "name": "CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CANCEL_SUBSCRIPTION_RESULT_CANCELLED",
          "number": 1
        },
        {
          "name": "CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED",
          "number": 2
        }
      ]
    },
    {
      "name": "SubscriptionAdminRefusalReason",
      "value": [
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION",
          "number": 1
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE",
          "number": 2
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED",
          "number": 3
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE",
          "number": 4
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED",
          "number": 5
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT",
          "number": 6
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION",
          "number": 7
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED",
          "number": 8
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH",
          "number": 9
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED",
          "number": 10
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE",
          "number": 11
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED",
          "number": 12
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID",
          "number": 13
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED",
          "number": 14
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE",
          "number": 15
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED",
          "number": 16
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE",
          "number": 17
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN",
          "number": 18
        },
        {
          "name": "SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE",
          "number": 19
        }
      ]
    },
    {
      "name": "StopRenewalByCardMatchResult",
      "value": [
        {
          "name": "STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED",
          "number": 1
        },
        {
          "name": "STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING",
          "number": 2
        },
        {
          "name": "STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED",
          "number": 3
        },
        {
          "name": "STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH",
          "number": 4
        }
      ]
    },
    {
      "name": "SwitchToMonthlyResult",
      "value": [
        {
          "name": "SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SWITCH_TO_MONTHLY_RESULT_SWITCHED",
          "number": 1
        },
        {
          "name": "SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND",
          "number": 2
        },
        {
          "name": "SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED",
          "number": 3
        }
      ]
    },
    {
      "name": "MonthlySwitchIneligibility",
      "value": [
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION",
          "number": 1
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION",
          "number": 2
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION",
          "number": 3
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION",
          "number": 4
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM",
          "number": 5
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY",
          "number": 6
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED",
          "number": 7
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN",
          "number": 8
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED",
          "number": 9
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE",
          "number": 10
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED",
          "number": 11
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND",
          "number": 12
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE",
          "number": 13
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED",
          "number": 14
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND",
          "number": 15
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN",
          "number": 16
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED",
          "number": 17
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH",
          "number": 18
        },
        {
          "name": "MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED",
          "number": 19
        }
      ]
    },
    {
      "name": "MembershipPartner",
      "value": [
        {
          "name": "MEMBERSHIP_PARTNER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MEMBERSHIP_PARTNER_REVOLUT",
          "number": 1
        },
        {
          "name": "MEMBERSHIP_PARTNER_UNIDAYS",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 800829.

```text
AEoCRIVCg1hZGRyZXNzX2xpbmVzGAIgAygJEhQKDGNvdW50cnlfY29kZRgDIAEoCRIOCgZ0YXhfaWQYBCABKAliBnByb3RvMw","chesscom/payments/v1/subscription_admin.proto":"Ci1jaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW4ucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIiMKDlBhaWRPcmRlckJhc2lzEhEKCWNoYXJnZV9pZBgBIAEoCSKMAQoWUGFydG5lck1lbWJlcnNoaXBCYXNpcxI4CgdwYXJ0bmVyGAEgASgOMicuY2hlc3Njb20ucGF5bWVudHMudjEuTWVtYmVyc2hpcFBhcnRuZXISEwoJY2hhcmdlX2lk
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18034"></a>
## FND-18034: Full frontend descriptor: chesscom/payments/v1/billing_history_entry.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/billing_history_entry.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "BillingHistoryEntry",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "display_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "order_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.OrderType",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "price",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money"
        },
        {
          "name": "placed_by",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.BillingHistoryEntryUser"
        },
        {
          "name": "gift_receiver",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.BillingHistoryEntryUser",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "created_date",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "invoice_available",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "oneof_decl": [
        {
          "name": "_display_name"
        },
        {
          "name": "_order_type"
        },
        {
          "name": "_gift_receiver"
        }
      ]
    },
    {
      "name": "BillingHistoryEntryUser",
      "field": [
        {
          "name": "username",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "email",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_email"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 805418.

```text
BIeChpNRU1CRVJTSElQX1BBUlRORVJfUkVWT0xVVBABEh4KGk1FTUJFUlNISVBfUEFSVE5FUl9VTklEQVlTEAJiBnByb3RvMw","chesscom/payments/v1/billing_history_entry.proto":"CjBjaGVzc2NvbS9wYXltZW50cy92MS9iaWxsaW5nX2hpc3RvcnlfZW50cnkucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIqkDChNCaWxsaW5nSGlzdG9yeUVudHJ5EgoKAmlkGAEgASgFEhkKDGRpc3BsYXlfbmFtZRgCIAEoCUgAiAEBEjgKCm9yZGVyX3R5cGUYAyABKA4yHy5jaGVzc2NvbS5wYXltZW50cy52MS5PcmRlclR5cGVIAYgBARIlCgVwcmljZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18035"></a>
## FND-18035: Full frontend descriptor: chesscom/payments/v1/billing_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/billing_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "GetUserBillingHistoryRequest"
    },
    {
      "name": "GetUserBillingHistoryResponse",
      "field": [
        {
          "name": "billing_history",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.BillingHistoryEntry"
        }
      ]
    },
    {
      "name": "GetUserBillingInformationRequest"
    },
    {
      "name": "GetUserBillingInformationResponse",
      "field": [
        {
          "name": "payment_method",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.PaymentMethod",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "country",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Country"
        },
        {
          "name": "is_tax_included_in_price",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "subscription_payment_status",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionPaymentStatus"
        }
      ],
      "oneof_decl": [
        {
          "name": "_payment_method"
        },
        {
          "name": "_is_tax_included_in_price"
        }
      ]
    },
    {
      "name": "GetOrderInvoiceRequest",
      "field": [
        {
          "name": "order_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "bill_to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.InvoiceBillTo"
        }
      ]
    },
    {
      "name": "GetOrderInvoiceResponse",
      "field": [
        {
          "name": "pdf",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES"
        },
        {
          "name": "file_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "BillingService",
      "method": [
        {
          "name": "GetUserBillingHistory",
          "input_type": ".chesscom.payments.v1.GetUserBillingHistoryRequest",
          "output_type": ".chesscom.payments.v1.GetUserBillingHistoryResponse"
        },
        {
          "name": "GetUserBillingInformation",
          "input_type": ".chesscom.payments.v1.GetUserBillingInformationRequest",
          "output_type": ".chesscom.payments.v1.GetUserBillingInformationResponse"
        },
        {
          "name": "GetOrderInvoice",
          "input_type": ".chesscom.payments.v1.GetOrderInvoiceRequest",
          "output_type": ".chesscom.payments.v1.GetOrderInvoiceResponse",
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
  Character offset 806250.

```text
0hpc3RvcnlFbnRyeVVzZXISEAoIdXNlcm5hbWUYASABKAkSEgoFZW1haWwYAiABKAlIAIgBAUIICgZfZW1haWxiBnByb3RvMw","chesscom/payments/v1/billing_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9iaWxsaW5nX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIh4KHEdldFVzZXJCaWxsaW5nSGlzdG9yeVJlcXVlc3QiYwodR2V0VXNlckJpbGxpbmdIaXN0b3J5UmVzcG9uc2USQgoPYmlsbGluZ19oaXN0b3J5GAEgAygLMikuY2hlc3Njb20ucGF5bWVudHMudjEuQmlsbGluZ0hpc3RvcnlFbnRyeSIiCiBHZXR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18039"></a>
## FND-18039: Full frontend descriptor: chesscom/payments/v1/support_family_plan.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/support_family_plan.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "SupportFamilyPlanInvitation",
      "field": [
        {
          "name": "invitation_ref",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invitee_user_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invitee_username",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "masked_email",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "expires_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    },
    {
      "name": "SupportFamilyPlanInviteeCheck",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "status",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SupportFamilyPlanJoinStatus"
        },
        {
          "name": "trial_cooldown_ends_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SupportFamilyPlanState",
      "value": [
        {
          "name": "SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_STATE_NONE",
          "number": 1
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_STATE_TRIAL",
          "number": 2
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_STATE_PAID",
          "number": 3
        }
      ]
    },
    {
      "name": "SupportFamilyPlanJoinStatus",
      "value": [
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN",
          "number": 1
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN",
          "number": 2
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER",
          "number": 3
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM",
          "number": 4
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY",
          "number": 5
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL",
          "number": 6
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER",
          "number": 7
        }
      ]
    },
    {
      "name": "SupportFamilyPlanRevokeResult",
      "value": [
        {
          "name": "SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED",
          "number": 1
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND",
          "number": 2
        }
      ]
    },
    {
      "name": "SupportFamilyPlanCooldownResult",
      "value": [
        {
          "name": "SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED",
          "number": 1
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN",
          "number": 2
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN",
          "number": 3
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL",
          "number": 4
        },
        {
          "name": "SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER",
          "number": 5
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 807846.

```text
0cy52MS5HZXRPcmRlckludm9pY2VSZXNwb25zZSIDkAICQh3KtywZCgQvcnBjEg8SDWFwaS5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/support_family_plan.proto":"Ci5jaGVzc2NvbS9wYXltZW50cy92MS9zdXBwb3J0X2ZhbWlseV9wbGFuLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSKwAQobU3VwcG9ydEZhbWlseVBsYW5JbnZpdGF0aW9uEhYKDmludml0YXRpb25fcmVmGAEgASgJEhkKEWludml0ZWVfdXNlcl91dWlkGAIgASgJEhgKEGludml0ZWVfdXNlcm5hbWUYAyABKAkSFAoMbWFza2VkX2VtYWlsGAQgASgJEi4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18040"></a>
## FND-18040: Full frontend descriptor: chesscom/payments/v1/member_subscription.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/member_subscription.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "MemberSubscription",
      "field": [
        {
          "name": "subscription_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "membership_level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MembershipLevel"
        },
        {
          "name": "plan_state",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.PlanState"
        },
        {
          "name": "plan_length",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "plan_unit",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionDurationUnit"
        },
        {
          "name": "price_cents",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "currency",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.ChargePlatform"
        },
        {
          "name": "gateway",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.PaymentGateway"
        },
        {
          "name": "started_at",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "current_period_ends_at",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "cancelled_at",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "cancellation_effect",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.CancellationEffect"
        },
        {
          "name": "trial_state",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.TrialState"
        },
        {
          "name": "payment_status",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionPaymentStatus"
        }
      ],
      "oneof_decl": [
        {
          "name": "_price_cents"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 810033.

```text
5TVVBQT1JUX0ZBTUlMWV9QTEFOX0NPT0xET1dOX1JFU1VMVF9GUklFTkRfTk9UX0ZST01fVEhJU19PV05FUhAFYgZwcm90bzM","chesscom/payments/v1/member_subscription.proto":"Ci5jaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJfc3Vic2NyaXB0aW9uLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSKLBgoSTWVtYmVyU3Vic2NyaXB0aW9uEhcKD3N1YnNjcmlwdGlvbl9pZBgBIAEoCRI/ChBtZW1iZXJzaGlwX2xldmVsGAIgASgOMiUuY2hlc3Njb20ucGF5bWVudHMudjEuTWVtYmVyc2hpcExldmVsEjMKCnBsYW5fc3RhdGUYAyABKA4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18041"></a>
## FND-18041: Full frontend descriptor: chesscom/payments/v1/refund_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/refund_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "IssueRefundRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "charge_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "amount_cents",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "context",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "cancellation_effect",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.CancellationEffect"
        }
      ],
      "reserved_range": [
        {
          "start": 3,
          "end": 4
        },
        {
          "start": 5,
          "end": 6
        },
        {
          "start": 7,
          "end": 8
        }
      ],
      "reserved_name": [
        "actor",
        "reason",
        "dry_run"
      ]
    },
    {
      "name": "IssueRefundResponse",
      "field": [
        {
          "name": "already_refunded",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "refunded_cents",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "action_result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        },
        {
          "name": "refund_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ListChargesRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "limit",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    },
    {
      "name": "ListChargesResponse",
      "field": [
        {
          "name": "charges",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Charge"
        }
      ]
    },
    {
      "name": "FindChargesRequest",
      "field": [
        {
          "name": "adyen_psp_reference",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          },
          "oneof_index": 0
        },
        {
          "name": "google_play_order_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          },
          "oneof_index": 0
        },
        {
          "name": "apple_transaction_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          },
          "oneof_index": 0
        },
        {
          "name": "apple_order_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          },
          "oneof_index": 0
        },
        {
          "name": "chesscom_order_number",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          },
          "oneof_index": 0
        },
        {
          "name": "user_uuid",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        }
      ],
      "oneof_decl": [
        {
          "name": "identifier"
        }
      ]
    },
    {
      "name": "FindChargesResponse",
      "field": [
        {
          "name": "charges",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.FoundCharge"
        },
        {
          "name": "privacy_withheld",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "action_result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    },
    {
      "name": "ListSubscriptionsRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ListSubscriptionsResponse",
      "field": [
        {
          "name": "subscriptions",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.MemberSubscription"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "RefundService",
      "method": [
        {
          "name": "IssueRefund",
          "input_type": ".chesscom.payments.v1.IssueRefundRequest",
          "output_type": ".chesscom.payments.v1.IssueRefundResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "ListCharges",
          "input_type": ".chesscom.payments.v1.ListChargesRequest",
          "output_type": ".chesscom.payments.v1.ListChargesResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "FindCharges",
          "input_type": ".chesscom.payments.v1.FindChargesRequest",
          "output_type": ".chesscom.payments.v1.FindChargesResponse",
          "options": {}
        },
        {
          "name": "ListSubscriptions",
          "input_type": ".chesscom.payments.v1.ListSubscriptionsRequest",
          "output_type": ".chesscom.payments.v1.ListSubscriptionsResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
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
  Character offset 811232.

```text
IvLmNoZXNzY29tLnBheW1lbnRzLnYxLlN1YnNjcmlwdGlvblBheW1lbnRTdGF0dXNCDgoMX3ByaWNlX2NlbnRzYgZwcm90bzM","chesscom/payments/v1/refund_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9yZWZ1bmRfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi/QEKEklzc3VlUmVmdW5kUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSEQoJY2hhcmdlX2lkGAIgASgJEhQKDGFtb3VudF9jZW50cxgEIAEoBRI6Cgdjb250ZXh0GAYgASgLMikuY2hlc3Njb20uc3VwcG9ydC52MS5TdXBwb3J0QWN0aW9uQ29udGV4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18046"></a>
## FND-18046: Full frontend descriptor: chesscom/payments/v1/group_membership_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/group_membership_type.proto",
  "package": "chesscom.payments.v1",
  "enum_type": [
    {
      "name": "GroupMembershipType",
      "value": [
        {
          "name": "GROUP_MEMBERSHIP_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GROUP_MEMBERSHIP_TYPE_PRIMARY",
          "number": 1
        },
        {
          "name": "GROUP_MEMBERSHIP_TYPE_SECONDARY",
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
  Character offset 827221.

```text
GNoYXJnZTIIY2hlc3Njb21CLsq3LCoKBC9ycGMSDxINYXBpLmNoZXNzLmNvbRoNEgtiZWFyZXJfYXV0aCoCkE5iBnByb3RvMw","chesscom/payments/v1/group_membership_type.proto":"CjBjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3R5cGUucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxKo0BChNHcm91cE1lbWJlcnNoaXBUeXBlEiUKIUdST1VQX01FTUJFUlNISVBfVFlQRV9VTlNQRUNJRklFRBAAEiEKHUdST1VQX01FTUJFUlNISVBfVFlQRV9QUklNQVJZEAESIwofR1JPVVBfTUVNQkVSU0hJUF9UWVBFX1NFQ09OR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18047"></a>
## FND-18047: Full frontend descriptor: chesscom/payments/v1/product_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/product_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "GetUserActiveMembershipRequest",
      "options": {}
    },
    {
      "name": "GetUserActiveMembershipResponse",
      "field": [
        {
          "name": "membership_level",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MembershipLevel"
        },
        {
          "name": "product",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Product",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "membership_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "will_expire",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_lifetime",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "status_code",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.StatusCode",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "group_membership_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.GroupMembershipType",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "renewal_date",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "renewal_price",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Money",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "expiry_date",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "membership_description",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "is_gift",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "is_free",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "has_active_billing",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "disallow_cancellation_reason",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "primary_account_holder",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView",
          "oneof_index": 12,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_product"
        },
        {
          "name": "_will_expire"
        },
        {
          "name": "_status_code"
        },
        {
          "name": "_group_membership_type"
        },
        {
          "name": "_renewal_date"
        },
        {
          "name": "_renewal_price"
        },
        {
          "name": "_expiry_date"
        },
        {
          "name": "_membership_description"
        },
        {
          "name": "_is_gift"
        },
        {
          "name": "_is_free"
        },
        {
          "name": "_has_active_billing"
        },
        {
          "name": "_disallow_cancellation_reason"
        },
        {
          "name": "_primary_account_holder"
        }
      ]
    },
    {
      "name": "GetUserIsEligibleToRestartMembershipRequest",
      "options": {}
    },
    {
      "name": "GetUserIsEligibleToRestartMembershipResponse",
      "field": [
        {
          "name": "is_eligible",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "RestartMembershipRequest",
      "options": {}
    },
    {
      "name": "RestartMembershipResponse",
      "options": {}
    }
  ],
  "service": [
    {
      "name": "ProductService",
      "method": [
        {
          "name": "GetUserActiveMembership",
          "input_type": ".chesscom.payments.v1.GetUserActiveMembershipRequest",
          "output_type": ".chesscom.payments.v1.GetUserActiveMembershipResponse"
        },
        {
          "name": "GetUserIsEligibleToRestartMembership",
          "input_type": ".chesscom.payments.v1.GetUserIsEligibleToRestartMembershipRequest",
          "output_type": ".chesscom.payments.v1.GetUserIsEligibleToRestartMembershipResponse"
        },
        {
          "name": "RestartMembership",
          "input_type": ".chesscom.payments.v1.RestartMembershipRequest",
          "output_type": ".chesscom.payments.v1.RestartMembershipResponse"
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
  Character offset 827574.

```text
NISVBfVFlQRV9QUklNQVJZEAESIwofR1JPVVBfTUVNQkVSU0hJUF9UWVBFX1NFQ09OREFSWRACGgeKph0DCgEBYgZwcm90bzM","chesscom/payments/v1/product_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0X3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIikKHkdldFVzZXJBY3RpdmVNZW1iZXJzaGlwUmVxdWVzdDoHgqYdAwoBASLxBwofR2V0VXNlckFjdGl2ZU1lbWJlcnNoaXBSZXNwb25zZRI/ChBtZW1iZXJzaGlwX2xldmVsGAEgASgOMiUuY2hlc3Njb20ucGF5bWVudHMudjEuTWVtYmVyc2hpcEx
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18051"></a>
## FND-18051: Full frontend descriptor: chesscom/payments/v1/available_payment_method.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/available_payment_method.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "AvailablePaymentMethod",
      "field": [
        {
          "name": "gateway",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "method",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "config",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PaymentMethodConfig"
        }
      ]
    },
    {
      "name": "PaymentMethodConfig",
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
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "image",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "parameters",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PaymentParameters",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "additional_data_required",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.AdditionalDataField"
        },
        {
          "name": "stored_payment_details",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.StoredPaymentDetail"
        },
        {
          "name": "cvv_confirmation_required",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "captcha",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_parameters"
        },
        {
          "name": "_cvv_confirmation_required"
        },
        {
          "name": "_captcha"
        }
      ]
    },
    {
      "name": "PaymentParameters",
      "field": [
        {
          "name": "environment",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "integrity",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "client_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "key",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "merchant",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "origin_key",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "sdk",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "script_src",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "merchant_id",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "merchant_name",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 9,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_environment"
        },
        {
          "name": "_integrity"
        },
        {
          "name": "_client_id"
        },
        {
          "name": "_key"
        },
        {
          "name": "_merchant"
        },
        {
          "name": "_origin_key"
        },
        {
          "name": "_sdk"
        },
        {
          "name": "_script_src"
        },
        {
          "name": "_merchant_id"
        },
        {
          "name": "_merchant_name"
        }
      ]
    },
    {
      "name": "AdditionalDataField",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "label",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.AdditionalDataFieldType"
        },
        {
          "name": "required",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "options",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.AdditionalDataFieldSelectOption"
        },
        {
          "name": "validation_rule",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "validation_err_msg",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_validation_rule"
        },
        {
          "name": "_validation_err_msg"
        }
      ]
    },
    {
      "name": "AdditionalDataFieldSelectOption",
      "field": [
        {
          "name": "label",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "StoredPaymentDetail",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "number",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "owner_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_number"
        },
        {
          "name": "_owner_name"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 830054.

```text
udjEuUmVzdGFydE1lbWJlcnNoaXBSZXNwb25zZRoHkqYdAwoBAUIZyrcsFQoEL3JwYxILEgljaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/available_payment_method.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9hdmFpbGFibGVfcGF5bWVudF9tZXRob2QucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxInQKFkF2YWlsYWJsZVBheW1lbnRNZXRob2QSDwoHZ2F0ZXdheRgBIAEoCRIOCgZtZXRob2QYAiABKAkSOQoGY29uZmlnGAMgASgLMikuY2hlc3Njb20ucGF5bWVudHMudjEuUGF5bWVudE1ldGhvZENvbmZpZyKdAwoTUG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18052"></a>
## FND-18052: Full frontend descriptor: chesscom/payments/v1/membership_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/membership_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "CancelMembershipRequest"
    },
    {
      "name": "CancelMembershipResponse"
    },
    {
      "name": "SubmitCancellationSurveyRequest",
      "field": [
        {
          "name": "reason",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.CancelSurveyReason"
        },
        {
          "name": "feedback",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_feedback"
        }
      ]
    },
    {
      "name": "SubmitCancellationSurveyResponse"
    },
    {
      "name": "ExtendMembershipRequest"
    },
    {
      "name": "ExtendMembershipResponse"
    }
  ],
  "service": [
    {
      "name": "MembershipService",
      "method": [
        {
          "name": "CancelMembership",
          "input_type": ".chesscom.payments.v1.CancelMembershipRequest",
          "output_type": ".chesscom.payments.v1.CancelMembershipResponse"
        },
        {
          "name": "SubmitCancellationSurvey",
          "input_type": ".chesscom.payments.v1.SubmitCancellationSurveyRequest",
          "output_type": ".chesscom.payments.v1.SubmitCancellationSurveyResponse"
        },
        {
          "name": "ExtendMembership",
          "input_type": ".chesscom.payments.v1.ExtendMembershipRequest",
          "output_type": ".chesscom.payments.v1.ExtendMembershipResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 832105.

```text
mVyGAIgASgJSACIAQESFwoKb3duZXJfbmFtZRgDIAEoCUgBiAEBQgkKB19udW1iZXJCDQoLX293bmVyX25hbWViBnByb3RvMw","chesscom/payments/v1/membership_service.proto":"Ci1jaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIhkKF0NhbmNlbE1lbWJlcnNoaXBSZXF1ZXN0IhoKGENhbmNlbE1lbWJlcnNoaXBSZXNwb25zZSJ/Ch9TdWJtaXRDYW5jZWxsYXRpb25TdXJ2ZXlSZXF1ZXN0EjgKBnJlYXNvbhgBIAEoDjIoLmNoZXNzY29tLnBheW1lbnRzLnYxLkNhbmNl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18056"></a>
## FND-18056: Full frontend descriptor: chesscom/payments/v1/group_membership_invitation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/group_membership_invitation.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "InvitationPlanDetails",
      "field": [
        {
          "name": "max_secondary_members",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "JoinEligibility",
      "field": [
        {
          "name": "is_eligible",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "status",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.JoinEligibilityStatus",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_status"
        }
      ]
    },
    {
      "name": "PendingInvitationForInvitee",
      "field": [
        {
          "name": "invitation_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "primary_account_holder",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        },
        {
          "name": "plan_details",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.InvitationPlanDetails"
        },
        {
          "name": "expires_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ],
      "options": {}
    },
    {
      "name": "PendingInviteeIdentity",
      "field": [
        {
          "name": "user",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView",
          "oneof_index": 0
        },
        {
          "name": "email",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "identity"
        }
      ]
    },
    {
      "name": "PendingInvitation",
      "field": [
        {
          "name": "invitation_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invitee",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "expires_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "invitee_identity",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PendingInviteeIdentity"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "JoinEligibilityStatus",
      "value": [
        {
          "name": "JOIN_ELIGIBILITY_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM",
          "number": 1
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION",
          "number": 2
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_INVALID_TYPE",
          "number": 3
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN",
          "number": 4
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED",
          "number": 5
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION",
          "number": 6
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY",
          "number": 7
        },
        {
          "name": "JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN",
          "number": 8
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 833184.

```text
tLnBheW1lbnRzLnYxLkV4dGVuZE1lbWJlcnNoaXBSZXNwb25zZUIZyrcsFQoEL3JwYxILEgljaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/group_membership_invitation.proto":"CjZjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX2ludml0YXRpb24ucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIj8KFUludml0YXRpb25QbGFuRGV0YWlscxIdChVtYXhfc2Vjb25kYXJ5X21lbWJlcnMYASABKAU6B4KmHQMKAQEifAoPSm9pbkVsaWdpYmlsaXR5EhMKC2lzX2VsaWdpYmxlGAEgASgIEkAKBnN0YXR1cxgCIAE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18057"></a>
## FND-18057: Full frontend descriptor: chesscom/payments/v1/member_promotion.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/member_promotion.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "MemberPromotion",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.IncentiveType"
        },
        {
          "name": "discount_percent",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "free_time_days",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "ends_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "redeemable_platforms",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        }
      ]
    },
    {
      "name": "PromotionOnCharge",
      "field": [
        {
          "name": "charge_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "charged_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "promotion",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.MemberPromotion"
        },
        {
          "name": "coupon_code_used",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "platform",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 834979.

```text
JZX1BSSU1BUlkQBxIqCiZKT0lOX0VMSUdJQklMSVRZX1NUQVRVU19UUklBTF9DT09MRE9XThAIGgeKph0DCgEBYgZwcm90bzM","chesscom/payments/v1/member_promotion.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJfcHJvbW90aW9uLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLqAQoPTWVtYmVyUHJvbW90aW9uEgwKBG5hbWUYASABKAkSMQoEdHlwZRgCIAEoDjIjLmNoZXNzY29tLnBheW1lbnRzLnYxLkluY2VudGl2ZVR5cGUSGAoQZGlzY291bnRfcGVyY2VudBgDIAEoAhIWCg5mcmVlX3RpbWVfZGF5cxgEIAEoBRIrCg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18058"></a>
## FND-18058: Full frontend descriptor: chesscom/payments/v1/support_promotion_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/support_promotion_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "CheckMemberPromotionsRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          }
        },
        {
          "name": "context",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "verification_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        }
      ]
    },
    {
      "name": "CheckMemberPromotionsResponse",
      "field": [
        {
          "name": "offers",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.MemberPromotion"
        },
        {
          "name": "applied",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PromotionOnCharge"
        },
        {
          "name": "code_applied",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "action_result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "SupportPromotionService",
      "method": [
        {
          "name": "CheckMemberPromotions",
          "input_type": ".chesscom.payments.v1.CheckMemberPromotionsRequest",
          "output_type": ".chesscom.payments.v1.CheckMemberPromotionsResponse",
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
  Character offset 835735.

```text
Vwb25fY29kZV91c2VkGAQgASgIEisKCHBsYXRmb3JtGAUgASgOMhkuY2hlc3Njb20uYXBpLnYxLlBsYXRmb3JtYgZwcm90bzM","chesscom/payments/v1/support_promotion_service.proto":"CjRjaGVzc2NvbS9wYXltZW50cy92MS9zdXBwb3J0X3Byb21vdGlvbl9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLMAQocQ2hlY2tNZW1iZXJQcm9tb3Rpb25zUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSFwoEY29kZRgCIAEoCUIJgAEByrsYAggDEjoKB2NvbnRleHQYAyABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18060"></a>
## FND-18060: Full frontend descriptor: chesscom/payments/v1/storefront_country.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/storefront_country.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "StorefrontCountry",
      "field": [
        {
          "name": "country_code",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "currency_code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "tax_inclusive_prices",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "should_display_checkout_disclaimer",
          "number": 4,
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
  Character offset 840908.

```text
VzIHVzZWQyCGNoZXNzY29tQi7KtywqCgQvcnBjEg8SDWFwaS5jaGVzcy5jb20aDRILYmVhcmVyX2F1dGgqApBOYgZwcm90bzM","chesscom/payments/v1/storefront_country.proto":"Ci1jaGVzc2NvbS9wYXltZW50cy92MS9zdG9yZWZyb250X2NvdW50cnkucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIooBChFTdG9yZWZyb250Q291bnRyeRIUCgxjb3VudHJ5X2NvZGUYASABKAkSFQoNY3VycmVuY3lfY29kZRgCIAEoCRIcChR0YXhfaW5jbHVzaXZlX3ByaWNlcxgDIAEoCBIqCiJzaG91bGRfZGlzcGxheV9jaGVja291dF9kaXNjbGFpbWVy
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18061"></a>
## FND-18061: Full frontend descriptor: chesscom/payments/v1/goodwill.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/goodwill.proto",
  "package": "chesscom.payments.v1",
  "enum_type": [
    {
      "name": "GoodwillSiteFault",
      "value": [
        {
          "name": "GOODWILL_SITE_FAULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GOODWILL_SITE_FAULT_OUTAGE",
          "number": 1
        },
        {
          "name": "GOODWILL_SITE_FAULT_BUG",
          "number": 2
        },
        {
          "name": "GOODWILL_SITE_FAULT_FAILED_OPERATION",
          "number": 3
        },
        {
          "name": "GOODWILL_SITE_FAULT_WRONG_ACTION",
          "number": 4
        }
      ]
    },
    {
      "name": "GrantGoodwillDiamondResult",
      "value": [
        {
          "name": "GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED",
          "number": 1
        },
        {
          "name": "GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841250.

```text
5jbHVzaXZlX3ByaWNlcxgDIAEoCBIqCiJzaG91bGRfZGlzcGxheV9jaGVja291dF9kaXNjbGFpbWVyGAQgASgIYgZwcm90bzM","chesscom/payments/v1/goodwill.proto":"CiNjaGVzc2NvbS9wYXltZW50cy92MS9nb29kd2lsbC5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEqxQEKEUdvb2R3aWxsU2l0ZUZhdWx0EiMKH0dPT0RXSUxMX1NJVEVfRkFVTFRfVU5TUEVDSUZJRUQQABIeChpHT09EV0lMTF9TSVRFX0ZBVUxUX09VVEFHRRABEhsKF0dPT0RXSUxMX1NJVEVfRkFVTFRfQlVHEAISKAokR09PRFdJTExfU0lURV9GQVVMVF9GQUlMRURfT1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18062"></a>
## FND-18062: Full frontend descriptor: chesscom/payments/v1/subscription_admin_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/subscription_admin_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "CancelSubscriptionRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "subscription_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "CancelSubscriptionResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.CancelSubscriptionResult"
        },
        {
          "name": "access_ends_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "action_result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        },
        {
          "name": "refusal_reason",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        }
      ]
    },
    {
      "name": "StopRenewalByCardMatchRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "card_last_four",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          }
        },
        {
          "name": "charge_amount_cents",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "debug_redact": true
          }
        },
        {
          "name": "charge_currency",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          }
        },
        {
          "name": "charge_date",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "debug_redact": true
          }
        },
        {
          "name": "context",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        }
      ]
    },
    {
      "name": "StopRenewalByCardMatchResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.StopRenewalByCardMatchResult"
        },
        {
          "name": "access_ends_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "action_result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    },
    {
      "name": "ExtendSubscriptionRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "days",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "context",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "subscription_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ExtendSubscriptionResponse",
      "field": [
        {
          "name": "days_added",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "action_result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        },
        {
          "name": "current_period_ends_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "refusal_reason",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        }
      ]
    },
    {
      "name": "GrantGoodwillDiamondRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "fault",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.GoodwillSiteFault"
        }
      ]
    },
    {
      "name": "GrantGoodwillDiamondResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.GrantGoodwillDiamondResult"
        },
        {
          "name": "days_granted",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "plan",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "access_ends_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "refusal_reason",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        },
        {
          "name": "next_eligible_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "action_result",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    },
    {
      "name": "GrantNoAdsOfferRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        }
      ]
    },
    {
      "name": "GrantNoAdsOfferResponse",
      "field": [
        {
          "name": "days_granted",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "plan",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "access_ends_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "refusal_reason",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        },
        {
          "name": "next_eligible_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "action_result",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    },
    {
      "name": "TransferMembershipRequest",
      "field": [
        {
          "name": "from_user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "to_user_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "from_verification_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "to_verification_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "TransferMembershipResponse",
      "field": [
        {
          "name": "subscriptions_transferred",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "action_result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        },
        {
          "name": "refusal_reason",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        }
      ]
    },
    {
      "name": "GrantMembershipRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "paid_order",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PaidOrderBasis",
          "oneof_index": 0
        },
        {
          "name": "partner_membership",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PartnerMembershipBasis",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "basis"
        }
      ]
    },
    {
      "name": "GrantMembershipResponse",
      "field": [
        {
          "name": "plan",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "subscription_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "access_ends_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "action_result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        },
        {
          "name": "refusal_reason",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        }
      ]
    },
    {
      "name": "SwitchToMonthlyRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        },
        {
          "name": "subscription_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SwitchToMonthlyResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SwitchToMonthlyResult"
        },
        {
          "name": "current_plan",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "target_plan",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "refund_cents",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "currency",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "refund_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "action_result",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        },
        {
          "name": "refusal_reason",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SubscriptionAdminRefusalReason"
        },
        {
          "name": "ineligibility",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MonthlySwitchIneligibility"
        }
      ]
    },
    {
      "name": "GetFamilyPlanInvitationsRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invitee_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "verification_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetFamilyPlanInvitationsResponse",
      "field": [
        {
          "name": "plan_state",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SupportFamilyPlanState"
        },
        {
          "name": "secondary_member_count",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "max_secondary_members",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "invitations",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.SupportFamilyPlanInvitation"
        },
        {
          "name": "invitee_checks",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.SupportFamilyPlanInviteeCheck"
        }
      ]
    },
    {
      "name": "RevokeFamilyPlanInvitationRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invitation_ref",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "verification_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        }
      ]
    },
    {
      "name": "RevokeFamilyPlanInvitationResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SupportFamilyPlanRevokeResult"
        },
        {
          "name": "action_result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    },
    {
      "name": "ClearFamilyPlanTrialCooldownRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invitee_user_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "verification_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionContext"
        }
      ]
    },
    {
      "name": "ClearFamilyPlanTrialCooldownResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.SupportFamilyPlanCooldownResult"
        },
        {
          "name": "action_result",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.support.v1.SupportActionResult"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "SubscriptionAdminService",
      "method": [
        {
          "name": "CancelSubscription",
          "input_type": ".chesscom.payments.v1.CancelSubscriptionRequest",
          "output_type": ".chesscom.payments.v1.CancelSubscriptionResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "StopRenewalByCardMatch",
          "input_type": ".chesscom.payments.v1.StopRenewalByCardMatchRequest",
          "output_type": ".chesscom.payments.v1.StopRenewalByCardMatchResponse",
          "options": {}
        },
        {
          "name": "ExtendSubscription",
          "input_type": ".chesscom.payments.v1.ExtendSubscriptionRequest",
          "output_type": ".chesscom.payments.v1.ExtendSubscriptionResponse",
          "options": {}
        },
        {
          "name": "GrantGoodwillDiamond",
          "input_type": ".chesscom.payments.v1.GrantGoodwillDiamondRequest",
          "output_type": ".chesscom.payments.v1.GrantGoodwillDiamondResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "GrantNoAdsOffer",
          "input_type": ".chesscom.payments.v1.GrantNoAdsOfferRequest",
          "output_type": ".chesscom.payments.v1.GrantNoAdsOfferResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "TransferMembership",
          "input_type": ".chesscom.payments.v1.TransferMembershipRequest",
          "output_type": ".chesscom.payments.v1.TransferMembershipResponse",
          "options": {}
        },
        {
          "name": "GrantMembership",
          "input_type": ".chesscom.payments.v1.GrantMembershipRequest",
          "output_type": ".chesscom.payments.v1.GrantMembershipResponse",
          "options": {}
        },
        {
          "name": "SwitchToMonthly",
          "input_type": ".chesscom.payments.v1.SwitchToMonthlyRequest",
          "output_type": ".chesscom.payments.v1.SwitchToMonthlyResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "GetFamilyPlanInvitations",
          "input_type": ".chesscom.payments.v1.GetFamilyPlanInvitationsRequest",
          "output_type": ".chesscom.payments.v1.GetFamilyPlanInvitationsResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "RevokeFamilyPlanInvitation",
          "input_type": ".chesscom.payments.v1.RevokeFamilyPlanInvitationRequest",
          "output_type": ".chesscom.payments.v1.RevokeFamilyPlanInvitationResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "ClearFamilyPlanTrialCooldown",
          "input_type": ".chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest",
          "output_type": ".chesscom.payments.v1.ClearFamilyPlanTrialCooldownResponse",
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
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18074"></a>
## FND-18074: Full frontend descriptor: chesscom/payments/v1/prices_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/prices_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "GetPriceForAllCountriesRequest",
      "field": [
        {
          "name": "sku",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GetPriceForAllCountriesResponse",
      "field": [
        {
          "name": "products_prices",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.ProductPrices"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "PricesService",
      "method": [
        {
          "name": "GetPriceForAllCountries",
          "input_type": ".chesscom.payments.v1.GetPriceForAllCountriesRequest",
          "output_type": ".chesscom.payments.v1.GetPriceForAllCountriesResponse",
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
  Character offset 897016.

```text
gcmVmdW5kMghjaGVzc2NvbUIuyrcsKgoEL3JwYxIPEg1hcGkuY2hlc3MuY29tGg0SC2JlYXJlcl9hdXRoKgKQTmIGcHJvdG8z","chesscom/payments/v1/prices_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9wcmljZXNfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEiLQoeR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXF1ZXN0EgsKA3NrdRgBIAMoCSJfCh9HZXRQcmljZUZvckFsbENvdW50cmllc1Jlc3BvbnNlEjwKD3Byb2R1Y3RzX3ByaWNlcxgBIAMoCzIjLmNoZXNzY29tLnBheW1lbnRzLnYxLlByb2R1Y3RQcmlj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18076"></a>
## FND-18076: Full frontend descriptor: chesscom/payments/v1/checkout_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/checkout_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "GetTotalBySkuRequest",
      "field": [
        {
          "name": "sku",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coupon_code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "request_location",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.RequestLocation",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "payment_target",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.PaymentTarget",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "offer_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "platform",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform",
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_coupon_code"
        },
        {
          "name": "_request_location"
        },
        {
          "name": "_payment_target"
        },
        {
          "name": "_offer_id"
        },
        {
          "name": "_platform"
        }
      ]
    },
    {
      "name": "GetTotalBySkuResponse",
      "field": [
        {
          "name": "checkout_total",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.CheckoutTotal"
        }
      ]
    },
    {
      "name": "GetTotalBySkuListRequest",
      "field": [
        {
          "name": "sku",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "coupon_code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "request_location",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.RequestLocation",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "payment_target",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.PaymentTarget",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_coupon_code"
        },
        {
          "name": "_request_location"
        },
        {
          "name": "_payment_target"
        }
      ]
    },
    {
      "name": "GetTotalBySkuListResponse",
      "field": [
        {
          "name": "checkout_total",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.CheckoutTotal"
        }
      ]
    },
    {
      "name": "GetStorefrontDetailsRequest",
      "field": [
        {
          "name": "request_location",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.RequestLocation",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_request_location"
        }
      ]
    },
    {
      "name": "GetStorefrontDetailsResponse",
      "field": [
        {
          "name": "storefront_country",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.StorefrontCountry"
        },
        {
          "name": "membership_level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.MembershipLevel",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_membership_level"
        }
      ]
    },
    {
      "name": "GetAvailablePaymentMethodsRequest",
      "field": [
        {
          "name": "sku",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "payment_context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.payments.v1.PaymentContext"
        },
        {
          "name": "coupon_code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_coupon_code"
        }
      ]
    },
    {
      "name": "GetAvailablePaymentMethodsResponse",
      "field": [
        {
          "name": "payment_methods",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.AvailablePaymentMethod"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "CheckoutService",
      "method": [
        {
          "name": "GetTotalBySku",
          "input_type": ".chesscom.payments.v1.GetTotalBySkuRequest",
          "output_type": ".chesscom.payments.v1.GetTotalBySkuResponse",
          "options": {}
        },
        {
          "name": "GetTotalBySkuList",
          "input_type": ".chesscom.payments.v1.GetTotalBySkuListRequest",
          "output_type": ".chesscom.payments.v1.GetTotalBySkuListResponse",
          "options": {}
        },
        {
          "name": "GetStorefrontDetails",
          "input_type": ".chesscom.payments.v1.GetStorefrontDetailsRequest",
          "output_type": ".chesscom.payments.v1.GetStorefrontDetailsResponse",
          "options": {}
        },
        {
          "name": "GetAvailablePaymentMethods",
          "input_type": ".chesscom.payments.v1.GetAvailablePaymentMethodsRequest",
          "output_type": ".chesscom.payments.v1.GetAvailablePaymentMethodsResponse",
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
  Character offset 897603.

```text
uR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXNwb25zZSIAQh3KtywZCgQvcnBjEg8SDXd3dy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/checkout_service.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9jaGVja291dF9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLgAgoUR2V0VG90YWxCeVNrdVJlcXVlc3QSCwoDc2t1GAEgASgJEhgKC2NvdXBvbl9jb2RlGAIgASgJSACIAQESRAoQcmVxdWVzdF9sb2NhdGlvbhgDIAEoCzIlLmNoZXNzY29tLnBheW1lbnRzLnYxLlJlcXVlc3RMb2NhdGlvbkgBiAEBEkAKDn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18081"></a>
## FND-18081: Full frontend descriptor: chesscom/payments/v1/gift_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/gift_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "ListEligibleGiftRecipientsRequest",
      "field": [
        {
          "name": "user_uuids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "product",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.Product",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_product"
        }
      ]
    },
    {
      "name": "ListEligibleGiftRecipientsResponse",
      "field": [
        {
          "name": "eligible_user_uuids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "GiftService",
      "method": [
        {
          "name": "ListEligibleGiftRecipients",
          "input_type": ".chesscom.payments.v1.ListEligibleGiftRecipientsRequest",
          "output_type": ".chesscom.payments.v1.ListEligibleGiftRecipientsResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900316.

```text
xLkdldEF2YWlsYWJsZVBheW1lbnRNZXRob2RzUmVzcG9uc2UiAEIZyrcsFQoEL3JwYxILEgljaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/gift_service.proto":"CidjaGVzc2NvbS9wYXltZW50cy92MS9naWZ0X3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIngKIUxpc3RFbGlnaWJsZUdpZnRSZWNpcGllbnRzUmVxdWVzdBISCgp1c2VyX3V1aWRzGAEgAygJEjMKB3Byb2R1Y3QYAiABKAsyHS5jaGVzc2NvbS5wYXltZW50cy52MS5Qcm9kdWN0SACIAQFCCgoIX3Byb2R1Y3QiQQoiTGlzdEVsaWdpYmxlR2lmdFJlY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18083"></a>
## FND-18083: Full frontend descriptor: chesscom/payments/v1/group_membership_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/payments/v1/group_membership_service.proto",
  "package": "chesscom.payments.v1",
  "message_type": [
    {
      "name": "GenerateInvitationLinkRequest",
      "options": {}
    },
    {
      "name": "GenerateInvitationLinkResponse",
      "field": [
        {
          "name": "invitation_link",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "CheckJoinEligibilityRequest",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "email",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "member_identifier"
        }
      ]
    },
    {
      "name": "CheckJoinEligibilityResponse",
      "field": [
        {
          "name": "is_eligible",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "InviteMemberRequest",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "email",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "invitee_identifier"
        }
      ]
    },
    {
      "name": "InviteMemberResponse",
      "options": {}
    },
    {
      "name": "RemoveMemberRequest",
      "field": [
        {
          "name": "member_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "RemoveMemberResponse",
      "options": {}
    },
    {
      "name": "GetMaxSecondaryMembersRequest",
      "options": {}
    },
    {
      "name": "GetMaxSecondaryMembersResponse",
      "field": [
        {
          "name": "max_secondary_members",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "GetSecondaryMembersRequest",
      "options": {}
    },
    {
      "name": "GetSecondaryMembersResponse",
      "field": [
        {
          "name": "secondary_members",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        },
        {
          "name": "pending_invitations",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PendingInvitation"
        }
      ],
      "options": {}
    },
    {
      "name": "LeaveGroupMembershipRequest",
      "options": {}
    },
    {
      "name": "LeaveGroupMembershipResponse",
      "options": {}
    },
    {
      "name": "PreviewInvitationRequest",
      "field": [
        {
          "name": "invitation_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "source",
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
          "name": "_source"
        }
      ]
    },
    {
      "name": "PreviewInvitationResponse",
      "field": [
        {
          "name": "primary_account_holder",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "plan_details",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.InvitationPlanDetails",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "eligibility",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.JoinEligibility"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_primary_account_holder"
        },
        {
          "name": "_plan_details"
        }
      ]
    },
    {
      "name": "JoinGroupFromInvitationRequest",
      "field": [
        {
          "name": "invitation_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "JoinGroupFromInvitationResponse",
      "options": {}
    },
    {
      "name": "ListPendingInvitationsRequest",
      "options": {}
    },
    {
      "name": "ListPendingInvitationsResponse",
      "field": [
        {
          "name": "invitations",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.payments.v1.PendingInvitationForInvitee"
        }
      ],
      "options": {}
    },
    {
      "name": "DeclineInvitationRequest",
      "field": [
        {
          "name": "invitation_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "DeclineInvitationResponse",
      "options": {}
    },
    {
      "name": "RevokeInvitationRequest",
      "field": [
        {
          "name": "invitation_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "RevokeInvitationResponse",
      "options": {}
    }
  ],
  "service": [
    {
      "name": "GroupMembershipService",
      "method": [
        {
          "name": "GenerateInvitationLink",
          "input_type": ".chesscom.payments.v1.GenerateInvitationLinkRequest",
          "output_type": ".chesscom.payments.v1.GenerateInvitationLinkResponse"
        },
        {
          "name": "CheckJoinEligibility",
          "input_type": ".chesscom.payments.v1.CheckJoinEligibilityRequest",
          "output_type": ".chesscom.payments.v1.CheckJoinEligibilityResponse"
        },
        {
          "name": "InviteMember",
          "input_type": ".chesscom.payments.v1.InviteMemberRequest",
          "output_type": ".chesscom.payments.v1.InviteMemberResponse"
        },
        {
          "name": "RemoveMember",
          "input_type": ".chesscom.payments.v1.RemoveMemberRequest",
          "output_type": ".chesscom.payments.v1.RemoveMemberResponse"
        },
        {
          "name": "GetMaxSecondaryMembers",
          "input_type": ".chesscom.payments.v1.GetMaxSecondaryMembersRequest",
          "output_type": ".chesscom.payments.v1.GetMaxSecondaryMembersResponse"
        },
        {
          "name": "GetSecondaryMembers",
          "input_type": ".chesscom.payments.v1.GetSecondaryMembersRequest",
          "output_type": ".chesscom.payments.v1.GetSecondaryMembersResponse"
        },
        {
          "name": "LeaveGroupMembership",
          "input_type": ".chesscom.payments.v1.LeaveGroupMembershipRequest",
          "output_type": ".chesscom.payments.v1.LeaveGroupMembershipResponse"
        },
        {
          "name": "PreviewInvitation",
          "input_type": ".chesscom.payments.v1.PreviewInvitationRequest",
          "output_type": ".chesscom.payments.v1.PreviewInvitationResponse"
        },
        {
          "name": "JoinGroupFromInvitation",
          "input_type": ".chesscom.payments.v1.JoinGroupFromInvitationRequest",
          "output_type": ".chesscom.payments.v1.JoinGroupFromInvitationResponse"
        },
        {
          "name": "ListPendingInvitations",
          "input_type": ".chesscom.payments.v1.ListPendingInvitationsRequest",
          "output_type": ".chesscom.payments.v1.ListPendingInvitationsResponse"
        },
        {
          "name": "DeclineInvitation",
          "input_type": ".chesscom.payments.v1.DeclineInvitationRequest",
          "output_type": ".chesscom.payments.v1.DeclineInvitationResponse"
        },
        {
          "name": "RevokeInvitation",
          "input_type": ".chesscom.payments.v1.RevokeInvitationRequest",
          "output_type": ".chesscom.payments.v1.RevokeInvitationResponse"
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
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18096"></a>
## FND-18096: Full frontend descriptor: chesscom/user_profile/v1/social.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_profile/v1/social.proto",
  "package": "chesscom.user_profile.v1",
  "message_type": [
    {
      "name": "FollowedUser",
      "field": [
        {
          "name": "uuid",
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
          "name": "avatar",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "country_code",
          "number": 4,
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
  Character offset 905456.

```text
MudjEuUmV2b2tlSW52aXRhdGlvblJlc3BvbnNlGgeSph0DCgEBQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/user_profile/v1/social.proto":"CiVjaGVzc2NvbS91c2VyX3Byb2ZpbGUvdjEvc29jaWFsLnByb3RvEhhjaGVzc2NvbS51c2VyX3Byb2ZpbGUudjEiXQoMRm9sbG93ZWRVc2VyEgwKBHV1aWQYASABKAkSEAoIdXNlcm5hbWUYAiABKAkSDgoGYXZhdGFyGAMgASgJEhQKDGNvdW50cnlfY29kZRgEIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/user_profile/v1/social_service.proto":"Ci1ja
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18097"></a>
## FND-18097: Full frontend descriptor: chesscom/user_profile/v1/social_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_profile/v1/social_service.proto",
  "package": "chesscom.user_profile.v1",
  "message_type": [
    {
      "name": "ListFollowedUsersRequest",
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
          "name": "requester_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
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
          "name": "_requester_uuid"
        }
      ]
    },
    {
      "name": "ListFollowedUsersResponse",
      "field": [
        {
          "name": "followed_users",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_profile.v1.FollowedUser"
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
      "name": "DoesUserFollowOtherUsersRequest",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "target_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_uuid"
        }
      ]
    },
    {
      "name": "DoesUserFollowOtherUsersResponse",
      "field": [
        {
          "name": "follow_status",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry"
        }
      ],
      "nested_type": [
        {
          "name": "FollowStatusEntry",
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
              "type": "TYPE_BOOL"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "SocialService",
      "method": [
        {
          "name": "ListFollowedUsers",
          "input_type": ".chesscom.user_profile.v1.ListFollowedUsersRequest",
          "output_type": ".chesscom.user_profile.v1.ListFollowedUsersResponse"
        },
        {
          "name": "DoesUserFollowOtherUsers",
          "input_type": ".chesscom.user_profile.v1.DoesUserFollowOtherUsersRequest",
          "output_type": ".chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse"
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
  Character offset 905723.

```text
SEAoIdXNlcm5hbWUYAiABKAkSDgoGYXZhdGFyGAMgASgJEhQKDGNvdW50cnlfY29kZRgEIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/user_profile/v1/social_service.proto":"Ci1jaGVzc2NvbS91c2VyX3Byb2ZpbGUvdjEvc29jaWFsX3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfcHJvZmlsZS52MSKfAQoYTGlzdEZvbGxvd2VkVXNlcnNSZXF1ZXN0EjsKCnBhZ2luYXRpb24YASABKAsyIi5jaGVzc2NvbS5hcGkudjEuUmVxdWVzdFBhZ2luYXRpb25IAIgBARIbCg5yZXF1ZXN0ZXJfdXVpZBgCIAEoCUgBiAEBOgeCph0DCgEBQg0K
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18100"></a>
## FND-18100: Full frontend descriptor: chesscom/inbox/v1/user_message_core.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/inbox/v1/user_message_core.proto",
  "package": "chesscom.inbox.v1",
  "enum_type": [
    {
      "name": "BatchMessageContext",
      "value": [
        {
          "name": "BATCH_MESSAGE_CONTEXT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BATCH_MESSAGE_CONTEXT_SHARE",
          "number": 1
        }
      ]
    },
    {
      "name": "MessageSendNotAllowedReason",
      "value": [
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY",
          "number": 1
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY",
          "number": 2
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED",
          "number": 3
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL",
          "number": 4
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE",
          "number": 5
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED",
          "number": 6
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT",
          "number": 7
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY",
          "number": 8
        },
        {
          "name": "MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN",
          "number": 9
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 907166.

```text
yRm9sbG93T3RoZXJVc2Vyc1Jlc3BvbnNlGgeSph0DCgEBQh3KtywZCgQvcnBjEg8SDWFwaS5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/inbox/v1/user_message_core.proto":"CiljaGVzc2NvbS9pbmJveC92MS91c2VyX21lc3NhZ2VfY29yZS5wcm90bxIRY2hlc3Njb20uaW5ib3gudjEqXQoTQmF0Y2hNZXNzYWdlQ29udGV4dBIlCiFCQVRDSF9NRVNTQUdFX0NPTlRFWFRfVU5TUEVDSUZJRUQQABIfChtCQVRDSF9NRVNTQUdFX0NPTlRFWFRfU0hBUkUQASqWBAobTWVzc2FnZVNlbmROb3RBbGxvd2VkUmVhc29uEi8KK01FU1NBR0VfU0VORF9O
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18101"></a>
## FND-18101: Full frontend descriptor: chesscom/inbox/v1/user_message_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/inbox/v1/user_message_service.proto",
  "package": "chesscom.inbox.v1",
  "message_type": [
    {
      "name": "BatchSendUserMessageRequest",
      "field": [
        {
          "name": "sender_user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "recipient_user_uuids",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "message_text",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.inbox.v1.BatchMessageContext"
        }
      ]
    },
    {
      "name": "BatchSendUserMessageResponse",
      "field": [
        {
          "name": "results",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.inbox.v1.BatchSendUserMessageResponse.Result"
        }
      ],
      "nested_type": [
        {
          "name": "Result",
          "field": [
            {
              "name": "recipient_user_uuid",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "success",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL"
            },
            {
              "name": "error_code",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING",
              "oneof_index": 0,
              "proto3_optional": true
            }
          ],
          "oneof_decl": [
            {
              "name": "_error_code"
            }
          ]
        }
      ]
    },
    {
      "name": "CheckCanSendUserMessageRequest",
      "field": [
        {
          "name": "sender_user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "recipient_user_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "CheckCanSendUserMessageResponse",
      "field": [
        {
          "name": "can_send",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "reason",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.inbox.v1.MessageSendNotAllowedReason"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "UserMessageService",
      "method": [
        {
          "name": "BatchSendUserMessage",
          "input_type": ".chesscom.inbox.v1.BatchSendUserMessageRequest",
          "output_type": ".chesscom.inbox.v1.BatchSendUserMessageResponse"
        },
        {
          "name": "CheckCanSendUserMessage",
          "input_type": ".chesscom.inbox.v1.CheckCanSendUserMessageRequest",
          "output_type": ".chesscom.inbox.v1.CheckCanSendUserMessageResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
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
  Character offset 908149.

```text
ERVJfUFJJVkFDWRAIEjIKLk1FU1NBR0VfU0VORF9OT1RfQUxMT1dFRF9SRUFTT05fQ09OVEVOVF9ISURERU4QCWIGcHJvdG8z","chesscom/inbox/v1/user_message_service.proto":"CixjaGVzc2NvbS9pbmJveC92MS91c2VyX21lc3NhZ2Vfc2VydmljZS5wcm90bxIRY2hlc3Njb20uaW5ib3gudjEipAEKG0JhdGNoU2VuZFVzZXJNZXNzYWdlUmVxdWVzdBIYChBzZW5kZXJfdXNlcl91dWlkGAEgASgJEhwKFHJlY2lwaWVudF91c2VyX3V1aWRzGAIgAygJEhQKDG1lc3NhZ2VfdGV4dBgDIAEoCRI3Cgdjb250ZXh0GAQgASgOMiYuY2hlc3Njb20ua
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-18104"></a>
## FND-18104: Full frontend descriptor: chesscom/audiences/v1/authenticated_audiences_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/audiences/v1/authenticated_audiences_service.proto",
  "package": "chesscom.audiences.v1",
  "message_type": [
    {
      "name": "IsAuthenticatedUserInAudiencesRequest",
      "field": [
        {
          "name": "audience_keys",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "IsAuthenticatedUserInAudiencesResponse",
      "field": [
        {
          "name": "in_audience",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry"
        }
      ],
      "nested_type": [
        {
          "name": "InAudienceEntry",
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
              "type": "TYPE_BOOL"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "AuthenticatedAudiencesService",
      "method": [
        {
          "name": "IsAuthenticatedUserInAudiences",
          "input_type": ".chesscom.audiences.v1.IsAuthenticatedUserInAudiencesRequest",
          "output_type": ".chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse",
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
  Character offset 909478.

```text
Vja0NhblNlbmRVc2VyTWVzc2FnZVJlc3BvbnNlIgOQAgFCHcq3LBkKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/audiences/v1/authenticated_audiences_service.proto":"CjtjaGVzc2NvbS9hdWRpZW5jZXMvdjEvYXV0aGVudGljYXRlZF9hdWRpZW5jZXNfc2VydmljZS5wcm90bxIVY2hlc3Njb20uYXVkaWVuY2VzLnYxIkcKJUlzQXV0aGVudGljYXRlZFVzZXJJbkF1ZGllbmNlc1JlcXVlc3QSFQoNYXVkaWVuY2Vfa2V5cxgBIAMoCToHgqYdAwoBASLIAQomSXNBdXRoZW50aWNhdGVkVXNlckluQXVkaWVuY2VzUm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.
