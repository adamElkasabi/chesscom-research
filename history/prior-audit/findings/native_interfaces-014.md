# native_interfaces — findings 1301–1400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13960"></a>
## FND-13960: chesscom.explanation_engine.v1.RelaxedLegalMovesResponse.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RelaxedLegalMovesResponse",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
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
**Related findings:** FND-13956, FND-13957, FND-13958

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13961"></a>
## FND-13961: Native message: chesscom.explanation_engine.v1.ResetEngineStateRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ResetEngineStateRequest",
  "field": [
    {
      "name": "engine_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_engine_id"
    }
  ]
}

### Evidence

- **SRC-0975** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_reset_engine_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38983df8d3f402452bcb0bf2d68c053d6b86045b2cd09aafb83fae2324af8fb4.bin)

**Source references:** SRC-0975, SRC-1763  
**URL references:** None independently associated  
**Related findings:** FND-13962, FND-13963

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13962"></a>
## FND-13962: chesscom.explanation_engine.v1.ResetEngineStateRequest.engine_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ResetEngineStateRequest",
  "name": "engine_id",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine_id",
  "proto3_optional": true,
  "source_id": "SRC-0975",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0975** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_reset_engine_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38983df8d3f402452bcb0bf2d68c053d6b86045b2cd09aafb83fae2324af8fb4.bin)

**Source references:** SRC-0975, SRC-1763  
**URL references:** None independently associated  
**Related findings:** FND-13961, FND-13963

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13963"></a>
## FND-13963: Native message: chesscom.explanation_engine.v1.ResetEngineStateResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ResetEngineStateResponse"
}

### Evidence

- **SRC-0975** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_reset_engine_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38983df8d3f402452bcb0bf2d68c053d6b86045b2cd09aafb83fae2324af8fb4.bin)

**Source references:** SRC-0975, SRC-1763  
**URL references:** None independently associated  
**Related findings:** FND-13961, FND-13962

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13964"></a>
## FND-13964: Native message: chesscom.explanation_engine.v1.RunLuaRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RunLuaRequest",
  "field": [
    {
      "name": "lua_code",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "keep_lua_session",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "lua_session_id",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "artifact_id",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ],
  "oneof_decl": [
    {
      "name": "_lua_session_id"
    }
  ]
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13965"></a>
## FND-13965: chesscom.explanation_engine.v1.RunLuaRequest.lua_code = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaRequest",
  "name": "lua_code",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13966"></a>
## FND-13966: chesscom.explanation_engine.v1.RunLuaRequest.keep_lua_session = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaRequest",
  "name": "keep_lua_session",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13967"></a>
## FND-13967: chesscom.explanation_engine.v1.RunLuaRequest.lua_session_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaRequest",
  "name": "lua_session_id",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_lua_session_id",
  "proto3_optional": true,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13968"></a>
## FND-13968: chesscom.explanation_engine.v1.RunLuaRequest.artifact_id = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaRequest",
  "name": "artifact_id",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13969"></a>
## FND-13969: Native message: chesscom.explanation_engine.v1.RunLuaResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RunLuaResponse",
  "field": [
    {
      "name": "is_lua_error",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "lua_error_msg",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "script_stdout",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "json_result",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "lua_session_id",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_lua_session_id"
    }
  ]
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13970"></a>
## FND-13970: chesscom.explanation_engine.v1.RunLuaResponse.is_lua_error = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaResponse",
  "name": "is_lua_error",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13971"></a>
## FND-13971: chesscom.explanation_engine.v1.RunLuaResponse.lua_error_msg = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaResponse",
  "name": "lua_error_msg",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13972"></a>
## FND-13972: chesscom.explanation_engine.v1.RunLuaResponse.script_stdout = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaResponse",
  "name": "script_stdout",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13973"></a>
## FND-13973: chesscom.explanation_engine.v1.RunLuaResponse.json_result = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaResponse",
  "name": "json_result",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13974"></a>
## FND-13974: chesscom.explanation_engine.v1.RunLuaResponse.lua_session_id = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunLuaResponse",
  "name": "lua_session_id",
  "number": 5,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_lua_session_id",
  "proto3_optional": true,
  "source_id": "SRC-0976",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0976** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_lua.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d065c5b401074a2f536426c3805f11d8cae7299a2e1b60a6292ef74ff30f126c.bin)

