# native_interfaces — findings 3401–3500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-16060"></a>
## FND-16060: chesscom.explanation_engine.v1alpha.InternalFeatureCharmInferenceResponse.results = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureCharmInferenceResponse",
  "name": "results",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CharmInferenceResult",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1068",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1068** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ee150c1da104b84d0ae1b302e1c955ea3a628888a018058d7e5521da9155081e.bin)

**Source references:** SRC-1068, SRC-1861  
**URL references:** None independently associated  
**Related findings:** FND-16049, FND-16050, FND-16051

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16061"></a>
## FND-16061: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureCheckAnatomyRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureCheckAnatomyRequest"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16062"></a>
## FND-16062: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureCheckAnatomyResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureCheckAnatomyResponse",
  "field": [
    {
      "name": "check",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.InCheckPosition",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_check"
    }
  ]
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16063"></a>
## FND-16063: chesscom.explanation_engine.v1alpha.InternalFeatureCheckAnatomyResponse.check = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureCheckAnatomyResponse",
  "name": "check",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.InCheckPosition",
  "label": "LABEL_OPTIONAL",
  "oneof": "_check",
  "proto3_optional": true,
  "source_id": "SRC-1069",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16064"></a>
## FND-16064: Native message: chesscom.explanation_engine.v1alpha.InCheckPosition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InCheckPosition",
  "field": [
    {
      "name": "checked_king_square",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "checkers",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    },
    {
      "name": "guarders",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.LocationFan"
    },
    {
      "name": "blockers",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    },
    {
      "name": "checker_defenders",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.LocationFan"
    }
  ]
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16065"></a>
## FND-16065: chesscom.explanation_engine.v1alpha.InCheckPosition.checked_king_square = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InCheckPosition",
  "name": "checked_king_square",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1069",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16066"></a>
## FND-16066: chesscom.explanation_engine.v1alpha.InCheckPosition.checkers = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InCheckPosition",
  "name": "checkers",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1069",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16067"></a>
## FND-16067: chesscom.explanation_engine.v1alpha.InCheckPosition.guarders = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InCheckPosition",
  "name": "guarders",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.LocationFan",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1069",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16068"></a>
## FND-16068: chesscom.explanation_engine.v1alpha.InCheckPosition.blockers = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InCheckPosition",
  "name": "blockers",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1069",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16069"></a>
## FND-16069: chesscom.explanation_engine.v1alpha.InCheckPosition.checker_defenders = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InCheckPosition",
  "name": "checker_defenders",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1alpha.LocationFan",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1069",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1069** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_check_anatomy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0dde579b778d9666e415df732f173058c3e523937a8b36fe38cb048a9dab035c.bin)

**Source references:** SRC-1069, SRC-1681  
**URL references:** None independently associated  
**Related findings:** FND-16061, FND-16062, FND-16063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16070"></a>
## FND-16070: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureCheckmateTypeRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureCheckmateTypeRequest"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16071"></a>
## FND-16071: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureCheckmateTypeResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureCheckmateTypeResponse",
  "field": [
    {
      "name": "checkmate",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePosition",
      "oneof_index": 0
    },
    {
      "name": "not_checkmate",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.NotCheckmatePosition",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "position"
    }
  ]
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16072"></a>
## FND-16072: chesscom.explanation_engine.v1alpha.InternalFeatureCheckmateTypeResponse.checkmate = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureCheckmateTypeResponse",
  "name": "checkmate",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "label": "LABEL_OPTIONAL",
  "oneof": "position",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16073"></a>
## FND-16073: chesscom.explanation_engine.v1alpha.InternalFeatureCheckmateTypeResponse.not_checkmate = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureCheckmateTypeResponse",
  "name": "not_checkmate",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.NotCheckmatePosition",
  "label": "LABEL_OPTIONAL",
  "oneof": "position",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16074"></a>
## FND-16074: Native message: chesscom.explanation_engine.v1alpha.CheckmatePosition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePosition",
  "field": [
    {
      "name": "pattern",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePattern"
    },
    {
      "name": "mated_king_square",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "checkers",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    },
    {
      "name": "guarders",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.LocationFan"
    },
    {
      "name": "blockers",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    },
    {
      "name": "checker_defenders",
      "number": 6,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.LocationFan"
    }
  ]
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16075"></a>
## FND-16075: chesscom.explanation_engine.v1alpha.CheckmatePosition.pattern = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "name": "pattern",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16076"></a>
## FND-16076: chesscom.explanation_engine.v1alpha.CheckmatePosition.mated_king_square = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "name": "mated_king_square",
  "number": 5,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16077"></a>
