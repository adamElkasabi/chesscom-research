# native_interfaces — findings 1101–1200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13760"></a>
## FND-13760: Native message: chesscom.explanation_engine.v1.GetErgonomicGameResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0945** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/29d7d74cec1b9d103d521cdbeb4313597875bb6a99e2ec21b3dd9561be195cd7.bin)

**Source references:** SRC-0945, SRC-1694  
**URL references:** None independently associated  
**Related findings:** FND-13756, FND-13757, FND-13758

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13761"></a>
## FND-13761: chesscom.explanation_engine.v1.GetErgonomicGameResponse.game = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicGameResponse",
  "name": "game",
  "number": 1,
  "type": ".chesscom.chess.v1.Game",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0945",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0945** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/29d7d74cec1b9d103d521cdbeb4313597875bb6a99e2ec21b3dd9561be195cd7.bin)

**Source references:** SRC-0945, SRC-1694  
**URL references:** None independently associated  
**Related findings:** FND-13756, FND-13757, FND-13758

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13762"></a>
## FND-13762: Native message: chesscom.explanation_engine.v1.GetErgonomicPositionRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetErgonomicPositionRequest",
  "field": [
    {
      "name": "compressed_position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES",
      "oneof_index": 0
    },
    {
      "name": "fen",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "position_to_convert"
    }
  ]
}

### Evidence

- **SRC-0946** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4060c062e8e6f5a967c3a9d1f95e98a913a10ebfddc30e053f163b4a3866b9de.bin)

**Source references:** SRC-0946, SRC-1796  
**URL references:** None independently associated  
**Related findings:** FND-13763, FND-13764

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13763"></a>
## FND-13763: chesscom.explanation_engine.v1.GetErgonomicPositionRequest.compressed_position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicPositionRequest",
  "name": "compressed_position",
  "number": 1,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": "position_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0946",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0946** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4060c062e8e6f5a967c3a9d1f95e98a913a10ebfddc30e053f163b4a3866b9de.bin)

**Source references:** SRC-0946, SRC-1796  
**URL references:** None independently associated  
**Related findings:** FND-13762, FND-13764

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13764"></a>
## FND-13764: chesscom.explanation_engine.v1.GetErgonomicPositionRequest.fen = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicPositionRequest",
  "name": "fen",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "position_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0946",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0946** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4060c062e8e6f5a967c3a9d1f95e98a913a10ebfddc30e053f163b4a3866b9de.bin)

**Source references:** SRC-0946, SRC-1796  
**URL references:** None independently associated  
**Related findings:** FND-13762, FND-13763

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13765"></a>
## FND-13765: Native message: chesscom.explanation_engine.v1.GetErgonomicPositionResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetErgonomicPositionResponse",
  "field": [
    {
      "name": "position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Position"
    }
  ]
}

### Evidence

- **SRC-0946** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4060c062e8e6f5a967c3a9d1f95e98a913a10ebfddc30e053f163b4a3866b9de.bin)

**Source references:** SRC-0946, SRC-1796  
**URL references:** None independently associated  
**Related findings:** FND-13762, FND-13763, FND-13764

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13766"></a>
## FND-13766: chesscom.explanation_engine.v1.GetErgonomicPositionResponse.position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicPositionResponse",
  "name": "position",
  "number": 1,
  "type": ".chesscom.chess.v1.Position",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0946",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0946** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4060c062e8e6f5a967c3a9d1f95e98a913a10ebfddc30e053f163b4a3866b9de.bin)

**Source references:** SRC-0946, SRC-1796  
**URL references:** None independently associated  
**Related findings:** FND-13762, FND-13763, FND-13764

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13767"></a>
## FND-13767: Native message: chesscom.explanation_engine.v1.GetFenRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetFenRequest",
  "field": [
    {
      "name": "position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Position",
      "oneof_index": 0
    },
    {
      "name": "compressed_position",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES",
      "oneof_index": 0
    },
    {
      "name": "fen_notation",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.FenNotation",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "position_to_convert"
    },
    {
      "name": "_fen_notation"
    }
  ]
}

