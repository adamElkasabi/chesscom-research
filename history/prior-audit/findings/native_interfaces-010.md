# native_interfaces — findings 901–1000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13560"></a>
## FND-13560: chesscom.explanation_engine.v1.BotConfigResourcesResponse.book = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotConfigResourcesResponse",
  "name": "book",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.BookResource",
  "label": "LABEL_OPTIONAL",
  "oneof": "_book",
  "proto3_optional": true,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13561"></a>
## FND-13561: chesscom.explanation_engine.v1.BotConfigResourcesResponse.nn = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotConfigResourcesResponse",
  "name": "nn",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.NnResource",
  "label": "LABEL_OPTIONAL",
  "oneof": "_nn",
  "proto3_optional": true,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13562"></a>
## FND-13562: Native message: chesscom.explanation_engine.v1.BotMoveFromConfigRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BotMoveFromConfigRequest",
  "field": [
    {
      "name": "bot_config",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "artifact_id",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "proto_config",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.BotMoveConfiguration",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_proto_config"
    }
  ]
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13563, FND-13564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13563"></a>
## FND-13563: chesscom.explanation_engine.v1.BotMoveFromConfigRequest.bot_config = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveFromConfigRequest",
  "name": "bot_config",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0919",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13562, FND-13564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13564"></a>
## FND-13564: chesscom.explanation_engine.v1.BotMoveFromConfigRequest.artifact_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveFromConfigRequest",
  "name": "artifact_id",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0919",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13562, FND-13563

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13565"></a>
## FND-13565: chesscom.explanation_engine.v1.BotMoveFromConfigRequest.proto_config = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveFromConfigRequest",
  "name": "proto_config",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.BotMoveConfiguration",
  "label": "LABEL_OPTIONAL",
  "oneof": "_proto_config",
  "proto3_optional": true,
  "source_id": "SRC-0919",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13562, FND-13563, FND-13564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13566"></a>
## FND-13566: Native message: chesscom.explanation_engine.v1.BotMoveFromConfigResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BotMoveFromConfigResponse",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "suggested_delay_seconds",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_suggested_delay_seconds"
    }
  ]
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13562, FND-13563, FND-13564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13567"></a>
## FND-13567: chesscom.explanation_engine.v1.BotMoveFromConfigResponse.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveFromConfigResponse",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0919",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13562, FND-13563, FND-13564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13568"></a>
## FND-13568: chesscom.explanation_engine.v1.BotMoveFromConfigResponse.suggested_delay_seconds = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveFromConfigResponse",
  "name": "suggested_delay_seconds",
  "number": 2,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_suggested_delay_seconds",
  "proto3_optional": true,
  "source_id": "SRC-0919",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0919** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_move_from_config.proto.bin` — [preserved redacted evidence](../evidence/descriptors/cf3d205658502697498fa600f96ffab16dce0b4931d77a4b2c2e5ac04939c57e.bin)

**Source references:** SRC-0919, SRC-1668  
**URL references:** None independently associated  
**Related findings:** FND-13562, FND-13563, FND-13564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13569"></a>
## FND-13569: Native message: chesscom.explanation_engine.v1.CeeInternalComponentsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CeeInternalComponentsRequest"
}

### Evidence

- **SRC-0920** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_internal_components.proto.bin` — [preserved redacted evidence](../evidence/descriptors/42aac98ec160c4ad885c01044128529bf66b452bb08985928ec48c753f697fa5.bin)

**Source references:** SRC-0920, SRC-1696  
**URL references:** None independently associated  
**Related findings:** FND-13570, FND-13571

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13570"></a>
## FND-13570: Native message: chesscom.explanation_engine.v1.CeeInternalComponentsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CeeInternalComponentsResponse",
  "field": [
    {
      "name": "components",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.CeeInternalComponent"
    }
  ]
}

### Evidence

- **SRC-0920** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_internal_components.proto.bin` — [preserved redacted evidence](../evidence/descriptors/42aac98ec160c4ad885c01044128529bf66b452bb08985928ec48c753f697fa5.bin)

**Source references:** SRC-0920, SRC-1696  
**URL references:** None independently associated  
**Related findings:** FND-13569, FND-13571

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13571"></a>
## FND-13571: chesscom.explanation_engine.v1.CeeInternalComponentsResponse.components = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CeeInternalComponentsResponse",
  "name": "components",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CeeInternalComponent",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0920",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0920** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_internal_components.proto.bin` — [preserved redacted evidence](../evidence/descriptors/42aac98ec160c4ad885c01044128529bf66b452bb08985928ec48c753f697fa5.bin)

**Source references:** SRC-0920, SRC-1696  
**URL references:** None independently associated  
**Related findings:** FND-13569, FND-13570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13572"></a>
## FND-13572: Native message: chesscom.explanation_engine.v1.CeeVersionRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CeeVersionRequest"
}

