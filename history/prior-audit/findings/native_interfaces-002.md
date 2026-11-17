# native_interfaces — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12760"></a>
## FND-12760: chesscom.chess.v1.GamePhase.GAME_PHASE_OPENING = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.GamePhase",
  "name": "GAME_PHASE_OPENING",
  "number": 1,
  "source_id": "SRC-0884",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0884** `research/refinement/wasm-descriptors/chesscom_chess_v1_game_phase.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d6f84b0a3e21ebc8a831c74cb5212ed8b1f0d5b500adc0da6f34ff140ea73062.bin)

**Source references:** SRC-0884, SRC-1884  
**URL references:** None independently associated  
**Related findings:** FND-12759, FND-12761

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12761"></a>
## FND-12761: chesscom.chess.v1.GamePhase.GAME_PHASE_MIDDLEGAME = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.GamePhase",
  "name": "GAME_PHASE_MIDDLEGAME",
  "number": 2,
  "source_id": "SRC-0884",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0884** `research/refinement/wasm-descriptors/chesscom_chess_v1_game_phase.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d6f84b0a3e21ebc8a831c74cb5212ed8b1f0d5b500adc0da6f34ff140ea73062.bin)

**Source references:** SRC-0884, SRC-1884  
**URL references:** None independently associated  
**Related findings:** FND-12759, FND-12760

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12762"></a>
## FND-12762: chesscom.chess.v1.GamePhase.GAME_PHASE_ENDGAME = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.GamePhase",
  "name": "GAME_PHASE_ENDGAME",
  "number": 3,
  "source_id": "SRC-0884",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0884** `research/refinement/wasm-descriptors/chesscom_chess_v1_game_phase.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d6f84b0a3e21ebc8a831c74cb5212ed8b1f0d5b500adc0da6f34ff140ea73062.bin)

**Source references:** SRC-0884, SRC-1884  
**URL references:** None independently associated  
**Related findings:** FND-12759, FND-12760, FND-12761

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12763"></a>
## FND-12763: Native message: chesscom.chess.v1.HeadToHeadRecord

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "HeadToHeadRecord",
  "field": [
    {
      "name": "wins",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "draws",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "losses",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    }
  ]
}

### Evidence

- **SRC-0885** `research/refinement/wasm-descriptors/chesscom_chess_v1_head_to_head_record.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5de88c13f2e866bf6208133de83f0eff98330ab1b397b95fcb5f583a946d905a.bin)

**Source references:** SRC-0885, SRC-1724  
**URL references:** None independently associated  
**Related findings:** FND-12764, FND-12765

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12764"></a>
## FND-12764: chesscom.chess.v1.HeadToHeadRecord.wins = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.HeadToHeadRecord",
  "name": "wins",
  "number": 1,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0885",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0885** `research/refinement/wasm-descriptors/chesscom_chess_v1_head_to_head_record.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5de88c13f2e866bf6208133de83f0eff98330ab1b397b95fcb5f583a946d905a.bin)

**Source references:** SRC-0885, SRC-1724  
**URL references:** None independently associated  
**Related findings:** FND-12763, FND-12765

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12765"></a>
## FND-12765: chesscom.chess.v1.HeadToHeadRecord.draws = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.HeadToHeadRecord",
  "name": "draws",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0885",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0885** `research/refinement/wasm-descriptors/chesscom_chess_v1_head_to_head_record.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5de88c13f2e866bf6208133de83f0eff98330ab1b397b95fcb5f583a946d905a.bin)

**Source references:** SRC-0885, SRC-1724  
**URL references:** None independently associated  
**Related findings:** FND-12763, FND-12764

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12766"></a>
## FND-12766: chesscom.chess.v1.HeadToHeadRecord.losses = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.HeadToHeadRecord",
  "name": "losses",
  "number": 3,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0885",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0885** `research/refinement/wasm-descriptors/chesscom_chess_v1_head_to_head_record.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5de88c13f2e866bf6208133de83f0eff98330ab1b397b95fcb5f583a946d905a.bin)