### Evidence

- **SRC-0947** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/78343a343812408000e9cb0ca0d9c4a0b3d8402219ae01943df19eb9376b18a6.bin)

**Source references:** SRC-0947, SRC-1674  
**URL references:** None independently associated  
**Related findings:** FND-13768, FND-13769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13768"></a>
## FND-13768: chesscom.explanation_engine.v1.GetFenRequest.position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetFenRequest",
  "name": "position",
  "number": 1,
  "type": ".chesscom.chess.v1.Position",
  "label": "LABEL_OPTIONAL",
  "oneof": "position_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0947",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0947** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/78343a343812408000e9cb0ca0d9c4a0b3d8402219ae01943df19eb9376b18a6.bin)

**Source references:** SRC-0947, SRC-1674  
**URL references:** None independently associated  
**Related findings:** FND-13767, FND-13769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13769"></a>
## FND-13769: chesscom.explanation_engine.v1.GetFenRequest.compressed_position = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetFenRequest",
  "name": "compressed_position",
  "number": 2,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": "position_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0947",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0947** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/78343a343812408000e9cb0ca0d9c4a0b3d8402219ae01943df19eb9376b18a6.bin)

**Source references:** SRC-0947, SRC-1674  
**URL references:** None independently associated  
**Related findings:** FND-13767, FND-13768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13770"></a>
## FND-13770: chesscom.explanation_engine.v1.GetFenRequest.fen_notation = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetFenRequest",
  "name": "fen_notation",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.FenNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": "_fen_notation",
  "proto3_optional": true,
  "source_id": "SRC-0947",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0947** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/78343a343812408000e9cb0ca0d9c4a0b3d8402219ae01943df19eb9376b18a6.bin)

**Source references:** SRC-0947, SRC-1674  
**URL references:** None independently associated  
**Related findings:** FND-13767, FND-13768, FND-13769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13771"></a>
## FND-13771: Native message: chesscom.explanation_engine.v1.GetFenResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetFenResponse",
  "field": [
    {
      "name": "fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0947** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/78343a343812408000e9cb0ca0d9c4a0b3d8402219ae01943df19eb9376b18a6.bin)

**Source references:** SRC-0947, SRC-1674  
**URL references:** None independently associated  
**Related findings:** FND-13767, FND-13768, FND-13769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13772"></a>
## FND-13772: chesscom.explanation_engine.v1.GetFenResponse.fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetFenResponse",
  "name": "fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0947",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0947** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/78343a343812408000e9cb0ca0d9c4a0b3d8402219ae01943df19eb9376b18a6.bin)

**Source references:** SRC-0947, SRC-1674  
**URL references:** None independently associated  
**Related findings:** FND-13767, FND-13768, FND-13769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13773"></a>
## FND-13773: Native message: chesscom.explanation_engine.v1.GetGameResultRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetGameResultRequest"
}

### Evidence

- **SRC-0948** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/98a8085edf0c38af2c6bc3137f9604de65091ccee0d4eb9388955bfdba3ef801.bin)

**Source references:** SRC-0948, SRC-1710  
**URL references:** None independently associated  
**Related findings:** FND-13774, FND-13775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13774"></a>
## FND-13774: Native message: chesscom.explanation_engine.v1.GetGameResultResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetGameResultResponse",
  "field": [
    {
      "name": "game_result",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameResult",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_game_result"
    }
  ]
}

### Evidence

- **SRC-0948** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/98a8085edf0c38af2c6bc3137f9604de65091ccee0d4eb9388955bfdba3ef801.bin)

**Source references:** SRC-0948, SRC-1710  
**URL references:** None independently associated  
**Related findings:** FND-13773, FND-13775

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13775"></a>
## FND-13775: chesscom.explanation_engine.v1.GetGameResultResponse.game_result = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameResultResponse",
  "name": "game_result",
  "number": 1,
  "type": ".chesscom.chess.v1.GameResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_result",
  "proto3_optional": true,
  "source_id": "SRC-0948",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0948** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/98a8085edf0c38af2c6bc3137f9604de65091ccee0d4eb9388955bfdba3ef801.bin)

