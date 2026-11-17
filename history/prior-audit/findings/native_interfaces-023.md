# native_interfaces — findings 2201–2300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14860"></a>
## FND-14860: chesscom.explanation_engine.v1.PuzzleTheme.pawn_structure = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "pawn_structure",
  "number": 22,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemePawnStructure",
  "label": "LABEL_OPTIONAL",
  "oneof": "theme",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14861"></a>
## FND-14861: chesscom.explanation_engine.v1.PuzzleTheme.ladder_mate = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "ladder_mate",
  "number": 23,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeLadderMate",
  "label": "LABEL_OPTIONAL",
  "oneof": "theme",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14862"></a>
## FND-14862: chesscom.explanation_engine.v1.PuzzleTheme.theme_type = 255

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "theme_type",
  "number": 255,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14863"></a>
## FND-14863: Native message: chesscom.explanation_engine.v1.TacticalGoal

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoal",
  "field": [
    {
      "name": "checkmate",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalCheckmate",
      "oneof_index": 0
    },
    {
      "name": "promotion",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalPromotion",
      "oneof_index": 0
    },
    {
      "name": "attack_the_king",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalAttackTheKing",
      "oneof_index": 0
    },
    {
      "name": "win_material",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalWinMaterial",
      "oneof_index": 0
    },
    {
      "name": "defense",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalDefense",
      "oneof_index": 0
    },
    {
      "name": "promotion_position",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalPromotionPosition",
      "oneof_index": 0
    },
    {
      "name": "distant_checkmate",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate",
      "oneof_index": 0
    },
    {
      "name": "goal_type",
      "number": 255,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoalType"
    }
  ],
  "oneof_decl": [
    {
      "name": "goal"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14864"></a>
## FND-14864: chesscom.explanation_engine.v1.TacticalGoal.checkmate = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "checkmate",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalCheckmate",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14865"></a>
## FND-14865: chesscom.explanation_engine.v1.TacticalGoal.promotion = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "promotion",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalPromotion",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14866"></a>
## FND-14866: chesscom.explanation_engine.v1.TacticalGoal.attack_the_king = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "attack_the_king",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalAttackTheKing",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14867"></a>
## FND-14867: chesscom.explanation_engine.v1.TacticalGoal.win_material = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "win_material",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalWinMaterial",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14868"></a>
## FND-14868: chesscom.explanation_engine.v1.TacticalGoal.defense = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "defense",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalDefense",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14869"></a>
## FND-14869: chesscom.explanation_engine.v1.TacticalGoal.promotion_position = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "promotion_position",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalPromotionPosition",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14870"></a>
## FND-14870: chesscom.explanation_engine.v1.TacticalGoal.distant_checkmate = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "distant_checkmate",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal",
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14871"></a>
## FND-14871: chesscom.explanation_engine.v1.TacticalGoal.goal_type = 255

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoal",
  "name": "goal_type",
  "number": 255,
  "type": ".chesscom.explanation_engine.v1.TacticalGoalType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14872"></a>
## FND-14872: Native message: chesscom.explanation_engine.v1.StrategicGoal

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "StrategicGoal",
  "field": [
    {
      "name": "goal_type",
      "number": 255,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.StrategicGoalType"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14873"></a>
## FND-14873: chesscom.explanation_engine.v1.StrategicGoal.goal_type = 255

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.StrategicGoal",
  "name": "goal_type",
  "number": 255,
  "type": ".chesscom.explanation_engine.v1.StrategicGoalType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14874"></a>
## FND-14874: Native message: chesscom.explanation_engine.v1.TacticalGoalCheckmate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalCheckmate"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14875"></a>
## FND-14875: Native message: chesscom.explanation_engine.v1.TacticalGoalPromotion

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalPromotion"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14876"></a>
## FND-14876: Native message: chesscom.explanation_engine.v1.TacticalGoalAttackTheKing

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalAttackTheKing"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14877"></a>
## FND-14877: Native message: chesscom.explanation_engine.v1.TacticalGoalDefense

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalDefense"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14878"></a>
## FND-14878: Native message: chesscom.explanation_engine.v1.TacticalGoalWinMaterial

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalWinMaterial",
  "field": [
    {
      "name": "won_piece",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Piece",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_won_piece"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14879"></a>
## FND-14879: chesscom.explanation_engine.v1.TacticalGoalWinMaterial.won_piece = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.TacticalGoalWinMaterial",
  "name": "won_piece",
  "number": 1,
  "type": ".chesscom.chess.v1.Piece",
  "label": "LABEL_OPTIONAL",
  "oneof": "_won_piece",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14880"></a>
## FND-14880: Native message: chesscom.explanation_engine.v1.TacticalGoalPromotionPosition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalPromotionPosition"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14881"></a>
## FND-14881: Native message: chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TacticalGoalDistantCheckmate"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14882"></a>
## FND-14882: Native message: chesscom.explanation_engine.v1.PuzzleThemeMateIn1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeMateIn1"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14883"></a>
## FND-14883: Native message: chesscom.explanation_engine.v1.PuzzleThemeMateIn2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeMateIn2"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14884"></a>
## FND-14884: Native message: chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeMateIn3Plus"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14885"></a>
## FND-14885: Native message: chesscom.explanation_engine.v1.PuzzleThemeScholarsMate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeScholarsMate"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14886"></a>
## FND-14886: Native message: chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeEndgameTactics"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14887"></a>
## FND-14887: Native message: chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeTrappedPiece"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14888"></a>
## FND-14888: Native message: chesscom.explanation_engine.v1.PuzzleThemeFork

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeFork"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14889"></a>
## FND-14889: Native message: chesscom.explanation_engine.v1.PuzzleThemeSkewer

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeSkewer"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14890"></a>
## FND-14890: Native message: chesscom.explanation_engine.v1.PuzzleThemeHangingPiece

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeHangingPiece"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14891"></a>
## FND-14891: Native message: chesscom.explanation_engine.v1.PuzzleThemeDiscovery

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeDiscovery"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14892"></a>
## FND-14892: Native message: chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeQueenSacrifice"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14893"></a>
## FND-14893: Native message: chesscom.explanation_engine.v1.PuzzleThemeOpposition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeOpposition"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14894"></a>
## FND-14894: Native message: chesscom.explanation_engine.v1.PuzzleThemeMatingNet

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeMatingNet"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14895"></a>
## FND-14895: Native message: chesscom.explanation_engine.v1.PuzzleThemePawnEndgame

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemePawnEndgame"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14896"></a>
## FND-14896: Native message: chesscom.explanation_engine.v1.PuzzleThemePromotion

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemePromotion"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14897"></a>
## FND-14897: Native message: chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeUnderPromotion"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14898"></a>
## FND-14898: Native message: chesscom.explanation_engine.v1.PuzzleThemeSacrifice

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeSacrifice"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14899"></a>
## FND-14899: Native message: chesscom.explanation_engine.v1.PuzzleThemeBackRankMate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeBackRankMate"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14900"></a>
## FND-14900: Native message: chesscom.explanation_engine.v1.PuzzleThemePin

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemePin"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14901"></a>
## FND-14901: Native message: chesscom.explanation_engine.v1.PuzzleThemeKingSafety

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeKingSafety",
  "field": [
    {
      "name": "subtheme_weaken",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "subtheme_attack",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "subtheme_defend",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend",
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_subtheme_weaken"
    },
    {
      "name": "_subtheme_attack"
    },
    {
      "name": "_subtheme_defend"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14902"></a>
## FND-14902: chesscom.explanation_engine.v1.PuzzleThemeKingSafety.subtheme_weaken = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemeKingSafety",
  "name": "subtheme_weaken",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_weaken",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14903"></a>
## FND-14903: chesscom.explanation_engine.v1.PuzzleThemeKingSafety.subtheme_attack = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemeKingSafety",
  "name": "subtheme_attack",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_attack",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14904"></a>
## FND-14904: chesscom.explanation_engine.v1.PuzzleThemeKingSafety.subtheme_defend = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemeKingSafety",
  "name": "subtheme_defend",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_defend",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14905"></a>
## FND-14905: Native message: chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemeKingSafetyWeaken"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14906"></a>
## FND-14906: Native message: chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemeKingSafetyAttack"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14907"></a>
## FND-14907: Native message: chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemeKingSafetyDefend"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14908"></a>
## FND-14908: Native message: chesscom.explanation_engine.v1.PuzzleThemePiecePlay

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemePiecePlay",
  "field": [
    {
      "name": "subtheme_activity",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "subtheme_prevention",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "subtheme_trades",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades",
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_subtheme_activity"
    },
    {
      "name": "_subtheme_prevention"
    },
    {
      "name": "_subtheme_trades"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14909"></a>
## FND-14909: chesscom.explanation_engine.v1.PuzzleThemePiecePlay.subtheme_activity = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemePiecePlay",
  "name": "subtheme_activity",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_activity",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14910"></a>
## FND-14910: chesscom.explanation_engine.v1.PuzzleThemePiecePlay.subtheme_prevention = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemePiecePlay",
  "name": "subtheme_prevention",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_prevention",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14911"></a>
## FND-14911: chesscom.explanation_engine.v1.PuzzleThemePiecePlay.subtheme_trades = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemePiecePlay",
  "name": "subtheme_trades",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_trades",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14912"></a>
## FND-14912: Native message: chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemePiecePlayActivity"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14913"></a>
## FND-14913: Native message: chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemePiecePlayPrevention"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14914"></a>
## FND-14914: Native message: chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemePiecePlayTrades"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14915"></a>
## FND-14915: Native message: chesscom.explanation_engine.v1.PuzzleThemePawnStructure

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemePawnStructure",
  "field": [
    {
      "name": "subtheme_healthy",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "subtheme_creates_weaknesses",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_subtheme_healthy"
    },
    {
      "name": "_subtheme_creates_weaknesses"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14916"></a>
## FND-14916: chesscom.explanation_engine.v1.PuzzleThemePawnStructure.subtheme_healthy = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemePawnStructure",
  "name": "subtheme_healthy",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_healthy",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14917"></a>
## FND-14917: chesscom.explanation_engine.v1.PuzzleThemePawnStructure.subtheme_creates_weaknesses = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleThemePawnStructure",
  "name": "subtheme_creates_weaknesses",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses",
  "label": "LABEL_OPTIONAL",
  "oneof": "_subtheme_creates_weaknesses",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14918"></a>
## FND-14918: Native message: chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemePawnStructureHealthy"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14919"></a>
## FND-14919: Native message: chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleSubthemePawnStructureCreatesWeaknesses"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14920"></a>
## FND-14920: Native message: chesscom.explanation_engine.v1.PuzzleThemeLadderMate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleThemeLadderMate"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14921"></a>
## FND-14921: chesscom.explanation_engine.v1.PuzzleGenMode.PUZZLE_GEN_MODE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenMode",
  "name": "PUZZLE_GEN_MODE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14922"></a>
## FND-14922: chesscom.explanation_engine.v1.PuzzleGenMode.PUZZLE_GEN_MODE_TACTICAL = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenMode",
  "name": "PUZZLE_GEN_MODE_TACTICAL",
  "number": 1,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14923"></a>
## FND-14923: chesscom.explanation_engine.v1.PuzzleGenMode.PUZZLE_GEN_MODE_STRATEGIC = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenMode",
  "name": "PUZZLE_GEN_MODE_STRATEGIC",
  "number": 2,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14924"></a>
## FND-14924: chesscom.explanation_engine.v1.PuzzleWinningResult.PUZZLE_WINNING_RESULT_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleWinningResult",
  "name": "PUZZLE_WINNING_RESULT_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14925"></a>
## FND-14925: chesscom.explanation_engine.v1.PuzzleWinningResult.PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleWinningResult",
  "name": "PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD",
  "number": 1,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14926"></a>
## FND-14926: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14927"></a>
## FND-14927: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_CHECKMATE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_CHECKMATE",
  "number": 1,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14928"></a>
## FND-14928: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_PROMOTION = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_PROMOTION",
  "number": 2,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14929"></a>
## FND-14929: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_ATTACK_THE_KING",
  "number": 3,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14930"></a>
## FND-14930: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_WIN_MATERIAL",
  "number": 4,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14931"></a>
## FND-14931: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_DEFENSE = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_DEFENSE",
  "number": 5,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14932"></a>
## FND-14932: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_PROMOTION_POSITION",
  "number": 6,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14933"></a>
## FND-14933: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.TacticalGoalType",
  "name": "TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE",
  "number": 7,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14934"></a>
## FND-14934: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14935"></a>
## FND-14935: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS",
  "number": 1,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14936"></a>
## FND-14936: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS",
  "number": 2,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14937"></a>
## FND-14937: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES",
  "number": 3,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14938"></a>
## FND-14938: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_RESTRICT_PIECES",
  "number": 4,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14939"></a>
## FND-14939: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_TRADE_PIECES",
  "number": 5,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14940"></a>
## FND-14940: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.StrategicGoalType",
  "name": "STRATEGIC_GOAL_TYPE_ATTACK_THE_KING",
  "number": 6,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14941"></a>
## FND-14941: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14942"></a>
## FND-14942: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATE_IN_1 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_MATE_IN_1",
  "number": 1,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14943"></a>
## FND-14943: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATE_IN_2 = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_MATE_IN_2",
  "number": 2,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14944"></a>
## FND-14944: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_SCHOLARS_MATE",
  "number": 3,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14945"></a>
## FND-14945: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_ENDGAME_TACTICS",
  "number": 4,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14946"></a>
## FND-14946: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_TRAPPED_PIECE",
  "number": 5,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14947"></a>
## FND-14947: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_FORK = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_FORK",
  "number": 6,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14948"></a>
## FND-14948: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_SKEWER = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_SKEWER",
  "number": 7,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14949"></a>
## FND-14949: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_HANGING_PIECE = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_HANGING_PIECE",
  "number": 8,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14950"></a>
## FND-14950: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_DISCOVERY = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_DISCOVERY",
  "number": 9,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14951"></a>
## FND-14951: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_QUEEN_SACRIFICE",
  "number": 10,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14952"></a>
## FND-14952: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_OPPOSITION = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_OPPOSITION",
  "number": 11,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14953"></a>
## FND-14953: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_MATE_IN_3_PLUS",
  "number": 12,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14954"></a>
## FND-14954: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATING_NET = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_MATING_NET",
  "number": 13,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14955"></a>
## FND-14955: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_PAWN_ENDGAME",
  "number": 14,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14956"></a>
## FND-14956: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PROMOTION = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_PROMOTION",
  "number": 15,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14957"></a>
## FND-14957: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_UNDER_PROMOTION",
  "number": 16,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14958"></a>
## FND-14958: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_SACRIFICE = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_SACRIFICE",
  "number": 17,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14959"></a>
## FND-14959: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_BACK_RANK_MATE",
  "number": 18,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
