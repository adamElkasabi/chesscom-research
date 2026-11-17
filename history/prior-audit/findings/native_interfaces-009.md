# native_interfaces — findings 801–900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13460"></a>
## FND-13460: chesscom.explanation_engine.v1.CharmInferenceResult.elo = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "elo",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13461"></a>
## FND-13461: chesscom.explanation_engine.v1.CharmInferenceResult.moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "moves",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.MovePrediction",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13462"></a>
## FND-13462: chesscom.explanation_engine.v1.CharmInferenceResult.expected_points = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "expected_points",
  "number": 4,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13463"></a>
## FND-13463: chesscom.explanation_engine.v1.CharmInferenceResult.rank_probabilities = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "rank_probabilities",
  "number": 5,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13464"></a>
## FND-13464: chesscom.explanation_engine.v1.CharmInferenceResult.strength_probabilities = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "strength_probabilities",
  "number": 6,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13465"></a>
## FND-13465: chesscom.explanation_engine.v1.CharmInferenceResult.time_taken_probabilities = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "time_taken_probabilities",
  "number": 7,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13466"></a>
## FND-13466: chesscom.explanation_engine.v1.CharmInferenceResult.ldw_probabilities = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "ldw_probabilities",
  "number": 8,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13467"></a>
## FND-13467: chesscom.explanation_engine.v1.CharmInferenceResult.strength_rating_sensitive_probabilities = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "strength_rating_sensitive_probabilities",
  "number": 9,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13468"></a>
## FND-13468: chesscom.explanation_engine.v1.CharmInferenceResult.engine_line_uci_moves = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "engine_line_uci_moves",
  "number": 10,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13469"></a>
## FND-13469: chesscom.explanation_engine.v1.CharmInferenceResult.engine = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "engine",
  "number": 11,
  "type": ".chesscom.engine.v1.Engine",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine",
  "proto3_optional": true,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13470"></a>
## FND-13470: Native message: chesscom.explanation_engine.v1.CharmInferenceCode

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmInferenceCode",
  "field": [
    {
      "name": "model_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "ratings",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    },
    {
      "name": "engine_line_move_indexes",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "coded_values",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    }
  ]
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13471"></a>
## FND-13471: chesscom.explanation_engine.v1.CharmInferenceCode.model_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCode",
  "name": "model_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13472"></a>
## FND-13472: chesscom.explanation_engine.v1.CharmInferenceCode.ratings = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCode",
  "name": "ratings",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13473"></a>
## FND-13473: chesscom.explanation_engine.v1.CharmInferenceCode.engine_line_move_indexes = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCode",
  "name": "engine_line_move_indexes",
  "number": 3,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13474"></a>
## FND-13474: chesscom.explanation_engine.v1.CharmInferenceCode.coded_values = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCode",
  "name": "coded_values",
  "number": 4,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13475"></a>
## FND-13475: Native message: chesscom.explanation_engine.v1.NodeCharmInferenceCodes

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NodeCharmInferenceCodes",
  "field": [
    {
      "name": "inferences",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CharmInferenceCode"
    }
  ]
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13476"></a>
## FND-13476: chesscom.explanation_engine.v1.NodeCharmInferenceCodes.inferences = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NodeCharmInferenceCodes",
  "name": "inferences",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CharmInferenceCode",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13477"></a>
## FND-13477: Native message: chesscom.explanation_engine.v1.CharmInferenceCodes

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmInferenceCodes",
  "field": [
    {
      "name": "codebook_version",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "nodes",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry"
    }
  ],
  "nested_type": [
    {
      "name": "NodesEntry",
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
          "type_name": ".chesscom.explanation_engine.v1.NodeCharmInferenceCodes"
        }
      ],
      "options": {
        "map_entry": true
      }
    }
  ]
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13478"></a>
## FND-13478: chesscom.explanation_engine.v1.CharmInferenceCodes.codebook_version = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCodes",
  "name": "codebook_version",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13479"></a>
