# native_interfaces — findings 1201–1300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13860"></a>
## FND-13860: Native message: chesscom.explanation_engine.v1.GetSanMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetSanMovesRequest",
  "field": [
    {
      "name": "fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "proto_moves",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveList",
      "oneof_index": 0
    },
    {
      "name": "uci_moves",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.UciMoveList",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "variation"
    },
    {
      "name": "_fen"
    }
  ]
}

### Evidence

- **SRC-0958** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_san_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6dfbca175ca0756997abe740f9f033dbdf13038eee4c20d9a24e090a374e88.bin)

**Source references:** SRC-0958, SRC-1813  
**URL references:** None independently associated  
**Related findings:** FND-13861, FND-13862

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13861"></a>
## FND-13861: chesscom.explanation_engine.v1.GetSanMovesRequest.fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetSanMovesRequest",
  "name": "fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_fen",
  "proto3_optional": true,
  "source_id": "SRC-0958",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0958** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_san_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6dfbca175ca0756997abe740f9f033dbdf13038eee4c20d9a24e090a374e88.bin)

**Source references:** SRC-0958, SRC-1813  
**URL references:** None independently associated  
**Related findings:** FND-13860, FND-13862

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13862"></a>
## FND-13862: chesscom.explanation_engine.v1.GetSanMovesRequest.proto_moves = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetSanMovesRequest",
  "name": "proto_moves",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveList",
  "label": "LABEL_OPTIONAL",
  "oneof": "variation",
  "proto3_optional": false,
  "source_id": "SRC-0958",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0958** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_san_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6dfbca175ca0756997abe740f9f033dbdf13038eee4c20d9a24e090a374e88.bin)

**Source references:** SRC-0958, SRC-1813  
**URL references:** None independently associated  
**Related findings:** FND-13860, FND-13861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13863"></a>
## FND-13863: chesscom.explanation_engine.v1.GetSanMovesRequest.uci_moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetSanMovesRequest",
  "name": "uci_moves",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.UciMoveList",
  "label": "LABEL_OPTIONAL",
  "oneof": "variation",
  "proto3_optional": false,
  "source_id": "SRC-0958",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0958** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_san_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6dfbca175ca0756997abe740f9f033dbdf13038eee4c20d9a24e090a374e88.bin)

**Source references:** SRC-0958, SRC-1813  
**URL references:** None independently associated  
**Related findings:** FND-13860, FND-13861, FND-13862

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13864"></a>
## FND-13864: Native message: chesscom.explanation_engine.v1.GetSanMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetSanMovesResponse",
  "field": [
    {
      "name": "san_moves",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0958** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_san_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6dfbca175ca0756997abe740f9f033dbdf13038eee4c20d9a24e090a374e88.bin)

**Source references:** SRC-0958, SRC-1813  
**URL references:** None independently associated  
**Related findings:** FND-13860, FND-13861, FND-13862

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13865"></a>
## FND-13865: chesscom.explanation_engine.v1.GetSanMovesResponse.san_moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetSanMovesResponse",
  "name": "san_moves",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0958",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0958** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_san_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6dfbca175ca0756997abe740f9f033dbdf13038eee4c20d9a24e090a374e88.bin)

**Source references:** SRC-0958, SRC-1813  
**URL references:** None independently associated  
**Related findings:** FND-13860, FND-13861, FND-13862

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13866"></a>
## FND-13866: Native message: chesscom.explanation_engine.v1.GradeTrainItemMoveRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GradeTrainItemMoveRequest",
  "field": [
    {
      "name": "challenge",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.train.v1.TrainChallenge"
    },
    {
      "name": "original_move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0959** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_grade_train_item_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe1ae37213a8e823007859077d63fef1a8f1cbb748e477e2b22b5a7b768a7277.bin)

**Source references:** SRC-0959, SRC-1885  
**URL references:** None independently associated  
**Related findings:** FND-13867, FND-13868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13867"></a>
## FND-13867: chesscom.explanation_engine.v1.GradeTrainItemMoveRequest.challenge = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GradeTrainItemMoveRequest",
  "name": "challenge",
  "number": 1,
  "type": ".chesscom.train.v1.TrainChallenge",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0959",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0959** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_grade_train_item_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe1ae37213a8e823007859077d63fef1a8f1cbb748e477e2b22b5a7b768a7277.bin)

**Source references:** SRC-0959, SRC-1885  
**URL references:** None independently associated  
**Related findings:** FND-13866, FND-13868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13868"></a>
## FND-13868: chesscom.explanation_engine.v1.GradeTrainItemMoveRequest.original_move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GradeTrainItemMoveRequest",
  "name": "original_move",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0959",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0959** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_grade_train_item_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe1ae37213a8e823007859077d63fef1a8f1cbb748e477e2b22b5a7b768a7277.bin)

**Source references:** SRC-0959, SRC-1885  
**URL references:** None independently associated  
**Related findings:** FND-13866, FND-13867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13869"></a>
## FND-13869: Native message: chesscom.explanation_engine.v1.GradeTrainItemMoveResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GradeTrainItemMoveResponse",
  "field": [
    {
      "name": "grade",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.train.v1.TrainMoveGrade"
    },
    {
      "name": "reply_speech",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    }
  ]
}

### Evidence

- **SRC-0959** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_grade_train_item_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe1ae37213a8e823007859077d63fef1a8f1cbb748e477e2b22b5a7b768a7277.bin)

**Source references:** SRC-0959, SRC-1885  
**URL references:** None independently associated  
**Related findings:** FND-13866, FND-13867, FND-13868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13870"></a>
## FND-13870: chesscom.explanation_engine.v1.GradeTrainItemMoveResponse.grade = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GradeTrainItemMoveResponse",
  "name": "grade",
  "number": 1,
  "type": ".chesscom.train.v1.TrainMoveGrade",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0959",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0959** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_grade_train_item_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe1ae37213a8e823007859077d63fef1a8f1cbb748e477e2b22b5a7b768a7277.bin)

**Source references:** SRC-0959, SRC-1885  
**URL references:** None independently associated  
**Related findings:** FND-13866, FND-13867, FND-13868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13871"></a>
## FND-13871: chesscom.explanation_engine.v1.GradeTrainItemMoveResponse.reply_speech = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GradeTrainItemMoveResponse",
  "name": "reply_speech",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0959",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0959** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_grade_train_item_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fe1ae37213a8e823007859077d63fef1a8f1cbb748e477e2b22b5a7b768a7277.bin)

**Source references:** SRC-0959, SRC-1885  
**URL references:** None independently associated  
**Related findings:** FND-13866, FND-13867, FND-13868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13872"></a>
## FND-13872: Native message: chesscom.explanation_engine.v1.LegalMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LegalMovesRequest"
}

