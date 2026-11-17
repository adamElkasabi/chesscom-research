# native_interfaces — findings 1801–1900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14460"></a>
## FND-14460: chesscom.explanation_engine.v1.PlayedMove.coach_emotion = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayedMove",
  "name": "coach_emotion",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.CoachEmotion",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14461"></a>
## FND-14461: chesscom.explanation_engine.v1.PlayedMove.skills_earned = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayedMove",
  "name": "skills_earned",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.SkillsPosition",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14462"></a>
## FND-14462: chesscom.explanation_engine.v1.PlayedMove.explain_line = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayedMove",
  "name": "explain_line",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.PlayedMove",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14463"></a>
## FND-14463: chesscom.explanation_engine.v1.PlayedMove.best_next_move = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayedMove",
  "name": "best_next_move",
  "number": 8,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": "_best_next_move",
  "proto3_optional": true,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14464"></a>
## FND-14464: Native message: chesscom.explanation_engine.v1.Move

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14465"></a>
## FND-14465: chesscom.explanation_engine.v1.Move.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Move",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14466"></a>
## FND-14466: chesscom.explanation_engine.v1.Move.move_classification = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Move",
  "name": "move_classification",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14467"></a>
## FND-14467: chesscom.explanation_engine.v1.Move.score = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Move",
  "name": "score",
  "number": 4,
  "type": ".chesscom.engine.v1.Score",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14468"></a>
## FND-14468: chesscom.explanation_engine.v1.Move.speech = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Move",
  "name": "speech",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14469"></a>
## FND-14469: chesscom.explanation_engine.v1.Move.show_moves_buttons = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Move",
  "name": "show_moves_buttons",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.ShowMoves",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14470"></a>
## FND-14470: chesscom.explanation_engine.v1.Move.board_markings = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Move",
  "name": "board_markings",
  "number": 7,
  "type": ".chesscom.chess.v1.BoardMarkings",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14471"></a>
## FND-14471: Native message: chesscom.explanation_engine.v1.ShowMoves

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14472"></a>
## FND-14472: chesscom.explanation_engine.v1.ShowMoves.moves_to_show = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ShowMoves",
  "name": "moves_to_show",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14473"></a>
## FND-14473: chesscom.explanation_engine.v1.ShowMoves.show_text = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ShowMoves",
  "name": "show_text",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14474"></a>
## FND-14474: chesscom.explanation_engine.v1.ShowMoves.hide_text = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ShowMoves",
  "name": "hide_text",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0997",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0997** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96541d88d75774af124e4734c877ab1e40bfde08b4cf2561fbe92a82d046aa6a.bin)

