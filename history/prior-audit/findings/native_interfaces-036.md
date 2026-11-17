# native_interfaces — findings 3501–3600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-16160"></a>
## FND-16160: chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo.move_classification = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo",
  "name": "move_classification",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1075",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1075** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2ddcf998526a8561b20f8d8036e14a0079fafb48cdfc60557956abadae38c7e9.bin)

**Source references:** SRC-1075, SRC-1860  
**URL references:** None independently associated  
**Related findings:** FND-16154, FND-16155, FND-16156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16161"></a>
## FND-16161: chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo.move_precision = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo",
  "name": "move_precision",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1075",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1075** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2ddcf998526a8561b20f8d8036e14a0079fafb48cdfc60557956abadae38c7e9.bin)

**Source references:** SRC-1075, SRC-1860  
**URL references:** None independently associated  
**Related findings:** FND-16154, FND-16155, FND-16156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16162"></a>
## FND-16162: chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo.who_moved = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo",
  "name": "who_moved",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1075",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1075** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2ddcf998526a8561b20f8d8036e14a0079fafb48cdfc60557956abadae38c7e9.bin)

**Source references:** SRC-1075, SRC-1860  
**URL references:** None independently associated  
**Related findings:** FND-16154, FND-16155, FND-16156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16163"></a>
## FND-16163: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetCoherenceRequest",
  "field": [
    {
      "name": "coherence_type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.CoherenceType"
    },
    {
      "name": "cee_lines",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CeeLines",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "fen",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "elo",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "model_key",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "uci_move",
      "number": 6,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ],
  "oneof_decl": [
    {
      "name": "_cee_lines"
    },
    {
      "name": "_fen"
    },
    {
      "name": "_elo"
    },
    {
      "name": "_model_key"
    }
  ]
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16164"></a>
## FND-16164: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest.coherence_type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest",
  "name": "coherence_type",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.CoherenceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16165"></a>
## FND-16165: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest.cee_lines = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest",
  "name": "cee_lines",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.CeeLines",
  "label": "LABEL_OPTIONAL",
  "oneof": "_cee_lines",
  "proto3_optional": true,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16166"></a>
## FND-16166: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest.fen = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest",
  "name": "fen",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_fen",
  "proto3_optional": true,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16167"></a>
## FND-16167: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest.elo = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest",
  "name": "elo",
  "number": 4,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_elo",
  "proto3_optional": true,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16168"></a>
## FND-16168: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest.model_key = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest",
  "name": "model_key",
  "number": 5,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_model_key",
  "proto3_optional": true,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16169"></a>
## FND-16169: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest.uci_move = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceRequest",
  "name": "uci_move",
  "number": 6,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16170"></a>
## FND-16170: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetCoherenceResponse",
  "field": [
    {
      "name": "coherence",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_coherence"
    }
  ]
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16171"></a>
## FND-16171: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceResponse.coherence = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoherenceResponse",
  "name": "coherence",
  "number": 1,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": "_coherence",
  "proto3_optional": true,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16172"></a>
## FND-16172: chesscom.explanation_engine.v1alpha.CoherenceType.COHERENCE_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.CoherenceType",
  "name": "COHERENCE_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16173"></a>
## FND-16173: chesscom.explanation_engine.v1alpha.CoherenceType.COHERENCE_TYPE_CHARM = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.CoherenceType",
  "name": "COHERENCE_TYPE_CHARM",
  "number": 1,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16174"></a>
## FND-16174: chesscom.explanation_engine.v1alpha.CoherenceType.COHERENCE_TYPE_SQ_DISTANCE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.CoherenceType",
  "name": "COHERENCE_TYPE_SQ_DISTANCE",
  "number": 2,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16175"></a>
## FND-16175: chesscom.explanation_engine.v1alpha.CoherenceType.COHERENCE_TYPE_STATIC_EVAL = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.CoherenceType",
  "name": "COHERENCE_TYPE_STATIC_EVAL",
  "number": 3,
  "source_id": "SRC-1076",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1076** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coherence.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c32e662f710128757fa9f33486a2feefb8ed1d98e75906199137a820c6f55536.bin)