### Evidence

- **SRC-0960** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5e74946fba46279d5fc58d670c38da816d554d8309a89c241ec486417772ada7.bin)

**Source references:** SRC-0960, SRC-1898  
**URL references:** None independently associated  
**Related findings:** FND-13873, FND-13874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13873"></a>
## FND-13873: Native message: chesscom.explanation_engine.v1.LegalMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LegalMovesResponse",
  "field": [
    {
      "name": "legal_moves",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0960** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5e74946fba46279d5fc58d670c38da816d554d8309a89c241ec486417772ada7.bin)

**Source references:** SRC-0960, SRC-1898  
**URL references:** None independently associated  
**Related findings:** FND-13872, FND-13874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13874"></a>
## FND-13874: chesscom.explanation_engine.v1.LegalMovesResponse.legal_moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegalMovesResponse",
  "name": "legal_moves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0960",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0960** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5e74946fba46279d5fc58d670c38da816d554d8309a89c241ec486417772ada7.bin)

**Source references:** SRC-0960, SRC-1898  
**URL references:** None independently associated  
**Related findings:** FND-13872, FND-13873

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13875"></a>
## FND-13875: Native message: chesscom.explanation_engine.v1.LegalPremovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_from"
    },
    {
      "name": "_color"
    }
  ]
}

### Evidence

- **SRC-0961** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_premoves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/947c411fa7cf264bc747ae8e746fcffcbea2277ecfa0659be015704b22aff6f7.bin)

**Source references:** SRC-0961, SRC-1752  
**URL references:** None independently associated  
**Related findings:** FND-13876, FND-13877

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13876"></a>
## FND-13876: chesscom.explanation_engine.v1.LegalPremovesRequest.previous_premoves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegalPremovesRequest",
  "name": "previous_premoves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0961",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0961** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_premoves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/947c411fa7cf264bc747ae8e746fcffcbea2277ecfa0659be015704b22aff6f7.bin)

**Source references:** SRC-0961, SRC-1752  
**URL references:** None independently associated  
**Related findings:** FND-13875, FND-13877

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13877"></a>
## FND-13877: chesscom.explanation_engine.v1.LegalPremovesRequest.from = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegalPremovesRequest",
  "name": "from",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": "_from",
  "proto3_optional": true,
  "source_id": "SRC-0961",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0961** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_premoves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/947c411fa7cf264bc747ae8e746fcffcbea2277ecfa0659be015704b22aff6f7.bin)