### Evidence

- **SRC-0921** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2336a5dc15babdb552a87148d1b669a6131febe9c5ed7a7f4b5e152bfcb05632.bin)

**Source references:** SRC-0921, SRC-1896  
**URL references:** None independently associated  
**Related findings:** FND-13573, FND-13574

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13573"></a>
## FND-13573: Native message: chesscom.explanation_engine.v1.CeeVersionResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CeeVersionResponse",
  "field": [
    {
      "name": "cee_version",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.api.v1.SemanticVersion"
    },
    {
      "name": "cee_git_sha",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "definitions_git_sha",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "uci_version",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.api.v1.SemanticVersion"
    }
  ]
}

### Evidence

- **SRC-0921** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2336a5dc15babdb552a87148d1b669a6131febe9c5ed7a7f4b5e152bfcb05632.bin)

**Source references:** SRC-0921, SRC-1896  
**URL references:** None independently associated  
**Related findings:** FND-13572, FND-13574

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13574"></a>
## FND-13574: chesscom.explanation_engine.v1.CeeVersionResponse.cee_version = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CeeVersionResponse",
  "name": "cee_version",
  "number": 1,
  "type": ".chesscom.api.v1.SemanticVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0921",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0921** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2336a5dc15babdb552a87148d1b669a6131febe9c5ed7a7f4b5e152bfcb05632.bin)

**Source references:** SRC-0921, SRC-1896  
**URL references:** None independently associated  
**Related findings:** FND-13572, FND-13573

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13575"></a>
## FND-13575: chesscom.explanation_engine.v1.CeeVersionResponse.cee_git_sha = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CeeVersionResponse",
  "name": "cee_git_sha",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0921",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0921** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2336a5dc15babdb552a87148d1b669a6131febe9c5ed7a7f4b5e152bfcb05632.bin)

**Source references:** SRC-0921, SRC-1896  
**URL references:** None independently associated  
**Related findings:** FND-13572, FND-13573, FND-13574

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13576"></a>
## FND-13576: chesscom.explanation_engine.v1.CeeVersionResponse.definitions_git_sha = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CeeVersionResponse",
  "name": "definitions_git_sha",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0921",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0921** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2336a5dc15babdb552a87148d1b669a6131febe9c5ed7a7f4b5e152bfcb05632.bin)

**Source references:** SRC-0921, SRC-1896  
**URL references:** None independently associated  
**Related findings:** FND-13572, FND-13573, FND-13574

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13577"></a>
## FND-13577: chesscom.explanation_engine.v1.CeeVersionResponse.uci_version = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CeeVersionResponse",
  "name": "uci_version",
  "number": 4,
  "type": ".chesscom.api.v1.SemanticVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0921",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0921** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_cee_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2336a5dc15babdb552a87148d1b669a6131febe9c5ed7a7f4b5e152bfcb05632.bin)

**Source references:** SRC-0921, SRC-1896  
**URL references:** None independently associated  
**Related findings:** FND-13572, FND-13573, FND-13574

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13578"></a>
## FND-13578: Native message: chesscom.explanation_engine.v1.CharmInferenceRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmInferenceRequest",
  "field": [
    {
      "name": "grv2",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CharmGameRatingV2Settings",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "tricky",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CharmTrickySettings",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_grv2"
    },
    {
      "name": "_tricky"
    }
  ]
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13579, FND-13580

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13579"></a>
## FND-13579: chesscom.explanation_engine.v1.CharmInferenceRequest.grv2 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceRequest",
  "name": "grv2",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CharmGameRatingV2Settings",
  "label": "LABEL_OPTIONAL",
  "oneof": "_grv2",
  "proto3_optional": true,
  "source_id": "SRC-0922",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13578, FND-13580

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13580"></a>
## FND-13580: chesscom.explanation_engine.v1.CharmInferenceRequest.tricky = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceRequest",
  "name": "tricky",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.CharmTrickySettings",
  "label": "LABEL_OPTIONAL",
  "oneof": "_tricky",
  "proto3_optional": true,
  "source_id": "SRC-0922",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13578, FND-13579

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13581"></a>
## FND-13581: Native message: chesscom.explanation_engine.v1.CharmInferenceResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmInferenceResponse",
  "field": [
    {
      "name": "results",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CharmInferenceResult"
    }
  ]
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13578, FND-13579, FND-13580

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13582"></a>
## FND-13582: chesscom.explanation_engine.v1.CharmInferenceResponse.results = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResponse",
  "name": "results",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CharmInferenceResult",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0922",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13578, FND-13579, FND-13580

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13583"></a>
## FND-13583: Native message: chesscom.explanation_engine.v1.CharmGameRatingV2Settings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmGameRatingV2Settings"
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13578, FND-13579, FND-13580

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13584"></a>
## FND-13584: Native message: chesscom.explanation_engine.v1.CharmTrickySettings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmTrickySettings"
}