## FND-16077: chesscom.explanation_engine.v1alpha.CheckmatePosition.checkers = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "name": "checkers",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16078"></a>
## FND-16078: chesscom.explanation_engine.v1alpha.CheckmatePosition.guarders = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "name": "guarders",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.LocationFan",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16079"></a>
## FND-16079: chesscom.explanation_engine.v1alpha.CheckmatePosition.blockers = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "name": "blockers",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16080"></a>
## FND-16080: chesscom.explanation_engine.v1alpha.CheckmatePosition.checker_defenders = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePosition",
  "name": "checker_defenders",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1alpha.LocationFan",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16081"></a>
## FND-16081: Native message: chesscom.explanation_engine.v1alpha.NotCheckmatePosition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NotCheckmatePosition"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16082"></a>
## FND-16082: Native message: chesscom.explanation_engine.v1alpha.CheckmatePattern

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePattern",
  "field": [
    {
      "name": "arabian",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternArabian",
      "oneof_index": 0
    },
    {
      "name": "anastasia",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternAnastasia",
      "oneof_index": 0
    },
    {
      "name": "two_bishops",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternTwoBishops",
      "oneof_index": 0
    },
    {
      "name": "backrank",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternBackrank",
      "oneof_index": 0
    },
    {
      "name": "smothered",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternSmothered",
      "oneof_index": 0
    },
    {
      "name": "scholar",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternScholar",
      "oneof_index": 0
    },
    {
      "name": "fools",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternFools",
      "oneof_index": 0
    },
    {
      "name": "bodens",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternBodens",
      "oneof_index": 0
    },
    {
      "name": "two_rooks",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternTwoRooks",
      "oneof_index": 0
    },
    {
      "name": "king_queen",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternKingQueen",
      "oneof_index": 0
    },
    {
      "name": "king_rook",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternKingRook",
      "oneof_index": 0
    },
    {
      "name": "unrecognized",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CheckmatePatternUnrecognized",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "pattern"
    }
  ]
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16083"></a>
## FND-16083: chesscom.explanation_engine.v1alpha.CheckmatePattern.arabian = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "arabian",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternArabian",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16084"></a>
## FND-16084: chesscom.explanation_engine.v1alpha.CheckmatePattern.anastasia = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "anastasia",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternAnastasia",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16085"></a>
## FND-16085: chesscom.explanation_engine.v1alpha.CheckmatePattern.two_bishops = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "two_bishops",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternTwoBishops",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16086"></a>
## FND-16086: chesscom.explanation_engine.v1alpha.CheckmatePattern.backrank = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "backrank",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternBackrank",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16087"></a>
## FND-16087: chesscom.explanation_engine.v1alpha.CheckmatePattern.smothered = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "smothered",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternSmothered",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16088"></a>
## FND-16088: chesscom.explanation_engine.v1alpha.CheckmatePattern.scholar = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "scholar",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternScholar",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16089"></a>
## FND-16089: chesscom.explanation_engine.v1alpha.CheckmatePattern.fools = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "fools",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternFools",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16090"></a>
## FND-16090: chesscom.explanation_engine.v1alpha.CheckmatePattern.bodens = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "bodens",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternBodens",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16091"></a>
## FND-16091: chesscom.explanation_engine.v1alpha.CheckmatePattern.two_rooks = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "two_rooks",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternTwoRooks",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16092"></a>
## FND-16092: chesscom.explanation_engine.v1alpha.CheckmatePattern.king_queen = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "king_queen",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternKingQueen",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16093"></a>
## FND-16093: chesscom.explanation_engine.v1alpha.CheckmatePattern.king_rook = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "king_rook",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternKingRook",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16094"></a>
## FND-16094: chesscom.explanation_engine.v1alpha.CheckmatePattern.unrecognized = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CheckmatePattern",
  "name": "unrecognized",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1alpha.CheckmatePatternUnrecognized",
  "label": "LABEL_OPTIONAL",
  "oneof": "pattern",
  "proto3_optional": false,
  "source_id": "SRC-1070",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16095"></a>
## FND-16095: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternArabian

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternArabian"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16096"></a>
## FND-16096: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternAnastasia

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternAnastasia"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16097"></a>
## FND-16097: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternTwoBishops

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternTwoBishops"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16098"></a>
## FND-16098: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternBackrank

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternBackrank"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16099"></a>
## FND-16099: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternSmothered

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternSmothered"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16100"></a>
## FND-16100: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternScholar

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternScholar"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16101"></a>
## FND-16101: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternFools

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternFools"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16102"></a>
## FND-16102: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternBodens

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternBodens"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16103"></a>
## FND-16103: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternTwoRooks

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternTwoRooks"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16104"></a>
## FND-16104: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternKingQueen

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternKingQueen"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16105"></a>
## FND-16105: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternKingRook

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternKingRook"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16106"></a>
## FND-16106: Native message: chesscom.explanation_engine.v1alpha.CheckmatePatternUnrecognized

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CheckmatePatternUnrecognized"
}