**Source references:** SRC-0948, SRC-1710  
**URL references:** None independently associated  
**Related findings:** FND-13773, FND-13774

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13776"></a>
## FND-13776: Native message: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetGameReviewEvaluationsRequest",
  "field": [
    {
      "name": "game_review_search_settings",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameReviewSearchSettings"
    },
    {
      "name": "search_moves",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "engine_id",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "guarantee_nodes",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "guarantee_nodes_null_move",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "disable_maia",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "evaluate_sacrifice_acceptance",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "torch_search_mode",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TorchSearchMode",
      "oneof_index": 5,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_engine_id"
    },
    {
      "name": "_guarantee_nodes"
    },
    {
      "name": "_guarantee_nodes_null_move"
    },
    {
      "name": "_disable_maia"
    },
    {
      "name": "_evaluate_sacrifice_acceptance"
    },
    {
      "name": "_torch_search_mode"
    }
  ]
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13777"></a>
## FND-13777: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.game_review_search_settings = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "game_review_search_settings",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13778"></a>
## FND-13778: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.search_moves = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "search_moves",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13779"></a>
## FND-13779: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.engine_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "engine_id",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine_id",
  "proto3_optional": true,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13780"></a>
## FND-13780: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.guarantee_nodes = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "guarantee_nodes",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_guarantee_nodes",
  "proto3_optional": true,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13781"></a>
## FND-13781: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.guarantee_nodes_null_move = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "guarantee_nodes_null_move",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_guarantee_nodes_null_move",
  "proto3_optional": true,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13782"></a>
## FND-13782: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.disable_maia = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "disable_maia",
  "number": 6,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_disable_maia",
  "proto3_optional": true,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13783"></a>
## FND-13783: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.evaluate_sacrifice_acceptance = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "evaluate_sacrifice_acceptance",
  "number": 7,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_evaluate_sacrifice_acceptance",
  "proto3_optional": true,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13784"></a>
## FND-13784: chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest.torch_search_mode = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsRequest",
  "name": "torch_search_mode",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.TorchSearchMode",
  "label": "LABEL_OPTIONAL",
  "oneof": "_torch_search_mode",
  "proto3_optional": true,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13785"></a>
## FND-13785: Native message: chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetGameReviewEvaluationsResponse",
  "field": [
    {
      "name": "evaluations",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Evaluation"
    },
    {
      "name": "progress",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "aborted",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "log",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13786"></a>
## FND-13786: chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse.evaluations = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse",
  "name": "evaluations",
  "number": 1,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13787"></a>
## FND-13787: chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse.progress = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse",
  "name": "progress",
  "number": 2,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13788"></a>
## FND-13788: chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse.aborted = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse",
  "name": "aborted",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13789"></a>
## FND-13789: chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse.log = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameReviewEvaluationsResponse",
  "name": "log",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0949",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0949** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_review_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e0c9416ff28480055ef9adb57dd7b349896f57fcb3cd22fc9016be3fbd335148.bin)

**Source references:** SRC-0949, SRC-1727  
**URL references:** None independently associated  
**Related findings:** FND-13776, FND-13777, FND-13778

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13790"></a>
## FND-13790: Native message: chesscom.explanation_engine.v1.GetGameStateRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetGameStateRequest"
}

### Evidence

- **SRC-0950** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/318b8a5d260117b61061c7b899aa7652a58e3caa953bcd46ba7ed7a04879bd8a.bin)

**Source references:** SRC-0950, SRC-1839  
**URL references:** None independently associated  
**Related findings:** FND-13791, FND-13792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13791"></a>
## FND-13791: Native message: chesscom.explanation_engine.v1.GetGameStateResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0950** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/318b8a5d260117b61061c7b899aa7652a58e3caa953bcd46ba7ed7a04879bd8a.bin)