### Evidence

- **SRC-0922** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4ea6bc96ed648ea5060a3f0e843366ebddace5f2bd49d9406787828ee515dae6.bin)

**Source references:** SRC-0922, SRC-1751  
**URL references:** None independently associated  
**Related findings:** FND-13578, FND-13579, FND-13580

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13585"></a>
## FND-13585: Native message: chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ConvertFromProtoMovesRequest",
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
      "name": "moves",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0923** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_from_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c3e967e20589373538482067b2848f7f243c273fe1657882a3d64b4e498952a8.bin)

**Source references:** SRC-0923, SRC-1745  
**URL references:** None independently associated  
**Related findings:** FND-13586, FND-13587

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13586"></a>
## FND-13586: chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest.move_notation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest",
  "name": "move_notation",
  "number": 1,
  "type": ".chesscom.chess.v1.MoveNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0923",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0923** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_from_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c3e967e20589373538482067b2848f7f243c273fe1657882a3d64b4e498952a8.bin)

**Source references:** SRC-0923, SRC-1745  
**URL references:** None independently associated  
**Related findings:** FND-13585, FND-13587

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13587"></a>
## FND-13587: chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest.initial_fen = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest",
  "name": "initial_fen",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0923",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0923** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_from_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c3e967e20589373538482067b2848f7f243c273fe1657882a3d64b4e498952a8.bin)

**Source references:** SRC-0923, SRC-1745  
**URL references:** None independently associated  
**Related findings:** FND-13585, FND-13586

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13588"></a>
## FND-13588: chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest.moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertFromProtoMovesRequest",
  "name": "moves",
  "number": 3,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0923",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0923** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_from_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c3e967e20589373538482067b2848f7f243c273fe1657882a3d64b4e498952a8.bin)

**Source references:** SRC-0923, SRC-1745  
**URL references:** None independently associated  
**Related findings:** FND-13585, FND-13586, FND-13587

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13589"></a>
## FND-13589: Native message: chesscom.explanation_engine.v1.ConvertFromProtoMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ConvertFromProtoMovesResponse",
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

- **SRC-0923** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_from_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c3e967e20589373538482067b2848f7f243c273fe1657882a3d64b4e498952a8.bin)

**Source references:** SRC-0923, SRC-1745  
**URL references:** None independently associated  
**Related findings:** FND-13585, FND-13586, FND-13587

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13590"></a>
## FND-13590: chesscom.explanation_engine.v1.ConvertFromProtoMovesResponse.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertFromProtoMovesResponse",
  "name": "moves",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0923",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0923** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_from_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c3e967e20589373538482067b2848f7f243c273fe1657882a3d64b4e498952a8.bin)

**Source references:** SRC-0923, SRC-1745  
**URL references:** None independently associated  
**Related findings:** FND-13585, FND-13586, FND-13587

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13591"></a>
## FND-13591: Native message: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ConvertToProtoMovesRequest",
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
      "name": "moves_to_convert",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0924** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3c2cb85f2e9e02f5bf2c9ab578037bce913a403fc4876f5dad2fd40c00c5cf6e.bin)

**Source references:** SRC-0924, SRC-1854  
**URL references:** None independently associated  
**Related findings:** FND-13592, FND-13593

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13592"></a>
## FND-13592: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest.move_notation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertToProtoMovesRequest",
  "name": "move_notation",
  "number": 1,
  "type": ".chesscom.chess.v1.MoveNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0924",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0924** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3c2cb85f2e9e02f5bf2c9ab578037bce913a403fc4876f5dad2fd40c00c5cf6e.bin)

**Source references:** SRC-0924, SRC-1854  
**URL references:** None independently associated  
**Related findings:** FND-13591, FND-13593

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13593"></a>
## FND-13593: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest.initial_fen = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertToProtoMovesRequest",
  "name": "initial_fen",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0924",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0924** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3c2cb85f2e9e02f5bf2c9ab578037bce913a403fc4876f5dad2fd40c00c5cf6e.bin)

**Source references:** SRC-0924, SRC-1854  
**URL references:** None independently associated  
**Related findings:** FND-13591, FND-13592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13594"></a>
## FND-13594: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest.moves_to_convert = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertToProtoMovesRequest",
  "name": "moves_to_convert",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0924",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0924** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3c2cb85f2e9e02f5bf2c9ab578037bce913a403fc4876f5dad2fd40c00c5cf6e.bin)