**Source references:** SRC-0961, SRC-1752  
**URL references:** None independently associated  
**Related findings:** FND-13875, FND-13876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13878"></a>
## FND-13878: chesscom.explanation_engine.v1.LegalPremovesRequest.color = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegalPremovesRequest",
  "name": "color",
  "number": 3,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": "_color",
  "proto3_optional": true,
  "source_id": "SRC-0961",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0961** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_premoves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/947c411fa7cf264bc747ae8e746fcffcbea2277ecfa0659be015704b22aff6f7.bin)

**Source references:** SRC-0961, SRC-1752  
**URL references:** None independently associated  
**Related findings:** FND-13875, FND-13876, FND-13877

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13879"></a>
## FND-13879: Native message: chesscom.explanation_engine.v1.LegalPremovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0961** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_premoves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/947c411fa7cf264bc747ae8e746fcffcbea2277ecfa0659be015704b22aff6f7.bin)

**Source references:** SRC-0961, SRC-1752  
**URL references:** None independently associated  
**Related findings:** FND-13875, FND-13876, FND-13877

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13880"></a>
## FND-13880: chesscom.explanation_engine.v1.LegalPremovesResponse.legal_premoves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegalPremovesResponse",
  "name": "legal_premoves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0961",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0961** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_legal_premoves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/947c411fa7cf264bc747ae8e746fcffcbea2277ecfa0659be015704b22aff6f7.bin)

**Source references:** SRC-0961, SRC-1752  
**URL references:** None independently associated  
**Related findings:** FND-13875, FND-13876, FND-13877

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13881"></a>
## FND-13881: Native message: chesscom.explanation_engine.v1.LoadAndSetCoachRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadAndSetCoachRequest",
  "field": [
    {
      "name": "text_asset",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TextAsset"
    }
  ]
}

### Evidence

- **SRC-0962** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_and_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9c54c56ed21c412d30bb50451c4ae1e39b9cb4531003f9740c6ec3e12c65021c.bin)

**Source references:** SRC-0962, SRC-1846  
**URL references:** None independently associated  
**Related findings:** FND-13882, FND-13883

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13882"></a>
## FND-13882: chesscom.explanation_engine.v1.LoadAndSetCoachRequest.text_asset = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadAndSetCoachRequest",
  "name": "text_asset",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.TextAsset",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0962",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0962** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_and_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9c54c56ed21c412d30bb50451c4ae1e39b9cb4531003f9740c6ec3e12c65021c.bin)

**Source references:** SRC-0962, SRC-1846  
**URL references:** None independently associated  
**Related findings:** FND-13881, FND-13883

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13883"></a>
## FND-13883: Native message: chesscom.explanation_engine.v1.LoadAndSetCoachResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadAndSetCoachResponse"
}

### Evidence

- **SRC-0962** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_and_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9c54c56ed21c412d30bb50451c4ae1e39b9cb4531003f9740c6ec3e12c65021c.bin)

**Source references:** SRC-0962, SRC-1846  
**URL references:** None independently associated  
**Related findings:** FND-13881, FND-13882

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13884"></a>
## FND-13884: Native message: chesscom.explanation_engine.v1.LoadBotRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadBotRequest",
  "field": [
    {
      "name": "bot_name",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "content_format",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.BotContentFormat"
    },
    {
      "name": "bot_content",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "artifact_id",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13885"></a>
## FND-13885: chesscom.explanation_engine.v1.LoadBotRequest.bot_name = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadBotRequest",
  "name": "bot_name",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13886"></a>
## FND-13886: chesscom.explanation_engine.v1.LoadBotRequest.content_format = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadBotRequest",
  "name": "content_format",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.BotContentFormat",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13887"></a>
## FND-13887: chesscom.explanation_engine.v1.LoadBotRequest.bot_content = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadBotRequest",
  "name": "bot_content",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13888"></a>
## FND-13888: chesscom.explanation_engine.v1.LoadBotRequest.artifact_id = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadBotRequest",
  "name": "artifact_id",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13889"></a>
## FND-13889: Native message: chesscom.explanation_engine.v1.LoadBotResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadBotResponse"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13890"></a>
## FND-13890: chesscom.explanation_engine.v1.BotContentFormat.BOT_CONTENT_FORMAT_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.BotContentFormat",
  "name": "BOT_CONTENT_FORMAT_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13891"></a>
## FND-13891: chesscom.explanation_engine.v1.BotContentFormat.BOT_CONTENT_FORMAT_JSON = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.BotContentFormat",
  "name": "BOT_CONTENT_FORMAT_JSON",
  "number": 1,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13892"></a>
## FND-13892: chesscom.explanation_engine.v1.BotContentFormat.BOT_CONTENT_FORMAT_BASE64 = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.BotContentFormat",
  "name": "BOT_CONTENT_FORMAT_BASE64",
  "number": 2,
  "source_id": "SRC-0963",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0963** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_bot.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4593bf5deb94b296f0e6a3e8635b957bf72ddfcb1d32cfd9343d2972a514d5cd.bin)

**Source references:** SRC-0963, SRC-1669  
**URL references:** None independently associated  
**Related findings:** FND-13884, FND-13885, FND-13886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13893"></a>
## FND-13893: Native message: chesscom.explanation_engine.v1.LoadCharmModelRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadCharmModelRequest",
  "field": [
    {
      "name": "model_path",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    },
    {
      "name": "artifact_id",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    },
    {
      "name": "model_key",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "model_source"
    },
    {
      "name": "_model_key"
    }
  ]
}