**Source references:** SRC-0976, SRC-1794  
**URL references:** None independently associated  
**Related findings:** FND-13964, FND-13965, FND-13966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13975"></a>
## FND-13975: Native message: chesscom.explanation_engine.v1.RunSearchRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RunSearchRequest",
  "field": [
    {
      "name": "search_parameters",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SearchParameters",
      "oneof_index": 0
    },
    {
      "name": "null_move_search_parameters",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SearchParameters",
      "oneof_index": 0
    },
    {
      "name": "game_review_search_settings",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
      "oneof_index": 0
    },
    {
      "name": "search_moves",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "stream_results",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "engine_id",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "heartbeat_interval_seconds",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "guarantee_nodes",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "guarantee_nodes_null_move",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "disable_maia",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "torch_search_mode",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.TorchSearchMode",
      "oneof_index": 5,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "search"
    },
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
      "name": "_torch_search_mode"
    }
  ]
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13976"></a>
## FND-13976: chesscom.explanation_engine.v1.RunSearchRequest.search_parameters = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "search_parameters",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13977"></a>
## FND-13977: chesscom.explanation_engine.v1.RunSearchRequest.null_move_search_parameters = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "null_move_search_parameters",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.SearchParameters",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13978"></a>
## FND-13978: chesscom.explanation_engine.v1.RunSearchRequest.game_review_search_settings = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "game_review_search_settings",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
  "label": "LABEL_OPTIONAL",
  "oneof": "search",
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13979"></a>
## FND-13979: chesscom.explanation_engine.v1.RunSearchRequest.search_moves = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "search_moves",
  "number": 4,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13980"></a>
## FND-13980: chesscom.explanation_engine.v1.RunSearchRequest.stream_results = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "stream_results",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13981"></a>
## FND-13981: chesscom.explanation_engine.v1.RunSearchRequest.engine_id = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "engine_id",
  "number": 6,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_engine_id",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13982"></a>
## FND-13982: chesscom.explanation_engine.v1.RunSearchRequest.heartbeat_interval_seconds = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "heartbeat_interval_seconds",
  "number": 7,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13983"></a>
## FND-13983: chesscom.explanation_engine.v1.RunSearchRequest.guarantee_nodes = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "guarantee_nodes",
  "number": 8,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_guarantee_nodes",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13984"></a>
## FND-13984: chesscom.explanation_engine.v1.RunSearchRequest.guarantee_nodes_null_move = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "guarantee_nodes_null_move",
  "number": 9,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_guarantee_nodes_null_move",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13985"></a>
## FND-13985: chesscom.explanation_engine.v1.RunSearchRequest.disable_maia = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "disable_maia",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_disable_maia",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13986"></a>
## FND-13986: chesscom.explanation_engine.v1.RunSearchRequest.torch_search_mode = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchRequest",
  "name": "torch_search_mode",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1.TorchSearchMode",
  "label": "LABEL_OPTIONAL",
  "oneof": "_torch_search_mode",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13987"></a>
## FND-13987: Native message: chesscom.explanation_engine.v1.RunSearchResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RunSearchResponse",
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
    },
    {
      "name": "is_heartbeat",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13988"></a>
## FND-13988: chesscom.explanation_engine.v1.RunSearchResponse.evaluations = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchResponse",
  "name": "evaluations",
  "number": 1,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13989"></a>
## FND-13989: chesscom.explanation_engine.v1.RunSearchResponse.progress = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchResponse",
  "name": "progress",
  "number": 2,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13990"></a>
## FND-13990: chesscom.explanation_engine.v1.RunSearchResponse.aborted = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchResponse",
  "name": "aborted",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13991"></a>
## FND-13991: chesscom.explanation_engine.v1.RunSearchResponse.log = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchResponse",
  "name": "log",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13992"></a>
## FND-13992: chesscom.explanation_engine.v1.RunSearchResponse.is_heartbeat = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RunSearchResponse",
  "name": "is_heartbeat",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13993"></a>
## FND-13993: Native message: chesscom.explanation_engine.v1.SearchLimits

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SearchLimits",
  "field": [
    {
      "name": "depth",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "nodes",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "time_ms",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 2,
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
    }
  ]
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13994"></a>
## FND-13994: chesscom.explanation_engine.v1.SearchLimits.depth = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchLimits",
  "name": "depth",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_depth",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13995"></a>
## FND-13995: chesscom.explanation_engine.v1.SearchLimits.nodes = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchLimits",
  "name": "nodes",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_nodes",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13996"></a>
## FND-13996: chesscom.explanation_engine.v1.SearchLimits.time_ms = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchLimits",
  "name": "time_ms",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_ms",
  "proto3_optional": true,
  "source_id": "SRC-0977",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0977** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_run_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/2358516f559ab23301015c0c896f31da14516ba3a99167790af70f33fb217349.bin)

