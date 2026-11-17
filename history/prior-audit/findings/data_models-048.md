# data_models — findings 4701–4800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04975"></a>
## FND-04975: chesscom.game_gateway.v2.SortField.SORT_FIELD_GAME_LOCATION = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_GAME_LOCATION = 22;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 922.

```text
RT_FIELD_OPPONENT_USERNAME = 19;
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
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .c
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04976"></a>
## FND-04976: chesscom.game_gateway.v2.SortField.SORT_FIELD_VS_COMPUTER = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_VS_COMPUTER = 23;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 955.

```text
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
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04977"></a>
## FND-04977: chesscom.game_gateway.v2.SortField.SORT_FIELD_GAME_SOURCE = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_GAME_SOURCE = 24;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 986.

```text
ORT_FIELD_OPPONENT_ACCURACY = 21;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .googl
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04978"></a>
## FND-04978: chesscom.game_gateway.v2.SortField.SORT_FIELD_FRIEND = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_FRIEND = 25;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1017.

```text
1;
  SORT_FIELD_GAME_LOCATION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04979"></a>
## FND-04979: chesscom.game_gateway.v2.SortField.SORT_FIELD_RANDOM_ORDER = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_RANDOM_ORDER = 26;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1043.

```text
ION = 22;
  SORT_FIELD_VS_COMPUTER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGa
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04980"></a>
## FND-04980: chesscom.game_gateway.v2.SortField.SORT_FIELD_LEGACY_GAME_ID = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_FIELD_LEGACY_GAME_ID = 27;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1075.

```text
ER = 23;
  SORT_FIELD_GAME_SOURCE = 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04981"></a>
## FND-04981: message declaration: chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HydrateGamesByCriteriaRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1110.

```text
 24;
  SORT_FIELD_FRIEND = 25;
  SORT_FIELD_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.Hydrat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04982"></a>
## FND-04982: oneof declaration: chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1152.

```text
D_RANDOM_ORDER = 26;
  SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .che
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04983"></a>
## FND-04983: chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest.pagination = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1174.

```text
 SORT_FIELD_LEGACY_GAME_ID = 27;
}

message HydrateGamesByCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponseP
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04984"></a>
## FND-04984: chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest.criteria = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.Criteria criteria = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1231.

```text
yCriteriaRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message AggregateGameResults
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04985"></a>
## FND-04985: chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest.field_mask = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1291.

```text
RequestPagination pagination = 3;
  }
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04986"></a>
## FND-04986: message declaration: chesscom.game_gateway.v2.HydrateGamesByCriteriaResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HydrateGamesByCriteriaResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1346.

```text
com.game_gateway.v2.Criteria criteria = 1;
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
  .chesscom.game_gateway.v2.AggregateCriteria aggregate_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04987"></a>
## FND-04987: chesscom.game_gateway.v2.HydrateGamesByCriteriaResponse.hydrated_games = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1389.

```text
  optional .google.protobuf.FieldMask field_mask = 2;
}

message HydrateGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
  .chesscom.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;
  }
  optional string player_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04988"></a>
## FND-04988: chesscom.game_gateway.v2.HydrateGamesByCriteriaResponse.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1459.

```text
teGamesByCriteriaResponse {
  repeated .chesscom.game_gateway.v2.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
  .chesscom.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;
  }
  optional string player_id = 1;
}

message AggregateGameResultsByPlayerAndCriteriaResponse {
 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04989"></a>
## FND-04989: message declaration: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AggregateGameResultsByPlayerAndCriteriaRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1523.

```text
.HydratedGame hydrated_games = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
  .chesscom.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;
  }
  optional string player_id = 1;
}

message AggregateGameResultsByPlayerAndCriteriaResponse {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04990"></a>
## FND-04990: oneof declaration: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaRequest._aggregate_criteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _aggregate_criteria {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1582.

```text
v1.ResponsePagination pagination = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
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

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04991"></a>
## FND-04991: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaRequest.aggregate_criteria = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1612.

```text
on = 2;
}

message AggregateGameResultsByPlayerAndCriteriaRequest {
  oneof _aggregate_criteria {
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
  .chess
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04992"></a>
## FND-04992: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaRequest.player_id = 1

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

<a id="FND-04993"></a>
## FND-04993: message declaration: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AggregateGameResultsByPlayerAndCriteriaResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1720.

```text
m.game_gateway.v2.AggregateCriteria aggregate_criteria = 2;
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
  .chesscom.chess.v1.Variant variant = 4;
  }

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04994"></a>
## FND-04994: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaResponse.wins = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 wins = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1780.