### Evidence

- **SRC-1070** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_checkmate_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fad94c4cdb7398f5aa35808ff98fbdeb173519b5a1da434ea7146a4822e3587c.bin)

**Source references:** SRC-1070, SRC-1774  
**URL references:** None independently associated  
**Related findings:** FND-16070, FND-16071, FND-16072

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16107"></a>
## FND-16107: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureExtractPVLineRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureExtractPVLineRequest",
  "field": [
    {
      "name": "type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1071** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_extract_pvline.proto.bin` — [preserved redacted evidence](../evidence/descriptors/454e855f2c96f3f4ede1d57a75b5d8ae3d3ec9345c88fa34e5b3a913f33ca660.bin)

**Source references:** SRC-1071, SRC-1672  
**URL references:** None independently associated  
**Related findings:** FND-16108, FND-16109

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16108"></a>
## FND-16108: chesscom.explanation_engine.v1alpha.InternalFeatureExtractPVLineRequest.type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureExtractPVLineRequest",
  "name": "type",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1071",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1071** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_extract_pvline.proto.bin` — [preserved redacted evidence](../evidence/descriptors/454e855f2c96f3f4ede1d57a75b5d8ae3d3ec9345c88fa34e5b3a913f33ca660.bin)

**Source references:** SRC-1071, SRC-1672  
**URL references:** None independently associated  
**Related findings:** FND-16107, FND-16109

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16109"></a>
## FND-16109: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureExtractPVLineResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureExtractPVLineResponse",
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

- **SRC-1071** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_extract_pvline.proto.bin` — [preserved redacted evidence](../evidence/descriptors/454e855f2c96f3f4ede1d57a75b5d8ae3d3ec9345c88fa34e5b3a913f33ca660.bin)

**Source references:** SRC-1071, SRC-1672  
**URL references:** None independently associated  
**Related findings:** FND-16107, FND-16108

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16110"></a>
## FND-16110: chesscom.explanation_engine.v1alpha.InternalFeatureExtractPVLineResponse.line = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureExtractPVLineResponse",
  "name": "line",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1071",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1071** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_extract_pvline.proto.bin` — [preserved redacted evidence](../evidence/descriptors/454e855f2c96f3f4ede1d57a75b5d8ae3d3ec9345c88fa34e5b3a913f33ca660.bin)

**Source references:** SRC-1071, SRC-1672  
**URL references:** None independently associated  
**Related findings:** FND-16107, FND-16108, FND-16109

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16111"></a>
## FND-16111: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGameFeaturesRequest",
  "field": [
    {
      "name": "ignore_missing_move_timestamps",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "skip_charm",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16112"></a>
## FND-16112: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesRequest.ignore_missing_move_timestamps = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesRequest",
  "name": "ignore_missing_move_timestamps",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16113"></a>
## FND-16113: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesRequest.skip_charm = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesRequest",
  "name": "skip_charm",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16114"></a>
## FND-16114: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGameFeaturesResponse",
  "field": [
    {
      "name": "moves",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.MoveFeatures"
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
      "type": "TYPE_UINT32"
    },
    {
      "name": "opening_name",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "white_accuracy",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "black_accuracy",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "white_game_rating",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PlayerGameRating"
    },
    {
      "name": "black_game_rating",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PlayerGameRating"
    },
    {
      "name": "computation",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GameFeatureComputation"
    },
    {
      "name": "features",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameFeatures"
    }
  ],
  "oneof_decl": [
    {
      "name": "_white_accuracy"
    },
    {
      "name": "_black_accuracy"
    }
  ]
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16115"></a>
## FND-16115: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.MoveFeatures",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16116"></a>
## FND-16116: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.eco_code = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "eco_code",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16117"></a>
## FND-16117: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.eco_family_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "eco_family_id",
  "number": 3,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16118"></a>
## FND-16118: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.opening_name = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "opening_name",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16119"></a>
## FND-16119: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.white_accuracy = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "white_accuracy",
  "number": 5,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_white_accuracy",
  "proto3_optional": true,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16120"></a>
## FND-16120: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.black_accuracy = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "black_accuracy",
  "number": 6,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_black_accuracy",
  "proto3_optional": true,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16121"></a>
## FND-16121: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.white_game_rating = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "white_game_rating",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1alpha.PlayerGameRating",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16122"></a>
## FND-16122: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.black_game_rating = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "black_game_rating",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1alpha.PlayerGameRating",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16123"></a>
## FND-16123: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.computation = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "computation",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1alpha.GameFeatureComputation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16124"></a>
## FND-16124: chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse.features = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGameFeaturesResponse",
  "name": "features",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1.GameFeatures",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1072",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1072** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_game_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8fcec798906fede23edc2f6976d4fceda0bcfbff373d6d65fe2c89675c9dc085.bin)

**Source references:** SRC-1072, SRC-1762  
**URL references:** None independently associated  
**Related findings:** FND-16111, FND-16112, FND-16113

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16125"></a>
## FND-16125: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGeneratePvtreeRequest",
  "field": [
    {
      "name": "depth",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "nodes",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "time_ms",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "at_least_n_root_moves",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "use_split_depth_limit",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "split_depth_limit",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "use_split_width_limit",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 6,
      "proto3_optional": true
    },
    {
      "name": "split_width_limit",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 7,
      "proto3_optional": true
    },
    {
      "name": "keep_equal_subtrees",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 8,
      "proto3_optional": true
    },
    {
      "name": "allowed_excess_depth",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 9,
      "proto3_optional": true
    },
    {
      "name": "allowed_excess_width",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 10,
      "proto3_optional": true
    },
    {
      "name": "rating",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 11,
      "proto3_optional": true
    },
    {
      "name": "ep_loss_margin",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT",
      "oneof_index": 12,
      "proto3_optional": true
    },
    {
      "name": "max_allowed_cp_margin",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 13,
      "proto3_optional": true
    },
    {
      "name": "return_lines_directly",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 14,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_depth"
    },
    {
      "name": "_nodes"
    },
    {
      "name": "_time_ms"
    },
    {
      "name": "_at_least_n_root_moves"
    },
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
    },
    {
      "name": "_max_allowed_cp_margin"
    },
    {
      "name": "_return_lines_directly"
    }
  ]
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16126"></a>
## FND-16126: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.depth = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "depth",
  "number": 1,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_depth",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16127"></a>
## FND-16127: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.nodes = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "nodes",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_nodes",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16128"></a>
## FND-16128: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.time_ms = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "time_ms",
  "number": 3,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_ms",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16129"></a>
## FND-16129: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.at_least_n_root_moves = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "at_least_n_root_moves",
  "number": 4,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_at_least_n_root_moves",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16130"></a>
## FND-16130: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.use_split_depth_limit = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "use_split_depth_limit",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_use_split_depth_limit",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16131"></a>
## FND-16131: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.split_depth_limit = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "split_depth_limit",
  "number": 6,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_split_depth_limit",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16132"></a>
## FND-16132: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.use_split_width_limit = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "use_split_width_limit",
  "number": 7,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_use_split_width_limit",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16133"></a>
## FND-16133: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.split_width_limit = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "split_width_limit",
  "number": 8,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_split_width_limit",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16134"></a>
## FND-16134: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.keep_equal_subtrees = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "keep_equal_subtrees",
  "number": 9,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_keep_equal_subtrees",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16135"></a>
## FND-16135: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.allowed_excess_depth = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "allowed_excess_depth",
  "number": 10,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_allowed_excess_depth",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16136"></a>
## FND-16136: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.allowed_excess_width = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "allowed_excess_width",
  "number": 11,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_allowed_excess_width",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16137"></a>
## FND-16137: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.rating = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "rating",
  "number": 12,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_rating",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16138"></a>
## FND-16138: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.ep_loss_margin = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "ep_loss_margin",
  "number": 13,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": "_ep_loss_margin",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16139"></a>
## FND-16139: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.max_allowed_cp_margin = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "max_allowed_cp_margin",
  "number": 14,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_max_allowed_cp_margin",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16140"></a>
## FND-16140: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest.return_lines_directly = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeRequest",
  "name": "return_lines_directly",
  "number": 15,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_return_lines_directly",
  "proto3_optional": true,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16141"></a>
## FND-16141: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGeneratePvtreeResponse",
  "field": [
    {
      "name": "good_evaluations",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Evaluation"
    },
    {
      "name": "bad_evaluations",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Evaluation"
    }
  ]
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16142"></a>
## FND-16142: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeResponse.good_evaluations = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeResponse",
  "name": "good_evaluations",
  "number": 1,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16143"></a>
## FND-16143: chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeResponse.bad_evaluations = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGeneratePvtreeResponse",
  "name": "bad_evaluations",
  "number": 2,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1073",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1073** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_pvtree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fc34196f04b375567d7d697adbb61bad3ecf988d02ba4382bc12b2739ba53e6b.bin)

**Source references:** SRC-1073, SRC-1853  
**URL references:** None independently associated  
**Related findings:** FND-16125, FND-16126, FND-16127

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16144"></a>
## FND-16144: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGenerateTrainItemsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGenerateTrainItemsRequest"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16145"></a>
## FND-16145: Native message: chesscom.explanation_engine.v1alpha.GeneratedTrainItem

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GeneratedTrainItem",
  "field": [
    {
      "name": "pre_pitch_fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "user_color",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "opponent_pitch_move",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "ply",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "source_played_move",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "challenge",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.train.v1.TrainChallenge"
    }
  ]
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16146"></a>
## FND-16146: chesscom.explanation_engine.v1alpha.GeneratedTrainItem.pre_pitch_fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "name": "pre_pitch_fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16147"></a>
## FND-16147: chesscom.explanation_engine.v1alpha.GeneratedTrainItem.user_color = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "name": "user_color",
  "number": 2,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16148"></a>
## FND-16148: chesscom.explanation_engine.v1alpha.GeneratedTrainItem.opponent_pitch_move = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "name": "opponent_pitch_move",
  "number": 3,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16149"></a>
## FND-16149: chesscom.explanation_engine.v1alpha.GeneratedTrainItem.ply = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "name": "ply",
  "number": 4,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16150"></a>
## FND-16150: chesscom.explanation_engine.v1alpha.GeneratedTrainItem.source_played_move = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "name": "source_played_move",
  "number": 5,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16151"></a>
## FND-16151: chesscom.explanation_engine.v1alpha.GeneratedTrainItem.challenge = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "name": "challenge",
  "number": 6,
  "type": ".chesscom.train.v1.TrainChallenge",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16152"></a>
## FND-16152: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGenerateTrainItemsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGenerateTrainItemsResponse",
  "field": [
    {
      "name": "train_items",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GeneratedTrainItem"
    }
  ]
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16153"></a>
## FND-16153: chesscom.explanation_engine.v1alpha.InternalFeatureGenerateTrainItemsResponse.train_items = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGenerateTrainItemsResponse",
  "name": "train_items",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.GeneratedTrainItem",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1074",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1074** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_generate_train_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a921e0e2cb3a65e595bd19931d22389ebc97ac9a872785b5fe61884815ee01e.bin)

**Source references:** SRC-1074, SRC-1801  
**URL references:** None independently associated  
**Related findings:** FND-16144, FND-16145, FND-16146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16154"></a>
## FND-16154: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoachEmotionRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetCoachEmotionRequest"
}

