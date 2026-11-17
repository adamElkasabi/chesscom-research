# native_interfaces — findings 2101–2200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14760"></a>
## FND-14760: chesscom.explanation_engine.v1.MoveDetails.time_taken_ms = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "time_taken_ms",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14761"></a>
## FND-14761: chesscom.explanation_engine.v1.MoveDetails.regular_move = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "regular_move",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.NormalMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "kind",
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14762"></a>
## FND-14762: chesscom.explanation_engine.v1.MoveDetails.castling_move = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "castling_move",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.CastlingMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "kind",
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14763"></a>
## FND-14763: chesscom.explanation_engine.v1.MoveDetails.promotion_move = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "promotion_move",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.PromotionMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "kind",
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14764"></a>
## FND-14764: chesscom.explanation_engine.v1.MoveDetails.en_passant_move = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "en_passant_move",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.EnpassantMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "kind",
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14765"></a>
## FND-14765: chesscom.explanation_engine.v1.MoveDetails.null_move = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "null_move",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.NullMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "kind",
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14766"></a>
## FND-14766: chesscom.explanation_engine.v1.MoveDetails.moved_color = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "moved_color",
  "number": 9,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14767"></a>
## FND-14767: chesscom.explanation_engine.v1.MoveDetails.full_move_number = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "full_move_number",
  "number": 10,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14768"></a>
## FND-14768: chesscom.explanation_engine.v1.MoveDetails.game_result = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "game_result",
  "number": 11,
  "type": ".chesscom.chess.v1.GameResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_result",
  "proto3_optional": true,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14769"></a>
## FND-14769: Native message: chesscom.explanation_engine.v1.MoveList

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-1022** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_list.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ae59d4cd855a7923ae7a7d6a5b08bfc0509eba9fcd2c702a206039fba10aefbe.bin)

**Source references:** SRC-1022, SRC-1692  
**URL references:** None independently associated  
**Related findings:** FND-14770, FND-14771

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14770"></a>
## FND-14770: chesscom.explanation_engine.v1.MoveList.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveList",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1022",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1022** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_list.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ae59d4cd855a7923ae7a7d6a5b08bfc0509eba9fcd2c702a206039fba10aefbe.bin)

**Source references:** SRC-1022, SRC-1692  
**URL references:** None independently associated  
**Related findings:** FND-14769, FND-14771

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14771"></a>
## FND-14771: Native message: chesscom.explanation_engine.v1.UciMoveList

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "UciMoveList",
  "field": [
    {
      "name": "moves",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1022** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_list.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ae59d4cd855a7923ae7a7d6a5b08bfc0509eba9fcd2c702a206039fba10aefbe.bin)

**Source references:** SRC-1022, SRC-1692  
**URL references:** None independently associated  
**Related findings:** FND-14769, FND-14770

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14772"></a>
## FND-14772: chesscom.explanation_engine.v1.UciMoveList.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.UciMoveList",
  "name": "moves",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1022",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1022** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_list.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ae59d4cd855a7923ae7a7d6a5b08bfc0509eba9fcd2c702a206039fba10aefbe.bin)

**Source references:** SRC-1022, SRC-1692  
**URL references:** None independently associated  
**Related findings:** FND-14769, FND-14770, FND-14771

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14773"></a>
## FND-14773: Native message: chesscom.explanation_engine.v1.NewGame

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "from"
    }
  ]
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14774"></a>
## FND-14774: chesscom.explanation_engine.v1.NewGame.game = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGame",
  "name": "game",
  "number": 1,
  "type": ".chesscom.chess.v1.Game",
  "label": "LABEL_OPTIONAL",
  "oneof": "from",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14775"></a>
## FND-14775: chesscom.explanation_engine.v1.NewGame.initial_position = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGame",
  "name": "initial_position",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GameInitialPosition",
  "label": "LABEL_OPTIONAL",
  "oneof": "from",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14776"></a>
