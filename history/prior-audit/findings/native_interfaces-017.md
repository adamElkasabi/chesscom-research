# native_interfaces — findings 1601–1700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14260"></a>
## FND-14260: chesscom.explanation_engine.v1.PieceOnSquare.piece_type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceOnSquare",
  "name": "piece_type",
  "number": 1,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14261"></a>
## FND-14261: chesscom.explanation_engine.v1.PieceOnSquare.square = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceOnSquare",
  "name": "square",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14262"></a>
## FND-14262: Native message: chesscom.explanation_engine.v1.MoveTagProfile

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveTagProfile",
  "field": [
    {
      "name": "actor",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceOnSquare"
    },
    {
      "name": "targets",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceOnSquare"
    }
  ]
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14263"></a>
## FND-14263: chesscom.explanation_engine.v1.MoveTagProfile.actor = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveTagProfile",
  "name": "actor",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PieceOnSquare",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14264"></a>
## FND-14264: chesscom.explanation_engine.v1.MoveTagProfile.targets = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveTagProfile",
  "name": "targets",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PieceOnSquare",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14265"></a>
## FND-14265: Native message: chesscom.explanation_engine.v1.MoveTag

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveTag",
  "field": [
    {
      "name": "type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveTagType"
    },
    {
      "name": "profile",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveTagProfile"
    }
  ]
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14266"></a>
## FND-14266: chesscom.explanation_engine.v1.MoveTag.type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveTag",
  "name": "type",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveTagType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14267"></a>
## FND-14267: chesscom.explanation_engine.v1.MoveTag.profile = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveTag",
  "name": "profile",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveTagProfile",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14268"></a>
## FND-14268: Native message: chesscom.explanation_engine.v1.MoveFeatures

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
      "type": "TYPE_INT32"
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
      "type_name": ".chesscom.explanation_engine.v1.MoveStringReprs"
    },
    {
      "name": "before",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PositionInfo"
    },
    {
      "name": "after",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PositionInfo"
    },
    {
      "name": "move_classification",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "move_precision",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "is_key_moment",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "accuracy",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "engine_best_move",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveStringReprs"
    },
    {
      "name": "engine_best_move_piece_type",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    },
    {
      "name": "engine_second_best_expected_points_loss",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "best_move_probability_at_mover_rating",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "played_move_probability_at_mover_rating",
      "number": 16,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "best_move_skill_gap",
      "number": 17,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "adjusted_position_difficulty",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "adjusted_position_difficulty_bucket",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PositionDifficultyBucket"
    },
    {
      "name": "move_time",
      "number": 20,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".google.protobuf.Duration",
      "oneof_index": 6,
      "proto3_optional": true
    },
    {
      "name": "time_usage",
      "number": 21,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.TimeUsage"
    },
    {
      "name": "game_phase",
      "number": 22,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase"
    },
    {
      "name": "position_type",
      "number": 23,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PositionType"
    },
    {
      "name": "player_activity",
      "number": 24,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.ActivityLevel"
    },
    {
      "name": "opponent_activity",
      "number": 25,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.ActivityLevel"
    },
    {
      "name": "tactical_category",
      "number": 26,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.TacticalCategory"
    },
    {
      "name": "tags",
      "number": 27,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveTag"
    },
    {
      "name": "coach_speech",
      "number": 28,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "only_move",
      "number": 29,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 7,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_accuracy"
    },
    {
      "name": "_engine_second_best_expected_points_loss"
    },
    {
      "name": "_best_move_probability_at_mover_rating"
    },
    {
      "name": "_played_move_probability_at_mover_rating"
    },
    {
      "name": "_best_move_skill_gap"
    },
    {
      "name": "_adjusted_position_difficulty"
    },
    {
      "name": "_move_time"
    },
    {
      "name": "_only_move"
    }
  ]
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14269"></a>
## FND-14269: chesscom.explanation_engine.v1.MoveFeatures.ply = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "ply",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14270"></a>
## FND-14270: chesscom.explanation_engine.v1.MoveFeatures.full_move_number = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "full_move_number",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14271"></a>
## FND-14271: chesscom.explanation_engine.v1.MoveFeatures.moved_color = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "moved_color",
  "number": 3,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14272"></a>
