# data_models — findings 3201–3300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03475"></a>
## FND-03475: message declaration: chesscom.explanation_engine.v1.NewGameRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NewGameRequest {

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 125.

```text
nation_engine/v1/feature_new_game.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message NewGameRequest {
  optional .chesscom.explanation_engine.v1.NewGame new_game = 1;
  optional bool enable_typed_invalid_game_errors = 2;
}

message NewGameResponse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInf
```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03476, FND-03477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03476"></a>
## FND-03476: chesscom.explanation_engine.v1.NewGameRequest.new_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.NewGame new_game = 1;

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 152.

```text
w_game.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message NewGameRequest {
  optional .chesscom.explanation_engine.v1.NewGame new_game = 1;
  optional bool enable_typed_invalid_game_errors = 2;
}

message NewGameResponse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03475, FND-03477

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03477"></a>
## FND-03477: chesscom.explanation_engine.v1.NewGameRequest.enable_typed_invalid_game_errors = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_typed_invalid_game_errors = 2;

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 217.

```text
ne.v1;

message NewGameRequest {
  optional .chesscom.explanation_engine.v1.NewGame new_game = 1;
  optional bool enable_typed_invalid_game_errors = 2;
}

message NewGameResponse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03475, FND-03476

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03478"></a>
## FND-03478: message declaration: chesscom.explanation_engine.v1.NewGameResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NewGameResponse {

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 272.

```text
xplanation_engine.v1.NewGame new_game = 1;
  optional bool enable_typed_invalid_game_errors = 2;
}

message NewGameResponse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03475, FND-03476, FND-03477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03479"></a>
## FND-03479: oneof declaration: chesscom.explanation_engine.v1.NewGameResponse._invalid_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _invalid_game {

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 300.

```text
 new_game = 1;
  optional bool enable_typed_invalid_game_errors = 2;
}

message NewGameResponse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03475, FND-03476, FND-03477

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03480"></a>
## FND-03480: chesscom.explanation_engine.v1.NewGameResponse.invalid_game = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 324.