**Source references:** SRC-0885, SRC-1724  
**URL references:** None independently associated  
**Related findings:** FND-12763, FND-12764, FND-12765

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12767"></a>
## FND-12767: Native message: chesscom.chess.v1.CastlingDetails

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CastlingDetails",
  "field": [
    {
      "name": "king_from",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "king_to",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "rook_from",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "rook_to",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12768"></a>
## FND-12768: chesscom.chess.v1.CastlingDetails.king_from = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.CastlingDetails",
  "name": "king_from",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12769"></a>
## FND-12769: chesscom.chess.v1.CastlingDetails.king_to = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.CastlingDetails",
  "name": "king_to",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12770"></a>
## FND-12770: chesscom.chess.v1.CastlingDetails.rook_from = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.CastlingDetails",
  "name": "rook_from",
  "number": 3,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12771"></a>
## FND-12771: chesscom.chess.v1.CastlingDetails.rook_to = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.CastlingDetails",
  "name": "rook_to",
  "number": 4,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12772"></a>
## FND-12772: Native message: chesscom.chess.v1.Move

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Move",
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
      "name": "promotion_piece_type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PromotionPieceType",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "time_taken_ms",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "options": {
        "deprecated": true
      },
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "castling_details",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.CastlingDetails",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "remaining_clock_ms",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "drop_piece_type",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "time_taken_duration",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".google.protobuf.Duration",
      "oneof_index": 5,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_promotion_piece_type"
    },
    {
      "name": "_time_taken_ms"
    },
    {
      "name": "_castling_details"
    },
    {
      "name": "_remaining_clock_ms"
    },
    {
      "name": "_drop_piece_type"
    },
    {
      "name": "_time_taken_duration"
    }
  ]
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12773"></a>
## FND-12773: chesscom.chess.v1.Move.from = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "from",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12774"></a>
## FND-12774: chesscom.chess.v1.Move.to = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "to",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12775"></a>
## FND-12775: chesscom.chess.v1.Move.promotion_piece_type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "promotion_piece_type",
  "number": 3,
  "type": ".chesscom.chess.v1.PromotionPieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": "_promotion_piece_type",
  "proto3_optional": true,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12776"></a>
## FND-12776: chesscom.chess.v1.Move.time_taken_ms = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "time_taken_ms",
  "number": 4,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_taken_ms",
  "proto3_optional": true,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12777"></a>
## FND-12777: chesscom.chess.v1.Move.castling_details = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "castling_details",
  "number": 5,
  "type": ".chesscom.chess.v1.CastlingDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": "_castling_details",
  "proto3_optional": true,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12778"></a>
## FND-12778: chesscom.chess.v1.Move.remaining_clock_ms = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "remaining_clock_ms",
  "number": 6,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_remaining_clock_ms",
  "proto3_optional": true,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12779"></a>
## FND-12779: chesscom.chess.v1.Move.drop_piece_type = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "drop_piece_type",
  "number": 7,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": "_drop_piece_type",
  "proto3_optional": true,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12780"></a>
## FND-12780: chesscom.chess.v1.Move.time_taken_duration = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Move",
  "name": "time_taken_duration",
  "number": 8,
  "type": ".google.protobuf.Duration",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_taken_duration",
  "proto3_optional": true,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12781"></a>
## FND-12781: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PromotionPieceType",
  "name": "PROMOTION_PIECE_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12782"></a>
## FND-12782: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_KNIGHT = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PromotionPieceType",
  "name": "PROMOTION_PIECE_TYPE_KNIGHT",
  "number": 1,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12783"></a>
## FND-12783: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_BISHOP = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PromotionPieceType",
  "name": "PROMOTION_PIECE_TYPE_BISHOP",
  "number": 2,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12784"></a>
## FND-12784: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_ROOK = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PromotionPieceType",
  "name": "PROMOTION_PIECE_TYPE_ROOK",
  "number": 3,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12785"></a>
## FND-12785: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_QUEEN = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PromotionPieceType",
  "name": "PROMOTION_PIECE_TYPE_QUEEN",
  "number": 4,
  "source_id": "SRC-0886",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0886** `research/refinement/wasm-descriptors/chesscom_chess_v1_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/96cf8d73617e2a966fc22f123782e7d29544c7bc4d8679073b13d4fa4033abf7.bin)

**Source references:** SRC-0886, SRC-1902  
**URL references:** None independently associated  
**Related findings:** FND-12767, FND-12768, FND-12769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12786"></a>
## FND-12786: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MoveNotation",
  "name": "MOVE_NOTATION_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0887",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0887** `research/refinement/wasm-descriptors/chesscom_chess_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d39a10c69e32cf55690d7e784a181c4549d217aebebde92ddb678702466f0719.bin)