```text
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
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp g
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04995"></a>
## FND-04995: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaResponse.draws = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 draws = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1807.

```text
r_id = 1;
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
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04996"></a>
## FND-04996: chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaResponse.losses = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 losses = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1835.

```text
teGameResultsByPlayerAndCriteriaResponse {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04997"></a>
## FND-04997: message declaration: chesscom.game_gateway.v2.PlayerOverviewStatsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerOverviewStatsRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1865.

```text
iaResponse {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp g
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04998"></a>
## FND-04998: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsRequest._time_class

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_class {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1904.

```text

  optional int64 draws = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional str
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04999"></a>
## FND-04999: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.time_class = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.TimeClass time_class = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1926.

```text
s = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  o
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05000"></a>
## FND-05000: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsRequest._variant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _variant {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1977.

```text
erOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05001"></a>
## FND-05001: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.variant = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Variant variant = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1996.

```text
est {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05002"></a>
## FND-05002: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsRequest._game_end_time_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_end_time_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2042.

```text
v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05003"></a>
## FND-05003: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.game_end_time_from = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_end_time_from = 8;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2072.

```text
 }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach = 7;
}

message PlayerOverviewS
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05004"></a>
## FND-05004: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsRequest._game_end_time_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_end_time_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2129.

```text
t = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach = 7;
}

message PlayerOverviewStatsResponse {
  oneof _daily_game_timeout_count {
  uint
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05005"></a>
## FND-05005: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.game_end_time_to = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_end_time_to = 9;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2157.

```text
_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach = 7;
}

message PlayerOverviewStatsResponse {
  oneof _daily_game_timeout_count {
  uint32 daily_game_timeout_count 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05006"></a>
## FND-05006: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.player_id = 1

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

<a id="FND-05007"></a>
## FND-05007: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.field_mask = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2245.

```text
time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach = 7;
}

message PlayerOverviewStatsResponse {
  oneof _daily_game_timeout_count {
  uint32 daily_game_timeout_count = 12;
  }
  oneof _best_win_opponent_username {
  string best_win_opponent_username = 13
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05008"></a>
## FND-05008: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.is_vs_computer = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_vs_computer = 6;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2299.

```text
o = 9;
  }
  optional string player_id = 1;
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
  string best_win_ga
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05009"></a>
## FND-05009: chesscom.game_gateway.v2.PlayerOverviewStatsRequest.is_vs_coach = 7

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

<a id="FND-05010"></a>
## FND-05010: message declaration: chesscom.game_gateway.v2.PlayerOverviewStatsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerOverviewStatsResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2369.

```text
f.FieldMask field_mask = 5;
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
  oneof _most_played_eco_family_id {
  uint32 most_pla
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05011"></a>
## FND-05011: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsResponse._daily_game_timeout_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_game_timeout_count {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2409.

```text
ool is_vs_computer = 6;
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
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05012"></a>
## FND-05012: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.daily_game_timeout_count = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 daily_game_timeout_count = 12;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2445.

```text
ool is_vs_coach = 7;
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
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGam
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05013"></a>
## FND-05013: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsResponse._best_win_opponent_username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_win_opponent_username {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2489.

```text
ewStatsResponse {
  oneof _daily_game_timeout_count {
  uint32 daily_game_timeout_count = 12;
  }
  oneof _best_win_opponent_username {
  string best_win_opponent_username = 13;
  }
  oneof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chessco
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05014"></a>
## FND-05014: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.best_win_opponent_username = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string best_win_opponent_username = 13;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2527.

```text
timeout_count {
  uint32 daily_game_timeout_count = 12;
  }
  oneof _best_win_opponent_username {
  string best_win_opponent_username = 13;
  }
  oneof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount bl
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05015"></a>
## FND-05015: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsResponse._best_win_game_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_win_game_id {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2573.

```text
unt = 12;
  }
  oneof _best_win_opponent_username {
  string best_win_opponent_username = 13;
  }
  oneof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rati
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05016"></a>
## FND-05016: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.best_win_game_id = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string best_win_game_id = 14;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2601.

```text
win_opponent_username {
  string best_win_opponent_username = 13;
  }
  oneof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.p
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05017"></a>
## FND-05017: oneof declaration: chesscom.game_gateway.v2.PlayerOverviewStatsResponse._most_played_eco_family_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _most_played_eco_family_id {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2637.

```text
t_win_opponent_username = 13;
  }
  oneof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_dat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05018"></a>