**Source references:** SRC-0977, SRC-1816  
**URL references:** None independently associated  
**Related findings:** FND-13975, FND-13976, FND-13977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13997"></a>
## FND-13997: Native message: chesscom.explanation_engine.v1.SetCoachRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetCoachRequest",
  "field": [
    {
      "name": "text_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "locale",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0978** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b9c94112ab2f8a291040539e174d73dadde7327a217496a09da1edf8b3de18fb.bin)

**Source references:** SRC-0978, SRC-1830  
**URL references:** None independently associated  
**Related findings:** FND-13998, FND-13999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13998"></a>
## FND-13998: chesscom.explanation_engine.v1.SetCoachRequest.text_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SetCoachRequest",
  "name": "text_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0978",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0978** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b9c94112ab2f8a291040539e174d73dadde7327a217496a09da1edf8b3de18fb.bin)

**Source references:** SRC-0978, SRC-1830  
**URL references:** None independently associated  
**Related findings:** FND-13997, FND-13999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13999"></a>
## FND-13999: chesscom.explanation_engine.v1.SetCoachRequest.locale = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SetCoachRequest",
  "name": "locale",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0978",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0978** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b9c94112ab2f8a291040539e174d73dadde7327a217496a09da1edf8b3de18fb.bin)

**Source references:** SRC-0978, SRC-1830  
**URL references:** None independently associated  
**Related findings:** FND-13997, FND-13998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14000"></a>
## FND-14000: Native message: chesscom.explanation_engine.v1.SetCoachResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetCoachResponse"
}

### Evidence

- **SRC-0978** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_coach.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b9c94112ab2f8a291040539e174d73dadde7327a217496a09da1edf8b3de18fb.bin)

**Source references:** SRC-0978, SRC-1830  
**URL references:** None independently associated  
**Related findings:** FND-13997, FND-13998, FND-13999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14001"></a>
## FND-14001: Native message: chesscom.explanation_engine.v1.SetGameResultRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetGameResultRequest",
  "field": [
    {
      "name": "claimed_game_result",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameResult"
    }
  ]
}

### Evidence

- **SRC-0979** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_game_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/877212646a268761cad60c54b3b93dca6ece0698d6746d3ef8b475b9dbc74162.bin)

**Source references:** SRC-0979, SRC-1779  
**URL references:** None independently associated  
**Related findings:** FND-14002, FND-14003

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14002"></a>
## FND-14002: chesscom.explanation_engine.v1.SetGameResultRequest.claimed_game_result = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SetGameResultRequest",
  "name": "claimed_game_result",
  "number": 1,
  "type": ".chesscom.chess.v1.GameResult",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0979",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0979** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_game_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/877212646a268761cad60c54b3b93dca6ece0698d6746d3ef8b475b9dbc74162.bin)

**Source references:** SRC-0979, SRC-1779  
**URL references:** None independently associated  
**Related findings:** FND-14001, FND-14003

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14003"></a>
## FND-14003: Native message: chesscom.explanation_engine.v1.SetGameResultResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetGameResultResponse"
}

### Evidence