**Source references:** SRC-0887, SRC-1691  
**URL references:** None independently associated  
**Related findings:** FND-12787, FND-12788

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12787"></a>
## FND-12787: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_TCN = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MoveNotation",
  "name": "MOVE_NOTATION_TCN",
  "number": 1,
  "source_id": "SRC-0887",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0887** `research/refinement/wasm-descriptors/chesscom_chess_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d39a10c69e32cf55690d7e784a181c4549d217aebebde92ddb678702466f0719.bin)

**Source references:** SRC-0887, SRC-1691  
**URL references:** None independently associated  
**Related findings:** FND-12786, FND-12788

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12788"></a>
## FND-12788: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_SAN = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MoveNotation",
  "name": "MOVE_NOTATION_SAN",
  "number": 2,
  "source_id": "SRC-0887",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0887** `research/refinement/wasm-descriptors/chesscom_chess_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d39a10c69e32cf55690d7e784a181c4549d217aebebde92ddb678702466f0719.bin)

**Source references:** SRC-0887, SRC-1691  
**URL references:** None independently associated  
**Related findings:** FND-12786, FND-12787

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12789"></a>
## FND-12789: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_UCI_LAN = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MoveNotation",
  "name": "MOVE_NOTATION_UCI_LAN",
  "number": 3,
  "source_id": "SRC-0887",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0887** `research/refinement/wasm-descriptors/chesscom_chess_v1_notation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d39a10c69e32cf55690d7e784a181c4549d217aebebde92ddb678702466f0719.bin)

**Source references:** SRC-0887, SRC-1691  
**URL references:** None independently associated  
**Related findings:** FND-12786, FND-12787, FND-12788

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12790"></a>
## FND-12790: Native message: chesscom.chess.v1.Piece

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Piece",
  "field": [
    {
      "name": "color",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "type",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    }
  ]
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12791"></a>
## FND-12791: chesscom.chess.v1.Piece.color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Piece",
  "name": "color",
  "number": 1,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12792"></a>
## FND-12792: chesscom.chess.v1.Piece.type = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Piece",
  "name": "type",
  "number": 2,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12793"></a>
## FND-12793: chesscom.chess.v1.PieceType.PIECE_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12794"></a>
## FND-12794: chesscom.chess.v1.PieceType.PIECE_TYPE_PAWN = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_PAWN",
  "number": 1,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12795"></a>
## FND-12795: chesscom.chess.v1.PieceType.PIECE_TYPE_KNIGHT = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_KNIGHT",
  "number": 2,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12796"></a>
## FND-12796: chesscom.chess.v1.PieceType.PIECE_TYPE_BISHOP = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_BISHOP",
  "number": 3,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12797"></a>
## FND-12797: chesscom.chess.v1.PieceType.PIECE_TYPE_ROOK = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_ROOK",
  "number": 4,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12798"></a>
## FND-12798: chesscom.chess.v1.PieceType.PIECE_TYPE_QUEEN = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_QUEEN",
  "number": 5,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12799"></a>
## FND-12799: chesscom.chess.v1.PieceType.PIECE_TYPE_KING = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.PieceType",
  "name": "PIECE_TYPE_KING",
  "number": 6,
  "source_id": "SRC-0888",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0888** `research/refinement/wasm-descriptors/chesscom_chess_v1_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/534b298b2a86b833af39713d1cbdacb86f150ce840afec313420a5eb31928fcd.bin)

**Source references:** SRC-0888, SRC-1836  
**URL references:** None independently associated  
**Related findings:** FND-12790, FND-12791, FND-12792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12800"></a>
## FND-12800: Native message: chesscom.chess.v1.Position

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Position",
  "field": [
    {
      "name": "pieces",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Placement"
    },
    {
      "name": "active_color",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "castling_rights",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.CastlingRight"
    },
    {
      "name": "en_passant_square",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "halfmove_clock",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "fullmove_number",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "in_check",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_en_passant_square"
    },
    {
      "name": "_in_check"
    }
  ]
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12801"></a>
## FND-12801: chesscom.chess.v1.Position.pieces = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "pieces",
  "number": 1,
  "type": ".chesscom.chess.v1.Placement",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12802"></a>
## FND-12802: chesscom.chess.v1.Position.active_color = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "active_color",
  "number": 2,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12803"></a>