### Evidence

- **SRC-0964** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/417612dd25c411b01a1da75ce43bbeb4d1a0918ddfadf0806f0668f189fba2b3.bin)

**Source references:** SRC-0964, SRC-1776  
**URL references:** None independently associated  
**Related findings:** FND-13894, FND-13895

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13894"></a>
## FND-13894: chesscom.explanation_engine.v1.LoadCharmModelRequest.model_path = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadCharmModelRequest",
  "name": "model_path",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "model_source",
  "proto3_optional": false,
  "source_id": "SRC-0964",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0964** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/417612dd25c411b01a1da75ce43bbeb4d1a0918ddfadf0806f0668f189fba2b3.bin)

**Source references:** SRC-0964, SRC-1776  
**URL references:** None independently associated  
**Related findings:** FND-13893, FND-13895

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13895"></a>
## FND-13895: chesscom.explanation_engine.v1.LoadCharmModelRequest.artifact_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadCharmModelRequest",
  "name": "artifact_id",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "model_source",
  "proto3_optional": false,
  "source_id": "SRC-0964",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0964** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/417612dd25c411b01a1da75ce43bbeb4d1a0918ddfadf0806f0668f189fba2b3.bin)

**Source references:** SRC-0964, SRC-1776  
**URL references:** None independently associated  
**Related findings:** FND-13893, FND-13894

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13896"></a>
## FND-13896: chesscom.explanation_engine.v1.LoadCharmModelRequest.model_key = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadCharmModelRequest",
  "name": "model_key",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_model_key",
  "proto3_optional": true,
  "source_id": "SRC-0964",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0964** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/417612dd25c411b01a1da75ce43bbeb4d1a0918ddfadf0806f0668f189fba2b3.bin)

**Source references:** SRC-0964, SRC-1776  
**URL references:** None independently associated  
**Related findings:** FND-13893, FND-13894, FND-13895

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13897"></a>
## FND-13897: Native message: chesscom.explanation_engine.v1.LoadCharmModelResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadCharmModelResponse",
  "field": [
    {
      "name": "model_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0964** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/417612dd25c411b01a1da75ce43bbeb4d1a0918ddfadf0806f0668f189fba2b3.bin)

**Source references:** SRC-0964, SRC-1776  
**URL references:** None independently associated  
**Related findings:** FND-13893, FND-13894, FND-13895

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13898"></a>
## FND-13898: chesscom.explanation_engine.v1.LoadCharmModelResponse.model_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadCharmModelResponse",
  "name": "model_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0964",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0964** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/417612dd25c411b01a1da75ce43bbeb4d1a0918ddfadf0806f0668f189fba2b3.bin)

**Source references:** SRC-0964, SRC-1776  
**URL references:** None independently associated  
**Related findings:** FND-13893, FND-13894, FND-13895

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13899"></a>
## FND-13899: Native message: chesscom.explanation_engine.v1.LoadCoachRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0965** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/506f8ccb268c46d9e120870e146ab2fc8ce21496c3b841971df943f4841701d2.bin)

**Source references:** SRC-0965, SRC-1872  
**URL references:** None independently associated  
**Related findings:** FND-13900, FND-13901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13900"></a>
## FND-13900: chesscom.explanation_engine.v1.LoadCoachRequest.text_asset = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadCoachRequest",
  "name": "text_asset",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.TextAsset",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0965",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0965** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/506f8ccb268c46d9e120870e146ab2fc8ce21496c3b841971df943f4841701d2.bin)

**Source references:** SRC-0965, SRC-1872  
**URL references:** None independently associated  
**Related findings:** FND-13899, FND-13901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13901"></a>
## FND-13901: Native message: chesscom.explanation_engine.v1.LoadCoachResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadCoachResponse"
}