**Source references:** SRC-1076, SRC-1809  
**URL references:** None independently associated  
**Related findings:** FND-16163, FND-16164, FND-16165

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16176"></a>
## FND-16176: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetPieceRequest",
  "field": [
    {
      "name": "square",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square",
      "oneof_index": 0
    },
    {
      "name": "piece_id",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "piece"
    }
  ]
}

### Evidence

- **SRC-1077** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4c20c3d43d39bd34583b9531dc8980c155e1e87f6a3bee22fd54e9dfeb79cc79.bin)

**Source references:** SRC-1077, SRC-1868  
**URL references:** None independently associated  
**Related findings:** FND-16177, FND-16178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16177"></a>
## FND-16177: chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceRequest.square = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceRequest",
  "name": "square",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": "piece",
  "proto3_optional": false,
  "source_id": "SRC-1077",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1077** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4c20c3d43d39bd34583b9531dc8980c155e1e87f6a3bee22fd54e9dfeb79cc79.bin)

**Source references:** SRC-1077, SRC-1868  
**URL references:** None independently associated  
**Related findings:** FND-16176, FND-16178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16178"></a>
## FND-16178: chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceRequest.piece_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceRequest",
  "name": "piece_id",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "piece",
  "proto3_optional": false,
  "source_id": "SRC-1077",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1077** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4c20c3d43d39bd34583b9531dc8980c155e1e87f6a3bee22fd54e9dfeb79cc79.bin)

**Source references:** SRC-1077, SRC-1868  
**URL references:** None independently associated  
**Related findings:** FND-16176, FND-16177

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16179"></a>
## FND-16179: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetPieceResponse",
  "field": [
    {
      "name": "piece_details",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    }
  ]
}

### Evidence

- **SRC-1077** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4c20c3d43d39bd34583b9531dc8980c155e1e87f6a3bee22fd54e9dfeb79cc79.bin)

**Source references:** SRC-1077, SRC-1868  
**URL references:** None independently associated  
**Related findings:** FND-16176, FND-16177, FND-16178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16180"></a>
## FND-16180: chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceResponse.piece_details = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetPieceResponse",
  "name": "piece_details",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1077",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1077** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_piece.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4c20c3d43d39bd34583b9531dc8980c155e1e87f6a3bee22fd54e9dfeb79cc79.bin)

**Source references:** SRC-1077, SRC-1868  
**URL references:** None independently associated  
**Related findings:** FND-16176, FND-16177, FND-16178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16181"></a>
## FND-16181: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureKeyGameStateRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureKeyGameStateRequest",
  "field": [
    {
      "name": "game_state_spec",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameStateSpec"
    }
  ]
}

### Evidence

- **SRC-1078** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_key_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ad81b8d923fe4573caa1e5eb0adffc6c2796f27a5322088a9f3d1e06d224b9cf.bin)

**Source references:** SRC-1078, SRC-1781  
**URL references:** None independently associated  
**Related findings:** FND-16182, FND-16183

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16182"></a>
## FND-16182: chesscom.explanation_engine.v1alpha.InternalFeatureKeyGameStateRequest.game_state_spec = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureKeyGameStateRequest",
  "name": "game_state_spec",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameStateSpec",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1078",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1078** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_key_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ad81b8d923fe4573caa1e5eb0adffc6c2796f27a5322088a9f3d1e06d224b9cf.bin)