- **SRC-0979** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_game_result.proto.bin` — [preserved redacted evidence](../evidence/descriptors/877212646a268761cad60c54b3b93dca6ece0698d6746d3ef8b475b9dbc74162.bin)

**Source references:** SRC-0979, SRC-1779  
**URL references:** None independently associated  
**Related findings:** FND-14001, FND-14002

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14004"></a>
## FND-14004: Native message: chesscom.explanation_engine.v1.SetPgnHeadersRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetPgnHeadersRequest",
  "field": [
    {
      "name": "headers",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry"
    }
  ],
  "nested_type": [
    {
      "name": "HeadersEntry",
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
  ]
}

### Evidence

- **SRC-0980** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_pgn_headers.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ddb0655e68551b52bf8de90ede424c3e973e757317cc545bf51554ec266e0180.bin)

**Source references:** SRC-0980, SRC-1778  
**URL references:** None independently associated  
**Related findings:** FND-14005, FND-14006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14005"></a>
## FND-14005: chesscom.explanation_engine.v1.SetPgnHeadersRequest.headers = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SetPgnHeadersRequest",
  "name": "headers",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0980",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0980** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_pgn_headers.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ddb0655e68551b52bf8de90ede424c3e973e757317cc545bf51554ec266e0180.bin)

**Source references:** SRC-0980, SRC-1778  
**URL references:** None independently associated  
**Related findings:** FND-14004, FND-14006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14006"></a>
## FND-14006: Native message: chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "HeadersEntry",
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

- **SRC-0980** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_pgn_headers.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ddb0655e68551b52bf8de90ede424c3e973e757317cc545bf51554ec266e0180.bin)

**Source references:** SRC-0980, SRC-1778  
**URL references:** None independently associated  
**Related findings:** FND-14004, FND-14005

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14007"></a>
## FND-14007: chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0980",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0980** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_pgn_headers.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ddb0655e68551b52bf8de90ede424c3e973e757317cc545bf51554ec266e0180.bin)

**Source references:** SRC-0980, SRC-1778  
**URL references:** None independently associated  
**Related findings:** FND-14004, FND-14005, FND-14006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14008"></a>
## FND-14008: chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SetPgnHeadersRequest.HeadersEntry",
  "name": "value",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0980",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0980** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_pgn_headers.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ddb0655e68551b52bf8de90ede424c3e973e757317cc545bf51554ec266e0180.bin)

**Source references:** SRC-0980, SRC-1778  
**URL references:** None independently associated  
**Related findings:** FND-14004, FND-14005, FND-14006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14009"></a>
## FND-14009: Native message: chesscom.explanation_engine.v1.SetPgnHeadersResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetPgnHeadersResponse"
}

### Evidence

- **SRC-0980** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_pgn_headers.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ddb0655e68551b52bf8de90ede424c3e973e757317cc545bf51554ec266e0180.bin)

**Source references:** SRC-0980, SRC-1778  
**URL references:** None independently associated  
**Related findings:** FND-14004, FND-14005, FND-14006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14010"></a>
## FND-14010: Native message: chesscom.explanation_engine.v1.SetPlayedLineRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetPlayedLineRequest"
}

### Evidence

- **SRC-0981** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_played_line.proto.bin` — [preserved redacted evidence](../evidence/descriptors/80670a1e7d374f2000f62f334e33516b37c166d97f346d1db69a47aa64fd3afd.bin)

**Source references:** SRC-0981, SRC-1743  
**URL references:** None independently associated  
**Related findings:** FND-14011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14011"></a>
## FND-14011: Native message: chesscom.explanation_engine.v1.SetPlayedLineResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SetPlayedLineResponse"
}

### Evidence