## FND-13479: chesscom.explanation_engine.v1.CharmInferenceCodes.nodes = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCodes",
  "name": "nodes",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13480"></a>
## FND-13480: Native message: chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NodesEntry",
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
      "type_name": ".chesscom.explanation_engine.v1.NodeCharmInferenceCodes"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13481"></a>
## FND-13481: chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13482"></a>
## FND-13482: chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry",
  "name": "value",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.NodeCharmInferenceCodes",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0908",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0908** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference_code.proto.bin` — [preserved redacted evidence](../evidence/descriptors/27adf12affac3c40f21e3e0fa78e870209ba766081a11b4029b0eb4c9cb44981.bin)

**Source references:** SRC-0908, SRC-1892  
**URL references:** None independently associated  
**Related findings:** FND-13470, FND-13471, FND-13472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13483"></a>
## FND-13483: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13484"></a>
## FND-13484: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_BASE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_BASE",
  "number": 1,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13485"></a>
## FND-13485: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_THREATENS = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_THREATENS",
  "number": 2,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13486"></a>
## FND-13486: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_PREVENTS = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_PREVENTS",
  "number": 3,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13487"></a>
## FND-13487: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_PERMITS = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_PERMITS",
  "number": 4,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13488"></a>
## FND-13488: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_MISSES = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_MISSES",
  "number": 5,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13489"></a>
## FND-13489: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_MISSES_SAME = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_MISSES_SAME",
  "number": 6,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13490"></a>
## FND-13490: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_ENDGAME = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_ENDGAME",
  "number": 7,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13491"></a>
## FND-13491: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_GAME_STATUS = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_GAME_STATUS",
  "number": 8,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13492"></a>
## FND-13492: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_LEADS_TO = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_LEADS_TO",
  "number": 9,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13493"></a>
## FND-13493: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_WINS_MATERIAL = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_WINS_MATERIAL",
  "number": 10,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13494"></a>
## FND-13494: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_GAME_OVER = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_GAME_OVER",
  "number": 11,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13495"></a>
## FND-13495: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_MATE = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_MATE",
  "number": 12,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13496"></a>
## FND-13496: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_BRILLIANT = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_BRILLIANT",
  "number": 13,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13497"></a>
## FND-13497: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_GREAT_FIND = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_GREAT_FIND",
  "number": 14,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13498"></a>
## FND-13498: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_LONG_THINK = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_LONG_THINK",
  "number": 15,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13499"></a>
## FND-13499: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_SHORT_THINK = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_SHORT_THINK",
  "number": 16,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13500"></a>
## FND-13500: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_TIME_TROUBLE = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_TIME_TROUBLE",
  "number": 17,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13501"></a>
## FND-13501: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_FORCES = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Circumstance",
  "name": "CIRCUMSTANCE_FORCES",
  "number": 18,
  "source_id": "SRC-0909",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0909** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1b6ad77c543a27ed99b4986b490064b20059bfba56a96023810f80240fb82bb2.bin)

**Source references:** SRC-0909, SRC-1734  
**URL references:** None independently associated  
**Related findings:** FND-13483, FND-13484, FND-13485

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13502"></a>
## FND-13502: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13503"></a>
## FND-13503: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_IDLE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_IDLE",
  "number": 1,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13504"></a>
## FND-13504: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_SURPRISED = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_SURPRISED",
  "number": 2,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13505"></a>
## FND-13505: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_HAPPY = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_HAPPY",
  "number": 3,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13506"></a>
## FND-13506: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_IMPRESSED = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_IMPRESSED",
  "number": 4,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13507"></a>
## FND-13507: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_SHOCKED = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_SHOCKED",
  "number": 5,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13508"></a>
## FND-13508: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_THINKING = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_THINKING",
  "number": 6,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13509"></a>
## FND-13509: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_CONCERNED = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_CONCERNED",
  "number": 7,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13510"></a>
## FND-13510: chesscom.explanation_engine.v1.CoachEmotion.COACH_EMOTION_SAD = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CoachEmotion",
  "name": "COACH_EMOTION_SAD",
  "number": 8,
  "source_id": "SRC-0910",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0910** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_emotion.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d7b3a7f0d3df518f796439919782934a1eea0eaceaf4a1671a15417eddf0ead8.bin)

**Source references:** SRC-0910, SRC-1790  
**URL references:** None independently associated  
**Related findings:** FND-13502, FND-13503, FND-13504

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13511"></a>
## FND-13511: Native message: chesscom.explanation_engine.v1.CoachState

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CoachState",
  "field": [
    {
      "name": "ply_since_retry_offered",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "ply_since_flip_board_offered",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_ply_since_retry_offered"
    },
    {
      "name": "_ply_since_flip_board_offered"
    }
  ]
}

### Evidence

- **SRC-0911** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/368ad3293881ed73a94bcbbec2cbd487877f578138e3d0387f3d4ec56ac002ad.bin)

**Source references:** SRC-0911, SRC-1843  
**URL references:** None independently associated  
**Related findings:** FND-13512, FND-13513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13512"></a>
## FND-13512: chesscom.explanation_engine.v1.CoachState.ply_since_retry_offered = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachState",
  "name": "ply_since_retry_offered",
  "number": 1,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_ply_since_retry_offered",
  "proto3_optional": true,
  "source_id": "SRC-0911",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0911** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/368ad3293881ed73a94bcbbec2cbd487877f578138e3d0387f3d4ec56ac002ad.bin)

**Source references:** SRC-0911, SRC-1843  
**URL references:** None independently associated  
**Related findings:** FND-13511, FND-13513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13513"></a>
## FND-13513: chesscom.explanation_engine.v1.CoachState.ply_since_flip_board_offered = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachState",
  "name": "ply_since_flip_board_offered",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_ply_since_flip_board_offered",
  "proto3_optional": true,
  "source_id": "SRC-0911",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0911** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_coach_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/368ad3293881ed73a94bcbbec2cbd487877f578138e3d0387f3d4ec56ac002ad.bin)

**Source references:** SRC-0911, SRC-1843  
**URL references:** None independently associated  
**Related findings:** FND-13511, FND-13512

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13514"></a>
## FND-13514: Native message: chesscom.explanation_engine.v1.CommandType

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CommandType",
  "field": [
    {
      "name": "feature_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.FeatureId",
      "oneof_index": 0
    },
    {
      "name": "cee_command",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "command_type"
    }
  ]
}

### Evidence

- **SRC-0912** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_command_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/863ef611da5204d9f06810b3fbaca4158ea12c0592b4592bec80b2f1646c0726.bin)

**Source references:** SRC-0912, SRC-1802  
**URL references:** None independently associated  
**Related findings:** FND-13515, FND-13516

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13515"></a>
## FND-13515: chesscom.explanation_engine.v1.CommandType.feature_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CommandType",
  "name": "feature_id",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.FeatureId",
  "label": "LABEL_OPTIONAL",
  "oneof": "command_type",
  "proto3_optional": false,
  "source_id": "SRC-0912",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0912** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_command_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/863ef611da5204d9f06810b3fbaca4158ea12c0592b4592bec80b2f1646c0726.bin)

**Source references:** SRC-0912, SRC-1802  
**URL references:** None independently associated  
**Related findings:** FND-13514, FND-13516

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13516"></a>
## FND-13516: chesscom.explanation_engine.v1.CommandType.cee_command = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CommandType",
  "name": "cee_command",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "command_type",
  "proto3_optional": false,
  "source_id": "SRC-0912",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0912** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_command_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/863ef611da5204d9f06810b3fbaca4158ea12c0592b4592bec80b2f1646c0726.bin)

**Source references:** SRC-0912, SRC-1802  
**URL references:** None independently associated  
**Related findings:** FND-13514, FND-13515

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13517"></a>
## FND-13517: Native message: chesscom.explanation_engine.v1.CompactCharmInference

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CompactCharmInference",
  "field": [
    {
      "name": "model_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "ratings",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    },
    {
      "name": "uci_moves",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "move_probabilities",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "expected_points",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "rank_probabilities",
      "number": 6,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "strength_probabilities",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "time_taken_probabilities",
      "number": 8,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "ldw_probabilities",
      "number": 9,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "strength_rating_sensitive_probabilities",
      "number": 10,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "engine_line_move_indexes",
      "number": 11,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    },
    {
      "name": "move_indexes",
      "number": 12,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    }
  ]
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13518"></a>
## FND-13518: chesscom.explanation_engine.v1.CompactCharmInference.model_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "model_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13519"></a>
## FND-13519: chesscom.explanation_engine.v1.CompactCharmInference.ratings = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "ratings",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13520"></a>
## FND-13520: chesscom.explanation_engine.v1.CompactCharmInference.uci_moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "uci_moves",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13521"></a>
## FND-13521: chesscom.explanation_engine.v1.CompactCharmInference.move_probabilities = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "move_probabilities",
  "number": 4,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13522"></a>
## FND-13522: chesscom.explanation_engine.v1.CompactCharmInference.expected_points = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "expected_points",
  "number": 5,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13523"></a>
## FND-13523: chesscom.explanation_engine.v1.CompactCharmInference.rank_probabilities = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "rank_probabilities",
  "number": 6,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13524"></a>
## FND-13524: chesscom.explanation_engine.v1.CompactCharmInference.strength_probabilities = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "strength_probabilities",
  "number": 7,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13525"></a>
## FND-13525: chesscom.explanation_engine.v1.CompactCharmInference.time_taken_probabilities = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "time_taken_probabilities",
  "number": 8,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13526"></a>
## FND-13526: chesscom.explanation_engine.v1.CompactCharmInference.ldw_probabilities = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "ldw_probabilities",
  "number": 9,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13527"></a>
## FND-13527: chesscom.explanation_engine.v1.CompactCharmInference.strength_rating_sensitive_probabilities = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "strength_rating_sensitive_probabilities",
  "number": 10,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13528"></a>
## FND-13528: chesscom.explanation_engine.v1.CompactCharmInference.engine_line_move_indexes = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "engine_line_move_indexes",
  "number": 11,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13529"></a>
## FND-13529: chesscom.explanation_engine.v1.CompactCharmInference.move_indexes = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInference",
  "name": "move_indexes",
  "number": 12,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13530"></a>
## FND-13530: Native message: chesscom.explanation_engine.v1.CompactCharmInferences

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CompactCharmInferences",
  "field": [
    {
      "name": "inferences",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CompactCharmInference"
    },
    {
      "name": "quantization_bits",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13531"></a>
## FND-13531: chesscom.explanation_engine.v1.CompactCharmInferences.inferences = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInferences",
  "name": "inferences",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CompactCharmInference",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13532"></a>
## FND-13532: chesscom.explanation_engine.v1.CompactCharmInferences.quantization_bits = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CompactCharmInferences",
  "name": "quantization_bits",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0913",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0913** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_compact_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a1865b8c9c5f836f272b0aee04176af2c721d1ba09d3583f175ae263f4801026.bin)

**Source references:** SRC-0913, SRC-1732  
**URL references:** None independently associated  
**Related findings:** FND-13517, FND-13518, FND-13519

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13533"></a>
## FND-13533: Native message: chesscom.explanation_engine.v1.DisposeGamePointRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeGamePointRequest"
}

### Evidence

- **SRC-0914** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_dispose_game_point.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e45b8564ab31f0dc662b46bba0a426a25d40615293044af6ba2e8ea5f1877668.bin)

**Source references:** SRC-0914, SRC-1867  
**URL references:** None independently associated  
**Related findings:** FND-13534

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13534"></a>
## FND-13534: Native message: chesscom.explanation_engine.v1.DisposeGamePointResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeGamePointResponse"
}

### Evidence

- **SRC-0914** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_dispose_game_point.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e45b8564ab31f0dc662b46bba0a426a25d40615293044af6ba2e8ea5f1877668.bin)

**Source references:** SRC-0914, SRC-1867  
**URL references:** None independently associated  
**Related findings:** FND-13533

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13535"></a>
## FND-13535: Native message: chesscom.explanation_engine.v1.AddCharmInferenceRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddCharmInferenceRequest",
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

- **SRC-0915** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e86402b3b4a23314e09615485aba1ab16e43c882bea5eedaba299572404751e.bin)

**Source references:** SRC-0915, SRC-1756  
**URL references:** None independently associated  
**Related findings:** FND-13536, FND-13537

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13536"></a>
## FND-13536: chesscom.explanation_engine.v1.AddCharmInferenceRequest.results = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AddCharmInferenceRequest",
  "name": "results",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CharmInferenceResult",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0915",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0915** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e86402b3b4a23314e09615485aba1ab16e43c882bea5eedaba299572404751e.bin)

**Source references:** SRC-0915, SRC-1756  
**URL references:** None independently associated  
**Related findings:** FND-13535, FND-13537

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13537"></a>
## FND-13537: Native message: chesscom.explanation_engine.v1.AddCharmInferenceResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddCharmInferenceResponse"
}

### Evidence

- **SRC-0915** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e86402b3b4a23314e09615485aba1ab16e43c882bea5eedaba299572404751e.bin)

**Source references:** SRC-0915, SRC-1756  
**URL references:** None independently associated  
**Related findings:** FND-13535, FND-13536

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13538"></a>
## FND-13538: Native message: chesscom.explanation_engine.v1.AddEvaluationsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddEvaluationsRequest",
  "field": [
    {
      "name": "evaluations",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Evaluation"
    },
    {
      "name": "skip_eval_normalization",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-0916** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3bce78fe7fe1f0ee615c138098978ecb1f8a757dfe8b3934225e00190414a7cb.bin)

**Source references:** SRC-0916, SRC-1891  
**URL references:** None independently associated  
**Related findings:** FND-13539, FND-13540

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13539"></a>
## FND-13539: chesscom.explanation_engine.v1.AddEvaluationsRequest.evaluations = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AddEvaluationsRequest",
  "name": "evaluations",
  "number": 1,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0916",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0916** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3bce78fe7fe1f0ee615c138098978ecb1f8a757dfe8b3934225e00190414a7cb.bin)

**Source references:** SRC-0916, SRC-1891  
**URL references:** None independently associated  
**Related findings:** FND-13538, FND-13540

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13540"></a>
## FND-13540: chesscom.explanation_engine.v1.AddEvaluationsRequest.skip_eval_normalization = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AddEvaluationsRequest",
  "name": "skip_eval_normalization",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0916",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0916** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3bce78fe7fe1f0ee615c138098978ecb1f8a757dfe8b3934225e00190414a7cb.bin)

**Source references:** SRC-0916, SRC-1891  
**URL references:** None independently associated  
**Related findings:** FND-13538, FND-13539

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13541"></a>
## FND-13541: Native message: chesscom.explanation_engine.v1.AddEvaluationsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddEvaluationsResponse",
  "field": [
    {
      "name": "added_variation_start_game_points",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0916** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3bce78fe7fe1f0ee615c138098978ecb1f8a757dfe8b3934225e00190414a7cb.bin)

**Source references:** SRC-0916, SRC-1891  
**URL references:** None independently associated  
**Related findings:** FND-13538, FND-13539, FND-13540

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13542"></a>
## FND-13542: chesscom.explanation_engine.v1.AddEvaluationsResponse.added_variation_start_game_points = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AddEvaluationsResponse",
  "name": "added_variation_start_game_points",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0916",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0916** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_add_evaluations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3bce78fe7fe1f0ee615c138098978ecb1f8a757dfe8b3934225e00190414a7cb.bin)

**Source references:** SRC-0916, SRC-1891  
**URL references:** None independently associated  
**Related findings:** FND-13538, FND-13539, FND-13540

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13543"></a>
## FND-13543: Native message: chesscom.explanation_engine.v1.AnalysisAnnotationsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AnalysisAnnotationsRequest",
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

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13544, FND-13545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13544"></a>
## FND-13544: chesscom.explanation_engine.v1.AnalysisAnnotationsRequest.stream_results = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnalysisAnnotationsRequest",
  "name": "stream_results",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0917",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13543, FND-13545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13545"></a>
## FND-13545: chesscom.explanation_engine.v1.AnalysisAnnotationsRequest.enable_pv_classifications = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnalysisAnnotationsRequest",
  "name": "enable_pv_classifications",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0917",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13543, FND-13544

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13546"></a>
## FND-13546: Native message: chesscom.explanation_engine.v1.AnalysisAnnotationsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AnalysisAnnotationsResponse",
  "field": [
    {
      "name": "move_classifications",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassificationResponse"
    },
    {
      "name": "threats",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SimpleThreatsResponse"
    },
    {
      "name": "progress",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    }
  ]
}

### Evidence

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13543, FND-13544, FND-13545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13547"></a>
## FND-13547: chesscom.explanation_engine.v1.AnalysisAnnotationsResponse.move_classifications = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnalysisAnnotationsResponse",
  "name": "move_classifications",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveClassificationResponse",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0917",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13543, FND-13544, FND-13545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13548"></a>
## FND-13548: chesscom.explanation_engine.v1.AnalysisAnnotationsResponse.threats = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnalysisAnnotationsResponse",
  "name": "threats",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.SimpleThreatsResponse",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0917",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13543, FND-13544, FND-13545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13549"></a>
## FND-13549: chesscom.explanation_engine.v1.AnalysisAnnotationsResponse.progress = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnalysisAnnotationsResponse",
  "name": "progress",
  "number": 3,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0917",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0917** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_analysis_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d2deee289927063b0e6df4a27e9ac817035efb1c473b1a0710f9f6a9a7adb3df.bin)

**Source references:** SRC-0917, SRC-1804  
**URL references:** None independently associated  
**Related findings:** FND-13543, FND-13544, FND-13545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13550"></a>
## FND-13550: Native message: chesscom.explanation_engine.v1.BotConfigResourcesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BotConfigResourcesRequest",
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

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13551"></a>
## FND-13551: chesscom.explanation_engine.v1.BotConfigResourcesRequest.bot_config = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotConfigResourcesRequest",
  "name": "bot_config",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13552"></a>
## FND-13552: chesscom.explanation_engine.v1.BotConfigResourcesRequest.artifact_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotConfigResourcesRequest",
  "name": "artifact_id",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13553"></a>
## FND-13553: chesscom.explanation_engine.v1.BotConfigResourcesRequest.proto_config = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotConfigResourcesRequest",
  "name": "proto_config",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.BotMoveConfiguration",
  "label": "LABEL_OPTIONAL",
  "oneof": "_proto_config",
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

<a id="FND-13554"></a>
## FND-13554: Native message: chesscom.explanation_engine.v1.BookResource

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BookResource",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "move_count",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13555"></a>
## FND-13555: chesscom.explanation_engine.v1.BookResource.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BookResource",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13556"></a>
## FND-13556: chesscom.explanation_engine.v1.BookResource.move_count = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BookResource",
  "name": "move_count",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13557"></a>
## FND-13557: Native message: chesscom.explanation_engine.v1.NnResource

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NnResource",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13558"></a>
## FND-13558: chesscom.explanation_engine.v1.NnResource.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnResource",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0918",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13559"></a>
## FND-13559: Native message: chesscom.explanation_engine.v1.BotConfigResourcesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BotConfigResourcesResponse",
  "field": [
    {
      "name": "book",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.BookResource",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "nn",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.NnResource",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_book"
    },
    {
      "name": "_nn"
    }
  ]
}

### Evidence

- **SRC-0918** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_bot_config_resources.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ba0275a8867cf91267168c44919a5578b598f2fe087fb37e6333aa93140c3679.bin)

**Source references:** SRC-0918, SRC-1905  
**URL references:** None independently associated  
**Related findings:** FND-13550, FND-13551, FND-13552

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