## FND-12803: chesscom.chess.v1.Position.castling_rights = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "castling_rights",
  "number": 3,
  "type": ".chesscom.chess.v1.CastlingRight",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12804"></a>
## FND-12804: chesscom.chess.v1.Position.en_passant_square = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "en_passant_square",
  "number": 4,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": "_en_passant_square",
  "proto3_optional": true,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12805"></a>
## FND-12805: chesscom.chess.v1.Position.halfmove_clock = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "halfmove_clock",
  "number": 5,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12806"></a>
## FND-12806: chesscom.chess.v1.Position.fullmove_number = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "fullmove_number",
  "number": 6,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12807"></a>
## FND-12807: chesscom.chess.v1.Position.in_check = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Position",
  "name": "in_check",
  "number": 7,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_in_check",
  "proto3_optional": true,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12808"></a>
## FND-12808: Native message: chesscom.chess.v1.Placement

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Placement",
  "field": [
    {
      "name": "piece",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Piece"
    },
    {
      "name": "square",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12809"></a>
## FND-12809: chesscom.chess.v1.Placement.piece = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Placement",
  "name": "piece",
  "number": 1,
  "type": ".chesscom.chess.v1.Piece",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12810"></a>
## FND-12810: chesscom.chess.v1.Placement.square = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Placement",
  "name": "square",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12811"></a>
## FND-12811: Native message: chesscom.chess.v1.CastlingRight

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CastlingRight",
  "field": [
    {
      "name": "color",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "rook_file",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.File"
    }
  ]
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12812"></a>
## FND-12812: chesscom.chess.v1.CastlingRight.color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.CastlingRight",
  "name": "color",
  "number": 1,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12813"></a>
## FND-12813: chesscom.chess.v1.CastlingRight.rook_file = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.CastlingRight",
  "name": "rook_file",
  "number": 2,
  "type": ".chesscom.chess.v1.File",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0889",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0889** `research/refinement/wasm-descriptors/chesscom_chess_v1_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/de13fbfdd5ef0f43b4b509fd181a3b2a68ccb82958777a90ba1eccf323ae6d60.bin)

**Source references:** SRC-0889, SRC-1708  
**URL references:** None independently associated  
**Related findings:** FND-12800, FND-12801, FND-12802

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12814"></a>
## FND-12814: chesscom.chess.v1.Rank.RANK_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12815"></a>
## FND-12815: chesscom.chess.v1.Rank.RANK_1 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_1",
  "number": 1,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12816"></a>
## FND-12816: chesscom.chess.v1.Rank.RANK_2 = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_2",
  "number": 2,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12817"></a>
## FND-12817: chesscom.chess.v1.Rank.RANK_3 = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_3",
  "number": 3,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12818"></a>
## FND-12818: chesscom.chess.v1.Rank.RANK_4 = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_4",
  "number": 4,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12819"></a>
## FND-12819: chesscom.chess.v1.Rank.RANK_5 = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_5",
  "number": 5,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12820"></a>
## FND-12820: chesscom.chess.v1.Rank.RANK_6 = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_6",
  "number": 6,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12821"></a>
## FND-12821: chesscom.chess.v1.Rank.RANK_7 = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_7",
  "number": 7,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12822"></a>
## FND-12822: chesscom.chess.v1.Rank.RANK_8 = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Rank",
  "name": "RANK_8",
  "number": 8,
  "source_id": "SRC-0890",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0890** `research/refinement/wasm-descriptors/chesscom_chess_v1_rank.proto.bin` — [preserved redacted evidence](../evidence/descriptors/626673362fc4c722328e562d187ec8e870a7c87f03dc236ad45814f7098a5cd6.bin)

**Source references:** SRC-0890, SRC-1866  
**URL references:** None independently associated  
**Related findings:** FND-12814, FND-12815, FND-12816

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12823"></a>
## FND-12823: chesscom.chess.v1.Result.RESULT_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Result",
  "name": "RESULT_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12824"></a>
## FND-12824: chesscom.chess.v1.Result.RESULT_WHITE_WIN = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Result",
  "name": "RESULT_WHITE_WIN",
  "number": 1,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12825"></a>
## FND-12825: chesscom.chess.v1.Result.RESULT_BLACK_WIN = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Result",
  "name": "RESULT_BLACK_WIN",
  "number": 2,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12826"></a>
## FND-12826: chesscom.chess.v1.Result.RESULT_DRAW = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Result",
  "name": "RESULT_DRAW",
  "number": 3,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12827"></a>
## FND-12827: chesscom.chess.v1.Result.RESULT_ABORT = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Result",
  "name": "RESULT_ABORT",
  "number": 4,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12828"></a>
## FND-12828: chesscom.chess.v1.ResultType.RESULT_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12829"></a>
## FND-12829: chesscom.chess.v1.ResultType.RESULT_TYPE_CHECKMATE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_CHECKMATE",
  "number": 1,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12830"></a>
## FND-12830: chesscom.chess.v1.ResultType.RESULT_TYPE_STALEMATE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_STALEMATE",
  "number": 2,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12831"></a>
## FND-12831: chesscom.chess.v1.ResultType.RESULT_TYPE_INSUFFICIENT_MATERIAL = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_INSUFFICIENT_MATERIAL",
  "number": 3,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12832"></a>
## FND-12832: chesscom.chess.v1.ResultType.RESULT_TYPE_RESIGNATION = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_RESIGNATION",
  "number": 4,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12833"></a>
## FND-12833: chesscom.chess.v1.ResultType.RESULT_TYPE_DRAW_OFFER = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_DRAW_OFFER",
  "number": 5,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12834"></a>
## FND-12834: chesscom.chess.v1.ResultType.RESULT_TYPE_TIMEOUT = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_TIMEOUT",
  "number": 6,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12835"></a>
## FND-12835: chesscom.chess.v1.ResultType.RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL",
  "number": 7,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12836"></a>
## FND-12836: chesscom.chess.v1.ResultType.RESULT_TYPE_ABANDONMENT = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_ABANDONMENT",
  "number": 8,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12837"></a>
## FND-12837: chesscom.chess.v1.ResultType.RESULT_TYPE_50_MOVE_RULE = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_50_MOVE_RULE",
  "number": 9,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12838"></a>
## FND-12838: chesscom.chess.v1.ResultType.RESULT_TYPE_THREEFOLD = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_THREEFOLD",
  "number": 10,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12839"></a>
## FND-12839: chesscom.chess.v1.ResultType.RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_BUGHOUSE_PARTNER_LOSE",
  "number": 11,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12840"></a>
## FND-12840: chesscom.chess.v1.ResultType.RESULT_TYPE_THREE_CHECK = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_THREE_CHECK",
  "number": 12,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12841"></a>
## FND-12841: chesscom.chess.v1.ResultType.RESULT_TYPE_KING_OF_THE_HILL = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_KING_OF_THE_HILL",
  "number": 13,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12842"></a>
## FND-12842: chesscom.chess.v1.ResultType.RESULT_TYPE_DOUBLE_FORFEIT = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ResultType",
  "name": "RESULT_TYPE_DOUBLE_FORFEIT",
  "number": 14,
  "source_id": "SRC-0891",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0891** `research/refinement/wasm-descriptors/chesscom_chess_v1_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/778db6e3a10075c4b4f03a14c0fa289774e03e3f607cc9b11846c8d2d911feca.bin)

**Source references:** SRC-0891, SRC-1826  
**URL references:** None independently associated  
**Related findings:** FND-12823, FND-12824, FND-12825

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12843"></a>
## FND-12843: Native message: chesscom.chess.v1.Score

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Score",
  "field": [
    {
      "name": "score_centipawns_white",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_SINT32",
      "oneof_index": 0
    },
    {
      "name": "mate_in_white",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0
    },
    {
      "name": "mate_in_black",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0
    },
    {
      "name": "stalemate",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Stalemate",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "score"
    }
  ]
}

### Evidence

- **SRC-0892** `research/refinement/wasm-descriptors/chesscom_chess_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e543ec4ef90fbe94747241bc9cd62094ea8066caa91cfcf9841a14fdd42f7275.bin)

**Source references:** SRC-0892, SRC-1906  
**URL references:** None independently associated  
**Related findings:** FND-12844, FND-12845

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12844"></a>
## FND-12844: chesscom.chess.v1.Score.score_centipawns_white = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Score",
  "name": "score_centipawns_white",
  "number": 1,
  "type": "TYPE_SINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "score",
  "proto3_optional": false,
  "source_id": "SRC-0892",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0892** `research/refinement/wasm-descriptors/chesscom_chess_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e543ec4ef90fbe94747241bc9cd62094ea8066caa91cfcf9841a14fdd42f7275.bin)

**Source references:** SRC-0892, SRC-1906  
**URL references:** None independently associated  
**Related findings:** FND-12843, FND-12845

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12845"></a>
## FND-12845: chesscom.chess.v1.Score.mate_in_white = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Score",
  "name": "mate_in_white",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "score",
  "proto3_optional": false,
  "source_id": "SRC-0892",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0892** `research/refinement/wasm-descriptors/chesscom_chess_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e543ec4ef90fbe94747241bc9cd62094ea8066caa91cfcf9841a14fdd42f7275.bin)