- **SRC-0981** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_set_played_line.proto.bin` — [preserved redacted evidence](../evidence/descriptors/80670a1e7d374f2000f62f334e33516b37c166d97f346d1db69a47aa64fd3afd.bin)

**Source references:** SRC-0981, SRC-1743  
**URL references:** None independently associated  
**Related findings:** FND-14010

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14012"></a>
## FND-14012: Native message: chesscom.explanation_engine.v1.SimpleThreatsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SimpleThreatsRequest",
  "field": [
    {
      "name": "threats_limit",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0982** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_simple_threats.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3610cefa18b8991903b2ac9352142d2cc7da818e5169d84d7ed9bdf5b9b2d6a4.bin)

**Source references:** SRC-0982, SRC-1810  
**URL references:** None independently associated  
**Related findings:** FND-14013, FND-14014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14013"></a>
## FND-14013: chesscom.explanation_engine.v1.SimpleThreatsRequest.threats_limit = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleThreatsRequest",
  "name": "threats_limit",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0982",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0982** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_simple_threats.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3610cefa18b8991903b2ac9352142d2cc7da818e5169d84d7ed9bdf5b9b2d6a4.bin)

**Source references:** SRC-0982, SRC-1810  
**URL references:** None independently associated  
**Related findings:** FND-14012, FND-14014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14014"></a>
## FND-14014: Native message: chesscom.explanation_engine.v1.SimpleThreatsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SimpleThreatsResponse",
  "field": [
    {
      "name": "threats",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SimpleThreat"
    }
  ]
}

### Evidence

- **SRC-0982** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_simple_threats.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3610cefa18b8991903b2ac9352142d2cc7da818e5169d84d7ed9bdf5b9b2d6a4.bin)

**Source references:** SRC-0982, SRC-1810  
**URL references:** None independently associated  
**Related findings:** FND-14012, FND-14013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14015"></a>
## FND-14015: chesscom.explanation_engine.v1.SimpleThreatsResponse.threats = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleThreatsResponse",
  "name": "threats",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SimpleThreat",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0982",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0982** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_simple_threats.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3610cefa18b8991903b2ac9352142d2cc7da818e5169d84d7ed9bdf5b9b2d6a4.bin)

**Source references:** SRC-0982, SRC-1810  
**URL references:** None independently associated  
**Related findings:** FND-14012, FND-14013, FND-14014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14016"></a>
## FND-14016: Native message: chesscom.explanation_engine.v1.SwitchSidesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SwitchSidesRequest"
}

### Evidence

- **SRC-0983** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_switch_sides.proto.bin` — [preserved redacted evidence](../evidence/descriptors/46b11fd9cedcc28cd95f40ff24347e434432ba89c0686235b2d3164e5fe81d85.bin)

**Source references:** SRC-0983, SRC-1746  
**URL references:** None independently associated  
**Related findings:** FND-14017

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14017"></a>
## FND-14017: Native message: chesscom.explanation_engine.v1.SwitchSidesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SwitchSidesResponse"
}

### Evidence

- **SRC-0983** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_switch_sides.proto.bin` — [preserved redacted evidence](../evidence/descriptors/46b11fd9cedcc28cd95f40ff24347e434432ba89c0686235b2d3164e5fe81d85.bin)

**Source references:** SRC-0983, SRC-1746  
**URL references:** None independently associated  
**Related findings:** FND-14016

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14018"></a>
## FND-14018: Native message: chesscom.explanation_engine.v1.UnmakeMovesRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "UnmakeMovesRequest"
}

### Evidence

- **SRC-0984** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_unmake_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/68abd4de66aa70fec62e0b8641964c5f5595ea354f2064f643343acd12b80371.bin)

**Source references:** SRC-0984, SRC-1874  
**URL references:** None independently associated  
**Related findings:** FND-14019

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14019"></a>
## FND-14019: Native message: chesscom.explanation_engine.v1.UnmakeMovesResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "UnmakeMovesResponse"
}

### Evidence

- **SRC-0984** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_unmake_moves.proto.bin` — [preserved redacted evidence](../evidence/descriptors/68abd4de66aa70fec62e0b8641964c5f5595ea354f2064f643343acd12b80371.bin)

**Source references:** SRC-0984, SRC-1874  
**URL references:** None independently associated  
**Related findings:** FND-14018

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14020"></a>
## FND-14020: Native message: chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "UpdateExperimentalOptionsRequest",
  "field": [
    {
      "name": "options",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.ExperimentalOptions"
    }
  ]
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14021"></a>
## FND-14021: chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest.options = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest",
  "name": "options",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.ExperimentalOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0985",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14022"></a>
## FND-14022: Native message: chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "UpdateExperimentalOptionsResponse",
  "field": [
    {
      "name": "options",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.ExperimentalOptions"
    }
  ]
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14023"></a>
## FND-14023: chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse.options = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse",
  "name": "options",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.ExperimentalOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0985",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14024"></a>
