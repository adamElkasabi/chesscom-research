# data_models — findings 2901–3000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03175"></a>
## FND-03175: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest.move_notation = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.MoveNotation move_notation = 1;

### Evidence

- **SRC-0358** `research/proto/chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto` — [preserved redacted evidence](../evidence/text/23087ab03f9ab25f8931091685a44a4f62451b459d4b3de63d25d237990630a6.proto)
  Character offset 178.

```text

// syntax: proto3

package chesscom.explanation_engine.v1;

message ConvertToProtoMovesRequest {
  optional .chesscom.chess.v1.MoveNotation move_notation = 1;
  optional string initial_fen = 2;
  repeated string moves_to_convert = 3;
}

message ConvertToProtoMovesResponse {
  repeated .chesscom.chess.v1.Move moves = 1;
}

```

**Source references:** SRC-0358, SRC-1329  
**URL references:** None independently associated  
**Related findings:** FND-03174, FND-03176

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03176"></a>
## FND-03176: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest.initial_fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string initial_fen = 2;

### Evidence

- **SRC-0358** `research/proto/chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto` — [preserved redacted evidence](../evidence/text/23087ab03f9ab25f8931091685a44a4f62451b459d4b3de63d25d237990630a6.proto)
  Character offset 240.

```text
essage ConvertToProtoMovesRequest {
  optional .chesscom.chess.v1.MoveNotation move_notation = 1;
  optional string initial_fen = 2;
  repeated string moves_to_convert = 3;
}

message ConvertToProtoMovesResponse {
  repeated .chesscom.chess.v1.Move moves = 1;
}

```

**Source references:** SRC-0358, SRC-1329  
**URL references:** None independently associated  
**Related findings:** FND-03174, FND-03175

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03177"></a>
## FND-03177: chesscom.explanation_engine.v1.ConvertToProtoMovesRequest.moves_to_convert = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string moves_to_convert = 3;

### Evidence

- **SRC-0358** `research/proto/chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto` — [preserved redacted evidence](../evidence/text/23087ab03f9ab25f8931091685a44a4f62451b459d4b3de63d25d237990630a6.proto)
  Character offset 275.

```text

  optional .chesscom.chess.v1.MoveNotation move_notation = 1;
  optional string initial_fen = 2;
  repeated string moves_to_convert = 3;
}

message ConvertToProtoMovesResponse {
  repeated .chesscom.chess.v1.Move moves = 1;
}

```

**Source references:** SRC-0358, SRC-1329  
**URL references:** None independently associated  
**Related findings:** FND-03174, FND-03175, FND-03176

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03178"></a>
## FND-03178: message declaration: chesscom.explanation_engine.v1.ConvertToProtoMovesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ConvertToProtoMovesResponse {

### Evidence

- **SRC-0358** `research/proto/chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto` — [preserved redacted evidence](../evidence/text/23087ab03f9ab25f8931091685a44a4f62451b459d4b3de63d25d237990630a6.proto)
  Character offset 316.

```text
on move_notation = 1;
  optional string initial_fen = 2;
  repeated string moves_to_convert = 3;
}

message ConvertToProtoMovesResponse {
  repeated .chesscom.chess.v1.Move moves = 1;
}

```

**Source references:** SRC-0358, SRC-1329  
**URL references:** None independently associated  
**Related findings:** FND-03174, FND-03175, FND-03176

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03179"></a>
## FND-03179: chesscom.explanation_engine.v1.ConvertToProtoMovesResponse.moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move moves = 1;

### Evidence

- **SRC-0358** `research/proto/chesscom/explanation_engine/v1/feature_convert_to_proto_moves.proto` — [preserved redacted evidence](../evidence/text/23087ab03f9ab25f8931091685a44a4f62451b459d4b3de63d25d237990630a6.proto)
  Character offset 356.

```text
initial_fen = 2;
  repeated string moves_to_convert = 3;
}

message ConvertToProtoMovesResponse {
  repeated .chesscom.chess.v1.Move moves = 1;
}

```

**Source references:** SRC-0358, SRC-1329  
**URL references:** None independently associated  
**Related findings:** FND-03174, FND-03175, FND-03176

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03180"></a>
## FND-03180: message declaration: chesscom.explanation_engine.v1.ExpectedPointsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExpectedPointsRequest {

### Evidence

- **SRC-0359** `research/proto/chesscom/explanation_engine/v1/feature_expected_points.proto` — [preserved redacted evidence](../evidence/text/ba03a8183a960c01c6f112eab943519ae2b62baf93393066e668e1c58342bad0.proto)
  Character offset 132.