**Source references:** SRC-0924, SRC-1854  
**URL references:** None independently associated  
**Related findings:** FND-13591, FND-13592, FND-13593

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13595"></a>
## FND-13595: Native message: chesscom.explanation_engine.v1.ConvertToProtoMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ConvertToProtoMovesResponse",
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

- **SRC-0924** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3c2cb85f2e9e02f5bf2c9ab578037bce913a403fc4876f5dad2fd40c00c5cf6e.bin)

**Source references:** SRC-0924, SRC-1854  
**URL references:** None independently associated  
**Related findings:** FND-13591, FND-13592, FND-13593

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13596"></a>
## FND-13596: chesscom.explanation_engine.v1.ConvertToProtoMovesResponse.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ConvertToProtoMovesResponse",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0924",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0924** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_convert_to_proto_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3c2cb85f2e9e02f5bf2c9ab578037bce913a403fc4876f5dad2fd40c00c5cf6e.bin)

**Source references:** SRC-0924, SRC-1854  
**URL references:** None independently associated  
**Related findings:** FND-13591, FND-13592, FND-13593

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13597"></a>
## FND-13597: Native message: chesscom.explanation_engine.v1.DeletePgnMoveRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DeletePgnMoveRequest"
}

### Evidence

- **SRC-0925** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_delete_pgn_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2b9b5d3b37f8dedec87f4ad01a9184dba4c4c5f9fb17b50be7b63dde6d6ed074.bin)

**Source references:** SRC-0925, SRC-1735  
**URL references:** None independently associated  
**Related findings:** FND-13598

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13598"></a>
## FND-13598: Native message: chesscom.explanation_engine.v1.DeletePgnMoveResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DeletePgnMoveResponse"
}

### Evidence

- **SRC-0925** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_delete_pgn_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2b9b5d3b37f8dedec87f4ad01a9184dba4c4c5f9fb17b50be7b63dde6d6ed074.bin)

**Source references:** SRC-0925, SRC-1735  
**URL references:** None independently associated  
**Related findings:** FND-13597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13599"></a>
## FND-13599: Native message: chesscom.explanation_engine.v1.EditPgnMoveAnnotationRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EditPgnMoveAnnotationRequest",
  "field": [
    {
      "name": "comment",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "before_comment",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_comment"
    },
    {
      "name": "_before_comment"
    }
  ]
}

### Evidence

- **SRC-0926** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0758976785628b938640de20d0d21bb4ac1307950c8c7f09552be1b5a4de8fec.bin)

**Source references:** SRC-0926, SRC-1678  
**URL references:** None independently associated  
**Related findings:** FND-13600, FND-13601

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13600"></a>
## FND-13600: chesscom.explanation_engine.v1.EditPgnMoveAnnotationRequest.comment = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EditPgnMoveAnnotationRequest",
  "name": "comment",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_comment",
  "proto3_optional": true,
  "source_id": "SRC-0926",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0926** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0758976785628b938640de20d0d21bb4ac1307950c8c7f09552be1b5a4de8fec.bin)

**Source references:** SRC-0926, SRC-1678  
**URL references:** None independently associated  
**Related findings:** FND-13599, FND-13601

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13601"></a>
## FND-13601: chesscom.explanation_engine.v1.EditPgnMoveAnnotationRequest.before_comment = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EditPgnMoveAnnotationRequest",
  "name": "before_comment",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_before_comment",
  "proto3_optional": true,
  "source_id": "SRC-0926",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0926** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0758976785628b938640de20d0d21bb4ac1307950c8c7f09552be1b5a4de8fec.bin)

**Source references:** SRC-0926, SRC-1678  
**URL references:** None independently associated  
**Related findings:** FND-13599, FND-13600

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13602"></a>
## FND-13602: Native message: chesscom.explanation_engine.v1.EditPgnMoveAnnotationResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EditPgnMoveAnnotationResponse"
}

### Evidence

- **SRC-0926** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0758976785628b938640de20d0d21bb4ac1307950c8c7f09552be1b5a4de8fec.bin)

**Source references:** SRC-0926, SRC-1678  
**URL references:** None independently associated  
**Related findings:** FND-13599, FND-13600, FND-13601

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13603"></a>
## FND-13603: Native message: chesscom.explanation_engine.v1.EditPgnNagsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EditPgnNagsRequest",
  "field": [
    {
      "name": "nags",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0927** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_nags.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c8603fdc9df7cc85ff45f26f00c98df1e8f594b3c3772dc302c9592d91a8f8b1.bin)

**Source references:** SRC-0927, SRC-1695  
**URL references:** None independently associated  
**Related findings:** FND-13604, FND-13605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13604"></a>
## FND-13604: chesscom.explanation_engine.v1.EditPgnNagsRequest.nags = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EditPgnNagsRequest",
  "name": "nags",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0927",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0927** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_nags.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c8603fdc9df7cc85ff45f26f00c98df1e8f594b3c3772dc302c9592d91a8f8b1.bin)

**Source references:** SRC-0927, SRC-1695  
**URL references:** None independently associated  
**Related findings:** FND-13603, FND-13605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13605"></a>
## FND-13605: Native message: chesscom.explanation_engine.v1.EditPgnNagsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EditPgnNagsResponse"
}

