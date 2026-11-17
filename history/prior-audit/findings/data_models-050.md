# data_models — findings 4901–5000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05175"></a>
## FND-05175: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.field_mask = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 6;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8345.

```text
nal .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optional bool is_vs_computer = 5;
  optional .google.protobuf.FieldMask field_mask = 6;
  optional bool is_vs_coach = 7;
}

message HydrateGameByLegacyIdResponse {
  optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05176"></a>
## FND-05176: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.is_vs_coach = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_vs_coach = 7;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2335.

```text
id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach = 7;
}

message PlayerOverviewStatsResponse {
  oneof _daily_game_timeout_count {
  uint32 daily_game_timeout_count = 12;
  }
  oneof _best_win_opponent_username {
  string best_win_opponent_username = 13;
  }
  oneof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05177"></a>
## FND-05177: message declaration: chesscom.game_gateway.v2.HydrateGameByLegacyIdResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HydrateGameByLegacyIdResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8433.

```text
uter = 5;
  optional .google.protobuf.FieldMask field_mask = 6;
  optional bool is_vs_coach = 7;
}

message HydrateGameByLegacyIdResponse {
  optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

messag
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05178"></a>
## FND-05178: chesscom.game_gateway.v2.HydrateGameByLegacyIdResponse.hydrated_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8475.

```text
dMask field_mask = 6;
  optional bool is_vs_coach = 7;
}

message HydrateGameByLegacyIdResponse {
  optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  opt
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05179"></a>
## FND-05179: message declaration: chesscom.game_gateway.v2.OpeningCriteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OpeningCriteria {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8545.

```text
ateGameByLegacyIdResponse {
  optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  o
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05180"></a>
## FND-05180: oneof declaration: chesscom.game_gateway.v2.OpeningCriteria.criteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof criteria {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8573.

```text
  optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05181"></a>
## FND-05181: chesscom.game_gateway.v2.OpeningCriteria.eco_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 eco_id = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8592.

```text
m.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05182"></a>
## FND-05182: chesscom.game_gateway.v2.OpeningCriteria.eco_family_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 eco_family_id = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8613.

```text
ratedGame hydrated_game = 1;
}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05183"></a>
## FND-05183: chesscom.game_gateway.v2.OpeningCriteria.eco_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string eco_code = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8641.

```text

}

message OpeningCriteria {
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAl
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05184"></a>
## FND-05184: message declaration: chesscom.game_gateway.v2.CountTournamentsByPlayerRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CountTournamentsByPlayerRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8669.

```text
{
  oneof criteria {
  uint32 eco_id = 1;
  uint32 eco_family_id = 2;
  string eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05185"></a>
## FND-05185: chesscom.game_gateway.v2.CountTournamentsByPlayerRequest.player_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string player_id = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1686.

```text
f _aggregate_criteria {
  .chesscom.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;
  }
  optional string player_id = 1;
}

message AggregateGameResultsByPlayerAndCriteriaResponse {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05186"></a>
## FND-05186: message declaration: chesscom.game_gateway.v2.CountTournamentsByPlayerResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CountTournamentsByPlayerResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8747.

```text
 eco_code = 3;
  }
}

message CountTournamentsByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05187"></a>
## FND-05187: chesscom.game_gateway.v2.CountTournamentsByPlayerResponse.total = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 total = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8792.

```text
sByPlayerRequest {
  optional string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant varia
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05188"></a>
## FND-05188: message declaration: chesscom.game_gateway.v2.PlayerOverviewAllStatsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerOverviewAllStatsRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8822.

```text
string player_id = 1;
}

message CountTournamentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.c
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05189"></a>
## FND-05189: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewAllStatsRequest._days

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _days {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8864.

```text
namentsByPlayerResponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  option
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05190"></a>
## FND-05190: chesscom.game_gateway.v2.PlayerOverviewAllStatsRequest.days = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 days = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8880.

```text
esponse {
  optional uint32 total = 1;
}

message PlayerOverviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05191"></a>
## FND-05191: chesscom.game_gateway.v2.PlayerOverviewAllStatsRequest.player_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string player_id = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1686.

```text
f _aggregate_criteria {
  .chesscom.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;
  }
  optional string player_id = 1;
}

message AggregateGameResultsByPlayerAndCriteriaResponse {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05192"></a>
## FND-05192: message declaration: chesscom.game_gateway.v2.PlayerOverviewAllStatsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerOverviewAllStatsResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8937.

```text
verviewAllStatsRequest {
  oneof _days {
  uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05193"></a>
## FND-05193: chesscom.game_gateway.v2.PlayerOverviewAllStatsResponse.entries = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8980.

```text
uint32 days = 2;
  }
  optional string player_id = 1;
}

message PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05194"></a>
## FND-05194: message declaration: chesscom.game_gateway.v2.AllStatsEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AllStatsEntry {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 9045.

```text
PlayerOverviewAllStatsResponse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05195"></a>
## FND-05195: chesscom.game_gateway.v2.AllStatsEntry.variant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Variant variant = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 9071.

```text
onse {
  repeated .chesscom.game_gateway.v2.AllStatsEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05196"></a>
## FND-05196: chesscom.game_gateway.v2.AllStatsEntry.time_class = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.TimeClass time_class = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 9122.

```text
sEntry entries = 1;
}

message AllStatsEntry {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05197"></a>
## FND-05197: chesscom.game_gateway.v2.AllStatsEntry.rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 rating = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 9178.

```text
l .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05198"></a>
## FND-05198: chesscom.game_gateway.v2.AllStatsEntry.rating_change = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating_change = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 9208.

```text
ariant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05199"></a>
## FND-05199: chesscom.game_gateway.v2.AllStatsEntry.total_games = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 total_games = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 9244.

```text
ss.v1.TimeClass time_class = 2;
  optional uint32 rating = 3;
  optional int32 rating_change = 4;
  optional uint32 total_games = 5;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05200"></a>
## FND-05200: message declaration: chesscom.game_gateway.v2.HydratedGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HydratedGame {

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 110.

```text
 chesscom/game_gateway/v2/hydrated_game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message HydratedGame {
  optional .chesscom.game_gateway.v2.Game game = 1;
  optional .chesscom.cheat_metadata_storage.v1.GameCheatMetadata cheat_metadata = 2;
  optional .chesscom.game_gateway.v1.GameRelationshipMetadata relationship_metadata = 3;
  optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_meta
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05201, FND-05202

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05201"></a>
## FND-05201: chesscom.game_gateway.v2.HydratedGame.game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.Game game = 1;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 135.

```text
/hydrated_game.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message HydratedGame {
  optional .chesscom.game_gateway.v2.Game game = 1;
  optional .chesscom.cheat_metadata_storage.v1.GameCheatMetadata cheat_metadata = 2;
  optional .chesscom.game_gateway.v1.GameRelationshipMetadata relationship_metadata = 3;
  optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_metadata = 4;
  optional .che
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05202"></a>
## FND-05202: chesscom.game_gateway.v2.HydratedGame.cheat_metadata = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.cheat_metadata_storage.v1.GameCheatMetadata cheat_metadata = 2;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 187.

```text
scom.game_gateway.v2;

message HydratedGame {
  optional .chesscom.game_gateway.v2.Game game = 1;
  optional .chesscom.cheat_metadata_storage.v1.GameCheatMetadata cheat_metadata = 2;
  optional .chesscom.game_gateway.v1.GameRelationshipMetadata relationship_metadata = 3;
  optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_metadata = 4;
  optional .chesscom.game_gateway.v1.PlayerDetailsMetadata player_m
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05203"></a>
## FND-05203: chesscom.game_gateway.v2.HydratedGame.relationship_metadata = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.GameRelationshipMetadata relationship_metadata = 3;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 272.

```text
me game = 1;
  optional .chesscom.cheat_metadata_storage.v1.GameCheatMetadata cheat_metadata = 2;
  optional .chesscom.game_gateway.v1.GameRelationshipMetadata relationship_metadata = 3;
  optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_metadata = 4;
  optional .chesscom.game_gateway.v1.PlayerDetailsMetadata player_metadata = 5;
  optional .chesscom.game_gateway.v1.FavoriteMetadata favorite_metadata 
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05204"></a>
## FND-05204: chesscom.game_gateway.v2.HydratedGame.analysis_metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_metadata = 4;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 361.

```text
ata = 2;
  optional .chesscom.game_gateway.v1.GameRelationshipMetadata relationship_metadata = 3;
  optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_metadata = 4;
  optional .chesscom.game_gateway.v1.PlayerDetailsMetadata player_metadata = 5;
  optional .chesscom.game_gateway.v1.FavoriteMetadata favorite_metadata = 6;
  optional .chesscom.bots.v1.BotMetadata bot_metadata = 7;
  optional .chesscom.coac
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05205"></a>
## FND-05205: chesscom.game_gateway.v2.HydratedGame.player_metadata = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.PlayerDetailsMetadata player_metadata = 5;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 442.

```text
ip_metadata = 3;
  optional .chesscom.game_gateway.v1.GameAnalysisMetadata analysis_metadata = 4;
  optional .chesscom.game_gateway.v1.PlayerDetailsMetadata player_metadata = 5;
  optional .chesscom.game_gateway.v1.FavoriteMetadata favorite_metadata = 6;
  optional .chesscom.bots.v1.BotMetadata bot_metadata = 7;
  optional .chesscom.coaches.v2.Coach coach_metadata = 8;
  optional .chesscom.game_gateway.v1.OpeningMeta
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05206"></a>
## FND-05206: chesscom.game_gateway.v2.HydratedGame.favorite_metadata = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.FavoriteMetadata favorite_metadata = 6;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 522.

```text
sis_metadata = 4;
  optional .chesscom.game_gateway.v1.PlayerDetailsMetadata player_metadata = 5;
  optional .chesscom.game_gateway.v1.FavoriteMetadata favorite_metadata = 6;
  optional .chesscom.bots.v1.BotMetadata bot_metadata = 7;
  optional .chesscom.coaches.v2.Coach coach_metadata = 8;
  optional .chesscom.game_gateway.v1.OpeningMetadata opening_metadata = 9;
  optional .chesscom.game_gateway.v1.PgnMetadata pgn_
```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05207"></a>
## FND-05207: chesscom.game_gateway.v2.HydratedGame.bot_metadata = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotMetadata bot_metadata = 7;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 599.

```text
player_metadata = 5;
  optional .chesscom.game_gateway.v1.FavoriteMetadata favorite_metadata = 6;
  optional .chesscom.bots.v1.BotMetadata bot_metadata = 7;
  optional .chesscom.coaches.v2.Coach coach_metadata = 8;
  optional .chesscom.game_gateway.v1.OpeningMetadata opening_metadata = 9;
  optional .chesscom.game_gateway.v1.PgnMetadata pgn_metadata = 10;
}

```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05208"></a>
## FND-05208: chesscom.game_gateway.v2.HydratedGame.coach_metadata = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.Coach coach_metadata = 8;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 658.

```text
avoriteMetadata favorite_metadata = 6;
  optional .chesscom.bots.v1.BotMetadata bot_metadata = 7;
  optional .chesscom.coaches.v2.Coach coach_metadata = 8;
  optional .chesscom.game_gateway.v1.OpeningMetadata opening_metadata = 9;
  optional .chesscom.game_gateway.v1.PgnMetadata pgn_metadata = 10;
}

```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05209"></a>
## FND-05209: chesscom.game_gateway.v2.HydratedGame.opening_metadata = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.OpeningMetadata opening_metadata = 9;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 716.

```text
m.bots.v1.BotMetadata bot_metadata = 7;
  optional .chesscom.coaches.v2.Coach coach_metadata = 8;
  optional .chesscom.game_gateway.v1.OpeningMetadata opening_metadata = 9;
  optional .chesscom.game_gateway.v1.PgnMetadata pgn_metadata = 10;
}

```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05210"></a>
## FND-05210: chesscom.game_gateway.v2.HydratedGame.pgn_metadata = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v1.PgnMetadata pgn_metadata = 10;

### Evidence

- **SRC-0452** `research/proto/chesscom/game_gateway/v2/hydrated_game.proto` — [preserved redacted evidence](../evidence/text/f9f525d6ed937ab9b889621f7c6b2c538fb2ec5a20e8e4f14a8f0404903e7c53.proto)
  Character offset 791.

```text
ch coach_metadata = 8;
  optional .chesscom.game_gateway.v1.OpeningMetadata opening_metadata = 9;
  optional .chesscom.game_gateway.v1.PgnMetadata pgn_metadata = 10;
}

```

**Source references:** SRC-0452, SRC-1423  
**URL references:** None independently associated  
**Related findings:** FND-05200, FND-05201, FND-05202

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05211"></a>
## FND-05211: message declaration: chesscom.game_gateway.v2.Player

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Player {

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 103.

```text
source: chesscom/game_gateway/v2/player.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message Player {
  oneof _client {
  string client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storag
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05212, FND-05213

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05212"></a>
## FND-05212: oneof declaration: chesscom.game_gateway.v2.Player._client

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _client {

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 122.

```text
me_gateway/v2/player.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message Player {
  oneof _client {
  string client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType typ
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05213

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05213"></a>
## FND-05213: chesscom.game_gateway.v2.Player.client = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string client = 6;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 140.

```text
er.proto
// syntax: proto3

package chesscom.game_gateway.v2;

message Player {
  oneof _client {
  string client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional 
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05214"></a>
## FND-05214: oneof declaration: chesscom.game_gateway.v2.Player._rating_diff

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_diff {

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 165.

```text
3

package chesscom.game_gateway.v2;

message Player {
  oneof _client {
  string client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05215"></a>
## FND-05215: chesscom.game_gateway.v2.Player.rating_diff = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float rating_diff = 7;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 188.

```text
e_gateway.v2;

message Player {
  oneof _client {
  string client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provide
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05216"></a>
## FND-05216: oneof declaration: chesscom.game_gateway.v2.Player._dw_incident_logged

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _dw_incident_logged {

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 217.

```text
 {
  oneof _client {
  string client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key 
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05217"></a>
## FND-05217: chesscom.game_gateway.v2.Player.dw_incident_logged = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 dw_incident_logged = 8;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 247.

```text
client = 6;
  }
  oneof _rating_diff {
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_r
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05218"></a>
## FND-05218: oneof declaration: chesscom.game_gateway.v2.Player._bad_sport_behavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bad_sport_behavior {

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 284.

```text
{
  float rating_diff = 7;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05219"></a>
## FND-05219: chesscom.game_gateway.v2.Player.bad_sport_behavior = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 314.

```text

  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 8;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05220"></a>
## FND-05220: chesscom.game_gateway.v2.Player.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerType type = 1;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 393.

```text
d_sport_behavior {
  .chesscom.game_storage.v2.PlayerBadSportBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2
```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05221"></a>
## FND-05221: chesscom.game_gateway.v2.Player.provider = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerProvider provider = 2;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 451.

```text
ortBehavior bad_sport_behavior = 9;
  }
  optional .chesscom.game_storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2.PlayerTitle title = 11;
}

```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05222"></a>
## FND-05222: chesscom.game_gateway.v2.Player.key = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 3;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 517.

```text
storage.v2.PlayerType type = 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2.PlayerTitle title = 11;
}

```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05223"></a>
## FND-05223: chesscom.game_gateway.v2.Player.final_rating = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 final_rating = 4;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 544.

```text
= 1;
  optional .chesscom.game_storage.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2.PlayerTitle title = 11;
}

```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05224"></a>
## FND-05224: chesscom.game_gateway.v2.Player.result = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerResult result = 5;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 580.

```text
ge.v2.PlayerProvider provider = 2;
  optional string key = 3;
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2.PlayerTitle title = 11;
}

```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05225"></a>
## FND-05225: chesscom.game_gateway.v2.Player.display_name = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string display_name = 10;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 642.

```text
  optional uint32 final_rating = 4;
  optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2.PlayerTitle title = 11;
}

```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05226"></a>
## FND-05226: chesscom.game_gateway.v2.Player.title = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerTitle title = 11;

### Evidence

- **SRC-0453** `research/proto/chesscom/game_gateway/v2/player.proto` — [preserved redacted evidence](../evidence/text/8eb5f83219e174bd56c45eec7819873ddae0c0d062caa1dcc1bb2766afc861a4.proto)
  Character offset 679.

```text
 optional .chesscom.game_storage.v2.PlayerResult result = 5;
  optional string display_name = 10;
  optional .chesscom.game_storage.v2.PlayerTitle title = 11;
}

```

**Source references:** SRC-0453, SRC-1424  
**URL references:** None independently associated  
**Related findings:** FND-05211, FND-05212, FND-05213

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05227"></a>
## FND-05227: enum declaration: chesscom.game_review.v2.GameReviewScreen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewScreen {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 108.

```text
e: chesscom/game_review/v2/user_activity.proto
// syntax: proto3

package chesscom.game_review.v2;

enum GameReviewScreen {
  GAME_REVIEW_SCREEN_UNSPECIFIED = 0;
  GAME_REVIEW_SCREEN_OVERVIEW = 1;
  GAME_REVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05228"></a>
## FND-05228: chesscom.game_review.v2.GameReviewScreen.GAME_REVIEW_SCREEN_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SCREEN_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 134.

```text
/user_activity.proto
// syntax: proto3

package chesscom.game_review.v2;

enum GameReviewScreen {
  GAME_REVIEW_SCREEN_UNSPECIFIED = 0;
  GAME_REVIEW_SCREEN_OVERVIEW = 1;
  GAME_REVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05229"></a>
## FND-05229: chesscom.game_review.v2.GameReviewScreen.GAME_REVIEW_SCREEN_OVERVIEW = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SCREEN_OVERVIEW = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 172.

```text


package chesscom.game_review.v2;

enum GameReviewScreen {
  GAME_REVIEW_SCREEN_UNSPECIFIED = 0;
  GAME_REVIEW_SCREEN_OVERVIEW = 1;
  GAME_REVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05230"></a>
## FND-05230: chesscom.game_review.v2.GameReviewScreen.GAME_REVIEW_SCREEN_MOVES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SCREEN_MOVES = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 207.

```text

enum GameReviewScreen {
  GAME_REVIEW_SCREEN_UNSPECIFIED = 0;
  GAME_REVIEW_SCREEN_OVERVIEW = 1;
  GAME_REVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05231"></a>
## FND-05231: enum declaration: chesscom.game_review.v2.ShowMovesButtonState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ShowMovesButtonState {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 240.

```text
EVIEW_SCREEN_UNSPECIFIED = 0;
  GAME_REVIEW_SCREEN_OVERVIEW = 1;
  GAME_REVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMet
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05232"></a>
## FND-05232: chesscom.game_review.v2.ShowMovesButtonState.SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 270.

```text
  GAME_REVIEW_SCREEN_OVERVIEW = 1;
  GAME_REVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIG
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05233"></a>
## FND-05233: chesscom.game_review.v2.ShowMovesButtonState.SHOW_MOVES_BUTTON_STATE_SHOW = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOW_MOVES_BUTTON_STATE_SHOW = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 313.

```text
EVIEW_SCREEN_MOVES = 2;
}

enum ShowMovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05234"></a>
## FND-05234: chesscom.game_review.v2.ShowMovesButtonState.SHOW_MOVES_BUTTON_STATE_HIDE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOW_MOVES_BUTTON_STATE_HIDE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 349.

```text
MovesButtonState {
  SHOW_MOVES_BUTTON_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CL
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05235"></a>
## FND-05235: enum declaration: chesscom.game_review.v2.UserOrOpponentMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserOrOpponentMove {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 386.

```text
N_STATE_UNSPECIFIED = 0;
  SHOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGAT
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05236"></a>
## FND-05236: chesscom.game_review.v2.UserOrOpponentMove.USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 414.

```text
HOW_MOVES_BUTTON_STATE_SHOW = 1;
  SHOW_MOVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_T
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05237"></a>
## FND-05237: chesscom.game_review.v2.UserOrOpponentMove.USER_OR_OPPONENT_MOVE_USER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_OR_OPPONENT_MOVE_USER = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 455.

```text
OVES_BUTTON_STATE_HIDE = 2;
}

enum UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05238"></a>
## FND-05238: chesscom.game_review.v2.UserOrOpponentMove.USER_OR_OPPONENT_MOVE_OPPONENT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_OR_OPPONENT_MOVE_OPPONENT = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 489.

```text
m UserOrOpponentMove {
  USER_OR_OPPONENT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05239"></a>
## FND-05239: enum declaration: chesscom.game_review.v2.GameReviewMoveNavigationMethod

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewMoveNavigationMethod {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 528.

```text
NT_MOVE_UNSPECIFIED = 0;
  USER_OR_OPPONENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PRE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05240"></a>
## FND-05240: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 568.

```text
ENT_MOVE_USER = 1;
  USER_OR_OPPONENT_MOVE_OPPONENT = 2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVI
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05241"></a>
## FND-05241: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 622.

```text
2;
}

enum GameReviewMoveNavigationMethod {
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05242"></a>
## FND-05242: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 682.

```text
VE_NAVIGATION_METHOD_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05243"></a>
## FND-05243: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 747.

```text
ON_METHOD_MOVE_NODE_CLICKED = 1;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;
  G
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05244"></a>
## FND-05244: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 810.

```text
METHOD_NEXT_MOVE_ARROW_TAPPED = 2;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05245"></a>
## FND-05245: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 879.

```text
OD_NEXT_MOVE_ARROW_HOLD = 3;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GA
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05246"></a>
## FND-05246: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 946.

```text
REVIOUS_MOVE_ARROW_TAPPED = 4;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05247"></a>
## FND-05247: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1007.

```text
METHOD_PREVIOUS_MOVE_ARROW_HOLD = 5;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_M
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05248"></a>
## FND-05248: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1066.

```text
IGATION_METHOD_MOVE_WHEEL_DRAGGED = 6;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_MOVE_WHEEL_FLUNG = 7;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05249"></a>
## FND-05249: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1132.

```text
ON_METHOD_MOVE_WHEEL_FLUNG = 7;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_FIRST_MOVE_ARROW_TAPPED = 8;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButt
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05250"></a>
## FND-05250: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1197.

```text
HOD_FIRST_MOVE_ARROW_TAPPED = 8;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REV
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05251"></a>
## FND-05251: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1256.

```text
ION_METHOD_LAST_MOVE_ARROW_TAPPED = 9;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05252"></a>
## FND-05252: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1314.

```text
NAVIGATION_METHOD_ARROW_KEY_RIGHT = 10;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeed
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05253"></a>
## FND-05253: chesscom.game_review.v2.GameReviewMoveNavigationMethod.GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1370.

```text
VE_NAVIGATION_METHOD_ARROW_KEY_LEFT = 11;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIF
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05254"></a>
## FND-05254: enum declaration: chesscom.game_review.v2.GameReviewBackButtonWeb

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewBackButtonWeb {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1429.

```text
E_NAVIGATION_METHOD_ARROW_KEY_UP = 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GA
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05255"></a>
## FND-05255: chesscom.game_review.v2.GameReviewBackButtonWeb.GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1462.

```text
= 12;
  GAME_REVIEW_MOVE_NAVIGATION_METHOD_ARROW_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05256"></a>
## FND-05256: chesscom.game_review.v2.GameReviewBackButtonWeb.GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1509.

```text
W_KEY_DOWN = 13;
}

enum GameReviewBackButtonWeb {
  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05257"></a>
## FND-05257: chesscom.game_review.v2.GameReviewBackButtonWeb.GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1559.

```text

  GAME_REVIEW_BACK_BUTTON_WEB_UNSPECIFIED = 0;
  GAME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEX
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05258"></a>
## FND-05258: enum declaration: chesscom.game_review.v2.GameReviewMoveFeedbackButton

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewMoveFeedbackButton {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1611.

```text
ME_REVIEW_BACK_BUTTON_WEB_SIDEBAR_HEADER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_H
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05259"></a>
## FND-05259: chesscom.game_review.v2.GameReviewMoveFeedbackButton.GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1649.

```text
ER = 1;
  GAME_REVIEW_BACK_BUTTON_WEB_END_OF_MOVELIST = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModa
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05260"></a>
## FND-05260: chesscom.game_review.v2.GameReviewMoveFeedbackButton.GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1701.

```text
T = 2;
}

enum GameReviewMoveFeedbackButton {
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECI
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05261"></a>
## FND-05261: chesscom.game_review.v2.GameReviewMoveFeedbackButton.GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1747.

```text
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_C
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05262"></a>
## FND-05262: chesscom.game_review.v2.GameReviewMoveFeedbackButton.GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1797.

```text
;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_RETRY = 1;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSI
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05263"></a>
## FND-05263: chesscom.game_review.v2.GameReviewMoveFeedbackButton.GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1843.

```text
;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_BEST_MOVE = 2;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BAC
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05264"></a>
## FND-05264: chesscom.game_review.v2.GameReviewMoveFeedbackButton.GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1897.

```text
GAME_REVIEW_MOVE_FEEDBACK_BUTTON_SHARE = 3;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_S
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05265"></a>
## FND-05265: enum declaration: chesscom.game_review.v2.GameReviewPremiumModalButton

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewPremiumModalButton {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1943.

```text
GAME_REVIEW_MOVE_FEEDBACK_BUTTON_NEXT_KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_STA
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05266"></a>
## FND-05266: chesscom.game_review.v2.GameReviewPremiumModalButton.GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 1981.

```text
KEY_MOVE = 4;
  GAME_REVIEW_MOVE_FEEDBACK_BUTTON_HINT = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_STAR
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05267"></a>
## FND-05267: chesscom.game_review.v2.GameReviewPremiumModalButton.GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2033.

```text
T = 5;
}

enum GameReviewPremiumModalButton {
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURC
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05268"></a>
## FND-05268: chesscom.game_review.v2.GameReviewPremiumModalButton.GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2079.

```text
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05269"></a>
## FND-05269: chesscom.game_review.v2.GameReviewPremiumModalButton.GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2127.

```text
 0;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_CLOSE = 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05270"></a>
## FND-05270: enum declaration: chesscom.game_review.v2.GameReviewStartSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewStartSource {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2173.

```text
 1;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05271"></a>
## FND-05271: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2204.

```text
_BUTTON_OUTSIDE = 2;
  GAME_REVIEW_PREMIUM_MODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05272"></a>
## FND-05272: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_HOME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_HOME = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2248.

```text
ODAL_BUTTON_BACK = 3;
}

enum GameReviewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05273"></a>
## FND-05273: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2285.

```text
iewStartSource {
  GAME_REVIEW_START_SOURCE_UNSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAM
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05274"></a>
## FND-05274: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_PROFILE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_PROFILE = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2330.

```text
NSPECIFIED = 0;
  GAME_REVIEW_START_SOURCE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