## FND-14272: chesscom.explanation_engine.v1.MoveFeatures.moved_piece_type = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "moved_piece_type",
  "number": 4,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14273"></a>
## FND-14273: chesscom.explanation_engine.v1.MoveFeatures.played = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "played",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.MoveStringReprs",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14274"></a>
## FND-14274: chesscom.explanation_engine.v1.MoveFeatures.before = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "before",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.PositionInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14275"></a>
## FND-14275: chesscom.explanation_engine.v1.MoveFeatures.after = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "after",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.PositionInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14276"></a>
## FND-14276: chesscom.explanation_engine.v1.MoveFeatures.move_classification = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "move_classification",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14277"></a>
## FND-14277: chesscom.explanation_engine.v1.MoveFeatures.move_precision = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "move_precision",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14278"></a>
## FND-14278: chesscom.explanation_engine.v1.MoveFeatures.is_key_moment = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "is_key_moment",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14279"></a>
## FND-14279: chesscom.explanation_engine.v1.MoveFeatures.accuracy = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "accuracy",
  "number": 11,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_accuracy",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14280"></a>
## FND-14280: chesscom.explanation_engine.v1.MoveFeatures.engine_best_move = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "engine_best_move",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1.MoveStringReprs",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14281"></a>
## FND-14281: chesscom.explanation_engine.v1.MoveFeatures.engine_best_move_piece_type = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "engine_best_move_piece_type",
  "number": 13,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14282"></a>
## FND-14282: chesscom.explanation_engine.v1.MoveFeatures.engine_second_best_expected_points_loss = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "engine_second_best_expected_points_loss",
  "number": 14,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine_second_best_expected_points_loss",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14283"></a>
## FND-14283: chesscom.explanation_engine.v1.MoveFeatures.best_move_probability_at_mover_rating = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "best_move_probability_at_mover_rating",
  "number": 15,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_best_move_probability_at_mover_rating",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14284"></a>
## FND-14284: chesscom.explanation_engine.v1.MoveFeatures.played_move_probability_at_mover_rating = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "played_move_probability_at_mover_rating",
  "number": 16,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_played_move_probability_at_mover_rating",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14285"></a>
## FND-14285: chesscom.explanation_engine.v1.MoveFeatures.best_move_skill_gap = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "best_move_skill_gap",
  "number": 17,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_best_move_skill_gap",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14286"></a>
## FND-14286: chesscom.explanation_engine.v1.MoveFeatures.adjusted_position_difficulty = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "adjusted_position_difficulty",
  "number": 18,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_adjusted_position_difficulty",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14287"></a>
## FND-14287: chesscom.explanation_engine.v1.MoveFeatures.adjusted_position_difficulty_bucket = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "adjusted_position_difficulty_bucket",
  "number": 19,
  "type": ".chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14288"></a>
## FND-14288: chesscom.explanation_engine.v1.MoveFeatures.move_time = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "move_time",
  "number": 20,
  "type": ".google.protobuf.Duration",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move_time",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14289"></a>
## FND-14289: chesscom.explanation_engine.v1.MoveFeatures.time_usage = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "time_usage",
  "number": 21,
  "type": ".chesscom.explanation_engine.v1.TimeUsage",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14290"></a>
## FND-14290: chesscom.explanation_engine.v1.MoveFeatures.game_phase = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "game_phase",
  "number": 22,
  "type": ".chesscom.chess.v1.GamePhase",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14291"></a>
## FND-14291: chesscom.explanation_engine.v1.MoveFeatures.position_type = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "position_type",
  "number": 23,
  "type": ".chesscom.explanation_engine.v1.PositionType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14292"></a>
