# native_interfaces — findings 3201–3300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-15860"></a>
## FND-15860: chesscom.explanation_engine.v1alpha.PositionInfo.fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PositionInfo",
  "name": "fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15861"></a>
## FND-15861: chesscom.explanation_engine.v1alpha.PositionInfo.score_centipawns = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PositionInfo",
  "name": "score_centipawns",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_score_centipawns",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15862"></a>
## FND-15862: chesscom.explanation_engine.v1alpha.PositionInfo.mate_in = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PositionInfo",
  "name": "mate_in",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_mate_in",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15863"></a>
## FND-15863: chesscom.explanation_engine.v1alpha.PositionInfo.expected_points = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PositionInfo",
  "name": "expected_points",
  "number": 4,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_expected_points",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15864"></a>
## FND-15864: chesscom.explanation_engine.v1alpha.PositionInfo.clock_ms = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PositionInfo",
  "name": "clock_ms",
  "number": 5,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_clock_ms",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15865"></a>
## FND-15865: Native message: chesscom.explanation_engine.v1alpha.MoveStringReprs

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveStringReprs",
  "field": [
    {
      "name": "san",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "uci",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15866"></a>
## FND-15866: chesscom.explanation_engine.v1alpha.MoveStringReprs.san = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveStringReprs",
  "name": "san",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15867"></a>
## FND-15867: chesscom.explanation_engine.v1alpha.MoveStringReprs.uci = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveStringReprs",
  "name": "uci",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15868"></a>
## FND-15868: Native message: chesscom.explanation_engine.v1alpha.MoveFeatures

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveFeatures",
  "field": [
    {
      "name": "ply",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "full_move_number",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "moved_color",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "moved_piece_type",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    },
    {
      "name": "played",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.MoveStringReprs"
    },
    {
      "name": "before",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PositionInfo"
    },
    {
      "name": "after",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PositionInfo"
    },
    {
      "name": "move_classification",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "score_difference",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "expected_points_difference",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "accuracy",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "engine_best_move",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.MoveStringReprs"
    },
    {
      "name": "engine_second_best_move",
      "number": 21,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.MoveStringReprs"
    },
    {
      "name": "engine_second_best_move_classification",
      "number": 23,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "engine_second_best_expected_points",
      "number": 24,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "rating_spread",
      "number": 25,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.RatingSpread"
    },
    {
      "name": "adjusted_position_difficulty",
      "number": 26,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "adjusted_position_difficulty_bucket",
      "number": 27,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.PositionDifficultyBucket"
    },
    {
      "name": "move_time",
      "number": 30,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".google.protobuf.Duration",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "game_phase",
      "number": 31,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase"
    },
    {
      "name": "position_type",
      "number": 32,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.PositionType"
    },
    {
      "name": "player_activity",
      "number": 33,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.ActivityLevel"
    },
    {
      "name": "opponent_activity",
      "number": 34,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.ActivityLevel"
    },
    {
      "name": "tactical_category",
      "number": 35,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.TacticalCategory"
    },
    {
      "name": "puzzle_themes_found",
      "number": 36,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeType"
    },
    {
      "name": "puzzle_themes_missed",
      "number": 37,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeType"
    },
    {
      "name": "puzzle_themes_allowed",
      "number": 38,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeType"
    },
    {
      "name": "player_permits_material_win",
      "number": 39,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "player_permits_adjacent_forward_material_win",
      "number": 40,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "was_permitted_material_win_by_opponent_previous_move",
      "number": 41,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "opponent_permitted_on_previous_move",
      "number": 42,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "took_adjacent_forward_material_win",
      "number": 43,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "player_had_material_threat_on_previous_move",
      "number": 44,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "is_direct_sacrifice_enprise_adjacent_forward",
      "number": 45,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "board_events",
      "number": 46,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEvent"
    },
    {
      "name": "game_review_prioritized_board_events",
      "number": 47,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEvent"
    },
    {
      "name": "coach_speech",
      "number": 48,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ],
  "oneof_decl": [
    {
      "name": "_score_difference"
    },
    {
      "name": "_expected_points_difference"
    },
    {
      "name": "_accuracy"
    },
    {
      "name": "_engine_second_best_expected_points"
    },
    {
      "name": "_adjusted_position_difficulty"
    },
    {
      "name": "_move_time"
    }
  ],
  "reserved_range": [
    {
      "start": 6,
      "end": 7
    },
    {
      "start": 10,
      "end": 11
    },
    {
      "start": 11,
      "end": 12
    },
    {
      "start": 13,
      "end": 14
    },
    {
      "start": 14,
      "end": 15
    },
    {
      "start": 16,
      "end": 17
    },
    {
      "start": 17,
      "end": 18
    },
    {
      "start": 20,
      "end": 21
    },
    {
      "start": 22,
      "end": 23
    },
    {
      "start": 28,
      "end": 29
    },
    {
      "start": 29,
      "end": 30
    }
  ]
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15869"></a>
## FND-15869: chesscom.explanation_engine.v1alpha.MoveFeatures.ply = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "ply",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15870"></a>
## FND-15870: chesscom.explanation_engine.v1alpha.MoveFeatures.full_move_number = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "full_move_number",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15871"></a>
## FND-15871: chesscom.explanation_engine.v1alpha.MoveFeatures.moved_color = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "moved_color",
  "number": 3,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15872"></a>
## FND-15872: chesscom.explanation_engine.v1alpha.MoveFeatures.moved_piece_type = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "moved_piece_type",
  "number": 4,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15873"></a>
## FND-15873: chesscom.explanation_engine.v1alpha.MoveFeatures.played = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "played",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1alpha.MoveStringReprs",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15874"></a>
## FND-15874: chesscom.explanation_engine.v1alpha.MoveFeatures.before = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "before",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1alpha.PositionInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15875"></a>
## FND-15875: chesscom.explanation_engine.v1alpha.MoveFeatures.after = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "after",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1alpha.PositionInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15876"></a>
## FND-15876: chesscom.explanation_engine.v1alpha.MoveFeatures.move_classification = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "move_classification",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15877"></a>
## FND-15877: chesscom.explanation_engine.v1alpha.MoveFeatures.score_difference = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "score_difference",
  "number": 12,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_score_difference",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15878"></a>
## FND-15878: chesscom.explanation_engine.v1alpha.MoveFeatures.expected_points_difference = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "expected_points_difference",
  "number": 15,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_expected_points_difference",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15879"></a>
## FND-15879: chesscom.explanation_engine.v1alpha.MoveFeatures.accuracy = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "accuracy",
  "number": 18,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_accuracy",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15880"></a>
## FND-15880: chesscom.explanation_engine.v1alpha.MoveFeatures.engine_best_move = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "engine_best_move",
  "number": 19,
  "type": ".chesscom.explanation_engine.v1alpha.MoveStringReprs",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15881"></a>
## FND-15881: chesscom.explanation_engine.v1alpha.MoveFeatures.engine_second_best_move = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "engine_second_best_move",
  "number": 21,
  "type": ".chesscom.explanation_engine.v1alpha.MoveStringReprs",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15882"></a>
## FND-15882: chesscom.explanation_engine.v1alpha.MoveFeatures.engine_second_best_move_classification = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "engine_second_best_move_classification",
  "number": 23,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15883"></a>
## FND-15883: chesscom.explanation_engine.v1alpha.MoveFeatures.engine_second_best_expected_points = 24

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "engine_second_best_expected_points",
  "number": 24,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine_second_best_expected_points",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15884"></a>
## FND-15884: chesscom.explanation_engine.v1alpha.MoveFeatures.rating_spread = 25

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "rating_spread",
  "number": 25,
  "type": ".chesscom.explanation_engine.v1alpha.RatingSpread",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15885"></a>
## FND-15885: chesscom.explanation_engine.v1alpha.MoveFeatures.adjusted_position_difficulty = 26

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "adjusted_position_difficulty",
  "number": 26,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_adjusted_position_difficulty",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15886"></a>
## FND-15886: chesscom.explanation_engine.v1alpha.MoveFeatures.adjusted_position_difficulty_bucket = 27

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "adjusted_position_difficulty_bucket",
  "number": 27,
  "type": ".chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15887"></a>
## FND-15887: chesscom.explanation_engine.v1alpha.MoveFeatures.move_time = 30

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "move_time",
  "number": 30,
  "type": ".google.protobuf.Duration",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move_time",
  "proto3_optional": true,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15888"></a>
## FND-15888: chesscom.explanation_engine.v1alpha.MoveFeatures.game_phase = 31

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "game_phase",
  "number": 31,
  "type": ".chesscom.chess.v1.GamePhase",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15889"></a>
## FND-15889: chesscom.explanation_engine.v1alpha.MoveFeatures.position_type = 32

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "position_type",
  "number": 32,
  "type": ".chesscom.explanation_engine.v1alpha.PositionType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15890"></a>
## FND-15890: chesscom.explanation_engine.v1alpha.MoveFeatures.player_activity = 33

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "player_activity",
  "number": 33,
  "type": ".chesscom.explanation_engine.v1alpha.ActivityLevel",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15891"></a>
## FND-15891: chesscom.explanation_engine.v1alpha.MoveFeatures.opponent_activity = 34

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "opponent_activity",
  "number": 34,
  "type": ".chesscom.explanation_engine.v1alpha.ActivityLevel",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15892"></a>
## FND-15892: chesscom.explanation_engine.v1alpha.MoveFeatures.tactical_category = 35

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "tactical_category",
  "number": 35,
  "type": ".chesscom.explanation_engine.v1alpha.TacticalCategory",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15893"></a>
## FND-15893: chesscom.explanation_engine.v1alpha.MoveFeatures.puzzle_themes_found = 36

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "puzzle_themes_found",
  "number": 36,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeType",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15894"></a>
## FND-15894: chesscom.explanation_engine.v1alpha.MoveFeatures.puzzle_themes_missed = 37

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "puzzle_themes_missed",
  "number": 37,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeType",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15895"></a>
## FND-15895: chesscom.explanation_engine.v1alpha.MoveFeatures.puzzle_themes_allowed = 38

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "puzzle_themes_allowed",
  "number": 38,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeType",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15896"></a>
## FND-15896: chesscom.explanation_engine.v1alpha.MoveFeatures.player_permits_material_win = 39

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "player_permits_material_win",
  "number": 39,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15897"></a>
## FND-15897: chesscom.explanation_engine.v1alpha.MoveFeatures.player_permits_adjacent_forward_material_win = 40

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "player_permits_adjacent_forward_material_win",
  "number": 40,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15898"></a>
## FND-15898: chesscom.explanation_engine.v1alpha.MoveFeatures.was_permitted_material_win_by_opponent_previous_move = 41

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "was_permitted_material_win_by_opponent_previous_move",
  "number": 41,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15899"></a>
## FND-15899: chesscom.explanation_engine.v1alpha.MoveFeatures.opponent_permitted_on_previous_move = 42

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "opponent_permitted_on_previous_move",
  "number": 42,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15900"></a>
## FND-15900: chesscom.explanation_engine.v1alpha.MoveFeatures.took_adjacent_forward_material_win = 43

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "took_adjacent_forward_material_win",
  "number": 43,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15901"></a>
## FND-15901: chesscom.explanation_engine.v1alpha.MoveFeatures.player_had_material_threat_on_previous_move = 44

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "player_had_material_threat_on_previous_move",
  "number": 44,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15902"></a>
## FND-15902: chesscom.explanation_engine.v1alpha.MoveFeatures.is_direct_sacrifice_enprise_adjacent_forward = 45

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "is_direct_sacrifice_enprise_adjacent_forward",
  "number": 45,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15903"></a>
## FND-15903: chesscom.explanation_engine.v1alpha.MoveFeatures.board_events = 46

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "board_events",
  "number": 46,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEvent",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15904"></a>
## FND-15904: chesscom.explanation_engine.v1alpha.MoveFeatures.game_review_prioritized_board_events = 47

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "game_review_prioritized_board_events",
  "number": 47,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEvent",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15905"></a>
## FND-15905: chesscom.explanation_engine.v1alpha.MoveFeatures.coach_speech = 48

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.MoveFeatures",
  "name": "coach_speech",
  "number": 48,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15906"></a>
## FND-15906: chesscom.explanation_engine.v1alpha.PositionType.POSITION_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionType",
  "name": "POSITION_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15907"></a>
## FND-15907: chesscom.explanation_engine.v1alpha.PositionType.POSITION_TYPE_NONE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionType",
  "name": "POSITION_TYPE_NONE",
  "number": 1,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15908"></a>
## FND-15908: chesscom.explanation_engine.v1alpha.PositionType.POSITION_TYPE_OPEN = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionType",
  "name": "POSITION_TYPE_OPEN",
  "number": 2,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15909"></a>
## FND-15909: chesscom.explanation_engine.v1alpha.PositionType.POSITION_TYPE_SEMI_OPEN = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionType",
  "name": "POSITION_TYPE_SEMI_OPEN",
  "number": 3,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15910"></a>
## FND-15910: chesscom.explanation_engine.v1alpha.PositionType.POSITION_TYPE_CLOSED = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionType",
  "name": "POSITION_TYPE_CLOSED",
  "number": 4,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15911"></a>
## FND-15911: chesscom.explanation_engine.v1alpha.ActivityLevel.ACTIVITY_LEVEL_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ActivityLevel",
  "name": "ACTIVITY_LEVEL_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15912"></a>
## FND-15912: chesscom.explanation_engine.v1alpha.ActivityLevel.ACTIVITY_LEVEL_ACTIVE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ActivityLevel",
  "name": "ACTIVITY_LEVEL_ACTIVE",
  "number": 1,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15913"></a>
## FND-15913: chesscom.explanation_engine.v1alpha.ActivityLevel.ACTIVITY_LEVEL_PASSIVE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ActivityLevel",
  "name": "ACTIVITY_LEVEL_PASSIVE",
  "number": 2,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15914"></a>
## FND-15914: chesscom.explanation_engine.v1alpha.ActivityLevel.ACTIVITY_LEVEL_NEITHER = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ActivityLevel",
  "name": "ACTIVITY_LEVEL_NEITHER",
  "number": 3,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15915"></a>
## FND-15915: chesscom.explanation_engine.v1alpha.TacticalCategory.TACTICAL_CATEGORY_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.TacticalCategory",
  "name": "TACTICAL_CATEGORY_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15916"></a>
## FND-15916: chesscom.explanation_engine.v1alpha.TacticalCategory.TACTICAL_CATEGORY_CALM = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.TacticalCategory",
  "name": "TACTICAL_CATEGORY_CALM",
  "number": 1,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15917"></a>
## FND-15917: chesscom.explanation_engine.v1alpha.TacticalCategory.TACTICAL_CATEGORY_SHARP = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.TacticalCategory",
  "name": "TACTICAL_CATEGORY_SHARP",
  "number": 2,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15918"></a>
## FND-15918: chesscom.explanation_engine.v1alpha.TacticalCategory.TACTICAL_CATEGORY_THREATENED = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.TacticalCategory",
  "name": "TACTICAL_CATEGORY_THREATENED",
  "number": 3,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15919"></a>
## FND-15919: chesscom.explanation_engine.v1alpha.TacticalCategory.TACTICAL_CATEGORY_THREATENING = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.TacticalCategory",
  "name": "TACTICAL_CATEGORY_THREATENING",
  "number": 4,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15920"></a>
## FND-15920: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15921"></a>
## FND-15921: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_BOOK = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_BOOK",
  "number": 1,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15922"></a>
## FND-15922: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EARLY_OPENING = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EARLY_OPENING",
  "number": 2,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15923"></a>
## FND-15923: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EQUAL_EASY = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EQUAL_EASY",
  "number": 3,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15924"></a>
## FND-15924: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EQUAL_MEDIUM = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EQUAL_MEDIUM",
  "number": 4,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15925"></a>
## FND-15925: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EQUAL_HARD = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EQUAL_HARD",
  "number": 5,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15926"></a>
## FND-15926: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_WINNING_EASY = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_WINNING_EASY",
  "number": 6,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15927"></a>
## FND-15927: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_WINNING_MEDIUM = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_WINNING_MEDIUM",
  "number": 7,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15928"></a>
## FND-15928: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_WINNING_HARD = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_WINNING_HARD",
  "number": 8,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15929"></a>
## FND-15929: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_LOSING = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_LOSING",
  "number": 9,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15930"></a>
## FND-15930: chesscom.explanation_engine.v1alpha.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_FORCED = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_FORCED",
  "number": 10,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15931"></a>
## FND-15931: chesscom.explanation_engine.v1alpha.RatingInputKind.RATING_INPUT_KIND_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.RatingInputKind",
  "name": "RATING_INPUT_KIND_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15932"></a>
## FND-15932: chesscom.explanation_engine.v1alpha.RatingInputKind.RATING_INPUT_KIND_EMPIRICAL = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.RatingInputKind",
  "name": "RATING_INPUT_KIND_EMPIRICAL",
  "number": 1,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15933"></a>
## FND-15933: chesscom.explanation_engine.v1alpha.RatingInputKind.RATING_INPUT_KIND_REFERENCE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.RatingInputKind",
  "name": "RATING_INPUT_KIND_REFERENCE",
  "number": 2,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15934"></a>
## FND-15934: chesscom.explanation_engine.v1alpha.RatingInputKind.RATING_INPUT_KIND_POSITION_DIFFICULTY = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.RatingInputKind",
  "name": "RATING_INPUT_KIND_POSITION_DIFFICULTY",
  "number": 3,
  "source_id": "SRC-1059",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1059** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0d529c14fa3449122518d92d5aa47eba764a94fb068769150c29848eb9d65422.bin)

**Source references:** SRC-1059, SRC-1842  
**URL references:** None independently associated  
**Related findings:** FND-15849, FND-15850, FND-15851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15935"></a>
## FND-15935: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15936, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15936"></a>
## FND-15936: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_GREATLY_LOSING = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_GREATLY_LOSING",
  "number": 1,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15937"></a>
## FND-15937: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_LOSING = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_LOSING",
  "number": 2,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15936

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15938"></a>
## FND-15938: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_PROBABLY_LOSING = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_PROBABLY_LOSING",
  "number": 3,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15936, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15939"></a>
## FND-15939: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_DRAWING = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_DRAWING",
  "number": 4,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15936, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15940"></a>
## FND-15940: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_PROBABLY_WINNING = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_PROBABLY_WINNING",
  "number": 5,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15936, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15941"></a>
## FND-15941: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_WINNING = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_WINNING",
  "number": 6,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15936, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15942"></a>
## FND-15942: chesscom.explanation_engine.v1alpha.GameStatus.GAME_STATUS_GREATLY_WINNING = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.GameStatus",
  "name": "GAME_STATUS_GREATLY_WINNING",
  "number": 7,
  "source_id": "SRC-1060",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1060** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_status.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1923559348863d4741230b29d2689d2a026394fe1c24fc533bebdcc1def1847c.bin)

**Source references:** SRC-1060, SRC-1782  
**URL references:** None independently associated  
**Related findings:** FND-15935, FND-15936, FND-15937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15943"></a>
## FND-15943: Native message: chesscom.explanation_engine.v1alpha.DecisiveMistake

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DecisiveMistake",
  "field": [
    {
      "name": "phase",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase"
    },
    {
      "name": "state_prior",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.DecisiveMistakeGameState"
    },
    {
      "name": "type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.DecisiveMistakeType"
    }
  ]
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15944"></a>
## FND-15944: chesscom.explanation_engine.v1alpha.DecisiveMistake.phase = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.DecisiveMistake",
  "name": "phase",
  "number": 1,
  "type": ".chesscom.chess.v1.GamePhase",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15945"></a>
## FND-15945: chesscom.explanation_engine.v1alpha.DecisiveMistake.state_prior = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.DecisiveMistake",
  "name": "state_prior",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.DecisiveMistakeGameState",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15946"></a>
## FND-15946: chesscom.explanation_engine.v1alpha.DecisiveMistake.type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.DecisiveMistake",
  "name": "type",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.DecisiveMistakeType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15947"></a>
## FND-15947: Native message: chesscom.explanation_engine.v1alpha.GameSummary

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameSummary",
  "field": [
    {
      "name": "result_summary",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.ResultSummary"
    },
    {
      "name": "decisive_mistake",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DecisiveMistake",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "key_move_type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.KeyMoveType"
    }
  ],
  "oneof_decl": [
    {
      "name": "_decisive_mistake"
    }
  ]
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15948"></a>
## FND-15948: chesscom.explanation_engine.v1alpha.GameSummary.result_summary = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GameSummary",
  "name": "result_summary",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.ResultSummary",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15949"></a>
## FND-15949: chesscom.explanation_engine.v1alpha.GameSummary.decisive_mistake = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GameSummary",
  "name": "decisive_mistake",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.DecisiveMistake",
  "label": "LABEL_OPTIONAL",
  "oneof": "_decisive_mistake",
  "proto3_optional": true,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15950"></a>
## FND-15950: chesscom.explanation_engine.v1alpha.GameSummary.key_move_type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GameSummary",
  "name": "key_move_type",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.KeyMoveType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15951"></a>
## FND-15951: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15952"></a>
## FND-15952: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_FALLBACK = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_FALLBACK",
  "number": 1,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15953"></a>
## FND-15953: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_WIN_RESULT = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_WIN_RESULT",
  "number": 2,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15954"></a>
## FND-15954: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_WIN_BY_FLAG_FROM_WORSE_POSITION = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_WIN_BY_FLAG_FROM_WORSE_POSITION",
  "number": 3,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15955"></a>
## FND-15955: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_WIN_BY_FLAG_FROM_EQUAL_POSITION = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_WIN_BY_FLAG_FROM_EQUAL_POSITION",
  "number": 4,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15956"></a>
## FND-15956: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_DRAW_RESULT = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_DRAW_RESULT",
  "number": 5,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15957"></a>
## FND-15957: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_DRAW_FROM_WORSE_POSITION = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_DRAW_FROM_WORSE_POSITION",
  "number": 6,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15958"></a>
## FND-15958: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_DRAW_FROM_BETTER_POSITION = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_DRAW_FROM_BETTER_POSITION",
  "number": 7,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15959"></a>
## FND-15959: chesscom.explanation_engine.v1alpha.ResultSummary.RESULT_SUMMARY_DRAW_TIMEOUT_VS_INSUFFICIENT_FROM_BETTER_POSITION = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.ResultSummary",
  "name": "RESULT_SUMMARY_DRAW_TIMEOUT_VS_INSUFFICIENT_FROM_BETTER_POSITION",
  "number": 8,
  "source_id": "SRC-1061",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1061** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_game_summary.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f0a57941ab455f0353c3a089ccc929feced9f97a9466c99e067a6737ab77cf95.bin)

**Source references:** SRC-1061, SRC-1845  
**URL references:** None independently associated  
**Related findings:** FND-15943, FND-15944, FND-15945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