### Evidence

- **SRC-1075** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2ddcf998526a8561b20f8d8036e14a0079fafb48cdfc60557956abadae38c7e9.bin)

**Source references:** SRC-1075, SRC-1860  
**URL references:** None independently associated  
**Related findings:** FND-16155, FND-16156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16155"></a>
## FND-16155: Native message: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoachEmotionResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetCoachEmotionResponse",
  "field": [
    {
      "name": "coach_emotion",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.CoachEmotion"
    },
    {
      "name": "debug_info",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo"
    }
  ]
}

### Evidence

- **SRC-1075** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2ddcf998526a8561b20f8d8036e14a0079fafb48cdfc60557956abadae38c7e9.bin)

**Source references:** SRC-1075, SRC-1860  
**URL references:** None independently associated  
**Related findings:** FND-16154, FND-16156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16156"></a>
## FND-16156: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoachEmotionResponse.coach_emotion = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoachEmotionResponse",
  "name": "coach_emotion",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CoachEmotion",
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
**Related findings:** FND-16154, FND-16155

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16157"></a>
## FND-16157: chesscom.explanation_engine.v1alpha.InternalFeatureGetCoachEmotionResponse.debug_info = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InternalFeatureGetCoachEmotionResponse",
  "name": "debug_info",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo",
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

<a id="FND-16158"></a>
## FND-16158: Native message: chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CoachEmotionDebugInfo",
  "field": [
    {
      "name": "is_key_moment",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "move_classification",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "move_precision",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "who_moved",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1075** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_internal_feature_get_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2ddcf998526a8561b20f8d8036e14a0079fafb48cdfc60557956abadae38c7e9.bin)

**Source references:** SRC-1075, SRC-1860  
**URL references:** None independently associated  
**Related findings:** FND-16154, FND-16155, FND-16156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-16159"></a>
## FND-16159: chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo.is_key_moment = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.CoachEmotionDebugInfo",
  "name": "is_key_moment",
  "number": 1,
  "type": "TYPE_BOOL",
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