**Source references:** SRC-0892, SRC-1906  
**URL references:** None independently associated  
**Related findings:** FND-12843, FND-12844

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12846"></a>
## FND-12846: chesscom.chess.v1.Score.mate_in_black = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Score",
  "name": "mate_in_black",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "score",
  "proto3_optional": false,
  "source_id": "SRC-0892",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0892** `research/refinement/wasm-descriptors/chesscom_chess_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e543ec4ef90fbe94747241bc9cd62094ea8066caa91cfcf9841a14fdd42f7275.bin)

**Source references:** SRC-0892, SRC-1906  
**URL references:** None independently associated  
**Related findings:** FND-12843, FND-12844, FND-12845

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12847"></a>
## FND-12847: chesscom.chess.v1.Score.stalemate = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Score",
  "name": "stalemate",
  "number": 4,
  "type": ".chesscom.chess.v1.Stalemate",
  "label": "LABEL_OPTIONAL",
  "oneof": "score",
  "proto3_optional": false,
  "source_id": "SRC-0892",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0892** `research/refinement/wasm-descriptors/chesscom_chess_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e543ec4ef90fbe94747241bc9cd62094ea8066caa91cfcf9841a14fdd42f7275.bin)

**Source references:** SRC-0892, SRC-1906  
**URL references:** None independently associated  
**Related findings:** FND-12843, FND-12844, FND-12845

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12848"></a>
## FND-12848: Native message: chesscom.chess.v1.Stalemate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Stalemate"
}