## FND-14292: chesscom.explanation_engine.v1.MoveFeatures.player_activity = 24

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "player_activity",
  "number": 24,
  "type": ".chesscom.explanation_engine.v1.ActivityLevel",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14293"></a>
## FND-14293: chesscom.explanation_engine.v1.MoveFeatures.opponent_activity = 25

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "opponent_activity",
  "number": 25,
  "type": ".chesscom.explanation_engine.v1.ActivityLevel",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14294"></a>
## FND-14294: chesscom.explanation_engine.v1.MoveFeatures.tactical_category = 26

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "tactical_category",
  "number": 26,
  "type": ".chesscom.explanation_engine.v1.TacticalCategory",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14295"></a>
## FND-14295: chesscom.explanation_engine.v1.MoveFeatures.tags = 27

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "tags",
  "number": 27,
  "type": ".chesscom.explanation_engine.v1.MoveTag",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14296"></a>
## FND-14296: chesscom.explanation_engine.v1.MoveFeatures.coach_speech = 28

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "coach_speech",
  "number": 28,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14297"></a>
## FND-14297: chesscom.explanation_engine.v1.MoveFeatures.only_move = 29

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveFeatures",
  "name": "only_move",
  "number": 29,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_only_move",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14298"></a>
## FND-14298: Native message: chesscom.explanation_engine.v1.PlayerGameFeatures

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PlayerGameFeatures",
  "field": [
    {
      "name": "accuracy",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "game_rating",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PlayerGameRating"
    },
    {
      "name": "classification_tallies",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.ClassificationTally"
    },
    {
      "name": "comeback",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "cleanliness",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "worst_ep_loss",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "narrative_moves",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    }
  ],
  "oneof_decl": [
    {
      "name": "_accuracy"
    },
    {
      "name": "_comeback"
    },
    {
      "name": "_cleanliness"
    },
    {
      "name": "_worst_ep_loss"
    }
  ]
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14299"></a>
## FND-14299: chesscom.explanation_engine.v1.PlayerGameFeatures.accuracy = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "accuracy",
  "number": 1,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_accuracy",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14300"></a>
## FND-14300: chesscom.explanation_engine.v1.PlayerGameFeatures.game_rating = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "game_rating",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PlayerGameRating",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14301"></a>
## FND-14301: chesscom.explanation_engine.v1.PlayerGameFeatures.classification_tallies = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "classification_tallies",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.ClassificationTally",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14302"></a>
## FND-14302: chesscom.explanation_engine.v1.PlayerGameFeatures.comeback = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "comeback",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_comeback",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14303"></a>
## FND-14303: chesscom.explanation_engine.v1.PlayerGameFeatures.cleanliness = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "cleanliness",
  "number": 5,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_cleanliness",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14304"></a>
## FND-14304: chesscom.explanation_engine.v1.PlayerGameFeatures.worst_ep_loss = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "worst_ep_loss",
  "number": 6,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_worst_ep_loss",
  "proto3_optional": true,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14305"></a>
## FND-14305: chesscom.explanation_engine.v1.PlayerGameFeatures.narrative_moves = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerGameFeatures",
  "name": "narrative_moves",
  "number": 7,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14306"></a>
## FND-14306: Native message: chesscom.explanation_engine.v1.GameFeatures

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameFeatures",
  "field": [
    {
      "name": "computation",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameFeatureComputation"
    },
    {
      "name": "eco_code",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "eco_family_id",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "opening_name",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "white",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PlayerGameFeatures"
    },
    {
      "name": "black",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PlayerGameFeatures"
    },
    {
      "name": "moves",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveFeatures"
    }
  ]
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14307"></a>
## FND-14307: chesscom.explanation_engine.v1.GameFeatures.computation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "computation",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameFeatureComputation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14308"></a>
## FND-14308: chesscom.explanation_engine.v1.GameFeatures.eco_code = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "eco_code",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14309"></a>
## FND-14309: chesscom.explanation_engine.v1.GameFeatures.eco_family_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "eco_family_id",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14310"></a>
## FND-14310: chesscom.explanation_engine.v1.GameFeatures.opening_name = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "opening_name",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14311"></a>
## FND-14311: chesscom.explanation_engine.v1.GameFeatures.white = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "white",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.PlayerGameFeatures",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14312"></a>
## FND-14312: chesscom.explanation_engine.v1.GameFeatures.black = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "black",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.PlayerGameFeatures",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14313"></a>
## FND-14313: chesscom.explanation_engine.v1.GameFeatures.moves = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameFeatures",
  "name": "moves",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.MoveFeatures",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14314"></a>
