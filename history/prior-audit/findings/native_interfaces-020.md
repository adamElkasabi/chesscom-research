# native_interfaces — findings 1901–2000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14560"></a>
## FND-14560: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse.white_stat_examples = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse",
  "name": "white_stat_examples",
  "number": 4,
  "type": ".chesscom.stats.v1.AdvancedStatExample",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14561"></a>
## FND-14561: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse.black_stat_examples = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse",
  "name": "black_stat_examples",
  "number": 5,
  "type": ".chesscom.stats.v1.AdvancedStatExample",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14562"></a>
## FND-14562: chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse.cee_version = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureAdvancedStatsDatapointResponse",
  "name": "cee_version",
  "number": 6,
  "type": ".chesscom.api.v1.SemanticVersion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_cee_version",
  "proto3_optional": true,
  "source_id": "SRC-1002",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1002** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_advanced_stats_datapoint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c0414f739f4e3b8c1d57ab17fa9e85e4cbb463aec16b83a39be6df23c7a1130e.bin)

**Source references:** SRC-1002, SRC-1671  
**URL references:** None independently associated  
**Related findings:** FND-14553, FND-14554, FND-14555

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14563"></a>
## FND-14563: Native message: chesscom.explanation_engine.v1.InternalFeatureCompressDataRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureCompressDataRequest",
  "field": [
    {
      "name": "uncompressed_data",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    },
    {
      "name": "encrypt",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-1003** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_compress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1c8f568c319b2ac9267d3793dcdf070a09f48c6ab6c907e7060334fc3d890016.bin)

**Source references:** SRC-1003, SRC-1657  
**URL references:** None independently associated  
**Related findings:** FND-14564, FND-14565

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14564"></a>
## FND-14564: chesscom.explanation_engine.v1.InternalFeatureCompressDataRequest.uncompressed_data = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureCompressDataRequest",
  "name": "uncompressed_data",
  "number": 1,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1003",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1003** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_compress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1c8f568c319b2ac9267d3793dcdf070a09f48c6ab6c907e7060334fc3d890016.bin)

**Source references:** SRC-1003, SRC-1657  
**URL references:** None independently associated  
**Related findings:** FND-14563, FND-14565

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14565"></a>
## FND-14565: chesscom.explanation_engine.v1.InternalFeatureCompressDataRequest.encrypt = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureCompressDataRequest",
  "name": "encrypt",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1003",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1003** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_compress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1c8f568c319b2ac9267d3793dcdf070a09f48c6ab6c907e7060334fc3d890016.bin)

**Source references:** SRC-1003, SRC-1657  
**URL references:** None independently associated  
**Related findings:** FND-14563, FND-14564

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14566"></a>
## FND-14566: Native message: chesscom.explanation_engine.v1.InternalFeatureCompressDataResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureCompressDataResponse",
  "field": [
    {
      "name": "compressed_data",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    }
  ]
}

### Evidence

- **SRC-1003** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_compress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1c8f568c319b2ac9267d3793dcdf070a09f48c6ab6c907e7060334fc3d890016.bin)

**Source references:** SRC-1003, SRC-1657  
**URL references:** None independently associated  
**Related findings:** FND-14563, FND-14564, FND-14565

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14567"></a>
## FND-14567: chesscom.explanation_engine.v1.InternalFeatureCompressDataResponse.compressed_data = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureCompressDataResponse",
  "name": "compressed_data",
  "number": 1,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1003",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1003** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_compress_data.proto.bin` — [preserved redacted evidence](../evidence/descriptors/1c8f568c319b2ac9267d3793dcdf070a09f48c6ab6c907e7060334fc3d890016.bin)

**Source references:** SRC-1003, SRC-1657  
**URL references:** None independently associated  
**Related findings:** FND-14563, FND-14564, FND-14565

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14568"></a>
## FND-14568: Native message: chesscom.explanation_engine.v1.InternalFeatureDebugInfoRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureDebugInfoRequest"
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14569, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14569"></a>
## FND-14569: Native message: chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureDebugInfoResponse",
  "field": [
    {
      "name": "active_feature_tasks",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "allocated_features",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "game_debug_info",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameDebugInfo"
    }
  ]
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14570"></a>
## FND-14570: chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse.active_feature_tasks = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse",
  "name": "active_feature_tasks",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1004",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14569

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14571"></a>
## FND-14571: chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse.allocated_features = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse",
  "name": "allocated_features",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1004",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14569, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14572"></a>