```text
engine/v1/feature_expected_points.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message ExpectedPointsRequest {
}

message ExpectedPointsResponse {
  optional double expected_points = 1;
}

```

**Source references:** SRC-0359, SRC-1330  
**URL references:** None independently associated  
**Related findings:** FND-03181, FND-03182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03181"></a>
## FND-03181: message declaration: chesscom.explanation_engine.v1.ExpectedPointsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExpectedPointsResponse {

### Evidence

- **SRC-0359** `research/proto/chesscom/explanation_engine/v1/feature_expected_points.proto` — [preserved redacted evidence](../evidence/text/ba03a8183a960c01c6f112eab943519ae2b62baf93393066e668e1c58342bad0.proto)
  Character offset 167.

```text
roto
// syntax: proto3

package chesscom.explanation_engine.v1;

message ExpectedPointsRequest {
}

message ExpectedPointsResponse {
  optional double expected_points = 1;
}

```

**Source references:** SRC-0359, SRC-1330  
**URL references:** None independently associated  
**Related findings:** FND-03180, FND-03182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03182"></a>
## FND-03182: chesscom.explanation_engine.v1.ExpectedPointsResponse.expected_points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double expected_points = 1;

### Evidence

- **SRC-0359** `research/proto/chesscom/explanation_engine/v1/feature_expected_points.proto` — [preserved redacted evidence](../evidence/text/ba03a8183a960c01c6f112eab943519ae2b62baf93393066e668e1c58342bad0.proto)
  Character offset 202.

```text
sscom.explanation_engine.v1;

message ExpectedPointsRequest {
}

message ExpectedPointsResponse {
  optional double expected_points = 1;
}

```

**Source references:** SRC-0359, SRC-1330  
**URL references:** None independently associated  
**Related findings:** FND-03180, FND-03181

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03183"></a>
## FND-03183: message declaration: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePhaseTransitionsRequest {

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 139.