## FND-14314: chesscom.explanation_engine.v1.PositionType.POSITION_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionType",
  "name": "POSITION_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14315"></a>
## FND-14315: chesscom.explanation_engine.v1.PositionType.POSITION_TYPE_NONE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionType",
  "name": "POSITION_TYPE_NONE",
  "number": 1,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14316"></a>
## FND-14316: chesscom.explanation_engine.v1.PositionType.POSITION_TYPE_OPEN = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionType",
  "name": "POSITION_TYPE_OPEN",
  "number": 2,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14317"></a>
## FND-14317: chesscom.explanation_engine.v1.PositionType.POSITION_TYPE_SEMI_OPEN = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionType",
  "name": "POSITION_TYPE_SEMI_OPEN",
  "number": 3,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14318"></a>
## FND-14318: chesscom.explanation_engine.v1.PositionType.POSITION_TYPE_CLOSED = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionType",
  "name": "POSITION_TYPE_CLOSED",
  "number": 4,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14319"></a>
## FND-14319: chesscom.explanation_engine.v1.ActivityLevel.ACTIVITY_LEVEL_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ActivityLevel",
  "name": "ACTIVITY_LEVEL_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14320"></a>
## FND-14320: chesscom.explanation_engine.v1.ActivityLevel.ACTIVITY_LEVEL_ACTIVE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ActivityLevel",
  "name": "ACTIVITY_LEVEL_ACTIVE",
  "number": 1,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14321"></a>
## FND-14321: chesscom.explanation_engine.v1.ActivityLevel.ACTIVITY_LEVEL_PASSIVE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ActivityLevel",
  "name": "ACTIVITY_LEVEL_PASSIVE",
  "number": 2,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14322"></a>
## FND-14322: chesscom.explanation_engine.v1.ActivityLevel.ACTIVITY_LEVEL_NEITHER = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ActivityLevel",
  "name": "ACTIVITY_LEVEL_NEITHER",
  "number": 3,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14323"></a>
## FND-14323: chesscom.explanation_engine.v1.TacticalCategory.TACTICAL_CATEGORY_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalCategory",
  "name": "TACTICAL_CATEGORY_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14324"></a>
## FND-14324: chesscom.explanation_engine.v1.TacticalCategory.TACTICAL_CATEGORY_CALM = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalCategory",
  "name": "TACTICAL_CATEGORY_CALM",
  "number": 1,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14325"></a>
## FND-14325: chesscom.explanation_engine.v1.TacticalCategory.TACTICAL_CATEGORY_SHARP = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalCategory",
  "name": "TACTICAL_CATEGORY_SHARP",
  "number": 2,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14326"></a>
## FND-14326: chesscom.explanation_engine.v1.TacticalCategory.TACTICAL_CATEGORY_THREATENED = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalCategory",
  "name": "TACTICAL_CATEGORY_THREATENED",
  "number": 3,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14327"></a>
## FND-14327: chesscom.explanation_engine.v1.TacticalCategory.TACTICAL_CATEGORY_THREATENING = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalCategory",
  "name": "TACTICAL_CATEGORY_THREATENING",
  "number": 4,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14328"></a>
## FND-14328: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14329"></a>
## FND-14329: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_BOOK = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_BOOK",
  "number": 1,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14330"></a>
## FND-14330: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EARLY_OPENING = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EARLY_OPENING",
  "number": 2,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14331"></a>
## FND-14331: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EQUAL_EASY = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EQUAL_EASY",
  "number": 3,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14332"></a>