### Evidence

- **SRC-0927** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_edit_pgn_nags.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c8603fdc9df7cc85ff45f26f00c98df1e8f594b3c3772dc302c9592d91a8f8b1.bin)

**Source references:** SRC-0927, SRC-1695  
**URL references:** None independently associated  
**Related findings:** FND-13603, FND-13604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13606"></a>
## FND-13606: Native message: chesscom.explanation_engine.v1.ExtendedSearchParameters

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ExtendedSearchParameters",
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
      "type_name": ".chesscom.explanation_engine.v1.SearchParameters",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_null_move_search_parameters"
    }
  ]
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13607"></a>
## FND-13607: chesscom.explanation_engine.v1.ExtendedSearchParameters.search_parameters = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExtendedSearchParameters",
  "name": "search_parameters",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13608"></a>
## FND-13608: chesscom.explanation_engine.v1.ExtendedSearchParameters.null_move_search_parameters = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExtendedSearchParameters",
  "name": "null_move_search_parameters",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.SearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": "_null_move_search_parameters",
  "proto3_optional": true,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13609"></a>
## FND-13609: Native message: chesscom.explanation_engine.v1.EvaluateGameRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EvaluateGameRequest",
  "field": [
    {
      "name": "extended_search_parameters",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.ExtendedSearchParameters",
      "oneof_index": 0
    },
    {
      "name": "game_review_search_settings",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
      "oneof_index": 0
    },
    {
      "name": "starting_game_point",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "stream_progress_updates",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "engine_id",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "reduce_nodes_on_successive_searches",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "reduce_nodes_on_successive_multisearch_searches",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "enable_soft_nodes_limit",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "heartbeat_interval_seconds",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "torch_search_mode",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TorchSearchMode",
      "oneof_index": 3,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "search"
    },
    {
      "name": "_starting_game_point"
    },
    {
      "name": "_engine_id"
    },
    {
      "name": "_torch_search_mode"
    }
  ]
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13610"></a>
## FND-13610: chesscom.explanation_engine.v1.EvaluateGameRequest.extended_search_parameters = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "extended_search_parameters",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.ExtendedSearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13611"></a>
## FND-13611: chesscom.explanation_engine.v1.EvaluateGameRequest.game_review_search_settings = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "game_review_search_settings",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13612"></a>
## FND-13612: chesscom.explanation_engine.v1.EvaluateGameRequest.starting_game_point = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "starting_game_point",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_starting_game_point",
  "proto3_optional": true,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13613"></a>
## FND-13613: chesscom.explanation_engine.v1.EvaluateGameRequest.stream_progress_updates = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "stream_progress_updates",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13614"></a>
## FND-13614: chesscom.explanation_engine.v1.EvaluateGameRequest.engine_id = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "engine_id",
  "number": 6,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine_id",
  "proto3_optional": true,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13615"></a>
## FND-13615: chesscom.explanation_engine.v1.EvaluateGameRequest.reduce_nodes_on_successive_searches = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "reduce_nodes_on_successive_searches",
  "number": 7,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13616"></a>
## FND-13616: chesscom.explanation_engine.v1.EvaluateGameRequest.reduce_nodes_on_successive_multisearch_searches = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "reduce_nodes_on_successive_multisearch_searches",
  "number": 8,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13617"></a>
## FND-13617: chesscom.explanation_engine.v1.EvaluateGameRequest.enable_soft_nodes_limit = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "enable_soft_nodes_limit",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13618"></a>
## FND-13618: chesscom.explanation_engine.v1.EvaluateGameRequest.heartbeat_interval_seconds = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "heartbeat_interval_seconds",
  "number": 9,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13619"></a>
## FND-13619: chesscom.explanation_engine.v1.EvaluateGameRequest.torch_search_mode = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameRequest",
  "name": "torch_search_mode",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1.TorchSearchMode",
  "label": "LABEL_OPTIONAL",
  "oneof": "_torch_search_mode",
  "proto3_optional": true,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13620"></a>