## FND-14572: chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse.game_debug_info = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureDebugInfoResponse",
  "name": "game_debug_info",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GameDebugInfo",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1004",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14569, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14573"></a>
## FND-14573: Native message: chesscom.explanation_engine.v1.GameDebugInfo

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameDebugInfo",
  "field": [
    {
      "name": "game_handle",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "tree_nodes",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14569, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14574"></a>
## FND-14574: chesscom.explanation_engine.v1.GameDebugInfo.game_handle = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameDebugInfo",
  "name": "game_handle",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1004",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14569, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14575"></a>
## FND-14575: chesscom.explanation_engine.v1.GameDebugInfo.tree_nodes = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameDebugInfo",
  "name": "tree_nodes",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1004",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1004** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_debug_info.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e4d2286f2c5913aa5090d609faadc543d8bb96257073c1667956470d4cb79d3.bin)

**Source references:** SRC-1004, SRC-1683  
**URL references:** None independently associated  
**Related findings:** FND-14568, FND-14569, FND-14570

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14576"></a>
## FND-14576: Native message: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureEnableGameMocksRequest",
  "field": [
    {
      "name": "mode",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode"
    },
    {
      "name": "mock_dir",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ],
  "enum_type": [
    {
      "name": "Mode",
      "value": [
        {
          "name": "MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MODE_DISABLED",
          "number": 1
        },
        {
          "name": "MODE_LOOKUP_ONLY",
          "number": 2
        },
        {
          "name": "MODE_GENERATE",
          "number": 3
        }
      ]
    }
  ]
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14577, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14577"></a>
## FND-14577: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.mode = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest",
  "name": "mode",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1005",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14578"></a>
## FND-14578: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.mock_dir = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest",
  "name": "mock_dir",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1005",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14579"></a>
## FND-14579: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode.MODE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode",
  "name": "MODE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1005",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14577, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14580"></a>
## FND-14580: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode.MODE_DISABLED = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode",
  "name": "MODE_DISABLED",
  "number": 1,
  "source_id": "SRC-1005",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14577, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14581"></a>
## FND-14581: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode.MODE_LOOKUP_ONLY = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode",
  "name": "MODE_LOOKUP_ONLY",
  "number": 2,
  "source_id": "SRC-1005",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14577, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14582"></a>
## FND-14582: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode.MODE_GENERATE = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksRequest.Mode",
  "name": "MODE_GENERATE",
  "number": 3,
  "source_id": "SRC-1005",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14577, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14583"></a>
## FND-14583: Native message: chesscom.explanation_engine.v1.InternalFeatureEnableGameMocksResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureEnableGameMocksResponse"
}

### Evidence

- **SRC-1005** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_game_mocks.proto.bin` — [preserved redacted evidence](../evidence/descriptors/05c05e39889492cdeba78ab47c2bb2078bca5eb483d6f33351f04d273844bcd8.bin)

**Source references:** SRC-1005, SRC-1819  
**URL references:** None independently associated  
**Related findings:** FND-14576, FND-14577, FND-14578

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14584"></a>
## FND-14584: Native message: chesscom.explanation_engine.v1.InternalFeatureEnableTestModeRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureEnableTestModeRequest"
}

### Evidence

- **SRC-1006** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_test_mode.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2f5144185cfda07503662f8f91f49c534147f0821d703bccb9ed55df0012e172.bin)

**Source references:** SRC-1006, SRC-1686  
**URL references:** None independently associated  
**Related findings:** FND-14585

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14585"></a>
## FND-14585: Native message: chesscom.explanation_engine.v1.InternalFeatureEnableTestModeResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureEnableTestModeResponse"
}

### Evidence

- **SRC-1006** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_enable_test_mode.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2f5144185cfda07503662f8f91f49c534147f0821d703bccb9ed55df0012e172.bin)

**Source references:** SRC-1006, SRC-1686  
**URL references:** None independently associated  
**Related findings:** FND-14584

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14586"></a>
## FND-14586: Native message: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGameAnalysisJsonRequest",
  "field": [
    {
      "name": "uci_options",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry"
    },
    {
      "name": "stats",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.AdvancedStatsForGame",
      "oneof_index": 0,
      "proto3_optional": true
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
    }
  ]
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14587, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14587"></a>
## FND-14587: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.uci_options = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest",
  "name": "uci_options",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1007",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14588"></a>
## FND-14588: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.stats = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest",
  "name": "stats",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.AdvancedStatsForGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "_stats",
  "proto3_optional": true,
  "source_id": "SRC-1007",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14587

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14589"></a>
## FND-14589: Native message: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry

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

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14587, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14590"></a>
## FND-14590: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1007",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14587, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14591"></a>
## FND-14591: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonRequest.UciOptionsEntry",
  "name": "value",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1007",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14587, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14592"></a>
## FND-14592: Native message: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGameAnalysisJsonResponse",
  "field": [
    {
      "name": "game_analysis_json",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14587, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14593"></a>
## FND-14593: chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonResponse.game_analysis_json = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureGameAnalysisJsonResponse",
  "name": "game_analysis_json",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1007",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1007** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_game_analysis_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38d22918f5c2942946f2db59bbf68f63494e02165a22efcbdb37c669991f66f6.bin)

**Source references:** SRC-1007, SRC-1904  
**URL references:** None independently associated  
**Related findings:** FND-14586, FND-14587, FND-14588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14594"></a>
## FND-14594: Native message: chesscom.explanation_engine.v1.InternalFeatureGetMoveAnnotationsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetMoveAnnotationsRequest"
}

### Evidence

- **SRC-1008** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_get_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fdb45176e9df7b7ce7b195192cf361668eaf2642bfd11e706317631d89d15f82.bin)

**Source references:** SRC-1008, SRC-1806  
**URL references:** None independently associated  
**Related findings:** FND-14595, FND-14596

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14595"></a>
## FND-14595: Native message: chesscom.explanation_engine.v1.InternalFeatureGetMoveAnnotationsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGetMoveAnnotationsResponse",
  "field": [
    {
      "name": "annotation",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveAnnotation"
    }
  ]
}

### Evidence

- **SRC-1008** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_get_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fdb45176e9df7b7ce7b195192cf361668eaf2642bfd11e706317631d89d15f82.bin)

**Source references:** SRC-1008, SRC-1806  
**URL references:** None independently associated  
**Related findings:** FND-14594, FND-14596

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14596"></a>
## FND-14596: chesscom.explanation_engine.v1.InternalFeatureGetMoveAnnotationsResponse.annotation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureGetMoveAnnotationsResponse",
  "name": "annotation",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveAnnotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1008",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1008** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_get_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/fdb45176e9df7b7ce7b195192cf361668eaf2642bfd11e706317631d89d15f82.bin)

**Source references:** SRC-1008, SRC-1806  
**URL references:** None independently associated  
**Related findings:** FND-14594, FND-14595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14597"></a>
## FND-14597: Native message: chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureKeyPositionSearchRequest",
  "field": [
    {
      "name": "engine",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Engine"
    },
    {
      "name": "run_search_req",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RunSearchRequest"
    }
  ]
}

### Evidence

- **SRC-1009** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_key_position_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f488532c1b8d2a7351aee1afb6327fef7b85860139be12871a268797890bdfd2.bin)

**Source references:** SRC-1009, SRC-1654  
**URL references:** None independently associated  
**Related findings:** FND-14598, FND-14599

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14598"></a>
## FND-14598: chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchRequest.engine = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchRequest",
  "name": "engine",
  "number": 1,
  "type": ".chesscom.engine.v1.Engine",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1009",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1009** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_key_position_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f488532c1b8d2a7351aee1afb6327fef7b85860139be12871a268797890bdfd2.bin)

**Source references:** SRC-1009, SRC-1654  
**URL references:** None independently associated  
**Related findings:** FND-14597, FND-14599

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14599"></a>
## FND-14599: chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchRequest.run_search_req = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchRequest",
  "name": "run_search_req",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.RunSearchRequest",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1009",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1009** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_key_position_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f488532c1b8d2a7351aee1afb6327fef7b85860139be12871a268797890bdfd2.bin)

**Source references:** SRC-1009, SRC-1654  
**URL references:** None independently associated  
**Related findings:** FND-14597, FND-14598

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14600"></a>
## FND-14600: Native message: chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureKeyPositionSearchResponse",
  "field": [
    {
      "name": "search_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1009** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_key_position_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f488532c1b8d2a7351aee1afb6327fef7b85860139be12871a268797890bdfd2.bin)

**Source references:** SRC-1009, SRC-1654  
**URL references:** None independently associated  
**Related findings:** FND-14597, FND-14598, FND-14599

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14601"></a>
## FND-14601: chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchResponse.search_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureKeyPositionSearchResponse",
  "name": "search_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1009",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1009** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_key_position_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f488532c1b8d2a7351aee1afb6327fef7b85860139be12871a268797890bdfd2.bin)

**Source references:** SRC-1009, SRC-1654  
**URL references:** None independently associated  
**Related findings:** FND-14597, FND-14598, FND-14599

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14602"></a>
## FND-14602: Native message: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest

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

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14603, FND-14604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14603"></a>
## FND-14603: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest.elo_self = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest",
  "name": "elo_self",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1010",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14602, FND-14604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14604"></a>
## FND-14604: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest.elo_oppo = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest",
  "name": "elo_oppo",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1010",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14602, FND-14603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14605"></a>
## FND-14605: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest.json = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest",
  "name": "json",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1010",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14602, FND-14603, FND-14604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14606"></a>
## FND-14606: Native message: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse

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

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14602, FND-14603, FND-14604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14607"></a>
## FND-14607: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1010",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14602, FND-14603, FND-14604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14608"></a>
## FND-14608: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse.json = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse",
  "name": "json",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1010",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1010** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_maia_botmove.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a20cde4d6f01218b612e9ba57e56a06b00631048df4104fe367a3b5312ba441b.bin)

**Source references:** SRC-1010, SRC-1699  
**URL references:** None independently associated  
**Related findings:** FND-14602, FND-14603, FND-14604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14609"></a>
## FND-14609: Native message: chesscom.explanation_engine.v1.PuzzleGenFailureReason

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleGenFailureReason",
  "field": [
    {
      "name": "failure_phase",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGenPhase"
    },
    {
      "name": "failure_type",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGenFailureType"
    },
    {
      "name": "failure_message",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14610"></a>
## FND-14610: chesscom.explanation_engine.v1.PuzzleGenFailureReason.failure_phase = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGenFailureReason",
  "name": "failure_phase",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleGenPhase",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14611"></a>
## FND-14611: chesscom.explanation_engine.v1.PuzzleGenFailureReason.failure_type = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGenFailureReason",
  "name": "failure_type",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14612"></a>
## FND-14612: chesscom.explanation_engine.v1.PuzzleGenFailureReason.failure_message = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PuzzleGenFailureReason",
  "name": "failure_message",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14613"></a>
## FND-14613: Native message: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeaturePuzzleGenRequest",
  "field": [
    {
      "name": "stream_progress",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "full_selected_line",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "do_puzzle_tree_generation",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "do_selected_line_verification",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "do_pitch_verification",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "add_variations_to_pgn",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "mode",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGenMode",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "engine",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.CeeInternalEngine",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "include_board_events_in_pgn",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 6,
      "proto3_optional": true
    },
    {
      "name": "filter_board_events_in_pgn",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 7,
      "proto3_optional": true
    },
    {
      "name": "include_speech_in_pgn",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 8,
      "proto3_optional": true
    },
    {
      "name": "heartbeat_interval_seconds",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ],
  "oneof_decl": [
    {
      "name": "_do_puzzle_tree_generation"
    },
    {
      "name": "_do_selected_line_verification"
    },
    {
      "name": "_do_pitch_verification"
    },
    {
      "name": "_add_variations_to_pgn"
    },
    {
      "name": "_mode"
    },
    {
      "name": "_engine"
    },
    {
      "name": "_include_board_events_in_pgn"
    },
    {
      "name": "_filter_board_events_in_pgn"
    },
    {
      "name": "_include_speech_in_pgn"
    }
  ]
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14614"></a>
## FND-14614: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.stream_progress = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "stream_progress",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14615"></a>
## FND-14615: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.full_selected_line = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "full_selected_line",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14616"></a>
## FND-14616: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.do_puzzle_tree_generation = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "do_puzzle_tree_generation",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_do_puzzle_tree_generation",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14617"></a>
## FND-14617: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.do_selected_line_verification = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "do_selected_line_verification",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_do_selected_line_verification",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14618"></a>
## FND-14618: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.do_pitch_verification = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "do_pitch_verification",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_do_pitch_verification",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14619"></a>
## FND-14619: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.add_variations_to_pgn = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "add_variations_to_pgn",
  "number": 6,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_add_variations_to_pgn",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14620"></a>
## FND-14620: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.mode = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "mode",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.PuzzleGenMode",
  "label": "LABEL_OPTIONAL",
  "oneof": "_mode",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14621"></a>
## FND-14621: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.engine = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "engine",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.CeeInternalEngine",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14622"></a>
## FND-14622: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.include_board_events_in_pgn = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "include_board_events_in_pgn",
  "number": 9,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_include_board_events_in_pgn",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14623"></a>
## FND-14623: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.filter_board_events_in_pgn = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "filter_board_events_in_pgn",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_filter_board_events_in_pgn",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14624"></a>
## FND-14624: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.include_speech_in_pgn = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "include_speech_in_pgn",
  "number": 11,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_include_speech_in_pgn",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14625"></a>
## FND-14625: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.heartbeat_interval_seconds = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "name": "heartbeat_interval_seconds",
  "number": 12,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14626"></a>
## FND-14626: Native message: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeaturePuzzleGenResponse",
  "field": [
    {
      "name": "puzzle_gen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGen",
      "oneof_index": 0
    },
    {
      "name": "progress",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGenPhase",
      "oneof_index": 0
    },
    {
      "name": "log",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "failure_reason",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGenFailureReason",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "is_heartbeat",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ],
  "oneof_decl": [
    {
      "name": "puzzle_response"
    },
    {
      "name": "_failure_reason"
    }
  ]
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14627"></a>
## FND-14627: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.puzzle_gen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
  "name": "puzzle_gen",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleGen",
  "label": "LABEL_OPTIONAL",
  "oneof": "puzzle_response",
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14628"></a>
## FND-14628: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.progress = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
  "name": "progress",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PuzzleGenPhase",
  "label": "LABEL_OPTIONAL",
  "oneof": "puzzle_response",
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14629"></a>
## FND-14629: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.log = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
  "name": "log",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14630"></a>
## FND-14630: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.failure_reason = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
  "name": "failure_reason",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.PuzzleGenFailureReason",
  "label": "LABEL_OPTIONAL",
  "oneof": "_failure_reason",
  "proto3_optional": true,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14631"></a>
## FND-14631: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.is_heartbeat = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
  "name": "is_heartbeat",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14632"></a>
## FND-14632: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14633"></a>
## FND-14633: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_INIT = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_INIT",
  "number": 1,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14634"></a>
## FND-14634: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE",
  "number": 2,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14635"></a>
## FND-14635: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE",
  "number": 3,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14636"></a>
## FND-14636: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE",
  "number": 4,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14637"></a>
## FND-14637: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS",
  "number": 5,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14638"></a>
## FND-14638: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS",
  "number": 6,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14639"></a>
## FND-14639: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_COMPUTING_GOALS",
  "number": 7,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14640"></a>
## FND-14640: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_COMPUTING_THEMES",
  "number": 8,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14641"></a>
## FND-14641: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_DONE = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenPhase",
  "name": "PUZZLE_GEN_PHASE_DONE",
  "number": 9,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14642"></a>
## FND-14642: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14643"></a>
## FND-14643: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE",
  "number": 1,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14644"></a>
## FND-14644: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT",
  "number": 2,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14645"></a>
## FND-14645: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME",
  "number": 3,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14646"></a>
## FND-14646: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING",
  "number": 4,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14647"></a>
## FND-14647: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING",
  "number": 5,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14648"></a>
## FND-14648: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG",
  "number": 6,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14649"></a>
## FND-14649: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING",
  "number": 7,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14650"></a>
## FND-14650: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE",
  "number": 8,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14651"></a>
## FND-14651: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE",
  "number": 9,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14652"></a>
## FND-14652: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL",
  "number": 10,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14653"></a>
## FND-14653: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE",
  "number": 11,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14654"></a>
## FND-14654: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE",
  "number": 12,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14655"></a>
## FND-14655: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL",
  "number": 13,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14656"></a>
## FND-14656: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE",
  "number": 14,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14657"></a>
## FND-14657: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME",
  "number": 15,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14658"></a>
## FND-14658: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleGenFailureType",
  "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT",
  "number": 16,
  "source_id": "SRC-1011",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1011** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f1c24233c48ddbe84849cf002f924df6295e4ce4297d3be732e7801ed99f2718.bin)

**Source references:** SRC-1011, SRC-1889  
**URL references:** None independently associated  
**Related findings:** FND-14609, FND-14610, FND-14611

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14659"></a>
## FND-14659: Native message: chesscom.explanation_engine.v1.InternalFeatureSetMoveAnnotationsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureSetMoveAnnotationsRequest",
  "field": [
    {
      "name": "annotation",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveAnnotation"
    }
  ]
}

### Evidence

- **SRC-1012** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_set_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/20a5bf1004ba4f91a6bd73da074d2b845b6208aae7b1169f69e82d3f3ba6d87c.bin)

**Source references:** SRC-1012, SRC-1895  
**URL references:** None independently associated  
**Related findings:** FND-14660, FND-14661

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
