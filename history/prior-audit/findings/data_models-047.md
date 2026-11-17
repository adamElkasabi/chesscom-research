# data_models — findings 4601–4700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04875"></a>
## FND-04875: chesscom.friends_search.v1.GetFriendsCountResponse.friend_count = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 friend_count = 4;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 2192.

```text
message GetFriendsCountRequest {
  optional string uuid = 1;
}

message GetFriendsCountResponse {
  optional int32 friend_count = 4;
}

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04876"></a>
## FND-04876: message declaration: chesscom.game_gateway.v1.FavoriteMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FavoriteMetadata {

### Evidence

- **SRC-0442** `research/proto/chesscom/game_gateway/v1/favorite_metadata.proto` — [preserved redacted evidence](../evidence/text/d8bde2d29e2dcbf859cd0a7cad0fd869969f31251d0dde933f590f2c713bd671.proto)
  Character offset 114.

```text
sscom/game_gateway/v1/favorite_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message FavoriteMetadata {
  optional bool is_favorite = 1;
}

```

**Source references:** SRC-0442, SRC-1413  
**URL references:** None independently associated  
**Related findings:** FND-04877

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04877"></a>
## FND-04877: chesscom.game_gateway.v1.FavoriteMetadata.is_favorite = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_favorite = 1;

### Evidence

- **SRC-0442** `research/proto/chesscom/game_gateway/v1/favorite_metadata.proto` — [preserved redacted evidence](../evidence/text/d8bde2d29e2dcbf859cd0a7cad0fd869969f31251d0dde933f590f2c713bd671.proto)
  Character offset 143.

```text
e_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message FavoriteMetadata {
  optional bool is_favorite = 1;
}