**Source references:** SRC-1078, SRC-1781  
**URL references:** None independently associated  
**Related findings:** FND-16181, FND-16183

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16183"></a>
## FND-16183: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureKeyGameStateResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureKeyGameStateResponse",
  "field": [
    {
      "name": "game_state_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1078** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_key_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ad81b8d923fe4573caa1e5eb0adffc6c2796f27a5322088a9f3d1e06d224b9cf.bin)

**Source references:** SRC-1078, SRC-1781  
**URL references:** None independently associated  
**Related findings:** FND-16181, FND-16182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16184"></a>
## FND-16184: chesscom.explanation_engine.v1alpha.InternalFeatureKeyGameStateResponse.game_state_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureKeyGameStateResponse",
  "name": "game_state_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1078",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1078** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_key_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ad81b8d923fe4573caa1e5eb0adffc6c2796f27a5322088a9f3d1e06d224b9cf.bin)

**Source references:** SRC-1078, SRC-1781  
**URL references:** None independently associated  
**Related findings:** FND-16181, FND-16182, FND-16183

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16185"></a>
## FND-16185: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureLoadCharmModelRequest",
  "field": [
    {
      "name": "model_path",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "model_key",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "artifact_id",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_model_path"
    },
    {
      "name": "_model_key"
    },
    {
      "name": "_artifact_id"
    }
  ]
}

### Evidence

- **SRC-1080** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ce01f06d587db0f5b5041d08e934f036037e146fabd07d10589bbea5eaa02d4b.bin)

**Source references:** SRC-1080, SRC-1738  
**URL references:** None independently associated  
**Related findings:** FND-16186, FND-16187

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16186"></a>
## FND-16186: chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest.model_path = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest",
  "name": "model_path",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_model_path",
  "proto3_optional": true,
  "source_id": "SRC-1080",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1080** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ce01f06d587db0f5b5041d08e934f036037e146fabd07d10589bbea5eaa02d4b.bin)

**Source references:** SRC-1080, SRC-1738  
**URL references:** None independently associated  
**Related findings:** FND-16185, FND-16187

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16187"></a>
## FND-16187: chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest.model_key = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest",
  "name": "model_key",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_model_key",
  "proto3_optional": true,
  "source_id": "SRC-1080",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1080** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ce01f06d587db0f5b5041d08e934f036037e146fabd07d10589bbea5eaa02d4b.bin)

**Source references:** SRC-1080, SRC-1738  
**URL references:** None independently associated  
**Related findings:** FND-16185, FND-16186

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16188"></a>
## FND-16188: chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest.artifact_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelRequest",
  "name": "artifact_id",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_artifact_id",
  "proto3_optional": true,
  "source_id": "SRC-1080",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1080** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ce01f06d587db0f5b5041d08e934f036037e146fabd07d10589bbea5eaa02d4b.bin)

**Source references:** SRC-1080, SRC-1738  
**URL references:** None independently associated  
**Related findings:** FND-16185, FND-16186, FND-16187

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16189"></a>
## FND-16189: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureLoadCharmModelResponse",
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

- **SRC-1080** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ce01f06d587db0f5b5041d08e934f036037e146fabd07d10589bbea5eaa02d4b.bin)

**Source references:** SRC-1080, SRC-1738  
**URL references:** None independently associated  
**Related findings:** FND-16185, FND-16186, FND-16187

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16190"></a>
## FND-16190: chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelResponse.model_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureLoadCharmModelResponse",
  "name": "model_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1080",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1080** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_load_charm_model.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ce01f06d587db0f5b5041d08e934f036037e146fabd07d10589bbea5eaa02d4b.bin)