## FND-14024: Native message: chesscom.explanation_engine.v1.ExperimentalOptions

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ExperimentalOptions",
  "field": [
    {
      "name": "play_coach_flip_board_enabled",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "play_coach_retry_misses_enabled",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "illegal_move_explanation_mode",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.IllegalMoveExplanationMode",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "allow_tricky_classification",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 3,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_play_coach_flip_board_enabled"
    },
    {
      "name": "_play_coach_retry_misses_enabled"
    },
    {
      "name": "_illegal_move_explanation_mode"
    },
    {
      "name": "_allow_tricky_classification"
    }
  ],
  "reserved_range": [
    {
      "start": 1,
      "end": 5
    }
  ]
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14025"></a>
## FND-14025: chesscom.explanation_engine.v1.ExperimentalOptions.play_coach_flip_board_enabled = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExperimentalOptions",
  "name": "play_coach_flip_board_enabled",
  "number": 5,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_play_coach_flip_board_enabled",
  "proto3_optional": true,
  "source_id": "SRC-0985",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14026"></a>
## FND-14026: chesscom.explanation_engine.v1.ExperimentalOptions.play_coach_retry_misses_enabled = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExperimentalOptions",
  "name": "play_coach_retry_misses_enabled",
  "number": 6,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_play_coach_retry_misses_enabled",
  "proto3_optional": true,
  "source_id": "SRC-0985",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14027"></a>
## FND-14027: chesscom.explanation_engine.v1.ExperimentalOptions.illegal_move_explanation_mode = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExperimentalOptions",
  "name": "illegal_move_explanation_mode",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.IllegalMoveExplanationMode",
  "label": "LABEL_OPTIONAL",
  "oneof": "_illegal_move_explanation_mode",
  "proto3_optional": true,
  "source_id": "SRC-0985",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14028"></a>
## FND-14028: chesscom.explanation_engine.v1.ExperimentalOptions.allow_tricky_classification = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ExperimentalOptions",
  "name": "allow_tricky_classification",
  "number": 8,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_allow_tricky_classification",
  "proto3_optional": true,
  "source_id": "SRC-0985",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0985** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_update_experimental_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/54d0e906f7664089b1fec5697d29c637f061080cf86272473fbf227704a8b8a0.bin)

**Source references:** SRC-0985, SRC-1848  
**URL references:** None independently associated  
**Related findings:** FND-14020, FND-14021, FND-14022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14029"></a>
## FND-14029: Native message: chesscom.explanation_engine.v1.ValidateFenRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ValidateFenRequest",
  "field": [
    {
      "name": "fen",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "check_syntax_only",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    }
  ]
}

### Evidence

- **SRC-0987** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f8100bb9e38a0bb846e467501abe327f27d7d7fe28a6b36b83f75025cecbd7e2.bin)

**Source references:** SRC-0987, SRC-1670  
**URL references:** None independently associated  
**Related findings:** FND-14030, FND-14031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14030"></a>
## FND-14030: chesscom.explanation_engine.v1.ValidateFenRequest.fen = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateFenRequest",
  "name": "fen",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0987",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0987** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f8100bb9e38a0bb846e467501abe327f27d7d7fe28a6b36b83f75025cecbd7e2.bin)

**Source references:** SRC-0987, SRC-1670  
**URL references:** None independently associated  
**Related findings:** FND-14029, FND-14031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14031"></a>
## FND-14031: chesscom.explanation_engine.v1.ValidateFenRequest.check_syntax_only = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateFenRequest",
  "name": "check_syntax_only",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0987",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0987** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f8100bb9e38a0bb846e467501abe327f27d7d7fe28a6b36b83f75025cecbd7e2.bin)

**Source references:** SRC-0987, SRC-1670  
**URL references:** None independently associated  
**Related findings:** FND-14029, FND-14030

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14032"></a>
## FND-14032: Native message: chesscom.explanation_engine.v1.ValidateFenResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ValidateFenResponse",
  "field": [
    {
      "name": "error",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "result_type",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.ResultType",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_error"
    },
    {
      "name": "_result_type"
    }
  ]
}

### Evidence

- **SRC-0987** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f8100bb9e38a0bb846e467501abe327f27d7d7fe28a6b36b83f75025cecbd7e2.bin)

**Source references:** SRC-0987, SRC-1670  
**URL references:** None independently associated  
**Related findings:** FND-14029, FND-14030, FND-14031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14033"></a>
## FND-14033: chesscom.explanation_engine.v1.ValidateFenResponse.error = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateFenResponse",
  "name": "error",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_error",
  "proto3_optional": true,
  "source_id": "SRC-0987",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0987** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f8100bb9e38a0bb846e467501abe327f27d7d7fe28a6b36b83f75025cecbd7e2.bin)