## FND-14776: chesscom.explanation_engine.v1.NewGame.tcn_game = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGame",
  "name": "tcn_game",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.TcnGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "from",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14777"></a>
## FND-14777: chesscom.explanation_engine.v1.NewGame.position_with_moves = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGame",
  "name": "position_with_moves",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.PositionWithMoves",
  "label": "LABEL_OPTIONAL",
  "oneof": "from",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14778"></a>
## FND-14778: chesscom.explanation_engine.v1.NewGame.pgn_game = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGame",
  "name": "pgn_game",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.PgnGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "from",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14779"></a>
## FND-14779: chesscom.explanation_engine.v1.NewGame.settings = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGame",
  "name": "settings",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GameSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14780"></a>
## FND-14780: Native message: chesscom.explanation_engine.v1.PositionWithMoves

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "move_list"
    }
  ]
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14781"></a>
## FND-14781: chesscom.explanation_engine.v1.PositionWithMoves.initial_position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PositionWithMoves",
  "name": "initial_position",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameInitialPosition",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14782"></a>
## FND-14782: chesscom.explanation_engine.v1.PositionWithMoves.uci_moves = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PositionWithMoves",
  "name": "uci_moves",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.UciMoveList",
  "label": "LABEL_OPTIONAL",
  "oneof": "move_list",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14783"></a>
## FND-14783: chesscom.explanation_engine.v1.PositionWithMoves.moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PositionWithMoves",
  "name": "moves",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.MoveList",
  "label": "LABEL_OPTIONAL",
  "oneof": "move_list",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14784"></a>
## FND-14784: Native message: chesscom.explanation_engine.v1.GameInitialPosition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "initial_position"
    }
  ]
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14785"></a>
## FND-14785: chesscom.explanation_engine.v1.GameInitialPosition.metadata = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameInitialPosition",
  "name": "metadata",
  "number": 1,
  "type": ".chesscom.chess.v1.GameMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14786"></a>
## FND-14786: chesscom.explanation_engine.v1.GameInitialPosition.position = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameInitialPosition",
  "name": "position",
  "number": 2,
  "type": ".chesscom.chess.v1.Position",
  "label": "LABEL_OPTIONAL",
  "oneof": "initial_position",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14787"></a>
## FND-14787: chesscom.explanation_engine.v1.GameInitialPosition.compressed_position = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameInitialPosition",
  "name": "compressed_position",
  "number": 3,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": "initial_position",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14788"></a>
## FND-14788: chesscom.explanation_engine.v1.GameInitialPosition.fen = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameInitialPosition",
  "name": "fen",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "initial_position",
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14789"></a>
## FND-14789: Native message: chesscom.explanation_engine.v1.PgnGame

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14790"></a>
## FND-14790: chesscom.explanation_engine.v1.PgnGame.pgn = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGame",
  "name": "pgn",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14791"></a>
## FND-14791: chesscom.explanation_engine.v1.PgnGame.take_first_game_only = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGame",
  "name": "take_first_game_only",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14792"></a>
## FND-14792: chesscom.explanation_engine.v1.PgnGame.artifact_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGame",
  "name": "artifact_id",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14793"></a>
## FND-14793: chesscom.explanation_engine.v1.PgnGame.metadata = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGame",
  "name": "metadata",
  "number": 4,
  "type": ".chesscom.chess.v1.GameMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1023",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1023** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b88ac3dc23ccbe200804081a84e18703bf07f17ba09c9400f28009e2d212c528.bin)

**Source references:** SRC-1023, SRC-1858  
**URL references:** None independently associated  
**Related findings:** FND-14773, FND-14774, FND-14775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14794"></a>
## FND-14794: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FenNotation",
  "name": "FEN_NOTATION_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1024",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1024** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe145d3ea75409493a842a59e0d16c2c04142e32ab2298a6d6f20a3e17cfbc1e.bin)