```text
v1/feature_game_phase_transitions.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GamePhaseTransitionsRequest {
  oneof _starting_game_point {
  int32 starting_game_point = 1;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions
```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03184, FND-03185

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03184"></a>
## FND-03184: oneof declaration: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest._starting_game_point

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _starting_game_point {

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 179.

```text
// syntax: proto3

package chesscom.explanation_engine.v1;

message GamePhaseTransitionsRequest {
  oneof _starting_game_point {
  int32 starting_game_point = 1;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;
}

```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03183, FND-03185

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03185"></a>
## FND-03185: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest.starting_game_point = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 starting_game_point = 1;

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 210.

```text
scom.explanation_engine.v1;

message GamePhaseTransitionsRequest {
  oneof _starting_game_point {
  int32 starting_game_point = 1;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;
}

```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03183, FND-03184

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03186"></a>
## FND-03186: oneof declaration: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest._game_phase_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_phase_version {

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 247.

```text
GamePhaseTransitionsRequest {
  oneof _starting_game_point {
  int32 starting_game_point = 1;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;
}

```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03183, FND-03184, FND-03185

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03187"></a>
## FND-03187: chesscom.explanation_engine.v1.GamePhaseTransitionsRequest.game_phase_version = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 277.

```text
  oneof _starting_game_point {
  int32 starting_game_point = 1;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;
}

```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03183, FND-03184, FND-03185

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03188"></a>
## FND-03188: message declaration: chesscom.explanation_engine.v1.GamePhaseTransitionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePhaseTransitionsResponse {

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 357.

```text
e_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;
}

```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03183, FND-03184, FND-03185

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03189"></a>
## FND-03189: chesscom.explanation_engine.v1.GamePhaseTransitionsResponse.game_phase_transition = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;

### Evidence

- **SRC-0360** `research/proto/chesscom/explanation_engine/v1/feature_game_phase_transitions.proto` — [preserved redacted evidence](../evidence/text/26cd74cc261f1c0818fb9616ac43da8f0bdd1f61e4a18214305fc95445bd3053.proto)
  Character offset 398.

```text
_engine.v1.GamePhaseVersion game_phase_version = 2;
  }
}

message GamePhaseTransitionsResponse {
  optional .chesscom.explanation_engine.v1.GamePhaseTransitions game_phase_transition = 1;
}

```

**Source references:** SRC-0360, SRC-1331  
**URL references:** None independently associated  
**Related findings:** FND-03183, FND-03184, FND-03185

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03190"></a>
## FND-03190: message declaration: chesscom.explanation_engine.v1.GamePointInfoRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePointInfoRequest {

### Evidence

- **SRC-0361** `research/proto/chesscom/explanation_engine/v1/feature_game_point_info.proto` — [preserved redacted evidence](../evidence/text/edb9de015eea3cf0d8e4bd7d75a9fc857d78ea40a6fe8efa66d4f0e12ca80812.proto)
  Character offset 132.

```text
engine/v1/feature_game_point_info.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GamePointInfoRequest {
}

message GamePointInfoResponse {
  optional .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;
}

```

**Source references:** SRC-0361, SRC-1332  
**URL references:** None independently associated  
**Related findings:** FND-03191, FND-03192

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03191"></a>
## FND-03191: message declaration: chesscom.explanation_engine.v1.GamePointInfoResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePointInfoResponse {

### Evidence

- **SRC-0361** `research/proto/chesscom/explanation_engine/v1/feature_game_point_info.proto` — [preserved redacted evidence](../evidence/text/edb9de015eea3cf0d8e4bd7d75a9fc857d78ea40a6fe8efa66d4f0e12ca80812.proto)
  Character offset 166.

```text
proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GamePointInfoRequest {
}

message GamePointInfoResponse {
  optional .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;
}

```

**Source references:** SRC-0361, SRC-1332  
**URL references:** None independently associated  
**Related findings:** FND-03190, FND-03192

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03192"></a>
## FND-03192: chesscom.explanation_engine.v1.GamePointInfoResponse.game_point_info = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;

### Evidence

- **SRC-0361** `research/proto/chesscom/explanation_engine/v1/feature_game_point_info.proto` — [preserved redacted evidence](../evidence/text/edb9de015eea3cf0d8e4bd7d75a9fc857d78ea40a6fe8efa66d4f0e12ca80812.proto)
  Character offset 200.

```text
hesscom.explanation_engine.v1;

message GamePointInfoRequest {
}

message GamePointInfoResponse {
  optional .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;
}

```

**Source references:** SRC-0361, SRC-1332  
**URL references:** None independently associated  
**Related findings:** FND-03190, FND-03191

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03193"></a>
## FND-03193: message declaration: chesscom.explanation_engine.v1.GameReviewRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewRequest {

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 128.

```text
ion_engine/v1/feature_game_review.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GameReviewRequest {
  oneof _stats {
  .chesscom.explanation_engine.v1.AdvancedStatsForGame stats = 1;
  }
  oneof _starting_game_point {
  int32 starting_game_point = 2;
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4
```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03194, FND-03195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03194"></a>
## FND-03194: oneof declaration: chesscom.explanation_engine.v1.GameReviewRequest._stats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats {

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 158.

```text
iew.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GameReviewRequest {
  oneof _stats {
  .chesscom.explanation_engine.v1.AdvancedStatsForGame stats = 1;
  }
  oneof _starting_game_point {
  int32 starting_game_point = 2;
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_l
```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03195"></a>
## FND-03195: chesscom.explanation_engine.v1.GameReviewRequest.stats = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.AdvancedStatsForGame stats = 1;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 175.

```text
ax: proto3

package chesscom.explanation_engine.v1;

message GameReviewRequest {
  oneof _stats {
  .chesscom.explanation_engine.v1.AdvancedStatsForGame stats = 1;
  }
  oneof _starting_game_point {
  int32 starting_game_point = 2;
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways =
```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03196"></a>
## FND-03196: oneof declaration: chesscom.explanation_engine.v1.GameReviewRequest._starting_game_point

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _starting_game_point {

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 245.

```text
wRequest {
  oneof _stats {
  .chesscom.explanation_engine.v1.AdvancedStatsForGame stats = 1;
  }
  oneof _starting_game_point {
  int32 starting_game_point = 2;
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional 
```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03197"></a>
## FND-03197: chesscom.explanation_engine.v1.GameReviewRequest.starting_game_point = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 starting_game_point = 2;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 276.

```text
chesscom.explanation_engine.v1.AdvancedStatsForGame stats = 1;
  }
  oneof _starting_game_point {
  int32 starting_game_point = 2;
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

messag
```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03198"></a>
## FND-03198: chesscom.explanation_engine.v1.GameReviewRequest.uci_options = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 313.

```text
edStatsForGame stats = 1;
  }
  oneof _starting_game_point {
  int32 starting_game_point = 2;
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .ch
```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03199"></a>
## FND-03199: chesscom.explanation_engine.v1.GameReviewRequest.include_train_takeaways = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool include_train_takeaways = 4;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 407.

```text
  }
  repeated .chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03200"></a>
## FND-03200: chesscom.explanation_engine.v1.GameReviewRequest.can_access_locked_takeaways = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool can_access_locked_takeaways = 5;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 452.

```text
1.GameReviewRequest.UciOptionsEntry uci_options = 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03201"></a>
## FND-03201: message declaration: chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UciOptionsEntry {

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 501.

```text
 3;
  optional bool include_train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03202"></a>
## FND-03202: chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 529.

```text
train_takeaways = 4;
  optional bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03203"></a>
## FND-03203: chesscom.explanation_engine.v1.GameReviewRequest.UciOptionsEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 556.

```text
onal bool can_access_locked_takeaways = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03204"></a>
## FND-03204: message declaration: chesscom.explanation_engine.v1.GameReviewResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewResponse {

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 590.

```text
ays = 5;
  message UciOptionsEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03205"></a>
## FND-03205: chesscom.explanation_engine.v1.GameReviewResponse.game_review = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameReview game_review = 1;

### Evidence

- **SRC-0362** `research/proto/chesscom/explanation_engine/v1/feature_game_review.proto` — [preserved redacted evidence](../evidence/text/4f46fda25a29135cb170c3cc1efd629cc0ddf5306bf68fbe6ea4005e23c6e6e5.proto)
  Character offset 621.

```text
try {
  optional string key = 1;
  optional string value = 2;
  }
}

message GameReviewResponse {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 1;
}

```

**Source references:** SRC-0362, SRC-1333  
**URL references:** None independently associated  
**Related findings:** FND-03193, FND-03194, FND-03195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03206"></a>
## FND-03206: message declaration: chesscom.explanation_engine.v1.GameTreeRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameTreeRequest {

### Evidence

- **SRC-0363** `research/proto/chesscom/explanation_engine/v1/feature_game_tree.proto` — [preserved redacted evidence](../evidence/text/224dbf6ff841190f463a47ccdef7e2529ec086aef3a5080fec5ee768eb7b83f8.proto)
  Character offset 126.

```text
ation_engine/v1/feature_game_tree.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GameTreeRequest {
}

message GameTreeResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;
}

```

**Source references:** SRC-0363, SRC-1334  
**URL references:** None independently associated  
**Related findings:** FND-03207, FND-03208

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03207"></a>
## FND-03207: message declaration: chesscom.explanation_engine.v1.GameTreeResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameTreeResponse {

### Evidence

- **SRC-0363** `research/proto/chesscom/explanation_engine/v1/feature_game_tree.proto` — [preserved redacted evidence](../evidence/text/224dbf6ff841190f463a47ccdef7e2529ec086aef3a5080fec5ee768eb7b83f8.proto)
  Character offset 155.

```text
tree.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GameTreeRequest {
}

message GameTreeResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;
}

```

**Source references:** SRC-0363, SRC-1334  
**URL references:** None independently associated  
**Related findings:** FND-03206, FND-03208

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03208"></a>
## FND-03208: chesscom.explanation_engine.v1.GameTreeResponse.game_point_info = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;

### Evidence

- **SRC-0363** `research/proto/chesscom/explanation_engine/v1/feature_game_tree.proto` — [preserved redacted evidence](../evidence/text/224dbf6ff841190f463a47ccdef7e2529ec086aef3a5080fec5ee768eb7b83f8.proto)
  Character offset 184.

```text

package chesscom.explanation_engine.v1;

message GameTreeRequest {
}

message GameTreeResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo game_point_info = 1;
}

```

**Source references:** SRC-0363, SRC-1334  
**URL references:** None independently associated  
**Related findings:** FND-03206, FND-03207

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03209"></a>
## FND-03209: message declaration: chesscom.explanation_engine.v1.GetBotChatRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetBotChatRequest {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 129.

```text
on_engine/v1/feature_get_bot_chat.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetBotChatRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03210"></a>
## FND-03210: oneof declaration: chesscom.explanation_engine.v1.GetBotChatRequest._move_notation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_notation {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 159.

```text
hat.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetBotChatRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03211"></a>
## FND-03211: chesscom.explanation_engine.v1.GetBotChatRequest.move_notation = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.MoveNotation move_notation = 2;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 184.

```text
o3

package chesscom.explanation_engine.v1;

message GetBotChatRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  s
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03212"></a>
## FND-03212: oneof declaration: chesscom.explanation_engine.v1.GetBotChatRequest._request_hint

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _request_hint {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 241.

```text
otChatRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.e
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03213"></a>
## FND-03213: chesscom.explanation_engine.v1.GetBotChatRequest.request_hint = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool request_hint = 3;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 265.

```text
_move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.Bot
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03214"></a>
## FND-03214: oneof declaration: chesscom.explanation_engine.v1.GetBotChatRequest._json

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _json {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 294.

```text
chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info 
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03215"></a>
## FND-03215: chesscom.explanation_engine.v1.GetBotChatRequest.json = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string json = 4;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 310.

```text
ation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optio
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03216"></a>
## FND-03216: chesscom.explanation_engine.v1.GetBotChatRequest.bot_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_name = 1;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 333.

```text
;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanati
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03217"></a>
## FND-03217: message declaration: chesscom.explanation_engine.v1.GetBotChatResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetBotChatResponse {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 366.

```text
ool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03218"></a>
## FND-03218: oneof declaration: chesscom.explanation_engine.v1.GetBotChatResponse._hinted_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _hinted_move {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 397.

```text
of _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03219"></a>
## FND-03219: chesscom.explanation_engine.v1.GetBotChatResponse.hinted_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 420.

```text
n = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03220"></a>
## FND-03220: oneof declaration: chesscom.explanation_engine.v1.GetBotChatResponse._json

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _json {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 294.

```text
chess.v1.MoveNotation move_notation = 2;
  }
  oneof _request_hint {
  bool request_hint = 3;
  }
  oneof _json {
  string json = 4;
  }
  optional string bot_name = 1;
}