**Source references:** SRC-0997, SRC-1758  
**URL references:** None independently associated  
**Related findings:** FND-14399, FND-14400, FND-14401

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14475"></a>
## FND-14475: Native message: chesscom.explanation_engine.v1.GameSettings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameSettings",
  "field": [
    {
      "name": "search_settings",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SearchSettings",
      "oneof_index": 0
    },
    {
      "name": "game_review_search_settings",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
      "oneof_index": 0
    },
    {
      "name": "preset",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.SearchPreset",
      "oneof_index": 0
    },
    {
      "name": "user_color",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "locale",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.Locale",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "game_phase_version",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.GamePhaseVersion",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "game_analysis_speech_version",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.GameAnalysisSpeechVersion",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "move_classification_version",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassificationVersion",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "force_disable_internal_engine_searches",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 6,
      "proto3_optional": true
    },
    {
      "name": "enable_skills",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 7,
      "proto3_optional": true
    },
    {
      "name": "enabled_feature_flags",
      "number": 11,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "feature_flag_config",
      "number": 12,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry"
    }
  ],
  "nested_type": [
    {
      "name": "FeatureFlagConfigEntry",
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
  "oneof_decl": [
    {
      "name": "search"
    },
    {
      "name": "_user_color"
    },
    {
      "name": "_locale"
    },
    {
      "name": "_game_phase_version"
    },
    {
      "name": "_game_analysis_speech_version"
    },
    {
      "name": "_move_classification_version"
    },
    {
      "name": "_force_disable_internal_engine_searches"
    },
    {
      "name": "_enable_skills"
    }
  ],
  "reserved_range": [
    {
      "start": 1,
      "end": 2
    },
    {
      "start": 2,
      "end": 3
    }
  ]
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14476"></a>
## FND-14476: chesscom.explanation_engine.v1.GameSettings.search_settings = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "search_settings",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.SearchSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14477"></a>
## FND-14477: chesscom.explanation_engine.v1.GameSettings.game_review_search_settings = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "game_review_search_settings",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14478"></a>
## FND-14478: chesscom.explanation_engine.v1.GameSettings.preset = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "preset",
  "number": 13,
  "type": ".chesscom.explanation_engine.v1.SearchPreset",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14479"></a>
## FND-14479: chesscom.explanation_engine.v1.GameSettings.user_color = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "user_color",
  "number": 3,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": "_user_color",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14480"></a>
## FND-14480: chesscom.explanation_engine.v1.GameSettings.locale = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "locale",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.Locale",
  "label": "LABEL_OPTIONAL",
  "oneof": "_locale",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14481"></a>
## FND-14481: chesscom.explanation_engine.v1.GameSettings.game_phase_version = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "game_phase_version",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.GamePhaseVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_phase_version",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14482"></a>
## FND-14482: chesscom.explanation_engine.v1.GameSettings.game_analysis_speech_version = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "game_analysis_speech_version",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.GameAnalysisSpeechVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_analysis_speech_version",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14483"></a>
## FND-14483: chesscom.explanation_engine.v1.GameSettings.move_classification_version = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "move_classification_version",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.MoveClassificationVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move_classification_version",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14484"></a>
## FND-14484: chesscom.explanation_engine.v1.GameSettings.force_disable_internal_engine_searches = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "force_disable_internal_engine_searches",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_force_disable_internal_engine_searches",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14485"></a>
## FND-14485: chesscom.explanation_engine.v1.GameSettings.enable_skills = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "enable_skills",
  "number": 14,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_enable_skills",
  "proto3_optional": true,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14486"></a>
## FND-14486: chesscom.explanation_engine.v1.GameSettings.enabled_feature_flags = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "enabled_feature_flags",
  "number": 11,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14487"></a>
## FND-14487: chesscom.explanation_engine.v1.GameSettings.feature_flag_config = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings",
  "name": "feature_flag_config",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14488"></a>
## FND-14488: Native message: chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "FeatureFlagConfigEntry",
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

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14489"></a>
## FND-14489: chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14490"></a>
## FND-14490: chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry",
  "name": "value",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14491"></a>
## FND-14491: Native message: chesscom.explanation_engine.v1.SearchSettings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SearchSettings",
  "field": [
    {
      "name": "search_parameters",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SearchParameters"
    },
    {
      "name": "null_move_search_parameters",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SearchParameters"
    }
  ]
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14492"></a>
## FND-14492: chesscom.explanation_engine.v1.SearchSettings.search_parameters = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchSettings",
  "name": "search_parameters",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14493"></a>
## FND-14493: chesscom.explanation_engine.v1.SearchSettings.null_move_search_parameters = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchSettings",
  "name": "null_move_search_parameters",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.SearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0998",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0998** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_settings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d38e4622d2e6052489aef9b253c0b6fad0c7a40e0ac0deefc1bce4c41b598cc1.bin)

**Source references:** SRC-0998, SRC-1863  
**URL references:** None independently associated  
**Related findings:** FND-14475, FND-14476, FND-14477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14494"></a>
## FND-14494: Native message: chesscom.explanation_engine.v1.GameState

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameState",
  "field": [
    {
      "name": "game_state_version",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.api.v1.SemanticVersion"
    },
    {
      "name": "game_tree",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameTree",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "game_settings",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameSettings"
    },
    {
      "name": "game_metadata",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMetadata"
    },
    {
      "name": "default_eval_source_engine",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Engine"
    },
    {
      "name": "coach_state",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachState"
    },
    {
      "name": "charm_inferences",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState.CharmInferencesEntry",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "annotations",
      "number": 8,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState.AnnotationsEntry"
    },
    {
      "name": "compact_charm_inferences",
      "number": 9,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "compact_game_tree",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CompactGameTree"
    },
    {
      "name": "quantized_charm_inferences",
      "number": 11,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "charm_inference_codes",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CharmInferenceCodes"
    }
  ],
  "nested_type": [
    {
      "name": "CharmInferencesEntry",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SimpleCharmInferences"
        }
      ],
      "options": {
        "map_entry": true
      }
    },
    {
      "name": "AnnotationsEntry",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MoveAnnotation"
        }
      ],
      "options": {
        "map_entry": true
      }
    },
    {
      "name": "CompactCharmInferencesEntry",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CompactCharmInferences"
        }
      ],
      "options": {
        "map_entry": true
      }
    },
    {
      "name": "QuantizedCharmInferencesEntry",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CompactCharmInferences"
        }
      ],
      "options": {
        "map_entry": true
      }
    }
  ]
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14495"></a>
## FND-14495: chesscom.explanation_engine.v1.GameState.game_state_version = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "game_state_version",
  "number": 1,
  "type": ".chesscom.api.v1.SemanticVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14496"></a>