### Evidence

- **SRC-0892** `research/refinement/wasm-descriptors/chesscom_chess_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e543ec4ef90fbe94747241bc9cd62094ea8066caa91cfcf9841a14fdd42f7275.bin)

**Source references:** SRC-0892, SRC-1906  
**URL references:** None independently associated  
**Related findings:** FND-12843, FND-12844, FND-12845

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12849"></a>
## FND-12849: chesscom.chess.v1.Square.SQUARE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12850"></a>
## FND-12850: chesscom.chess.v1.Square.SQUARE_A1 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_A1",
  "number": 1,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12851"></a>
## FND-12851: chesscom.chess.v1.Square.SQUARE_B1 = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_B1",
  "number": 2,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12852"></a>
## FND-12852: chesscom.chess.v1.Square.SQUARE_C1 = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_C1",
  "number": 3,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12853"></a>
## FND-12853: chesscom.chess.v1.Square.SQUARE_D1 = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_D1",
  "number": 4,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12854"></a>
## FND-12854: chesscom.chess.v1.Square.SQUARE_E1 = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_E1",
  "number": 5,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12855"></a>
## FND-12855: chesscom.chess.v1.Square.SQUARE_F1 = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_F1",
  "number": 6,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12856"></a>
## FND-12856: chesscom.chess.v1.Square.SQUARE_G1 = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_G1",
  "number": 7,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12857"></a>
## FND-12857: chesscom.chess.v1.Square.SQUARE_H1 = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_H1",
  "number": 8,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12858"></a>
## FND-12858: chesscom.chess.v1.Square.SQUARE_A2 = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_A2",
  "number": 9,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12859"></a>
## FND-12859: chesscom.chess.v1.Square.SQUARE_B2 = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Square",
  "name": "SQUARE_B2",
  "number": 10,
  "source_id": "SRC-0893",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0893** `research/refinement/wasm-descriptors/chesscom_chess_v1_square.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ed005b796c3557da5cc0a33087f173cf4a554cae14a6d4342d2ed8950ffb3551.bin)

**Source references:** SRC-0893, SRC-1655  
**URL references:** None independently associated  
**Related findings:** FND-12849, FND-12850, FND-12851

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