```text
l bool enable_typed_invalid_game_errors = 2;
}

message NewGameResponse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03475, FND-03476, FND-03477

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03481"></a>
## FND-03481: chesscom.explanation_engine.v1.NewGameResponse.played_line = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;

### Evidence

- **SRC-0390** `research/proto/chesscom/explanation_engine/v1/feature_new_game.proto` — [preserved redacted evidence](../evidence/text/b14ce3ebe835adce3f2b492d4574224ae20537dda7d37b8c939765e6904e3db8.proto)
  Character offset 392.

```text
nse {
  oneof _invalid_game {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 2;
  }
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0390, SRC-1361  
**URL references:** None independently associated  
**Related findings:** FND-03475, FND-03476, FND-03477

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03482"></a>
## FND-03482: message declaration: chesscom.explanation_engine.v1.RunLuaRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunLuaRequest {

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 124.

```text
anation_engine/v1/feature_run_lua.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message RunLuaRequest {
  oneof _lua_session_id {
  int32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional st
```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03483, FND-03484

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03483"></a>
## FND-03483: oneof declaration: chesscom.explanation_engine.v1.RunLuaRequest._lua_session_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lua_session_id {

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 150.

```text
run_lua.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message RunLuaRequest {
  oneof _lua_session_id {
  int32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  
```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03484

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03484"></a>
## FND-03484: chesscom.explanation_engine.v1.RunLuaRequest.lua_session_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 lua_session_id = 3;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 176.

```text
roto3

package chesscom.explanation_engine.v1;

message RunLuaRequest {
  oneof _lua_session_id {
  int32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_std
```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03485"></a>
## FND-03485: chesscom.explanation_engine.v1.RunLuaRequest.lua_code = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string lua_code = 1;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 208.

```text
ion_engine.v1;

message RunLuaRequest {
  oneof _lua_session_id {
  int32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_
```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03486"></a>
## FND-03486: chesscom.explanation_engine.v1.RunLuaRequest.keep_lua_session = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool keep_lua_session = 2;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 240.

```text
quest {
  oneof _lua_session_id {
  int32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03487"></a>
## FND-03487: chesscom.explanation_engine.v1.RunLuaRequest.artifact_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string artifact_id = 4;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 278.

```text
t32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03488"></a>
## FND-03488: message declaration: chesscom.explanation_engine.v1.RunLuaResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunLuaResponse {

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 314.

```text
al string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03489"></a>
## FND-03489: oneof declaration: chesscom.explanation_engine.v1.RunLuaResponse._lua_session_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lua_session_id {

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 150.

```text
run_lua.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message RunLuaRequest {
  oneof _lua_session_id {
  int32 lua_session_id = 3;
  }
  optional string lua_code = 1;
  optional bool keep_lua_session = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  
```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03490"></a>
## FND-03490: chesscom.explanation_engine.v1.RunLuaResponse.lua_session_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 lua_session_id = 5;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 367.

```text
ion = 2;
  optional string artifact_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03491"></a>
## FND-03491: chesscom.explanation_engine.v1.RunLuaResponse.is_lua_error = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_lua_error = 1;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 399.

```text
act_id = 4;
}

message RunLuaResponse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03492"></a>
## FND-03492: chesscom.explanation_engine.v1.RunLuaResponse.lua_error_msg = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string lua_error_msg = 2;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 433.

```text
nse {
  oneof _lua_session_id {
  int32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03493"></a>
## FND-03493: chesscom.explanation_engine.v1.RunLuaResponse.script_stdout = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string script_stdout = 3;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 470.

```text
32 lua_session_id = 5;
  }
  optional bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03494"></a>
## FND-03494: chesscom.explanation_engine.v1.RunLuaResponse.json_result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string json_result = 4;

### Evidence

- **SRC-0391** `research/proto/chesscom/explanation_engine/v1/feature_run_lua.proto` — [preserved redacted evidence](../evidence/text/67b16f8737825896db0d3a25acc2010d612e24c86fd0bb0bf8da8317532ab033.proto)
  Character offset 507.

```text
 bool is_lua_error = 1;
  optional string lua_error_msg = 2;
  optional string script_stdout = 3;
  optional string json_result = 4;
}

```

**Source references:** SRC-0391, SRC-1362  
**URL references:** None independently associated  
**Related findings:** FND-03482, FND-03483, FND-03484

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03495"></a>
## FND-03495: message declaration: chesscom.explanation_engine.v1.RunSearchRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchRequest {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 127.

```text
tion_engine/v1/feature_run_search.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message RunSearchRequest {
  oneof search {
  .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
 
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03496"></a>
## FND-03496: oneof declaration: chesscom.explanation_engine.v1.RunSearchRequest.search

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof search {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 156.

```text
arch.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message RunSearchRequest {
  oneof search {
  .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  o
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03497"></a>
## FND-03497: chesscom.explanation_engine.v1.RunSearchRequest.search_parameters = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 173.

```text
tax: proto3

package chesscom.explanation_engine.v1;

message RunSearchRequest {
  oneof search {
  .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_n
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03498"></a>
## FND-03498: chesscom.explanation_engine.v1.RunSearchRequest.null_move_search_parameters = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 247.

```text
uest {
  oneof search {
  .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move 
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03499"></a>
## FND-03499: chesscom.explanation_engine.v1.RunSearchRequest.game_review_search_settings = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 331.

```text
rameters = 1;
  .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_m
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03500"></a>
## FND-03500: oneof declaration: chesscom.explanation_engine.v1.RunSearchRequest._engine_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _engine_id {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 427.

```text
;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode tor
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03501"></a>
## FND-03501: chesscom.explanation_engine.v1.RunSearchRequest.engine_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 engine_id = 6;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 448.

```text
tion_engine.v1.GameReviewSearchSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03502"></a>
## FND-03502: oneof declaration: chesscom.explanation_engine.v1.RunSearchRequest._guarantee_nodes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _guarantee_nodes {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 475.

```text
archSettings game_review_search_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.ch
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03503"></a>
## FND-03503: chesscom.explanation_engine.v1.RunSearchRequest.guarantee_nodes = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool guarantee_nodes = 8;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 502.

```text
arch_settings = 3;
  }
  oneof _engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03504"></a>
## FND-03504: oneof declaration: chesscom.explanation_engine.v1.RunSearchRequest._guarantee_nodes_null_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _guarantee_nodes_null_move {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 534.

```text
engine_id {
  int32 engine_id = 6;
  }
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_result
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03505"></a>
## FND-03505: chesscom.explanation_engine.v1.RunSearchRequest.guarantee_nodes_null_move = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool guarantee_nodes_null_move = 9;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 571.

```text
}
  oneof _guarantee_nodes {
  bool guarantee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_int
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03506"></a>
## FND-03506: oneof declaration: chesscom.explanation_engine.v1.RunSearchRequest._disable_maia

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _disable_maia {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 613.

```text
tee_nodes = 8;
  }
  oneof _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchRes
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03507"></a>
## FND-03507: chesscom.explanation_engine.v1.RunSearchRequest.disable_maia = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool disable_maia = 10;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 637.

```text
of _guarantee_nodes_null_move {
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .ches
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03508"></a>
## FND-03508: oneof declaration: chesscom.explanation_engine.v1.RunSearchRequest._torch_search_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _torch_search_mode {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 667.

```text
{
  bool guarantee_nodes_null_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation eval
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03509"></a>
## FND-03509: chesscom.explanation_engine.v1.RunSearchRequest.torch_search_mode = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 696.

```text
_move = 9;
  }
  oneof _disable_maia {
  bool disable_maia = 10;
  }
  oneof _torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03510"></a>
## FND-03510: chesscom.explanation_engine.v1.RunSearchRequest.search_moves = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move search_moves = 4;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 774.

```text
torch_search_mode {
  .chesscom.explanation_engine.v1.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optio
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03511"></a>
## FND-03511: chesscom.explanation_engine.v1.RunSearchRequest.stream_results = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool stream_results = 5;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 827.

```text
.TorchSearchMode torch_search_mode = 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03512"></a>
## FND-03512: chesscom.explanation_engine.v1.RunSearchRequest.heartbeat_interval_seconds = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 heartbeat_interval_seconds = 7;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 863.

```text
 11;
  }
  repeated .chesscom.chess.v1.Move search_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03513"></a>
## FND-03513: message declaration: chesscom.explanation_engine.v1.RunSearchResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchResponse {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 913.

```text
_moves = 4;
  optional bool stream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneo
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03514"></a>
## FND-03514: chesscom.explanation_engine.v1.RunSearchResponse.evaluations = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.engine.v1.Evaluation evaluations = 1;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 943.

```text
ream_results = 5;
  optional int32 heartbeat_interval_seconds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms =
```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03515"></a>
## FND-03515: chesscom.explanation_engine.v1.RunSearchResponse.progress = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float progress = 2;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1002.

```text
ds = 7;
}

message RunSearchResponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03516"></a>
## FND-03516: chesscom.explanation_engine.v1.RunSearchResponse.aborted = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool aborted = 3;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1033.

```text
ponse {
  repeated .chesscom.engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03517"></a>
## FND-03517: chesscom.explanation_engine.v1.RunSearchResponse.log = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string log = 4;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1062.

```text
engine.v1.Evaluation evaluations = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03518"></a>
## FND-03518: chesscom.explanation_engine.v1.RunSearchResponse.is_heartbeat = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_heartbeat = 5;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1089.

```text
tions = 1;
  optional float progress = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03519"></a>
## FND-03519: message declaration: chesscom.explanation_engine.v1.SearchLimits

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SearchLimits {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1124.

```text
s = 2;
  optional bool aborted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03520"></a>
## FND-03520: oneof declaration: chesscom.explanation_engine.v1.SearchLimits._depth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _depth {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1149.

```text
orted = 3;
  repeated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03521"></a>
## FND-03521: chesscom.explanation_engine.v1.SearchLimits.depth = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 depth = 1;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1166.

```text
ated string log = 4;
  optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03522"></a>
## FND-03522: oneof declaration: chesscom.explanation_engine.v1.SearchLimits._nodes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _nodes {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1189.

```text
optional bool is_heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03523"></a>
## FND-03523: chesscom.explanation_engine.v1.SearchLimits.nodes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 nodes = 2;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1206.

```text
heartbeat = 5;
}

message SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03524"></a>
## FND-03524: oneof declaration: chesscom.explanation_engine.v1.SearchLimits._time_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_ms {

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1229.

```text
ge SearchLimits {
  oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03525"></a>
## FND-03525: chesscom.explanation_engine.v1.SearchLimits.time_ms = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 time_ms = 3;

### Evidence

- **SRC-0392** `research/proto/chesscom/explanation_engine/v1/feature_run_search.proto` — [preserved redacted evidence](../evidence/text/5b49b8bbedb17793037dca90e4f7b7fe67c593e8b53bcebd73c04d1770c02a11.proto)
  Character offset 1248.

```text
 oneof _depth {
  int32 depth = 1;
  }
  oneof _nodes {
  int32 nodes = 2;
  }
  oneof _time_ms {
  int32 time_ms = 3;
  }
}

```

**Source references:** SRC-0392, SRC-1363  
**URL references:** None independently associated  
**Related findings:** FND-03495, FND-03496, FND-03497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03526"></a>
## FND-03526: message declaration: chesscom.explanation_engine.v1.SetCoachRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCoachRequest {

### Evidence

- **SRC-0393** `research/proto/chesscom/explanation_engine/v1/feature_set_coach.proto` — [preserved redacted evidence](../evidence/text/63455c03d651d2e045c6f4d4745fe63ea5107811da27f27aeffced3e84ef5732.proto)
  Character offset 126.

```text
ation_engine/v1/feature_set_coach.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SetCoachRequest {
  optional string text_id = 1;
  optional string locale = 2;
}

message SetCoachResponse {
}

```

**Source references:** SRC-0393, SRC-1364  
**URL references:** None independently associated  
**Related findings:** FND-03527, FND-03528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03527"></a>
## FND-03527: chesscom.explanation_engine.v1.SetCoachRequest.text_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text_id = 1;

### Evidence

- **SRC-0393** `research/proto/chesscom/explanation_engine/v1/feature_set_coach.proto` — [preserved redacted evidence](../evidence/text/63455c03d651d2e045c6f4d4745fe63ea5107811da27f27aeffced3e84ef5732.proto)
  Character offset 154.

```text
coach.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SetCoachRequest {
  optional string text_id = 1;
  optional string locale = 2;
}

message SetCoachResponse {
}

```

**Source references:** SRC-0393, SRC-1364  
**URL references:** None independently associated  
**Related findings:** FND-03526, FND-03528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03528"></a>
## FND-03528: chesscom.explanation_engine.v1.SetCoachRequest.locale = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string locale = 2;

### Evidence

- **SRC-0393** `research/proto/chesscom/explanation_engine/v1/feature_set_coach.proto` — [preserved redacted evidence](../evidence/text/63455c03d651d2e045c6f4d4745fe63ea5107811da27f27aeffced3e84ef5732.proto)
  Character offset 185.

```text
package chesscom.explanation_engine.v1;

message SetCoachRequest {
  optional string text_id = 1;
  optional string locale = 2;
}

message SetCoachResponse {
}

```

**Source references:** SRC-0393, SRC-1364  
**URL references:** None independently associated  
**Related findings:** FND-03526, FND-03527

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03529"></a>
## FND-03529: message declaration: chesscom.explanation_engine.v1.SetCoachResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCoachResponse {

### Evidence

- **SRC-0393** `research/proto/chesscom/explanation_engine/v1/feature_set_coach.proto` — [preserved redacted evidence](../evidence/text/63455c03d651d2e045c6f4d4745fe63ea5107811da27f27aeffced3e84ef5732.proto)
  Character offset 216.

```text
gine.v1;

message SetCoachRequest {
  optional string text_id = 1;
  optional string locale = 2;
}

message SetCoachResponse {
}

```

**Source references:** SRC-0393, SRC-1364  
**URL references:** None independently associated  
**Related findings:** FND-03526, FND-03527, FND-03528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03530"></a>
## FND-03530: message declaration: chesscom.explanation_engine.v1.SetGameResultRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetGameResultRequest {

### Evidence

- **SRC-0394** `research/proto/chesscom/explanation_engine/v1/feature_set_game_result.proto` — [preserved redacted evidence](../evidence/text/028d19ae8cdcae7971bd900a43cf49eb59663575aedf2fa55de4e41ca6ac15c2.proto)
  Character offset 132.

```text
engine/v1/feature_set_game_result.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SetGameResultRequest {
  optional .chesscom.chess.v1.GameResult claimed_game_result = 1;
}

message SetGameResultResponse {
}

```

**Source references:** SRC-0394, SRC-1365  
**URL references:** None independently associated  
**Related findings:** FND-03531, FND-03532

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03531"></a>
## FND-03531: chesscom.explanation_engine.v1.SetGameResultRequest.claimed_game_result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GameResult claimed_game_result = 1;

### Evidence

- **SRC-0394** `research/proto/chesscom/explanation_engine/v1/feature_set_game_result.proto` — [preserved redacted evidence](../evidence/text/028d19ae8cdcae7971bd900a43cf49eb59663575aedf2fa55de4e41ca6ac15c2.proto)
  Character offset 165.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SetGameResultRequest {
  optional .chesscom.chess.v1.GameResult claimed_game_result = 1;
}

message SetGameResultResponse {
}

```

**Source references:** SRC-0394, SRC-1365  
**URL references:** None independently associated  
**Related findings:** FND-03530, FND-03532

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03532"></a>
## FND-03532: message declaration: chesscom.explanation_engine.v1.SetGameResultResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetGameResultResponse {

### Evidence

- **SRC-0394** `research/proto/chesscom/explanation_engine/v1/feature_set_game_result.proto` — [preserved redacted evidence](../evidence/text/028d19ae8cdcae7971bd900a43cf49eb59663575aedf2fa55de4e41ca6ac15c2.proto)
  Character offset 232.

```text
message SetGameResultRequest {
  optional .chesscom.chess.v1.GameResult claimed_game_result = 1;
}

message SetGameResultResponse {
}

```

**Source references:** SRC-0394, SRC-1365  
**URL references:** None independently associated  
**Related findings:** FND-03530, FND-03531

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03533"></a>
## FND-03533: message declaration: chesscom.explanation_engine.v1.SetPlayedLineRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetPlayedLineRequest {

### Evidence

- **SRC-0395** `research/proto/chesscom/explanation_engine/v1/feature_set_played_line.proto` — [preserved redacted evidence](../evidence/text/55d1d32e6a3364acf12de70830829210e2e9da7109df04edfd86e5967dcb9d89.proto)
  Character offset 132.

```text
engine/v1/feature_set_played_line.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SetPlayedLineRequest {
}

message SetPlayedLineResponse {
}

```

**Source references:** SRC-0395, SRC-1366  
**URL references:** None independently associated  
**Related findings:** FND-03534

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03534"></a>
## FND-03534: message declaration: chesscom.explanation_engine.v1.SetPlayedLineResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetPlayedLineResponse {

### Evidence

- **SRC-0395** `research/proto/chesscom/explanation_engine/v1/feature_set_played_line.proto` — [preserved redacted evidence](../evidence/text/55d1d32e6a3364acf12de70830829210e2e9da7109df04edfd86e5967dcb9d89.proto)
  Character offset 166.

```text
proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SetPlayedLineRequest {
}

message SetPlayedLineResponse {
}

```

**Source references:** SRC-0395, SRC-1366  
**URL references:** None independently associated  
**Related findings:** FND-03533

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03535"></a>
## FND-03535: message declaration: chesscom.explanation_engine.v1.SimpleThreatsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SimpleThreatsRequest {

### Evidence

- **SRC-0396** `research/proto/chesscom/explanation_engine/v1/feature_simple_threats.proto` — [preserved redacted evidence](../evidence/text/5ce265eef8d623ed2dfb5b40d2cddf463368427521c85d7391938894cedd122d.proto)
  Character offset 131.

```text
_engine/v1/feature_simple_threats.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SimpleThreatsRequest {
  optional int32 threats_limit = 1;
}

message SimpleThreatsResponse {
  repeated .chesscom.explanation_engine.v1.SimpleThreat threats = 1;
}

```

**Source references:** SRC-0396, SRC-1367  
**URL references:** None independently associated  
**Related findings:** FND-03536, FND-03537

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03536"></a>
## FND-03536: chesscom.explanation_engine.v1.SimpleThreatsRequest.threats_limit = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 threats_limit = 1;

### Evidence

- **SRC-0396** `research/proto/chesscom/explanation_engine/v1/feature_simple_threats.proto` — [preserved redacted evidence](../evidence/text/5ce265eef8d623ed2dfb5b40d2cddf463368427521c85d7391938894cedd122d.proto)
  Character offset 164.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SimpleThreatsRequest {
  optional int32 threats_limit = 1;
}

message SimpleThreatsResponse {
  repeated .chesscom.explanation_engine.v1.SimpleThreat threats = 1;
}

```

**Source references:** SRC-0396, SRC-1367  
**URL references:** None independently associated  
**Related findings:** FND-03535, FND-03537

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03537"></a>
## FND-03537: message declaration: chesscom.explanation_engine.v1.SimpleThreatsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SimpleThreatsResponse {

### Evidence

- **SRC-0396** `research/proto/chesscom/explanation_engine/v1/feature_simple_threats.proto` — [preserved redacted evidence](../evidence/text/5ce265eef8d623ed2dfb5b40d2cddf463368427521c85d7391938894cedd122d.proto)
  Character offset 201.

```text
sscom.explanation_engine.v1;

message SimpleThreatsRequest {
  optional int32 threats_limit = 1;
}

message SimpleThreatsResponse {
  repeated .chesscom.explanation_engine.v1.SimpleThreat threats = 1;
}

```

**Source references:** SRC-0396, SRC-1367  
**URL references:** None independently associated  
**Related findings:** FND-03535, FND-03536

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03538"></a>
## FND-03538: chesscom.explanation_engine.v1.SimpleThreatsResponse.threats = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SimpleThreat threats = 1;

### Evidence

- **SRC-0396** `research/proto/chesscom/explanation_engine/v1/feature_simple_threats.proto` — [preserved redacted evidence](../evidence/text/5ce265eef8d623ed2dfb5b40d2cddf463368427521c85d7391938894cedd122d.proto)
  Character offset 235.

```text
age SimpleThreatsRequest {
  optional int32 threats_limit = 1;
}

message SimpleThreatsResponse {
  repeated .chesscom.explanation_engine.v1.SimpleThreat threats = 1;
}

```

**Source references:** SRC-0396, SRC-1367  
**URL references:** None independently associated  
**Related findings:** FND-03535, FND-03536, FND-03537

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03539"></a>
## FND-03539: message declaration: chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateExperimentalOptionsRequest {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 144.

```text
ature_update_experimental_options.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message UpdateExperimentalOptionsRequest {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message UpdateExperimentalOptionsResponse {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bo
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03540, FND-03541

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03540"></a>
## FND-03540: chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest.options = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 189.

```text
ntax: proto3

package chesscom.explanation_engine.v1;

message UpdateExperimentalOptionsRequest {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message UpdateExperimentalOptionsResponse {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  o
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03541"></a>
## FND-03541: message declaration: chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateExperimentalOptionsResponse {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 266.

```text
ntalOptionsRequest {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message UpdateExperimentalOptionsResponse {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enable
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03542"></a>
## FND-03542: chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse.options = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 189.

```text
ntax: proto3

package chesscom.explanation_engine.v1;

message UpdateExperimentalOptionsRequest {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message UpdateExperimentalOptionsResponse {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  o
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03543"></a>
## FND-03543: message declaration: chesscom.explanation_engine.v1.ExperimentalOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExperimentalOptions {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 389.

```text
talOptionsResponse {
  optional .chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_mo
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03544"></a>
## FND-03544: oneof declaration: chesscom.explanation_engine.v1.ExperimentalOptions._play_coach_flip_board_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_coach_flip_board_enabled {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 421.

```text
.chesscom.explanation_engine.v1.ExperimentalOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  o
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03545"></a>
## FND-03545: chesscom.explanation_engine.v1.ExperimentalOptions.play_coach_flip_board_enabled = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool play_coach_flip_board_enabled = 5;

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 462.

```text
talOptions options = 1;
}

message ExperimentalOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  boo
```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03546"></a>
## FND-03546: oneof declaration: chesscom.explanation_engine.v1.ExperimentalOptions._play_coach_retry_misses_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_coach_retry_misses_enabled {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 508.

```text
lOptions {
  oneof _play_coach_flip_board_enabled {
  bool play_coach_flip_board_enabled = 5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  bool allow_tricky_classification = 8;
  }
}

```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03547"></a>
## FND-03547: chesscom.explanation_engine.v1.ExperimentalOptions.play_coach_retry_misses_enabled = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool play_coach_retry_misses_enabled = 6;

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 551.

```text
nabled {
  bool play_coach_flip_board_enabled = 5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  bool allow_tricky_classification = 8;
  }
}

```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03548"></a>
## FND-03548: oneof declaration: chesscom.explanation_engine.v1.ExperimentalOptions._illegal_move_explanation_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _illegal_move_explanation_mode {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 599.

```text
5;
  }
  oneof _play_coach_retry_misses_enabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  bool allow_tricky_classification = 8;
  }
}

```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03549"></a>
## FND-03549: chesscom.explanation_engine.v1.ExperimentalOptions.illegal_move_explanation_mode = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 640.

```text
nabled {
  bool play_coach_retry_misses_enabled = 6;
  }
  oneof _illegal_move_explanation_mode {
  .chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  bool allow_tricky_classification = 8;
  }
}

```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03550"></a>
## FND-03550: oneof declaration: chesscom.explanation_engine.v1.ExperimentalOptions._allow_tricky_classification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _allow_tricky_classification {

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 740.

```text
.chesscom.explanation_engine.v1.IllegalMoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  bool allow_tricky_classification = 8;
  }
}

```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03551"></a>
## FND-03551: chesscom.explanation_engine.v1.ExperimentalOptions.allow_tricky_classification = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool allow_tricky_classification = 8;

### Evidence

- **SRC-0397** `research/proto/chesscom/explanation_engine/v1/feature_update_experimental_options.proto` — [preserved redacted evidence](../evidence/text/4a391fc01444fc3a96e2cc583ab91b4706bb542b3b7ee60fe719c052402dd22d.proto)
  Character offset 779.

```text
MoveExplanationMode illegal_move_explanation_mode = 7;
  }
  oneof _allow_tricky_classification {
  bool allow_tricky_classification = 8;
  }
}

```

**Source references:** SRC-0397, SRC-1368  
**URL references:** None independently associated  
**Related findings:** FND-03539, FND-03540, FND-03541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03552"></a>
## FND-03552: message declaration: chesscom.explanation_engine.v1.ValidateFenRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ValidateFenRequest {

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 129.

```text
on_engine/v1/feature_validate_fen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message ValidateFenRequest {
  optional string fen = 1;
  optional bool check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03553, FND-03554

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03553"></a>
## FND-03553: chesscom.explanation_engine.v1.ValidateFenRequest.fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 1;

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 160.

```text
en.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message ValidateFenRequest {
  optional string fen = 1;
  optional bool check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03554

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03554"></a>
## FND-03554: chesscom.explanation_engine.v1.ValidateFenRequest.check_syntax_only = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool check_syntax_only = 2;

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 187.

```text

package chesscom.explanation_engine.v1;

message ValidateFenRequest {
  optional string fen = 1;
  optional bool check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03553

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03555"></a>
## FND-03555: message declaration: chesscom.explanation_engine.v1.ValidateFenResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ValidateFenResponse {

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 227.

```text


message ValidateFenRequest {
  optional string fen = 1;
  optional bool check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03553, FND-03554

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03556"></a>
## FND-03556: oneof declaration: chesscom.explanation_engine.v1.ValidateFenResponse._error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _error {

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 259.

```text
 optional string fen = 1;
  optional bool check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03553, FND-03554

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03557"></a>
## FND-03557: chesscom.explanation_engine.v1.ValidateFenResponse.error = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string error = 1;

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 276.

```text
fen = 1;
  optional bool check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03553, FND-03554

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03558"></a>
## FND-03558: oneof declaration: chesscom.explanation_engine.v1.ValidateFenResponse._result_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result_type {

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 300.

```text
 check_syntax_only = 2;
}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03553, FND-03554

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03559"></a>
## FND-03559: chesscom.explanation_engine.v1.ValidateFenResponse.result_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.ResultType result_type = 2;

### Evidence

- **SRC-0398** `research/proto/chesscom/explanation_engine/v1/feature_validate_fen.proto` — [preserved redacted evidence](../evidence/text/3f7cc3a588fedf713ff16a33d218aee3470e5af4bdf9251eb8a78a670965dc6d.proto)
  Character offset 323.

```text

}

message ValidateFenResponse {
  oneof _error {
  string error = 1;
  }
  oneof _result_type {
  .chesscom.chess.v1.ResultType result_type = 2;
  }
}

```

**Source references:** SRC-0398, SRC-1369  
**URL references:** None independently associated  
**Related findings:** FND-03552, FND-03553, FND-03554

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03560"></a>
## FND-03560: message declaration: chesscom.explanation_engine.v1.ValidatePgnRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ValidatePgnRequest {

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 129.

```text
on_engine/v1/feature_validate_pgn.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message ValidatePgnRequest {
  optional string pgn = 1;
  optional string artifact_id = 2;
}

message ValidatePgnResponse {
  repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess succ
```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03561, FND-03562

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03561"></a>
## FND-03561: chesscom.explanation_engine.v1.ValidatePgnRequest.pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn = 1;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 160.

```text
gn.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message ValidatePgnRequest {
  optional string pgn = 1;
  optional string artifact_id = 2;
}

message ValidatePgnResponse {
  repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanatio
```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03562

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03562"></a>
## FND-03562: chesscom.explanation_engine.v1.ValidatePgnRequest.artifact_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string artifact_id = 2;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 187.

```text

package chesscom.explanation_engine.v1;

message ValidatePgnRequest {
  optional string pgn = 1;
  optional string artifact_id = 2;
}

message ValidatePgnResponse {
  repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidati
```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03563"></a>
## FND-03563: message declaration: chesscom.explanation_engine.v1.ValidatePgnResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ValidatePgnResponse {

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 223.

```text
.v1;

message ValidatePgnRequest {
  optional string pgn = 1;
  optional string artifact_id = 2;
}

message ValidatePgnResponse {
  repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message Pg
```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03564"></a>
## FND-03564: chesscom.explanation_engine.v1.ValidatePgnResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 255.

```text
 {
  optional string pgn = 1;
  optional string artifact_id = 2;
}

message ValidatePgnResponse {
  repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optio
```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03565"></a>
## FND-03565: message declaration: chesscom.explanation_engine.v1.PgnGameValidationResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PgnGameValidationResult {

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 335.

```text
datePgnResponse {
  repeated .chesscom.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string e
```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03566"></a>
## FND-03566: oneof declaration: chesscom.explanation_engine.v1.PgnGameValidationResult.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 371.

```text
om.explanation_engine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03567"></a>
## FND-03567: chesscom.explanation_engine.v1.PgnGameValidationResult.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 388.

```text
gine.v1.PgnGameValidationResult result = 1;
}

message PgnGameValidationResult {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03568"></a>
## FND-03568: chesscom.explanation_engine.v1.PgnGameValidationResult.error = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PgnGameValidationError error = 2;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 460.

```text
Result {
  oneof result {
  .chesscom.explanation_engine.v1.PgnGameValidationSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03569"></a>
## FND-03569: message declaration: chesscom.explanation_engine.v1.PgnGameValidationSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PgnGameValidationSuccess {

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 533.

```text
tionSuccess success = 1;
  .chesscom.explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03570"></a>
## FND-03570: chesscom.explanation_engine.v1.PgnGameValidationSuccess.game_pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_pgn = 1;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 570.

```text
explanation_engine.v1.PgnGameValidationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03571"></a>
## FND-03571: message declaration: chesscom.explanation_engine.v1.PgnGameValidationError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PgnGameValidationError {

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 603.

```text
dationError error = 2;
  }
}

message PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03572"></a>
## FND-03572: chesscom.explanation_engine.v1.PgnGameValidationError.error = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string error = 1;

### Evidence

- **SRC-0399** `research/proto/chesscom/explanation_engine/v1/feature_validate_pgn.proto` — [preserved redacted evidence](../evidence/text/ead7f53d78977492d0e620515975929f9615f6cf94eafb6a986dd19aa818e998.proto)
  Character offset 638.

```text
ge PgnGameValidationSuccess {
  optional string game_pgn = 1;
}

message PgnGameValidationError {
  optional string error = 1;
}

```

**Source references:** SRC-0399, SRC-1370  
**URL references:** None independently associated  
**Related findings:** FND-03560, FND-03561, FND-03562

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03573"></a>
## FND-03573: enum declaration: chesscom.explanation_engine.v1.FeatureId

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FeatureId {

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 117.

```text
om/explanation_engine/v1/features.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum FeatureId {
  FEATURE_ID_UNSPECIFIED = 0;
  FEATURE_ID_ADD_EVALUATIONS = 1;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  F
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03574"></a>
## FND-03574: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_UNSPECIFIED = 0;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 136.

```text
ne/v1/features.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum FeatureId {
  FEATURE_ID_UNSPECIFIED = 0;
  FEATURE_ID_ADD_EVALUATIONS = 1;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_M
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