**Source references:** SRC-0950, SRC-1839  
**URL references:** None independently associated  
**Related findings:** FND-13790, FND-13792

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13792"></a>
## FND-13792: chesscom.explanation_engine.v1.GetGameStateResponse.game_state = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetGameStateResponse",
  "name": "game_state",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameState",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0950",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0950** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/318b8a5d260117b61061c7b899aa7652a58e3caa953bcd46ba7ed7a04879bd8a.bin)

**Source references:** SRC-0950, SRC-1839  
**URL references:** None independently associated  
**Related findings:** FND-13790, FND-13791

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13793"></a>
## FND-13793: Native message: chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetIllegalMoveExplanationRequest",
  "field": [
    {
      "name": "attempted_move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13794"></a>
## FND-13794: chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest.attempted_move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest",
  "name": "attempted_move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13795"></a>
## FND-13795: Native message: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetIllegalMoveExplanationResponse",
  "field": [
    {
      "name": "illegal_move_case",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.IllegalMoveCase",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "speech",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "board_markings",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.BoardMarkings"
    }
  ],
  "oneof_decl": [
    {
      "name": "_illegal_move_case"
    }
  ]
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13796"></a>
## FND-13796: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse.illegal_move_case = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse",
  "name": "illegal_move_case",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.IllegalMoveCase",
  "label": "LABEL_OPTIONAL",
  "oneof": "_illegal_move_case",
  "proto3_optional": true,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13797"></a>
## FND-13797: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse.speech = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse",
  "name": "speech",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13798"></a>
## FND-13798: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse.board_markings = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse",
  "name": "board_markings",
  "number": 3,
  "type": ".chesscom.chess.v1.BoardMarkings",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13799"></a>
## FND-13799: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13800"></a>
## FND-13800: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_IN_CHECK = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_IN_CHECK",
  "number": 1,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13801"></a>
## FND-13801: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING",
  "number": 2,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13802"></a>
## FND-13802: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES",
  "number": 3,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13803"></a>
## FND-13803: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES",
  "number": 4,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13804"></a>
## FND-13804: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE",
  "number": 5,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13805"></a>
## FND-13805: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES",
  "number": 6,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13806"></a>
## FND-13806: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED",
  "number": 7,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13807"></a>
## FND-13807: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK",
  "number": 8,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13808"></a>
## FND-13808: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveCase",
  "name": "ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK",
  "number": 9,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13809"></a>
## FND-13809: chesscom.explanation_engine.v1.IllegalMoveExplanationMode.ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveExplanationMode",
  "name": "ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13810"></a>
## FND-13810: chesscom.explanation_engine.v1.IllegalMoveExplanationMode.ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveExplanationMode",
  "name": "ILLEGAL_MOVE_EXPLANATION_MODE_ALL",
  "number": 1,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13811"></a>
## FND-13811: chesscom.explanation_engine.v1.IllegalMoveExplanationMode.ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.IllegalMoveExplanationMode",
  "name": "ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES",
  "number": 2,
  "source_id": "SRC-0951",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0951** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_illegal_move_explanation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91ad4ea47b30f940acd3ae6fd5ef2dded03b47bcf15376735b82288308bae5e7.bin)

**Source references:** SRC-0951, SRC-1707  
**URL references:** None independently associated  
**Related findings:** FND-13793, FND-13794, FND-13795

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13812"></a>
## FND-13812: Native message: chesscom.explanation_engine.v1.GetMoveDetailsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_move_notation"
    }
  ]
}

### Evidence

- **SRC-0952** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/717f70927482986d42b0cfaed7e4782f06b98b50e6346ad75cb79cb2ee51290b.bin)

**Source references:** SRC-0952, SRC-1709  
**URL references:** None independently associated  
**Related findings:** FND-13813, FND-13814

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13813"></a>
## FND-13813: chesscom.explanation_engine.v1.GetMoveDetailsRequest.move_notation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetMoveDetailsRequest",
  "name": "move_notation",
  "number": 1,
  "type": ".chesscom.chess.v1.MoveNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move_notation",
  "proto3_optional": true,
  "source_id": "SRC-0952",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0952** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/717f70927482986d42b0cfaed7e4782f06b98b50e6346ad75cb79cb2ee51290b.bin)