### Evidence

- **SRC-0965** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/506f8ccb268c46d9e120870e146ab2fc8ce21496c3b841971df943f4841701d2.bin)

**Source references:** SRC-0965, SRC-1872  
**URL references:** None independently associated  
**Related findings:** FND-13899, FND-13900

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13902"></a>
## FND-13902: Native message: chesscom.explanation_engine.v1.LoadEcoBookRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadEcoBookRequest",
  "field": [
    {
      "name": "artifact_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0966** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_eco_book.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7ce7207cbe1d83ba9dede34e80c1a17e6531741fded4b5c728145faa2ad7b4d.bin)

**Source references:** SRC-0966, SRC-1831  
**URL references:** None independently associated  
**Related findings:** FND-13903, FND-13904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13903"></a>
## FND-13903: chesscom.explanation_engine.v1.LoadEcoBookRequest.artifact_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadEcoBookRequest",
  "name": "artifact_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0966",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0966** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_eco_book.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7ce7207cbe1d83ba9dede34e80c1a17e6531741fded4b5c728145faa2ad7b4d.bin)

**Source references:** SRC-0966, SRC-1831  
**URL references:** None independently associated  
**Related findings:** FND-13902, FND-13904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13904"></a>
## FND-13904: Native message: chesscom.explanation_engine.v1.LoadEcoBookResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LoadEcoBookResponse",
  "field": [
    {
      "name": "position_count",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    }
  ]
}

### Evidence

- **SRC-0966** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_eco_book.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7ce7207cbe1d83ba9dede34e80c1a17e6531741fded4b5c728145faa2ad7b4d.bin)

**Source references:** SRC-0966, SRC-1831  
**URL references:** None independently associated  
**Related findings:** FND-13902, FND-13903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13905"></a>
## FND-13905: chesscom.explanation_engine.v1.LoadEcoBookResponse.position_count = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadEcoBookResponse",
  "name": "position_count",
  "number": 1,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0966",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0966** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_eco_book.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7ce7207cbe1d83ba9dede34e80c1a17e6531741fded4b5c728145faa2ad7b4d.bin)

**Source references:** SRC-0966, SRC-1831  
**URL references:** None independently associated  
**Related findings:** FND-13902, FND-13903, FND-13904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13906"></a>
## FND-13906: Native message: chesscom.explanation_engine.v1.LoadGameStateRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0967** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/119d7b180e39e720292cba690c8801d516c8b20e1fd2fb1d1b7b87321e67d334.bin)

**Source references:** SRC-0967, SRC-1851  
**URL references:** None independently associated  
**Related findings:** FND-13907, FND-13908

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13907"></a>
## FND-13907: chesscom.explanation_engine.v1.LoadGameStateRequest.game_state = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadGameStateRequest",
  "name": "game_state",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameState",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0967",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0967** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/119d7b180e39e720292cba690c8801d516c8b20e1fd2fb1d1b7b87321e67d334.bin)

**Source references:** SRC-0967, SRC-1851  
**URL references:** None independently associated  
**Related findings:** FND-13906, FND-13908

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13908"></a>
## FND-13908: Native message: chesscom.explanation_engine.v1.LoadGameStateResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0967** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/119d7b180e39e720292cba690c8801d516c8b20e1fd2fb1d1b7b87321e67d334.bin)

**Source references:** SRC-0967, SRC-1851  
**URL references:** None independently associated  
**Related findings:** FND-13906, FND-13907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13909"></a>
## FND-13909: chesscom.explanation_engine.v1.LoadGameStateResponse.played_line = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LoadGameStateResponse",
  "name": "played_line",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0967",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0967** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_load_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/119d7b180e39e720292cba690c8801d516c8b20e1fd2fb1d1b7b87321e67d334.bin)

**Source references:** SRC-0967, SRC-1851  
**URL references:** None independently associated  
**Related findings:** FND-13906, FND-13907, FND-13908

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13910"></a>
## FND-13910: Native message: chesscom.explanation_engine.v1.LuaCompletionRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LuaCompletionRequest"
}

### Evidence

- **SRC-0968** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_lua_completion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e733180481b71adc408d85c18ad97dfdbd939c2b4b5051e46420175530543bd5.bin)