## FND-05018: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.most_played_eco_family_id = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 most_played_eco_family_id = 15;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2674.

```text
neof _best_win_game_id {
  string best_win_game_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05019"></a>
## FND-05019: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.white_counts = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2719.

```text
me_id = 14;
  }
  oneof _most_played_eco_family_id {
  uint32 most_played_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  op
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05020"></a>
## FND-05020: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.black_counts = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2792.

```text
_eco_family_id = 15;
  }
  optional .chesscom.game_gateway.v2.OverviewGameCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_oppo
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05021"></a>
## FND-05021: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.highest_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 highest_rating = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2865.

```text
eCount white_counts = 1;
  optional .chesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05022"></a>
## FND-05022: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.highest_rating_date = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp highest_rating_date = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2903.

```text
hesscom.game_gateway.v2.OverviewGameCount black_counts = 2;
  optional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05023"></a>
## FND-05023: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.best_win = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 best_win = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2966.

```text
ptional uint32 highest_rating = 3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGam
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05024"></a>
## FND-05024: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.best_win_streak = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 best_win_streak = 6;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2998.

```text
3;
  optional .google.protobuf.Timestamp highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optiona
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05025"></a>
## FND-05025: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.average_opponent_rating = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 average_opponent_rating = 7;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3037.

```text
p highest_rating_date = 4;
  optional uint32 best_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05026"></a>
## FND-05026: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.average_opponent_rating_win = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 average_opponent_rating_win = 8;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3084.

```text
st_win = 5;
  optional uint32 best_win_streak = 6;
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .goog
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05027"></a>
## FND-05027: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.average_opponent_rating_lose = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 average_opponent_rating_lose = 9;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3135.

```text
  optional uint32 average_opponent_rating = 7;
  optional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uin
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05028"></a>
## FND-05028: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.average_opponent_rating_draw = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 average_opponent_rating_draw = 10;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3187.

```text
ional uint32 average_opponent_rating_win = 8;
  optional uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  opt
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05029"></a>
## FND-05029: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.ratings = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3240.

```text
nal uint32 average_opponent_rating_lose = 9;
  optional uint32 average_opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  o
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05030"></a>
## FND-05030: chesscom.game_gateway.v2.PlayerOverviewStatsResponse.brilliant_moves_count = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 brilliant_moves_count = 16;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3311.

```text
opponent_rating_draw = 10;
  repeated .chesscom.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _openi
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05031"></a>
## FND-05031: message declaration: chesscom.game_gateway.v2.OverviewGameRatings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OverviewGameRatings {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3358.

```text
.game_gateway.v2.OverviewGameRatings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteri
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05032"></a>
## FND-05032: chesscom.game_gateway.v2.OverviewGameRatings.timestamp = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp timestamp = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3390.

```text
ings ratings = 11;
  optional uint32 brilliant_moves_count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _oppo
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05033"></a>
## FND-05033: chesscom.game_gateway.v2.OverviewGameRatings.rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 rating = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3443.

```text
count = 16;
}

message OverviewGameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _colo
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05034"></a>
## FND-05034: message declaration: chesscom.game_gateway.v2.OverviewGameCount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OverviewGameCount {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3474.

```text
GameRatings {
  optional .google.protobuf.Timestamp timestamp = 1;
  optional uint32 rating = 2;
}

message OverviewGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05035"></a>
## FND-05035: chesscom.game_gateway.v2.OverviewGameCount.wins = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 wins = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1780.

```text
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
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp g
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05036"></a>
## FND-05036: chesscom.game_gateway.v2.OverviewGameCount.draws = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 draws = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1807.