**Source references:** SRC-0952, SRC-1709  
**URL references:** None independently associated  
**Related findings:** FND-13812, FND-13814

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13814"></a>
## FND-13814: Native message: chesscom.explanation_engine.v1.GetMoveDetailsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0952** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/717f70927482986d42b0cfaed7e4782f06b98b50e6346ad75cb79cb2ee51290b.bin)

**Source references:** SRC-0952, SRC-1709  
**URL references:** None independently associated  
**Related findings:** FND-13812, FND-13813

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13815"></a>
## FND-13815: chesscom.explanation_engine.v1.GetMoveDetailsResponse.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetMoveDetailsResponse",
  "name": "move",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0952",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0952** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/717f70927482986d42b0cfaed7e4782f06b98b50e6346ad75cb79cb2ee51290b.bin)

**Source references:** SRC-0952, SRC-1709  
**URL references:** None independently associated  
**Related findings:** FND-13812, FND-13813, FND-13814

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13816"></a>
## FND-13816: Native message: chesscom.explanation_engine.v1.GetNonChessTextRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetNonChessTextRequest",
  "field": [
    {
      "name": "type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.NonChessTextType"
    }
  ]
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13817"></a>
## FND-13817: chesscom.explanation_engine.v1.GetNonChessTextRequest.type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetNonChessTextRequest",
  "name": "type",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.NonChessTextType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13818"></a>
## FND-13818: Native message: chesscom.explanation_engine.v1.GetNonChessTextResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetNonChessTextResponse",
  "field": [
    {
      "name": "speech",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    }
  ]
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13819"></a>
## FND-13819: chesscom.explanation_engine.v1.GetNonChessTextResponse.speech = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetNonChessTextResponse",
  "name": "speech",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13820"></a>
## FND-13820: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NonChessTextType",
  "name": "NON_CHESS_TEXT_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13821"></a>
## FND-13821: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NonChessTextType",
  "name": "NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL",
  "number": 1,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13822"></a>
## FND-13822: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NonChessTextType",
  "name": "NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL",
  "number": 2,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13823"></a>
## FND-13823: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_RESUME_GAME = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NonChessTextType",
  "name": "NON_CHESS_TEXT_TYPE_RESUME_GAME",
  "number": 3,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13824"></a>