**Source references:** SRC-0968, SRC-1693  
**URL references:** None independently associated  
**Related findings:** FND-13911, FND-13912

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13911"></a>
## FND-13911: Native message: chesscom.explanation_engine.v1.LuaCompletionResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LuaCompletionResponse",
  "field": [
    {
      "name": "items",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0968** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_lua_completion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e733180481b71adc408d85c18ad97dfdbd939c2b4b5051e46420175530543bd5.bin)

**Source references:** SRC-0968, SRC-1693  
**URL references:** None independently associated  
**Related findings:** FND-13910, FND-13912

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13912"></a>
## FND-13912: chesscom.explanation_engine.v1.LuaCompletionResponse.items = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LuaCompletionResponse",
  "name": "items",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0968",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0968** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_lua_completion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e733180481b71adc408d85c18ad97dfdbd939c2b4b5051e46420175530543bd5.bin)

**Source references:** SRC-0968, SRC-1693  
**URL references:** None independently associated  
**Related findings:** FND-13910, FND-13911

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13913"></a>
## FND-13913: Native message: chesscom.explanation_engine.v1.MakeMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MakeMovesRequest",
  "field": [
    {
      "name": "moves",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "is_played_line",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-0969** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_make_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/dba2641bdb3a68f6e99da8257c8a36008426bd72751f6c3ccc8a4fbada624779.bin)

**Source references:** SRC-0969, SRC-1760  
**URL references:** None independently associated  
**Related findings:** FND-13914, FND-13915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13914"></a>
## FND-13914: chesscom.explanation_engine.v1.MakeMovesRequest.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MakeMovesRequest",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0969",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0969** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_make_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/dba2641bdb3a68f6e99da8257c8a36008426bd72751f6c3ccc8a4fbada624779.bin)

**Source references:** SRC-0969, SRC-1760  
**URL references:** None independently associated  
**Related findings:** FND-13913, FND-13915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13915"></a>
## FND-13915: chesscom.explanation_engine.v1.MakeMovesRequest.is_played_line = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MakeMovesRequest",
  "name": "is_played_line",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0969",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0969** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_make_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/dba2641bdb3a68f6e99da8257c8a36008426bd72751f6c3ccc8a4fbada624779.bin)

**Source references:** SRC-0969, SRC-1760  
**URL references:** None independently associated  
**Related findings:** FND-13913, FND-13914

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13916"></a>
## FND-13916: Native message: chesscom.explanation_engine.v1.MakeMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MakeMovesResponse",
  "field": [
    {
      "name": "line",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
    }
  ]
}

### Evidence

- **SRC-0969** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_make_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/dba2641bdb3a68f6e99da8257c8a36008426bd72751f6c3ccc8a4fbada624779.bin)

**Source references:** SRC-0969, SRC-1760  
**URL references:** None independently associated  
**Related findings:** FND-13913, FND-13914, FND-13915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13917"></a>
## FND-13917: chesscom.explanation_engine.v1.MakeMovesResponse.line = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MakeMovesResponse",
  "name": "line",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0969",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0969** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_make_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/dba2641bdb3a68f6e99da8257c8a36008426bd72751f6c3ccc8a4fbada624779.bin)

**Source references:** SRC-0969, SRC-1760  
**URL references:** None independently associated  
**Related findings:** FND-13913, FND-13914, FND-13915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13918"></a>
## FND-13918: Native message: chesscom.explanation_engine.v1.MoveClassificationRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13919"></a>
## FND-13919: chesscom.explanation_engine.v1.MoveClassificationRequest.stream_results = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveClassificationRequest",
  "name": "stream_results",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13920"></a>
## FND-13920: chesscom.explanation_engine.v1.MoveClassificationRequest.enable_pv_classifications = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveClassificationRequest",
  "name": "enable_pv_classifications",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13921"></a>
## FND-13921: Native message: chesscom.explanation_engine.v1.MoveClassificationResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_alternative"
    },
    {
      "name": "_pv_classifications"
    }
  ]
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13922"></a>
## FND-13922: chesscom.explanation_engine.v1.MoveClassificationResponse.active = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveClassificationResponse",
  "name": "active",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.EvalClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13923"></a>
## FND-13923: chesscom.explanation_engine.v1.MoveClassificationResponse.alternative = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveClassificationResponse",
  "name": "alternative",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.AltMoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": "_alternative",
  "proto3_optional": true,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13924"></a>
## FND-13924: chesscom.explanation_engine.v1.MoveClassificationResponse.progress = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveClassificationResponse",
  "name": "progress",
  "number": 3,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13925"></a>
## FND-13925: chesscom.explanation_engine.v1.MoveClassificationResponse.pv_classifications = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveClassificationResponse",
  "name": "pv_classifications",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.PvClassifications",
  "label": "LABEL_OPTIONAL",
  "oneof": "_pv_classifications",
  "proto3_optional": true,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13926"></a>