**Source references:** SRC-1024, SRC-1838  
**URL references:** None independently associated  
**Related findings:** FND-14795, FND-14796

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14795"></a>
## FND-14795: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_INFERRED = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FenNotation",
  "name": "FEN_NOTATION_INFERRED",
  "number": 1,
  "source_id": "SRC-1024",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1024** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe145d3ea75409493a842a59e0d16c2c04142e32ab2298a6d6f20a3e17cfbc1e.bin)

**Source references:** SRC-1024, SRC-1838  
**URL references:** None independently associated  
**Related findings:** FND-14794, FND-14796

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14796"></a>
## FND-14796: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_STANDARD = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FenNotation",
  "name": "FEN_NOTATION_STANDARD",
  "number": 2,
  "source_id": "SRC-1024",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1024** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe145d3ea75409493a842a59e0d16c2c04142e32ab2298a6d6f20a3e17cfbc1e.bin)

**Source references:** SRC-1024, SRC-1838  
**URL references:** None independently associated  
**Related findings:** FND-14794, FND-14795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14797"></a>
## FND-14797: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_SHREDDER = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FenNotation",
  "name": "FEN_NOTATION_SHREDDER",
  "number": 3,
  "source_id": "SRC-1024",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1024** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe145d3ea75409493a842a59e0d16c2c04142e32ab2298a6d6f20a3e17cfbc1e.bin)

**Source references:** SRC-1024, SRC-1838  
**URL references:** None independently associated  
**Related findings:** FND-14794, FND-14795, FND-14796

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14798"></a>
## FND-14798: Native message: chesscom.explanation_engine.v1.Opening

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Opening",
  "field": [
    {
      "name": "opening_name",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "tcn_moves",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "eco_code",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "url",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 3,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_opening_name"
    },
    {
      "name": "_tcn_moves"
    },
    {
      "name": "_eco_code"
    },
    {
      "name": "_url"
    }
  ]
}

### Evidence

- **SRC-1025** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9fa0011a7b92764789efa9dd20077b951a51dd1f426e5ace53745ccf0302c6ef.bin)

**Source references:** SRC-1025, SRC-1653  
**URL references:** None independently associated  
**Related findings:** FND-14799, FND-14800

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14799"></a>
## FND-14799: chesscom.explanation_engine.v1.Opening.opening_name = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Opening",
  "name": "opening_name",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_opening_name",
  "proto3_optional": true,
  "source_id": "SRC-1025",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1025** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9fa0011a7b92764789efa9dd20077b951a51dd1f426e5ace53745ccf0302c6ef.bin)

**Source references:** SRC-1025, SRC-1653  
**URL references:** None independently associated  
**Related findings:** FND-14798, FND-14800

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14800"></a>
## FND-14800: chesscom.explanation_engine.v1.Opening.tcn_moves = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Opening",
  "name": "tcn_moves",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_tcn_moves",
  "proto3_optional": true,
  "source_id": "SRC-1025",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1025** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9fa0011a7b92764789efa9dd20077b951a51dd1f426e5ace53745ccf0302c6ef.bin)

**Source references:** SRC-1025, SRC-1653  
**URL references:** None independently associated  
**Related findings:** FND-14798, FND-14799

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14801"></a>
## FND-14801: chesscom.explanation_engine.v1.Opening.eco_code = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Opening",
  "name": "eco_code",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_eco_code",
  "proto3_optional": true,
  "source_id": "SRC-1025",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1025** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9fa0011a7b92764789efa9dd20077b951a51dd1f426e5ace53745ccf0302c6ef.bin)

**Source references:** SRC-1025, SRC-1653  
**URL references:** None independently associated  
**Related findings:** FND-14798, FND-14799, FND-14800

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14802"></a>
## FND-14802: chesscom.explanation_engine.v1.Opening.url = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Opening",
  "name": "url",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_url",
  "proto3_optional": true,
  "source_id": "SRC-1025",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1025** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9fa0011a7b92764789efa9dd20077b951a51dd1f426e5ace53745ccf0302c6ef.bin)

