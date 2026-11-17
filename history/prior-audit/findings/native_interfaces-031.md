# native_interfaces — findings 3001–3100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-15660"></a>
## FND-15660: chesscom.explanation_engine.v1alpha.LogEntry.result = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.LogEntry",
  "name": "result",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.ApiResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "entry",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15661"></a>
## FND-15661: chesscom.explanation_engine.v1alpha.LogEntry.search_mock = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.LogEntry",
  "name": "search_mock",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.SearchMock",
  "label": "LABEL_OPTIONAL",
  "oneof": "entry",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15662"></a>
## FND-15662: Native message: chesscom.explanation_engine.v1alpha.HeartbeatCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "HeartbeatCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15663"></a>
## FND-15663: Native message: chesscom.explanation_engine.v1alpha.InitCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InitCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15664"></a>
## FND-15664: Native message: chesscom.explanation_engine.v1alpha.InitWithOptsCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InitWithOptsCall",
  "field": [
    {
      "name": "n_async_task_processors",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "engine_pool_size",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15665"></a>
## FND-15665: chesscom.explanation_engine.v1alpha.InitWithOptsCall.n_async_task_processors = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InitWithOptsCall",
  "name": "n_async_task_processors",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15666"></a>
## FND-15666: chesscom.explanation_engine.v1alpha.InitWithOptsCall.engine_pool_size = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.InitWithOptsCall",
  "name": "engine_pool_size",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15667"></a>
## FND-15667: Native message: chesscom.explanation_engine.v1alpha.DisposeCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15668"></a>
## FND-15668: Native message: chesscom.explanation_engine.v1alpha.EnableLogCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EnableLogCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15669"></a>
## FND-15669: Native message: chesscom.explanation_engine.v1alpha.DisableLogCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisableLogCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15670"></a>
## FND-15670: Native message: chesscom.explanation_engine.v1alpha.RunCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RunCall",
  "field": [
    {
      "name": "feature_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "async",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15671"></a>
## FND-15671: chesscom.explanation_engine.v1alpha.RunCall.feature_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.RunCall",
  "name": "feature_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15672"></a>
## FND-15672: chesscom.explanation_engine.v1alpha.RunCall.async = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.RunCall",
  "name": "async",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15673"></a>
## FND-15673: Native message: chesscom.explanation_engine.v1alpha.GetUpdateCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetUpdateCall",
  "field": [
    {
      "name": "feature_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "result_proto_ptr",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64"
    },
    {
      "name": "size",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "non_blocking",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15674"></a>
## FND-15674: chesscom.explanation_engine.v1alpha.GetUpdateCall.feature_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetUpdateCall",
  "name": "feature_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15675"></a>
## FND-15675: chesscom.explanation_engine.v1alpha.GetUpdateCall.result_proto_ptr = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetUpdateCall",
  "name": "result_proto_ptr",
  "number": 2,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15676"></a>
## FND-15676: chesscom.explanation_engine.v1alpha.GetUpdateCall.size = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetUpdateCall",
  "name": "size",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15677"></a>
## FND-15677: chesscom.explanation_engine.v1alpha.GetUpdateCall.non_blocking = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetUpdateCall",
  "name": "non_blocking",
  "number": 4,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15678"></a>
## FND-15678: Native message: chesscom.explanation_engine.v1alpha.StopCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "StopCall",
  "field": [
    {
      "name": "feature_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "non_blocking",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15679"></a>
## FND-15679: chesscom.explanation_engine.v1alpha.StopCall.feature_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.StopCall",
  "name": "feature_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15680"></a>
## FND-15680: chesscom.explanation_engine.v1alpha.StopCall.non_blocking = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.StopCall",
  "name": "non_blocking",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15681"></a>
## FND-15681: Native message: chesscom.explanation_engine.v1alpha.JoinCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "JoinCall",
  "field": [
    {
      "name": "feature_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15682"></a>
## FND-15682: chesscom.explanation_engine.v1alpha.JoinCall.feature_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.JoinCall",
  "name": "feature_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15683"></a>
## FND-15683: Native message: chesscom.explanation_engine.v1alpha.NewFeatureCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NewFeatureCall",
  "field": [
    {
      "name": "feature_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "game_point_handle",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "feature_proto",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15684"></a>
## FND-15684: chesscom.explanation_engine.v1alpha.NewFeatureCall.feature_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.NewFeatureCall",
  "name": "feature_id",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15685"></a>
## FND-15685: chesscom.explanation_engine.v1alpha.NewFeatureCall.game_point_handle = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.NewFeatureCall",
  "name": "game_point_handle",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15686"></a>
## FND-15686: chesscom.explanation_engine.v1alpha.NewFeatureCall.feature_proto = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.NewFeatureCall",
  "name": "feature_proto",
  "number": 3,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15687"></a>
## FND-15687: Native message: chesscom.explanation_engine.v1alpha.IsValidGamePointCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "IsValidGamePointCall",
  "field": [
    {
      "name": "game_point_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15688"></a>
## FND-15688: chesscom.explanation_engine.v1alpha.IsValidGamePointCall.game_point_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.IsValidGamePointCall",
  "name": "game_point_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15689"></a>
## FND-15689: Native message: chesscom.explanation_engine.v1alpha.DisposeFeatureCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeFeatureCall",
  "field": [
    {
      "name": "feature_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15690"></a>
## FND-15690: chesscom.explanation_engine.v1alpha.DisposeFeatureCall.feature_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.DisposeFeatureCall",
  "name": "feature_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15691"></a>
## FND-15691: Native message: chesscom.explanation_engine.v1alpha.DisposeGameCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeGameCall",
  "field": [
    {
      "name": "game_point_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15692"></a>
## FND-15692: chesscom.explanation_engine.v1alpha.DisposeGameCall.game_point_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.DisposeGameCall",
  "name": "game_point_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15693"></a>
## FND-15693: Native message: chesscom.explanation_engine.v1alpha.DisposeAllGamesCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeAllGamesCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15694"></a>
## FND-15694: Native message: chesscom.explanation_engine.v1alpha.GetLastErrorCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetLastErrorCall"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15695"></a>
## FND-15695: Native message: chesscom.explanation_engine.v1alpha.SetLogFDCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetLogFDCall",
  "field": [
    {
      "name": "fd",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15696"></a>
## FND-15696: chesscom.explanation_engine.v1alpha.SetLogFDCall.fd = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.SetLogFDCall",
  "name": "fd",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15697"></a>
## FND-15697: Native message: chesscom.explanation_engine.v1alpha.SetLogFileCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetLogFileCall",
  "field": [
    {
      "name": "file_path",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15698"></a>
## FND-15698: chesscom.explanation_engine.v1alpha.SetLogFileCall.file_path = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.SetLogFileCall",
  "name": "file_path",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15699"></a>
## FND-15699: Native message: chesscom.explanation_engine.v1alpha.AddArtifactCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddArtifactCall",
  "field": [
    {
      "name": "artifact_ptr",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64"
    },
    {
      "name": "size",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "key",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_key"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15700"></a>
## FND-15700: chesscom.explanation_engine.v1alpha.AddArtifactCall.artifact_ptr = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactCall",
  "name": "artifact_ptr",
  "number": 1,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15701"></a>
## FND-15701: chesscom.explanation_engine.v1alpha.AddArtifactCall.size = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactCall",
  "name": "size",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15702"></a>
## FND-15702: chesscom.explanation_engine.v1alpha.AddArtifactCall.key = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactCall",
  "name": "key",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_key",
  "proto3_optional": true,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15703"></a>
## FND-15703: Native message: chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddArtifactFromFileCall",
  "field": [
    {
      "name": "path",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "key",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_key"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15704"></a>
## FND-15704: chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall.path = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall",
  "name": "path",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15705"></a>
## FND-15705: chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall.key = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall",
  "name": "key",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_key",
  "proto3_optional": true,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15706"></a>
## FND-15706: Native message: chesscom.explanation_engine.v1alpha.DisposeArtifactCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeArtifactCall",
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

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15707"></a>
## FND-15707: chesscom.explanation_engine.v1alpha.DisposeArtifactCall.artifact_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.DisposeArtifactCall",
  "name": "artifact_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15708"></a>
## FND-15708: Native message: chesscom.explanation_engine.v1alpha.HeartbeatResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "HeartbeatResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15709"></a>
## FND-15709: Native message: chesscom.explanation_engine.v1alpha.GetUpdateResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetUpdateResult",
  "field": [
    {
      "name": "error_code",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "result_proto",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15710"></a>
## FND-15710: chesscom.explanation_engine.v1alpha.GetUpdateResult.error_code = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetUpdateResult",
  "name": "error_code",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15711"></a>
## FND-15711: chesscom.explanation_engine.v1alpha.GetUpdateResult.result_proto = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetUpdateResult",
  "name": "result_proto",
  "number": 2,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15712"></a>
## FND-15712: Native message: chesscom.explanation_engine.v1alpha.StopResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "StopResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15713"></a>
## FND-15713: Native message: chesscom.explanation_engine.v1alpha.DisposeFeatureResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeFeatureResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15714"></a>
## FND-15714: Native message: chesscom.explanation_engine.v1alpha.NewFeatureResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NewFeatureResult",
  "field": [
    {
      "name": "feature_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15715"></a>
## FND-15715: chesscom.explanation_engine.v1alpha.NewFeatureResult.feature_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.NewFeatureResult",
  "name": "feature_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15716"></a>
## FND-15716: Native message: chesscom.explanation_engine.v1alpha.IsValidGamePointResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "IsValidGamePointResult",
  "field": [
    {
      "name": "is_valid",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15717"></a>
## FND-15717: chesscom.explanation_engine.v1alpha.IsValidGamePointResult.is_valid = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.IsValidGamePointResult",
  "name": "is_valid",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15718"></a>
## FND-15718: Native message: chesscom.explanation_engine.v1alpha.DisposeGameResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeGameResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15719"></a>
## FND-15719: Native message: chesscom.explanation_engine.v1alpha.DisposeAllGamesResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeAllGamesResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15720"></a>
## FND-15720: Native message: chesscom.explanation_engine.v1alpha.JoinResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "JoinResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15721"></a>
## FND-15721: Native message: chesscom.explanation_engine.v1alpha.GetLastErrorResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetLastErrorResult",
  "field": [
    {
      "name": "error",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15722"></a>
## FND-15722: chesscom.explanation_engine.v1alpha.GetLastErrorResult.error = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.GetLastErrorResult",
  "name": "error",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15723"></a>
## FND-15723: Native message: chesscom.explanation_engine.v1alpha.RunResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RunResult",
  "field": [
    {
      "name": "error_code",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15724"></a>
## FND-15724: chesscom.explanation_engine.v1alpha.RunResult.error_code = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.RunResult",
  "name": "error_code",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15725"></a>
## FND-15725: Native message: chesscom.explanation_engine.v1alpha.EnableLogResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EnableLogResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15726"></a>
## FND-15726: Native message: chesscom.explanation_engine.v1alpha.DisableLogResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisableLogResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15727"></a>
## FND-15727: Native message: chesscom.explanation_engine.v1alpha.InitResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InitResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15728"></a>
## FND-15728: Native message: chesscom.explanation_engine.v1alpha.InitWithOptsResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InitWithOptsResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15729"></a>
## FND-15729: Native message: chesscom.explanation_engine.v1alpha.DisposeResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15730"></a>
## FND-15730: Native message: chesscom.explanation_engine.v1alpha.SetLogFDResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetLogFDResult",
  "field": [
    {
      "name": "success",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15731"></a>
## FND-15731: chesscom.explanation_engine.v1alpha.SetLogFDResult.success = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.SetLogFDResult",
  "name": "success",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15732"></a>
## FND-15732: Native message: chesscom.explanation_engine.v1alpha.SetLogFileResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetLogFileResult",
  "field": [
    {
      "name": "success",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15733"></a>
## FND-15733: chesscom.explanation_engine.v1alpha.SetLogFileResult.success = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.SetLogFileResult",
  "name": "success",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15734"></a>
## FND-15734: Native message: chesscom.explanation_engine.v1alpha.AddArtifactResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddArtifactResult",
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

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15735"></a>
## FND-15735: chesscom.explanation_engine.v1alpha.AddArtifactResult.artifact_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactResult",
  "name": "artifact_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15736"></a>
## FND-15736: Native message: chesscom.explanation_engine.v1alpha.AddArtifactFromFileResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AddArtifactFromFileResult",
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

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15737"></a>
## FND-15737: chesscom.explanation_engine.v1alpha.AddArtifactFromFileResult.artifact_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.AddArtifactFromFileResult",
  "name": "artifact_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15738"></a>
## FND-15738: Native message: chesscom.explanation_engine.v1alpha.DisposeArtifactResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DisposeArtifactResult"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15739"></a>
## FND-15739: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15740"></a>
## FND-15740: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_BASE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_BASE",
  "number": 1,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15741"></a>
## FND-15741: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_THREATENS = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_THREATENS",
  "number": 2,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15742"></a>
## FND-15742: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_PREVENTS = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_PREVENTS",
  "number": 3,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15743"></a>
## FND-15743: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_PERMITS = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_PERMITS",
  "number": 4,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15744"></a>
## FND-15744: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_MISSES = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_MISSES",
  "number": 5,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15745"></a>
## FND-15745: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_MISSES_SAME = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_MISSES_SAME",
  "number": 6,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15746"></a>
## FND-15746: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_ENDGAME = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_ENDGAME",
  "number": 7,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15747"></a>
## FND-15747: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_GAME_STATUS = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_GAME_STATUS",
  "number": 8,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15748"></a>
## FND-15748: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_LEADS_TO = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_LEADS_TO",
  "number": 9,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15749"></a>
## FND-15749: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_WINS_MATERIAL = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_WINS_MATERIAL",
  "number": 10,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15750"></a>
## FND-15750: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_GAME_OVER = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_GAME_OVER",
  "number": 11,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15751"></a>
## FND-15751: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_MATE = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_MATE",
  "number": 12,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15752"></a>
## FND-15752: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_BRILLIANT = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_BRILLIANT",
  "number": 13,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15753"></a>
## FND-15753: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_GREAT_FIND = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_GREAT_FIND",
  "number": 14,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15754"></a>
## FND-15754: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_LONG_THINK = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_LONG_THINK",
  "number": 15,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15755"></a>
## FND-15755: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_SHORT_THINK = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_SHORT_THINK",
  "number": 16,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15756"></a>
## FND-15756: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_TIME_TROUBLE = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_TIME_TROUBLE",
  "number": 17,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15757"></a>
## FND-15757: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_FORCES = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_FORCES",
  "number": 18,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15758"></a>
## FND-15758: chesscom.explanation_engine.v1alpha.Circumstance.CIRCUMSTANCE_TRICKY = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.Circumstance",
  "name": "CIRCUMSTANCE_TRICKY",
  "number": 19,
  "source_id": "SRC-1046",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1046** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_circumstance.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3e4a0b94d78c8b86750c1bf5208654929bd2bac556eab7ac558aa0a9149132ae.bin)

**Source references:** SRC-1046, SRC-1651  
**URL references:** None independently associated  
**Related findings:** FND-15739, FND-15740, FND-15741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15759"></a>
## FND-15759: chesscom.explanation_engine.v1alpha.CoachChoiceType.COACH_CHOICE_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.CoachChoiceType",
  "name": "COACH_CHOICE_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1047",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1047** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_coach_choice_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9d14cabd32cdb5a19b9918de7650c6f0157bf1f9913c488c6b8b55cecc2a6a90.bin)

**Source references:** SRC-1047, SRC-1847  
**URL references:** None independently associated  
**Related findings:** FND-15760, FND-15761

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