## FND-13620: Native message: chesscom.explanation_engine.v1.EvaluateGameResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EvaluateGameResponse",
  "field": [
    {
      "name": "progress",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "game_state",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "evaluated_positions_count",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "is_heartbeat",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ],
  "oneof_decl": [
    {
      "name": "_game_state"
    }
  ]
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13621"></a>
## FND-13621: chesscom.explanation_engine.v1.EvaluateGameResponse.progress = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameResponse",
  "name": "progress",
  "number": 1,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13622"></a>
## FND-13622: chesscom.explanation_engine.v1.EvaluateGameResponse.game_state = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameResponse",
  "name": "game_state",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GameState",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_state",
  "proto3_optional": true,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13623"></a>
## FND-13623: chesscom.explanation_engine.v1.EvaluateGameResponse.evaluated_positions_count = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameResponse",
  "name": "evaluated_positions_count",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13624"></a>
## FND-13624: chesscom.explanation_engine.v1.EvaluateGameResponse.is_heartbeat = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvaluateGameResponse",
  "name": "is_heartbeat",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0928",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0928** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_evaluate_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8ea96679a62b84644da8c0d61b1e5c5e52c7f9ba877a721d58e92278a7c87118.bin)

**Source references:** SRC-0928, SRC-1684  
**URL references:** None independently associated  
**Related findings:** FND-13606, FND-13607, FND-13608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13625"></a>
## FND-13625: Native message: chesscom.explanation_engine.v1.ExpectedPointsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ExpectedPointsRequest"
}

### Evidence

- **SRC-0929** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_expected_points.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ec1894efd8980a7f4faa6996345b7924d94eeeb86d9fb06bf5d3b9f0a7c39546.bin)

**Source references:** SRC-0929, SRC-1659  
**URL references:** None independently associated  
**Related findings:** FND-13626, FND-13627

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13626"></a>
## FND-13626: Native message: chesscom.explanation_engine.v1.ExpectedPointsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ExpectedPointsResponse",
  "field": [
    {
      "name": "expected_points",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0929** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_expected_points.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ec1894efd8980a7f4faa6996345b7924d94eeeb86d9fb06bf5d3b9f0a7c39546.bin)

**Source references:** SRC-0929, SRC-1659  
**URL references:** None independently associated  
**Related findings:** FND-13625, FND-13627

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13627"></a>
## FND-13627: chesscom.explanation_engine.v1.ExpectedPointsResponse.expected_points = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExpectedPointsResponse",
  "name": "expected_points",
  "number": 1,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0929",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0929** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_expected_points.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ec1894efd8980a7f4faa6996345b7924d94eeeb86d9fb06bf5d3b9f0a7c39546.bin)

**Source references:** SRC-0929, SRC-1659  
**URL references:** None independently associated  
**Related findings:** FND-13625, FND-13626

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13628"></a>
## FND-13628: Native message: chesscom.explanation_engine.v1.ForceCrashRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ForceCrashRequest"
}

### Evidence

- **SRC-0930** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_force_crash.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c4044e2293b7139ccfcb07c0708d2ceb39c2a25db1fea80d9b7e8f34626bab.bin)

**Source references:** SRC-0930, SRC-1808  
**URL references:** None independently associated  
**Related findings:** FND-13629

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13629"></a>
## FND-13629: Native message: chesscom.explanation_engine.v1.ForceCrashResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ForceCrashResponse"
}

### Evidence

- **SRC-0930** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_force_crash.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c4044e2293b7139ccfcb07c0708d2ceb39c2a25db1fea80d9b7e8f34626bab.bin)

**Source references:** SRC-0930, SRC-1808  
**URL references:** None independently associated  
**Related findings:** FND-13628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13630"></a>
## FND-13630: Native message: chesscom.explanation_engine.v1.GameAnalysisRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameAnalysisRequest",
  "field": [
    {
      "name": "starting_game_point",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "locale",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.Locale"
    },
    {
      "name": "game_phase_version",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.GamePhaseVersion",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "speech_version",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.GameAnalysisSpeechVersion",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "move_classification_version",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassificationVersion",
      "oneof_index": 3,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_starting_game_point"
    },
    {
      "name": "_game_phase_version"
    },
    {
      "name": "_speech_version"
    },
    {
      "name": "_move_classification_version"
    }
  ]
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13631, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13631"></a>
## FND-13631: chesscom.explanation_engine.v1.GameAnalysisRequest.starting_game_point = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameAnalysisRequest",
  "name": "starting_game_point",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_starting_game_point",
  "proto3_optional": true,
  "source_id": "SRC-0931",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13632"></a>
## FND-13632: chesscom.explanation_engine.v1.GameAnalysisRequest.locale = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameAnalysisRequest",
  "name": "locale",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Locale",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0931",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13633"></a>
## FND-13633: chesscom.explanation_engine.v1.GameAnalysisRequest.game_phase_version = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameAnalysisRequest",
  "name": "game_phase_version",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GamePhaseVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_phase_version",
  "proto3_optional": true,
  "source_id": "SRC-0931",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13631, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13634"></a>