**Source references:** SRC-1025, SRC-1653  
**URL references:** None independently associated  
**Related findings:** FND-14798, FND-14799, FND-14800

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14803"></a>
## FND-14803: Native message: chesscom.explanation_engine.v1.PunishMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_arrow"
    },
    {
      "name": "_move"
    }
  ]
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14804, FND-14805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14804"></a>
## FND-14804: chesscom.explanation_engine.v1.PunishMove.arrow = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PunishMove",
  "name": "arrow",
  "number": 1,
  "type": ".chesscom.chess.v1.Arrow",
  "label": "LABEL_OPTIONAL",
  "oneof": "_arrow",
  "proto3_optional": true,
  "source_id": "SRC-1026",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14803, FND-14805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14805"></a>
## FND-14805: chesscom.explanation_engine.v1.PunishMove.evaluation = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PunishMove",
  "name": "evaluation",
  "number": 2,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1026",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14803, FND-14804

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14806"></a>
## FND-14806: chesscom.explanation_engine.v1.PunishMove.speech = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PunishMove",
  "name": "speech",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1026",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14803, FND-14804, FND-14805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14807"></a>
## FND-14807: chesscom.explanation_engine.v1.PunishMove.show_moves = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PunishMove",
  "name": "show_moves",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1026",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14803, FND-14804, FND-14805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14808"></a>
## FND-14808: chesscom.explanation_engine.v1.PunishMove.hide_moves = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PunishMove",
  "name": "hide_moves",
  "number": 5,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1026",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14803, FND-14804, FND-14805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14809"></a>
## FND-14809: chesscom.explanation_engine.v1.PunishMove.move = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PunishMove",
  "name": "move",
  "number": 6,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move",
  "proto3_optional": true,
  "source_id": "SRC-1026",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1026** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/806ddb9cb7b52575926365bd88fa6e021112314d27c9e190c8c2ecbccbfd12db.bin)