## FND-14332: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EQUAL_MEDIUM = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EQUAL_MEDIUM",
  "number": 4,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14333"></a>
## FND-14333: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_EQUAL_HARD = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_EQUAL_HARD",
  "number": 5,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14334"></a>
## FND-14334: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_WINNING_EASY = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_WINNING_EASY",
  "number": 6,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14335"></a>
## FND-14335: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_WINNING_MEDIUM = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_WINNING_MEDIUM",
  "number": 7,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14336"></a>
## FND-14336: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_WINNING_HARD = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_WINNING_HARD",
  "number": 8,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14337"></a>
## FND-14337: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_LOSING = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_LOSING",
  "number": 9,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14338"></a>
## FND-14338: chesscom.explanation_engine.v1.PositionDifficultyBucket.POSITION_DIFFICULTY_BUCKET_FORCED = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionDifficultyBucket",
  "name": "POSITION_DIFFICULTY_BUCKET_FORCED",
  "number": 10,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14339"></a>
## FND-14339: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14340"></a>
## FND-14340: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_NONE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_NONE",
  "number": 1,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14341"></a>
## FND-14341: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_PRESSURE_FORGIVE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_PRESSURE_FORGIVE",
  "number": 2,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14342"></a>
## FND-14342: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_RUSHED_HARD = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_RUSHED_HARD",
  "number": 3,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14343"></a>
## FND-14343: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_QUICK_UNDER_PRESSURE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_QUICK_UNDER_PRESSURE",
  "number": 4,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14344"></a>
## FND-14344: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_QUICK_INSTINCT = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_QUICK_INSTINCT",
  "number": 5,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14345"></a>
## FND-14345: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_INVESTED_ADVANTAGE = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_INVESTED_ADVANTAGE",
  "number": 6,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14346"></a>
## FND-14346: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_PATIENCE_REWARDED = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_PATIENCE_REWARDED",
  "number": 7,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14347"></a>
## FND-14347: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_BURNED_ADVANTAGE = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_BURNED_ADVANTAGE",
  "number": 8,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14348"></a>
## FND-14348: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_TIME_LEAK = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_TIME_LEAK",
  "number": 9,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14349"></a>
## FND-14349: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_BURNED_ADVANTAGE_MISS = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_BURNED_ADVANTAGE_MISS",
  "number": 10,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14350"></a>
## FND-14350: chesscom.explanation_engine.v1.TimeUsage.TIME_USAGE_OVERTHINK_MISS = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TimeUsage",
  "name": "TIME_USAGE_OVERTHINK_MISS",
  "number": 11,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14351"></a>
## FND-14351: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14352"></a>
## FND-14352: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_CAPTURES = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_CAPTURES",
  "number": 1,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14353"></a>
## FND-14353: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_CHECK = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_CHECK",
  "number": 2,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14354"></a>
## FND-14354: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_DOUBLE_CHECK = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_DOUBLE_CHECK",
  "number": 3,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14355"></a>
## FND-14355: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_CHECKMATE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_CHECKMATE",
  "number": 4,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14356"></a>
## FND-14356: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_FORCES_MATE = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_FORCES_MATE",
  "number": 5,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14357"></a>
## FND-14357: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_SACRIFICE = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_SACRIFICE",
  "number": 6,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14358"></a>
## FND-14358: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_WINS_MATERIAL = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_WINS_MATERIAL",
  "number": 7,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14359"></a>
## FND-14359: chesscom.explanation_engine.v1.MoveTagType.MOVE_TAG_TYPE_ATTACKS = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveTagType",
  "name": "MOVE_TAG_TYPE_ATTACKS",
  "number": 8,
  "source_id": "SRC-0994",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0994** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/301fe3f199c9f8ee6f64f80ea797fdc1adc471a06ee6f4633f72863c6904c7bb.bin)

**Source references:** SRC-0994, SRC-1878  
**URL references:** None independently associated  
**Related findings:** FND-14249, FND-14250, FND-14251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