## FND-13634: chesscom.explanation_engine.v1.GameAnalysisRequest.speech_version = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameAnalysisRequest",
  "name": "speech_version",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.GameAnalysisSpeechVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_speech_version",
  "proto3_optional": true,
  "source_id": "SRC-0931",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13631, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13635"></a>
## FND-13635: chesscom.explanation_engine.v1.GameAnalysisRequest.move_classification_version = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameAnalysisRequest",
  "name": "move_classification_version",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.MoveClassificationVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move_classification_version",
  "proto3_optional": true,
  "source_id": "SRC-0931",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13631, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13636"></a>
## FND-13636: Native message: chesscom.explanation_engine.v1.GameAnalysisResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameAnalysisResponse",
  "field": [
    {
      "name": "game_analysis",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameAnalysis"
    }
  ]
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13631, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13637"></a>
## FND-13637: chesscom.explanation_engine.v1.GameAnalysisResponse.game_analysis = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameAnalysisResponse",
  "name": "game_analysis",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameAnalysis",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0931",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0931** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/31da65caa400079004f470a443bc4b77ee327eb42a1355faf02928dbb6ea685f.bin)

**Source references:** SRC-0931, SRC-1812  
**URL references:** None independently associated  
**Related findings:** FND-13630, FND-13631, FND-13632

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13638"></a>
## FND-13638: Native message: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GamePhaseTransitionsRequest",
  "field": [
    {
      "name": "starting_game_point",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "game_phase_version",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.GamePhaseVersion",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_starting_game_point"
    },
    {
      "name": "_game_phase_version"
    }
  ]
}

### Evidence

- **SRC-0932** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_phase_transitions.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54e07db092c1a51f8e30d7daf1c3655188d4d9ecb5dabb467f1fcc7a8dfe70c5.bin)

**Source references:** SRC-0932, SRC-1741  
**URL references:** None independently associated  
**Related findings:** FND-13639, FND-13640

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13639"></a>
## FND-13639: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest.starting_game_point = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseTransitionsRequest",
  "name": "starting_game_point",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_starting_game_point",
  "proto3_optional": true,
  "source_id": "SRC-0932",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0932** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_phase_transitions.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54e07db092c1a51f8e30d7daf1c3655188d4d9ecb5dabb467f1fcc7a8dfe70c5.bin)

**Source references:** SRC-0932, SRC-1741  
**URL references:** None independently associated  
**Related findings:** FND-13638, FND-13640

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13640"></a>
## FND-13640: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest.game_phase_version = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseTransitionsRequest",
  "name": "game_phase_version",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GamePhaseVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_phase_version",
  "proto3_optional": true,
  "source_id": "SRC-0932",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0932** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_phase_transitions.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54e07db092c1a51f8e30d7daf1c3655188d4d9ecb5dabb467f1fcc7a8dfe70c5.bin)

**Source references:** SRC-0932, SRC-1741  
**URL references:** None independently associated  
**Related findings:** FND-13638, FND-13639

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13641"></a>
## FND-13641: Native message: chesscom.explanation_engine.v1.GamePhaseTransitionsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GamePhaseTransitionsResponse",
  "field": [
    {
      "name": "game_phase_transition",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePhaseTransitions"
    }
  ]
}

### Evidence

- **SRC-0932** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_phase_transitions.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54e07db092c1a51f8e30d7daf1c3655188d4d9ecb5dabb467f1fcc7a8dfe70c5.bin)

**Source references:** SRC-0932, SRC-1741  
**URL references:** None independently associated  
**Related findings:** FND-13638, FND-13639, FND-13640

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13642"></a>
## FND-13642: chesscom.explanation_engine.v1.GamePhaseTransitionsResponse.game_phase_transition = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseTransitionsResponse",
  "name": "game_phase_transition",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePhaseTransitions",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0932",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0932** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_phase_transitions.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54e07db092c1a51f8e30d7daf1c3655188d4d9ecb5dabb467f1fcc7a8dfe70c5.bin)

**Source references:** SRC-0932, SRC-1741  
**URL references:** None independently associated  
**Related findings:** FND-13638, FND-13639, FND-13640

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13643"></a>
## FND-13643: Native message: chesscom.explanation_engine.v1.GamePointInfoRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GamePointInfoRequest"
}

### Evidence

- **SRC-0933** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_point_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/901075d85a34e2a4e60f8457aceeea0b11c6d80f1ffb46af652b9645908ad63c.bin)

**Source references:** SRC-0933, SRC-1805  
**URL references:** None independently associated  
**Related findings:** FND-13644, FND-13645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13644"></a>
## FND-13644: Native message: chesscom.explanation_engine.v1.GamePointInfoResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GamePointInfoResponse",
  "field": [
    {
      "name": "game_point_info",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
    }
  ]
}