```text
r_id = 1;
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
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05037"></a>
## FND-05037: chesscom.game_gateway.v2.OverviewGameCount.losses = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 losses = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 1835.

```text
teGameResultsByPlayerAndCriteriaResponse {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message PlayerOverviewStatsRequest {
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05038"></a>
## FND-05038: message declaration: chesscom.game_gateway.v2.AggregateCriteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AggregateCriteria {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3589.

```text
wGameCount {
  optional int64 wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timest
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05039"></a>
## FND-05039: oneof declaration: chesscom.game_gateway.v2.AggregateCriteria._opening

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3619.

```text
wins = 1;
  optional int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05040"></a>
## FND-05040: chesscom.game_gateway.v2.AggregateCriteria.opening = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_gateway.v2.OpeningCriteria opening = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3638.

```text
l int64 draws = 2;
  optional int64 losses = 3;
}

message AggregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05041"></a>
## FND-05041: oneof declaration: chesscom.game_gateway.v2.AggregateCriteria._opponent_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_id {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3699.

```text
gregateCriteria {
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05042"></a>
## FND-05042: chesscom.game_gateway.v2.AggregateCriteria.opponent_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opponent_id = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3722.

```text
of _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chessc
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05043"></a>
## FND-05043: oneof declaration: chesscom.game_gateway.v2.AggregateCriteria._color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _color {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3752.

```text
_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_cla
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05044"></a>
## FND-05044: chesscom.game_gateway.v2.AggregateCriteria.color = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color color = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3769.

```text
ngCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repea
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05045"></a>
## FND-05045: oneof declaration: chesscom.game_gateway.v2.AggregateCriteria._is_rated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_rated {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3811.

```text
ent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05046"></a>
## FND-05046: chesscom.game_gateway.v2.AggregateCriteria.is_rated = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_rated = 6;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3831.

```text
ponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criter
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05047"></a>
## FND-05047: oneof declaration: chesscom.game_gateway.v2.AggregateCriteria._game_end_time_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_end_time_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2042.

```text
v1.TimeClass time_class = 3;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05048"></a>
## FND-05048: chesscom.game_gateway.v2.AggregateCriteria.game_end_time_from = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_end_time_from = 7;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3886.

```text
1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05049"></a>
## FND-05049: oneof declaration: chesscom.game_gateway.v2.AggregateCriteria._game_end_time_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_end_time_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 2129.

```text
t = 4;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 8;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 9;
  }
  optional string player_id = 1;
  optional .google.protobuf.FieldMask field_mask = 5;
  optional bool is_vs_computer = 6;
  optional bool is_vs_coach = 7;
}

message PlayerOverviewStatsResponse {
  oneof _daily_game_timeout_count {
  uint
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05050"></a>
## FND-05050: chesscom.game_gateway.v2.AggregateCriteria.game_end_time_to = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_end_time_to = 8;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3971.

```text
_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05051"></a>
## FND-05051: chesscom.game_gateway.v2.AggregateCriteria.time_classes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.TimeClass time_classes = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4026.

```text
_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05052"></a>
## FND-05052: chesscom.game_gateway.v2.AggregateCriteria.variants = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Variant variants = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4084.

```text
buf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05053"></a>
## FND-05053: message declaration: chesscom.game_gateway.v2.Criteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Criteria {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4137.

```text
hesscom.chess.v1.TimeClass time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_us
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05054"></a>
## FND-05054: oneof declaration: chesscom.game_gateway.v2.Criteria._accuracy_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _accuracy_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4158.

```text
Class time_classes = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  one
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05055"></a>
## FND-05055: chesscom.game_gateway.v2.Criteria.accuracy_from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float accuracy_from = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4183.

```text
 repeated .chesscom.chess.v1.Variant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string u
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05056"></a>
## FND-05056: oneof declaration: chesscom.game_gateway.v2.Criteria._accuracy_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _accuracy_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4214.

```text
riant variants = 2;
}

message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _ratin
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05057"></a>
## FND-05057: chesscom.game_gateway.v2.Criteria.accuracy_to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float accuracy_to = 2;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4237.

```text
message Criteria {
  oneof _accuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 ratin
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05058"></a>
## FND-05058: oneof declaration: chesscom.game_gateway.v2.Criteria._opponent_accuracy_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_accuracy_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4266.

```text
ccuracy_from {
  float accuracy_from = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rati
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05059"></a>
## FND-05059: chesscom.game_gateway.v2.Criteria.opponent_accuracy_from = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float opponent_accuracy_from = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4300.

```text
om = 1;
  }
  oneof _accuracy_to {
  float accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05060"></a>
## FND-05060: oneof declaration: chesscom.game_gateway.v2.Criteria._opponent_accuracy_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_accuracy_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4340.

```text
at accuracy_to = 2;
  }
  oneof _opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uin
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05061"></a>
## FND-05061: chesscom.game_gateway.v2.Criteria.opponent_accuracy_to = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float opponent_accuracy_to = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4372.

```text
_opponent_accuracy_from {
  float opponent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05062"></a>
## FND-05062: oneof declaration: chesscom.game_gateway.v2.Criteria._opponent_username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_username {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4410.

```text
nent_accuracy_from = 3;
  }
  oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uin
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05063"></a>
## FND-05063: chesscom.game_gateway.v2.Criteria.opponent_username = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opponent_username = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4439.

```text
 oneof _opponent_accuracy_to {
  float opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05064"></a>
## FND-05064: oneof declaration: chesscom.game_gateway.v2.Criteria._username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4475.

```text
at opponent_accuracy_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.che
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05065"></a>
## FND-05065: chesscom.game_gateway.v2.Criteria.username = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string username = 7;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4495.

```text
_to = 4;
  }
  oneof _opponent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05066"></a>
## FND-05066: oneof declaration: chesscom.game_gateway.v2.Criteria._rating_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4522.

```text
ent_username {
  string opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friend
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05067"></a>
## FND-05067: chesscom.game_gateway.v2.Criteria.rating_from = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 rating_from = 9;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4545.

```text
 opponent_username = 5;
  }
  oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05068"></a>
## FND-05068: oneof declaration: chesscom.game_gateway.v2.Criteria._rating_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4575.

```text
oneof _username {
  string username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends = 14;
  }
  oneof _theme {
  s
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05069"></a>
## FND-05069: chesscom.game_gateway.v2.Criteria.rating_to = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 rating_to = 10;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4596.

```text
tring username = 7;
  }
  oneof _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends = 14;
  }
  oneof _theme {
  string theme = 15;
  }
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05070"></a>
## FND-05070: oneof declaration: chesscom.game_gateway.v2.Criteria._opponent_rating_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_rating_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4625.

```text
of _rating_from {
  uint32 rating_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends = 14;
  }
  oneof _theme {
  string theme = 15;
  }
  oneof _opponent_theme {
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05071"></a>
## FND-05071: chesscom.game_gateway.v2.Criteria.opponent_rating_from = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 opponent_rating_from = 11;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4657.

```text
g_from = 9;
  }
  oneof _rating_to {
  uint32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends = 14;
  }
  oneof _theme {
  string theme = 15;
  }
  oneof _opponent_theme {
  string opponent_theme = 16;
  }

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05072"></a>
## FND-05072: oneof declaration: chesscom.game_gateway.v2.Criteria._opponent_rating_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_rating_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4697.

```text
int32 rating_to = 10;
  }
  oneof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends = 14;
  }
  oneof _theme {
  string theme = 15;
  }
  oneof _opponent_theme {
  string opponent_theme = 16;
  }
  oneof _opening {
  .chesscom.game_gate
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05073"></a>
## FND-05073: chesscom.game_gateway.v2.Criteria.opponent_rating_to = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 opponent_rating_to = 12;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4727.

```text
eof _opponent_rating_from {
  uint32 opponent_rating_from = 11;
  }
  oneof _opponent_rating_to {
  uint32 opponent_rating_to = 12;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 13;
  }
  oneof _are_friends {
  bool are_friends = 14;
  }
  oneof _theme {
  string theme = 15;
  }
  oneof _opponent_theme {
  string opponent_theme = 16;
  }
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05074"></a>
## FND-05074: oneof declaration: chesscom.game_gateway.v2.Criteria._color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _color {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 3752.

```text
_gateway.v2.OpeningCriteria opening = 3;
  }
  oneof _opponent_id {
  string opponent_id = 4;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _is_rated {
  bool is_rated = 6;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 7;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 8;
  }
  repeated .chesscom.chess.v1.TimeClass time_cla
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