message GetBotChatResponse {
  oneof _hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info 
```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03221"></a>
## FND-03221: chesscom.explanation_engine.v1.GetBotChatResponse.json = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string json = 3;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 503.

```text
_hinted_move {
  .chesscom.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03222"></a>
## FND-03222: oneof declaration: chesscom.explanation_engine.v1.GetBotChatResponse._trigger_info

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trigger_info {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 526.

```text
com.explanation_engine.v1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03223"></a>
## FND-03223: chesscom.explanation_engine.v1.GetBotChatResponse.trigger_info = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 550.

```text
1.MoveDetails hinted_move = 2;
  }
  oneof _json {
  string json = 3;
  }
  oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03224"></a>
## FND-03224: chesscom.explanation_engine.v1.GetBotChatResponse.speech = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 1;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 625.

```text
 oneof _trigger_info {
  .chesscom.explanation_engine.v1.BotChatTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03225"></a>
## FND-03225: message declaration: chesscom.explanation_engine.v1.BotChatTriggerInfo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotChatTriggerInfo {

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 688.

```text
tTriggerInfo trigger_info = 4;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03226"></a>
## FND-03226: chesscom.explanation_engine.v1.BotChatTriggerInfo.label = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string label = 1;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 719.

```text
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03227"></a>
## FND-03227: chesscom.explanation_engine.v1.BotChatTriggerInfo.alternative = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 alternative = 2;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 748.

```text
anation_engine.v1.Speech speech = 1;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03228"></a>
## FND-03228: chesscom.explanation_engine.v1.BotChatTriggerInfo.personality = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string personality = 3;

### Evidence

- **SRC-0364** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_chat.proto` — [preserved redacted evidence](../evidence/text/811620cefaedbeb2aa37d8dcb43e7a82512c105602b60372da7f23dea41b0b6c.proto)
  Character offset 783.

```text
;
}

message BotChatTriggerInfo {
  optional string label = 1;
  optional uint32 alternative = 2;
  optional string personality = 3;
}

```

**Source references:** SRC-0364, SRC-1335  
**URL references:** None independently associated  
**Related findings:** FND-03209, FND-03210, FND-03211

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03229"></a>
## FND-03229: message declaration: chesscom.explanation_engine.v1.GetBotMoveRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetBotMoveRequest {

### Evidence

- **SRC-0365** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_move.proto` — [preserved redacted evidence](../evidence/text/848b46110957a8a5d4c8887e7b5a6981d581d75cdd9883201dcb515d3ee84d16.proto)
  Character offset 129.

```text
on_engine/v1/feature_get_bot_move.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetBotMoveRequest {
  optional .chesscom.explanation_engine.v1.BotOptions options = 2;
  optional .chesscom.explanation_engine.v1.BotEngine engine = 1;
}

message GetBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0365, SRC-1336  
**URL references:** None independently associated  
**Related findings:** FND-03230, FND-03231

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03230"></a>
## FND-03230: chesscom.explanation_engine.v1.GetBotMoveRequest.options = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotOptions options = 2;

### Evidence

- **SRC-0365** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_move.proto` — [preserved redacted evidence](../evidence/text/848b46110957a8a5d4c8887e7b5a6981d581d75cdd9883201dcb515d3ee84d16.proto)
  Character offset 159.

```text
ove.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetBotMoveRequest {
  optional .chesscom.explanation_engine.v1.BotOptions options = 2;
  optional .chesscom.explanation_engine.v1.BotEngine engine = 1;
}

message GetBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0365, SRC-1336  
**URL references:** None independently associated  
**Related findings:** FND-03229, FND-03231

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03231"></a>
## FND-03231: chesscom.explanation_engine.v1.GetBotMoveRequest.engine = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotEngine engine = 1;

### Evidence

- **SRC-0365** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_move.proto` — [preserved redacted evidence](../evidence/text/848b46110957a8a5d4c8887e7b5a6981d581d75cdd9883201dcb515d3ee84d16.proto)
  Character offset 226.

```text
;

message GetBotMoveRequest {
  optional .chesscom.explanation_engine.v1.BotOptions options = 2;
  optional .chesscom.explanation_engine.v1.BotEngine engine = 1;
}

message GetBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0365, SRC-1336  
**URL references:** None independently associated  
**Related findings:** FND-03229, FND-03230

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03232"></a>
## FND-03232: message declaration: chesscom.explanation_engine.v1.GetBotMoveResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetBotMoveResponse {

### Evidence

- **SRC-0365** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_move.proto` — [preserved redacted evidence](../evidence/text/848b46110957a8a5d4c8887e7b5a6981d581d75cdd9883201dcb515d3ee84d16.proto)
  Character offset 292.

```text
gine.v1.BotOptions options = 2;
  optional .chesscom.explanation_engine.v1.BotEngine engine = 1;
}

message GetBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0365, SRC-1336  
**URL references:** None independently associated  
**Related findings:** FND-03229, FND-03230, FND-03231

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03233"></a>
## FND-03233: chesscom.explanation_engine.v1.GetBotMoveResponse.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0365** `research/proto/chesscom/explanation_engine/v1/feature_get_bot_move.proto` — [preserved redacted evidence](../evidence/text/848b46110957a8a5d4c8887e7b5a6981d581d75cdd9883201dcb515d3ee84d16.proto)
  Character offset 323.

```text

  optional .chesscom.explanation_engine.v1.BotEngine engine = 1;
}

message GetBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0365, SRC-1336  
**URL references:** None independently associated  
**Related findings:** FND-03229, FND-03230, FND-03231

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03234"></a>
## FND-03234: message declaration: chesscom.explanation_engine.v1.GetCoachChatRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachChatRequest {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 131.

```text
_engine/v1/feature_get_coach_chat.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetCoachChatRequest {
}

message GetCoachChatResponse {
  oneof _debug_info {
  .chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03235"></a>
## FND-03235: message declaration: chesscom.explanation_engine.v1.GetCoachChatResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachChatResponse {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 164.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetCoachChatRequest {
}

message GetCoachChatResponse {
  oneof _debug_info {
  .chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mist
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03236"></a>
## FND-03236: oneof declaration: chesscom.explanation_engine.v1.GetCoachChatResponse._debug_info

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _debug_info {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 197.

```text
 chesscom.explanation_engine.v1;

message GetCoachChatRequest {
}

message GetCoachChatResponse {
  oneof _debug_info {
  .chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_eng
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03237"></a>
## FND-03237: chesscom.explanation_engine.v1.GetCoachChatResponse.debug_info = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 219.

```text
engine.v1;

message GetCoachChatRequest {
}

message GetCoachChatResponse {
  oneof _debug_info {
  .chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistak
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03238"></a>
## FND-03238: oneof declaration: chesscom.explanation_engine.v1.GetCoachChatResponse._speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _speech {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 292.

```text
 {
  oneof _debug_info {
  .chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explan
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03239"></a>
## FND-03239: chesscom.explanation_engine.v1.GetCoachChatResponse.speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Speech speech = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 310.

```text
info {
  .chesscom.explanation_engine.v1.CoachChatDebugInfo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.Co
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03240"></a>
## FND-03240: oneof declaration: chesscom.explanation_engine.v1.GetCoachChatResponse._retry_mistake

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _retry_mistake {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 367.

```text
fo debug_info = 1;
  }
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03241"></a>
## FND-03241: chesscom.explanation_engine.v1.GetCoachChatResponse.retry_mistake = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 392.

```text
oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_en
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03242"></a>
## FND-03242: oneof declaration: chesscom.explanation_engine.v1.GetCoachChatResponse._flip_board_mistake

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flip_board_mistake {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 462.

```text
 }
  oneof _retry_mistake {
  .chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03243"></a>
## FND-03243: chesscom.explanation_engine.v1.GetCoachChatResponse.flip_board_mistake = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 492.

```text
.chesscom.explanation_engine.v1.RetryMistake retry_mistake = 3;
  }
  oneof _flip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skil
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03244"></a>
## FND-03244: oneof declaration: chesscom.explanation_engine.v1.GetCoachChatResponse._coach_emotion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coach_emotion {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 571.

```text
ip_board_mistake {
  .chesscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engin
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03245"></a>
## FND-03245: chesscom.explanation_engine.v1.GetCoachChatResponse.coach_emotion = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 596.

```text
sscom.explanation_engine.v1.FlipBoardMistake flip_board_mistake = 4;
  }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03246"></a>
## FND-03246: oneof declaration: chesscom.explanation_engine.v1.GetCoachChatResponse._retry_miss

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _retry_miss {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 666.

```text
 }
  oneof _coach_emotion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;

```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03247"></a>
## FND-03247: chesscom.explanation_engine.v1.GetCoachChatResponse.retry_miss = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 688.

```text
ion {
  .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.e
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03248"></a>
## FND-03248: chesscom.explanation_engine.v1.GetCoachChatResponse.skills_earned = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 752.

```text
on = 6;
  }
  oneof _retry_miss {
  .chesscom.explanation_engine.v1.RetryMiss retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  opti
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03249"></a>
## FND-03249: message declaration: chesscom.explanation_engine.v1.RetryMistake

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RetryMistake {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 830.

```text
retry_miss = 7;
  }
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03250"></a>
## FND-03250: chesscom.explanation_engine.v1.RetryMistake.speech = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 855.

```text
ional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03251"></a>
## FND-03251: chesscom.explanation_engine.v1.RetryMistake.arrows_and_squares = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 917.

```text
rned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardM
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03252"></a>
## FND-03252: chesscom.explanation_engine.v1.RetryMistake.keep_playing_choice = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 988.

```text
gine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  opti
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03253"></a>
## FND-03253: chesscom.explanation_engine.v1.RetryMistake.retry_choice = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1068.

```text
_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional stri
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03254"></a>
## FND-03254: chesscom.explanation_engine.v1.RetryMistake.ply_until_cooldown = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 ply_until_cooldown = 5;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1141.

```text
keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech off
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03255"></a>
## FND-03255: chesscom.explanation_engine.v1.RetryMistake.board_event = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_event = 6;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1183.

```text
com.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;
  optional .chesscom.explan
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03256"></a>
## FND-03256: message declaration: chesscom.explanation_engine.v1.FlipBoardMistake

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FlipBoardMistake {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1219.

```text
e retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;
  optional .chesscom.explanation_engine.v1.CoachChoice switch_s
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03257"></a>
## FND-03257: chesscom.explanation_engine.v1.FlipBoardMistake.refutation_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move refutation_move = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1248.

```text
l uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;
  optional .chesscom.explanation_engine.v1.CoachChoice switch_sides_choice = 5;
  optional .
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03258"></a>
## FND-03258: chesscom.explanation_engine.v1.FlipBoardMistake.arrows_and_squares = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 917.

```text
rned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardM
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03259"></a>
## FND-03259: chesscom.explanation_engine.v1.FlipBoardMistake.board_event = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_event = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1375.

```text
.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;
  optional .chesscom.explanation_engine.v1.CoachChoice switch_sides_choice = 5;
  optional .chesscom.explanation_engine.v1.CoachChoice decline_choice = 6;
  optional .chesscom.explanation_engine.v1.Speech success_speech
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03260"></a>
## FND-03260: chesscom.explanation_engine.v1.FlipBoardMistake.offer_speech = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1410.

```text
al .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;
  optional .chesscom.explanation_engine.v1.CoachChoice switch_sides_choice = 5;
  optional .chesscom.explanation_engine.v1.CoachChoice decline_choice = 6;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 7;
  repeated .chesscom.explanat
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03261"></a>
## FND-03261: chesscom.explanation_engine.v1.FlipBoardMistake.switch_sides_choice = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice switch_sides_choice = 5;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1478.

```text
ional string board_event = 3;
  optional .chesscom.explanation_engine.v1.Speech offer_speech = 4;
  optional .chesscom.explanation_engine.v1.CoachChoice switch_sides_choice = 5;
  optional .chesscom.explanation_engine.v1.CoachChoice decline_choice = 6;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 7;
  repeated .chesscom.explanation_engine.v1.Speech failure_speech = 8;
  optional .chesscom.explan
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03262"></a>
## FND-03262: chesscom.explanation_engine.v1.FlipBoardMistake.decline_choice = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice decline_choice = 6;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1558.

```text
offer_speech = 4;
  optional .chesscom.explanation_engine.v1.CoachChoice switch_sides_choice = 5;
  optional .chesscom.explanation_engine.v1.CoachChoice decline_choice = 6;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 7;
  repeated .chesscom.explanation_engine.v1.Speech failure_speech = 8;
  optional .chesscom.explanation_engine.v1.Speech failure_almost_speech = 10;
  optional .chesscom.explanat
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03263"></a>
## FND-03263: chesscom.explanation_engine.v1.FlipBoardMistake.success_speech = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech success_speech = 7;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1633.

```text
itch_sides_choice = 5;
  optional .chesscom.explanation_engine.v1.CoachChoice decline_choice = 6;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 7;
  repeated .chesscom.explanation_engine.v1.Speech failure_speech = 8;
  optional .chesscom.explanation_engine.v1.Speech failure_almost_speech = 10;
  optional .chesscom.explanation_engine.v1.CoachChoice continue_after_flip_choice = 9;
}

message RetryM
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03264"></a>
## FND-03264: chesscom.explanation_engine.v1.FlipBoardMistake.failure_speech = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Speech failure_speech = 8;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1703.

```text
hChoice decline_choice = 6;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 7;
  repeated .chesscom.explanation_engine.v1.Speech failure_speech = 8;
  optional .chesscom.explanation_engine.v1.Speech failure_almost_speech = 10;
  optional .chesscom.explanation_engine.v1.CoachChoice continue_after_flip_choice = 9;
}

message RetryMiss {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03265"></a>
## FND-03265: chesscom.explanation_engine.v1.FlipBoardMistake.failure_almost_speech = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech failure_almost_speech = 10;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1773.

```text
.Speech success_speech = 7;
  repeated .chesscom.explanation_engine.v1.Speech failure_speech = 8;
  optional .chesscom.explanation_engine.v1.Speech failure_almost_speech = 10;
  optional .chesscom.explanation_engine.v1.CoachChoice continue_after_flip_choice = 9;
}

message RetryMiss {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03266"></a>
## FND-03266: chesscom.explanation_engine.v1.FlipBoardMistake.continue_after_flip_choice = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice continue_after_flip_choice = 9;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1851.

```text
failure_speech = 8;
  optional .chesscom.explanation_engine.v1.Speech failure_almost_speech = 10;
  optional .chesscom.explanation_engine.v1.CoachChoice continue_after_flip_choice = 9;
}

message RetryMiss {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03267"></a>
## FND-03267: message declaration: chesscom.explanation_engine.v1.RetryMiss

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RetryMiss {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1939.

```text
ech = 10;
  optional .chesscom.explanation_engine.v1.CoachChoice continue_after_flip_choice = 9;
}

message RetryMiss {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional str
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03268"></a>
## FND-03268: chesscom.explanation_engine.v1.RetryMiss.speech = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 855.

```text
ional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03269"></a>
## FND-03269: chesscom.explanation_engine.v1.RetryMiss.arrows_and_squares = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 917.

```text
rned = 5;
}

message RetryMistake {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardM
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03270"></a>
## FND-03270: chesscom.explanation_engine.v1.RetryMiss.keep_playing_choice = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 988.

```text
gine.v1.Speech speech = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  opti
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03271"></a>
## FND-03271: chesscom.explanation_engine.v1.RetryMiss.retry_choice = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 1068.

```text
_and_squares = 2;
  optional .chesscom.explanation_engine.v1.CoachChoice keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional uint32 ply_until_cooldown = 5;
  optional string board_event = 6;
}

message FlipBoardMistake {
  optional .chesscom.chess.v1.Move refutation_move = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
  optional stri
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03272"></a>
## FND-03272: chesscom.explanation_engine.v1.RetryMiss.board_event = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_event = 5;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2247.

```text
keep_playing_choice = 3;
  optional .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional string board_event = 5;
  repeated .chesscom.explanation_engine.v1.Speech attempt_speech = 6;
  optional .chesscom.explanation_engine.v1.Speech failure_speech = 7;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03273"></a>
## FND-03273: chesscom.explanation_engine.v1.RetryMiss.attempt_speech = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Speech attempt_speech = 6;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2282.

```text
 .chesscom.explanation_engine.v1.CoachChoice retry_choice = 4;
  optional string board_event = 5;
  repeated .chesscom.explanation_engine.v1.Speech attempt_speech = 6;
  optional .chesscom.explanation_engine.v1.Speech failure_speech = 7;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chess
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03274"></a>
## FND-03274: chesscom.explanation_engine.v1.RetryMiss.failure_speech = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech failure_speech = 7;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2352.

```text
nal string board_event = 5;
  repeated .chesscom.explanation_engine.v1.Speech attempt_speech = 6;
  optional .chesscom.explanation_engine.v1.Speech failure_speech = 7;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