## FND-14496: chesscom.explanation_engine.v1.GameState.game_tree = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "game_tree",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GameTree",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14497"></a>
## FND-14497: chesscom.explanation_engine.v1.GameState.game_settings = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "game_settings",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GameSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14498"></a>
## FND-14498: chesscom.explanation_engine.v1.GameState.game_metadata = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "game_metadata",
  "number": 4,
  "type": ".chesscom.chess.v1.GameMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14499"></a>
## FND-14499: chesscom.explanation_engine.v1.GameState.default_eval_source_engine = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "default_eval_source_engine",
  "number": 5,
  "type": ".chesscom.engine.v1.Engine",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14500"></a>
## FND-14500: chesscom.explanation_engine.v1.GameState.coach_state = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "coach_state",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.CoachState",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14501"></a>
## FND-14501: chesscom.explanation_engine.v1.GameState.charm_inferences = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "charm_inferences",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.GameState.CharmInferencesEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14502"></a>
## FND-14502: chesscom.explanation_engine.v1.GameState.annotations = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "annotations",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.GameState.AnnotationsEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14503"></a>
## FND-14503: chesscom.explanation_engine.v1.GameState.compact_charm_inferences = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "compact_charm_inferences",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14504"></a>
## FND-14504: chesscom.explanation_engine.v1.GameState.compact_game_tree = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "compact_game_tree",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1.CompactGameTree",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14505"></a>
## FND-14505: chesscom.explanation_engine.v1.GameState.quantized_charm_inferences = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "quantized_charm_inferences",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14506"></a>
## FND-14506: chesscom.explanation_engine.v1.GameState.charm_inference_codes = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState",
  "name": "charm_inference_codes",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1.CharmInferenceCodes",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14507"></a>
## FND-14507: Native message: chesscom.explanation_engine.v1.GameState.CharmInferencesEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmInferencesEntry",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "value",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SimpleCharmInferences"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14508"></a>
## FND-14508: chesscom.explanation_engine.v1.GameState.CharmInferencesEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.CharmInferencesEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14509"></a>
## FND-14509: chesscom.explanation_engine.v1.GameState.CharmInferencesEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.CharmInferencesEntry",
  "name": "value",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.SimpleCharmInferences",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14510"></a>
## FND-14510: Native message: chesscom.explanation_engine.v1.GameState.AnnotationsEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AnnotationsEntry",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "value",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveAnnotation"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14511"></a>
## FND-14511: chesscom.explanation_engine.v1.GameState.AnnotationsEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.AnnotationsEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14512"></a>
## FND-14512: chesscom.explanation_engine.v1.GameState.AnnotationsEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.AnnotationsEntry",
  "name": "value",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveAnnotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14513"></a>
## FND-14513: Native message: chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CompactCharmInferencesEntry",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "value",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CompactCharmInferences"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14514"></a>
## FND-14514: chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14515"></a>
## FND-14515: chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry",
  "name": "value",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.CompactCharmInferences",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14516"></a>
## FND-14516: Native message: chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "QuantizedCharmInferencesEntry",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "value",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CompactCharmInferences"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14517"></a>
## FND-14517: chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14518"></a>
## FND-14518: chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry",
  "name": "value",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.CompactCharmInferences",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14519"></a>
## FND-14519: Native message: chesscom.explanation_engine.v1.GameTree

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameTree",
  "field": [
    {
      "name": "nodes",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameTreeNode"
    }
  ]
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14520"></a>
## FND-14520: chesscom.explanation_engine.v1.GameTree.nodes = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTree",
  "name": "nodes",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameTreeNode",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14521"></a>