**Source references:** SRC-0987, SRC-1670  
**URL references:** None independently associated  
**Related findings:** FND-14029, FND-14030, FND-14031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14034"></a>
## FND-14034: chesscom.explanation_engine.v1.ValidateFenResponse.result_type = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateFenResponse",
  "name": "result_type",
  "number": 2,
  "type": ".chesscom.chess.v1.ResultType",
  "label": "LABEL_OPTIONAL",
  "oneof": "_result_type",
  "proto3_optional": true,
  "source_id": "SRC-0987",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0987** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_fen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f8100bb9e38a0bb846e467501abe327f27d7d7fe28a6b36b83f75025cecbd7e2.bin)

**Source references:** SRC-0987, SRC-1670  
**URL references:** None independently associated  
**Related findings:** FND-14029, FND-14030, FND-14031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14035"></a>
## FND-14035: Native message: chesscom.explanation_engine.v1.ValidateGameForAnalysisRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ValidateGameForAnalysisRequest",
  "field": [
    {
      "name": "starting_game_point",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_starting_game_point"
    }
  ]
}

### Evidence

- **SRC-0988** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_game_for_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8e4c3c659fbc0902b09318c9c14317232af3dde389538fbafa99e0245dcdcdbb.bin)

**Source references:** SRC-0988, SRC-1820  
**URL references:** None independently associated  
**Related findings:** FND-14036, FND-14037

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14036"></a>
## FND-14036: chesscom.explanation_engine.v1.ValidateGameForAnalysisRequest.starting_game_point = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateGameForAnalysisRequest",
  "name": "starting_game_point",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_starting_game_point",
  "proto3_optional": true,
  "source_id": "SRC-0988",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0988** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_game_for_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8e4c3c659fbc0902b09318c9c14317232af3dde389538fbafa99e0245dcdcdbb.bin)

**Source references:** SRC-0988, SRC-1820  
**URL references:** None independently associated  
**Related findings:** FND-14035, FND-14037

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14037"></a>
## FND-14037: Native message: chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ValidateGameForAnalysisResponse",
  "field": [
    {
      "name": "error",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "analyzability_constraint",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGame",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "invalid_game",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGame",
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_error"
    },
    {
      "name": "_analyzability_constraint"
    },
    {
      "name": "_invalid_game"
    }
  ]
}

### Evidence

- **SRC-0988** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_game_for_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8e4c3c659fbc0902b09318c9c14317232af3dde389538fbafa99e0245dcdcdbb.bin)

**Source references:** SRC-0988, SRC-1820  
**URL references:** None independently associated  
**Related findings:** FND-14035, FND-14036

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14038"></a>
## FND-14038: chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse.error = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse",
  "name": "error",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_error",
  "proto3_optional": true,
  "source_id": "SRC-0988",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0988** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_game_for_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8e4c3c659fbc0902b09318c9c14317232af3dde389538fbafa99e0245dcdcdbb.bin)

**Source references:** SRC-0988, SRC-1820  
**URL references:** None independently associated  
**Related findings:** FND-14035, FND-14036, FND-14037

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14039"></a>
## FND-14039: chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse.analyzability_constraint = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse",
  "name": "analyzability_constraint",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.UnanalyzableGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "_analyzability_constraint",
  "proto3_optional": true,
  "source_id": "SRC-0988",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0988** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_game_for_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8e4c3c659fbc0902b09318c9c14317232af3dde389538fbafa99e0245dcdcdbb.bin)

**Source references:** SRC-0988, SRC-1820  
**URL references:** None independently associated  
**Related findings:** FND-14035, FND-14036, FND-14037

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14040"></a>
## FND-14040: chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse.invalid_game = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidateGameForAnalysisResponse",
  "name": "invalid_game",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.InvalidGame",
  "label": "LABEL_OPTIONAL",
  "oneof": "_invalid_game",
  "proto3_optional": true,
  "source_id": "SRC-0988",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0988** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_game_for_analysis.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8e4c3c659fbc0902b09318c9c14317232af3dde389538fbafa99e0245dcdcdbb.bin)