## FND-13926: Native message: chesscom.explanation_engine.v1.PvClassifications

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13927"></a>
## FND-13927: chesscom.explanation_engine.v1.PvClassifications.classifications = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PvClassifications",
  "name": "classifications",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.EvalClassification",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13928"></a>
## FND-13928: Native message: chesscom.explanation_engine.v1.AltMoveClassification

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13929"></a>
## FND-13929: chesscom.explanation_engine.v1.AltMoveClassification.classification = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AltMoveClassification",
  "name": "classification",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.EvalClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13930"></a>
## FND-13930: chesscom.explanation_engine.v1.AltMoveClassification.move = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AltMoveClassification",
  "name": "move",
  "number": 3,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13931"></a>
## FND-13931: chesscom.explanation_engine.v1.AltMoveClassification.progress = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AltMoveClassification",
  "name": "progress",
  "number": 4,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0970",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0970** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/eb58406636d7284e48a168d8f1adafe8076f51c9163c4a6cf591483e7c2aac4a.bin)

**Source references:** SRC-0970, SRC-1857  
**URL references:** None independently associated  
**Related findings:** FND-13918, FND-13919, FND-13920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13932"></a>
## FND-13932: Native message: chesscom.explanation_engine.v1.NewGameRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0971** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7c3c5ce5217ac2ec14bb10d12b202e76ea4adb5b8bf24d1de7d27ad11d949f7.bin)

**Source references:** SRC-0971, SRC-1704  
**URL references:** None independently associated  
**Related findings:** FND-13933, FND-13934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13933"></a>
## FND-13933: chesscom.explanation_engine.v1.NewGameRequest.new_game = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGameRequest",
  "name": "new_game",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.NewGame",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0971",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0971** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7c3c5ce5217ac2ec14bb10d12b202e76ea4adb5b8bf24d1de7d27ad11d949f7.bin)

**Source references:** SRC-0971, SRC-1704  
**URL references:** None independently associated  
**Related findings:** FND-13932, FND-13934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13934"></a>
## FND-13934: chesscom.explanation_engine.v1.NewGameRequest.enable_typed_invalid_game_errors = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGameRequest",
  "name": "enable_typed_invalid_game_errors",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0971",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0971** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7c3c5ce5217ac2ec14bb10d12b202e76ea4adb5b8bf24d1de7d27ad11d949f7.bin)

**Source references:** SRC-0971, SRC-1704  
**URL references:** None independently associated  
**Related findings:** FND-13932, FND-13933

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13935"></a>
## FND-13935: Native message: chesscom.explanation_engine.v1.NewGameResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_invalid_game"
    }
  ]
}

### Evidence

- **SRC-0971** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7c3c5ce5217ac2ec14bb10d12b202e76ea4adb5b8bf24d1de7d27ad11d949f7.bin)

**Source references:** SRC-0971, SRC-1704  
**URL references:** None independently associated  
**Related findings:** FND-13932, FND-13933, FND-13934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13936"></a>
## FND-13936: chesscom.explanation_engine.v1.NewGameResponse.played_line = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGameResponse",
  "name": "played_line",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0971",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0971** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7c3c5ce5217ac2ec14bb10d12b202e76ea4adb5b8bf24d1de7d27ad11d949f7.bin)

**Source references:** SRC-0971, SRC-1704  
**URL references:** None independently associated  
**Related findings:** FND-13932, FND-13933, FND-13934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13937"></a>
## FND-13937: chesscom.explanation_engine.v1.NewGameResponse.invalid_game = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NewGameResponse",
  "name": "invalid_game",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.InvalidGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "_invalid_game",
  "proto3_optional": true,
  "source_id": "SRC-0971",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0971** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_new_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c7c3c5ce5217ac2ec14bb10d12b202e76ea4adb5b8bf24d1de7d27ad11d949f7.bin)

