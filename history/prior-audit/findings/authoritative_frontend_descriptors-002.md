# authoritative_frontend_descriptors — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17515"></a>
## FND-17515: Full frontend descriptor: chesscom/computer/v1/computer_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/computer/v1/computer_game.proto",
  "package": "chesscom.computer.v1",
  "message_type": [
    {
      "name": "AssistedGameFeatures",
      "field": [
        {
          "name": "chat",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "analysis",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "hints",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "threats",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "CustomModeConfiguration",
      "field": [
        {
          "name": "game_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.Variant"
        },
        {
          "name": "base_time_ms",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "time_increment_ms",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "assisted_game_features",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.computer.v1.AssistedGameFeature"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "UserColor",
      "value": [
        {
          "name": "USER_COLOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_COLOR_WHITE",
          "number": 1
        },
        {
          "name": "USER_COLOR_BLACK",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "GameMode",
      "value": [
        {
          "name": "GAME_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_MODE_CHALLENGE",
          "number": 1
        },
        {
          "name": "GAME_MODE_FRIENDLY",
          "number": 2
        },
        {
          "name": "GAME_MODE_ASSISTED",
          "number": 3
        },
        {
          "name": "GAME_MODE_CUSTOM",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "AssistedGameFeature",
      "value": [
        {
          "name": "ASSISTED_GAME_FEATURE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ASSISTED_GAME_FEATURE_CHAT",
          "number": 1
        },
        {
          "name": "ASSISTED_GAME_FEATURE_ANALYSIS",
          "number": 2
        },
        {
          "name": "ASSISTED_GAME_FEATURE_HINTS",
          "number": 3
        },
        {
          "name": "ASSISTED_GAME_FEATURE_THREATS",
          "number": 4
        },
        {
          "name": "ASSISTED_GAME_FEATURE_EVALUATION",
          "number": 5
        },
        {
          "name": "ASSISTED_GAME_FEATURE_ENGINE",
          "number": 6
        },
        {
          "name": "ASSISTED_GAME_FEATURE_SUGGESTIONS",
          "number": 7
        },
        {
          "name": "ASSISTED_GAME_FEATURE_TAKEBACKS",
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
  Character offset 114213.

```text
RFX0RBSUxZEAIaCso+BwoCAQISAQQSJQoVUExBWV9NT0RFX1ZTX0NPTVBVVEVSEAMaCso+BwoCAQISAQAaAhgBYgZwcm90bzM","chesscom/computer/v1/computer_game.proto":"CihjaGVzc2NvbS9jb21wdXRlci92MS9jb21wdXRlcl9nYW1lLnByb3RvEhRjaGVzc2NvbS5jb21wdXRlci52MSJWChRBc3Npc3RlZEdhbWVGZWF0dXJlcxIMCgRjaGF0GAEgASgIEhAKCGFuYWx5c2lzGAIgASgIEg0KBWhpbnRzGAMgASgIEg8KB3RocmVhdHMYBCABKAgi1AEKF0N1c3RvbU1vZGVDb25maWd1cmF0aW9uEjQKCWdhbWVfdHlwZRgBIAEoDjIhLmNoZXNzY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17516"></a>
## FND-17516: Full frontend descriptor: chesscom/coaches/v2/service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/coaches/v2/service.proto",
  "package": "chesscom.coaches.v2",
  "message_type": [
    {
      "name": "ListCoachesRequest",
      "field": [
        {
          "name": "locale_override",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "with_celebrity_coaches",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_locale_override"
        },
        {
          "name": "_with_celebrity_coaches"
        }
      ]
    },
    {
      "name": "ListCoachesResponse",
      "field": [
        {
          "name": "coach_categories",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.CoachCategory"
        }
      ],
      "options": {}
    },
    {
      "name": "ListOnboardingCoachesRequest",
      "field": [
        {
          "name": "locale_override",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "with_celebrity_coaches",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_locale_override"
        },
        {
          "name": "_with_celebrity_coaches"
        }
      ]
    },
    {
      "name": "ListOnboardingCoachesResponse",
      "field": [
        {
          "name": "coach_categories",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.CoachCategory"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachRequest",
      "field": [
        {
          "name": "coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachResponse",
      "field": [
        {
          "name": "coach",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.Coach"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachesRequest",
      "field": [
        {
          "name": "coach_ids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachesResponse",
      "field": [
        {
          "name": "coaches",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.Coach"
        }
      ],
      "options": {}
    },
    {
      "name": "SetCurrentCoachRequest",
      "field": [
        {
          "name": "coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "locale_override",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
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
          "name": "_locale_override"
        }
      ]
    },
    {
      "name": "SetCurrentCoachResponse",
      "field": [
        {
          "name": "current_coach",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.Coach"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCurrentCoachRequest",
      "field": [
        {
          "name": "locale_override",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "device_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "bucketing_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "with_celebrity_coaches",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_locale_override"
        },
        {
          "name": "_device_id"
        },
        {
          "name": "_bucketing_id"
        },
        {
          "name": "_with_celebrity_coaches"
        }
      ]
    },
    {
      "name": "GetCurrentCoachResponse",
      "field": [
        {
          "name": "current_coach",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.Coach"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachQuotaRequest",
      "options": {}
    },
    {
      "name": "GetCoachQuotaResponse",
      "field": [
        {
          "name": "remaining",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "StartedGameAgainstCoachRequest",
      "field": [
        {
          "name": "game_token",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "StartedGameAgainstCoachResponse",
      "options": {}
    },
    {
      "name": "SetSettingsResponse",
      "options": {}
    },
    {
      "name": "SetSettingsRequest",
      "field": [
        {
          "name": "enable_motivational",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "enable_voice",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "enable_reminders",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "puzzle_goals",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "puzzle_mistake_feedback",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "puzzle_hints",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "voice_speed",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachVoiceSpeed",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "show_coach_avatar_game_review",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "enable_auto_save_coach_games",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "enable_evaluation_bar",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "enable_suggestion_arrows",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "enable_threat_arrows",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "enable_skills",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "enable_teach_legal_moves",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 13,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_enable_motivational"
        },
        {
          "name": "_enable_voice"
        },
        {
          "name": "_enable_reminders"
        },
        {
          "name": "_puzzle_goals"
        },
        {
          "name": "_puzzle_mistake_feedback"
        },
        {
          "name": "_puzzle_hints"
        },
        {
          "name": "_voice_speed"
        },
        {
          "name": "_show_coach_avatar_game_review"
        },
        {
          "name": "_enable_auto_save_coach_games"
        },
        {
          "name": "_enable_evaluation_bar"
        },
        {
          "name": "_enable_suggestion_arrows"
        },
        {
          "name": "_enable_threat_arrows"
        },
        {
          "name": "_enable_skills"
        },
        {
          "name": "_enable_teach_legal_moves"
        }
      ]
    },
    {
      "name": "GetSettingsRequest",
      "options": {}
    },
    {
      "name": "GetSettingsResponse",
      "field": [
        {
          "name": "enable_motivational",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_voice",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_reminders",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_puzzle_goals",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_puzzle_mistake_feedback",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_puzzle_hints",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "voice_speed",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachVoiceSpeed"
        },
        {
          "name": "show_coach_avatar_game_review",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_auto_save_coach_games",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_evaluation_bar",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_suggestion_arrows",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_threat_arrows",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_skills",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_teach_legal_moves",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "SaveCoachGameRequest",
      "field": [
        {
          "name": "user_position",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.computer.v1.UserColor"
        },
        {
          "name": "coach_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coach_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "coach_result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerResult"
        },
        {
          "name": "user_result",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerResult"
        },
        {
          "name": "initial_fen",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "final_fen",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_start_time",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "game_end_time",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "move_text",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_result",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameResult"
        },
        {
          "name": "game_uuid",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "finish_vs_coach",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_uuid"
        }
      ]
    },
    {
      "name": "HideCoachGameRequest",
      "field": [
        {
          "name": "game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64"
        }
      ],
      "options": {}
    },
    {
      "name": "HideCoachGameResponse",
      "options": {}
    },
    {
      "name": "SaveCoachGameResponse",
      "field": [
        {
          "name": "game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64"
        },
        {
          "name": "game_uuid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachSpeechRequest",
      "field": [
        {
          "name": "coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachContext"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCoachSpeechResponse",
      "field": [
        {
          "name": "speech",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.SpeechString"
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "CoachesService",
      "method": [
        {
          "name": "ListCoaches",
          "input_type": ".chesscom.coaches.v2.ListCoachesRequest",
          "output_type": ".chesscom.coaches.v2.ListCoachesResponse",
          "options": {}
        },
        {
          "name": "ListOnboardingCoaches",
          "input_type": ".chesscom.coaches.v2.ListOnboardingCoachesRequest",
          "output_type": ".chesscom.coaches.v2.ListOnboardingCoachesResponse",
          "options": {}
        },
        {
          "name": "SetCurrentCoach",
          "input_type": ".chesscom.coaches.v2.SetCurrentCoachRequest",
          "output_type": ".chesscom.coaches.v2.SetCurrentCoachResponse",
          "options": {}
        },
        {
          "name": "GetCurrentCoach",
          "input_type": ".chesscom.coaches.v2.GetCurrentCoachRequest",
          "output_type": ".chesscom.coaches.v2.GetCurrentCoachResponse",
          "options": {}
        },
        {
          "name": "GetCoach",
          "input_type": ".chesscom.coaches.v2.GetCoachRequest",
          "output_type": ".chesscom.coaches.v2.GetCoachResponse",
          "options": {}
        },
        {
          "name": "GetCoaches",
          "input_type": ".chesscom.coaches.v2.GetCoachesRequest",
          "output_type": ".chesscom.coaches.v2.GetCoachesResponse",
          "options": {}
        },
        {
          "name": "GetCoachQuota",
          "input_type": ".chesscom.coaches.v2.GetCoachQuotaRequest",
          "output_type": ".chesscom.coaches.v2.GetCoachQuotaResponse",
          "options": {}
        },
        {
          "name": "StartedGameAgainstCoach",
          "input_type": ".chesscom.coaches.v2.StartedGameAgainstCoachRequest",
          "output_type": ".chesscom.coaches.v2.StartedGameAgainstCoachResponse",
          "options": {}
        },
        {
          "name": "GetSettings",
          "input_type": ".chesscom.coaches.v2.GetSettingsRequest",
          "output_type": ".chesscom.coaches.v2.GetSettingsResponse",
          "options": {}
        },
        {
          "name": "SetSettings",
          "input_type": ".chesscom.coaches.v2.SetSettingsRequest",
          "output_type": ".chesscom.coaches.v2.SetSettingsResponse",
          "options": {}
        },
        {
          "name": "SaveCoachGame",
          "input_type": ".chesscom.coaches.v2.SaveCoachGameRequest",
          "output_type": ".chesscom.coaches.v2.SaveCoachGameResponse"
        },
        {
          "name": "GetCoachSpeech",
          "input_type": ".chesscom.coaches.v2.GetCoachSpeechRequest",
          "output_type": ".chesscom.coaches.v2.GetCoachSpeechResponse"
        },
        {
          "name": "HideCoachGame",
          "input_type": ".chesscom.coaches.v2.HideCoachGameRequest",
          "output_type": ".chesscom.coaches.v2.HideCoachGameResponse"
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
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17530"></a>
## FND-17530: Full frontend descriptor: chesscom/coaches/v2/user_activity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/coaches/v2/user_activity.proto",
  "package": "chesscom.coaches.v2",
  "message_type": [
    {
      "name": "CoachSwitched",
      "field": [
        {
          "name": "new_coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "source",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachSwitchSource"
        }
      ],
      "options": {}
    },
    {
      "name": "ChooseYourCoachModalOpened",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachSwitchSource"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachTaglineShown",
      "field": [
        {
          "name": "coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coach_tagline_ui",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachTaglineUi"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachWelcomeModalShown",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "PlayCoachOpened",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.PlayCoachOpenedSource"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachSettingChanged",
      "field": [
        {
          "name": "setting",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.PlayCoachAssistanceSetting"
        },
        {
          "name": "enabled",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachGameStarted",
      "field": [
        {
          "name": "coach_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "coach_level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {}
        },
        {
          "name": "assistance_settings",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot"
        },
        {
          "name": "finish_vs_coach",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.FinishVsCoachContext"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachGameCompleted",
      "field": [
        {
          "name": "coach_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "coach_level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {}
        },
        {
          "name": "result",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerResult",
          "options": {}
        },
        {
          "name": "game_result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Result"
        },
        {
          "name": "game_result_type",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.ResultType"
        },
        {
          "name": "bot_personality",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "finish_vs_coach",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.FinishVsCoachContext"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachHintRequested",
      "field": [
        {
          "name": "coach_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coach_level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "stage",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.PlayCoachHint",
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "PlayCoachHintReceived",
      "field": [
        {
          "name": "coach_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coach_level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "stage",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.PlayCoachHint"
        },
        {
          "name": "fen",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachMonetizationModalShowed",
      "options": {}
    },
    {
      "name": "PlayCoachSignUpModalShowed",
      "options": {}
    },
    {
      "name": "PlayCoachSignUpModalCTATapped",
      "options": {}
    },
    {
      "name": "CoachSettingsOpened",
      "options": {}
    },
    {
      "name": "CoachCouldWarnOfMistake",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "cooldown_counter",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachWarnedOfMistake",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachMistakeWarningAnswered",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "choice",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachMistakeWarningChoice"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachFlipBoardOffered",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachFlipBoardAnswered",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "choice",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.CoachFlipBoardChoice"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachFlipBoardExerciseCompleted",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "found_correct_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "wrong_attempts",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachContextExtension",
      "field": [
        {
          "name": "coach_analytics_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coach_locale",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachRetryMissContextExtension",
      "field": [
        {
          "name": "boardevent",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "found_correct_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "wrong_attempts",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_found_correct_move"
        },
        {
          "name": "_wrong_attempts"
        }
      ]
    },
    {
      "name": "CoachAnimationShown",
      "field": [
        {
          "name": "animation_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "interface",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "options": {}
    },
    {
      "name": "GuidedCoachGameStarted",
      "field": [
        {
          "name": "script_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "source",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.GuidedCoachGameSource"
        }
      ],
      "options": {}
    },
    {
      "name": "GuidedCoachGameResigned",
      "field": [
        {
          "name": "script_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ply_index",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "GuidedCoachGameCompleted",
      "field": [
        {
          "name": "script_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "CoachSwitchSource",
      "value": [
        {
          "name": "COACH_SWITCH_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_SWITCH_SOURCE_SETTINGS",
          "number": 1
        },
        {
          "name": "COACH_SWITCH_SOURCE_GAME_REVIEW",
          "number": 2
        },
        {
          "name": "COACH_SWITCH_SOURCE_PLAY_COACH",
          "number": 3
        },
        {
          "name": "COACH_SWITCH_SOURCE_DAILY_PUZZLE",
          "number": 4
        },
        {
          "name": "COACH_SWITCH_SOURCE_PUZZLES_ROOT",
          "number": 5
        },
        {
          "name": "COACH_SWITCH_SOURCE_PUZZLE",
          "number": 6
        },
        {
          "name": "COACH_SWITCH_SOURCE_LESSONS_ROOT",
          "number": 7
        },
        {
          "name": "COACH_SWITCH_SOURCE_LESSON",
          "number": 8
        },
        {
          "name": "COACH_SWITCH_SOURCE_COACH_GAME_SETUP",
          "number": 9
        },
        {
          "name": "COACH_SWITCH_SOURCE_LEARN_ROOT",
          "number": 10
        },
        {
          "name": "COACH_SWITCH_SOURCE_DEEPLINK",
          "number": 11
        },
        {
          "name": "COACH_SWITCH_SOURCE_WELCOME_MODAL",
          "number": 12
        },
        {
          "name": "COACH_SWITCH_SOURCE_ONBOARDING",
          "number": 13
        },
        {
          "name": "COACH_SWITCH_SOURCE_HOME",
          "number": 14
        },
        {
          "name": "COACH_SWITCH_SOURCE_TRAIN",
          "number": 15
        }
      ],
      "options": {}
    },
    {
      "name": "CoachTaglineUi",
      "value": [
        {
          "name": "COACH_TAGLINE_UI_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_TAGLINE_UI_CHOOSE_COACH_MODAL",
          "number": 1
        },
        {
          "name": "COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP",
          "number": 2
        },
        {
          "name": "COACH_TAGLINE_UI_SELECT_COACH_SETTINGS",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachOpenedSource",
      "value": [
        {
          "name": "PLAY_COACH_OPENED_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAY_COACH_OPENED_SOURCE_PLAY_ROOT",
          "number": 1
        },
        {
          "name": "PLAY_COACH_OPENED_SOURCE_HOME",
          "number": 2
        },
        {
          "name": "PLAY_COACH_OPENED_SOURCE_LEARN_ROOT",
          "number": 3
        },
        {
          "name": "PLAY_COACH_OPENED_SOURCE_LEARN_NAV",
          "number": 4
        },
        {
          "name": "PLAY_COACH_OPENED_SOURCE_PLAY_NAV",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachAssistanceSetting",
      "value": [
        {
          "name": "PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS",
          "number": 1
        },
        {
          "name": "PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS",
          "number": 2
        },
        {
          "name": "PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR",
          "number": 3
        },
        {
          "name": "PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK",
          "number": 4
        },
        {
          "name": "PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachHint",
      "value": [
        {
          "name": "PLAY_COACH_HINT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAY_COACH_HINT_SPEECH",
          "number": 1
        },
        {
          "name": "PLAY_COACH_HINT_HIGHLIGHTED_SQUARE",
          "number": 2
        },
        {
          "name": "PLAY_COACH_HINT_BEST_MOVE",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "CoachMistakeWarningChoice",
      "value": [
        {
          "name": "COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_MISTAKE_WARNING_CHOICE_RETRY",
          "number": 1
        },
        {
          "name": "COACH_MISTAKE_WARNING_CHOICE_CONTINUE",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "CoachFlipBoardChoice",
      "value": [
        {
          "name": "COACH_FLIP_BOARD_CHOICE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES",
          "number": 1
        },
        {
          "name": "COACH_FLIP_BOARD_CHOICE_CONTINUE",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "GuidedCoachGameSource",
      "value": [
        {
          "name": "GUIDED_COACH_GAME_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GUIDED_COACH_GAME_SOURCE_SIGNUP",
          "number": 1
        },
        {
          "name": "GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY",
          "number": 2
        },
        {
          "name": "GUIDED_COACH_GAME_SOURCE_REPLAY",
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
  Character offset 122761.

```text
F0Zm9ybS5jb20SGnN0YWdpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoAYgZwcm90bzM","chesscom/coaches/v2/user_activity.proto":"CidjaGVzc2NvbS9jb2FjaGVzL3YyL3VzZXJfYWN0aXZpdHkucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIiiwEKDUNvYWNoU3dpdGNoZWQSIQoMbmV3X2NvYWNoX2lkGAEgASgJQgvS8xgHY29hY2hJZBI2CgZzb3VyY2UYAiABKA4yJi5jaGVzc2NvbS5jb2FjaGVzLnYyLkNvYWNoU3dpdGNoU291cmNlOh/C8xgUCg5Td2l0Y2hlZCBDb2FjaBACIAyCph0DCgEBIo0BCh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17531"></a>
## FND-17531: Full frontend descriptor: chesscom/cheat_metadata_storage/v1/cheat_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/cheat_metadata_storage/v1/cheat_metadata.proto",
  "package": "chesscom.cheat_metadata_storage.v1",
  "message_type": [
    {
      "name": "GameCheatMetadata",
      "field": [
        {
          "name": "game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "created_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "white_player_metadata",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.cheat_metadata_storage.v1.CheatMetadata"
        },
        {
          "name": "black_player_metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.cheat_metadata_storage.v1.CheatMetadata"
        },
        {
          "name": "white_client",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "black_client",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "white_moves_from_multiple_clients",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "black_moves_from_multiple_clients",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "CheatMetadata",
      "field": [
        {
          "name": "move_hold_times",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "toggled_moves",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "bot_moves",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "change_of_heart_moves",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "draw_offer_moves",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "pointer_offsets",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "not_user_generated_moves",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "untrusted_event_moves",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "blur_on_own_turn_moves",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "blur_on_opponent_turn_moves",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "focus_on_own_turn_moves",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "focus_on_opponent_turn_moves",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "move_to_first_blur_times",
          "number": 13,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "last_focus_to_move_times",
          "number": 14,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_blur_time",
          "number": 15,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_focus_time",
          "number": 16,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "blur_counts",
          "number": 17,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "external_board_moves",
          "number": 18,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "premoves",
          "number": 19,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "screenshot_detected_moves",
          "number": 20,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "browser_extension",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "square_widths",
          "number": 22,
          "label": "LABEL_REPEATED",
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
  Character offset 130568.

```text
1BMQVlfQ09BQ0hfRU5UUlkQAhIjCh9HVUlERURfQ09BQ0hfR0FNRV9TT1VSQ0VfUkVQTEFZEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/cheat_metadata_storage/v1/cheat_metadata.proto":"CjdjaGVzc2NvbS9jaGVhdF9tZXRhZGF0YV9zdG9yYWdlL3YxL2NoZWF0X21ldGFkYXRhLnByb3RvEiJjaGVzc2NvbS5jaGVhdF9tZXRhZGF0YV9zdG9yYWdlLnYxIoQDChFHYW1lQ2hlYXRNZXRhZGF0YRIPCgdnYW1lX2lkGAEgASgJEi4KCmNyZWF0ZWRfYXQYAiABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1wElAKFXdoaXRlX3BsYXllcl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17532"></a>
## FND-17532: Full frontend descriptor: chesscom/game_gateway/v1/favorite_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v1/favorite_metadata.proto",
  "package": "chesscom.game_gateway.v1",
  "message_type": [
    {
      "name": "FavoriteMetadata",
      "field": [
        {
          "name": "is_favorite",
          "number": 1,
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
  Character offset 132159.

```text
CADKA0SGQoRYnJvd3Nlcl9leHRlbnNpb24YFSABKAkSFQoNc3F1YXJlX3dpZHRocxgWIAMoBToIgqYdBAoCAQJiBnByb3RvMw","chesscom/game_gateway/v1/favorite_metadata.proto":"CjBjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvZmF2b3JpdGVfbWV0YWRhdGEucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MSIxChBGYXZvcml0ZU1ldGFkYXRhEhMKC2lzX2Zhdm9yaXRlGAEgASgIOgiCph0ECgIBAmIGcHJvdG8z","chesscom/game_gateway/v1/game_relationship_metadata.proto":"CjljaGVzc2NvbS9nYW1lX2dhdG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17533"></a>
## FND-17533: Full frontend descriptor: chesscom/game_gateway/v1/game_relationship_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v1/game_relationship_metadata.proto",
  "package": "chesscom.game_gateway.v1",
  "message_type": [
    {
      "name": "GameRelationshipMetadata",
      "field": [
        {
          "name": "are_friends",
          "number": 1,
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
  Character offset 132393.

```text
hbWVfZ2F0ZXdheS52MSIxChBGYXZvcml0ZU1ldGFkYXRhEhMKC2lzX2Zhdm9yaXRlGAEgASgIOgiCph0ECgIBAmIGcHJvdG8z","chesscom/game_gateway/v1/game_relationship_metadata.proto":"CjljaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvZ2FtZV9yZWxhdGlvbnNoaXBfbWV0YWRhdGEucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MSI5ChhHYW1lUmVsYXRpb25zaGlwTWV0YWRhdGESEwoLYXJlX2ZyaWVuZHMYASABKAg6CIKmHQQKAgECYgZwcm90bzM","chesscom/analysis/v1/move_classifications.proto":"Ci9j
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17534"></a>
## FND-17534: Full frontend descriptor: chesscom/analysis/v1/move_classifications.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/analysis/v1/move_classifications.proto",
  "package": "chesscom.analysis.v1",
  "enum_type": [
    {
      "name": "MoveClassification",
      "value": [
        {
          "name": "MOVE_CLASSIFICATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOOK",
          "number": 1
        },
        {
          "name": "BRILLIANT",
          "number": 2
        },
        {
          "name": "GREATFIND",
          "number": 3
        },
        {
          "name": "BEST",
          "number": 4
        },
        {
          "name": "EXCELLENT",
          "number": 5
        },
        {
          "name": "GOOD",
          "number": 6
        },
        {
          "name": "INACCURACY",
          "number": 7
        },
        {
          "name": "INACCURACY_OPENING_PHASE",
          "number": 8
        },
        {
          "name": "INACCURACY_MID_GAME_PHASE",
          "number": 9
        },
        {
          "name": "INACCURACY_END_GAME_PHASE",
          "number": 10
        },
        {
          "name": "MISTAKE",
          "number": 11
        },
        {
          "name": "MISTAKE_OPENING_PHASE",
          "number": 12
        },
        {
          "name": "MISTAKE_MID_GAME_PHASE",
          "number": 13
        },
        {
          "name": "MISTAKE_END_GAME_PHASE",
          "number": 14
        },
        {
          "name": "BLUNDER",
          "number": 15
        },
        {
          "name": "BLUNDER_OPENING_PHASE",
          "number": 16
        },
        {
          "name": "BLUNDER_MID_GAME_PHASE",
          "number": 17
        },
        {
          "name": "BLUNDER_END_GAME_PHASE",
          "number": 18
        },
        {
          "name": "FORCED",
          "number": 19
        },
        {
          "name": "MISS",
          "number": 20
        },
        {
          "name": "MISS_OPENING_PHASE",
          "number": 21
        },
        {
          "name": "MISS_MID_GAME_PHASE",
          "number": 22
        },
        {
          "name": "MISS_END_GAME_PHASE",
          "number": 23
        },
        {
          "name": "MISSED_MATE",
          "number": 24
        },
        {
          "name": "FASTER_MATE",
          "number": 25
        },
        {
          "name": "WINNING_TO_LOSING",
          "number": 26
        },
        {
          "name": "CRITICAL",
          "number": 27
        },
        {
          "name": "MISSEDWIN",
          "number": 28
        },
        {
          "name": "MISSED_WIN_OPENING_PHASE",
          "number": 29
        },
        {
          "name": "MISSED_WIN_MID_GAME_PHASE",
          "number": 30
        },
        {
          "name": "MISSED_WIN_END_GAME_PHASE",
          "number": 31
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 132659.

```text
dheS52MSI5ChhHYW1lUmVsYXRpb25zaGlwTWV0YWRhdGESEwoLYXJlX2ZyaWVuZHMYASABKAg6CIKmHQQKAgECYgZwcm90bzM","chesscom/analysis/v1/move_classifications.proto":"Ci9jaGVzc2NvbS9hbmFseXNpcy92MS9tb3ZlX2NsYXNzaWZpY2F0aW9ucy5wcm90bxIUY2hlc3Njb20uYW5hbHlzaXMudjEqzAUKEk1vdmVDbGFzc2lmaWNhdGlvbhIjCh9NT1ZFX0NMQVNTSUZJQ0FUSU9OX1VOU1BFQ0lGSUVEEAASCAoEQk9PSxABEg0KCUJSSUxMSUFOVBACEg0KCUdSRUFURklORBADEggKBEJFU1QQBBINCglFWENFTExFTlQQBRIICgRHT0
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17535"></a>
## FND-17535: Full frontend descriptor: chesscom/analysis/v2/move_classifications.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/analysis/v2/move_classifications.proto",
  "package": "chesscom.analysis.v2",
  "enum_type": [
    {
      "name": "MoveClassification",
      "value": [
        {
          "name": "MOVE_CLASSIFICATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MOVE_CLASSIFICATION_BOOK",
          "number": 1
        },
        {
          "name": "MOVE_CLASSIFICATION_BRILLIANT",
          "number": 2
        },
        {
          "name": "MOVE_CLASSIFICATION_GREAT_FIND",
          "number": 3
        },
        {
          "name": "MOVE_CLASSIFICATION_BEST",
          "number": 4
        },
        {
          "name": "MOVE_CLASSIFICATION_EXCELLENT",
          "number": 5
        },
        {
          "name": "MOVE_CLASSIFICATION_GOOD",
          "number": 6
        },
        {
          "name": "MOVE_CLASSIFICATION_INACCURACY",
          "number": 7
        },
        {
          "name": "MOVE_CLASSIFICATION_MISTAKE",
          "number": 8
        },
        {
          "name": "MOVE_CLASSIFICATION_BLUNDER",
          "number": 9
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_WIN",
          "number": 10
        },
        {
          "name": "MOVE_CLASSIFICATION_FORCED",
          "number": 11
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_FASTER_MATE",
          "number": 12
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_MATE",
          "number": 13
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_FREE_PIECE",
          "number": 14
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_TACTIC",
          "number": 15
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_COMEBACK",
          "number": 16
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_OPPORTUNITY",
          "number": 17
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_BRILLIANT",
          "number": 18
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED_CRITICAL",
          "number": 19
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 133776.

```text
TRURfV0lOX01JRF9HQU1FX1BIQVNFEB4SHQoZTUlTU0VEX1dJTl9FTkRfR0FNRV9QSEFTRRAfGgiKph0ECgIBAmIGcHJvdG8z","chesscom/analysis/v2/move_classifications.proto":"Ci9jaGVzc2NvbS9hbmFseXNpcy92Mi9tb3ZlX2NsYXNzaWZpY2F0aW9ucy5wcm90bxIUY2hlc3Njb20uYW5hbHlzaXMudjIq/AUKEk1vdmVDbGFzc2lmaWNhdGlvbhIjCh9NT1ZFX0NMQVNTSUZJQ0FUSU9OX1VOU1BFQ0lGSUVEEAASHAoYTU9WRV9DTEFTU0lGSUNBVElPTl9CT09LEAESIQodTU9WRV9DTEFTU0lGSUNBVElPTl9CUklMTElBTlQQAhIiCh5NT1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17536"></a>
## FND-17536: Full frontend descriptor: chesscom/game_gateway/v1/game_analysis_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v1/game_analysis_metadata.proto",
  "package": "chesscom.game_gateway.v1",
  "message_type": [
    {
      "name": "GameAnalysisMetadata",
      "field": [
        {
          "name": "white_player_metadata",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.AnalysisData"
        },
        {
          "name": "black_player_metadata",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.AnalysisData"
        }
      ],
      "options": {}
    },
    {
      "name": "AnalysisData",
      "field": [
        {
          "name": "themes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.AnalysisData.AnalysisTheme"
        },
        {
          "name": "move_classification_counts",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "accuracy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "move_classification_counts_v2",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2"
        }
      ],
      "nested_type": [
        {
          "name": "MoveClassificationCounts",
          "field": [
            {
              "name": "move_classification",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.analysis.v1.MoveClassification"
            },
            {
              "name": "count",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_UINT32"
            }
          ]
        },
        {
          "name": "MoveClassificationCountsV2",
          "field": [
            {
              "name": "move_classification",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_ENUM",
              "type_name": ".chesscom.analysis.v2.MoveClassification"
            },
            {
              "name": "count",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_UINT32"
            }
          ]
        },
        {
          "name": "AnalysisTheme",
          "field": [
            {
              "name": "theme",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "ply",
              "number": 2,
              "label": "LABEL_REPEATED",
              "type": "TYPE_UINT32"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_accuracy"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 134957.

```text
FRF9CUklMTElBTlQQEhInCiNNT1ZFX0NMQVNTSUZJQ0FUSU9OX01JU1NFRF9DUklUSUNBTBATGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_gateway/v1/game_analysis_metadata.proto":"CjVjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvZ2FtZV9hbmFseXNpc19tZXRhZGF0YS5wcm90bxIYY2hlc3Njb20uZ2FtZV9nYXRld2F5LnYxIq4BChRHYW1lQW5hbHlzaXNNZXRhZGF0YRJFChV3aGl0ZV9wbGF5ZXJfbWV0YWRhdGEYASABKAsyJi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuQW5hbHlzaXNEYXRhEkUKFWJsYWNrX3BsYXllcl9tZXRh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17537"></a>
## FND-17537: Full frontend descriptor: chesscom/game_gateway/v1/opening_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v1/opening_metadata.proto",
  "package": "chesscom.game_gateway.v1",
  "message_type": [
    {
      "name": "OpeningMetadata",
      "field": [
        {
          "name": "eco_family_name",
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
  Character offset 136196.

```text
NQW5hbHlzaXNUaGVtZRINCgV0aGVtZRgBIAEoCRILCgNwbHkYAiADKA06CIKmHQQKAgECQgsKCV9hY2N1cmFjeWIGcHJvdG8z","chesscom/game_gateway/v1/opening_metadata.proto":"Ci9jaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvb3BlbmluZ19tZXRhZGF0YS5wcm90bxIYY2hlc3Njb20uZ2FtZV9nYXRld2F5LnYxIjQKD09wZW5pbmdNZXRhZGF0YRIXCg9lY29fZmFtaWx5X25hbWUYASABKAk6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v1/pgn_metadata.proto":"CitjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvcG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17538"></a>
## FND-17538: Full frontend descriptor: chesscom/game_gateway/v1/pgn_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v1/pgn_metadata.proto",
  "package": "chesscom.game_gateway.v1",
  "message_type": [
    {
      "name": "PgnMetadata",
      "field": [
        {
          "name": "pgn",
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
  Character offset 136432.

```text
9nYXRld2F5LnYxIjQKD09wZW5pbmdNZXRhZGF0YRIXCg9lY29fZmFtaWx5X25hbWUYASABKAk6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v1/pgn_metadata.proto":"CitjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvcGduX21ldGFkYXRhLnByb3RvEhhjaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEiJAoLUGduTWV0YWRhdGESCwoDcGduGAEgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/user/v1/user_type.proto":"CiBjaGVzc2NvbS91c2VyL3YxL3VzZXJfdHlwZS5wcm90bxIQY2hlc3Njb20udXNlci52MSpwCghVc2Vy
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17539"></a>
## FND-17539: Full frontend descriptor: chesscom/user/v1/user_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user/v1/user_type.proto",
  "package": "chesscom.user.v1",
  "enum_type": [
    {
      "name": "UserType",
      "value": [
        {
          "name": "USER_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_TYPE_USER",
          "number": 1
        },
        {
          "name": "USER_TYPE_GUEST",
          "number": 2
        },
        {
          "name": "USER_TYPE_COMPUTER",
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
  Character offset 136637.

```text
vEhhjaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEiJAoLUGduTWV0YWRhdGESCwoDcGduGAEgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/user/v1/user_type.proto":"CiBjaGVzc2NvbS91c2VyL3YxL3VzZXJfdHlwZS5wcm90bxIQY2hlc3Njb20udXNlci52MSpwCghVc2VyVHlwZRIZChVVU0VSX1RZUEVfVU5TUEVDSUZJRUQQABISCg5VU0VSX1RZUEVfVVNFUhABEhMKD1VTRVJfVFlQRV9HVUVTVBACEhYKElVTRVJfVFlQRV9DT01QVVRFUhADGgiKph0ECgIBAmIGcHJvdG8z","chesscom/unlockables/v1/resources.proto":"CidjaGVz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17540"></a>
## FND-17540: Full frontend descriptor: chesscom/unlockables/v1/resources.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/unlockables/v1/resources.proto",
  "package": "chesscom.unlockables.v1",
  "message_type": [
    {
      "name": "UnlockableResourceIdentifier",
      "field": [
        {
          "name": "resource_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.unlockables.v1.ResourceType"
        },
        {
          "name": "resource_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "UnlockablePreview",
      "field": [
        {
          "name": "label",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "image_url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "UnlockablePreviewItem",
      "field": [
        {
          "name": "identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockableResourceIdentifier"
        },
        {
          "name": "preview",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        }
      ]
    },
    {
      "name": "Unlockable",
      "field": [
        {
          "name": "identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockableResourceIdentifier"
        },
        {
          "name": "preview",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        },
        {
          "name": "unlocked_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_unlocked_at"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ResourceType",
      "value": [
        {
          "name": "RESOURCE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RESOURCE_TYPE_FLAIR",
          "number": 1
        },
        {
          "name": "RESOURCE_TYPE_THEME_BACKGROUND",
          "number": 2
        },
        {
          "name": "RESOURCE_TYPE_THEME_BOARD_STYLE",
          "number": 3
        },
        {
          "name": "RESOURCE_TYPE_THEME_PIECE_SET",
          "number": 4
        },
        {
          "name": "RESOURCE_TYPE_THEME_SOUND_SET",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "ResourceStatus",
      "value": [
        {
          "name": "RESOURCE_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RESOURCE_STATUS_LOCKED",
          "number": 1
        },
        {
          "name": "RESOURCE_STATUS_UNLOCKED",
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
  Character offset 136907.

```text
ZUEVfVVNFUhABEhMKD1VTRVJfVFlQRV9HVUVTVBACEhYKElVTRVJfVFlQRV9DT01QVVRFUhADGgiKph0ECgIBAmIGcHJvdG8z","chesscom/unlockables/v1/resources.proto":"CidjaGVzc2NvbS91bmxvY2thYmxlcy92MS9yZXNvdXJjZXMucHJvdG8SF2NoZXNzY29tLnVubG9ja2FibGVzLnYxInsKHFVubG9ja2FibGVSZXNvdXJjZUlkZW50aWZpZXISPAoNcmVzb3VyY2VfdHlwZRgBIAEoDjIlLmNoZXNzY29tLnVubG9ja2FibGVzLnYxLlJlc291cmNlVHlwZRITCgtyZXNvdXJjZV9pZBgCIAEoCToIgqYdBAoCAQIiPwoRVW5sb2NrYWJsZVByZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17541"></a>
## FND-17541: Full frontend descriptor: chesscom/flair/v1/flair.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/flair/v1/flair.proto",
  "package": "chesscom.flair.v1",
  "message_type": [
    {
      "name": "Flair",
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
          "name": "images",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair.ImagesEntry"
        },
        {
          "name": "category",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair.Category"
        },
        {
          "name": "display_priority",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "unlockable_preview",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        },
        {
          "name": "legacy_code",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "nested_type": [
        {
          "name": "ImagesEntry",
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
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "Category",
          "field": [
            {
              "name": "name",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_legacy_code"
        }
      ]
    },
    {
      "name": "FlairSelectionItem",
      "field": [
        {
          "name": "flair",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair"
        },
        {
          "name": "available",
          "number": 2,
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
  Character offset 138288.

```text
WUkVTT1VSQ0VfU1RBVFVTX0xPQ0tFRBABEhwKGFJFU09VUkNFX1NUQVRVU19VTkxPQ0tFRBACGgiKph0ECgIBAmIGcHJvdG8z","chesscom/flair/v1/flair.proto":"Ch1jaGVzc2NvbS9mbGFpci92MS9mbGFpci5wcm90bxIRY2hlc3Njb20uZmxhaXIudjEi/wIKBUZsYWlyEgoKAmlkGAEgASgJEgwKBG5hbWUYAiABKAkSEwoLZGVzY3JpcHRpb24YAyABKAkSNAoGaW1hZ2VzGAQgAygLMiQuY2hlc3Njb20uZmxhaXIudjEuRmxhaXIuSW1hZ2VzRW50cnkSMwoIY2F0ZWdvcnkYBSABKAsyIS5jaGVzc2NvbS5mbGFpci52MS5GbGFpci5DYXRlZ29yeRIY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17542"></a>
## FND-17542: Full frontend descriptor: chesscom/flair/v1/flair_view.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/flair/v1/flair_view.proto",
  "package": "chesscom.flair.v1",
  "message_type": [
    {
      "name": "FlairView",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "images",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.FlairView.ImagesEntry"
        },
        {
          "name": "description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "nested_type": [
        {
          "name": "ImagesEntry",
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
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    },
    {
      "name": "UserFlair",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "flair",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.FlairView",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_flair"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 139037.

```text
mxhaXIYASABKAsyGC5jaGVzc2NvbS5mbGFpci52MS5GbGFpchIRCglhdmFpbGFibGUYAiABKAg6B4KmHQMKAQFiBnByb3RvMw","chesscom/flair/v1/flair_view.proto":"CiJjaGVzc2NvbS9mbGFpci92MS9mbGFpcl92aWV3LnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSKfAQoJRmxhaXJWaWV3EgoKAmlkGAEgASgJEjgKBmltYWdlcxgCIAMoCzIoLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyVmlldy5JbWFnZXNFbnRyeRITCgtkZXNjcmlwdGlvbhgDIAEoCRotCgtJbWFnZXNFbnRyeRILCgNrZXkYASABKAkSDQoFdmFsdWUYAiABKAk6AjgBOgiCph0
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17543"></a>
## FND-17543: Full frontend descriptor: chesscom/flair/v1/flair_internal_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/flair/v1/flair_internal_service.proto",
  "package": "chesscom.flair.v1",
  "message_type": [
    {
      "name": "ListFlairInternalRequest"
    },
    {
      "name": "ListFlairInternalResponse",
      "field": [
        {
          "name": "flair",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair"
        }
      ]
    },
    {
      "name": "ListFlairByIdsInternalRequest",
      "field": [
        {
          "name": "flair_ids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ListFlairByIdsInternalResponse",
      "field": [
        {
          "name": "flair",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair"
        }
      ]
    },
    {
      "name": "SetUserFlairInternalRequest",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "flair_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SetUserFlairInternalResponse"
    }
  ],
  "service": [
    {
      "name": "FlairInternalService",
      "method": [
        {
          "name": "ListFlairInternal",
          "input_type": ".chesscom.flair.v1.ListFlairInternalRequest",
          "output_type": ".chesscom.flair.v1.ListFlairInternalResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListFlairByIdsInternal",
          "input_type": ".chesscom.flair.v1.ListFlairByIdsInternalRequest",
          "output_type": ".chesscom.flair.v1.ListFlairByIdsInternalResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "SetUserFlairInternal",
          "input_type": ".chesscom.flair.v1.SetUserFlairInternalRequest",
          "output_type": ".chesscom.flair.v1.SetUserFlairInternalResponse",
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
  Character offset 139509.

```text
mbGFpchgCIAEoCzIcLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyVmlld0gAiAEBOgeCph0DCgEBQggKBl9mbGFpcmIGcHJvdG8z","chesscom/flair/v1/flair_internal_service.proto":"Ci5jaGVzc2NvbS9mbGFpci92MS9mbGFpcl9pbnRlcm5hbF9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIaChhMaXN0RmxhaXJJbnRlcm5hbFJlcXVlc3QiRAoZTGlzdEZsYWlySW50ZXJuYWxSZXNwb25zZRInCgVmbGFpchgBIAMoCzIYLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyIjIKHUxpc3RGbGFpckJ5SWRzSW50ZXJuYWxSZXF1ZXN0EhEKCWZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17547"></a>
## FND-17547: Full frontend descriptor: chesscom/proto_options/manifest/v1/annotations.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/manifest/v1/annotations.proto",
  "package": "chesscom.proto_options.manifest.v1",
  "message_type": [
    {
      "name": "GnsServiceOptions",
      "field": [
        {
          "name": "providers",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "cli_group",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "scope",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "skip",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "cli_alias",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "default_access",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.manifest.v1.GnsAccess"
        }
      ]
    },
    {
      "name": "GnsMethodOptions",
      "field": [
        {
          "name": "cli_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "scope",
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
          "name": "examples",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "skip",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "agent_tool",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.manifest.v1.GnsAgentTool"
        },
        {
          "name": "access",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.manifest.v1.GnsAccess"
        }
      ]
    },
    {
      "name": "GnsAgentTool",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GnsAccess",
      "field": [
        {
          "name": "requires",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "GnsFieldOptions",
      "field": [
        {
          "name": "client_hash",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.manifest.v1.ClientHash"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ClientHash",
      "value": [
        {
          "name": "CLIENT_HASH_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CLIENT_HASH_EMAIL_SHA256",
          "number": 1
        },
        {
          "name": "CLIENT_HASH_PHONE_SHA256",
          "number": 2
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "gns_service",
      "extendee": ".google.protobuf.ServiceOptions",
      "number": 50100,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.manifest.v1.GnsServiceOptions",
      "json_name": "gnsService"
    },
    {
      "name": "gns_method",
      "extendee": ".google.protobuf.MethodOptions",
      "number": 50101,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.manifest.v1.GnsMethodOptions",
      "json_name": "gnsMethod"
    },
    {
      "name": "gns_field",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 50102,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.manifest.v1.GnsFieldOptions",
      "json_name": "gnsField"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 140679.

```text
mxhaXJJbnRlcm5hbFJlc3BvbnNlIgBCKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/proto_options/manifest/v1/annotations.proto":"CjRjaGVzc2NvbS9wcm90b19vcHRpb25zL21hbmlmZXN0L3YxL2Fubm90YXRpb25zLnByb3RvEiJjaGVzc2NvbS5wcm90b19vcHRpb25zLm1hbmlmZXN0LnYxIsUBChFHbnNTZXJ2aWNlT3B0aW9ucxIRCglwcm92aWRlcnMYASADKAkSEQoJY2xpX2dyb3VwGAIgASgJEg0KBXNjb3BlGAMgASgJEhMKC2Rlc2NyaXB0aW9uGAQgASgJEgwKBHNraXAYBSABK
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17548"></a>
## FND-17548: Full frontend descriptor: chesscom/flair/v1/flair_admin_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/flair/v1/flair_admin_service.proto",
  "package": "chesscom.flair.v1",
  "message_type": [
    {
      "name": "ListFlairRequest"
    },
    {
      "name": "ListFlairResponse",
      "field": [
        {
          "name": "flair",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair"
        }
      ]
    },
    {
      "name": "ListFlairByIdsRequest",
      "field": [
        {
          "name": "flair_ids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ListFlairByIdsResponse",
      "field": [
        {
          "name": "flair",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair"
        }
      ]
    },
    {
      "name": "ListFlairByNamePrefixRequest",
      "field": [
        {
          "name": "name_prefix",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ListFlairByNamePrefixResponse",
      "field": [
        {
          "name": "flair",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.Flair"
        }
      ]
    },
    {
      "name": "SetUserFlairRequest",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "flair_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "SetUserFlairResponse",
      "options": {
        "deprecated": true
      }
    }
  ],
  "service": [
    {
      "name": "FlairAdminService",
      "method": [
        {
          "name": "ListFlair",
          "input_type": ".chesscom.flair.v1.ListFlairRequest",
          "output_type": ".chesscom.flair.v1.ListFlairResponse",
          "options": {}
        },
        {
          "name": "ListFlairByIds",
          "input_type": ".chesscom.flair.v1.ListFlairByIdsRequest",
          "output_type": ".chesscom.flair.v1.ListFlairByIdsResponse",
          "options": {}
        },
        {
          "name": "ListFlairByNamePrefix",
          "input_type": ".chesscom.flair.v1.ListFlairByNamePrefixRequest",
          "output_type": ".chesscom.flair.v1.ListFlairByNamePrefixResponse",
          "options": {}
        },
        {
          "name": "SetUserFlair",
          "input_type": ".chesscom.flair.v1.SetUserFlairRequest",
          "output_type": ".chesscom.flair.v1.SetUserFlairResponse",
          "options": {
            "deprecated": true
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
  Character offset 142295.

```text
AsyMy5jaGVzc2NvbS5wcm90b19vcHRpb25zLm1hbmlmZXN0LnYxLkduc0ZpZWxkT3B0aW9uc1IIZ25zRmllbGRiBnByb3RvMw","chesscom/flair/v1/flair_admin_service.proto":"CitjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9hZG1pbl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSISChBMaXN0RmxhaXJSZXF1ZXN0IjwKEUxpc3RGbGFpclJlc3BvbnNlEicKBWZsYWlyGAEgAygLMhguY2hlc3Njb20uZmxhaXIudjEuRmxhaXIiKgoVTGlzdEZsYWlyQnlJZHNSZXF1ZXN0EhEKCWZsYWlyX2lkcxgBIAMoCSJBChZMaXN0RmxhaXJCeU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17553"></a>
## FND-17553: Full frontend descriptor: chesscom/flair/v1/flair_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/flair/v1/flair_service.proto",
  "package": "chesscom.flair.v1",
  "message_type": [
    {
      "name": "ListFlairSelectionRequest",
      "options": {}
    },
    {
      "name": "ListFlairSelectionResponse",
      "field": [
        {
          "name": "flair_selection",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.FlairSelectionItem"
        }
      ],
      "options": {}
    },
    {
      "name": "SelectFlairRequest",
      "field": [
        {
          "name": "flair_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "SelectFlairResponse",
      "options": {}
    },
    {
      "name": "RemoveFlairRequest",
      "options": {}
    },
    {
      "name": "RemoveFlairResponse",
      "options": {}
    },
    {
      "name": "GetUserFlairRequest",
      "field": [
        {
          "name": "user_id",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_id"
        }
      ]
    },
    {
      "name": "GetUserFlairResponse",
      "field": [
        {
          "name": "user_flair",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.UserFlair"
        }
      ],
      "options": {}
    },
    {
      "name": "ListUserFlairRequest",
      "field": [
        {
          "name": "user_ids",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "ListUserFlairResponse",
      "field": [
        {
          "name": "user_flair",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.UserFlair"
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "FlairService",
      "method": [
        {
          "name": "ListFlairSelection",
          "input_type": ".chesscom.flair.v1.ListFlairSelectionRequest",
          "output_type": ".chesscom.flair.v1.ListFlairSelectionResponse",
          "options": {}
        },
        {
          "name": "SelectFlair",
          "input_type": ".chesscom.flair.v1.SelectFlairRequest",
          "output_type": ".chesscom.flair.v1.SelectFlairResponse",
          "options": {}
        },
        {
          "name": "RemoveFlair",
          "input_type": ".chesscom.flair.v1.RemoveFlairRequest",
          "output_type": ".chesscom.flair.v1.RemoveFlairResponse",
          "options": {}
        },
        {
          "name": "GetUserFlair",
          "input_type": ".chesscom.flair.v1.GetUserFlairRequest",
          "output_type": ".chesscom.flair.v1.GetUserFlairResponse",
          "options": {}
        },
        {
          "name": "ListUserFlair",
          "input_type": ".chesscom.flair.v1.ListUserFlairRequest",
          "output_type": ".chesscom.flair.v1.ListUserFlairResponse",
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
  Character offset 145830.

```text
iBuYW1lIHByZWZpeDIIY2hlc3Njb21CKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/flair/v1/flair_service.proto":"CiVjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIkChlMaXN0RmxhaXJTZWxlY3Rpb25SZXF1ZXN0OgeCph0DCgEBImUKGkxpc3RGbGFpclNlbGVjdGlvblJlc3BvbnNlEj4KD2ZsYWlyX3NlbGVjdGlvbhgBIAMoCzIlLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyU2VsZWN0aW9uSXRlbToHgqYdAwoBASIvChJTZWxlY3RG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17559"></a>
## FND-17559: Full frontend descriptor: chesscom/user/v1/user_view.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user/v1/user_view.proto",
  "package": "chesscom.user.v1",
  "message_type": [
    {
      "name": "UserView",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user.v1.UserType"
        },
        {
          "name": "username",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "first_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_name",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "chess_title",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "avatar",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.Avatar"
        },
        {
          "name": "flair",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.FlairView",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "membership",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "country",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "timezone",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "created_at",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "updated_at",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "is_enabled",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "is_content_hidden",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "is_streamer",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_verified",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "content_language_includes_english",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "flair_code",
          "number": 99,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_first_name"
        },
        {
          "name": "_last_name"
        },
        {
          "name": "_chess_title"
        },
        {
          "name": "_flair"
        },
        {
          "name": "_country"
        },
        {
          "name": "_timezone"
        },
        {
          "name": "_created_at"
        },
        {
          "name": "_updated_at"
        },
        {
          "name": "_is_enabled"
        },
        {
          "name": "_is_content_hidden"
        },
        {
          "name": "_is_verified"
        },
        {
          "name": "_content_language_includes_english"
        }
      ]
    },
    {
      "name": "Avatar",
      "field": [
        {
          "name": "url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "high_resolution_url",
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
  Character offset 147456.

```text
hlc3Njb20uZmxhaXIudjEuTGlzdFVzZXJGbGFpclJlc3BvbnNlIgAaB5KmHQMKAQFCDsq3LAoKBC9ycGMSABoAYgZwcm90bzM","chesscom/user/v1/user_view.proto":"CiBjaGVzc2NvbS91c2VyL3YxL3VzZXJfdmlldy5wcm90bxIQY2hlc3Njb20udXNlci52MSK4BgoIVXNlclZpZXcSCgoCaWQYASABKAkSDwoHdXNlcl9pZBgCIAEoAxIoCgR0eXBlGAMgASgOMhouY2hlc3Njb20udXNlci52MS5Vc2VyVHlwZRIQCgh1c2VybmFtZRgEIAEoCRIXCgpmaXJzdF9uYW1lGAUgASgJSACIAQESFgoJbGFzdF9uYW1lGAYgASgJSAGIAQESGAoLY2hlc3Nfd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17560"></a>
## FND-17560: Full frontend descriptor: chesscom/support/v1/support_action_confirmation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/support/v1/support_action_confirmation.proto",
  "package": "chesscom.support.v1",
  "enum_type": [
    {
      "name": "SupportActionConfirmation",
      "value": [
        {
          "name": "SUPPORT_ACTION_CONFIRMATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SUPPORT_ACTION_CONFIRMATION_HUMAN_DIRECT",
          "number": 1
        },
        {
          "name": "SUPPORT_ACTION_CONFIRMATION_HUMAN_CONFIRMED",
          "number": 2
        },
        {
          "name": "SUPPORT_ACTION_CONFIRMATION_AGENT_AUTONOMOUS",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 148760.

```text
XNoIjwKBkF2YXRhchILCgN1cmwYASABKAkSGwoTaGlnaF9yZXNvbHV0aW9uX3VybBgCIAEoCToIgqYdBAoCAQJiBnByb3RvMw","chesscom/support/v1/support_action_confirmation.proto":"CjVjaGVzc2NvbS9zdXBwb3J0L3YxL3N1cHBvcnRfYWN0aW9uX2NvbmZpcm1hdGlvbi5wcm90bxITY2hlc3Njb20uc3VwcG9ydC52MSrZAQoZU3VwcG9ydEFjdGlvbkNvbmZpcm1hdGlvbhIrCidTVVBQT1JUX0FDVElPTl9DT05GSVJNQVRJT05fVU5TUEVDSUZJRUQQABIsCihTVVBQT1JUX0FDVElPTl9DT05GSVJNQVRJT05fSFVNQU5fRElSRUNUEAES
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17561"></a>
## FND-17561: Full frontend descriptor: chesscom/support/v1/support_action_context.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/support/v1/support_action_context.proto",
  "package": "chesscom.support.v1",
  "message_type": [
    {
      "name": "SupportActionContext",
      "field": [
        {
          "name": "actor",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "confirmation",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.support.v1.SupportActionConfirmation"
        },
        {
          "name": "confirmed_by",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "source_ref",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "reason",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "dry_run",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "idempotency_key",
          "number": 7,
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
  Character offset 149225.

```text
UFOX0NPTkZJUk1FRBACEjAKLFNVUFBPUlRfQUNUSU9OX0NPTkZJUk1BVElPTl9BR0VOVF9BVVRPTk9NT1VTEANiBnByb3RvMw","chesscom/support/v1/support_action_context.proto":"CjBjaGVzc2NvbS9zdXBwb3J0L3YxL3N1cHBvcnRfYWN0aW9uX2NvbnRleHQucHJvdG8SE2NoZXNzY29tLnN1cHBvcnQudjEizwEKFFN1cHBvcnRBY3Rpb25Db250ZXh0Eg0KBWFjdG9yGAEgASgJEkQKDGNvbmZpcm1hdGlvbhgCIAEoDjIuLmNoZXNzY29tLnN1cHBvcnQudjEuU3VwcG9ydEFjdGlvbkNvbmZpcm1hdGlvbhIUCgxjb25maXJtZWRfYnkYAyABK
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17562"></a>
## FND-17562: Full frontend descriptor: chesscom/support/v1/support_action_result.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/support/v1/support_action_result.proto",
  "package": "chesscom.support.v1",
  "message_type": [
    {
      "name": "SupportActionResult",
      "field": [
        {
          "name": "applied",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "dry_run",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "idempotency_key",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "replayed",
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
  Character offset 149665.

```text
hgEIAEoCRIOCgZyZWFzb24YBSABKAkSDwoHZHJ5X3J1bhgGIAEoCBIXCg9pZGVtcG90ZW5jeV9rZXkYByABKAliBnByb3RvMw","chesscom/support/v1/support_action_result.proto":"Ci9jaGVzc2NvbS9zdXBwb3J0L3YxL3N1cHBvcnRfYWN0aW9uX3Jlc3VsdC5wcm90bxITY2hlc3Njb20uc3VwcG9ydC52MSJiChNTdXBwb3J0QWN0aW9uUmVzdWx0Eg8KB2FwcGxpZWQYASABKAgSDwoHZHJ5X3J1bhgCIAEoCBIXCg9pZGVtcG90ZW5jeV9rZXkYAyABKAkSEAoIcmVwbGF5ZWQYBCABKAhiBnByb3RvMw","chesscom/support/v1/refund_in
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17563"></a>
## FND-17563: Full frontend descriptor: chesscom/support/v1/refund_ineligibility_reason.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/support/v1/refund_ineligibility_reason.proto",
  "package": "chesscom.support.v1",
  "enum_type": [
    {
      "name": "RefundIneligibilityReason",
      "value": [
        {
          "name": "REFUND_INELIGIBILITY_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_NO_ACTIVE_SUBSCRIPTION",
          "number": 1
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_OUTSIDE_REFUND_WINDOW",
          "number": 2
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_ALREADY_REFUNDED",
          "number": 3
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_NOT_REFUNDABLE_PAYMENT_METHOD",
          "number": 4
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_INTERNAL_ERROR",
          "number": 5
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_ZERO_AMOUNT_CHARGE",
          "number": 6
        },
        {
          "name": "REFUND_INELIGIBILITY_REASON_NOT_CURRENT_SUBSCRIPTION_CHARGE",
          "number": 7
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 149956.

```text
SABKAgSDwoHZHJ5X3J1bhgCIAEoCBIXCg9pZGVtcG90ZW5jeV9rZXkYAyABKAkSEAoIcmVwbGF5ZWQYBCABKAhiBnByb3RvMw","chesscom/support/v1/refund_ineligibility_reason.proto":"CjVjaGVzc2NvbS9zdXBwb3J0L3YxL3JlZnVuZF9pbmVsaWdpYmlsaXR5X3JlYXNvbi5wcm90bxITY2hlc3Njb20uc3VwcG9ydC52MSrNAwoZUmVmdW5kSW5lbGlnaWJpbGl0eVJlYXNvbhIrCidSRUZVTkRfSU5FTElHSUJJTElUWV9SRUFTT05fVU5TUEVDSUZJRUQQABI2CjJSRUZVTkRfSU5FTElHSUJJTElUWV9SRUFTT05fTk9fQUNUSVZFX1NVQlND
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17564"></a>
## FND-17564: Full frontend descriptor: chesscom/audit_logs/v1/audit_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/audit_logs/v1/audit_options.proto",
  "package": "chesscom.audit_logs.v1",
  "message_type": [
    {
      "name": "AuditFieldOptions",
      "field": [
        {
          "name": "field_sensitivity",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.audit_logs.v1.FieldSensitivity"
        },
        {
          "name": "description",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "required_permissions",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "indexed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "index_alias",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_indexed"
        },
        {
          "name": "_index_alias"
        }
      ]
    },
    {
      "name": "AuditMessageOptions",
      "field": [
        {
          "name": "message_sensitivity",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.audit_logs.v1.MessageSensitivity"
        },
        {
          "name": "description",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "required_permissions",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "AuditMethodOptions",
      "field": [
        {
          "name": "action_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sensitivity",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.audit_logs.v1.MessageSensitivity"
        },
        {
          "name": "required_permissions",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "request_reference_id_field",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "response_reference_id_field",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "log_errors",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "log_response",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_log_errors"
        },
        {
          "name": "_log_response"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "FieldSensitivity",
      "value": [
        {
          "name": "FIELD_SENSITIVITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FIELD_SENSITIVITY_DEFAULT",
          "number": 1
        },
        {
          "name": "FIELD_SENSITIVITY_ADVANCED",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "FIELD_SENSITIVITY_RESTRICTED",
          "number": 3
        }
      ]
    },
    {
      "name": "MessageSensitivity",
      "value": [
        {
          "name": "MESSAGE_SENSITIVITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MESSAGE_SENSITIVITY_DEFAULT",
          "number": 1
        },
        {
          "name": "MESSAGE_SENSITIVITY_RESTRICTED",
          "number": 2
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "audit_field",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 50105,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.audit_logs.v1.AuditFieldOptions",
      "json_name": "auditField"
    },
    {
      "name": "audit_message",
      "extendee": ".google.protobuf.MessageOptions",
      "number": 50106,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.audit_logs.v1.AuditMessageOptions",
      "json_name": "auditMessage"
    },
    {
      "name": "audit_rpc",
      "extendee": ".google.protobuf.MethodOptions",
      "number": 50103,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.audit_logs.v1.AuditMethodOptions",
      "json_name": "auditRpc"
    },
    {
      "name": "audit_rpc_defaults",
      "extendee": ".google.protobuf.ServiceOptions",
      "number": 50104,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.audit_logs.v1.AuditMethodOptions",
      "json_name": "auditRpcDefaults"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 150746.

```text
I/CjtSRUZVTkRfSU5FTElHSUJJTElUWV9SRUFTT05fTk9UX0NVUlJFTlRfU1VCU0NSSVBUSU9OX0NIQVJHRRAHYgZwcm90bzM","chesscom/audit_logs/v1/audit_options.proto":"CipjaGVzc2NvbS9hdWRpdF9sb2dzL3YxL2F1ZGl0X29wdGlvbnMucHJvdG8SFmNoZXNzY29tLmF1ZGl0X2xvZ3MudjEi1wEKEUF1ZGl0RmllbGRPcHRpb25zEkMKEWZpZWxkX3NlbnNpdGl2aXR5GAEgASgOMiguY2hlc3Njb20uYXVkaXRfbG9ncy52MS5GaWVsZFNlbnNpdGl2aXR5EhMKC2Rlc2NyaXB0aW9uGAIgASgJEhwKFHJlcXVpcmVkX3Blcm1pc3Npb25zGAM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17565"></a>
## FND-17565: Full frontend descriptor: chesscom/game_gateway/v1/player_details_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v1/player_details_metadata.proto",
  "package": "chesscom.game_gateway.v1",
  "message_type": [
    {
      "name": "PlayerDetailsMetadata",
      "field": [
        {
          "name": "white_player_metadata",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        },
        {
          "name": "black_player_metadata",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user.v1.UserView"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 152769.

```text
EoCzIqLmNoZXNzY29tLmF1ZGl0X2xvZ3MudjEuQXVkaXRNZXRob2RPcHRpb25zUhBhdWRpdFJwY0RlZmF1bHRzYgZwcm90bzM","chesscom/game_gateway/v1/player_details_metadata.proto":"CjZjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjEvcGxheWVyX2RldGFpbHNfbWV0YWRhdGEucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MSKXAQoVUGxheWVyRGV0YWlsc01ldGFkYXRhEjkKFXdoaXRlX3BsYXllcl9tZXRhZGF0YRgBIAEoCzIaLmNoZXNzY29tLnVzZXIudjEuVXNlclZpZXcSOQoVYmxhY2tfcGxheWVyX21ldGFkYXRhGAIgASg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17566"></a>
## FND-17566: Full frontend descriptor: chesscom/game_gateway/v2/hydrated_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v2/hydrated_game.proto",
  "package": "chesscom.game_gateway.v2",
  "message_type": [
    {
      "name": "HydratedGame",
      "field": [
        {
          "name": "game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.Game"
        },
        {
          "name": "cheat_metadata",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.cheat_metadata_storage.v1.GameCheatMetadata"
        },
        {
          "name": "relationship_metadata",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.GameRelationshipMetadata"
        },
        {
          "name": "analysis_metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.GameAnalysisMetadata"
        },
        {
          "name": "player_metadata",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.PlayerDetailsMetadata"
        },
        {
          "name": "favorite_metadata",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.FavoriteMetadata"
        },
        {
          "name": "bot_metadata",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotMetadata"
        },
        {
          "name": "coach_metadata",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.Coach"
        },
        {
          "name": "opening_metadata",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.OpeningMetadata"
        },
        {
          "name": "pgn_metadata",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v1.PgnMetadata"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 153155.

```text
mxhY2tfcGxheWVyX21ldGFkYXRhGAIgASgLMhouY2hlc3Njb20udXNlci52MS5Vc2VyVmlldzoIgqYdBAoCAQJiBnByb3RvMw","chesscom/game_gateway/v2/hydrated_game.proto":"CixjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvaHlkcmF0ZWRfZ2FtZS5wcm90bxIYY2hlc3Njb20uZ2FtZV9nYXRld2F5LnYyIq8FCgxIeWRyYXRlZEdhbWUSLAoEZ2FtZRgBIAEoCzIeLmNoZXNzY29tLmdhbWVfZ2F0ZXdheS52Mi5HYW1lEk0KDmNoZWF0X21ldGFkYXRhGAIgASgLMjUuY2hlc3Njb20uY2hlYXRfbWV0YWRhdGFfc3RvcmFnZS52MS5HYW1lQ2hlY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17567"></a>
## FND-17567: Full frontend descriptor: chesscom/game_gateway/v2/game_gateway_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v2/game_gateway_service.proto",
  "package": "chesscom.game_gateway.v2",
  "message_type": [
    {
      "name": "HydrateGamesByCriteriaRequest",
      "field": [
        {
          "name": "criteria",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.Criteria"
        },
        {
          "name": "field_mask",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        },
        {
          "name": "pagination",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 0,
          "proto3_optional": true
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
      "name": "HydrateGamesByCriteriaResponse",
      "field": [
        {
          "name": "hydrated_games",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.HydratedGame"
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
      "name": "AggregateGameResultsByPlayerAndCriteriaRequest",
      "field": [
        {
          "name": "player_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "aggregate_criteria",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.AggregateCriteria",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_aggregate_criteria"
        }
      ]
    },
    {
      "name": "AggregateGameResultsByPlayerAndCriteriaResponse",
      "field": [
        {
          "name": "wins",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "draws",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "losses",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayerOverviewStatsRequest",
      "field": [
        {
          "name": "player_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "time_class",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "variant",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "field_mask",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        },
        {
          "name": "is_vs_computer",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_vs_coach",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "game_end_time_from",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "game_end_time_to",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_time_class"
        },
        {
          "name": "_variant"
        },
        {
          "name": "_game_end_time_from"
        },
        {
          "name": "_game_end_time_to"
        }
      ]
    },
    {
      "name": "PlayerOverviewStatsResponse",
      "field": [
        {
          "name": "white_counts",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.OverviewGameCount"
        },
        {
          "name": "black_counts",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.OverviewGameCount"
        },
        {
          "name": "highest_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "highest_rating_date",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "best_win",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "best_win_streak",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "average_opponent_rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "average_opponent_rating_win",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "average_opponent_rating_lose",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "average_opponent_rating_draw",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "ratings",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.OverviewGameRatings"
        },
        {
          "name": "daily_game_timeout_count",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "best_win_opponent_username",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "best_win_game_id",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "most_played_eco_family_id",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "brilliant_moves_count",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_daily_game_timeout_count"
        },
        {
          "name": "_best_win_opponent_username"
        },
        {
          "name": "_best_win_game_id"
        },
        {
          "name": "_most_played_eco_family_id"
        }
      ]
    },
    {
      "name": "OverviewGameRatings",
      "field": [
        {
          "name": "timestamp",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    },
    {
      "name": "OverviewGameCount",
      "field": [
        {
          "name": "wins",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "draws",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "losses",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        }
      ],
      "options": {}
    },
    {
      "name": "AggregateCriteria",
      "field": [
        {
          "name": "time_classes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "variants",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "opening",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.OpeningCriteria",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "opponent_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
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
          "name": "is_rated",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "game_end_time_from",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "game_end_time_to",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_opening"
        },
        {
          "name": "_opponent_id"
        },
        {
          "name": "_color"
        },
        {
          "name": "_is_rated"
        },
        {
          "name": "_game_end_time_from"
        },
        {
          "name": "_game_end_time_to"
        }
      ]
    },
    {
      "name": "Criteria",
      "field": [
        {
          "name": "accuracy_from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "accuracy_to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "opponent_accuracy_from",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "opponent_accuracy_to",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "opponent_username",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "opponent_ids",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "username",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "opponent_titles",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerTitle"
        },
        {
          "name": "rating_from",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "rating_to",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "opponent_rating_from",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "opponent_rating_to",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "color",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "are_friends",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "theme",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "opponent_theme",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "opening",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.OpeningCriteria",
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "ply_from",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "ply_to",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "base_time",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "time_increment",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "time_classes",
          "number": 22,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "game_provider",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameProvider",
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "is_vs_computer",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "game_results",
          "number": 25,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameResult"
        },
        {
          "name": "player_results",
          "number": 26,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerResult"
        },
        {
          "name": "opponent_player_results",
          "number": 27,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerResult"
        },
        {
          "name": "tournament_id",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "team_match_id",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "is_tournament",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "is_team_match",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "is_rated",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "game_end_time_from",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "game_end_time_to",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "game_start_time_from",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "game_start_time_to",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "variants",
          "number": 37,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "page",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "page_size",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "sort_direction",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_gateway.v2.SortDirection",
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "sort_fields",
          "number": 41,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_gateway.v2.SortField"
        },
        {
          "name": "base_time_from",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "base_time_to",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "time_increment_from",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "time_increment_to",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "game_ids",
          "number": 46,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "player_id",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "tournament_ids",
          "number": 48,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "brilliant_count_from",
          "number": 49,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "brilliant_count_to",
          "number": 50,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "arena_ids",
          "number": 51,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "is_arena",
          "number": 52,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "has_accuracy",
          "number": 53,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "toggle_rate_from",
          "number": 54,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "toggle_rate_to",
          "number": 55,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 43,
          "proto3_optional": true
        },
        {
          "name": "is_vs_coach",
          "number": 56,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 44,
          "proto3_optional": true
        },
        {
          "name": "random_order_seed",
          "number": 57,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 45,
          "proto3_optional": true
        },
        {
          "name": "is_favorite",
          "number": 58,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 46,
          "proto3_optional": true
        },
        {
          "name": "tournament_round",
          "number": 59,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 47,
          "proto3_optional": true
        },
        {
          "name": "player_titles",
          "number": 60,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerTitle"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_accuracy_from"
        },
        {
          "name": "_accuracy_to"
        },
        {
          "name": "_opponent_accuracy_from"
        },
        {
          "name": "_opponent_accuracy_to"
        },
        {
          "name": "_opponent_username"
        },
        {
          "name": "_username"
        },
        {
          "name": "_rating_from"
        },
        {
          "name": "_rating_to"
        },
        {
          "name": "_opponent_rating_from"
        },
        {
          "name": "_opponent_rating_to"
        },
        {
          "name": "_color"
        },
        {
          "name": "_are_friends"
        },
        {
          "name": "_theme"
        },
        {
          "name": "_opponent_theme"
        },
        {
          "name": "_opening"
        },
        {
          "name": "_ply_from"
        },
        {
          "name": "_ply_to"
        },
        {
          "name": "_base_time"
        },
        {
          "name": "_time_increment"
        },
        {
          "name": "_game_provider"
        },
        {
          "name": "_is_vs_computer"
        },
        {
          "name": "_tournament_id"
        },
        {
          "name": "_team_match_id"
        },
        {
          "name": "_is_tournament"
        },
        {
          "name": "_is_team_match"
        },
        {
          "name": "_is_rated"
        },
        {
          "name": "_game_end_time_from"
        },
        {
          "name": "_game_end_time_to"
        },
        {
          "name": "_game_start_time_from"
        },
        {
          "name": "_game_start_time_to"
        },
        {
          "name": "_page"
        },
        {
          "name": "_page_size"
        },
        {
          "name": "_sort_direction"
        },
        {
          "name": "_base_time_from"
        },
        {
          "name": "_base_time_to"
        },
        {
          "name": "_time_increment_from"
        },
        {
          "name": "_time_increment_to"
        },
        {
          "name": "_player_id"
        },
        {
          "name": "_brilliant_count_from"
        },
        {
          "name": "_brilliant_count_to"
        },
        {
          "name": "_is_arena"
        },
        {
          "name": "_has_accuracy"
        },
        {
          "name": "_toggle_rate_from"
        },
        {
          "name": "_toggle_rate_to"
        },
        {
          "name": "_is_vs_coach"
        },
        {
          "name": "_random_order_seed"
        },
        {
          "name": "_is_favorite"
        },
        {
          "name": "_tournament_round"
        }
      ]
    },
    {
      "name": "CountGamesByCriteriaRequest",
      "field": [
        {
          "name": "criteria",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.Criteria"
        }
      ],
      "options": {}
    },
    {
      "name": "CountGamesByCriteriaResponse",
      "field": [
        {
          "name": "count",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64"
        }
      ],
      "options": {}
    },
    {
      "name": "DeleteGameRequest",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "DeleteGameResponse",
      "options": {}
    },
    {
      "name": "HydrateGameByLegacyIdRequest",
      "field": [
        {
          "name": "legacy_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64"
        },
        {
          "name": "variants",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "time_classes",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "game_provider",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameProvider"
        },
        {
          "name": "is_vs_computer",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "field_mask",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.FieldMask"
        },
        {
          "name": "is_vs_coach",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "HydrateGameByLegacyIdResponse",
      "field": [
        {
          "name": "hydrated_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.HydratedGame"
        }
      ],
      "options": {}
    },
    {
      "name": "OpeningCriteria",
      "field": [
        {
          "name": "eco_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0
        },
        {
          "name": "eco_family_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0
        },
        {
          "name": "eco_code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
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
      "name": "CountTournamentsByPlayerRequest",
      "field": [
        {
          "name": "player_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "CountTournamentsByPlayerResponse",
      "field": [
        {
          "name": "total",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayerOverviewAllStatsRequest",
      "field": [
        {
          "name": "player_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "days",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_days"
        }
      ]
    },
    {
      "name": "PlayerOverviewAllStatsResponse",
      "field": [
        {
          "name": "entries",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.AllStatsEntry"
        }
      ],
      "options": {}
    },
    {
      "name": "AllStatsEntry",
      "field": [
        {
          "name": "variant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "time_class",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "rating_change",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "total_games",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "SortDirection",
      "value": [
        {
          "name": "SORT_DIRECTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SORT_DIRECTION_ASC",
          "number": 1
        },
        {
          "name": "SORT_DIRECTION_DESC",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "SortField",
      "value": [
        {
          "name": "SORT_FIELD_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SORT_FIELD_USERNAME",
          "number": 1
        },
        {
          "name": "SORT_FIELD_GAME_ID",
          "number": 2
        },
        {
          "name": "SORT_FIELD_GAME_START_TIME",
          "number": 3
        },
        {
          "name": "SORT_FIELD_GAME_END_TIME",
          "number": 4
        },
        {
          "name": "SORT_FIELD_RATED",
          "number": 5
        },
        {
          "name": "SORT_FIELD_IS_PRIVATE",
          "number": 6
        },
        {
          "name": "SORT_FIELD_BASE_TIME",
          "number": 7
        },
        {
          "name": "SORT_FIELD_TIME_INCREMENT",
          "number": 8
        },
        {
          "name": "SORT_FIELD_PLAYER_RESULT",
          "number": 9
        },
        {
          "name": "SORT_FIELD_PLY_COUNT",
          "number": 10
        },
        {
          "name": "SORT_FIELD_GAME_TIME_CLASS",
          "number": 11
        },
        {
          "name": "SORT_FIELD_COLOR",
          "number": 12
        },
        {
          "name": "SORT_FIELD_ARENA_ID",
          "number": 13
        },
        {
          "name": "SORT_FIELD_TOURNAMENT_ID",
          "number": 14
        },
        {
          "name": "SORT_FIELD_TEAM_MATCH_ID",
          "number": 15
        },
        {
          "name": "SORT_FIELD_RATING",
          "number": 16
        },
        {
          "name": "SORT_FIELD_OPPONENT_RATING",
          "number": 17
        },
        {
          "name": "SORT_FIELD_OPPONENT_TITLE",
          "number": 18
        },
        {
          "name": "SORT_FIELD_OPPONENT_USERNAME",
          "number": 19
        },
        {
          "name": "SORT_FIELD_ACCURACY",
          "number": 20
        },
        {
          "name": "SORT_FIELD_OPPONENT_ACCURACY",
          "number": 21
        },
        {
          "name": "SORT_FIELD_GAME_LOCATION",
          "number": 22
        },
        {
          "name": "SORT_FIELD_VS_COMPUTER",
          "number": 23
        },
        {
          "name": "SORT_FIELD_GAME_SOURCE",
          "number": 24
        },
        {
          "name": "SORT_FIELD_FRIEND",
          "number": 25
        },
        {
          "name": "SORT_FIELD_RANDOM_ORDER",
          "number": 26
        },
        {
          "name": "SORT_FIELD_LEGACY_GAME_ID",
          "number": 27
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "GameGatewayService",
      "method": [
        {
          "name": "HydrateGamesByCriteria",
          "input_type": ".chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest",
          "output_type": ".chesscom.game_gateway.v2.HydrateGamesByCriteriaResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "CountGamesByCriteria",
          "input_type": ".chesscom.game_gateway.v2.CountGamesByCriteriaRequest",
          "output_type": ".chesscom.game_gateway.v2.CountGamesByCriteriaResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "DeleteGame",
          "input_type": ".chesscom.game_gateway.v2.DeleteGameRequest",
          "output_type": ".chesscom.game_gateway.v2.DeleteGameResponse",
          "options": {}
        },
        {
          "name": "AggregateGameResultsByPlayerAndCriteria",
          "input_type": ".chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaRequest",
          "output_type": ".chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "HydrateGameByLegacyId",
          "input_type": ".chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest",
          "output_type": ".chesscom.game_gateway.v2.HydrateGameByLegacyIdResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "PlayerOverviewStats",
          "input_type": ".chesscom.game_gateway.v2.PlayerOverviewStatsRequest",
          "output_type": ".chesscom.game_gateway.v2.PlayerOverviewStatsResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "CountTournamentsByPlayer",
          "input_type": ".chesscom.game_gateway.v2.CountTournamentsByPlayerRequest",
          "output_type": ".chesscom.game_gateway.v2.CountTournamentsByPlayerResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "PlayerOverviewAllStats",
          "input_type": ".chesscom.game_gateway.v2.PlayerOverviewAllStatsRequest",
          "output_type": ".chesscom.game_gateway.v2.PlayerOverviewAllStatsResponse",
          "options": {
            "deprecated": true,
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
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17576"></a>
## FND-17576: Full frontend descriptor: chesscom/stats/v1/advanced_stat_percentile.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/stats/v1/advanced_stat_percentile.proto",
  "package": "chesscom.stats.v1",
  "message_type": [
    {
      "name": "AdvancedStatPercentile",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "games_played",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "ewma_12_percentile",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "ewma_50_percentile",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "requested_game_percentile",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_ewma_12_percentile"
        },
        {
          "name": "_ewma_50_percentile"
        },
        {
          "name": "_requested_game_percentile"
        }
      ]
    },
    {
      "name": "AdvancedStatCategoryStats",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "percentile",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "old_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "new_rating",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    },
    {
      "name": "AdvancedStatCategoryGamePerformance",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "percentile",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 166707.

```text
2Vzc2lkEgl4LWFwaS1rZXkSGHgtY2hlYXQtbWV0YWRhdGEtYXBpLWtleRILYmVhcmVyX2F1dGgiAggBKgNk2ARiBnByb3RvMw","chesscom/stats/v1/advanced_stat_percentile.proto":"CjBjaGVzc2NvbS9zdGF0cy92MS9hZHZhbmNlZF9zdGF0X3BlcmNlbnRpbGUucHJvdG8SEWNoZXNzY29tLnN0YXRzLnYxIqACChZBZHZhbmNlZFN0YXRQZXJjZW50aWxlEjEKBHR5cGUYASABKA4yIy5jaGVzc2NvbS5zdGF0cy52MS5BZHZhbmNlZFN0YXRUeXBlEhQKDGdhbWVzX3BsYXllZBgCIAEoDRIfChJld21hXzEyX3BlcmNlbnRpbGUYAyABKAJIAIgBA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17577"></a>
## FND-17577: Full frontend descriptor: chesscom/train/v1/train_challenge_bucket.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_challenge_bucket.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainChallengeBucket",
      "value": [
        {
          "name": "TRAIN_CHALLENGE_BUCKET_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_CHALLENGE_BUCKET_FREE_PIECES",
          "number": 1
        },
        {
          "name": "TRAIN_CHALLENGE_BUCKET_TACTICS",
          "number": 2
        },
        {
          "name": "TRAIN_CHALLENGE_BUCKET_LEADS_TO",
          "number": 3
        },
        {
          "name": "TRAIN_CHALLENGE_BUCKET_BRILLIANT",
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
  Character offset 167621.

```text
jLmNoZXNzY29tLnN0YXRzLnYxLkFkdmFuY2VkU3RhdFR5cGUSEgoKcGVyY2VudGlsZRgCIAEoAjoHgqYdAwoBAWIGcHJvdG8z","chesscom/train/v1/train_challenge_bucket.proto":"Ci5jaGVzc2NvbS90cmFpbi92MS90cmFpbl9jaGFsbGVuZ2VfYnVja2V0LnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSrfAQoUVHJhaW5DaGFsbGVuZ2VCdWNrZXQSJgoiVFJBSU5fQ0hBTExFTkdFX0JVQ0tFVF9VTlNQRUNJRklFRBAAEiYKIlRSQUlOX0NIQUxMRU5HRV9CVUNLRVRfRlJFRV9QSUVDRVMQARIiCh5UUkFJTl9DSEFMTEVOR0VfQlVDS0VUX1RBQ1R
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17578"></a>
## FND-17578: Full frontend descriptor: chesscom/train/v1/train_tactical_theme.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_tactical_theme.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainTacticalTheme",
      "value": [
        {
          "name": "TRAIN_TACTICAL_THEME_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_TACTICAL_THEME_FORK",
          "number": 1
        },
        {
          "name": "TRAIN_TACTICAL_THEME_PIN",
          "number": 2
        },
        {
          "name": "TRAIN_TACTICAL_THEME_DISCOVERY",
          "number": 3
        },
        {
          "name": "TRAIN_TACTICAL_THEME_REMOVES_DEFENDER",
          "number": 4
        },
        {
          "name": "TRAIN_TACTICAL_THEME_TRAPPED_PIECE",
          "number": 5
        },
        {
          "name": "TRAIN_TACTICAL_THEME_SKEWER",
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
  Character offset 168075.

```text
lVDS0VUX0xFQURTX1RPEAMSJAogVFJBSU5fQ0hBTExFTkdFX0JVQ0tFVF9CUklMTElBTlQQBBoIiqYdBAoCAQJiBnByb3RvMw","chesscom/train/v1/train_tactical_theme.proto":"CixjaGVzc2NvbS90cmFpbi92MS90cmFpbl90YWN0aWNhbF90aGVtZS5wcm90bxIRY2hlc3Njb20udHJhaW4udjEqmQIKElRyYWluVGFjdGljYWxUaGVtZRIkCiBUUkFJTl9UQUNUSUNBTF9USEVNRV9VTlNQRUNJRklFRBAAEh0KGVRSQUlOX1RBQ1RJQ0FMX1RIRU1FX0ZPUksQARIcChhUUkFJTl9UQUNUSUNBTF9USEVNRV9QSU4QAhIiCh5UUkFJTl9UQUNUSUNBT
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17579"></a>
## FND-17579: Full frontend descriptor: chesscom/train/v1/train_miss_challenge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_miss_challenge.proto",
  "package": "chesscom.train.v1",
  "message_type": [
    {
      "name": "TrainMissChallenge",
      "field": [
        {
          "name": "bucket",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainChallengeBucket"
        },
        {
          "name": "theme",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainTacticalTheme",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "correct_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "is_critical",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_theme"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 168601.

```text
fVEhFTUVfVFJBUFBFRF9QSUVDRRAFEh8KG1RSQUlOX1RBQ1RJQ0FMX1RIRU1FX1NLRVdFUhAGGgiKph0ECgIBAmIGcHJvdG8z","chesscom/train/v1/train_miss_challenge.proto":"CixjaGVzc2NvbS90cmFpbi92MS90cmFpbl9taXNzX2NoYWxsZW5nZS5wcm90bxIRY2hlc3Njb20udHJhaW4udjEi4AEKElRyYWluTWlzc0NoYWxsZW5nZRI3CgZidWNrZXQYASABKA4yJy5jaGVzc2NvbS50cmFpbi52MS5UcmFpbkNoYWxsZW5nZUJ1Y2tldBI5CgV0aGVtZRgCIAEoDjIlLmNoZXNzY29tLnRyYWluLnYxLlRyYWluVGFjdGljYWxUaGVtZUgAiAEBE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17580"></a>
## FND-17580: Full frontend descriptor: chesscom/train/v1/train_blunder_challenge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_blunder_challenge.proto",
  "package": "chesscom.train.v1",
  "message_type": [
    {
      "name": "TrainBlunderChallenge",
      "field": [
        {
          "name": "bucket",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainChallengeBucket"
        },
        {
          "name": "theme",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainTacticalTheme",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "correct_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_theme"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 169051.

```text
XLmNoZXNzY29tLmNoZXNzLnYxLk1vdmUSEwoLaXNfY3JpdGljYWwYBCABKAg6CIKmHQQKAgECQggKBl90aGVtZWIGcHJvdG8z","chesscom/train/v1/train_blunder_challenge.proto":"Ci9jaGVzc2NvbS90cmFpbi92MS90cmFpbl9ibHVuZGVyX2NoYWxsZW5nZS5wcm90bxIRY2hlc3Njb20udHJhaW4udjEizgEKFVRyYWluQmx1bmRlckNoYWxsZW5nZRI3CgZidWNrZXQYASABKA4yJy5jaGVzc2NvbS50cmFpbi52MS5UcmFpbkNoYWxsZW5nZUJ1Y2tldBI5CgV0aGVtZRgCIAEoDjIlLmNoZXNzY29tLnRyYWluLnYxLlRyYWluVGFjdGljYWxUaG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17581"></a>
## FND-17581: Full frontend descriptor: chesscom/train/v1/train_opening_theme.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_opening_theme.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainOpeningTheme",
      "value": [
        {
          "name": "TRAIN_OPENING_THEME_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT",
          "number": 1
        },
        {
          "name": "TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING",
          "number": 2
        },
        {
          "name": "TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK",
          "number": 3
        },
        {
          "name": "TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS",
          "number": 4
        },
        {
          "name": "TRAIN_OPENING_THEME_NEVER_PLAY_F3",
          "number": 5
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS",
          "number": 6
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING",
          "number": 7
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER",
          "number": 8
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE",
          "number": 9
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO",
          "number": 10
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE",
          "number": 11
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK",
          "number": 12
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT",
          "number": 13
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE",
          "number": 14
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE",
          "number": 15
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_FIANCHETTO",
          "number": 16
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_KINGSIDE",
          "number": 17
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_QUEENSIDE",
          "number": 18
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_CASTLES_KING_SIDE",
          "number": 19
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_CASTLES_QUEEN_SIDE",
          "number": 20
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_CASTLES_SAME_SIDE",
          "number": 21
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_CASTLES_OPPOSITE_SIDE",
          "number": 22
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_PREVENTS_CASTLING",
          "number": 23
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_FIRST_MOVE_CENTER_PAWN",
          "number": 24
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_PUTS_PAWN_IN_CENTER",
          "number": 25
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_WINS_TEMPO",
          "number": 26
        },
        {
          "name": "TRAIN_OPENING_THEME_MISSES_CONNECTS_ROOKS",
          "number": 27
        },
        {
          "name": "TRAIN_OPENING_THEME_MOVES_PAWN_IN_FRONT_OF_KING",
          "number": 28
        },
        {
          "name": "TRAIN_OPENING_THEME_DOUBLES_CASTLE_PAWNS",
          "number": 29
        },
        {
          "name": "TRAIN_OPENING_THEME_BLOCKS_CENTRAL_PAWN",
          "number": 30
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 169484.

```text
KDGNvcnJlY3RfbW92ZRgDIAEoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmU6CIKmHQQKAgECQggKBl90aGVtZWIGcHJvdG8z","chesscom/train/v1/train_opening_theme.proto":"CitjaGVzc2NvbS90cmFpbi92MS90cmFpbl9vcGVuaW5nX3RoZW1lLnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSqmDAoRVHJhaW5PcGVuaW5nVGhlbWUSIwofVFJBSU5fT1BFTklOR19USEVNRV9VTlNQRUNJRklFRBAAEjMKL1RSQUlOX09QRU5JTkdfVEhFTUVfVE9PX0VBUkxZX1FVRUVOX0RFVkVMT1BNRU5UEAESMwovVFJBSU5fT1BFTklOR19USEVNRV9NT1ZFU1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17582"></a>
## FND-17582: Full frontend descriptor: chesscom/train/v1/train_opening_mistake_challenge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_opening_mistake_challenge.proto",
  "package": "chesscom.train.v1",
  "message_type": [
    {
      "name": "TrainOpeningMistakeChallenge",
      "field": [
        {
          "name": "eco_family_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "theme",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainOpeningTheme"
        },
        {
          "name": "correct_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 171732.

```text
xFX1BBV05TEB0SKwonVFJBSU5fT1BFTklOR19USEVNRV9CTE9DS1NfQ0VOVFJBTF9QQVdOEB4aCIqmHQQKAgECYgZwcm90bzM","chesscom/train/v1/train_opening_mistake_challenge.proto":"CjdjaGVzc2NvbS90cmFpbi92MS90cmFpbl9vcGVuaW5nX21pc3Rha2VfY2hhbGxlbmdlLnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSKjAQocVHJhaW5PcGVuaW5nTWlzdGFrZUNoYWxsZW5nZRIVCg1lY29fZmFtaWx5X2lkGAEgASgFEjMKBXRoZW1lGAIgASgOMiQuY2hlc3Njb20udHJhaW4udjEuVHJhaW5PcGVuaW5nVGhlbWUSLQoMY29ycmVjdF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17583"></a>
## FND-17583: Full frontend descriptor: chesscom/train/v1/train_position_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_position_type.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainPositionType",
      "value": [
        {
          "name": "TRAIN_POSITION_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_POSITION_TYPE_OPEN",
          "number": 1
        },
        {
          "name": "TRAIN_POSITION_TYPE_SEMI_OPEN",
          "number": 2
        },
        {
          "name": "TRAIN_POSITION_TYPE_CLOSED",
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
  Character offset 172127.

```text
W5nVGhlbWUSLQoMY29ycmVjdF9tb3ZlGAMgASgLMhcuY2hlc3Njb20uY2hlc3MudjEuTW92ZToIgqYdBAoCAQJiBnByb3RvMw","chesscom/train/v1/train_position_type.proto":"CitjaGVzc2NvbS90cmFpbi92MS90cmFpbl9wb3NpdGlvbl90eXBlLnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSqjAQoRVHJhaW5Qb3NpdGlvblR5cGUSIwofVFJBSU5fUE9TSVRJT05fVFlQRV9VTlNQRUNJRklFRBAAEhwKGFRSQUlOX1BPU0lUSU9OX1RZUEVfT1BFThABEiEKHVRSQUlOX1BPU0lUSU9OX1RZUEVfU0VNSV9PUEVOEAISHgoaVFJBSU5fUE9TSVRJT0
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17584"></a>
## FND-17584: Full frontend descriptor: chesscom/train/v1/train_position_attribute.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_position_attribute.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainPositionAttribute",
      "value": [
        {
          "name": "TRAIN_POSITION_ATTRIBUTE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_POSITION_ATTRIBUTE_ATTACKING",
          "number": 1
        },
        {
          "name": "TRAIN_POSITION_ATTRIBUTE_DEFENDING",
          "number": 2
        },
        {
          "name": "TRAIN_POSITION_ATTRIBUTE_ACTIVE_PIECE_ADVANTAGE",
          "number": 3
        },
        {
          "name": "TRAIN_POSITION_ATTRIBUTE_SPACE_ADVANTAGE",
          "number": 4
        },
        {
          "name": "TRAIN_POSITION_ATTRIBUTE_PAWN_STRUCTURE_ADVANTAGE",
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
  Character offset 172494.

```text
0lUSU9OX1RZUEVfU0VNSV9PUEVOEAISHgoaVFJBSU5fUE9TSVRJT05fVFlQRV9DTE9TRUQQAxoIiqYdBAoCAQJiBnByb3RvMw","chesscom/train/v1/train_position_attribute.proto":"CjBjaGVzc2NvbS90cmFpbi92MS90cmFpbl9wb3NpdGlvbl9hdHRyaWJ1dGUucHJvdG8SEWNoZXNzY29tLnRyYWluLnYxKrYCChZUcmFpblBvc2l0aW9uQXR0cmlidXRlEigKJFRSQUlOX1BPU0lUSU9OX0FUVFJJQlVURV9VTlNQRUNJRklFRBAAEiYKIlRSQUlOX1BPU0lUSU9OX0FUVFJJQlVURV9BVFRBQ0tJTkcQARImCiJUUkFJTl9QT1NJVElPTl9BVFRSS
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17585"></a>
## FND-17585: Full frontend descriptor: chesscom/train/v1/train_strategy_theme.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_strategy_theme.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainStrategyTheme",
      "value": [
        {
          "name": "TRAIN_STRATEGY_THEME_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_STRATEGY_THEME_CREATES_BACKWARD_PAWN",
          "number": 1
        },
        {
          "name": "TRAIN_STRATEGY_THEME_ISOLATES_PAWN",
          "number": 2
        },
        {
          "name": "TRAIN_STRATEGY_THEME_ISOLATES_PAWN_ON_SEMI_OPEN_FILE",
          "number": 3
        },
        {
          "name": "TRAIN_STRATEGY_THEME_DOUBLES_PAWNS",
          "number": 4
        },
        {
          "name": "TRAIN_STRATEGY_THEME_DOUBLES_CASTLE_PAWNS",
          "number": 5
        },
        {
          "name": "TRAIN_STRATEGY_THEME_DOUBLED_ISOLATED_PAWN",
          "number": 6
        },
        {
          "name": "TRAIN_STRATEGY_THEME_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE",
          "number": 7
        },
        {
          "name": "TRAIN_STRATEGY_THEME_DOUBLED_BACKWARD_PAWN",
          "number": 8
        },
        {
          "name": "TRAIN_STRATEGY_THEME_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE",
          "number": 9
        },
        {
          "name": "TRAIN_STRATEGY_THEME_BACKWARD_PAWN_ON_SEMI_OPEN_FILE",
          "number": 10
        },
        {
          "name": "TRAIN_STRATEGY_THEME_CREATES_OPPONENT_PROTECTED_PASSED_PAWN",
          "number": 11
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MOVES_PAWN_IN_FRONT_OF_KING",
          "number": 12
        },
        {
          "name": "TRAIN_STRATEGY_THEME_CASTLES_INTO_ATTACK",
          "number": 13
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MOVES_TO_PASSIVE_SQUARE",
          "number": 14
        },
        {
          "name": "TRAIN_STRATEGY_THEME_ROOK_PASSIVE_PROTECTION",
          "number": 15
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_TAKES_OUTPOST",
          "number": 16
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ROOK_TAKES_OUTPOST",
          "number": 17
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_TAKES_OUTPOST_WITH_TEMPO",
          "number": 18
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CENTRALIZES_KNIGHT",
          "number": 19
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_BISHOP_GAINS_SCOPE",
          "number": 20
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CONNECTS_ROOKS",
          "number": 21
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CONNECTS_ROOKS_7TH",
          "number": 22
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_DOUBLES_ROOKS",
          "number": 23
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ROOK_LIFT",
          "number": 24
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PREPARES_TO_DOUBLE_ROOKS",
          "number": 25
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_TAKES_OPEN_FILE",
          "number": 26
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CHALLENGES_OPEN_FILE",
          "number": 27
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ROOK_BEHIND_OWN_PAWN",
          "number": 28
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ROOK_BEHIND_OPP_PAWN",
          "number": 29
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_MANEUVERS_TO_ACTIVE_SQUARE",
          "number": 30
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_MOVES_TO_ACTIVE_SQUARE",
          "number": 31
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PILLSBURY_KNIGHT",
          "number": 32
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CARLSBAD_KNIGHT",
          "number": 33
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_GAINS_CENTRAL_SPACE",
          "number": 34
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_GAINS_KINGSIDE_SPACE",
          "number": 35
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_GAINS_QUEENSIDE_SPACE",
          "number": 36
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_STRIKES_AT_CENTER",
          "number": 37
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CENTRAL_BREAK",
          "number": 38
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PREPARES_CENTRAL_PUSH",
          "number": 39
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PUTS_PAWN_IN_CENTER",
          "number": 40
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PREVENTS_CENTRAL_BREAK",
          "number": 41
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK",
          "number": 42
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CURES_BACKWARD_PAWN",
          "number": 43
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CURES_ISOLATED_PAWN",
          "number": 44
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_FIXES_PAWN_STRUCTURE",
          "number": 45
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_UNDOUBLES_PAWNS",
          "number": 46
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_UNTRIPLES_PAWNS",
          "number": 47
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CREATES_PAWN_CHAIN",
          "number": 48
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_SUPPORTS_PAWN_CHAIN",
          "number": 49
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_MAKES_PASSED_PAWN",
          "number": 50
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CREATES_LUFT",
          "number": 51
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PREVENTS_CASTLING",
          "number": 52
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ATTACKS_PAWN_CHAIN",
          "number": 53
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ATTACKS_PAWN_CHAIN_COVER",
          "number": 54
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_EDGE_PAWN_CHASES_KNIGHT",
          "number": 55
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_BLOCKADE",
          "number": 56
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_BLOCKADE_MOVING_PAWN",
          "number": 57
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_BLOCKADES_OPP_PUSHING_SQUARE",
          "number": 58
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_BLOCKADES_OPP_PROMOTION_SQUARE",
          "number": 59
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_CONTROLS_OPP_PUSHING_SQUARE",
          "number": 60
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_ELIMINATES_OPP_PASSED_PAWN",
          "number": 61
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PROTECTS_PASSED_PAWN",
          "number": 62
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_VACATES_PUSHING_SQUARE",
          "number": 63
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_PUSHES_PASSED_PAWN_MIDDLEGAME",
          "number": 64
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_TRADE_TO_SIMPLIFY",
          "number": 65
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_AVOIDS_TRADE",
          "number": 66
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MISSES_GOOD_TRADE",
          "number": 67
        },
        {
          "name": "TRAIN_STRATEGY_THEME_BAD_TRADE",
          "number": 68
        },
        {
          "name": "TRAIN_STRATEGY_THEME_INFERIOR_TRADE",
          "number": 69
        },
        {
          "name": "TRAIN_STRATEGY_THEME_BAD_TRADE_KNIGHT_FOR_BISHOP",
          "number": 70
        },
        {
          "name": "TRAIN_STRATEGY_THEME_BAD_TRADE_BISHOP_FOR_KNIGHT",
          "number": 71
        },
        {
          "name": "TRAIN_STRATEGY_THEME_QUEEN_FOR_TWO_ROOKS",
          "number": 72
        },
        {
          "name": "TRAIN_STRATEGY_THEME_QUEEN_FOR_ROOK_MINOR",
          "number": 73
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MINORS_FOR_ROOK_PAWN",
          "number": 74
        },
        {
          "name": "TRAIN_STRATEGY_THEME_LOSES_CASTLING_RIGHTS",
          "number": 75
        },
        {
          "name": "TRAIN_STRATEGY_THEME_MIDDLEGAME_START_NO_CASTLE",
          "number": 76
        },
        {
          "name": "TRAIN_STRATEGY_THEME_PASSIVE_RETREAT",
          "number": 77
        },
        {
          "name": "TRAIN_STRATEGY_THEME_BLOCKS_CENTRAL_PAWN",
          "number": 78
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 173068.

```text
SNQoxVFJBSU5fUE9TSVRJT05fQVRUUklCVVRFX1BBV05fU1RSVUNUVVJFX0FEVkFOVEFHRRAFGgiKph0ECgIBAmIGcHJvdG8z","chesscom/train/v1/train_strategy_theme.proto":"CixjaGVzc2NvbS90cmFpbi92MS90cmFpbl9zdHJhdGVneV90aGVtZS5wcm90bxIRY2hlc3Njb20udHJhaW4udjEqmSAKElRyYWluU3RyYXRlZ3lUaGVtZRIkCiBUUkFJTl9TVFJBVEVHWV9USEVNRV9VTlNQRUNJRklFRBAAEi4KKlRSQUlOX1NUUkFURUdZX1RIRU1FX0NSRUFURVNfQkFDS1dBUkRfUEFXThABEiYKIlRSQUlOX1NUUkFURUdZX1RIRU1FX0lTT0xBV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17586"></a>
## FND-17586: Full frontend descriptor: chesscom/train/v1/train_strategy_mistake_challenge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_strategy_mistake_challenge.proto",
  "package": "chesscom.train.v1",
  "message_type": [
    {
      "name": "TrainStrategyMistakeChallenge",
      "field": [
        {
          "name": "position_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainPositionType"
        },
        {
          "name": "position_attribute",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainPositionAttribute"
        },
        {
          "name": "theme",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainStrategyTheme"
        },
        {
          "name": "correct_move",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 178714.

```text
SRVRSRUFUEE0SLAooVFJBSU5fU1RSQVRFR1lfVEhFTUVfQkxPQ0tTX0NFTlRSQUxfUEFXThBOGgiKph0ECgIBAmIGcHJvdG8z","chesscom/train/v1/train_strategy_mistake_challenge.proto":"CjhjaGVzc2NvbS90cmFpbi92MS90cmFpbl9zdHJhdGVneV9taXN0YWtlX2NoYWxsZW5nZS5wcm90bxIRY2hlc3Njb20udHJhaW4udjEikgIKHVRyYWluU3RyYXRlZ3lNaXN0YWtlQ2hhbGxlbmdlEjsKDXBvc2l0aW9uX3R5cGUYASABKA4yJC5jaGVzc2NvbS50cmFpbi52MS5UcmFpblBvc2l0aW9uVHlwZRJFChJwb3NpdGlvbl9hdHRyaWJ1dGUYA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17587"></a>
## FND-17587: Full frontend descriptor: chesscom/train/v1/train_endgame_theme.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_endgame_theme.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainEndgameTheme",
      "value": [
        {
          "name": "TRAIN_ENDGAME_THEME_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_ENDGAME_THEME_QUEEN",
          "number": 1
        },
        {
          "name": "TRAIN_ENDGAME_THEME_ROOK_AND_PAWN",
          "number": 2
        },
        {
          "name": "TRAIN_ENDGAME_THEME_KING_AND_PAWN",
          "number": 3
        },
        {
          "name": "TRAIN_ENDGAME_THEME_OTHER",
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
  Character offset 179259.

```text
VneVRoZW1lEi0KDGNvcnJlY3RfbW92ZRgEIAEoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmU6CIKmHQQKAgECYgZwcm90bzM","chesscom/train/v1/train_endgame_theme.proto":"CitjaGVzc2NvbS90cmFpbi92MS90cmFpbl9lbmRnYW1lX3RoZW1lLnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSrOAQoRVHJhaW5FbmRnYW1lVGhlbWUSIwofVFJBSU5fRU5ER0FNRV9USEVNRV9VTlNQRUNJRklFRBAAEh0KGVRSQUlOX0VOREdBTUVfVEhFTUVfUVVFRU4QARIlCiFUUkFJTl9FTkRHQU1FX1RIRU1FX1JPT0tfQU5EX1BBV04QAhIlCiFUUkFJTl9FTk
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17588"></a>
## FND-17588: Full frontend descriptor: chesscom/train/v1/train_endgame_mistake_challenge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_endgame_mistake_challenge.proto",
  "package": "chesscom.train.v1",
  "message_type": [
    {
      "name": "TrainEndgameMistakeChallenge",
      "field": [
        {
          "name": "theme",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainEndgameTheme"
        },
        {
          "name": "correct_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 179683.

```text
1FX1RIRU1FX0tJTkdfQU5EX1BBV04QAxIdChlUUkFJTl9FTkRHQU1FX1RIRU1FX09USEVSEAQaCIqmHQQKAgECYgZwcm90bzM","chesscom/train/v1/train_endgame_mistake_challenge.proto":"CjdjaGVzc2NvbS90cmFpbi92MS90cmFpbl9lbmRnYW1lX21pc3Rha2VfY2hhbGxlbmdlLnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSKMAQocVHJhaW5FbmRnYW1lTWlzdGFrZUNoYWxsZW5nZRIzCgV0aGVtZRgBIAEoDjIkLmNoZXNzY29tLnRyYWluLnYxLlRyYWluRW5kZ2FtZVRoZW1lEi0KDGNvcnJlY3RfbW92ZRgCIAEoCzIXLmNoZXNzY29tLm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17589"></a>
## FND-17589: Full frontend descriptor: chesscom/train/v1/train_challenge.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_challenge.proto",
  "package": "chesscom.train.v1",
  "message_type": [
    {
      "name": "TrainChallenge",
      "field": [
        {
          "name": "miss",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.train.v1.TrainMissChallenge",
          "oneof_index": 0
        },
        {
          "name": "blunder",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.train.v1.TrainBlunderChallenge",
          "oneof_index": 0
        },
        {
          "name": "opening_mistake",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.train.v1.TrainOpeningMistakeChallenge",
          "oneof_index": 0
        },
        {
          "name": "strategy_mistake",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.train.v1.TrainStrategyMistakeChallenge",
          "oneof_index": 0
        },
        {
          "name": "endgame_mistake",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.train.v1.TrainEndgameMistakeChallenge",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "challenge"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 180047.

```text
FtZVRoZW1lEi0KDGNvcnJlY3RfbW92ZRgCIAEoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmU6CIKmHQQKAgECYgZwcm90bzM","chesscom/train/v1/train_challenge.proto":"CidjaGVzc2NvbS90cmFpbi92MS90cmFpbl9jaGFsbGVuZ2UucHJvdG8SEWNoZXNzY29tLnRyYWluLnYxIoEDCg5UcmFpbkNoYWxsZW5nZRI1CgRtaXNzGAEgASgLMiUuY2hlc3Njb20udHJhaW4udjEuVHJhaW5NaXNzQ2hhbGxlbmdlSAASOwoHYmx1bmRlchgCIAEoCzIoLmNoZXNzY29tLnRyYWluLnYxLlRyYWluQmx1bmRlckNoYWxsZW5nZUgAEkoKD29wZW5pbmdfbW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17590"></a>
## FND-17590: Full frontend descriptor: chesscom/train/v1/train_item_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_item_type.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainItemType",
      "value": [
        {
          "name": "TRAIN_ITEM_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_ITEM_TYPE_RETRY_MISS",
          "number": 1
        },
        {
          "name": "TRAIN_ITEM_TYPE_RETRY_BLUNDER",
          "number": 2
        },
        {
          "name": "TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE",
          "number": 3
        },
        {
          "name": "TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE",
          "number": 4
        },
        {
          "name": "TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE",
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
  Character offset 180700.

```text
vbS50cmFpbi52MS5UcmFpbkVuZGdhbWVNaXN0YWtlQ2hhbGxlbmdlSAA6CIKmHQQKAgECQgsKCWNoYWxsZW5nZWIGcHJvdG8z","chesscom/train/v1/train_item_type.proto":"CidjaGVzc2NvbS90cmFpbi92MS90cmFpbl9pdGVtX3R5cGUucHJvdG8SEWNoZXNzY29tLnRyYWluLnYxKv8BCg1UcmFpbkl0ZW1UeXBlEh8KG1RSQUlOX0lURU1fVFlQRV9VTlNQRUNJRklFRBAAEh4KGlRSQUlOX0lURU1fVFlQRV9SRVRSWV9NSVNTEAESIQodVFJBSU5fSVRFTV9UWVBFX1JFVFJZX0JMVU5ERVIQAhIpCiVUUkFJTl9JVEVNX1RZUEVfUkVUUllfT1BFTk
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17591"></a>
## FND-17591: Full frontend descriptor: chesscom/train/v1/train_backfill_status.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_backfill_status.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainBackfillStatus",
      "value": [
        {
          "name": "TRAIN_BACKFILL_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_BACKFILL_STATUS_IN_PROGRESS",
          "number": 1
        },
        {
          "name": "TRAIN_BACKFILL_STATUS_COMPLETED",
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
  Character offset 181180.

```text
dZX01JU1RBS0UQBBIpCiVUUkFJTl9JVEVNX1RZUEVfUkVUUllfRU5ER0FNRV9NSVNUQUtFEAUaCIqmHQQKAgECYgZwcm90bzM","chesscom/train/v1/train_backfill_status.proto":"Ci1jaGVzc2NvbS90cmFpbi92MS90cmFpbl9iYWNrZmlsbF9zdGF0dXMucHJvdG8SEWNoZXNzY29tLnRyYWluLnYxKpIBChNUcmFpbkJhY2tmaWxsU3RhdHVzEiUKIVRSQUlOX0JBQ0tGSUxMX1NUQVRVU19VTlNQRUNJRklFRBAAEiUKIVRSQUlOX0JBQ0tGSUxMX1NUQVRVU19JTl9QUk9HUkVTUxABEiMKH1RSQUlOX0JBQ0tGSUxMX1NUQVRVU19DT01QTEVURUQQ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17592"></a>
## FND-17592: Full frontend descriptor: chesscom/train/v1/train_membership_context.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_membership_context.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainMembershipContext",
      "value": [
        {
          "name": "TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_MEMBERSHIP_CONTEXT_PRO",
          "number": 1
        },
        {
          "name": "TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW",
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
  Character offset 181529.

```text
VRVU19JTl9QUk9HUkVTUxABEiMKH1RSQUlOX0JBQ0tGSUxMX1NUQVRVU19DT01QTEVURUQQAhoIiqYdBAoCAQJiBnByb3RvMw","chesscom/train/v1/train_membership_context.proto":"CjBjaGVzc2NvbS90cmFpbi92MS90cmFpbl9tZW1iZXJzaGlwX2NvbnRleHQucHJvdG8SEWNoZXNzY29tLnRyYWluLnYxKpUBChZUcmFpbk1lbWJlcnNoaXBDb250ZXh0EigKJFRSQUlOX01FTUJFUlNISVBfQ09OVEVYVF9VTlNQRUNJRklFRBAAEiAKHFRSQUlOX01FTUJFUlNISVBfQ09OVEVYVF9QUk8QARIlCiFUUkFJTl9NRU1CRVJTSElQX0NPTlRFWFRfR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17593"></a>
## FND-17593: Full frontend descriptor: chesscom/train/v1/train_outcome.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/train/v1/train_outcome.proto",
  "package": "chesscom.train.v1",
  "enum_type": [
    {
      "name": "TrainOutcome",
      "value": [
        {
          "name": "TRAIN_OUTCOME_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TRAIN_OUTCOME_CORRECT",
          "number": 1
        },
        {
          "name": "TRAIN_OUTCOME_INCORRECT",
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
  Character offset 181889.

```text
VBfQ09OVEVYVF9QUk8QARIlCiFUUkFJTl9NRU1CRVJTSElQX0NPTlRFWFRfRlJFRVZJRVcQAhoIiqYdBAoCAQJiBnByb3RvMw","chesscom/train/v1/train_outcome.proto":"CiVjaGVzc2NvbS90cmFpbi92MS90cmFpbl9vdXRjb21lLnByb3RvEhFjaGVzc2NvbS50cmFpbi52MSpvCgxUcmFpbk91dGNvbWUSHQoZVFJBSU5fT1VUQ09NRV9VTlNQRUNJRklFRBAAEhkKFVRSQUlOX09VVENPTUVfQ09SUkVDVBABEhsKF1RSQUlOX09VVENPTUVfSU5DT1JSRUNUEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/explanation_engine/v1/takeawa
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17594"></a>
## FND-17594: Full frontend descriptor: chesscom/explanation_engine/v1/takeaways.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/takeaways.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "Takeaway",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "classification",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.TakeawayClassification"
        },
        {
          "name": "speech",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "example",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.stats.v1.AdvancedStatExample",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "performance",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.TakeawayPerformance"
        },
        {
          "name": "train_speech",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "train_item_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.train.v1.TrainItemType",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_example"
        },
        {
          "name": "_train_speech"
        },
        {
          "name": "_train_item_type"
        }
      ]
    },
    {
      "name": "Takeaways",
      "field": [
        {
          "name": "takeaways",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Takeaway"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "TakeawayClassification",
      "value": [
        {
          "name": "TAKEAWAY_CLASSIFICATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH",
          "number": 1
        },
        {
          "name": "TAKEAWAY_CLASSIFICATION_BE_AWARE",
          "number": 2
        },
        {
          "name": "TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS",
          "number": 3
        },
        {
          "name": "TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "TakeawayPerformance",
      "value": [
        {
          "name": "TAKEAWAY_PERFORMANCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TAKEAWAY_PERFORMANCE_GOOD",
          "number": 1
        },
        {
          "name": "TAKEAWAY_PERFORMANCE_BAD",
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
  Character offset 182171.

```text
kKFVRSQUlOX09VVENPTUVfQ09SUkVDVBABEhsKF1RSQUlOX09VVENPTUVfSU5DT1JSRUNUEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/explanation_engine/v1/takeaways.proto":"Ci5jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvdGFrZWF3YXlzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEivgMKCFRha2Vhd2F5EjUKCGNhdGVnb3J5GAEgASgOMiMuY2hlc3Njb20uc3RhdHMudjEuQWR2YW5jZWRTdGF0VHlwZRJOCg5jbGFzc2lmaWNhdGlvbhgCIAEoDjI2LmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS5
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17595"></a>
## FND-17595: Full frontend descriptor: chesscom/explanation_engine/v1/skills.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/skills.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SkillsPosition",
      "field": [
        {
          "name": "ply",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "skills",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Skill"
        },
        {
          "name": "validation_hash",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "Skill",
      "value": [
        {
          "name": "SKILL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILL_CAPTURE",
          "number": 1
        },
        {
          "name": "SKILL_CHECK",
          "number": 2
        },
        {
          "name": "SKILL_CASTLE",
          "number": 3
        },
        {
          "name": "SKILL_CHECKMATE",
          "number": 4
        },
        {
          "name": "SKILL_FREE_PIECE",
          "number": 5
        },
        {
          "name": "SKILL_DEFEND_PIECE",
          "number": 6
        },
        {
          "name": "SKILL_RETREAT",
          "number": 7
        },
        {
          "name": "SKILL_DEVELOPS_PIECE",
          "number": 8
        },
        {
          "name": "SKILL_PAWNS_IN_CENTER",
          "number": 9
        },
        {
          "name": "SKILL_STRIKES_AT_CENTER",
          "number": 10
        },
        {
          "name": "SKILL_CONNECT_ROOKS",
          "number": 11
        },
        {
          "name": "SKILL_COMPLETE_DEVELOPMENT",
          "number": 12
        },
        {
          "name": "SKILL_ONE_BOOK_MOVE",
          "number": 13
        },
        {
          "name": "SKILL_TWO_BOOK_MOVES",
          "number": 14
        },
        {
          "name": "SKILL_THREE_BOOK_MOVES",
          "number": 15
        },
        {
          "name": "SKILL_FOUR_BOOK_MOVES",
          "number": 16
        },
        {
          "name": "SKILL_FIANCHETTO",
          "number": 17
        },
        {
          "name": "SKILL_RECAPTURE",
          "number": 18
        },
        {
          "name": "SKILL_WINNING_CAPTURE",
          "number": 19
        },
        {
          "name": "SKILL_BLOCKS_ATTACK",
          "number": 20
        },
        {
          "name": "SKILL_FORK",
          "number": 21
        },
        {
          "name": "SKILL_PIN",
          "number": 22
        },
        {
          "name": "SKILL_DEFEND_CHECKMATE",
          "number": 23
        },
        {
          "name": "SKILL_ABSOLUTE_PIN",
          "number": 24
        },
        {
          "name": "SKILL_DISCOVERED_ATTACK",
          "number": 25
        },
        {
          "name": "SKILL_KNIGHT_FORK",
          "number": 26
        },
        {
          "name": "SKILL_SKEWER",
          "number": 27
        },
        {
          "name": "SKILL_ATTACKING_PINNED_PIECE",
          "number": 28
        },
        {
          "name": "SKILL_TRAPPED_PIECE",
          "number": 29
        },
        {
          "name": "SKILL_REMOVES_DEFENDER",
          "number": 30
        },
        {
          "name": "SKILL_ROYAL_FORK",
          "number": 31
        },
        {
          "name": "SKILL_DISCOVERED_CHECK",
          "number": 32
        },
        {
          "name": "SKILL_COUNTER_THREAT",
          "number": 33
        },
        {
          "name": "SKILL_DEFEND_TACTIC",
          "number": 34
        },
        {
          "name": "SKILL_EXPLOITS_PIN",
          "number": 35
        },
        {
          "name": "SKILL_DOUBLE_CHECK",
          "number": 36
        },
        {
          "name": "SKILL_BRILLIANT_SACRIFICE",
          "number": 37
        },
        {
          "name": "SKILL_QUEEN_SACRIFICE",
          "number": 38
        },
        {
          "name": "SKILL_EQUAL_TRADE",
          "number": 39
        },
        {
          "name": "SKILL_POWERFUL_BISHOP",
          "number": 40
        },
        {
          "name": "SKILL_ROOK_TO_OPEN_FILE",
          "number": 41
        },
        {
          "name": "SKILL_KICK",
          "number": 42
        },
        {
          "name": "SKILL_OUTPOST",
          "number": 43
        },
        {
          "name": "SKILL_TRADING_TO_SIMPLIFY",
          "number": 44
        },
        {
          "name": "SKILL_DOUBLE_ROOKS",
          "number": 45
        },
        {
          "name": "SKILL_CREATES_BATTERY",
          "number": 46
        },
        {
          "name": "SKILL_PREVENT_CASTLING",
          "number": 47
        },
        {
          "name": "SKILL_WINS_TEMPO",
          "number": 48
        },
        {
          "name": "SKILL_AVOIDS_TRADE",
          "number": 49
        },
        {
          "name": "SKILL_DEVELOP_WITH_TEMPO",
          "number": 50
        },
        {
          "name": "SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE",
          "number": 51
        },
        {
          "name": "SKILL_EN_PASSANT",
          "number": 52
        },
        {
          "name": "SKILL_IMPROVES_PAWN_STRUCTURE",
          "number": 53
        },
        {
          "name": "SKILL_PAWN_STORM",
          "number": 54
        },
        {
          "name": "SKILL_PROMOTION",
          "number": 55
        },
        {
          "name": "SKILL_LADDER_MATE",
          "number": 56
        },
        {
          "name": "SKILL_BACKRANK_MATE",
          "number": 57
        },
        {
          "name": "SKILL_PUSHES_PASSED_PAWN",
          "number": 58
        },
        {
          "name": "SKILL_QUEEN_CHECKMATE",
          "number": 59
        },
        {
          "name": "SKILL_ROOK_CHECKMATE",
          "number": 60
        },
        {
          "name": "SKILL_MAKES_PASSED_PAWN",
          "number": 61
        },
        {
          "name": "SKILL_ACTIVATE_KING",
          "number": 62
        },
        {
          "name": "SKILL_ROOK_TO_SEVENTH",
          "number": 63
        },
        {
          "name": "SKILL_ROOK_BEHIND_OWN_PASSED_PAWN",
          "number": 64
        },
        {
          "name": "SKILL_OPPOSITION",
          "number": 65
        },
        {
          "name": "SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH",
          "number": 66
        },
        {
          "name": "SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN",
          "number": 67
        },
        {
          "name": "SKILL_MAKES_PROTECTED_PASSED_PAWN",
          "number": 68
        },
        {
          "name": "SKILL_KING_AND_PAWN_ENDGAMES",
          "number": 69
        },
        {
          "name": "SKILL_QUEEN_ENDGAMES",
          "number": 70
        },
        {
          "name": "SKILL_ROOK_ENDGAMES",
          "number": 71
        },
        {
          "name": "SKILL_KNIGHT_AND_BISHOP_ENDGAMES",
          "number": 72
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 183569.

```text
UtFQVdBWV9QRVJGT1JNQU5DRV9HT09EEAESHAoYVEFLRUFXQVlfUEVSRk9STUFOQ0VfQkFEEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/skills.proto":"CitjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc2tpbGxzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEidgoOU2tpbGxzUG9zaXRpb24SCwoDcGx5GAEgASgFEjUKBnNraWxscxgCIAMoDjIlLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbBIXCg92YWxpZGF0aW9uX2hhc2gYAyABKAk6B4KmHQMKAQEqiA8KBVNraW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17596"></a>
## FND-17596: Full frontend descriptor: chesscom/explanation_engine/v1/game_review.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_review.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GameReview",
      "field": [
        {
          "name": "eval_graph",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalGraph"
        },
        {
          "name": "highlights",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Highlights"
        },
        {
          "name": "review",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Review"
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameResult"
        },
        {
          "name": "metadata",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Metadata"
        },
        {
          "name": "opening",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Opening"
        }
      ],
      "options": {}
    },
    {
      "name": "Metadata",
      "field": [
        {
          "name": "cee_version",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.SemanticVersion"
        },
        {
          "name": "annotated_pgn",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "EvalGraph",
      "field": [
        {
          "name": "eval_graph_ticks",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalGraphTick"
        }
      ],
      "options": {}
    },
    {
      "name": "EvalGraphTick",
      "field": [
        {
          "name": "move_classification",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "move_score",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Score"
        },
        {
          "name": "is_key_moment",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "Highlights",
      "field": [
        {
          "name": "game_summary",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "accuracy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Accuracy"
        },
        {
          "name": "classification_tallies",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ClassificationTallies"
        },
        {
          "name": "report_card",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReviewReportCard"
        },
        {
          "name": "takeaways",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Takeaways"
        },
        {
          "name": "game_summary_coach_emotion",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.CoachEmotion"
        },
        {
          "name": "game_summary_play",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "ClassificationTallies",
      "field": [
        {
          "name": "white",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ClassificationTally"
        },
        {
          "name": "black",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ClassificationTally"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewReportCard",
      "field": [
        {
          "name": "white",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReviewPlayerReportCard"
        },
        {
          "name": "black",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReviewPlayerReportCard"
        },
        {
          "name": "speech",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "Accuracy",
      "field": [
        {
          "name": "white",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "black",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    },
    {
      "name": "ClassificationTally",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "tally",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewPlayerReportCard",
      "field": [
        {
          "name": "reports_by_phase",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseReportCard"
        },
        {
          "name": "reports_by_category",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard"
        },
        {
          "name": "effective_rating",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "game_rating_v2",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_rating_v2"
        }
      ]
    },
    {
      "name": "GamePhaseReportCard",
      "field": [
        {
          "name": "accuracy_glyph",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "phase",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.GamePhase"
        },
        {
          "name": "accuracy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    },
    {
      "name": "AdvancedStatCategoryReportCard",
      "field": [
        {
          "name": "category",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "performance",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "new_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "rating_change",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "Review",
      "field": [
        {
          "name": "game_summary",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "starting_fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "played_moves",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PlayedMove"
        },
        {
          "name": "final_fen",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayedMove",
      "field": [
        {
          "name": "is_key_moment",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "played_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Move"
        },
        {
          "name": "best_alternative_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Move",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "moved_color",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "coach_emotion",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.CoachEmotion"
        },
        {
          "name": "skills_earned",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SkillsPosition"
        },
        {
          "name": "explain_line",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PlayedMove"
        },
        {
          "name": "best_next_move",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_best_alternative_move"
        },
        {
          "name": "_best_next_move"
        }
      ]
    },
    {
      "name": "Move",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "move_classification",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "score",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Score"
        },
        {
          "name": "speech",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "show_moves_buttons",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ShowMoves"
        },
        {
          "name": "board_markings",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.BoardMarkings"
        }
      ],
      "options": {}
    },
    {
      "name": "ShowMoves",
      "field": [
        {
          "name": "moves_to_show",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "show_text",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "hide_text",
          "number": 3,
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
  Character offset 186466.

```text
MTF9ST09LX0VOREdBTUVTEEcSJAogU0tJTExfS05JR0hUX0FORF9CSVNIT1BfRU5ER0FNRVMQSBoHiqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/game_review.proto":"CjBjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9yZXZpZXcucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSLxAgoKR2FtZVJldmlldxI9CgpldmFsX2dyYXBoGAEgASgLMikuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkV2YWxHcmFwaBI+CgpoaWdobGlnaHRzGAIgASgLMiouY2hlc3Njb20uZXhwbGFuYXRpb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17597"></a>
## FND-17597: Full frontend descriptor: chesscom/explanation_engine/v1/tcn.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/tcn.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "TcnGame",
      "field": [
        {
          "name": "tcn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "initial_fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "move_timestamps",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_initial_fen"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 191387.

```text
Njb20uY2hlc3MudjEuTW92ZRIRCglzaG93X3RleHQYAiABKAkSEQoJaGlkZV90ZXh0GAMgASgJOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/tcn.proto":"CihjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvdGNuLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEilQEKB1RjbkdhbWUSCwoDdGNuGAEgASgJEhgKC2luaXRpYWxfZmVuGAIgASgJSACIAQESFwoPbW92ZV90aW1lc3RhbXBzGAMgAygNEjEKCG1ldGFkYXRhGAQgASgLMh8uY2hlc3Njb20uY2hlc3MudjEuR2FtZU1ldGFkYXRhOgeCph0DC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17598"></a>
## FND-17598: Full frontend descriptor: chesscom/explanation_engine/v1/move_list.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/move_list.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "MoveList",
      "field": [
        {
          "name": "moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    },
    {
      "name": "UciMoveList",
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
  Character offset 191745.

```text
hGAQgASgLMh8uY2hlc3Njb20uY2hlc3MudjEuR2FtZU1ldGFkYXRhOgeCph0DCgEBQg4KDF9pbml0aWFsX2ZlbmIGcHJvdG8z","chesscom/explanation_engine/v1/move_list.proto":"Ci5jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbW92ZV9saXN0LnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiOwoITW92ZUxpc3QSJgoFbW92ZXMYASADKAsyFy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlOgeCph0DCgEBIiUKC1VjaU1vdmVMaXN0Eg0KBW1vdmVzGAEgAygJOgeCph0DCgEBYgZwcm90bzM","chesscom/explanat
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17599"></a>
## FND-17599: Full frontend descriptor: chesscom/explanation_engine/v1/new_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/new_game.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "NewGame",
      "field": [
        {
          "name": "game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Game",
          "oneof_index": 0
        },
        {
          "name": "initial_position",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameInitialPosition",
          "oneof_index": 0
        },
        {
          "name": "tcn_game",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TcnGame",
          "oneof_index": 0
        },
        {
          "name": "position_with_moves",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PositionWithMoves",
          "oneof_index": 0
        },
        {
          "name": "pgn_game",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PgnGame",
          "oneof_index": 0
        },
        {
          "name": "settings",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameSettings"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "from"
        }
      ]
    },
    {
      "name": "PositionWithMoves",
      "field": [
        {
          "name": "initial_position",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameInitialPosition"
        },
        {
          "name": "uci_moves",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UciMoveList",
          "oneof_index": 0
        },
        {
          "name": "moves",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MoveList",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "move_list"
        }
      ]
    },
    {
      "name": "GameInitialPosition",
      "field": [
        {
          "name": "metadata",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata"
        },
        {
          "name": "position",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Position",
          "oneof_index": 0
        },
        {
          "name": "compressed_position",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES",
          "oneof_index": 0
        },
        {
          "name": "fen",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "initial_position"
        }
      ]
    },
    {
      "name": "PgnGame",
      "field": [
        {
          "name": "pgn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "take_first_game_only",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "artifact_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 192048.

```text
NvbS5jaGVzcy52MS5Nb3ZlOgeCph0DCgEBIiUKC1VjaU1vdmVMaXN0Eg0KBW1vdmVzGAEgAygJOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/new_game.proto":"Ci1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbmV3X2dhbWUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSKgAwoHTmV3R2FtZRInCgRnYW1lGAEgASgLMhcuY2hlc3Njb20uY2hlc3MudjEuR2FtZUgAEk8KEGluaXRpYWxfcG9zaXRpb24YAiABKAsyMy5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZUluaXRpYWxQ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17600"></a>
## FND-17600: Full frontend descriptor: chesscom/explanation_engine/v1/invalid_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/invalid_game.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "InvalidGameUnparsable",
      "options": {}
    },
    {
      "name": "InvalidGameIllegalMove",
      "options": {}
    },
    {
      "name": "InvalidGameIllegalKingCount",
      "options": {}
    },
    {
      "name": "InvalidGamePawnOnBackRank",
      "options": {}
    },
    {
      "name": "InvalidGameKingsAdjacent",
      "options": {}
    },
    {
      "name": "InvalidGameKingCapturable",
      "options": {}
    },
    {
      "name": "InvalidGame",
      "field": [
        {
          "name": "unparsable",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGameUnparsable",
          "oneof_index": 0
        },
        {
          "name": "illegal_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGameIllegalMove",
          "oneof_index": 0
        },
        {
          "name": "illegal_king_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGameIllegalKingCount",
          "oneof_index": 0
        },
        {
          "name": "pawn_on_back_rank",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank",
          "oneof_index": 0
        },
        {
          "name": "kings_adjacent",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGameKingsAdjacent",
          "oneof_index": 0
        },
        {
          "name": "king_capturable",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGameKingCapturable",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "invalid_game"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 193553.

```text
AEoCRIxCghtZXRhZGF0YRgEIAEoCzIfLmNoZXNzY29tLmNoZXNzLnYxLkdhbWVNZXRhZGF0YToIgqYdBAoCAQJiBnByb3RvMw","chesscom/explanation_engine/v1/invalid_game.proto":"CjFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvaW52YWxpZF9nYW1lLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiIAoVSW52YWxpZEdhbWVVbnBhcnNhYmxlOgeCph0DCgEBIiEKFkludmFsaWRHYW1lSWxsZWdhbE1vdmU6B4KmHQMKAQEiJgobSW52YWxpZEdhbWVJbGxlZ2FsS2luZ0NvdW50OgeCph0DCgEBIiQKGUludmFs
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17601"></a>
## FND-17601: Full frontend descriptor: chesscom/explanation_engine/v1/feature_new_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_new_game.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "NewGameRequest",
      "field": [
        {
          "name": "new_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NewGame"
        },
        {
          "name": "enable_typed_invalid_game_errors",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "NewGameResponse",
      "field": [
        {
          "name": "played_line",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        },
        {
          "name": "invalid_game",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGame",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_invalid_game"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 194755.

```text
9uX2VuZ2luZS52MS5JbnZhbGlkR2FtZUtpbmdDYXB0dXJhYmxlSAA6B4KmHQMKAQFCDgoMaW52YWxpZF9nYW1lYgZwcm90bzM","chesscom/explanation_engine/v1/feature_new_game.proto":"CjVjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9uZXdfZ2FtZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIn4KDk5ld0dhbWVSZXF1ZXN0EjkKCG5ld19nYW1lGAEgASgLMicuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLk5ld0dhbWUSKAogZW5hYmxlX3R5cGVkX2ludmFsaWRfZ2FtZV9lcnJv
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17602"></a>
## FND-17602: Full frontend descriptor: chesscom/explanation_engine/v1/cee_internal_engine.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/cee_internal_engine.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "CeeInternalEngine",
      "value": [
        {
          "name": "CEE_INTERNAL_ENGINE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CEE_INTERNAL_ENGINE_KOMODO",
          "number": 1
        },
        {
          "name": "CEE_INTERNAL_ENGINE_TORCH",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 195360.

```text
mV4cGxhbmF0aW9uX2VuZ2luZS52MS5JbnZhbGlkR2FtZUgAiAEBOgeCph0DCgEBQg8KDV9pbnZhbGlkX2dhbWViBnByb3RvMw","chesscom/explanation_engine/v1/cee_internal_engine.proto":"CjhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY2VlX2ludGVybmFsX2VuZ2luZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxKncKEUNlZUludGVybmFsRW5naW5lEiMKH0NFRV9JTlRFUk5BTF9FTkdJTkVfVU5TUEVDSUZJRUQQABIeChpDRUVfSU5URVJOQUxfRU5HSU5FX0tPTU9ETxABEh0KGUNFRV9JTlRFUk5BT
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17603"></a>
## FND-17603: Full frontend descriptor: chesscom/explanation_engine/v1/notation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/notation.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "FenNotation",
      "value": [
        {
          "name": "FEN_NOTATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FEN_NOTATION_INFERRED",
          "number": 1
        },
        {
          "name": "FEN_NOTATION_STANDARD",
          "number": 2
        },
        {
          "name": "FEN_NOTATION_SHREDDER",
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
  Character offset 195714.

```text
QABIeChpDRUVfSU5URVJOQUxfRU5HSU5FX0tPTU9ETxABEh0KGUNFRV9JTlRFUk5BTF9FTkdJTkVfVE9SQ0gQAmIGcHJvdG8z","chesscom/explanation_engine/v1/notation.proto":"Ci1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbm90YXRpb24ucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSqFAQoLRmVuTm90YXRpb24SHAoYRkVOX05PVEFUSU9OX1VOU1BFQ0lGSUVEEAASGQoVRkVOX05PVEFUSU9OX0lORkVSUkVEEAESGQoVRkVOX05PVEFUSU9OX1NUQU5EQVJEEAISGQoVRkVOX05PVEFUSU9OX1NIUkVEREVS
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17604"></a>
## FND-17604: Full frontend descriptor: chesscom/explanation_engine/v1/dispose_game_point.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/dispose_game_point.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "DisposeGamePointRequest"
    },
    {
      "name": "DisposeGamePointResponse"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 196063.

```text
AESGQoVRkVOX05PVEFUSU9OX1NUQU5EQVJEEAISGQoVRkVOX05PVEFUSU9OX1NIUkVEREVSEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/dispose_game_point.proto":"CjdjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZGlzcG9zZV9nYW1lX3BvaW50LnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiGQoXRGlzcG9zZUdhbWVQb2ludFJlcXVlc3QiGgoYRGlzcG9zZUdhbWVQb2ludFJlc3BvbnNlYgZwcm90bzM","chesscom/explanation_engine/v1/features.proto":"Ci1jaGVz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17605"></a>
## FND-17605: Full frontend descriptor: chesscom/explanation_engine/v1/features.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/features.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "FeatureId",
      "value": [
        {
          "name": "FEATURE_ID_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FEATURE_ID_ADD_EVALUATIONS",
          "number": 1
        },
        {
          "name": "FEATURE_ID_CEE_VERSION",
          "number": 2
        },
        {
          "name": "FEATURE_ID_EXPECTED_POINTS",
          "number": 3
        },
        {
          "name": "FEATURE_ID_GAME_ANALYSIS",
          "number": 4
        },
        {
          "name": "FEATURE_ID_GAME_PHASE_TRANSITIONS",
          "number": 5
        },
        {
          "name": "FEATURE_ID_GAME_POINT_INFO",
          "number": 6
        },
        {
          "name": "FEATURE_ID_GET_GAME_RESULT",
          "number": 7
        },
        {
          "name": "FEATURE_ID_GET_BOT_CHAT",
          "number": 8
        },
        {
          "name": "FEATURE_ID_GET_BOT_MOVE",
          "number": 9
        },
        {
          "name": "FEATURE_ID_GET_COMPRESSED_POSITION",
          "number": 10
        },
        {
          "name": "FEATURE_ID_GET_ERGONOMIC_GAME",
          "number": 11
        },
        {
          "name": "FEATURE_ID_GET_ERGONOMIC_POSITION",
          "number": 12
        },
        {
          "name": "FEATURE_ID_GET_FEN",
          "number": 13
        },
        {
          "name": "FEATURE_ID_GET_GAME_STATE",
          "number": 14
        },
        {
          "name": "FEATURE_ID_GET_MOVE_DETAILS",
          "number": 15
        },
        {
          "name": "FEATURE_ID_GET_OPENING",
          "number": 16
        },
        {
          "name": "FEATURE_ID_GET_PGN",
          "number": 17
        },
        {
          "name": "FEATURE_ID_GET_PUNISH_MOVE",
          "number": 18
        },
        {
          "name": "FEATURE_ID_LEGAL_MOVES",
          "number": 19
        },
        {
          "name": "FEATURE_ID_LEGAL_PREMOVES",
          "number": 20
        },
        {
          "name": "FEATURE_ID_LOAD_BOT",
          "number": 21
        },
        {
          "name": "FEATURE_ID_LOAD_GAME_STATE",
          "number": 22
        },
        {
          "name": "FEATURE_ID_LUA_COMPLETION",
          "number": 23
        },
        {
          "name": "FEATURE_ID_MAKE_MOVES",
          "number": 24
        },
        {
          "name": "FEATURE_ID_MOVE_CLASSIFICATION",
          "number": 25
        },
        {
          "name": "FEATURE_ID_NEW_GAME",
          "number": 26
        },
        {
          "name": "FEATURE_ID_RUN_LUA",
          "number": 28
        },
        {
          "name": "FEATURE_ID_RUN_SEARCH",
          "number": 29
        },
        {
          "name": "FEATURE_ID_SET_GAME_RESULT",
          "number": 30
        },
        {
          "name": "FEATURE_ID_SIMPLE_THREATS",
          "number": 31
        },
        {
          "name": "FEATURE_ID_VALIDATE_FEN",
          "number": 32
        },
        {
          "name": "FEATURE_ID_CEE_INTERNAL_COMPONENTS",
          "number": 33
        },
        {
          "name": "FEATURE_ID_GAME_TREE",
          "number": 34
        },
        {
          "name": "FEATURE_ID_INIT_ENGINE_POOL",
          "number": 35
        },
        {
          "name": "FEATURE_ID_SET_INTERNAL_ENGINE",
          "number": 36
        },
        {
          "name": "FEATURE_ID_ADD_EXTERNAL_ENGINE",
          "number": 37
        },
        {
          "name": "FEATURE_ID_REMOVE_EXTERNAL_ENGINE",
          "number": 38
        },
        {
          "name": "FEATURE_ID_GET_SAN_MOVES",
          "number": 39
        },
        {
          "name": "FEATURE_ID_LOAD_COACH",
          "number": 40
        },
        {
          "name": "FEATURE_ID_SET_COACH",
          "number": 41
        },
        {
          "name": "FEATURE_ID_GAME_REVIEW",
          "number": 42
        },
        {
          "name": "FEATURE_ID_UNMAKE_MOVES",
          "number": 43
        },
        {
          "name": "FEATURE_ID_GET_CHESS960_INITIAL_POSITION",
          "number": 44
        },
        {
          "name": "FEATURE_ID_GET_COACH_CHAT",
          "number": 45
        },
        {
          "name": "FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS",
          "number": 46
        },
        {
          "name": "FEATURE_ID_GET_COACH_HINT",
          "number": 47
        },
        {
          "name": "FEATURE_ID_LOAD_AND_SET_COACH",
          "number": 48
        },
        {
          "name": "FEATURE_ID_SWITCH_SIDES",
          "number": 49
        },
        {
          "name": "FEATURE_ID_CONVERT_TO_PROTO_MOVES",
          "number": 50
        },
        {
          "name": "FEATURE_ID_RELAXED_LEGAL_MOVES",
          "number": 51
        },
        {
          "name": "FEATURE_ID_RELAXED_APPLY_MOVE",
          "number": 52
        },
        {
          "name": "FEATURE_ID_GET_NON_CHESS_TEXT",
          "number": 53
        },
        {
          "name": "FEATURE_ID_EVALUATE_GAME",
          "number": 54
        },
        {
          "name": "FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES",
          "number": 55
        },
        {
          "name": "FEATURE_ID_RESET_ENGINE_STATE",
          "number": 56
        },
        {
          "name": "FEATURE_ID_CONVERT_FROM_PROTO_MOVES",
          "number": 57
        },
        {
          "name": "FEATURE_ID_FORCE_CRASH",
          "number": 58
        },
        {
          "name": "FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS",
          "number": 59
        },
        {
          "name": "FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS",
          "number": 60
        },
        {
          "name": "FEATURE_ID_BOT_MOVE_FROM_CONFIG",
          "number": 61
        },
        {
          "name": "FEATURE_ID_LOAD_CHARM_MODEL",
          "number": 62
        },
        {
          "name": "FEATURE_ID_VALIDATE_PGN",
          "number": 63
        },
        {
          "name": "FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2",
          "number": 64
        },
        {
          "name": "FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION",
          "number": 65
        },
        {
          "name": "FEATURE_ID_EDIT_PGN_NAGS",
          "number": 66
        },
        {
          "name": "FEATURE_ID_SET_PGN_HEADERS",
          "number": 67
        },
        {
          "name": "FEATURE_ID_CHARM_INFERENCE",
          "number": 68
        },
        {
          "name": "FEATURE_ID_ADD_CHARM_INFERENCE",
          "number": 69
        },
        {
          "name": "FEATURE_ID_BOT_CONFIG_RESOURCES",
          "number": 70
        },
        {
          "name": "FEATURE_ID_SET_PLAYED_LINE",
          "number": 71
        },
        {
          "name": "FEATURE_ID_GENERATE_UUID_V1",
          "number": 72
        },
        {
          "name": "FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION",
          "number": 73
        },
        {
          "name": "FEATURE_ID_ANALYSIS_ANNOTATIONS",
          "number": 74
        },
        {
          "name": "FEATURE_ID_DELETE_PGN_MOVE",
          "number": 75
        },
        {
          "name": "FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH",
          "number": 76
        },
        {
          "name": "FEATURE_ID_GRADE_TRAIN_ITEM_MOVE",
          "number": 77
        },
        {
          "name": "FEATURE_ID_BOT_CONFIG_RESOURCES_V2",
          "number": 78
        },
        {
          "name": "FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS",
          "number": 79
        },
        {
          "name": "FEATURE_ID_LOAD_ECO_BOOK",
          "number": 80
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURES",
          "number": 255
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES",
          "number": 258
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS",
          "number": 259
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS",
          "number": 260
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON",
          "number": 261
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS",
          "number": 262
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE",
          "number": 263
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_NEW_GAME",
          "number": 264
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO",
          "number": 265
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN",
          "number": 266
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE",
          "number": 267
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE",
          "number": 268
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT",
          "number": 269
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA",
          "number": 270
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH",
          "number": 271
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE",
          "number": 272
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET",
          "number": 273
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE",
          "number": 274
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA",
          "number": 275
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS",
          "number": 276
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE",
          "number": 277
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_KEY_POSITION_SEARCH",
          "number": 278
        },
        {
          "name": "FEATURE_ID_ADVANCED_STATS_CATEGORY_SPEECH",
          "number": 279
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_CAPS2",
          "number": 280
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GET_COACH_EMOTION",
          "number": 281
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ITEMS",
          "number": 282
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_POSITION_PROPERTIES",
          "number": 283
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_LOAD_CHARM_MODEL",
          "number": 285
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GET_COHERENCE",
          "number": 286
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_RUN_PVTREES",
          "number": 288
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_ENABLE_GAME_MOCKS",
          "number": 290
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_STATIC_EXCHANGE",
          "number": 292
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GET_PIECE",
          "number": 293
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENT_DETAILS",
          "number": 294
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_SET_MOVE_ANNOTATIONS",
          "number": 295
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GET_MOVE_ANNOTATIONS",
          "number": 296
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GENERATE_TRAIN_ITEMS",
          "number": 297
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_CHARM_INFERENCE",
          "number": 300
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_BUILD_AGENT_STABLE_TREE",
          "number": 301
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_CHECKMATE_TYPE",
          "number": 302
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_WEB_DEMO_JSON",
          "number": 303
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_GAME_FEATURES",
          "number": 304
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_CHECK_ANATOMY",
          "number": 305
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_BRANCH_SUMMARY",
          "number": 306
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_UNIT_TEST_CODE",
          "number": 307
        },
        {
          "name": "FEATURE_ID_INTERNAL_FEATURE_BRILLIANT_MOVES",
          "number": 308
        }
      ],
      "options": {},
      "reserved_range": [
        {
          "start": 27,
          "end": 27
        },
        {
          "start": 284,
          "end": 284
        },
        {
          "start": 287,
          "end": 287
        },
        {
          "start": 289,
          "end": 289
        },
        {
          "start": 291,
          "end": 291
        },
        {
          "start": 298,
          "end": 298
        },
        {
          "start": 299,
          "end": 299
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 196327.

```text
9lbmdpbmUudjEiGQoXRGlzcG9zZUdhbWVQb2ludFJlcXVlc3QiGgoYRGlzcG9zZUdhbWVQb2ludFJlc3BvbnNlYgZwcm90bzM","chesscom/explanation_engine/v1/features.proto":"Ci1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZXMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSroJwoJRmVhdHVyZUlkEhoKFkZFQVRVUkVfSURfVU5TUEVDSUZJRUQQABIeChpGRUFUVVJFX0lEX0FERF9FVkFMVUFUSU9OUxABEhoKFkZFQVRVUkVfSURfQ0VFX1ZFUlNJT04QAhIeChpGRUFUVVJFX0lEX0VYUEVDVEVE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17606"></a>
## FND-17606: Full frontend descriptor: chesscom/explanation_engine/v1/command_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/command_type.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CommandType",
      "field": [
        {
          "name": "feature_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.FeatureId",
          "oneof_index": 0
        },
        {
          "name": "cee_command",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "command_type"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 203293.

```text
QCGgeKph0DCgEBIgQIGxAbIgYInAIQnAIiBgifAhCfAiIGCKECEKECIgYIowIQowIiBgiqAhCqAiIGCKsCEKsCYgZwcm90bzM","chesscom/explanation_engine/v1/command_type.proto":"CjFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY29tbWFuZF90eXBlLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEidQoLQ29tbWFuZFR5cGUSPwoKZmVhdHVyZV9pZBgBIAEoDjIpLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5GZWF0dXJlSWRIABIVCgtjZWVfY29tbWFuZBgCIAEoCUgAQg4KDGNvbW1hbmRfdHlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17607"></a>
## FND-17607: Full frontend descriptor: chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "InternalFeatureUpdateDeveloperOptionsRequest",
      "field": [
        {
          "name": "options",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.DeveloperOptions"
        }
      ]
    },
    {
      "name": "InternalFeatureUpdateDeveloperOptionsResponse",
      "field": [
        {
          "name": "options",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.DeveloperOptions"
        }
      ]
    },
    {
      "name": "DeveloperOptions",
      "field": [
        {
          "name": "coach_debug_info",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "assume_speech_always_present",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_coach_debug_info"
        },
        {
          "name": "_assume_speech_always_present"
        }
      ],
      "reserved_range": [
        {
          "start": 1,
          "end": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 203628.

```text
0aW9uX2VuZ2luZS52MS5GZWF0dXJlSWRIABIVCgtjZWVfY29tbWFuZBgCIAEoCUgAQg4KDGNvbW1hbmRfdHlwZWIGcHJvdG8z","chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto":"Ck5jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvaW50ZXJuYWxfZmVhdHVyZV91cGRhdGVfZGV2ZWxvcGVyX29wdGlvbnMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJxCixJbnRlcm5hbEZlYXR1cmVVcGRhdGVEZXZlbG9wZXJPcHRpb25zUmVxdWVzdBJBCgdvcHRpb25zGAEgASgLMjA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17608"></a>
## FND-17608: Full frontend descriptor: chesscom/explanation_engine/v1/feature_expected_points.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_expected_points.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "ExpectedPointsRequest"
    },
    {
      "name": "ExpectedPointsResponse",
      "field": [
        {
          "name": "expected_points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 204387.

```text
gBiAEBQhMKEV9jb2FjaF9kZWJ1Z19pbmZvQh8KHV9hc3N1bWVfc3BlZWNoX2Fsd2F5c19wcmVzZW50SgQIARADYgZwcm90bzM","chesscom/explanation_engine/v1/feature_expected_points.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9leHBlY3RlZF9wb2ludHMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSIXChVFeHBlY3RlZFBvaW50c1JlcXVlc3QiMQoWRXhwZWN0ZWRQb2ludHNSZXNwb25zZRIXCg9leHBlY3RlZF9wb2ludHMYASABKAFiBnByb3RvMw","chesscom/explana
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17609"></a>
## FND-17609: Full frontend descriptor: chesscom/explanation_engine/v1/text_asset.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/text_asset.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "TextAsset",
      "field": [
        {
          "name": "encrypted_compressed_in_base64",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES",
          "oneof_index": 0
        },
        {
          "name": "json",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "artifact_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "text_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "locale",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "content"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 204691.

```text
FBvaW50c1JlcXVlc3QiMQoWRXhwZWN0ZWRQb2ludHNSZXNwb25zZRIXCg9leHBlY3RlZF9wb2ludHMYASABKAFiBnByb3RvMw","chesscom/explanation_engine/v1/text_asset.proto":"Ci9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvdGV4dF9hc3NldC5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIpEBCglUZXh0QXNzZXQSKAoeZW5jcnlwdGVkX2NvbXByZXNzZWRfaW5fYmFzZTY0GAEgASgMSAASDgoEanNvbhgCIAEoCUgAEhUKC2FydGlmYWN0X2lkGAYgASgJSAASDwoHdGV4dF9pZBgEIAEoCRIOCgZsb2NhbG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17610"></a>
## FND-17610: Full frontend descriptor: chesscom/explanation_engine/v1/feature_legal_premoves.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_legal_premoves.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LegalPremovesRequest",
      "field": [
        {
          "name": "previous_premoves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "from",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "color",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_from"
        },
        {
          "name": "_color"
        }
      ]
    },
    {
      "name": "LegalPremovesResponse",
      "field": [
        {
          "name": "legal_premoves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 205060.

```text
0X2lkGAYgASgJSAASDwoHdGV4dF9pZBgEIAEoCRIOCgZsb2NhbGUYBSABKAk6B4KmHQMKAQFCCQoHY29udGVudGIGcHJvdG8z","chesscom/explanation_engine/v1/feature_legal_premoves.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sZWdhbF9wcmVtb3Zlcy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIsIBChRMZWdhbFByZW1vdmVzUmVxdWVzdBIyChFwcmV2aW91c19wcmVtb3ZlcxgBIAMoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmUSLAoEZnJvbRgCIAEoDjIZLmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17611"></a>
## FND-17611: Full frontend descriptor: chesscom/explanation_engine/v1/feature_move_classification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_move_classification.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "MoveClassificationRequest",
      "field": [
        {
          "name": "stream_results",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_pv_classifications",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "MoveClassificationResponse",
      "field": [
        {
          "name": "active",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalClassification"
        },
        {
          "name": "alternative",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AltMoveClassification",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "progress",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "pv_classifications",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PvClassifications",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_alternative"
        },
        {
          "name": "_pv_classifications"
        }
      ]
    },
    {
      "name": "PvClassifications",
      "field": [
        {
          "name": "classifications",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalClassification"
        }
      ],
      "options": {}
    },
    {
      "name": "AltMoveClassification",
      "field": [
        {
          "name": "classification",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalClassification"
        },
        {
          "name": "move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "progress",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 205633.

```text
lc3BvbnNlEi8KDmxlZ2FsX3ByZW1vdmVzGAEgAygLMhcuY2hlc3Njb20uY2hlc3MudjEuTW92ZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_move_classification.proto":"CkBjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9tb3ZlX2NsYXNzaWZpY2F0aW9uLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiXwoZTW92ZUNsYXNzaWZpY2F0aW9uUmVxdWVzdBIWCg5zdHJlYW1fcmVzdWx0cxgBIAEoCBIhChllbmFibGVfcHZfY2xhc3NpZmljYXRpb25zGAIgASgIOgeCp
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17612"></a>
## FND-17612: Full frontend descriptor: chesscom/explanation_engine/v1/cee_internal_component.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/cee_internal_component.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "CeeInternalComponent",
      "value": [
        {
          "name": "CEE_INTERNAL_COMPONENT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CEE_INTERNAL_COMPONENT_LUA",
          "number": 1
        },
        {
          "name": "CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY",
          "number": 2
        },
        {
          "name": "CEE_INTERNAL_COMPONENT_TORCH_SMALL",
          "number": 3
        },
        {
          "name": "CEE_INTERNAL_COMPONENT_TORCH_LARGE",
          "number": 4
        },
        {
          "name": "CEE_INTERNAL_COMPONENT_KOMODO",
          "number": 5
        },
        {
          "name": "CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES",
          "number": 6
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 206781.

```text
QoEbW92ZRgDIAEoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmUSEAoIcHJvZ3Jlc3MYBCABKAI6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/cee_internal_component.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY2VlX2ludGVybmFsX2NvbXBvbmVudC5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxKq8CChRDZWVJbnRlcm5hbENvbXBvbmVudBImCiJDRUVfSU5URVJOQUxfQ09NUE9ORU5UX1VOU1BFQ0lGSUVEEAASHgoaQ0VFX0lOVEVSTkFMX0NPTVBPTkVOVF9MVUEQARIuCi
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17613"></a>
## FND-17613: Full frontend descriptor: chesscom/explanation_engine/v1/feature_cee_internal_components.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_cee_internal_components.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CeeInternalComponentsRequest"
    },
    {
      "name": "CeeInternalComponentsResponse",
      "field": [
        {
          "name": "components",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.CeeInternalComponent"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 207389.

```text
9DT01QT05FTlRfS09NT0RPEAUSLAooQ0VFX0lOVEVSTkFMX0NPTVBPTkVOVF9JTlRFUk5BTF9GRUFUVVJFUxAGYgZwcm90bzM","chesscom/explanation_engine/v1/feature_cee_internal_components.proto":"CkRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9jZWVfaW50ZXJuYWxfY29tcG9uZW50cy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIh4KHENlZUludGVybmFsQ29tcG9uZW50c1JlcXVlc3QiaQodQ2VlSW50ZXJuYWxDb21wb25lbnRzUmVzcG9uc2USSAoKY29tcG9uZW50cxgBIAMoD
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17614"></a>
## FND-17614: Full frontend descriptor: chesscom/explanation_engine/v1/feature_set_coach.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_set_coach.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SetCoachRequest",
      "field": [
        {
          "name": "text_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "locale",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "SetCoachResponse",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 207795.

```text
uZW50cxgBIAMoDjI0LmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5DZWVJbnRlcm5hbENvbXBvbmVudGIGcHJvdG8z","chesscom/explanation_engine/v1/feature_set_coach.proto":"CjZjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9zZXRfY29hY2gucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSI7Cg9TZXRDb2FjaFJlcXVlc3QSDwoHdGV4dF9pZBgBIAEoCRIOCgZsb2NhbGUYAiABKAk6B4KmHQMKAQEiGwoQU2V0Q29hY2hSZXNwb25zZToHgqYdAwoBAWIGcHJvdG8z","chesscom/exp
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17615"></a>
## FND-17615: Full frontend descriptor: chesscom/explanation_engine/v1/punish_move.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/punish_move.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "PunishMove",
      "field": [
        {
          "name": "arrow",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Arrow",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "evaluation",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Evaluation"
        },
        {
          "name": "speech",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "show_moves",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "hide_moves",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_arrow"
        },
        {
          "name": "_move"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 208103.

```text
4dF9pZBgBIAEoCRIOCgZsb2NhbGUYAiABKAk6B4KmHQMKAQEiGwoQU2V0Q29hY2hSZXNwb25zZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/punish_move.proto":"CjBjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvcHVuaXNoX21vdmUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSKWAgoKUHVuaXNoTW92ZRIsCgVhcnJvdxgBIAEoCzIYLmNoZXNzY29tLmNoZXNzLnYxLkFycm93SACIAQESMgoKZXZhbHVhdGlvbhgCIAEoCzIeLmNoZXNzY29tLmVuZ2luZS52MS5FdmFsdWF0aW9uEjYKBnNwZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17616"></a>
## FND-17616: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_punish_move.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_punish_move.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetPunishMoveRequest",
      "options": {}
    },
    {
      "name": "GetPunishMoveResponse",
      "field": [
        {
          "name": "punish_move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PunishMove"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 208652.

```text
UYBiABKAsyFy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlSAGIAQE6B4KmHQMKAQFCCAoGX2Fycm93QgcKBV9tb3ZlYgZwcm90bzM","chesscom/explanation_engine/v1/feature_get_punish_move.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfcHVuaXNoX21vdmUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSIfChRHZXRQdW5pc2hNb3ZlUmVxdWVzdDoHgqYdAwoBASJhChVHZXRQdW5pc2hNb3ZlUmVzcG9uc2USPwoLcHVuaXNoX21vdmUYASABKAsyKi5jaGVzc2NvbS5leHBsYW5hd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17617"></a>
## FND-17617: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_pgn.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_pgn.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetPgnRequest",
      "field": [
        {
          "name": "game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Game",
          "oneof_index": 0
        },
        {
          "name": "game_state",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState",
          "oneof_index": 0
        },
        {
          "name": "starting_game_point",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "pgn_fen_header_notation",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.FenNotation",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "main_line_only",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "user_variations_only",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "included_game_points",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "include_threats",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "include_all_scored_gamepoints",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "unscored_gamepoint_limit",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "explicit_included_game_points",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "annotation_serialization_format",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "game_to_convert"
        },
        {
          "name": "_pgn_fen_header_notation"
        },
        {
          "name": "_main_line_only"
        },
        {
          "name": "_user_variations_only"
        },
        {
          "name": "_include_threats"
        },
        {
          "name": "_include_all_scored_gamepoints"
        },
        {
          "name": "_unscored_gamepoint_limit"
        },
        {
          "name": "_annotation_serialization_format"
        }
      ]
    },
    {
      "name": "GetPgnResponse",
      "field": [
        {
          "name": "pgn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "PgnAnnotationSerializationFormat",
      "value": [
        {
          "name": "PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE",
          "number": 1
        },
        {
          "name": "PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM",
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
  Character offset 209030.

```text
oX21vdmUYASABKAsyKi5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuUHVuaXNoTW92ZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_pgn.proto":"CjRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfcGduLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEirAYKDUdldFBnblJlcXVlc3QSJwoEZ2FtZRgBIAEoCzIXLmNoZXNzY29tLmNoZXNzLnYxLkdhbWVIABI/CgpnYW1lX3N0YXRlGAIgASgLMikuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxL
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17618"></a>
## FND-17618: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_opening.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_opening.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetOpeningRequest",
      "field": [
        {
          "name": "locale",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Locale",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_locale"
        }
      ]
    },
    {
      "name": "GetOpeningResponse",
      "field": [
        {
          "name": "opening",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Opening",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_opening"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 210623.

```text
FTRRABEjEKLVBHTl9BTk5PVEFUSU9OX1NFUklBTElaQVRJT05fRk9STUFUX0NIRVNTX0NPTRACGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_get_opening.proto":"CjhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfb3BlbmluZy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxImQKEUdldE9wZW5pbmdSZXF1ZXN0EjsKBmxvY2FsZRgBIAEoDjImLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Mb2NhbGVIAIgBAToHgqYdAwoBAUIJCgdfbG9jYWxlImgKE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17619"></a>
## FND-17619: Full frontend descriptor: chesscom/explanation_engine/v1/feature_validate_pgn.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_validate_pgn.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "ValidatePgnRequest",
      "field": [
        {
          "name": "pgn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "artifact_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "ValidatePgnResponse",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PgnGameValidationResult"
        }
      ],
      "options": {}
    },
    {
      "name": "PgnGameValidationResult",
      "field": [
        {
          "name": "success",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PgnGameValidationSuccess",
          "oneof_index": 0
        },
        {
          "name": "error",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PgnGameValidationError",
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
      "name": "PgnGameValidationSuccess",
      "field": [
        {
          "name": "game_pgn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "PgnGameValidationError",
      "field": [
        {
          "name": "error",
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
  Character offset 211093.

```text
uY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLk9wZW5pbmdIAIgBAToHgqYdAwoBAUIKCghfb3BlbmluZ2IGcHJvdG8z","chesscom/explanation_engine/v1/feature_validate_pgn.proto":"CjljaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV92YWxpZGF0ZV9wZ24ucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSI/ChJWYWxpZGF0ZVBnblJlcXVlc3QSCwoDcGduGAEgASgJEhMKC2FydGlmYWN0X2lkGAIgASgJOgeCph0DCgEBImcKE1ZhbGlkYXRlUGduUmVzcG9uc2USRwoGcmVzdWx0GAEgAygL
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17620"></a>
## FND-17620: Full frontend descriptor: chesscom/explanation_engine/v1/bot.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/bot.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "BotTimeLimits",
      "field": [
        {
          "name": "time_limit_ms",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "time_left_ms",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "time_inc_ms",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_time_limit_ms"
        },
        {
          "name": "_time_left_ms"
        },
        {
          "name": "_time_inc_ms"
        }
      ]
    },
    {
      "name": "BotOptions",
      "field": [
        {
          "name": "rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "adaptive",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "personality",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.BotPersonality",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "book_path",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "time_limits",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotTimeLimits",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "artifact_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_adaptive"
        },
        {
          "name": "_personality"
        },
        {
          "name": "_book_path"
        },
        {
          "name": "_time_limits"
        },
        {
          "name": "_artifact_id"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "BotPersonality",
      "value": [
        {
          "name": "BOT_PERSONALITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOT_PERSONALITY_DEFAULT",
          "number": 1
        },
        {
          "name": "BOT_PERSONALITY_ACTIVE",
          "number": 2
        },
        {
          "name": "BOT_PERSONALITY_AGRESSIVE",
          "number": 3
        },
        {
          "name": "BOT_PERSONALITY_BEGINNER",
          "number": 4
        },
        {
          "name": "BOT_PERSONALITY_DEFENSIVE",
          "number": 5
        },
        {
          "name": "BOT_PERSONALITY_ENDGAME",
          "number": 6
        },
        {
          "name": "BOT_PERSONALITY_HUMAN",
          "number": 7
        },
        {
          "name": "BOT_PERSONALITY_POSITIONAL",
          "number": 8
        },
        {
          "name": "BOT_PERSONALITY_CARLSEN",
          "number": 9
        },
        {
          "name": "BOT_PERSONALITY_FISCHER",
          "number": 10
        },
        {
          "name": "BOT_PERSONALITY_HIKARU",
          "number": 11
        },
        {
          "name": "BOT_PERSONALITY_KASPAROV",
          "number": 12
        },
        {
          "name": "BOT_PERSONALITY_NEW_TO_CHESS",
          "number": 13
        },
        {
          "name": "BOT_PERSONALITY_DANNY",
          "number": 14
        },
        {
          "name": "BOT_PERSONALITY_UNLEASHED",
          "number": 15
        }
      ],
      "options": {}
    },
    {
      "name": "BotEngine",
      "value": [
        {
          "name": "BOT_ENGINE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOT_ENGINE_KOMODO",
          "number": 1
        },
        {
          "name": "BOT_ENGINE_TORCH",
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
  Character offset 211918.

```text
AEgASgJOgeCph0DCgEBIjAKFlBnbkdhbWVWYWxpZGF0aW9uRXJyb3ISDQoFZXJyb3IYASABKAk6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/bot.proto":"CihjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvYm90LnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEinAEKDUJvdFRpbWVMaW1pdHMSGgoNdGltZV9saW1pdF9tcxgBIAEoBUgAiAEBEhkKDHRpbWVfbGVmdF9tcxgCIAEoBUgBiAEBEhgKC3RpbWVfaW5jX21zGAMgASgFSAKIAQE6B4KmHQMKAQFCEAoOX3RpbWVfbGltaXRfbXNCDwoNX3Rpb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17621"></a>
## FND-17621: Full frontend descriptor: chesscom/explanation_engine/v1/stats.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/stats.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "AdvancedStatsUser",
      "field": [
        {
          "name": "advanced_stats_percentiles",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.stats.v1.AdvancedStatPercentile"
        },
        {
          "name": "category_performances",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.stats.v1.AdvancedStatCategoryStats"
        }
      ],
      "options": {}
    },
    {
      "name": "AdvancedStatsOther",
      "field": [
        {
          "name": "white_player_category_performances",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.stats.v1.AdvancedStatCategoryGamePerformance"
        },
        {
          "name": "black_player_category_performances",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.stats.v1.AdvancedStatCategoryGamePerformance"
        },
        {
          "name": "user_advanced_stats_percentiles",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.stats.v1.AdvancedStatPercentile"
        }
      ],
      "options": {}
    },
    {
      "name": "AdvancedStatsForGame",
      "field": [
        {
          "name": "advanced_stats_user",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AdvancedStatsUser",
          "oneof_index": 0
        },
        {
          "name": "advanced_stats_other",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AdvancedStatsOther",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "advanced_stats"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 213534.

```text
1BFQ0lGSUVEEAASFQoRQk9UX0VOR0lORV9LT01PRE8QARIUChBCT1RfRU5HSU5FX1RPUkNIEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/stats.proto":"CipjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc3RhdHMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSK4AQoRQWR2YW5jZWRTdGF0c1VzZXISTQoaYWR2YW5jZWRfc3RhdHNfcGVyY2VudGlsZXMYASADKAsyKS5jaGVzc2NvbS5zdGF0cy52MS5BZHZhbmNlZFN0YXRQZXJjZW50aWxlEksKFWNhdGVnb3J5X3BlcmZvcm1hbmNlcxgCIAM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17622"></a>
## FND-17622: Full frontend descriptor: chesscom/explanation_engine/v1/analysis_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/analysis_type.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "AnalysisType",
      "value": [
        {
          "name": "ANALYSIS_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ANALYSIS_TYPE_STALEMATE",
          "number": 1
        },
        {
          "name": "ANALYSIS_TYPE_FIFTY_MOVE",
          "number": 2
        },
        {
          "name": "ANALYSIS_TYPE_REPETITION",
          "number": 3
        },
        {
          "name": "ANALYSIS_TYPE_INSUFFICIENT",
          "number": 4
        },
        {
          "name": "ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE",
          "number": 5
        },
        {
          "name": "ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE",
          "number": 6
        },
        {
          "name": "ANALYSIS_TYPE_IGNORES_THREAT",
          "number": 7
        },
        {
          "name": "ANALYSIS_TYPE_INDIRECT_SACRIFICE",
          "number": 8
        },
        {
          "name": "ANALYSIS_TYPE_CHECKMATE",
          "number": 9
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_MATE",
          "number": 11
        },
        {
          "name": "ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE",
          "number": 12
        },
        {
          "name": "ANALYSIS_TYPE_SLOWER_MATE",
          "number": 14
        },
        {
          "name": "ANALYSIS_TYPE_STILL_MATE",
          "number": 15
        },
        {
          "name": "ANALYSIS_TYPE_MATE_THREAT",
          "number": 16
        },
        {
          "name": "ANALYSIS_TYPE_INTERESTING",
          "number": 17
        },
        {
          "name": "ANALYSIS_TYPE_FREE_PIECE",
          "number": 18
        },
        {
          "name": "ANALYSIS_TYPE_QUASI_FREE_PIECE",
          "number": 19
        },
        {
          "name": "ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK",
          "number": 20
        },
        {
          "name": "ANALYSIS_TYPE_FORK_WITH_MATE",
          "number": 21
        },
        {
          "name": "ANALYSIS_TYPE_FORK",
          "number": 22
        },
        {
          "name": "ANALYSIS_TYPE_MULTI_ATTACK",
          "number": 23
        },
        {
          "name": "ANALYSIS_TYPE_SKEWER",
          "number": 24
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLE_CHECK",
          "number": 25
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT",
          "number": 26
        },
        {
          "name": "ANALYSIS_TYPE_DISCOVERED_ATTACK",
          "number": 27
        },
        {
          "name": "ANALYSIS_TYPE_PROMOTION",
          "number": 28
        },
        {
          "name": "ANALYSIS_TYPE_DISCOVERED_CHECK",
          "number": 29
        },
        {
          "name": "ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE",
          "number": 30
        },
        {
          "name": "ANALYSIS_TYPE_THREATENS_PINNED",
          "number": 31
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS",
          "number": 32
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS",
          "number": 33
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_ISOLATED_PAWN",
          "number": 34
        },
        {
          "name": "ANALYSIS_TYPE_EQUAL_TRADE",
          "number": 35
        },
        {
          "name": "ANALYSIS_TYPE_IMMEDIATE_RECAPTURE",
          "number": 36
        },
        {
          "name": "ANALYSIS_TYPE_OBVIOUS_RECAPTURE",
          "number": 37
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURES_CHECKER",
          "number": 38
        },
        {
          "name": "ANALYSIS_TYPE_COUNTER_THREAT",
          "number": 39
        },
        {
          "name": "ANALYSIS_TYPE_REMOVES_ATTACKER",
          "number": 40
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKS_ATTACKER",
          "number": 41
        },
        {
          "name": "ANALYSIS_TYPE_UNPINS_DEFENDER",
          "number": 42
        },
        {
          "name": "ANALYSIS_TYPE_PINS_ATTACKER",
          "number": 43
        },
        {
          "name": "ANALYSIS_TYPE_PIN",
          "number": 44
        },
        {
          "name": "ANALYSIS_TYPE_RELATIVE_PIN",
          "number": 45
        },
        {
          "name": "ANALYSIS_TYPE_PROTECTS_PIECE",
          "number": 46
        },
        {
          "name": "ANALYSIS_TYPE_DEFENDS_PIECE",
          "number": 47
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_LUFT",
          "number": 48
        },
        {
          "name": "ANALYSIS_TYPE_GAMBITS_PAWN",
          "number": 49
        },
        {
          "name": "ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER",
          "number": 50
        },
        {
          "name": "ANALYSIS_TYPE_STRIKES_AT_CENTER",
          "number": 51
        },
        {
          "name": "ANALYSIS_TYPE_MAKES_PASSED_PAWN",
          "number": 52
        },
        {
          "name": "ANALYSIS_TYPE_PREVENTS_CASTLING",
          "number": 53
        },
        {
          "name": "ANALYSIS_TYPE_TAKES_OUTPOST",
          "number": 54
        },
        {
          "name": "ANALYSIS_TYPE_CHALLENGES_OPEN_FILE",
          "number": 55
        },
        {
          "name": "ANALYSIS_TYPE_TAKES_OPEN_FILE",
          "number": 56
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN",
          "number": 57
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN",
          "number": 58
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKS_CHECKER",
          "number": 59
        },
        {
          "name": "ANALYSIS_TYPE_KICKS_CHECKER",
          "number": 60
        },
        {
          "name": "ANALYSIS_TYPE_EVADES_CHECK",
          "number": 61
        },
        {
          "name": "ANALYSIS_TYPE_KICKS",
          "number": 62
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_ON_SEVENTH",
          "number": 63
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO",
          "number": 64
        },
        {
          "name": "ANALYSIS_TYPE_WINS_TEMPO",
          "number": 65
        },
        {
          "name": "ANALYSIS_TYPE_OFFERS_TRADE",
          "number": 66
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURE_THREAT",
          "number": 67
        },
        {
          "name": "ANALYSIS_TYPE_CONNECTS_ROOKS",
          "number": 68
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLES_ROOKS",
          "number": 69
        },
        {
          "name": "ANALYSIS_TYPE_UNDOUBLES_PAWNS",
          "number": 71
        },
        {
          "name": "ANALYSIS_TYPE_FIANCHETTO",
          "number": 72
        },
        {
          "name": "ANALYSIS_TYPE_CASTLES_SAME_SIDE",
          "number": 73
        },
        {
          "name": "ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE",
          "number": 74
        },
        {
          "name": "ANALYSIS_TYPE_CASTLES_KING_SIDE",
          "number": 75
        },
        {
          "name": "ANALYSIS_TYPE_CASTLES_QUEEN_SIDE",
          "number": 76
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURES",
          "number": 77
        },
        {
          "name": "ANALYSIS_TYPE_ACTIVATES_KING",
          "number": 78
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS",
          "number": 79
        },
        {
          "name": "ANALYSIS_TYPE_CENTRALIZES_KNIGHT",
          "number": 80
        },
        {
          "name": "ANALYSIS_TYPE_BISHOP_GAINS_SCOPE",
          "number": 81
        },
        {
          "name": "ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT",
          "number": 82
        },
        {
          "name": "ANALYSIS_TYPE_DELAYED_RECAPTURE",
          "number": 83
        },
        {
          "name": "ANALYSIS_TYPE_RETREAT",
          "number": 84
        },
        {
          "name": "ANALYSIS_TYPE_OBVIOUS_RETREAT",
          "number": 85
        },
        {
          "name": "ANALYSIS_TYPE_CRITICAL",
          "number": 86
        },
        {
          "name": "ANALYSIS_TYPE_WINNING",
          "number": 87
        },
        {
          "name": "ANALYSIS_TYPE_COMEBACK",
          "number": 88
        },
        {
          "name": "ANALYSIS_TYPE_BLUNDER_PUNISH",
          "number": 89
        },
        {
          "name": "ANALYSIS_TYPE_TAKES_OPPORTUNITY",
          "number": 90
        },
        {
          "name": "ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT",
          "number": 91
        },
        {
          "name": "ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG",
          "number": 92
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURE_THREAT_FROM",
          "number": 93
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURE_THREAT_TO",
          "number": 94
        },
        {
          "name": "ANALYSIS_TYPE_WINS_MATERIAL",
          "number": 95
        },
        {
          "name": "ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE",
          "number": 96
        },
        {
          "name": "ANALYSIS_TYPE_NO_LONGER_MATE",
          "number": 97
        },
        {
          "name": "ANALYSIS_TYPE_BAD_CAPTURE_CHOICE",
          "number": 98
        },
        {
          "name": "ANALYSIS_TYPE_LOSES_MATERIAL",
          "number": 100
        },
        {
          "name": "ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS",
          "number": 101
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS",
          "number": 102
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLES_PAWNS",
          "number": 103
        },
        {
          "name": "ANALYSIS_TYPE_ISOLATES_PAWN",
          "number": 104
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION",
          "number": 105
        },
        {
          "name": "ANALYSIS_TYPE_WINNING_TO_BETTER",
          "number": 106
        },
        {
          "name": "ANALYSIS_TYPE_WINNING_TO_EQUAL",
          "number": 107
        },
        {
          "name": "ANALYSIS_TYPE_WINNING_TO_WORSE",
          "number": 108
        },
        {
          "name": "ANALYSIS_TYPE_WINNING_TO_LOSING",
          "number": 109
        },
        {
          "name": "ANALYSIS_TYPE_BETTER_TO_EQUAL",
          "number": 110
        },
        {
          "name": "ANALYSIS_TYPE_BETTER_TO_WORSE",
          "number": 111
        },
        {
          "name": "ANALYSIS_TYPE_BETTER_TO_LOSING",
          "number": 112
        },
        {
          "name": "ANALYSIS_TYPE_EQUAL_TO_WORSE",
          "number": 113
        },
        {
          "name": "ANALYSIS_TYPE_EQUAL_TO_LOSING",
          "number": 114
        },
        {
          "name": "ANALYSIS_TYPE_WORSE_TO_LOSING",
          "number": 115
        },
        {
          "name": "ANALYSIS_TYPE_UNDERPROMOTION",
          "number": 116
        },
        {
          "name": "ANALYSIS_TYPE_UNDERPROMOTION_MATE",
          "number": 117
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_REPETITION",
          "number": 118
        },
        {
          "name": "ANALYSIS_TYPE_UNPINS_WITH_DEFENSE",
          "number": 119
        },
        {
          "name": "ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK",
          "number": 120
        },
        {
          "name": "ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER",
          "number": 121
        },
        {
          "name": "ANALYSIS_TYPE_PINS_DEFENDER",
          "number": 122
        },
        {
          "name": "ANALYSIS_TYPE_MAINTAINED_MATE",
          "number": 123
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS",
          "number": 124
        },
        {
          "name": "ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE",
          "number": 125
        },
        {
          "name": "ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE",
          "number": 126
        },
        {
          "name": "ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE",
          "number": 127
        },
        {
          "name": "ANALYSIS_TYPE_IGNORES_THREAT_MATE",
          "number": 128
        },
        {
          "name": "ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE",
          "number": 129
        },
        {
          "name": "ANALYSIS_TYPE_BACK_RANK_MATE",
          "number": 130
        },
        {
          "name": "ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION",
          "number": 131
        },
        {
          "name": "ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION",
          "number": 132
        },
        {
          "name": "ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION",
          "number": 133
        },
        {
          "name": "ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION",
          "number": 134
        },
        {
          "name": "ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER",
          "number": 135
        },
        {
          "name": "ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY",
          "number": 136
        },
        {
          "name": "ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK",
          "number": 137
        },
        {
          "name": "ANALYSIS_TYPE_PUNISH_MOVE_NONE",
          "number": 138
        },
        {
          "name": "ANALYSIS_TYPE_REMOVES_DEFENDER",
          "number": 140
        },
        {
          "name": "ANALYSIS_TYPE_REMOVES_MATE_DEFENDER",
          "number": 141
        },
        {
          "name": "ANALYSIS_TYPE_KICKS_DEFENDER",
          "number": 142
        },
        {
          "name": "ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER",
          "number": 143
        },
        {
          "name": "ANALYSIS_TYPE_KICKS_MATE_DEFENDER",
          "number": 144
        },
        {
          "name": "ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE",
          "number": 145
        },
        {
          "name": "ANALYSIS_TYPE_TRADE_TO_SIMPLIFY",
          "number": 146
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKADE",
          "number": 147
        },
        {
          "name": "ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN",
          "number": 148
        },
        {
          "name": "ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN",
          "number": 149
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_PAWN_CHAIN",
          "number": 150
        },
        {
          "name": "ANALYSIS_TYPE_UNTRIPLES_PAWNS",
          "number": 151
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_BACKWARD_PAWN",
          "number": 152
        },
        {
          "name": "ANALYSIS_TYPE_CURES_BACKWARD_PAWN",
          "number": 153
        },
        {
          "name": "ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING",
          "number": 154
        },
        {
          "name": "ANALYSIS_TYPE_CURES_ISOLATED_PAWN",
          "number": 155
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN",
          "number": 156
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_TAKES_OUTPOST",
          "number": 157
        },
        {
          "name": "ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE",
          "number": 158
        },
        {
          "name": "ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE",
          "number": 159
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN",
          "number": 160
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE",
          "number": 161
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN",
          "number": 162
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE",
          "number": 163
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN",
          "number": 164
        },
        {
          "name": "ANALYSIS_TYPE_WEAKENED_CASTLED_KING",
          "number": 165
        },
        {
          "name": "ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING",
          "number": 166
        },
        {
          "name": "ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME",
          "number": 167
        },
        {
          "name": "ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME",
          "number": 168
        },
        {
          "name": "ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME",
          "number": 169
        },
        {
          "name": "ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME",
          "number": 170
        },
        {
          "name": "ANALYSIS_TYPE_CHECKS_WITH_PIECE",
          "number": 171
        },
        {
          "name": "ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN",
          "number": 172
        },
        {
          "name": "ANALYSIS_TYPE_EXCHANGE_SACRIFICE",
          "number": 173
        },
        {
          "name": "ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE",
          "number": 174
        },
        {
          "name": "ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE",
          "number": 175
        },
        {
          "name": "ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE",
          "number": 176
        },
        {
          "name": "ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE",
          "number": 177
        },
        {
          "name": "ANALYSIS_TYPE_GAINS_CENTRAL_SPACE",
          "number": 178
        },
        {
          "name": "ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME",
          "number": 179
        },
        {
          "name": "ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME",
          "number": 180
        },
        {
          "name": "ANALYSIS_TYPE_LADDER_MATE",
          "number": 181
        },
        {
          "name": "ANALYSIS_TYPE_AVOIDS_TRADE",
          "number": 182
        },
        {
          "name": "ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN",
          "number": 183
        },
        {
          "name": "ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW",
          "number": 184
        },
        {
          "name": "ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE",
          "number": 185
        },
        {
          "name": "ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE",
          "number": 186
        },
        {
          "name": "ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE",
          "number": 187
        },
        {
          "name": "ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK",
          "number": 188
        },
        {
          "name": "ANALYSIS_TYPE_OPENS_UP_WEAK_KING",
          "number": 189
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_LAST_PIECE",
          "number": 190
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_CENTER",
          "number": 191
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_RECAPTURE",
          "number": 192
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_OPENING",
          "number": 193
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME",
          "number": 194
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_STALEMATE",
          "number": 195
        },
        {
          "name": "ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED",
          "number": 196
        },
        {
          "name": "ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED",
          "number": 197
        },
        {
          "name": "ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED",
          "number": 198
        },
        {
          "name": "ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING",
          "number": 199
        },
        {
          "name": "ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER",
          "number": 200
        },
        {
          "name": "ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO",
          "number": 201
        },
        {
          "name": "ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND",
          "number": 202
        },
        {
          "name": "ANALYSIS_TYPE_PAWN_STORM",
          "number": 203
        },
        {
          "name": "ANALYSIS_TYPE_LAUNCHES_PAWN_STORM",
          "number": 204
        },
        {
          "name": "ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN",
          "number": 205
        },
        {
          "name": "ANALYSIS_TYPE_PILE_TRADE",
          "number": 206
        },
        {
          "name": "ANALYSIS_TYPE_OPENS_UP_SCOPE",
          "number": 207
        },
        {
          "name": "ANALYSIS_TYPE_FORCED",
          "number": 208
        },
        {
          "name": "ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION",
          "number": 209
        },
        {
          "name": "ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION",
          "number": 210
        },
        {
          "name": "ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION",
          "number": 211
        },
        {
          "name": "ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN",
          "number": 212
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE",
          "number": 213
        },
        {
          "name": "ANALYSIS_TYPE_VACATES_PUSHING_SQUARE",
          "number": 214
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN",
          "number": 215
        },
        {
          "name": "ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC",
          "number": 216
        },
        {
          "name": "ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE",
          "number": 217
        },
        {
          "name": "ANALYSIS_TYPE_PROTECTS_PASSED_PAWN",
          "number": 218
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE",
          "number": 219
        },
        {
          "name": "ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE",
          "number": 220
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE",
          "number": 221
        },
        {
          "name": "ANALYSIS_TYPE_GOOD_TRADE",
          "number": 222
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN",
          "number": 223
        },
        {
          "name": "ANALYSIS_TYPE_NEVER_PLAY_F3",
          "number": 224
        },
        {
          "name": "ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE",
          "number": 225
        },
        {
          "name": "ANALYSIS_TYPE_DID_NOT_RECAPTURE",
          "number": 226
        },
        {
          "name": "ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER",
          "number": 227
        },
        {
          "name": "ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH",
          "number": 228
        },
        {
          "name": "ANALYSIS_TYPE_MOVES_PINNED_PIECE",
          "number": 229
        },
        {
          "name": "ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK",
          "number": 230
        },
        {
          "name": "ANALYSIS_TYPE_REMOVES_OWN_DEFENDER",
          "number": 231
        },
        {
          "name": "ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER",
          "number": 232
        },
        {
          "name": "ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT",
          "number": 233
        },
        {
          "name": "ANALYSIS_TYPE_CENTRAL_BREAK",
          "number": 234
        },
        {
          "name": "ANALYSIS_TYPE_HANGS_PIECE",
          "number": 235
        },
        {
          "name": "ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE",
          "number": 236
        },
        {
          "name": "ANALYSIS_TYPE_ESCAPES_THREAT",
          "number": 237
        },
        {
          "name": "ANALYSIS_TYPE_TEMPO_BEFORE_FREE_PIECE",
          "number": 238
        },
        {
          "name": "ANALYSIS_TYPE_CREATES_BATTERY",
          "number": 239
        },
        {
          "name": "ANALYSIS_TYPE_TAKES_OPPOSITION",
          "number": 240
        },
        {
          "name": "ANALYSIS_TYPE_ROYAL_FORK",
          "number": 241
        },
        {
          "name": "ANALYSIS_TYPE_PREPARES_TO_CASTLE_KINGSIDE",
          "number": 242
        },
        {
          "name": "ANALYSIS_TYPE_PREPARES_TO_CASTLE_QUEENSIDE",
          "number": 243
        },
        {
          "name": "ANALYSIS_TYPE_CONNECTS_ROOKS_7TH",
          "number": 244
        },
        {
          "name": "ANALYSIS_TYPE_IGNORES_ATTACKED_PAWN",
          "number": 245
        },
        {
          "name": "ANALYSIS_TYPE_DESPERADO",
          "number": 246
        },
        {
          "name": "ANALYSIS_TYPE_PSEUDO_FORK",
          "number": 247
        },
        {
          "name": "ANALYSIS_TYPE_PRESSURES_PINNED_PIECE",
          "number": 248
        },
        {
          "name": "ANALYSIS_TYPE_ENPASSANT",
          "number": 249
        },
        {
          "name": "ANALYSIS_TYPE_BREAKS_PIN",
          "number": 250
        },
        {
          "name": "ANALYSIS_TYPE_HANGS_PAWN",
          "number": 251
        },
        {
          "name": "ANALYSIS_TYPE_DEVELOPS_AND_PREVENTS_BREAK",
          "number": 252
        },
        {
          "name": "ANALYSIS_TYPE_KING_ROOK_MATE",
          "number": 253
        },
        {
          "name": "ANALYSIS_TYPE_ADDS_ATTACKER",
          "number": 254
        },
        {
          "name": "ANALYSIS_TYPE_KING_QUEEN_MATE",
          "number": 255
        },
        {
          "name": "ANALYSIS_TYPE_PREPARES_TO_DOUBLE_ROOKS",
          "number": 256
        },
        {
          "name": "ANALYSIS_TYPE_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL",
          "number": 257
        },
        {
          "name": "ANALYSIS_TYPE_CONCLUDES_MINORS_FOR_ROOK_PAWN",
          "number": 258
        },
        {
          "name": "ANALYSIS_TYPE_LAUNCHES_MINORITY_ATTACK",
          "number": 259
        },
        {
          "name": "ANALYSIS_TYPE_FIXES_PAWN_STRUCTURE",
          "number": 260
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_LIFT",
          "number": 261
        },
        {
          "name": "ANALYSIS_TYPE_MINORS_FOR_ROOK_PAWN",
          "number": 262
        },
        {
          "name": "ANALYSIS_TYPE_EDGE_PAWN_CHASES_KNIGHT",
          "number": 263
        },
        {
          "name": "ANALYSIS_TYPE_MOUSE_SLIP",
          "number": 264
        },
        {
          "name": "ANALYSIS_TYPE_CARLSBAD_KNIGHT",
          "number": 265
        },
        {
          "name": "ANALYSIS_TYPE_CONCLUDES_ROOK_PAWN_FOR_MINORS",
          "number": 266
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_PAWN_FOR_MINORS",
          "number": 267
        },
        {
          "name": "ANALYSIS_TYPE_CASTLES_INTO_ATTACK",
          "number": 268
        },
        {
          "name": "ANALYSIS_TYPE_PILLSBURY_KNIGHT",
          "number": 269
        },
        {
          "name": "ANALYSIS_TYPE_EQUAL_TRADE_SEQUENCE",
          "number": 270
        },
        {
          "name": "ANALYSIS_TYPE_PASSIVE_RETREAT",
          "number": 271
        },
        {
          "name": "ANALYSIS_TYPE_FORK_IF_CAPTURED",
          "number": 272
        },
        {
          "name": "ANALYSIS_TYPE_INFERIOR_TRADE",
          "number": 273
        },
        {
          "name": "ANALYSIS_TYPE_BAD_TRADE",
          "number": 274
        },
        {
          "name": "ANALYSIS_TYPE_BAD_TRADE_KNIGHT_FOR_BISHOP",
          "number": 275
        },
        {
          "name": "ANALYSIS_TYPE_BAD_TRADE_BISHOP_FOR_KNIGHT",
          "number": 276
        },
        {
          "name": "ANALYSIS_TYPE_FORCED_SACRIFICE_TO_STOP_MATE",
          "number": 277
        },
        {
          "name": "ANALYSIS_TYPE_DOUBLE_CHECK_MATE",
          "number": 278
        },
        {
          "name": "ANALYSIS_TYPE_THREEFOLD_REPETITION_WHEN_WINNING",
          "number": 279
        },
        {
          "name": "ANALYSIS_TYPE_ZWISCHENZUG_BEFORE_RECAPTURE",
          "number": 280
        },
        {
          "name": "ANALYSIS_TYPE_ZWISCHENZUG_BEFORE_THREAT_RESOLUTION",
          "number": 281
        },
        {
          "name": "ANALYSIS_TYPE_ATTRACTION",
          "number": 282
        },
        {
          "name": "ANALYSIS_TYPE_QUEEN_FOR_TWO_ROOKS_GOOD",
          "number": 283
        },
        {
          "name": "ANALYSIS_TYPE_UNNECESSARY_PAWN_MOVE",
          "number": 284
        },
        {
          "name": "ANALYSIS_TYPE_QUEEN_FOR_ROOK_MINOR_GOOD",
          "number": 285
        },
        {
          "name": "ANALYSIS_TYPE_QUEEN_FOR_TWO_ROOKS_BAD",
          "number": 286
        },
        {
          "name": "ANALYSIS_TYPE_QUEEN_FOR_ROOK_MINOR_BAD",
          "number": 287
        },
        {
          "name": "ANALYSIS_TYPE_DECOY",
          "number": 288
        },
        {
          "name": "ANALYSIS_TYPE_QUIET_MOVE",
          "number": 289
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_MINOR_FOR_QUEEN",
          "number": 300
        },
        {
          "name": "ANALYSIS_TYPE_TWO_ROOKS_FOR_QUEEN_GOOD",
          "number": 301
        },
        {
          "name": "ANALYSIS_TYPE_TWO_ROOKS_FOR_QUEEN_BAD",
          "number": 302
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_FOR_MINORS_GOOD",
          "number": 303
        },
        {
          "name": "ANALYSIS_TYPE_ROOK_FOR_MINORS_BAD",
          "number": 304
        },
        {
          "name": "ANALYSIS_TYPE_KINGSIDE_ATTACK",
          "number": 305
        },
        {
          "name": "ANALYSIS_TYPE_QUEENSIDE_ATTACK",
          "number": 306
        },
        {
          "name": "ANALYSIS_TYPE_COMPLETES_DEVELOPMENT",
          "number": 307
        },
        {
          "name": "ANALYSIS_TYPE_ADVANCED_PAWN",
          "number": 308
        },
        {
          "name": "ANALYSIS_TYPE_TRADES_WHILE_DOWN_MATERIAL",
          "number": 309
        },
        {
          "name": "ANALYSIS_TYPE_MANEUVERS_KNIGHT",
          "number": 310
        },
        {
          "name": "ANALYSIS_TYPE_BLOCKS_BISHOP_DEVELOPMENT",
          "number": 311
        },
        {
          "name": "ANALYSIS_TYPE_RESTRICTS_KNIGHT",
          "number": 312
        },
        {
          "name": "ANALYSIS_TYPE_TAKES_SEMI_OPEN_FILE",
          "number": 313
        },
        {
          "name": "ANALYSIS_TYPE_ANTICIPATES_THREAT",
          "number": 314
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 214656.

```text
W5hdGlvbl9lbmdpbmUudjEuQWR2YW5jZWRTdGF0c090aGVySAA6B4KmHQMKAQFCEAoOYWR2YW5jZWRfc3RhdHNiBnByb3RvMw","chesscom/explanation_engine/v1/analysis_type.proto":"CjJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvYW5hbHlzaXNfdHlwZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxKuJcCgxBbmFseXNpc1R5cGUSHQoZQU5BTFlTSVNfVFlQRV9VTlNQRUNJRklFRBAAEhsKF0FOQUxZU0lTX1RZUEVfU1RBTEVNQVRFEAESHAoYQU5BTFlTSVNfVFlQRV9GSUZUWV9NT1ZFEAISHAoYQU5BTFl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17623"></a>
## FND-17623: Full frontend descriptor: chesscom/explanation_engine/v1/circumstance.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/circumstance.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "Circumstance",
      "value": [
        {
          "name": "CIRCUMSTANCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CIRCUMSTANCE_BASE",
          "number": 1
        },
        {
          "name": "CIRCUMSTANCE_THREATENS",
          "number": 2
        },
        {
          "name": "CIRCUMSTANCE_PREVENTS",
          "number": 3
        },
        {
          "name": "CIRCUMSTANCE_PERMITS",
          "number": 4
        },
        {
          "name": "CIRCUMSTANCE_MISSES",
          "number": 5
        },
        {
          "name": "CIRCUMSTANCE_MISSES_SAME",
          "number": 6
        },
        {
          "name": "CIRCUMSTANCE_ENDGAME",
          "number": 7
        },
        {
          "name": "CIRCUMSTANCE_GAME_STATUS",
          "number": 8
        },
        {
          "name": "CIRCUMSTANCE_LEADS_TO",
          "number": 9
        },
        {
          "name": "CIRCUMSTANCE_WINS_MATERIAL",
          "number": 10
        },
        {
          "name": "CIRCUMSTANCE_GAME_OVER",
          "number": 11
        },
        {
          "name": "CIRCUMSTANCE_MATE",
          "number": 12
        },
        {
          "name": "CIRCUMSTANCE_BRILLIANT",
          "number": 13
        },
        {
          "name": "CIRCUMSTANCE_GREAT_FIND",
          "number": 14
        },
        {
          "name": "CIRCUMSTANCE_LONG_THINK",
          "number": 15
        },
        {
          "name": "CIRCUMSTANCE_SHORT_THINK",
          "number": 16
        },
        {
          "name": "CIRCUMSTANCE_TIME_TROUBLE",
          "number": 17
        },
        {
          "name": "CIRCUMSTANCE_FORCES",
          "number": 18
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 230671.

```text
NFTUlfT1BFTl9GSUxFELkCEiUKIEFOQUxZU0lTX1RZUEVfQU5USUNJUEFURVNfVEhSRUFUELoCGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/circumstance.proto":"CjFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY2lyY3Vtc3RhbmNlLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEqpgQKDENpcmN1bXN0YW5jZRIcChhDSVJDVU1TVEFOQ0VfVU5TUEVDSUZJRUQQABIVChFDSVJDVU1TVEFOQ0VfQkFTRRABEhoKFkNJUkNVTVNUQU5DRV9USFJFQVRFTlMQAhIZChVDSVJDVU1TVEFOQ0VfUFJF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17624"></a>
## FND-17624: Full frontend descriptor: chesscom/explanation_engine/v1/bot_move_configuration.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/bot_move_configuration.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "BotMoveConfiguration",
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
          "name": "version",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "settings",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotMoveSettings"
        },
        {
          "name": "additive",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AdditiveConfig",
          "oneof_index": 0
        },
        {
          "name": "nnmult",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NnMultConfig",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "mode"
        }
      ]
    },
    {
      "name": "BotMoveSettings",
      "field": [
        {
          "name": "depth",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "nodes",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 0
        },
        {
          "name": "book",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BookMovesSettings",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "sampling",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SamplingSettings",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "search_limit"
        },
        {
          "name": "_book"
        },
        {
          "name": "_sampling"
        }
      ]
    },
    {
      "name": "AdditiveConfig",
      "field": [
        {
          "name": "n_top_moves",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "n_bad_moves",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "time_taken_multiplier",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "behaviors",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AdditiveBehavior"
        }
      ],
      "options": {}
    },
    {
      "name": "NnMultConfig",
      "field": [
        {
          "name": "n_top_nn_candidates",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "nn",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NnConfig"
        },
        {
          "name": "behaviors",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NnMultBehavior"
        }
      ],
      "options": {}
    },
    {
      "name": "BookMovesSettings",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_count",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "SamplingSettings",
      "field": [
        {
          "name": "probability_threshold",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "options": {}
    },
    {
      "name": "AdditiveBehavior",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "enabled",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "weight",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "rules",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MatcherRule"
        },
        {
          "name": "piece_bonuses",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceBonus"
        },
        {
          "name": "max_eval_drop",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalThreshold",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "max_advantage",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalThreshold",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "context",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotMoveBehaviorContext"
        },
        {
          "name": "legacy_bot",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.LegacyBot",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "nn",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NnConfig",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "coherence",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoherenceConfig",
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_max_eval_drop"
        },
        {
          "name": "_max_advantage"
        },
        {
          "name": "_legacy_bot"
        },
        {
          "name": "_nn"
        },
        {
          "name": "_coherence"
        }
      ]
    },
    {
      "name": "NnMultBehavior",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "enabled",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "weight",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "rules",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NnMultRule"
        },
        {
          "name": "max_eval_drop",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "max_advantage",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "context",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotMoveBehaviorContext"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_max_eval_drop"
        },
        {
          "name": "_max_advantage"
        }
      ]
    },
    {
      "name": "MatcherRule",
      "field": [
        {
          "name": "circumstances",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Circumstance"
        },
        {
          "name": "tags",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.AnalysisType"
        },
        {
          "name": "move_classifications",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "weight",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_weight"
        }
      ]
    },
    {
      "name": "NnMultRule",
      "field": [
        {
          "name": "pieces",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceGate",
          "oneof_index": 0
        },
        {
          "name": "board_events",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MatcherGroup",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "body"
        }
      ]
    },
    {
      "name": "MatcherGroup",
      "field": [
        {
          "name": "matchers",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MatcherRule"
        }
      ],
      "options": {}
    },
    {
      "name": "PieceGate",
      "field": [
        {
          "name": "pieces",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PieceType"
        }
      ],
      "options": {}
    },
    {
      "name": "PieceBonus",
      "field": [
        {
          "name": "piece_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PieceType"
        },
        {
          "name": "bonus",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "options": {}
    },
    {
      "name": "EvalThreshold",
      "field": [
        {
          "name": "cp",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "penalty",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "options": {}
    },
    {
      "name": "EvalRange",
      "field": [
        {
          "name": "min_cp",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "max_cp",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "BotMoveBehaviorContext",
      "field": [
        {
          "name": "game_phase",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.GamePhase",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "eval_range",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EvalRange",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "rules",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MatcherRule"
        },
        {
          "name": "position_shapes",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PositionShape"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_phase"
        },
        {
          "name": "_eval_range"
        }
      ]
    },
    {
      "name": "LegacyBot",
      "field": [
        {
          "name": "rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "personality",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.BotPersonality"
        },
        {
          "name": "weight",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "options": {}
    },
    {
      "name": "NnConfig",
      "field": [
        {
          "name": "arch",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.ModelArch"
        },
        {
          "name": "model",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "weight",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "charm_input_search_depth",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "temperature",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "rating_scale",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "time_taken_multiplier",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "options": {}
    },
    {
      "name": "CoherenceConfig",
      "field": [
        {
          "name": "n_back",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "arch",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.ModelArch"
        },
        {
          "name": "model",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "charm_input_search_depth",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "weight",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "PositionShape",
      "value": [
        {
          "name": "POSITION_SHAPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "POSITION_SHAPE_PASSIVE",
          "number": 1
        },
        {
          "name": "POSITION_SHAPE_ACTIVE",
          "number": 2
        },
        {
          "name": "POSITION_SHAPE_CLOSED",
          "number": 3
        },
        {
          "name": "POSITION_SHAPE_OPEN",
          "number": 4
        },
        {
          "name": "POSITION_SHAPE_SEMI_OPEN",
          "number": 5
        },
        {
          "name": "POSITION_SHAPE_THREATENED",
          "number": 6
        },
        {
          "name": "POSITION_SHAPE_THREATENING",
          "number": 7
        },
        {
          "name": "POSITION_SHAPE_CALM",
          "number": 8
        },
        {
          "name": "POSITION_SHAPE_SHARP",
          "number": 9
        }
      ],
      "options": {}
    },
    {
      "name": "ModelArch",
      "value": [
        {
          "name": "MODEL_ARCH_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MODEL_ARCH_CHARM",
          "number": 1
        },
        {
          "name": "MODEL_ARCH_CHARM_SMALL",
          "number": 2
        },
        {
          "name": "MODEL_ARCH_MAIA",
          "number": 3
        },
        {
          "name": "MODEL_ARCH_MAIA3",
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
  Character offset 231585.

```text
IdChlDSVJDVU1TVEFOQ0VfVElNRV9UUk9VQkxFEBESFwoTQ0lSQ1VNU1RBTkNFX0ZPUkNFUxASGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/bot_move_configuration.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvYm90X21vdmVfY29uZmlndXJhdGlvbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIp8CChRCb3RNb3ZlQ29uZmlndXJhdGlvbhIKCgJpZBgBIAEoCRIMCgRuYW1lGAIgASgJEg8KB3ZlcnNpb24YAyABKAkSQQoIc2V0dGluZ3MYBCABKAsyLy5jaGVzc2NvbS5leH
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17625"></a>
## FND-17625: Full frontend descriptor: chesscom/explanation_engine/v1/feature_charm_inference.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_charm_inference.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CharmInferenceRequest",
      "field": [
        {
          "name": "grv2",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmGameRatingV2Settings",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "tricky",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmTrickySettings",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_grv2"
        },
        {
          "name": "_tricky"
        }
      ]
    },
    {
      "name": "CharmInferenceResponse",
      "field": [
        {
          "name": "results",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmInferenceResult"
        }
      ]
    },
    {
      "name": "CharmGameRatingV2Settings",
      "options": {}
    },
    {
      "name": "CharmTrickySettings",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 237253.

```text
NIQVJNX1NNQUxMEAISEwoPTU9ERUxfQVJDSF9NQUlBEAMSFAoQTU9ERUxfQVJDSF9NQUlBMxAEGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_charm_inference.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9jaGFybV9pbmZlcmVuY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSLMAQoVQ2hhcm1JbmZlcmVuY2VSZXF1ZXN0EkwKBGdydjIYASABKAsyOS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuQ2hhcm1HYW1lUmF0aW5nVjJTZXR0aW5nc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17626"></a>
## FND-17626: Full frontend descriptor: chesscom/explanation_engine/v1/move_details.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/move_details.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "PieceMove",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "piece",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Piece"
        }
      ],
      "options": {}
    },
    {
      "name": "NormalMove",
      "field": [
        {
          "name": "moved_piece",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceMove"
        },
        {
          "name": "captured_piece",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Piece",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_captured_piece"
        }
      ]
    },
    {
      "name": "CastlingMove",
      "field": [
        {
          "name": "king_move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceMove"
        },
        {
          "name": "rook_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceMove"
        }
      ],
      "options": {}
    },
    {
      "name": "PromotionMove",
      "field": [
        {
          "name": "moved_piece",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceMove"
        },
        {
          "name": "captured_piece",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Piece",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "promoted_piece_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PromotionPieceType"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_captured_piece"
        }
      ]
    },
    {
      "name": "EnpassantMove",
      "field": [
        {
          "name": "moved_piece",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceMove"
        },
        {
          "name": "capture_square",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ],
      "options": {}
    },
    {
      "name": "NullMove",
      "options": {}
    },
    {
      "name": "MoveDetails",
      "field": [
        {
          "name": "move_string",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "time_taken_ms",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "regular_move",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NormalMove",
          "oneof_index": 0
        },
        {
          "name": "castling_move",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CastlingMove",
          "oneof_index": 0
        },
        {
          "name": "promotion_move",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PromotionMove",
          "oneof_index": 0
        },
        {
          "name": "en_passant_move",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EnpassantMove",
          "oneof_index": 0
        },
        {
          "name": "null_move",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NullMove",
          "oneof_index": 0
        },
        {
          "name": "moved_color",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "full_move_number",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "game_result",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameResult",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "kind"
        },
        {
          "name": "_game_result"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 237954.

```text
hhcm1HYW1lUmF0aW5nVjJTZXR0aW5nczoHgqYdAwoBASIeChNDaGFybVRyaWNreVNldHRpbmdzOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/move_details.proto":"CjFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbW92ZV9kZXRhaWxzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEijQEKCVBpZWNlTW92ZRInCgRmcm9tGAEgASgOMhkuY2hlc3Njb20uY2hlc3MudjEuU3F1YXJlEiUKAnRvGAIgASgOMhkuY2hlc3Njb20uY2hlc3MudjEuU3F1YXJlEicKBXBpZWNlGAMgASgLMhguY2hlc3Nj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17627"></a>
## FND-17627: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_move_details.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_move_details.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetMoveDetailsRequest",
      "field": [
        {
          "name": "move_notation",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.MoveNotation",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_move_notation"
        }
      ]
    },
    {
      "name": "GetMoveDetailsResponse",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MoveDetails"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 240081.

```text
oZXNzY29tLmNoZXNzLnYxLkdhbWVSZXN1bHRIAYgBAToHgqYdAwoBAUIGCgRraW5kQg4KDF9nYW1lX3Jlc3VsdGIGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_move_details.proto":"Cj1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfbW92ZV9kZXRhaWxzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEibwoVR2V0TW92ZURldGFpbHNSZXF1ZXN0EjsKDW1vdmVfbm90YXRpb24YASABKA4yHy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlTm90YXRpb25IAIgBAToHgqYdAwoBAUIQ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17628"></a>
## FND-17628: Full frontend descriptor: chesscom/explanation_engine/v1/feature_bot_move_from_config.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_bot_move_from_config.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "BotMoveFromConfigRequest",
      "field": [
        {
          "name": "bot_config",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "artifact_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "proto_config",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotMoveConfiguration",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_proto_config"
        }
      ]
    },
    {
      "name": "BotMoveFromConfigResponse",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "suggested_delay_seconds",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_suggested_delay_seconds"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 240562.

```text
G1vdmUYASABKAsyKy5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuTW92ZURldGFpbHM6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_bot_move_from_config.proto":"CkFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9ib3RfbW92ZV9mcm9tX2NvbmZpZy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIrIBChhCb3RNb3ZlRnJvbUNvbmZpZ1JlcXVlc3QSFgoKYm90X2NvbmZpZxgBIAEoCUICGAESEwoLYXJ0aWZhY3RfaWQYAiABKAkSTwoMcHJvdG9fY29uZmln
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17629"></a>
## FND-17629: Full frontend descriptor: chesscom/explanation_engine/v1/feature_load_game_state.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_load_game_state.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LoadGameStateRequest",
      "field": [
        {
          "name": "game_state",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState"
        }
      ],
      "options": {}
    },
    {
      "name": "LoadGameStateResponse",
      "field": [
        {
          "name": "played_line",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 241209.

```text
0ZWRfZGVsYXlfc2Vjb25kcxgCIAEoAUgAiAEBOgeCph0DCgEBQhoKGF9zdWdnZXN0ZWRfZGVsYXlfc2Vjb25kc2IGcHJvdG8z","chesscom/explanation_engine/v1/feature_load_game_state.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sb2FkX2dhbWVfc3RhdGUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJeChRMb2FkR2FtZVN0YXRlUmVxdWVzdBI9CgpnYW1lX3N0YXRlGAEgASgLMikuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkdhbWVTdGF0ZToHgqYdAwoBASJkC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17630"></a>
## FND-17630: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_game_state.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_game_state.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetGameStateRequest",
      "options": {}
    },
    {
      "name": "GetGameStateResponse",
      "field": [
        {
          "name": "game_state",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 241675.

```text
pbmUYASADKAsyLS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZVBvaW50SW5mbzoHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_game_state.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfZ2FtZV9zdGF0ZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIh4KE0dldEdhbWVTdGF0ZVJlcXVlc3Q6B4KmHQMKAQEiXgoUR2V0R2FtZVN0YXRlUmVzcG9uc2USPQoKZ2FtZV9zdGF0ZRgBIAEoCzIpLmNoZXNzY29tLmV4cGxhbmF0aW9uX2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17631"></a>
## FND-17631: Full frontend descriptor: chesscom/explanation_engine/v1/feature_load_coach.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_load_coach.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LoadCoachRequest",
      "field": [
        {
          "name": "text_asset",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TextAsset"
        }
      ],
      "options": {}
    },
    {
      "name": "LoadCoachResponse",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 242046.

```text
V9zdGF0ZRgBIAEoCzIpLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5HYW1lU3RhdGU6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_load_coach.proto":"CjdjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sb2FkX2NvYWNoLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiWgoQTG9hZENvYWNoUmVxdWVzdBI9Cgp0ZXh0X2Fzc2V0GAIgASgLMikuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLlRleHRBc3NldDoHgqYdAwoBASIcChFMb2FkQ29hY2hSZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17632"></a>
## FND-17632: Full frontend descriptor: chesscom/explanation_engine/v1/feature_cee_version.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_cee_version.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CeeVersionRequest",
      "options": {}
    },
    {
      "name": "CeeVersionResponse",
      "field": [
        {
          "name": "cee_version",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.SemanticVersion"
        },
        {
          "name": "cee_git_sha",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "definitions_git_sha",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "uci_version",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.SemanticVersion"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 242399.

```text
uYXRpb25fZW5naW5lLnYxLlRleHRBc3NldDoHgqYdAwoBASIcChFMb2FkQ29hY2hSZXNwb25zZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_cee_version.proto":"CjhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9jZWVfdmVyc2lvbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIhwKEUNlZVZlcnNpb25SZXF1ZXN0OgeCph0DCgEBIr0BChJDZWVWZXJzaW9uUmVzcG9uc2USNQoLY2VlX3ZlcnNpb24YASABKAsyIC5jaGVzc2NvbS5hcGkudjEuU2VtYW50aWNWZXJza
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17633"></a>
## FND-17633: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_bot_chat.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_bot_chat.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetBotChatRequest",
      "field": [
        {
          "name": "bot_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_notation",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.MoveNotation",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "request_hint",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "json",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_move_notation"
        },
        {
          "name": "_request_hint"
        },
        {
          "name": "_json"
        }
      ]
    },
    {
      "name": "GetBotChatResponse",
      "field": [
        {
          "name": "speech",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "hinted_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MoveDetails",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "json",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "trigger_info",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotChatTriggerInfo",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_hinted_move"
        },
        {
          "name": "_json"
        },
        {
          "name": "_trigger_info"
        }
      ]
    },
    {
      "name": "BotChatTriggerInfo",
      "field": [
        {
          "name": "label",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "alternative",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "personality",
          "number": 3,
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
  Character offset 242888.

```text
kSNQoLdWNpX3ZlcnNpb24YBCABKAsyIC5jaGVzc2NvbS5hcGkudjEuU2VtYW50aWNWZXJzaW9uOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_get_bot_chat.proto":"CjljaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfYm90X2NoYXQucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSLJAQoRR2V0Qm90Q2hhdFJlcXVlc3QSEAoIYm90X25hbWUYASABKAkSOwoNbW92ZV9ub3RhdGlvbhgCIAEoDjIfLmNoZXNzY29tLmNoZXNzLnYxLk1vdmVOb3RhdGlvbkgAiAEBEhkK
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17634"></a>
## FND-17634: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetErgonomicGameRequest",
      "field": [
        {
          "name": "game_state",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState",
          "oneof_index": 0
        },
        {
          "name": "pgn",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "starting_game_point",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "game_to_convert"
        }
      ]
    },
    {
      "name": "GetErgonomicGameResponse",
      "field": [
        {
          "name": "game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Game"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 243877.

```text
QoFbGFiZWwYASABKAkSEwoLYWx0ZXJuYXRpdmUYAiABKA0SEwoLcGVyc29uYWxpdHkYAyABKAk6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfZXJnb25vbWljX2dhbWUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSKkAQoXR2V0RXJnb25vbWljR2FtZVJlcXVlc3QSPwoKZ2FtZV9zdGF0ZRgBIAEoCzIpLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5HYW1lU3RhdGVIAB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17635"></a>
## FND-17635: Full frontend descriptor: chesscom/explanation_engine/v1/simple_threat.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/simple_threat.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SimpleThreat",
      "field": [
        {
          "name": "threat_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.ThreatType"
        },
        {
          "name": "threatened_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "see_value",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Score"
        },
        {
          "name": "score",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Score"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "ThreatType",
      "value": [
        {
          "name": "THREAT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "THREAT_TYPE_CHECK",
          "number": 1
        },
        {
          "name": "THREAT_TYPE_CAPTURE",
          "number": 2
        },
        {
          "name": "THREAT_TYPE_MATE",
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
  Character offset 244410.

```text
ub21pY0dhbWVSZXNwb25zZRIlCgRnYW1lGAEgASgLMhcuY2hlc3Njb20uY2hlc3MudjEuR2FtZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/simple_threat.proto":"CjJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc2ltcGxlX3RocmVhdC5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIuEBCgxTaW1wbGVUaHJlYXQSPwoLdGhyZWF0X3R5cGUYASABKA4yKi5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuVGhyZWF0VHlwZRIwCg90aHJlYXRlbmVkX21vdmUYAiABKAsyFy5jaGVzc2N
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17636"></a>
## FND-17636: Full frontend descriptor: chesscom/explanation_engine/v1/feature_add_evaluations.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_add_evaluations.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "AddEvaluationsRequest",
      "field": [
        {
          "name": "evaluations",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Evaluation"
        },
        {
          "name": "skip_eval_normalization",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "AddEvaluationsResponse",
      "field": [
        {
          "name": "added_variation_start_game_points",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 245056.

```text
V9DSEVDSxABEhcKE1RIUkVBVF9UWVBFX0NBUFRVUkUQAhIUChBUSFJFQVRfVFlQRV9NQVRFEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_add_evaluations.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9hZGRfZXZhbHVhdGlvbnMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJtChVBZGRFdmFsdWF0aW9uc1JlcXVlc3QSMwoLZXZhbHVhdGlvbnMYASADKAsyHi5jaGVzc2NvbS5lbmdpbmUudjEuRXZhbHVhdGlvbhIfChdza2lwX2V2YWxfbm9ybWFsa
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17637"></a>
## FND-17637: Full frontend descriptor: chesscom/explanation_engine/v1/feature_simple_threats.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_simple_threats.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SimpleThreatsRequest",
      "field": [
        {
          "name": "threats_limit",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "SimpleThreatsResponse",
      "field": [
        {
          "name": "threats",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SimpleThreat"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 245498.

```text
BZGRFdmFsdWF0aW9uc1Jlc3BvbnNlEikKIWFkZGVkX3ZhcmlhdGlvbl9zdGFydF9nYW1lX3BvaW50cxgBIAMoBWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_simple_threats.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9zaW1wbGVfdGhyZWF0cy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIjYKFFNpbXBsZVRocmVhdHNSZXF1ZXN0EhUKDXRocmVhdHNfbGltaXQYASABKAU6B4KmHQMKAQEiXwoVU2ltcGxlVGhyZWF0c1Jlc3BvbnNlEj0KB3RocmVhdHMYASADKAsyLC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17638"></a>
## FND-17638: Full frontend descriptor: chesscom/explanation_engine/v1/feature_analysis_annotations.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_analysis_annotations.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "AnalysisAnnotationsRequest",
      "field": [
        {
          "name": "stream_results",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "enable_pv_classifications",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "AnalysisAnnotationsResponse",
      "field": [
        {
          "name": "move_classifications",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassificationResponse"
        },
        {
          "name": "threats",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SimpleThreatsResponse"
        },
        {
          "name": "progress",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 245902.

```text
VhdHMYASADKAsyLC5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuU2ltcGxlVGhyZWF0OgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_analysis_annotations.proto":"CkFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9hbmFseXNpc19hbm5vdGF0aW9ucy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxImAKGkFuYWx5c2lzQW5ub3RhdGlvbnNSZXF1ZXN0EhYKDnN0cmVhbV9yZXN1bHRzGAEgASgIEiEKGWVuYWJsZV9wdl9jbGFzc2lmaWNhdGlvbnMYAiABKAg6
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17639"></a>
## FND-17639: Full frontend descriptor: chesscom/explanation_engine/v1/feature_bot_config_resources.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_bot_config_resources.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "BotConfigResourcesRequest",
      "field": [
        {
          "name": "bot_config",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "artifact_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "proto_config",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotMoveConfiguration",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_proto_config"
        }
      ]
    },
    {
      "name": "BookResource",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_count",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "NnResource",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "BotConfigResourcesResponse",
      "field": [
        {
          "name": "book",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BookResource",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "nn",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NnResource",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_book"
        },
        {
          "name": "_nn"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 246541.

```text
uYXRpb25fZW5naW5lLnYxLlNpbXBsZVRocmVhdHNSZXNwb25zZRIQCghwcm9ncmVzcxgDIAEoAjoHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_bot_config_resources.proto":"CkFjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9ib3RfY29uZmlnX3Jlc291cmNlcy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIrMBChlCb3RDb25maWdSZXNvdXJjZXNSZXF1ZXN0EhYKCmJvdF9jb25maWcYASABKAlCAhgBEhMKC2FydGlmYWN0X2lkGAIgASgJEk8KDHByb3RvX2NvbmZp
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17640"></a>
## FND-17640: Full frontend descriptor: chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "ConvertToProtoMovesRequest",
      "field": [
        {
          "name": "move_notation",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.MoveNotation"
        },
        {
          "name": "initial_fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "moves_to_convert",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "ConvertToProtoMovesResponse",
      "field": [
        {
          "name": "moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 247366.

```text
20uZXhwbGFuYXRpb25fZW5naW5lLnYxLk5uUmVzb3VyY2VIAYgBAToHgqYdAwoBAUIHCgVfYm9va0IFCgNfbm5iBnByb3RvMw","chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto":"CkNjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9jb252ZXJ0X3RvX3Byb3RvX21vdmVzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEijAEKGkNvbnZlcnRUb1Byb3RvTW92ZXNSZXF1ZXN0EjYKDW1vdmVfbm90YXRpb24YASABKA4yHy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlTm90YXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17641"></a>
## FND-17641: Full frontend descriptor: chesscom/explanation_engine/v1/feature_game_phase_transitions.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_game_phase_transitions.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GamePhaseTransitionsRequest",
      "field": [
        {
          "name": "starting_game_point",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "game_phase_version",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseVersion",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_starting_game_point"
        },
        {
          "name": "_game_phase_version"
        }
      ]
    },
    {
      "name": "GamePhaseTransitionsResponse",
      "field": [
        {
          "name": "game_phase_transition",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseTransitions"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 247882.

```text
90b01vdmVzUmVzcG9uc2USJgoFbW92ZXMYASADKAsyFy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_game_phase_transitions.proto":"CkNjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nYW1lX3BoYXNlX3RyYW5zaXRpb25zLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiwQEKG0dhbWVQaGFzZVRyYW5zaXRpb25zUmVxdWVzdBIgChNzdGFydGluZ19nYW1lX3BvaW50GAEgASgFSACIAQESUQoSZ2FtZV9waGFzZV92ZXJzaW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17642"></a>
## FND-17642: Full frontend descriptor: chesscom/explanation_engine/v1/feature_game_point_info.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_game_point_info.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GamePointInfoRequest",
      "options": {}
    },
    {
      "name": "GamePointInfoResponse",
      "field": [
        {
          "name": "game_point_info",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 248518.

```text
l0aW9uGAEgASgLMjQuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkdhbWVQaGFzZVRyYW5zaXRpb25zYgZwcm90bzM","chesscom/explanation_engine/v1/feature_game_point_info.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nYW1lX3BvaW50X2luZm8ucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSIfChRHYW1lUG9pbnRJbmZvUmVxdWVzdDoHgqYdAwoBASJoChVHYW1lUG9pbnRJbmZvUmVzcG9uc2USRgoPZ2FtZV9wb2ludF9pbmZvGAEgASgLMi0uY2hlc3Njb20uZXhwb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17643"></a>
## FND-17643: Full frontend descriptor: chesscom/explanation_engine/v1/feature_game_review.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_game_review.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GameReviewRequest",
      "field": [
        {
          "name": "stats",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AdvancedStatsForGame",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "starting_game_point",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "uci_options",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry"
        },
        {
          "name": "include_train_takeaways",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "can_access_locked_takeaways",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "nested_type": [
        {
          "name": "UciOptionsEntry",
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
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_stats"
        },
        {
          "name": "_starting_game_point"
        }
      ]
    },
    {
      "name": "GameReviewResponse",
      "field": [
        {
          "name": "game_review",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReview"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 248906.

```text
mZvGAEgASgLMi0uY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkdhbWVQb2ludEluZm86B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_game_review.proto":"CjhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nYW1lX3Jldmlldy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIvsCChFHYW1lUmV2aWV3UmVxdWVzdBJICgVzdGF0cxgBIAEoCzI0LmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5BZHZhbmNlZFN0YXRzRm9yR2FtZUgAiAEBEiAKE3N0YXJ0a
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17644"></a>
## FND-17644: Full frontend descriptor: chesscom/explanation_engine/v1/feature_game_tree.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_game_tree.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GameTreeRequest"
    },
    {
      "name": "GameTreeResponse",
      "field": [
        {
          "name": "game_point_info",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 249736.

```text
yZXZpZXcYASABKAsyKi5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZVJldmlldzoHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_game_tree.proto":"CjZjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nYW1lX3RyZWUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSIRCg9HYW1lVHJlZVJlcXVlc3QiWgoQR2FtZVRyZWVSZXNwb25zZRJGCg9nYW1lX3BvaW50X2luZm8YASADKAsyLS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZVBvaW50SW5
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17645"></a>
## FND-17645: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_bot_move.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_bot_move.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetBotMoveRequest",
      "field": [
        {
          "name": "options",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.BotOptions"
        },
        {
          "name": "engine",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.BotEngine"
        }
      ],
      "options": {}
    },
    {
      "name": "GetBotMoveResponse",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 250072.

```text
lX3BvaW50X2luZm8YASADKAsyLS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZVBvaW50SW5mb2IGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_bot_move.proto":"CjljaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfYm90X21vdmUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSKUAQoRR2V0Qm90TW92ZVJlcXVlc3QSOwoHb3B0aW9ucxgCIAEoCzIqLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Cb3RPcHRpb25zEjkKBmVuZ2luZRgBIAEoDjIpLmNo
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17646"></a>
## FND-17646: Full frontend descriptor: chesscom/explanation_engine/v1/speech_debug_info.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/speech_debug_info.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SpeechDebugInfo",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "botchat_triggers",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "board_events",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "selected_keys",
          "number": 4,
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
  Character offset 250562.

```text
V0Qm90TW92ZVJlc3BvbnNlEiUKBG1vdmUYASABKAsyFy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/speech_debug_info.proto":"CjZjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc3BlZWNoX2RlYnVnX2luZm8ucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJxCg9TcGVlY2hEZWJ1Z0luZm8SDgoGc291cmNlGAEgASgJEhgKEGJvdGNoYXRfdHJpZ2dlcnMYAiADKAkSFAoMYm9hcmRfZXZlbnRzGAMgAygJEhUKDXNlbGVjdGVkX2tleXMYBCADKAk6B4K
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17647"></a>
## FND-17647: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_coach_chat.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_coach_chat.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetCoachChatRequest",
      "options": {}
    },
    {
      "name": "GetCoachChatResponse",
      "field": [
        {
          "name": "debug_info",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChatDebugInfo",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "speech",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "retry_mistake",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RetryMistake",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "flip_board_mistake",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.FlipBoardMistake",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "skills_earned",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SkillsPosition"
        },
        {
          "name": "coach_emotion",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.CoachEmotion",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "retry_miss",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RetryMiss",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_debug_info"
        },
        {
          "name": "_speech"
        },
        {
          "name": "_retry_mistake"
        },
        {
          "name": "_flip_board_mistake"
        },
        {
          "name": "_coach_emotion"
        },
        {
          "name": "_retry_miss"
        }
      ]
    },
    {
      "name": "RetryMistake",
      "field": [
        {
          "name": "speech",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "arrows_and_squares",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
        },
        {
          "name": "keep_playing_choice",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        },
        {
          "name": "retry_choice",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        },
        {
          "name": "ply_until_cooldown",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "board_event",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "FlipBoardMistake",
      "field": [
        {
          "name": "refutation_move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "arrows_and_squares",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
        },
        {
          "name": "board_event",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "offer_speech",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "switch_sides_choice",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        },
        {
          "name": "decline_choice",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        },
        {
          "name": "success_speech",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "failure_speech",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "failure_almost_speech",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "continue_after_flip_choice",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        }
      ],
      "options": {}
    },
    {
      "name": "RetryMiss",
      "field": [
        {
          "name": "speech",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "arrows_and_squares",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
        },
        {
          "name": "keep_playing_choice",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        },
        {
          "name": "retry_choice",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
        },
        {
          "name": "board_event",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "attempt_speech",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "failure_speech",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "success_speech",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "success_moves",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    },
    {
      "name": "CoachChoice",
      "field": [
        {
          "name": "button_text",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "response_speech",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "response_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_response_move"
        }
      ]
    },
    {
      "name": "CoachChatDebugInfo",
      "field": [
        {
          "name": "speech_debug_info",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SpeechDebugInfo"
        },
        {
          "name": "retry_mistake_debug_info",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RetryMistakeDebugInfo"
        },
        {
          "name": "used_botchat_triggers",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "used_board_events",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "flip_board_mistake_debug_info",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo"
        }
      ],
      "options": {}
    },
    {
      "name": "RetryMistakeDebugInfo",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "player_is_winning",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "ply_until_cooldown",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "FlipBoardMistakeDebugInfo",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "ply_until_flip_board_cooldown",
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
  Character offset 250904.

```text
2dlcnMYAiADKAkSFAoMYm9hcmRfZXZlbnRzGAMgAygJEhUKDXNlbGVjdGVkX2tleXMYBCADKAk6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_get_coach_chat.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfY29hY2hfY2hhdC5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIh4KE0dldENvYWNoQ2hhdFJlcXVlc3Q6B4KmHQMKAQEi/wQKFEdldENvYWNoQ2hhdFJlc3BvbnNlEksKCmRlYnVnX2luZm8YASABKAsyMi5jaGVzc2NvbS5leHBsYW5hdGlvbl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.