**Source references:** SRC-1080, SRC-1738  
**URL references:** None independently associated  
**Related findings:** FND-16185, FND-16186, FND-16187

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16191"></a>
## FND-16191: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureMaiaBotMoveRequest",
  "field": [
    {
      "name": "elo_self",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "elo_oppo",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "json",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16192, FND-16193

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16192"></a>
## FND-16192: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest.elo_self = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest",
  "name": "elo_self",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1081",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16191, FND-16193

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16193"></a>
## FND-16193: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest.elo_oppo = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest",
  "name": "elo_oppo",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1081",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16191, FND-16192

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16194"></a>
## FND-16194: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest.json = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveRequest",
  "name": "json",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1081",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16191, FND-16192, FND-16193

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16195"></a>
## FND-16195: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureMaiaBotMoveResponse",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "json",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16191, FND-16192, FND-16193

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16196"></a>
## FND-16196: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveResponse.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveResponse",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1081",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16191, FND-16192, FND-16193

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16197"></a>
## FND-16197: chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveResponse.json = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureMaiaBotMoveResponse",
  "name": "json",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1081",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1081** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b0ee12e4b6a5d61e679736bd83b76a6a367b0b6862a60f9d83fd58cee3d35a4a.bin)

**Source references:** SRC-1081, SRC-1767  
**URL references:** None independently associated  
**Related findings:** FND-16191, FND-16192, FND-16193

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16198"></a>
## FND-16198: Native message: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeaturePositionPropertiesRequest"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16199"></a>
## FND-16199: Native message: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeaturePositionPropertiesResponse",
  "field": [
    {
      "name": "is_open",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "is_semi_open",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "is_closed",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "white_is_active",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "white_is_passive",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "black_is_active",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "black_is_passive",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16200"></a>
## FND-16200: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.is_open = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "is_open",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16201"></a>
## FND-16201: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.is_semi_open = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "is_semi_open",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16202"></a>
## FND-16202: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.is_closed = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "is_closed",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16203"></a>
## FND-16203: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.white_is_active = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "white_is_active",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16204"></a>
## FND-16204: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.white_is_passive = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "white_is_passive",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16205"></a>
## FND-16205: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.black_is_active = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "black_is_active",
  "number": 6,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16206"></a>
## FND-16206: chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse.black_is_passive = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeaturePositionPropertiesResponse",
  "name": "black_is_passive",
  "number": 7,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1082",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1082** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_position_properties.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fb4c3d1393d4d1ae4fb164b135490293c6d7bcbad28b34e7796d18f5a7a104b3.bin)

**Source references:** SRC-1082, SRC-1795  
**URL references:** None independently associated  
**Related findings:** FND-16198, FND-16199, FND-16200

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16207"></a>
## FND-16207: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureRunPvTreesRequest",
  "field": [
    {
      "name": "request",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RunSearchRequest"
    },
    {
      "name": "pvtree_options",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PVTreeOptions",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_pvtree_options"
    }
  ]
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16208, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16208"></a>
## FND-16208: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesRequest.request = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesRequest",
  "name": "request",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.RunSearchRequest",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1083",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16209"></a>
## FND-16209: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesRequest.pvtree_options = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesRequest",
  "name": "pvtree_options",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": "_pvtree_options",
  "proto3_optional": true,
  "source_id": "SRC-1083",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16208

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16210"></a>
## FND-16210: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureRunPvTreesResponse",
  "field": [
    {
      "name": "search_response",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RunSearchResponse"
    },
    {
      "name": "game_tree",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
    },
    {
      "name": "best_line",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
    },
    {
      "name": "human_line",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
    }
  ]
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16208, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16211"></a>
## FND-16211: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse.search_response = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse",
  "name": "search_response",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.RunSearchResponse",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1083",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16208, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16212"></a>
## FND-16212: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse.game_tree = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse",
  "name": "game_tree",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1083",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16208, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16213"></a>
## FND-16213: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse.best_line = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse",
  "name": "best_line",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1083",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16208, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16214"></a>
## FND-16214: chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse.human_line = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunPvTreesResponse",
  "name": "human_line",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1083",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1083** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_pvtrees.proto.bin` — [preserved redacted evidence](../evidence/descriptors/65f8f4dfeb40ca5e1b66880bbf6e154c4c5978864cf455f7c0f69d0c1a6bd127.bin)

**Source references:** SRC-1083, SRC-1784  
**URL references:** None independently associated  
**Related findings:** FND-16207, FND-16208, FND-16209

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16215"></a>
## FND-16215: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureRunSearchRequest",
  "field": [
    {
      "name": "request",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RunSearchRequest"
    },
    {
      "name": "pvtree_options",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PVTreeOptions",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_pvtree_options"
    }
  ]
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16216"></a>
## FND-16216: chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchRequest.request = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchRequest",
  "name": "request",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.RunSearchRequest",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16217"></a>
## FND-16217: chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchRequest.pvtree_options = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchRequest",
  "name": "pvtree_options",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": "_pvtree_options",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16218"></a>
## FND-16218: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureRunSearchResponse",
  "field": [
    {
      "name": "response",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RunSearchResponse"
    }
  ]
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16219"></a>
## FND-16219: chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchResponse.response = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureRunSearchResponse",
  "name": "response",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.RunSearchResponse",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16220"></a>
## FND-16220: Native message: chesscom.explanation_engine.v1alpha.PVTreeOptions

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PVTreeOptions",
  "field": [
    {
      "name": "use_split_depth_limit",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "split_depth_limit",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "use_split_width_limit",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "split_width_limit",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "keep_equal_subtrees",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "allowed_excess_depth",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "allowed_excess_width",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 6,
      "proto3_optional": true
    },
    {
      "name": "rating",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 7,
      "proto3_optional": true
    },
    {
      "name": "ep_loss_margin",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT",
      "oneof_index": 8,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_use_split_depth_limit"
    },
    {
      "name": "_split_depth_limit"
    },
    {
      "name": "_use_split_width_limit"
    },
    {
      "name": "_split_width_limit"
    },
    {
      "name": "_keep_equal_subtrees"
    },
    {
      "name": "_allowed_excess_depth"
    },
    {
      "name": "_allowed_excess_width"
    },
    {
      "name": "_rating"
    },
    {
      "name": "_ep_loss_margin"
    }
  ]
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16221"></a>
## FND-16221: chesscom.explanation_engine.v1alpha.PVTreeOptions.use_split_depth_limit = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "use_split_depth_limit",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_use_split_depth_limit",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16222"></a>
## FND-16222: chesscom.explanation_engine.v1alpha.PVTreeOptions.split_depth_limit = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "split_depth_limit",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_split_depth_limit",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16223"></a>
## FND-16223: chesscom.explanation_engine.v1alpha.PVTreeOptions.use_split_width_limit = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "use_split_width_limit",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_use_split_width_limit",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16224"></a>
## FND-16224: chesscom.explanation_engine.v1alpha.PVTreeOptions.split_width_limit = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "split_width_limit",
  "number": 4,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_split_width_limit",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16225"></a>
## FND-16225: chesscom.explanation_engine.v1alpha.PVTreeOptions.keep_equal_subtrees = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "keep_equal_subtrees",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_keep_equal_subtrees",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16226"></a>
## FND-16226: chesscom.explanation_engine.v1alpha.PVTreeOptions.allowed_excess_depth = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "allowed_excess_depth",
  "number": 6,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_allowed_excess_depth",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16227"></a>
## FND-16227: chesscom.explanation_engine.v1alpha.PVTreeOptions.allowed_excess_width = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "allowed_excess_width",
  "number": 7,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_allowed_excess_width",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16228"></a>
## FND-16228: chesscom.explanation_engine.v1alpha.PVTreeOptions.rating = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "rating",
  "number": 8,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_rating",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16229"></a>
## FND-16229: chesscom.explanation_engine.v1alpha.PVTreeOptions.ep_loss_margin = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.PVTreeOptions",
  "name": "ep_loss_margin",
  "number": 9,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": "_ep_loss_margin",
  "proto3_optional": true,
  "source_id": "SRC-1085",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1085** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ebcddb43e5481cd5f36dcec8fdd41569d0362eb7c4006ba8ca90acfb4b1a8561.bin)

**Source references:** SRC-1085, SRC-1660  
**URL references:** None independently associated  
**Related findings:** FND-16215, FND-16216, FND-16217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16230"></a>
## FND-16230: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureStaticExchangeRequest",
  "field": [
    {
      "name": "color",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color",
      "oneof_index": 0
    },
    {
      "name": "square",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square",
      "oneof_index": 0
    },
    {
      "name": "piece_id",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "aggregate"
    }
  ]
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16231, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16231"></a>
## FND-16231: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest.color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest",
  "name": "color",
  "number": 1,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": "aggregate",
  "proto3_optional": false,
  "source_id": "SRC-1086",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16232"></a>
## FND-16232: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest.square = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest",
  "name": "square",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": "aggregate",
  "proto3_optional": false,
  "source_id": "SRC-1086",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16231

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16233"></a>
## FND-16233: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest.piece_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeRequest",
  "name": "piece_id",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "aggregate",
  "proto3_optional": false,
  "source_id": "SRC-1086",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16231, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16234"></a>
## FND-16234: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureStaticExchangeResponse",
  "field": [
    {
      "name": "square_control",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.SquareSet"
    },
    {
      "name": "threatening",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.StaticExchangeSquareDetails"
    },
    {
      "name": "threatened_by",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.StaticExchangeSquareDetails"
    }
  ]
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16231, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16235"></a>
## FND-16235: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse.square_control = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse",
  "name": "square_control",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.SquareSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1086",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16231, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16236"></a>
## FND-16236: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse.threatening = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse",
  "name": "threatening",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.StaticExchangeSquareDetails",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1086",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16231, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16237"></a>
## FND-16237: chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse.threatened_by = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureStaticExchangeResponse",
  "name": "threatened_by",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.StaticExchangeSquareDetails",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1086",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1086** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_static_exchange.proto.bin` — [preserved redacted evidence](../evidence/descriptors/049888328bfe0924b58f2a6f71a1a82921bc2c8712bbe1621f8f43a308ed06e7.bin)

**Source references:** SRC-1086, SRC-1890  
**URL references:** None independently associated  
**Related findings:** FND-16230, FND-16231, FND-16232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16238"></a>
## FND-16238: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUncompressDataRequest",
  "field": [
    {
      "name": "compressed_data",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    },
    {
      "name": "decrypt",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1087** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_uncompress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5ca61c2b4e4379e76b2be8f0b71dd819f0927c1606779ff7f912f76942159e08.bin)

**Source references:** SRC-1087, SRC-1882  
**URL references:** None independently associated  
**Related findings:** FND-16239, FND-16240

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16239"></a>
## FND-16239: chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataRequest.compressed_data = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataRequest",
  "name": "compressed_data",
  "number": 1,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1087",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1087** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_uncompress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5ca61c2b4e4379e76b2be8f0b71dd819f0927c1606779ff7f912f76942159e08.bin)

**Source references:** SRC-1087, SRC-1882  
**URL references:** None independently associated  
**Related findings:** FND-16238, FND-16240

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16240"></a>
## FND-16240: chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataRequest.decrypt = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataRequest",
  "name": "decrypt",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1087",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1087** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_uncompress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5ca61c2b4e4379e76b2be8f0b71dd819f0927c1606779ff7f912f76942159e08.bin)

**Source references:** SRC-1087, SRC-1882  
**URL references:** None independently associated  
**Related findings:** FND-16238, FND-16239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16241"></a>
## FND-16241: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUncompressDataResponse",
  "field": [
    {
      "name": "uncompressed_data",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    }
  ]
}

### Evidence

- **SRC-1087** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_uncompress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5ca61c2b4e4379e76b2be8f0b71dd819f0927c1606779ff7f912f76942159e08.bin)

**Source references:** SRC-1087, SRC-1882  
**URL references:** None independently associated  
**Related findings:** FND-16238, FND-16239, FND-16240

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16242"></a>
## FND-16242: chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataResponse.uncompressed_data = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureUncompressDataResponse",
  "name": "uncompressed_data",
  "number": 1,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1087",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1087** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_uncompress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5ca61c2b4e4379e76b2be8f0b71dd819f0927c1606779ff7f912f76942159e08.bin)

**Source references:** SRC-1087, SRC-1882  
**URL references:** None independently associated  
**Related findings:** FND-16238, FND-16239, FND-16240

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16243"></a>
## FND-16243: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureUnitTestCodeRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUnitTestCodeRequest",
  "field": [
    {
      "name": "num_pushed_moves",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1088** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_unit_test_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d5908966ef0cbbdef6bbe32f638f444c69ae84b4eb36df7b871191aeea978841.bin)

**Source references:** SRC-1088, SRC-1739  
**URL references:** None independently associated  
**Related findings:** FND-16244, FND-16245

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16244"></a>
## FND-16244: chesscom.explanation_engine.v1alpha.InternalFeatureUnitTestCodeRequest.num_pushed_moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureUnitTestCodeRequest",
  "name": "num_pushed_moves",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1088",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1088** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_unit_test_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d5908966ef0cbbdef6bbe32f638f444c69ae84b4eb36df7b871191aeea978841.bin)

**Source references:** SRC-1088, SRC-1739  
**URL references:** None independently associated  
**Related findings:** FND-16243, FND-16245

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16245"></a>
## FND-16245: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureUnitTestCodeResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUnitTestCodeResponse",
  "field": [
    {
      "name": "unit_test_code",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1088** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_unit_test_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d5908966ef0cbbdef6bbe32f638f444c69ae84b4eb36df7b871191aeea978841.bin)

**Source references:** SRC-1088, SRC-1739  
**URL references:** None independently associated  
**Related findings:** FND-16243, FND-16244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16246"></a>
## FND-16246: chesscom.explanation_engine.v1alpha.InternalFeatureUnitTestCodeResponse.unit_test_code = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureUnitTestCodeResponse",
  "name": "unit_test_code",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1088",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1088** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_unit_test_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d5908966ef0cbbdef6bbe32f638f444c69ae84b4eb36df7b871191aeea978841.bin)

**Source references:** SRC-1088, SRC-1739  
**URL references:** None independently associated  
**Related findings:** FND-16243, FND-16244, FND-16245

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16247"></a>
## FND-16247: Native message: chesscom.explanation_engine.v1alpha.LocationFan

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LocationFan",
  "field": [
    {
      "name": "source",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    },
    {
      "name": "targets",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-1089** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_location_fan.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a2efba3f593d1d4903fe3c100697cbdae56aa7de97635e24aed2bbccbf2376b8.bin)

**Source references:** SRC-1089, SRC-1761  
**URL references:** None independently associated  
**Related findings:** FND-16248, FND-16249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16248"></a>
## FND-16248: chesscom.explanation_engine.v1alpha.LocationFan.source = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.LocationFan",
  "name": "source",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1089",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1089** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_location_fan.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a2efba3f593d1d4903fe3c100697cbdae56aa7de97635e24aed2bbccbf2376b8.bin)

**Source references:** SRC-1089, SRC-1761  
**URL references:** None independently associated  
**Related findings:** FND-16247, FND-16249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16249"></a>
## FND-16249: chesscom.explanation_engine.v1alpha.LocationFan.targets = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.LocationFan",
  "name": "targets",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1089",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1089** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_location_fan.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a2efba3f593d1d4903fe3c100697cbdae56aa7de97635e24aed2bbccbf2376b8.bin)

**Source references:** SRC-1089, SRC-1761  
**URL references:** None independently associated  
**Related findings:** FND-16247, FND-16248

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16250"></a>
## FND-16250: Native message: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "V1x6Depth20Multipv2LabelsRecord",
  "field": [
    {
      "name": "ep_diff_side_to_move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "classification_name",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "uci",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "fen_before",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "fen",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "fen_after",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16251"></a>
## FND-16251: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord.ep_diff_side_to_move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord",
  "name": "ep_diff_side_to_move",
  "number": 1,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16252"></a>
## FND-16252: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord.classification_name = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord",
  "name": "classification_name",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16253"></a>
## FND-16253: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord.uci = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord",
  "name": "uci",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16254"></a>
## FND-16254: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord.fen_before = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord",
  "name": "fen_before",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16255"></a>
## FND-16255: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord.fen = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord",
  "name": "fen",
  "number": 5,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16256"></a>
## FND-16256: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord.fen_after = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2LabelsRecord",
  "name": "fen_after",
  "number": 6,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16257"></a>
## FND-16257: Native message: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2FeaturesRecord

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "V1x6Depth20Multipv2FeaturesRecord",
  "field": [
    {
      "name": "move_number",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "game_phase",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "ep_diff_side_that_moved",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "pv0_pv1_ep_diff_side_that_moved",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "ep_side_to_move",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "pv0_pv1_ep_diff_side_to_move",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "potential_legal_move_count_side_to_move",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "potential_legal_move_count_side_that_moved",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "previous_legal_move_count_side_that_moved",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "potential_legal_capture_count_side_to_move",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "potential_legal_capture_count_side_that_moved",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "previous_legal_capture_count_side_that_moved",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "potential_see_positive_capture_count_side_to_move",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "potential_see_positive_capture_count_side_that_moved",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "previous_see_positive_capture_count_side_that_moved",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "in_check_side_to_move",
      "number": 16,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "was_in_check_side_that_moved",
      "number": 17,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_distance",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_distance",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_piece_type",
      "number": 20,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_piece_type",
      "number": 21,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_capture_piece_type",
      "number": 22,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_capture_piece_type",
      "number": 23,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_bestline_capture_count",
      "number": 24,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_bestline_capture_count",
      "number": 25,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_good_tag_count",
      "number": 26,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_good_tag_count",
      "number": 27,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_bad_tag_count",
      "number": 28,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_bad_tag_count",
      "number": 29,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_obvious_or_easy",
      "number": 30,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_obvious_or_easy",
      "number": 31,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_backwards",
      "number": 32,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_backwards",
      "number": 33,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_check",
      "number": 34,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_check",
      "number": 35,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_tactic",
      "number": 36,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_tactic",
      "number": 37,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_sacrifice",
      "number": 38,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_sacrifice",
      "number": 39,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_deflection",
      "number": 40,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_deflection",
      "number": 41,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv0_is_underpromotion",
      "number": 42,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pv1_is_underpromotion",
      "number": 43,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "material_count",
      "number": 44,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "material_difference",
      "number": 45,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pawn_piece_count_side_to_move",
      "number": 46,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "knight_piece_count_side_to_move",
      "number": 47,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "bishop_piece_count_side_to_move",
      "number": 48,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "rook_piece_count_side_to_move",
      "number": 49,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "queen_piece_count_side_to_move",
      "number": 50,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "pawn_piece_count_side_that_moved",
      "number": 51,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "knight_piece_count_side_that_moved",
      "number": 52,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "bishop_piece_count_side_that_moved",
      "number": 53,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "rook_piece_count_side_that_moved",
      "number": 54,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "queen_piece_count_side_that_moved",
      "number": 55,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "chip_ep_side_to_move",
      "number": 56,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "chip_vs_engine_diff_ep_side_to_move",
      "number": 57,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "chip_think_time_s",
      "number": 58,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "chip_p_best",
      "number": 59,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "chip_p_alt",
      "number": 60,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16258"></a>
## FND-16258: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2FeaturesRecord.move_number = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2FeaturesRecord",
  "name": "move_number",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16259"></a>
## FND-16259: chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2FeaturesRecord.game_phase = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.V1x6Depth20Multipv2FeaturesRecord",
  "name": "game_phase",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1090",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1090** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_pd_v1_6_depth20_multipv2.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bd6de0efb0b83fe23254d08f4141c66863f3af3372c76ae6a982bb41e49b4349.bin)

**Source references:** SRC-1090, SRC-1715  
**URL references:** None independently associated  
**Related findings:** FND-16250, FND-16251, FND-16252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