## FND-14521: Native message: chesscom.explanation_engine.v1.GameTreeNode

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameTreeNode",
  "field": [
    {
      "name": "initial_fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    },
    {
      "name": "legal_move_index",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0
    },
    {
      "name": "is_played",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "is_explicitly_unscored",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "score",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_SINT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "depth",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_SINT32",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "additional_children",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_SINT32"
    },
    {
      "name": "time_on_clock_deciseconds",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "score_is_weak",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "manually_added",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ],
  "oneof_decl": [
    {
      "name": "board_state"
    },
    {
      "name": "_score"
    },
    {
      "name": "_depth"
    },
    {
      "name": "_time_on_clock_deciseconds"
    }
  ]
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14522"></a>
## FND-14522: chesscom.explanation_engine.v1.GameTreeNode.initial_fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "initial_fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "board_state",
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14523"></a>
## FND-14523: chesscom.explanation_engine.v1.GameTreeNode.legal_move_index = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "legal_move_index",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "board_state",
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14524"></a>
## FND-14524: chesscom.explanation_engine.v1.GameTreeNode.is_played = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "is_played",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14525"></a>
## FND-14525: chesscom.explanation_engine.v1.GameTreeNode.is_explicitly_unscored = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "is_explicitly_unscored",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14526"></a>
## FND-14526: chesscom.explanation_engine.v1.GameTreeNode.score = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "score",
  "number": 5,
  "type": "TYPE_SINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_score",
  "proto3_optional": true,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14527"></a>
## FND-14527: chesscom.explanation_engine.v1.GameTreeNode.depth = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "depth",
  "number": 6,
  "type": "TYPE_SINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_depth",
  "proto3_optional": true,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14528"></a>
## FND-14528: chesscom.explanation_engine.v1.GameTreeNode.additional_children = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "additional_children",
  "number": 7,
  "type": "TYPE_SINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14529"></a>
## FND-14529: chesscom.explanation_engine.v1.GameTreeNode.time_on_clock_deciseconds = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "time_on_clock_deciseconds",
  "number": 8,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_on_clock_deciseconds",
  "proto3_optional": true,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14530"></a>
## FND-14530: chesscom.explanation_engine.v1.GameTreeNode.score_is_weak = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "score_is_weak",
  "number": 9,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14531"></a>
## FND-14531: chesscom.explanation_engine.v1.GameTreeNode.manually_added = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeNode",
  "name": "manually_added",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14532"></a>
## FND-14532: Native message: chesscom.explanation_engine.v1.CompactGameTree

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CompactGameTree",
  "field": [
    {
      "name": "initial_fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "legal_move_indexes",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "node_flags",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    },
    {
      "name": "additional_children",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_SINT32"
    },
    {
      "name": "scores",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_SINT32"
    },
    {
      "name": "depths",
      "number": 6,
      "label": "LABEL_REPEATED",
      "type": "TYPE_SINT32"
    },
    {
      "name": "clocks_deciseconds",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    }
  ]
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14533"></a>
## FND-14533: chesscom.explanation_engine.v1.CompactGameTree.initial_fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "initial_fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14534"></a>
## FND-14534: chesscom.explanation_engine.v1.CompactGameTree.legal_move_indexes = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "legal_move_indexes",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14535"></a>
## FND-14535: chesscom.explanation_engine.v1.CompactGameTree.node_flags = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "node_flags",
  "number": 3,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14536"></a>
## FND-14536: chesscom.explanation_engine.v1.CompactGameTree.additional_children = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "additional_children",
  "number": 4,
  "type": "TYPE_SINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14537"></a>
## FND-14537: chesscom.explanation_engine.v1.CompactGameTree.scores = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "scores",
  "number": 5,
  "type": "TYPE_SINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14538"></a>
## FND-14538: chesscom.explanation_engine.v1.CompactGameTree.depths = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "depths",
  "number": 6,
  "type": "TYPE_SINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14539"></a>
## FND-14539: chesscom.explanation_engine.v1.CompactGameTree.clocks_deciseconds = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactGameTree",
  "name": "clocks_deciseconds",
  "number": 7,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14540"></a>
## FND-14540: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14541"></a>
## FND-14541: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_PLAYED = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_PLAYED",
  "number": 1,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14542"></a>
## FND-14542: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_EXPLICITLY_UNSCORED = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_EXPLICITLY_UNSCORED",
  "number": 2,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14543"></a>
## FND-14543: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_SCORE_IS_WEAK = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_SCORE_IS_WEAK",
  "number": 4,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14544"></a>
## FND-14544: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_MANUALLY_ADDED = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_MANUALLY_ADDED",
  "number": 8,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14545"></a>
## FND-14545: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_SCORE = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_HAS_SCORE",
  "number": 16,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14546"></a>
## FND-14546: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_DEPTH = 32

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_HAS_DEPTH",
  "number": 32,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14547"></a>
## FND-14547: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_HAS_ADDITIONAL_CHILDREN",
  "number": 64,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14548"></a>
## FND-14548: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_CLOCK = 128

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NodeFlag",
  "name": "NODE_FLAG_HAS_CLOCK",
  "number": 128,
  "source_id": "SRC-0999",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0999** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0dd1f86be91dff5a210a53c00da73e13bafa00891810fc347ebcfec60f2c09b.bin)

**Source references:** SRC-0999, SRC-1841  
**URL references:** None independently associated  
**Related findings:** FND-14494, FND-14495, FND-14496

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14549"></a>
## FND-14549: Native message: chesscom.explanation_engine.v1.GameStateSpec

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameStateSpec",
  "field": [
    {
      "name": "new_game_request",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.NewGameRequest"
    },
    {
      "name": "run_search_request",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RunSearchRequest"
    },
    {
      "name": "engine_type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Engine"
    }
  ]
}

### Evidence

- **SRC-1000** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state_spec.proto.bin` — [preserved redacted evidence](../evidence/descriptors/285ef45b536d44d62122daf5f2cc34048816f7f61352a89dceeae33ff4e0dfdb.bin)

**Source references:** SRC-1000, SRC-1800  
**URL references:** None independently associated  
**Related findings:** FND-14550, FND-14551

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14550"></a>
## FND-14550: chesscom.explanation_engine.v1.GameStateSpec.new_game_request = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameStateSpec",
  "name": "new_game_request",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.NewGameRequest",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1000",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1000** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state_spec.proto.bin` — [preserved redacted evidence](../evidence/descriptors/285ef45b536d44d62122daf5f2cc34048816f7f61352a89dceeae33ff4e0dfdb.bin)

**Source references:** SRC-1000, SRC-1800  
**URL references:** None independently associated  
**Related findings:** FND-14549, FND-14551

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14551"></a>
## FND-14551: chesscom.explanation_engine.v1.GameStateSpec.run_search_request = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameStateSpec",
  "name": "run_search_request",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.RunSearchRequest",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1000",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1000** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state_spec.proto.bin` — [preserved redacted evidence](../evidence/descriptors/285ef45b536d44d62122daf5f2cc34048816f7f61352a89dceeae33ff4e0dfdb.bin)

**Source references:** SRC-1000, SRC-1800  
**URL references:** None independently associated  
**Related findings:** FND-14549, FND-14550

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14552"></a>
## FND-14552: chesscom.explanation_engine.v1.GameStateSpec.engine_type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameStateSpec",
  "name": "engine_type",
  "number": 3,
  "type": ".chesscom.engine.v1.Engine",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1000",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1000** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_state_spec.proto.bin` — [preserved redacted evidence](../evidence/descriptors/285ef45b536d44d62122daf5f2cc34048816f7f61352a89dceeae33ff4e0dfdb.bin)

**Source references:** SRC-1000, SRC-1800  
**URL references:** None independently associated  
**Related findings:** FND-14549, FND-14550, FND-14551

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14553"></a>
## FND-14553: Native message: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureAdvancedStatsDatapointRequest",
  "field": [
    {
      "name": "heartbeat_interval_seconds",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "ignore_missing_move_timestamps",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14554"></a>
## FND-14554: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointRequest.heartbeat_interval_seconds = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointRequest",
  "name": "heartbeat_interval_seconds",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14555"></a>
## FND-14555: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointRequest.ignore_missing_move_timestamps = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointRequest",
  "name": "ignore_missing_move_timestamps",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14556"></a>
## FND-14556: Native message: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureAdvancedStatsDatapointResponse",
  "field": [
    {
      "name": "white_advanced_stats_datapoint",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.stats.v1.PlayerAdvancedStatsDatapoint"
    },
    {
      "name": "black_advanced_stats_datapoint",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.stats.v1.PlayerAdvancedStatsDatapoint"
    },
    {
      "name": "is_heartbeat",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "white_stat_examples",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.stats.v1.AdvancedStatExample"
    },
    {
      "name": "black_stat_examples",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.stats.v1.AdvancedStatExample"
    },
    {
      "name": "cee_version",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.api.v1.SemanticVersion",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_cee_version"
    }
  ]
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14557"></a>
## FND-14557: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse.white_advanced_stats_datapoint = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse",
  "name": "white_advanced_stats_datapoint",
  "number": 1,
  "type": ".chesscom.stats.v1.PlayerAdvancedStatsDatapoint",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14558"></a>
## FND-14558: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse.black_advanced_stats_datapoint = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse",
  "name": "black_advanced_stats_datapoint",
  "number": 2,
  "type": ".chesscom.stats.v1.PlayerAdvancedStatsDatapoint",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14559"></a>
## FND-14559: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse.is_heartbeat = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse",
  "name": "is_heartbeat",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