**Source references:** SRC-0971, SRC-1704  
**URL references:** None independently associated  
**Related findings:** FND-13932, FND-13933, FND-13934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13938"></a>
## FND-13938: Native message: chesscom.explanation_engine.v1.RelaxedApplyMoveRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RelaxedApplyMoveRequest",
  "field": [
    {
      "name": "fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "extra_occupancy",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "move",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13939"></a>
## FND-13939: chesscom.explanation_engine.v1.RelaxedApplyMoveRequest.fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveRequest",
  "name": "fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13940"></a>
## FND-13940: chesscom.explanation_engine.v1.RelaxedApplyMoveRequest.extra_occupancy = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveRequest",
  "name": "extra_occupancy",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13941"></a>
## FND-13941: chesscom.explanation_engine.v1.RelaxedApplyMoveRequest.move = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveRequest",
  "name": "move",
  "number": 3,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13942"></a>
## FND-13942: Native message: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RelaxedApplyMoveResponse",
  "field": [
    {
      "name": "result_fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "result_extra_occupancy",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "captured_opp_piece",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "captured_extra_occ",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "in_check",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "move_san",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13943"></a>
## FND-13943: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse.result_fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveResponse",
  "name": "result_fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13944"></a>
## FND-13944: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse.result_extra_occupancy = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveResponse",
  "name": "result_extra_occupancy",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13945"></a>
## FND-13945: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse.captured_opp_piece = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveResponse",
  "name": "captured_opp_piece",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13946"></a>
## FND-13946: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse.captured_extra_occ = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveResponse",
  "name": "captured_extra_occ",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13947"></a>
## FND-13947: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse.in_check = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveResponse",
  "name": "in_check",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13948"></a>
## FND-13948: chesscom.explanation_engine.v1.RelaxedApplyMoveResponse.move_san = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedApplyMoveResponse",
  "name": "move_san",
  "number": 6,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0972",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0972** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_apply_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7d9a0e274ffeec886cbe572ac9e512b5d55f3767f2f0a22a172214c751baf019.bin)

**Source references:** SRC-0972, SRC-1682  
**URL references:** None independently associated  
**Related findings:** FND-13938, FND-13939, FND-13940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13949"></a>
## FND-13949: Native message: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RelaxedConvertToProtoMovesRequest",
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
      "name": "extra_occupancy",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "moves_to_convert",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13950, FND-13951

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13950"></a>
## FND-13950: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest.move_notation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest",
  "name": "move_notation",
  "number": 1,
  "type": ".chesscom.chess.v1.MoveNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0973",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13949, FND-13951

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13951"></a>
## FND-13951: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest.initial_fen = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest",
  "name": "initial_fen",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0973",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13949, FND-13950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13952"></a>
## FND-13952: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest.extra_occupancy = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest",
  "name": "extra_occupancy",
  "number": 3,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0973",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13949, FND-13950, FND-13951

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13953"></a>
## FND-13953: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest.moves_to_convert = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesRequest",
  "name": "moves_to_convert",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0973",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13949, FND-13950, FND-13951

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13954"></a>
## FND-13954: Native message: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RelaxedConvertToProtoMovesResponse",
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

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13949, FND-13950, FND-13951

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13955"></a>
## FND-13955: chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesResponse.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedConvertToProtoMovesResponse",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0973",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0973** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3cfdfe868095a4b7d934998a842a72801a98a3df8f1503e08ba1f4cd88d4b321.bin)

**Source references:** SRC-0973, SRC-1759  
**URL references:** None independently associated  
**Related findings:** FND-13949, FND-13950, FND-13951

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13956"></a>
## FND-13956: Native message: chesscom.explanation_engine.v1.RelaxedLegalMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RelaxedLegalMovesRequest",
  "field": [
    {
      "name": "fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "extra_occupancy",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-0974** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/211eb4761773e8e58368e3376262410fa7f121e7e0cfe4dcc5fb3310086a33f6.bin)

**Source references:** SRC-0974, SRC-1865  
**URL references:** None independently associated  
**Related findings:** FND-13957, FND-13958

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13957"></a>
## FND-13957: chesscom.explanation_engine.v1.RelaxedLegalMovesRequest.fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedLegalMovesRequest",
  "name": "fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0974",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0974** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/211eb4761773e8e58368e3376262410fa7f121e7e0cfe4dcc5fb3310086a33f6.bin)

**Source references:** SRC-0974, SRC-1865  
**URL references:** None independently associated  
**Related findings:** FND-13956, FND-13958

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13958"></a>
## FND-13958: chesscom.explanation_engine.v1.RelaxedLegalMovesRequest.extra_occupancy = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedLegalMovesRequest",
  "name": "extra_occupancy",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0974",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0974** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/211eb4761773e8e58368e3376262410fa7f121e7e0cfe4dcc5fb3310086a33f6.bin)

**Source references:** SRC-0974, SRC-1865  
**URL references:** None independently associated  
**Related findings:** FND-13956, FND-13957

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13959"></a>
## FND-13959: Native message: chesscom.explanation_engine.v1.RelaxedLegalMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RelaxedLegalMovesResponse",
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

- **SRC-0974** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_relaxed_legal_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/211eb4761773e8e58368e3376262410fa7f121e7e0cfe4dcc5fb3310086a33f6.bin)

**Source references:** SRC-0974, SRC-1865  
**URL references:** None independently associated  
**Related findings:** FND-13956, FND-13957, FND-13958

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