**Source references:** SRC-0988, SRC-1820  
**URL references:** None independently associated  
**Related findings:** FND-14035, FND-14036, FND-14037

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14041"></a>
## FND-14041: Native message: chesscom.explanation_engine.v1.ValidatePgnRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ValidatePgnRequest",
  "field": [
    {
      "name": "pgn",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "artifact_id",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14042"></a>
## FND-14042: chesscom.explanation_engine.v1.ValidatePgnRequest.pgn = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidatePgnRequest",
  "name": "pgn",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14043"></a>
## FND-14043: chesscom.explanation_engine.v1.ValidatePgnRequest.artifact_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidatePgnRequest",
  "name": "artifact_id",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14044"></a>
## FND-14044: Native message: chesscom.explanation_engine.v1.ValidatePgnResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ValidatePgnResponse",
  "field": [
    {
      "name": "result",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PgnGameValidationResult"
    }
  ]
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14045"></a>
## FND-14045: chesscom.explanation_engine.v1.ValidatePgnResponse.result = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ValidatePgnResponse",
  "name": "result",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PgnGameValidationResult",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14046"></a>
## FND-14046: Native message: chesscom.explanation_engine.v1.PgnGameValidationResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PgnGameValidationResult",
  "field": [
    {
      "name": "success",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PgnGameValidationSuccess",
      "oneof_index": 0
    },
    {
      "name": "error",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PgnGameValidationError",
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

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14047"></a>
## FND-14047: chesscom.explanation_engine.v1.PgnGameValidationResult.success = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGameValidationResult",
  "name": "success",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PgnGameValidationSuccess",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14048"></a>
## FND-14048: chesscom.explanation_engine.v1.PgnGameValidationResult.error = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGameValidationResult",
  "name": "error",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PgnGameValidationError",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14049"></a>
## FND-14049: Native message: chesscom.explanation_engine.v1.PgnGameValidationSuccess

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PgnGameValidationSuccess",
  "field": [
    {
      "name": "game_pgn",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14050"></a>
## FND-14050: chesscom.explanation_engine.v1.PgnGameValidationSuccess.game_pgn = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGameValidationSuccess",
  "name": "game_pgn",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14051"></a>
## FND-14051: Native message: chesscom.explanation_engine.v1.PgnGameValidationError

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PgnGameValidationError",
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

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14052"></a>
## FND-14052: chesscom.explanation_engine.v1.PgnGameValidationError.error = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PgnGameValidationError",
  "name": "error",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0989",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0989** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_validate_pgn.proto.bin` — [preserved redacted evidence](../evidence/descriptors/e545520669d4ccc728c42e707ef24f21e2c726092a68e61c783b42f37427272d.bin)

**Source references:** SRC-0989, SRC-1870  
**URL references:** None independently associated  
**Related findings:** FND-14041, FND-14042, FND-14043

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14053"></a>
## FND-14053: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14054, FND-14055

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14054"></a>
## FND-14054: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_ADD_EVALUATIONS = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_ADD_EVALUATIONS",
  "number": 1,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14053, FND-14055

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14055"></a>
## FND-14055: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_CEE_VERSION = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_CEE_VERSION",
  "number": 2,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14053, FND-14054

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14056"></a>
## FND-14056: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_EXPECTED_POINTS = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_EXPECTED_POINTS",
  "number": 3,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14053, FND-14054, FND-14055

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14057"></a>
## FND-14057: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_ANALYSIS = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_GAME_ANALYSIS",
  "number": 4,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14053, FND-14054, FND-14055

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14058"></a>
## FND-14058: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_PHASE_TRANSITIONS = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_GAME_PHASE_TRANSITIONS",
  "number": 5,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14053, FND-14054, FND-14055

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14059"></a>
## FND-14059: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_POINT_INFO = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.FeatureId",
  "name": "FEATURE_ID_GAME_POINT_INFO",
  "number": 6,
  "source_id": "SRC-0990",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0990** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_features.proto.bin` — [preserved redacted evidence](../evidence/descriptors/26b41e4d42a351966093374854b69392a6398e43ea15a58ee4affeaba74ce1bc.bin)

**Source references:** SRC-0990, SRC-1680  
**URL references:** None independently associated  
**Related findings:** FND-14053, FND-14054, FND-14055

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