**Source references:** SRC-1026, SRC-1788  
**URL references:** None independently associated  
**Related findings:** FND-14803, FND-14804, FND-14805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14810"></a>
## FND-14810: Native message: chesscom.explanation_engine.v1.PuzzleGen

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleGen",
  "field": [
    {
      "name": "puzzle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Puzzle",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "puzzle_game_state",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState"
    },
    {
      "name": "mode",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGenMode"
    },
    {
      "name": "cee_version",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.api.v1.SemanticVersion"
    },
    {
      "name": "puzzle_quality_score",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    }
  ],
  "oneof_decl": [
    {
      "name": "_puzzle"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14811"></a>
## FND-14811: chesscom.explanation_engine.v1.PuzzleGen.puzzle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGen",
  "name": "puzzle",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Puzzle",
  "label": "LABEL_OPTIONAL",
  "oneof": "_puzzle",
  "proto3_optional": true,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14812"></a>
## FND-14812: chesscom.explanation_engine.v1.PuzzleGen.puzzle_game_state = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGen",
  "name": "puzzle_game_state",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GameState",
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
**Related findings:** FND-14810, FND-14811

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14813"></a>
## FND-14813: chesscom.explanation_engine.v1.PuzzleGen.mode = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGen",
  "name": "mode",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.PuzzleGenMode",
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

<a id="FND-14814"></a>
## FND-14814: chesscom.explanation_engine.v1.PuzzleGen.cee_version = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGen",
  "name": "cee_version",
  "number": 4,
  "type": ".chesscom.api.v1.SemanticVersion",
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

<a id="FND-14815"></a>
## FND-14815: chesscom.explanation_engine.v1.PuzzleGen.puzzle_quality_score = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGen",
  "name": "puzzle_quality_score",
  "number": 5,
  "type": "TYPE_FLOAT",
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

<a id="FND-14816"></a>
## FND-14816: Native message: chesscom.explanation_engine.v1.Puzzle

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Puzzle",
  "field": [
    {
      "name": "annotated_puzzle_pgn",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "initial_fen",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "puzzle_moves",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleMove"
    },
    {
      "name": "puzzle_themes",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleTheme"
    },
    {
      "name": "puzzle_goal",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGoal",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "game_phase",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase"
    },
    {
      "name": "origin_game_metadata",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMetadata",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "puzzle_goal_speech",
      "number": 8,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SpeechForLocale"
    },
    {
      "name": "initial_position",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Position"
    },
    {
      "name": "puzzle_result",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleResult"
    },
    {
      "name": "origin_game_ply",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_puzzle_goal"
    },
    {
      "name": "_origin_game_metadata"
    },
    {
      "name": "_origin_game_ply"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14817"></a>
## FND-14817: chesscom.explanation_engine.v1.Puzzle.annotated_puzzle_pgn = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "annotated_puzzle_pgn",
  "number": 1,
  "type": "TYPE_STRING",
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

<a id="FND-14818"></a>
## FND-14818: chesscom.explanation_engine.v1.Puzzle.initial_fen = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "initial_fen",
  "number": 2,
  "type": "TYPE_STRING",
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

<a id="FND-14819"></a>
## FND-14819: chesscom.explanation_engine.v1.Puzzle.puzzle_moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "puzzle_moves",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.PuzzleMove",
  "label": "LABEL_REPEATED",
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

<a id="FND-14820"></a>
## FND-14820: chesscom.explanation_engine.v1.Puzzle.puzzle_themes = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "puzzle_themes",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.PuzzleTheme",
  "label": "LABEL_REPEATED",
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

<a id="FND-14821"></a>
## FND-14821: chesscom.explanation_engine.v1.Puzzle.puzzle_goal = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "puzzle_goal",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.PuzzleGoal",
  "label": "LABEL_OPTIONAL",
  "oneof": "_puzzle_goal",
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

<a id="FND-14822"></a>
## FND-14822: chesscom.explanation_engine.v1.Puzzle.game_phase = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "game_phase",
  "number": 6,
  "type": ".chesscom.chess.v1.GamePhase",
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

<a id="FND-14823"></a>
## FND-14823: chesscom.explanation_engine.v1.Puzzle.origin_game_metadata = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "origin_game_metadata",
  "number": 7,
  "type": ".chesscom.chess.v1.GameMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": "_origin_game_metadata",
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

<a id="FND-14824"></a>
## FND-14824: chesscom.explanation_engine.v1.Puzzle.puzzle_goal_speech = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "puzzle_goal_speech",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.SpeechForLocale",
  "label": "LABEL_REPEATED",
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

<a id="FND-14825"></a>
## FND-14825: chesscom.explanation_engine.v1.Puzzle.initial_position = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "initial_position",
  "number": 9,
  "type": ".chesscom.chess.v1.Position",
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

<a id="FND-14826"></a>
## FND-14826: chesscom.explanation_engine.v1.Puzzle.puzzle_result = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "puzzle_result",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1.PuzzleResult",
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

<a id="FND-14827"></a>
## FND-14827: chesscom.explanation_engine.v1.Puzzle.origin_game_ply = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.Puzzle",
  "name": "origin_game_ply",
  "number": 11,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_origin_game_ply",
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

<a id="FND-14828"></a>
## FND-14828: Native message: chesscom.explanation_engine.v1.PuzzleMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleMove",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "classification",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "puzzle_hint_speech",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SpeechForLocale"
    },
    {
      "name": "legal_alternate_moves",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14829"></a>
## FND-14829: chesscom.explanation_engine.v1.PuzzleMove.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleMove",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
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

<a id="FND-14830"></a>
## FND-14830: chesscom.explanation_engine.v1.PuzzleMove.classification = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleMove",
  "name": "classification",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
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

<a id="FND-14831"></a>
## FND-14831: chesscom.explanation_engine.v1.PuzzleMove.puzzle_hint_speech = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleMove",
  "name": "puzzle_hint_speech",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.SpeechForLocale",
  "label": "LABEL_REPEATED",
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

<a id="FND-14832"></a>
## FND-14832: chesscom.explanation_engine.v1.PuzzleMove.legal_alternate_moves = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleMove",
  "name": "legal_alternate_moves",
  "number": 4,
  "type": "TYPE_INT32",
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

<a id="FND-14833"></a>
## FND-14833: Native message: chesscom.explanation_engine.v1.PuzzleResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleResult",
  "field": [
    {
      "name": "winning_result",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleWinningResult",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "result"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14834"></a>
## FND-14834: chesscom.explanation_engine.v1.PuzzleResult.winning_result = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleResult",
  "name": "winning_result",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleWinningResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
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

<a id="FND-14835"></a>
## FND-14835: Native message: chesscom.explanation_engine.v1.PuzzleGoal

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleGoal",
  "field": [
    {
      "name": "tactical_goal",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TacticalGoal",
      "oneof_index": 0
    },
    {
      "name": "strategic_goal",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.StrategicGoal",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "goal_type"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14836"></a>
## FND-14836: chesscom.explanation_engine.v1.PuzzleGoal.tactical_goal = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGoal",
  "name": "tactical_goal",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.TacticalGoal",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal_type",
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

<a id="FND-14837"></a>
## FND-14837: chesscom.explanation_engine.v1.PuzzleGoal.strategic_goal = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGoal",
  "name": "strategic_goal",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.StrategicGoal",
  "label": "LABEL_OPTIONAL",
  "oneof": "goal_type",
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

<a id="FND-14838"></a>
## FND-14838: Native message: chesscom.explanation_engine.v1.PuzzleTheme

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleTheme",
  "field": [
    {
      "name": "mate_in_1",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn1",
      "oneof_index": 0
    },
    {
      "name": "mate_in_2",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn2",
      "oneof_index": 0
    },
    {
      "name": "scholars_mate",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeScholarsMate",
      "oneof_index": 0
    },
    {
      "name": "endgame_tactics",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics",
      "oneof_index": 0
    },
    {
      "name": "trapped_piece",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece",
      "oneof_index": 0
    },
    {
      "name": "fork",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeFork",
      "oneof_index": 0
    },
    {
      "name": "skewer",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeSkewer",
      "oneof_index": 0
    },
    {
      "name": "hanging_piece",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeHangingPiece",
      "oneof_index": 0
    },
    {
      "name": "discovery",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeDiscovery",
      "oneof_index": 0
    },
    {
      "name": "queen_sacrifice",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice",
      "oneof_index": 0
    },
    {
      "name": "opposition",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeOpposition",
      "oneof_index": 0
    },
    {
      "name": "mate_in_3_plus",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus",
      "oneof_index": 0
    },
    {
      "name": "mating_net",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMatingNet",
      "oneof_index": 0
    },
    {
      "name": "pawn_endgame",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePawnEndgame",
      "oneof_index": 0
    },
    {
      "name": "promotion",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePromotion",
      "oneof_index": 0
    },
    {
      "name": "under_promotion",
      "number": 16,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion",
      "oneof_index": 0
    },
    {
      "name": "sacrifice",
      "number": 17,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeSacrifice",
      "oneof_index": 0
    },
    {
      "name": "back_rank_mate",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeBackRankMate",
      "oneof_index": 0
    },
    {
      "name": "pin",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePin",
      "oneof_index": 0
    },
    {
      "name": "king_safety",
      "number": 20,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeKingSafety",
      "oneof_index": 0
    },
    {
      "name": "piece_play",
      "number": 21,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePiecePlay",
      "oneof_index": 0
    },
    {
      "name": "pawn_structure",
      "number": 22,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePawnStructure",
      "oneof_index": 0
    },
    {
      "name": "ladder_mate",
      "number": 23,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeLadderMate",
      "oneof_index": 0
    },
    {
      "name": "theme_type",
      "number": 255,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeType"
    }
  ],
  "oneof_decl": [
    {
      "name": "theme"
    }
  ]
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14839"></a>
## FND-14839: chesscom.explanation_engine.v1.PuzzleTheme.mate_in_1 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "mate_in_1",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn1",
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

<a id="FND-14840"></a>
## FND-14840: chesscom.explanation_engine.v1.PuzzleTheme.mate_in_2 = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "mate_in_2",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn2",
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

<a id="FND-14841"></a>
## FND-14841: chesscom.explanation_engine.v1.PuzzleTheme.scholars_mate = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "scholars_mate",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeScholarsMate",
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

<a id="FND-14842"></a>
## FND-14842: chesscom.explanation_engine.v1.PuzzleTheme.endgame_tactics = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "endgame_tactics",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics",
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

<a id="FND-14843"></a>
## FND-14843: chesscom.explanation_engine.v1.PuzzleTheme.trapped_piece = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "trapped_piece",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece",
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

<a id="FND-14844"></a>
## FND-14844: chesscom.explanation_engine.v1.PuzzleTheme.fork = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "fork",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeFork",
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

<a id="FND-14845"></a>
## FND-14845: chesscom.explanation_engine.v1.PuzzleTheme.skewer = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "skewer",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeSkewer",
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

<a id="FND-14846"></a>
## FND-14846: chesscom.explanation_engine.v1.PuzzleTheme.hanging_piece = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "hanging_piece",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeHangingPiece",
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

<a id="FND-14847"></a>
## FND-14847: chesscom.explanation_engine.v1.PuzzleTheme.discovery = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "discovery",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeDiscovery",
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

<a id="FND-14848"></a>
## FND-14848: chesscom.explanation_engine.v1.PuzzleTheme.queen_sacrifice = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "queen_sacrifice",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice",
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

<a id="FND-14849"></a>
## FND-14849: chesscom.explanation_engine.v1.PuzzleTheme.opposition = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "opposition",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeOpposition",
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

<a id="FND-14850"></a>
## FND-14850: chesscom.explanation_engine.v1.PuzzleTheme.mate_in_3_plus = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "mate_in_3_plus",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus",
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

<a id="FND-14851"></a>
## FND-14851: chesscom.explanation_engine.v1.PuzzleTheme.mating_net = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "mating_net",
  "number": 13,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeMatingNet",
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

<a id="FND-14852"></a>
## FND-14852: chesscom.explanation_engine.v1.PuzzleTheme.pawn_endgame = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "pawn_endgame",
  "number": 14,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemePawnEndgame",
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

<a id="FND-14853"></a>
## FND-14853: chesscom.explanation_engine.v1.PuzzleTheme.promotion = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "promotion",
  "number": 15,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemePromotion",
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

<a id="FND-14854"></a>
## FND-14854: chesscom.explanation_engine.v1.PuzzleTheme.under_promotion = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "under_promotion",
  "number": 16,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion",
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

<a id="FND-14855"></a>
## FND-14855: chesscom.explanation_engine.v1.PuzzleTheme.sacrifice = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "sacrifice",
  "number": 17,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeSacrifice",
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

<a id="FND-14856"></a>
## FND-14856: chesscom.explanation_engine.v1.PuzzleTheme.back_rank_mate = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "back_rank_mate",
  "number": 18,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeBackRankMate",
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

<a id="FND-14857"></a>
## FND-14857: chesscom.explanation_engine.v1.PuzzleTheme.pin = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "pin",
  "number": 19,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemePin",
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

<a id="FND-14858"></a>
## FND-14858: chesscom.explanation_engine.v1.PuzzleTheme.king_safety = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "king_safety",
  "number": 20,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemeKingSafety",
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

<a id="FND-14859"></a>
## FND-14859: chesscom.explanation_engine.v1.PuzzleTheme.piece_play = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleTheme",
  "name": "piece_play",
  "number": 21,
  "type": ".chesscom.explanation_engine.v1.PuzzleThemePiecePlay",
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