## FND-13824: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.NonChessTextType",
  "name": "NON_CHESS_TEXT_TYPE_SWITCHED_COACH",
  "number": 4,
  "source_id": "SRC-0953",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0953** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_non_chess_text.proto.bin` — [preserved redacted evidence](../evidence/descriptors/61a3197a678f50a61846c79b5cc0c4303eaac2a02d825ea7f5c45bdf28a664f6.bin)

**Source references:** SRC-0953, SRC-1888  
**URL references:** None independently associated  
**Related findings:** FND-13816, FND-13817, FND-13818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13825"></a>
## FND-13825: Native message: chesscom.explanation_engine.v1.GetOpeningRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_locale"
    }
  ]
}

### Evidence

- **SRC-0954** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf34c92de686dc3c0bd91e4eb0733e9ae320124b34870b0e683ea9aa6f84d49f.bin)

**Source references:** SRC-0954, SRC-1768  
**URL references:** None independently associated  
**Related findings:** FND-13826, FND-13827

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13826"></a>
## FND-13826: chesscom.explanation_engine.v1.GetOpeningRequest.locale = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetOpeningRequest",
  "name": "locale",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Locale",
  "label": "LABEL_OPTIONAL",
  "oneof": "_locale",
  "proto3_optional": true,
  "source_id": "SRC-0954",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0954** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf34c92de686dc3c0bd91e4eb0733e9ae320124b34870b0e683ea9aa6f84d49f.bin)

**Source references:** SRC-0954, SRC-1768  
**URL references:** None independently associated  
**Related findings:** FND-13825, FND-13827

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13827"></a>
## FND-13827: Native message: chesscom.explanation_engine.v1.GetOpeningResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  "oneof_decl": [
    {
      "name": "_opening"
    }
  ]
}

### Evidence

- **SRC-0954** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf34c92de686dc3c0bd91e4eb0733e9ae320124b34870b0e683ea9aa6f84d49f.bin)

**Source references:** SRC-0954, SRC-1768  
**URL references:** None independently associated  
**Related findings:** FND-13825, FND-13826

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13828"></a>
## FND-13828: chesscom.explanation_engine.v1.GetOpeningResponse.opening = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetOpeningResponse",
  "name": "opening",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Opening",
  "label": "LABEL_OPTIONAL",
  "oneof": "_opening",
  "proto3_optional": true,
  "source_id": "SRC-0954",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0954** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_opening.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf34c92de686dc3c0bd91e4eb0733e9ae320124b34870b0e683ea9aa6f84d49f.bin)

**Source references:** SRC-0954, SRC-1768  
**URL references:** None independently associated  
**Related findings:** FND-13825, FND-13826, FND-13827

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13829"></a>
## FND-13829: Native message: chesscom.explanation_engine.v1.GetPgnRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13830"></a>
## FND-13830: chesscom.explanation_engine.v1.GetPgnRequest.game = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "game",
  "number": 1,
  "type": ".chesscom.chess.v1.Game",
  "label": "LABEL_OPTIONAL",
  "oneof": "game_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13831"></a>
## FND-13831: chesscom.explanation_engine.v1.GetPgnRequest.game_state = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "game_state",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GameState",
  "label": "LABEL_OPTIONAL",
  "oneof": "game_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13832"></a>
## FND-13832: chesscom.explanation_engine.v1.GetPgnRequest.starting_game_point = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "starting_game_point",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "game_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13833"></a>
## FND-13833: chesscom.explanation_engine.v1.GetPgnRequest.pgn_fen_header_notation = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "pgn_fen_header_notation",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.FenNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": "_pgn_fen_header_notation",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13834"></a>
## FND-13834: chesscom.explanation_engine.v1.GetPgnRequest.main_line_only = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "main_line_only",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_main_line_only",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13835"></a>
## FND-13835: chesscom.explanation_engine.v1.GetPgnRequest.user_variations_only = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "user_variations_only",
  "number": 6,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_user_variations_only",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13836"></a>
## FND-13836: chesscom.explanation_engine.v1.GetPgnRequest.included_game_points = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "included_game_points",
  "number": 7,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13837"></a>
## FND-13837: chesscom.explanation_engine.v1.GetPgnRequest.include_threats = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "include_threats",
  "number": 8,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_include_threats",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13838"></a>
## FND-13838: chesscom.explanation_engine.v1.GetPgnRequest.include_all_scored_gamepoints = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "include_all_scored_gamepoints",
  "number": 9,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_include_all_scored_gamepoints",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13839"></a>
## FND-13839: chesscom.explanation_engine.v1.GetPgnRequest.unscored_gamepoint_limit = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "unscored_gamepoint_limit",
  "number": 10,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_unscored_gamepoint_limit",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13840"></a>
## FND-13840: chesscom.explanation_engine.v1.GetPgnRequest.explicit_included_game_points = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "explicit_included_game_points",
  "number": 11,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13841"></a>
## FND-13841: chesscom.explanation_engine.v1.GetPgnRequest.annotation_serialization_format = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnRequest",
  "name": "annotation_serialization_format",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat",
  "label": "LABEL_OPTIONAL",
  "oneof": "_annotation_serialization_format",
  "proto3_optional": true,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13842"></a>
## FND-13842: Native message: chesscom.explanation_engine.v1.GetPgnResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetPgnResponse",
  "field": [
    {
      "name": "pgn",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13843"></a>
## FND-13843: chesscom.explanation_engine.v1.GetPgnResponse.pgn = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnResponse",
  "name": "pgn",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13844"></a>
## FND-13844: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat.PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat",
  "name": "PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13845"></a>
## FND-13845: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat.PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat",
  "name": "PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE",
  "number": 1,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13846"></a>
## FND-13846: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat.PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat",
  "name": "PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM",
  "number": 2,
  "source_id": "SRC-0955",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0955** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/451f465ce80704f3e4110152fdd96fac0a2040837bf8fd80a10138b092f2ad28.bin)

**Source references:** SRC-0955, SRC-1881  
**URL references:** None independently associated  
**Related findings:** FND-13829, FND-13830, FND-13831

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13847"></a>
## FND-13847: Native message: chesscom.explanation_engine.v1.GetPgnMoveAnnotationsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetPgnMoveAnnotationsRequest"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13848"></a>
## FND-13848: Native message: chesscom.explanation_engine.v1.PgnMoveAnnotation

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PgnMoveAnnotation",
  "field": [
    {
      "name": "comments",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "before_comment",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "nags",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    }
  ],
  "oneof_decl": [
    {
      "name": "_before_comment"
    }
  ]
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13849"></a>
## FND-13849: chesscom.explanation_engine.v1.PgnMoveAnnotation.comments = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnMoveAnnotation",
  "name": "comments",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0956",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13850"></a>
## FND-13850: chesscom.explanation_engine.v1.PgnMoveAnnotation.before_comment = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnMoveAnnotation",
  "name": "before_comment",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_before_comment",
  "proto3_optional": true,
  "source_id": "SRC-0956",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13851"></a>
## FND-13851: chesscom.explanation_engine.v1.PgnMoveAnnotation.nags = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnMoveAnnotation",
  "name": "nags",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0956",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13852"></a>
## FND-13852: Native message: chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetPgnMoveAnnotationsResponse",
  "field": [
    {
      "name": "annotations",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry"
    }
  ],
  "nested_type": [
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
          "type_name": ".chesscom.explanation_engine.v1.PgnMoveAnnotation"
        }
      ],
      "options": {
        "map_entry": true
      }
    }
  ]
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13853"></a>
## FND-13853: chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.annotations = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse",
  "name": "annotations",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0956",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13854"></a>
## FND-13854: Native message: chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry

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
      "type_name": ".chesscom.explanation_engine.v1.PgnMoveAnnotation"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13855"></a>
## FND-13855: chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0956",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13856"></a>
## FND-13856: chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPgnMoveAnnotationsResponse.AnnotationsEntry",
  "name": "value",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PgnMoveAnnotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0956",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0956** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_pgn_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/66d4f78016e86b97b36836b01568d6fbdf4731d8737fa94f937c89c2184d1505.bin)

**Source references:** SRC-0956, SRC-1701  
**URL references:** None independently associated  
**Related findings:** FND-13847, FND-13848, FND-13849

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13857"></a>
## FND-13857: Native message: chesscom.explanation_engine.v1.GetPunishMoveRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetPunishMoveRequest"
}

### Evidence

- **SRC-0957** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/db2191ecf426683fe8d8e5107ae1ae743f0745f6a124d8d656f626a19a43a355.bin)

**Source references:** SRC-0957, SRC-1740  
**URL references:** None independently associated  
**Related findings:** FND-13858, FND-13859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13858"></a>
## FND-13858: Native message: chesscom.explanation_engine.v1.GetPunishMoveResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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
  ]
}

### Evidence

- **SRC-0957** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/db2191ecf426683fe8d8e5107ae1ae743f0745f6a124d8d656f626a19a43a355.bin)

**Source references:** SRC-0957, SRC-1740  
**URL references:** None independently associated  
**Related findings:** FND-13857, FND-13859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13859"></a>
## FND-13859: chesscom.explanation_engine.v1.GetPunishMoveResponse.punish_move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetPunishMoveResponse",
  "name": "punish_move",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PunishMove",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0957",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0957** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_punish_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/db2191ecf426683fe8d8e5107ae1ae743f0745f6a124d8d656f626a19a43a355.bin)

**Source references:** SRC-0957, SRC-1740  
**URL references:** None independently associated  
**Related findings:** FND-13857, FND-13858

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