```

**Source references:** SRC-0442, SRC-1413  
**URL references:** None independently associated  
**Related findings:** FND-04876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04878"></a>
## FND-04878: message declaration: chesscom.game_gateway.v1.GameAnalysisMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameAnalysisMetadata {

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 119.

```text
/game_gateway/v1/game_analysis_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message GameAnalysisMetadata {
  optional .chesscom.game_gateway.v1.AnalysisData white_player_metadata = 1;
  optional .chesscom.game_gateway.v1.AnalysisData black_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04879, FND-04880

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04879"></a>
## FND-04879: chesscom.game_gateway.v1.GameAnalysisMetadata.white_player_metadata = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.AnalysisData white_player_metadata = 1;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 152.

```text
tadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message GameAnalysisMetadata {
  optional .chesscom.game_gateway.v1.AnalysisData white_player_metadata = 1;
  optional .chesscom.game_gateway.v1.AnalysisData black_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04880"></a>
## FND-04880: chesscom.game_gateway.v1.GameAnalysisMetadata.black_player_metadata = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.AnalysisData black_player_metadata = 2;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 229.

```text
meAnalysisMetadata {
  optional .chesscom.game_gateway.v1.AnalysisData white_player_metadata = 1;
  optional .chesscom.game_gateway.v1.AnalysisData black_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_co
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04881"></a>
## FND-04881: message declaration: chesscom.game_gateway.v1.AnalysisData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AnalysisData {

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 307.

```text
layer_metadata = 1;
  optional .chesscom.game_gateway.v1.AnalysisData black_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassification
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04882"></a>
## FND-04882: oneof declaration: chesscom.game_gateway.v1.AnalysisData._accuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _accuracy {

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 332.

```text
ional .chesscom.game_gateway.v1.AnalysisData black_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classificat
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04883"></a>
## FND-04883: chesscom.game_gateway.v1.AnalysisData.accuracy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float accuracy = 3;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 352.

```text
_gateway.v1.AnalysisData black_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classification_counts_v2 = 4;
 
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04884"></a>
## FND-04884: chesscom.game_gateway.v1.AnalysisData.themes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 378.

```text
lack_player_metadata = 2;
}

message AnalysisData {
  oneof _accuracy {
  float accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classification_counts_v2 = 4;
  message MoveClassificatio
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04885"></a>
## FND-04885: chesscom.game_gateway.v1.AnalysisData.move_classification_counts = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 454.

```text
oat accuracy = 3;
  }
  repeated .chesscom.game_gateway.v1.AnalysisData.AnalysisTheme themes = 1;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classification_counts_v2 = 4;
  message MoveClassificationCounts {
  optional .chesscom.analysis.v1.MoveClassification move_classific
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04886"></a>
## FND-04886: chesscom.game_gateway.v1.AnalysisData.move_classification_counts_v2 = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classification_counts_v2 = 4;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 561.

```text
d .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts move_classification_counts = 2;
  repeated .chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classification_counts_v2 = 4;
  message MoveClassificationCounts {
  optional .chesscom.analysis.v1.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.ana
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04887"></a>
## FND-04887: message declaration: chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveClassificationCounts {

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 673.

```text
esscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2 move_classification_counts_v2 = 4;
  message MoveClassificationCounts {
  optional .chesscom.analysis.v1.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04888"></a>
## FND-04888: chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.analysis.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 710.

```text
oveClassificationCountsV2 move_classification_counts_v2 = 4;
  message MoveClassificationCounts {
  optional .chesscom.analysis.v1.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeat
```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04889"></a>
## FND-04889: chesscom.game_gateway.v1.AnalysisData.MoveClassificationCounts.count = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 count = 2;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 787.

```text
assificationCounts {
  optional .chesscom.analysis.v1.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04890"></a>
## FND-04890: message declaration: chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveClassificationCountsV2 {

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 820.

```text
chesscom.analysis.v1.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04891"></a>
## FND-04891: chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.analysis.v2.MoveClassification move_classification = 1;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 859.

```text
 move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04892"></a>
## FND-04892: chesscom.game_gateway.v1.AnalysisData.MoveClassificationCountsV2.count = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 count = 2;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 787.

```text
assificationCounts {
  optional .chesscom.analysis.v1.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message MoveClassificationCountsV2 {
  optional .chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04893"></a>
## FND-04893: message declaration: chesscom.game_gateway.v1.AnalysisData.AnalysisTheme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AnalysisTheme {

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 969.

```text
chesscom.analysis.v2.MoveClassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04894"></a>
## FND-04894: chesscom.game_gateway.v1.AnalysisData.AnalysisTheme.theme = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string theme = 1;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 995.

```text
lassification move_classification = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04895"></a>
## FND-04895: chesscom.game_gateway.v1.AnalysisData.AnalysisTheme.ply = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 ply = 2;

### Evidence

- **SRC-0443** `research/proto/chesscom/game_gateway/v1/game_analysis_metadata.proto` — [preserved redacted evidence](../evidence/text/ecadb14717ed8ae6eb11dd0dcf198e7a3735f82f43ed652e8820022979c7a06b.proto)
  Character offset 1024.

```text
tion = 1;
  optional uint32 count = 2;
  }
  message AnalysisTheme {
  optional string theme = 1;
  repeated uint32 ply = 2;
  }
}

```

**Source references:** SRC-0443, SRC-1414  
**URL references:** None independently associated  
**Related findings:** FND-04878, FND-04879, FND-04880

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04896"></a>
## FND-04896: message declaration: chesscom.game_gateway.v1.GameRelationshipMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameRelationshipMetadata {

### Evidence

- **SRC-0444** `research/proto/chesscom/game_gateway/v1/game_relationship_metadata.proto` — [preserved redacted evidence](../evidence/text/e824954750ad788de1294c6591bdd361614bf5b7cba743056f1da5b3833d0d4e.proto)
  Character offset 123.

```text
e_gateway/v1/game_relationship_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message GameRelationshipMetadata {
  optional bool are_friends = 1;
}

```

**Source references:** SRC-0444, SRC-1415  
**URL references:** None independently associated  
**Related findings:** FND-04897

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04897"></a>
## FND-04897: chesscom.game_gateway.v1.GameRelationshipMetadata.are_friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool are_friends = 1;

### Evidence

- **SRC-0444** `research/proto/chesscom/game_gateway/v1/game_relationship_metadata.proto` — [preserved redacted evidence](../evidence/text/e824954750ad788de1294c6591bdd361614bf5b7cba743056f1da5b3833d0d4e.proto)
  Character offset 160.

```text
ta.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message GameRelationshipMetadata {
  optional bool are_friends = 1;
}

```

**Source references:** SRC-0444, SRC-1415  
**URL references:** None independently associated  
**Related findings:** FND-04896

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04898"></a>
## FND-04898: message declaration: chesscom.game_gateway.v1.OpeningMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OpeningMetadata {

### Evidence

- **SRC-0445** `research/proto/chesscom/game_gateway/v1/opening_metadata.proto` — [preserved redacted evidence](../evidence/text/ebe823be50719d7e29331936eae622ceb3974f0c1e0a7147f87b8f479b2b3d1d.proto)
  Character offset 113.

```text
esscom/game_gateway/v1/opening_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message OpeningMetadata {
  optional string eco_family_name = 1;
}

```

**Source references:** SRC-0445, SRC-1416  
**URL references:** None independently associated  
**Related findings:** FND-04899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04899"></a>
## FND-04899: chesscom.game_gateway.v1.OpeningMetadata.eco_family_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string eco_family_name = 1;

### Evidence

- **SRC-0445** `research/proto/chesscom/game_gateway/v1/opening_metadata.proto` — [preserved redacted evidence](../evidence/text/ebe823be50719d7e29331936eae622ceb3974f0c1e0a7147f87b8f479b2b3d1d.proto)
  Character offset 141.

```text
ng_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message OpeningMetadata {
  optional string eco_family_name = 1;
}

```

**Source references:** SRC-0445, SRC-1416  
**URL references:** None independently associated  
**Related findings:** FND-04898

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04900"></a>
## FND-04900: message declaration: chesscom.game_gateway.v1.PgnMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PgnMetadata {

### Evidence

- **SRC-0446** `research/proto/chesscom/game_gateway/v1/pgn_metadata.proto` — [preserved redacted evidence](../evidence/text/87a76adba68331cce16a01b8cb6ffb2478a62aa7adab1f9332e3282012310136.proto)
  Character offset 109.

```text
: chesscom/game_gateway/v1/pgn_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message PgnMetadata {
  optional string pgn = 1;
}

```

**Source references:** SRC-0446, SRC-1417  
**URL references:** None independently associated  
**Related findings:** FND-04901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04901"></a>
## FND-04901: chesscom.game_gateway.v1.PgnMetadata.pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn = 1;

### Evidence

- **SRC-0446** `research/proto/chesscom/game_gateway/v1/pgn_metadata.proto` — [preserved redacted evidence](../evidence/text/87a76adba68331cce16a01b8cb6ffb2478a62aa7adab1f9332e3282012310136.proto)
  Character offset 133.

```text
v1/pgn_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message PgnMetadata {
  optional string pgn = 1;
}

```

**Source references:** SRC-0446, SRC-1417  
**URL references:** None independently associated  
**Related findings:** FND-04900

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04902"></a>
## FND-04902: message declaration: chesscom.game_gateway.v1.PlayerDetailsMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerDetailsMetadata {

### Evidence

- **SRC-0447** `research/proto/chesscom/game_gateway/v1/player_details_metadata.proto` — [preserved redacted evidence](../evidence/text/5b188b2c2c199fa21e191a0be188f195c4175b06dda6f1cea30cbabd821b6301.proto)
  Character offset 120.

```text
game_gateway/v1/player_details_metadata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message PlayerDetailsMetadata {
  optional .chesscom.user.v1.UserView white_player_metadata = 1;
  optional .chesscom.user.v1.UserView black_player_metadata = 2;
}

```

**Source references:** SRC-0447, SRC-1418  
**URL references:** None independently associated  
**Related findings:** FND-04903, FND-04904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04903"></a>
## FND-04903: chesscom.game_gateway.v1.PlayerDetailsMetadata.white_player_metadata = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user.v1.UserView white_player_metadata = 1;

### Evidence

- **SRC-0447** `research/proto/chesscom/game_gateway/v1/player_details_metadata.proto` — [preserved redacted evidence](../evidence/text/5b188b2c2c199fa21e191a0be188f195c4175b06dda6f1cea30cbabd821b6301.proto)
  Character offset 154.

```text
adata.proto
// syntax: proto3

package chesscom.game_gateway.v1;

message PlayerDetailsMetadata {
  optional .chesscom.user.v1.UserView white_player_metadata = 1;
  optional .chesscom.user.v1.UserView black_player_metadata = 2;
}

```

**Source references:** SRC-0447, SRC-1418  
**URL references:** None independently associated  
**Related findings:** FND-04902, FND-04904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04904"></a>
## FND-04904: chesscom.game_gateway.v1.PlayerDetailsMetadata.black_player_metadata = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user.v1.UserView black_player_metadata = 2;

### Evidence

- **SRC-0447** `research/proto/chesscom/game_gateway/v1/player_details_metadata.proto` — [preserved redacted evidence](../evidence/text/5b188b2c2c199fa21e191a0be188f195c4175b06dda6f1cea30cbabd821b6301.proto)
  Character offset 219.

```text

message PlayerDetailsMetadata {
  optional .chesscom.user.v1.UserView white_player_metadata = 1;
  optional .chesscom.user.v1.UserView black_player_metadata = 2;
}

```

**Source references:** SRC-0447, SRC-1418  
**URL references:** None independently associated  
**Related findings:** FND-04902, FND-04903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04905"></a>
## FND-04905: message declaration: chesscom.game_gateway.v2.BughouseGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BughouseGame {

### Evidence

- **SRC-0448** `research/proto/chesscom/game_gateway/v2/bughouse_game.proto` — [preserved redacted evidence](../evidence/text/4058b11938007459552a6cf71f23d6caf1e5cfd0373dd748ae3f66da71080686.proto)
  Character offset 110.

```text
 chesscom/game_gateway/v2/bughouse_game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message BughouseGame {
  optional .chesscom.game_gateway.v2.ChessGame first_board = 1;
  optional string second_game_key = 2;
}

```

**Source references:** SRC-0448, SRC-1419  
**URL references:** None independently associated  
**Related findings:** FND-04906, FND-04907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04906"></a>
## FND-04906: chesscom.game_gateway.v2.BughouseGame.first_board = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.ChessGame first_board = 1;

### Evidence

- **SRC-0448** `research/proto/chesscom/game_gateway/v2/bughouse_game.proto` — [preserved redacted evidence](../evidence/text/4058b11938007459552a6cf71f23d6caf1e5cfd0373dd748ae3f66da71080686.proto)
  Character offset 135.

```text
/bughouse_game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message BughouseGame {
  optional .chesscom.game_gateway.v2.ChessGame first_board = 1;
  optional string second_game_key = 2;
}

```

**Source references:** SRC-0448, SRC-1419  
**URL references:** None independently associated  
**Related findings:** FND-04905, FND-04907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04907"></a>
## FND-04907: chesscom.game_gateway.v2.BughouseGame.second_game_key = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string second_game_key = 2;

### Evidence

- **SRC-0448** `research/proto/chesscom/game_gateway/v2/bughouse_game.proto` — [preserved redacted evidence](../evidence/text/4058b11938007459552a6cf71f23d6caf1e5cfd0373dd748ae3f66da71080686.proto)
  Character offset 199.

```text
teway.v2;

message BughouseGame {
  optional .chesscom.game_gateway.v2.ChessGame first_board = 1;
  optional string second_game_key = 2;
}

```

**Source references:** SRC-0448, SRC-1419  
**URL references:** None independently associated  
**Related findings:** FND-04905, FND-04906

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04908"></a>
## FND-04908: message declaration: chesscom.game_gateway.v2.ChessGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ChessGame {

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 107.

```text
ce: chesscom/game_gateway/v2/chess_game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player bla
```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04909, FND-04910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04909"></a>
## FND-04909: oneof declaration: chesscom.game_gateway.v2.ChessGame._initial_fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_fen {

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 129.

```text
way/v2/chess_game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04910"></a>
## FND-04910: chesscom.game_gateway.v2.ChessGame.initial_fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string initial_fen = 1;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 152.

```text

// syntax: proto3

package chesscom.game_gateway.v2;

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04911"></a>
## FND-04911: chesscom.game_gateway.v2.ChessGame.final_fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string final_fen = 2;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 182.

```text
esscom.game_gateway.v2;

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909, FND-04910

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04912"></a>
## FND-04912: chesscom.game_gateway.v2.ChessGame.ply_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 ply_count = 3;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 215.

```text
ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909, FND-04910

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04913"></a>
## FND-04913: chesscom.game_gateway.v2.ChessGame.move_text = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string move_text = 4;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 248.

```text
{
  string initial_fen = 1;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909, FND-04910

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04914"></a>
## FND-04914: chesscom.game_gateway.v2.ChessGame.move_timestamps = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 move_timestamps = 5;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 281.

```text
 optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909, FND-04910

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04915"></a>
## FND-04915: chesscom.game_gateway.v2.ChessGame.white_player = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.Player white_player = 6;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 320.

```text
nal uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909, FND-04910

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04916"></a>
## FND-04916: chesscom.game_gateway.v2.ChessGame.black_player = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.Player black_player = 7;

### Evidence

- **SRC-0449** `research/proto/chesscom/game_gateway/v2/chess_game.proto` — [preserved redacted evidence](../evidence/text/49e61a93ff3917c310e4741635dfa77bed2a4bc38e0700a661f29f6dd4b71659.proto)
  Character offset 382.

```text
epeated uint32 move_timestamps = 5;
  optional .chesscom.game_gateway.v2.Player white_player = 6;
  optional .chesscom.game_gateway.v2.Player black_player = 7;
}

```

**Source references:** SRC-0449, SRC-1420  
**URL references:** None independently associated  
**Related findings:** FND-04908, FND-04909, FND-04910

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04917"></a>
## FND-04917: message declaration: chesscom.game_gateway.v2.Game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Game {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 101.

```text
/ source: chesscom/game_gateway/v2/game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message Game {
  oneof game {
  .chesscom.game_gateway.v2.ChessGame chess_game = 17;
  .chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04918"></a>
## FND-04918: oneof declaration: chesscom.game_gateway.v2.Game.game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof game {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 118.

```text
m/game_gateway/v2/game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message Game {
  oneof game {
  .chesscom.game_gateway.v2.ChessGame chess_game = 17;
  .chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04919"></a>
## FND-04919: chesscom.game_gateway.v2.Game.chess_game = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_gateway.v2.ChessGame chess_game = 17;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 133.

```text
v2/game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message Game {
  oneof game {
  .chesscom.game_gateway.v2.ChessGame chess_game = 17;
  .chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04920"></a>
## FND-04920: chesscom.game_gateway.v2.Game.bughouse_game = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 188.

```text
gateway.v2;

message Game {
  oneof game {
  .chesscom.game_gateway.v2.ChessGame chess_game = 17;
  .chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsC
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04921"></a>
## FND-04921: oneof declaration: chesscom.game_gateway.v2.Game._name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _name {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 253.

```text
ay.v2.ChessGame chess_game = 17;
  .chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04922"></a>
## FND-04922: chesscom.game_gateway.v2.Game.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string name = 2;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 269.

```text
chess_game = 17;
  .chesscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string re
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04923"></a>
## FND-04923: oneof declaration: chesscom.game_gateway.v2.Game._special_game_event

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _special_game_event {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 292.

```text
sscom.game_gateway.v2.BughouseGame bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  on
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04924"></a>
## FND-04924: chesscom.game_gateway.v2.Game.special_game_event = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 322.

```text
Game bughouse_game = 18;
  }
  oneof _name {
  string name = 2;
  }
  oneof _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .c
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04925"></a>
## FND-04925: oneof declaration: chesscom.game_gateway.v2.Game._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 396.

```text
f _special_game_event {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  opt
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04926"></a>
## FND-04926: chesscom.game_gateway.v2.Game.legacy_id = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint64 legacy_id = 19;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 417.

```text
 {
  .chesscom.game_storage.v2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04927"></a>
## FND-04927: oneof declaration: chesscom.game_gateway.v2.Game._vs_computer_game_data

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vs_computer_game_data {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 446.

```text
2.SpecialGameEvent special_game_event = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_st
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04928"></a>
## FND-04928: chesscom.game_gateway.v2.Game.vs_computer_game_data = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 479.

```text
vent = 15;
  }
  oneof _legacy_id {
  uint64 legacy_id = 19;
  }
  oneof _vs_computer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04929"></a>
## FND-04929: oneof declaration: chesscom.game_gateway.v2.Game._rematch_of

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rematch_of {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 558.

```text
mputer_game_data {
  .chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.pro
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04930"></a>
## FND-04930: chesscom.game_gateway.v2.Game.rematch_of = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string rematch_of = 21;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 580.

```text
chesscom.game_storage.v2.VsComputerGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp starte
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04931"></a>
## FND-04931: oneof declaration: chesscom.game_gateway.v2.Game._vs_coach_game_data

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vs_coach_game_data {

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 610.

```text
puterGameData vs_computer_game_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.p
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04932"></a>
## FND-04932: chesscom.game_gateway.v2.Game.vs_coach_game_data = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 640.

```text
_data = 20;
  }
  oneof _rematch_of {
  string rematch_of = 21;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04933"></a>
## FND-04933: chesscom.game_gateway.v2.Game.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 713.

```text
of _vs_coach_game_data {
  .chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional 
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04934"></a>
## FND-04934: chesscom.game_gateway.v2.Game.provider = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GameProvider provider = 3;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 740.

```text
.chesscom.game_storage.v2.VsCoachGameData vs_coach_game_data = 23;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClas
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04935"></a>
## FND-04935: chesscom.game_gateway.v2.Game.created_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 4;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 804.

```text
3;
  }
  optional string key = 1;
  optional .chesscom.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingCla
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04936"></a>
## FND-04936: chesscom.game_gateway.v2.Game.started_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp started_at = 5;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 858.

```text
.game_storage.v2.GameProvider provider = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Var
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04937"></a>
## FND-04937: chesscom.game_gateway.v2.Game.ended_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp ended_at = 6;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 912.

```text
 .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04938"></a>
## FND-04938: chesscom.game_gateway.v2.Game.time_control = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.TimeControl time_control = 7;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 964.

```text
al .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v2.GameResult result = 11;
  optional .chesscom.game_
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04939"></a>
## FND-04939: chesscom.game_gateway.v2.Game.time_class = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.TimeClass time_class = 8;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1024.

```text
ogle.protobuf.Timestamp ended_at = 6;
  optional .chesscom.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v2.GameResult result = 11;
  optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.ga
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04940"></a>
## FND-04940: chesscom.game_gateway.v2.Game.rating_class = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.RatingClass rating_class = 9;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1080.

```text
om.chess.v1.TimeControl time_control = 7;
  optional .chesscom.chess.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v2.GameResult result = 11;
  optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.game_storage.v2.GameOrigin origin = 13;
  optional .chessc
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04941"></a>
## FND-04941: chesscom.game_gateway.v2.Game.variant = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Variant variant = 10;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1147.

```text
s.v1.TimeClass time_class = 8;
  optional .chesscom.game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v2.GameResult result = 11;
  optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.game_storage.v2.GameOrigin origin = 13;
  optional .chesscom.game_storage.v2.GameServer game_server = 14;
  optional .chessco
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04942"></a>
## FND-04942: chesscom.game_gateway.v2.Game.result = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GameResult result = 11;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1199.

```text
game_storage.v2.RatingClass rating_class = 9;
  optional .chesscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v2.GameResult result = 11;
  optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.game_storage.v2.GameOrigin origin = 13;
  optional .chesscom.game_storage.v2.GameServer game_server = 14;
  optional .chesscom.game_storage.v2.TournamentData tournament_data = 1
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04943"></a>
## FND-04943: chesscom.game_gateway.v2.Game.privacy = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1260.

```text
sscom.chess.v1.Variant variant = 10;
  optional .chesscom.game_storage.v2.GameResult result = 11;
  optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.game_storage.v2.GameOrigin origin = 13;
  optional .chesscom.game_storage.v2.GameServer game_server = 14;
  optional .chesscom.game_storage.v2.TournamentData tournament_data = 16;
  optional .chesscom.game_storage.v2.OpeningData opening_d
```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04944"></a>
## FND-04944: chesscom.game_gateway.v2.Game.origin = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GameOrigin origin = 13;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1323.

```text
storage.v2.GameResult result = 11;
  optional .chesscom.game_storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.game_storage.v2.GameOrigin origin = 13;
  optional .chesscom.game_storage.v2.GameServer game_server = 14;
  optional .chesscom.game_storage.v2.TournamentData tournament_data = 16;
  optional .chesscom.game_storage.v2.OpeningData opening_data = 22;
}

```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04945"></a>
## FND-04945: chesscom.game_gateway.v2.Game.game_server = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GameServer game_server = 14;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1384.

```text
storage.v2.GamePrivacy privacy = 12;
  optional .chesscom.game_storage.v2.GameOrigin origin = 13;
  optional .chesscom.game_storage.v2.GameServer game_server = 14;
  optional .chesscom.game_storage.v2.TournamentData tournament_data = 16;
  optional .chesscom.game_storage.v2.OpeningData opening_data = 22;
}

```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04946"></a>
## FND-04946: chesscom.game_gateway.v2.Game.tournament_data = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.TournamentData tournament_data = 16;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1450.

```text
rage.v2.GameOrigin origin = 13;
  optional .chesscom.game_storage.v2.GameServer game_server = 14;
  optional .chesscom.game_storage.v2.TournamentData tournament_data = 16;
  optional .chesscom.game_storage.v2.OpeningData opening_data = 22;
}

```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04947"></a>
## FND-04947: chesscom.game_gateway.v2.Game.opening_data = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.OpeningData opening_data = 22;

### Evidence

- **SRC-0450** `research/proto/chesscom/game_gateway/v2/game.proto` — [preserved redacted evidence](../evidence/text/974995a43c26a9a355e0b7e154fe0cba493c7d4a9d67ad71eac231f4a15de995.proto)
  Character offset 1524.

```text
erver game_server = 14;
  optional .chesscom.game_storage.v2.TournamentData tournament_data = 16;
  optional .chesscom.game_storage.v2.OpeningData opening_data = 22;
}

```

**Source references:** SRC-0450, SRC-1421  
**URL references:** None independently associated  
**Related findings:** FND-04917, FND-04918, FND-04919

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04948"></a>
## FND-04948: enum declaration: chesscom.game_gateway.v2.SortDirection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SortDirection {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 117.

```text
om/game_gateway/v2/game_gateway_service.proto
// syntax: proto3

package chesscom.game_gateway.v2;

enum SortDirection {
  SORT_DIRECTION_UNSPECIFIED = 0;
  SORT_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRI
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04949"></a>
## FND-04949: chesscom.game_gateway.v2.SortDirection.SORT_DIRECTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_DIRECTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 140.

```text
_gateway_service.proto
// syntax: proto3

package chesscom.game_gateway.v2;

enum SortDirection {
  SORT_DIRECTION_UNSPECIFIED = 0;
  SORT_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04950"></a>
## FND-04950: chesscom.game_gateway.v2.SortDirection.SORT_DIRECTION_ASC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_DIRECTION_ASC = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 174.

```text
proto3

package chesscom.game_gateway.v2;

enum SortDirection {
  SORT_DIRECTION_UNSPECIFIED = 0;
  SORT_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_I
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04951"></a>
## FND-04951: chesscom.game_gateway.v2.SortDirection.SORT_DIRECTION_DESC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_DIRECTION_DESC = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 200.

```text
ame_gateway.v2;

enum SortDirection {
  SORT_DIRECTION_UNSPECIFIED = 0;
  SORT_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04952"></a>
## FND-04952: enum declaration: chesscom.game_gateway.v2.SortField

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SortField {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 228.

```text
rection {
  SORT_DIRECTION_UNSPECIFIED = 0;
  SORT_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_F
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04953"></a>
## FND-04953: chesscom.game_gateway.v2.SortField.SORT_FIELD_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_UNSPECIFIED = 0;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 247.

```text
RECTION_UNSPECIFIED = 0;
  SORT_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04954"></a>
## FND-04954: chesscom.game_gateway.v2.SortField.SORT_FIELD_USERNAME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_USERNAME = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 277.

```text
T_DIRECTION_ASC = 1;
  SORT_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04955"></a>
## FND-04955: chesscom.game_gateway.v2.SortField.SORT_FIELD_GAME_ID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_GAME_ID = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 304.

```text
_DIRECTION_DESC = 2;
}

enum SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04956"></a>
## FND-04956: chesscom.game_gateway.v2.SortField.SORT_FIELD_GAME_START_TIME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_GAME_START_TIME = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 330.

```text
um SortField {
  SORT_FIELD_UNSPECIFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04957"></a>
## FND-04957: chesscom.game_gateway.v2.SortField.SORT_FIELD_GAME_END_TIME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_GAME_END_TIME = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 364.

```text
IFIED = 0;
  SORT_FIELD_USERNAME = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04958"></a>
## FND-04958: chesscom.game_gateway.v2.SortField.SORT_FIELD_RATED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_RATED = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 396.

```text
 = 1;
  SORT_FIELD_GAME_ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04959"></a>
## FND-04959: chesscom.game_gateway.v2.SortField.SORT_FIELD_IS_PRIVATE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_IS_PRIVATE = 6;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 420.

```text
ID = 2;
  SORT_FIELD_GAME_START_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATI
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04960"></a>
## FND-04960: chesscom.game_gateway.v2.SortField.SORT_FIELD_BASE_TIME = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_BASE_TIME = 7;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 449.

```text
RT_TIME = 3;
  SORT_FIELD_GAME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONEN
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04961"></a>
## FND-04961: chesscom.game_gateway.v2.SortField.SORT_FIELD_TIME_INCREMENT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_TIME_INCREMENT = 8;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 477.

```text
ME_END_TIME = 4;
  SORT_FIELD_RATED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04962"></a>
## FND-04962: chesscom.game_gateway.v2.SortField.SORT_FIELD_PLAYER_RESULT = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_PLAYER_RESULT = 9;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 510.

```text
ED = 5;
  SORT_FIELD_IS_PRIVATE = 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04963"></a>
## FND-04963: chesscom.game_gateway.v2.SortField.SORT_FIELD_PLY_COUNT = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_PLY_COUNT = 10;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 542.

```text
= 6;
  SORT_FIELD_BASE_TIME = 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04964"></a>
## FND-04964: chesscom.game_gateway.v2.SortField.SORT_FIELD_GAME_TIME_CLASS = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_GAME_TIME_CLASS = 11;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 571.

```text
 7;
  SORT_FIELD_TIME_INCREMENT = 8;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_F
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04965"></a>
## FND-04965: chesscom.game_gateway.v2.SortField.SORT_FIELD_COLOR = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_COLOR = 12;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 606.

```text
;
  SORT_FIELD_PLAYER_RESULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04966"></a>
## FND-04966: chesscom.game_gateway.v2.SortField.SORT_FIELD_ARENA_ID = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_ARENA_ID = 13;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 631.

```text
ULT = 9;
  SORT_FIELD_PLY_COUNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04967"></a>
## FND-04967: chesscom.game_gateway.v2.SortField.SORT_FIELD_TOURNAMENT_ID = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_TOURNAMENT_ID = 14;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 659.

```text
UNT = 10;
  SORT_FIELD_GAME_TIME_CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04968"></a>
## FND-04968: chesscom.game_gateway.v2.SortField.SORT_FIELD_TEAM_MATCH_ID = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_TEAM_MATCH_ID = 15;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 692.

```text
CLASS = 11;
  SORT_FIELD_COLOR = 12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 2
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04969"></a>
## FND-04969: chesscom.game_gateway.v2.SortField.SORT_FIELD_RATING = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_RATING = 16;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 725.

```text
12;
  SORT_FIELD_ARENA_ID = 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SO
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04970"></a>
## FND-04970: chesscom.game_gateway.v2.SortField.SORT_FIELD_OPPONENT_RATING = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_OPPONENT_RATING = 17;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 751.

```text
= 13;
  SORT_FIELD_TOURNAMENT_ID = 14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04971"></a>
## FND-04971: chesscom.game_gateway.v2.SortField.SORT_FIELD_OPPONENT_TITLE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_OPPONENT_TITLE = 18;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 786.

```text
14;
  SORT_FIELD_TEAM_MATCH_ID = 15;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04972"></a>
## FND-04972: chesscom.game_gateway.v2.SortField.SORT_FIELD_OPPONENT_USERNAME = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_OPPONENT_USERNAME = 19;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 820.

```text
5;
  SORT_FIELD_RATING = 16;
  SORT_FIELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteria
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04973"></a>
## FND-04973: chesscom.game_gateway.v2.SortField.SORT_FIELD_ACCURACY = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_ACCURACY = 20;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 857.

```text
IELD_OPPONENT_RATING = 17;
  SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .ch
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04974"></a>
## FND-04974: chesscom.game_gateway.v2.SortField.SORT_FIELD_OPPONENT_ACCURACY = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_OPPONENT_ACCURACY = 21;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 885.

```text
 SORT_FIELD_OPPONENT_TITLE = 18;
  SORT_FIELD_OPPONENT_USERNAME = 19;
  SORT_FIELD_ACCURACY = 20;
  SORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPaginat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