### Evidence

- **SRC-0933** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_point_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/901075d85a34e2a4e60f8457aceeea0b11c6d80f1ffb46af652b9645908ad63c.bin)

**Source references:** SRC-0933, SRC-1805  
**URL references:** None independently associated  
**Related findings:** FND-13643, FND-13645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13645"></a>
## FND-13645: chesscom.explanation_engine.v1.GamePointInfoResponse.game_point_info = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePointInfoResponse",
  "name": "game_point_info",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0933",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0933** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_point_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/901075d85a34e2a4e60f8457aceeea0b11c6d80f1ffb46af652b9645908ad63c.bin)

**Source references:** SRC-0933, SRC-1805  
**URL references:** None independently associated  
**Related findings:** FND-13643, FND-13644

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13646"></a>
## FND-13646: Native message: chesscom.explanation_engine.v1.GameReviewRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameReviewRequest",
  "field": [
    {
      "name": "stats",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.AdvancedStatsForGame",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "starting_game_point",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "uci_options",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry"
    },
    {
      "name": "include_train_takeaways",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "can_access_locked_takeaways",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ],
  "nested_type": [
    {
      "name": "UciOptionsEntry",
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
      "name": "_stats"
    },
    {
      "name": "_starting_game_point"
    }
  ]
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13647"></a>
## FND-13647: chesscom.explanation_engine.v1.GameReviewRequest.stats = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest",
  "name": "stats",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.AdvancedStatsForGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "_stats",
  "proto3_optional": true,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13648"></a>
## FND-13648: chesscom.explanation_engine.v1.GameReviewRequest.starting_game_point = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest",
  "name": "starting_game_point",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_starting_game_point",
  "proto3_optional": true,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13649"></a>
## FND-13649: chesscom.explanation_engine.v1.GameReviewRequest.uci_options = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest",
  "name": "uci_options",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13650"></a>
## FND-13650: chesscom.explanation_engine.v1.GameReviewRequest.include_train_takeaways = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest",
  "name": "include_train_takeaways",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13651"></a>
## FND-13651: chesscom.explanation_engine.v1.GameReviewRequest.can_access_locked_takeaways = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest",
  "name": "can_access_locked_takeaways",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13652"></a>
## FND-13652: Native message: chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "UciOptionsEntry",
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

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13653"></a>
## FND-13653: chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13654"></a>
## FND-13654: chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry",
  "name": "value",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13655"></a>
## FND-13655: Native message: chesscom.explanation_engine.v1.GameReviewResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameReviewResponse",
  "field": [
    {
      "name": "game_review",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameReview"
    }
  ]
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13656"></a>
## FND-13656: chesscom.explanation_engine.v1.GameReviewResponse.game_review = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewResponse",
  "name": "game_review",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameReview",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0934",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0934** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_review.proto.bin` — [preserved redacted evidence](../evidence/descriptors/91c331d8a736615ff4f15965a1f0c56877bdc9d273b272892959aeeda9bd0a38.bin)

**Source references:** SRC-0934, SRC-1726  
**URL references:** None independently associated  
**Related findings:** FND-13646, FND-13647, FND-13648

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13657"></a>
## FND-13657: Native message: chesscom.explanation_engine.v1.GameTreeRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameTreeRequest"
}

### Evidence

- **SRC-0935** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_tree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/160e47cb8eb4e6d05bdf6566aafd9914158e521646220d44b7b1de6985b2268a.bin)

**Source references:** SRC-0935, SRC-1822  
**URL references:** None independently associated  
**Related findings:** FND-13658, FND-13659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13658"></a>
## FND-13658: Native message: chesscom.explanation_engine.v1.GameTreeResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameTreeResponse",
  "field": [
    {
      "name": "game_point_info",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
    }
  ]
}

### Evidence

- **SRC-0935** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_tree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/160e47cb8eb4e6d05bdf6566aafd9914158e521646220d44b7b1de6985b2268a.bin)

**Source references:** SRC-0935, SRC-1822  
**URL references:** None independently associated  
**Related findings:** FND-13657, FND-13659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13659"></a>
## FND-13659: chesscom.explanation_engine.v1.GameTreeResponse.game_point_info = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameTreeResponse",
  "name": "game_point_info",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GamePointInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0935",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0935** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_game_tree.proto.bin` — [preserved redacted evidence](../evidence/descriptors/160e47cb8eb4e6d05bdf6566aafd9914158e521646220d44b7b1de6985b2268a.bin)

**Source references:** SRC-0935, SRC-1822  
**URL references:** None independently associated  
**Related findings:** FND-13657, FND-13658

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
