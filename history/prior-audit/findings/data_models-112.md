# data_models — findings 11101–11200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11375"></a>
## FND-11375: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1837.

```text
COUNT_PREVIOUS = 41;
  STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;
}

message StatsLiveProperty {
  oneof _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11376"></a>
## FND-11376: chesscom.user_properties.v1.StatsLiveProperty.rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 rating = 1;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1855.

```text
1;
  STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;
}

message StatsLiveProperty {
  oneof _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_w
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11377"></a>
## FND-11377: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._game_time_class

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_time_class {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1880.

```text
T_POINTS_PREVIOUS = 42;
}

message StatsLiveProperty {
  oneof _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  one
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11378"></a>
## FND-11378: chesscom.user_properties.v1.StatsLiveProperty.game_time_class = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_time_class = 2;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1907.

```text
message StatsLiveProperty {
  oneof _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11379"></a>
## FND-11379: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._total_move_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_move_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1941.

```text
f _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_ratin
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11380"></a>
## FND-11380: chesscom.user_properties.v1.StatsLiveProperty.total_move_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 total_move_count = 3;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1969.

```text
= 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_dat
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11381"></a>
## FND-11381: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._unrated_game_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _unrated_game_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2004.

```text

  string game_time_class = 2;
  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp la
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11382"></a>
## FND-11382: chesscom.user_properties.v1.StatsLiveProperty.unrated_game_count = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 unrated_game_count = 4;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2034.

```text

  }
  oneof _total_move_count {
  uint32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _high
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11383"></a>
## FND-11383: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._disconnect_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _disconnect_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2071.

```text
nt32 total_move_count = 3;
  }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11384"></a>
## FND-11384: chesscom.user_properties.v1.StatsLiveProperty.disconnect_count = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 disconnect_count = 5;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2099.

```text
 }
  oneof _unrated_game_count {
  uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_ra
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11385"></a>
## FND-11385: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._best_win_game_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_win_game_id {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2134.

```text
uint32 unrated_game_count = 4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Time
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11386"></a>
## FND-11386: chesscom.user_properties.v1.StatsLiveProperty.best_win_game_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint64 best_win_game_id = 6;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2162.

```text
4;
  }
  oneof _disconnect_count {
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11387"></a>
## FND-11387: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._highest_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_opponent_rating {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2197.

```text
  uint32 disconnect_count = 5;
  }
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11388"></a>
## FND-11388: chesscom.user_properties.v1.StatsLiveProperty.highest_opponent_rating = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 highest_opponent_rating = 7;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2232.

```text
  oneof _best_win_game_id {
  uint64 best_win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_ga
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11389"></a>
## FND-11389: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._last_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_date {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2274.

```text
win_game_id = 6;
  }
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  b
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11390"></a>
## FND-11390: chesscom.user_properties.v1.StatsLiveProperty.last_date = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_date = 8;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2295.

```text
  oneof _highest_opponent_rating {
  uint32 highest_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11391"></a>
## FND-11391: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._highest_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_rating {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2343.

```text
est_opponent_rating = 7;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 to
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11392"></a>
## FND-11392: chesscom.user_properties.v1.StatsLiveProperty.highest_rating = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 highest_rating = 9;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2369.

```text
 }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11393"></a>
## FND-11393: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._highest_rating_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_rating_date {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2402.

```text
.protobuf.Timestamp last_date = 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_cou
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11394"></a>
## FND-11394: chesscom.user_properties.v1.StatsLiveProperty.highest_rating_date = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp highest_rating_date = 10;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2433.

```text
 8;
  }
  oneof _highest_rating {
  uint32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_c
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11395"></a>
## FND-11395: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._last_game_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_game_date {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2492.

```text
 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 t
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11396"></a>
## FND-11396: chesscom.user_properties.v1.StatsLiveProperty.last_game_date = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_game_date = 11;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2518.

```text
ating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11397"></a>
## FND-11397: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._is_active

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_active {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2572.

```text
ng_date = 10;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11398"></a>
## FND-11398: chesscom.user_properties.v1.StatsLiveProperty.is_active = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_active = 12;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2593.

```text
neof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 1
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11399"></a>
## FND-11399: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._total_rated_game_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_game_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2620.

```text
oogle.protobuf.Timestamp last_game_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_str
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11400"></a>
## FND-11400: chesscom.user_properties.v1.StatsLiveProperty.total_rated_game_count = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 total_rated_game_count = 13;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2654.

```text
_date = 11;
  }
  oneof _is_active {
  bool is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11401"></a>
## FND-11401: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._total_rated_win_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_win_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2696.

```text
l is_active = 12;
  }
  oneof _total_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11402"></a>
## FND-11402: chesscom.user_properties.v1.StatsLiveProperty.total_rated_win_count = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 total_rated_win_count = 14;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2729.

```text
tal_rated_game_count {
  uint32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _ma
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11403"></a>
## FND-11403: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._total_rated_loss_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_loss_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2770.

```text
ed_game_count = 13;
  }
  oneof _total_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak =
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11404"></a>
## FND-11404: chesscom.user_properties.v1.StatsLiveProperty.total_rated_loss_count = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 total_rated_loss_count = 15;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2804.

```text
otal_rated_win_count {
  uint32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  b
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11405"></a>
## FND-11405: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._total_rated_draw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_draw_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2846.

```text
d_win_count = 14;
  }
  oneof _total_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_oppo
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11406"></a>
## FND-11406: chesscom.user_properties.v1.StatsLiveProperty.total_rated_draw_count = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 total_rated_draw_count = 16;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2880.

```text
al_rated_loss_count {
  uint32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponen
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11407"></a>
## FND-11407: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._current_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_streak {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2922.

```text
_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11408"></a>
## FND-11408: chesscom.user_properties.v1.StatsLiveProperty.current_streak = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 current_streak = 17;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2948.

```text
eof _total_rated_draw_count {
  uint32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game =
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11409"></a>
## FND-11409: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._max_win_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_win_streak {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 2981.

```text
int32 total_rated_draw_count = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11410"></a>
## FND-11410: chesscom.user_properties.v1.StatsLiveProperty.max_win_streak = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_win_streak = 18;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3007.

```text
nt = 16;
  }
  oneof _current_streak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11411"></a>
## FND-11411: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._max_loss_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_loss_streak {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3040.

```text
eak {
  int32 current_streak = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_co
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11412"></a>
## FND-11412: chesscom.user_properties.v1.StatsLiveProperty.max_loss_streak = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_loss_streak = 19;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3067.

```text
k = 17;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11413"></a>
## FND-11413: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._is_unrated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_unrated {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3101.

```text
k {
  int32 max_win_streak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11414"></a>
## FND-11414: chesscom.user_properties.v1.StatsLiveProperty.is_unrated = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_unrated = 20;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3123.

```text
reak = 18;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11415"></a>
## FND-11415: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._avg_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avg_opponent_rating {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3151.

```text
loss_streak {
  int32 max_loss_streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11416"></a>
## FND-11416: chesscom.user_properties.v1.StatsLiveProperty.avg_opponent_rating = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double avg_opponent_rating = 21;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3182.

```text
streak = 19;
  }
  oneof _is_unrated {
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_cou
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11417"></a>
## FND-11417: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._best_win_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_win_game {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3221.

```text
  bool is_unrated = 20;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_w
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11418"></a>
## FND-11418: chesscom.user_properties.v1.StatsLiveProperty.best_win_game = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string best_win_game = 22;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3246.

```text
 }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tourn
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11419"></a>
## FND-11419: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._moves_per_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _moves_per_game {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3279.

```text

  double avg_opponent_rating = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11420"></a>
## FND-11420: chesscom.user_properties.v1.StatsLiveProperty.moves_per_game = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 moves_per_game = 23;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3305.

```text
ing = 21;
  }
  oneof _best_win_game {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_los
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11421"></a>
## FND-11421: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._adjudicated_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _adjudicated_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3339.

```text
me {
  string best_win_game = 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11422"></a>
## FND-11422: chesscom.user_properties.v1.StatsLiveProperty.adjudicated_count = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 adjudicated_count = 24;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3368.

```text
 22;
  }
  oneof _moves_per_game {
  uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11423"></a>
## FND-11423: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._dw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _dw_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3405.

```text
uint32 moves_per_game = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11424"></a>
## FND-11424: chesscom.user_properties.v1.StatsLiveProperty.dw_count = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 dw_count = 25;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3425.

```text
e = 23;
  }
  oneof _adjudicated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_d
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11425"></a>
## FND-11425: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3453.

```text
ated_count {
  uint32 adjudicated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11426"></a>
## FND-11426: chesscom.user_properties.v1.StatsLiveProperty.tournament_count = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_count = 26;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3481.

```text
cated_count = 24;
  }
  oneof _dw_count {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  u
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11427"></a>
## FND-11427: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_game_win_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_game_win_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3517.

```text
unt {
  uint32 dw_count = 25;
  }
  oneof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11428"></a>
## FND-11428: chesscom.user_properties.v1.StatsLiveProperty.tournament_game_win_count = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_game_win_count = 27;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3554.

```text
neof _tournament_count {
  uint32 tournament_count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  u
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11429"></a>
## FND-11429: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_game_loss_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_game_loss_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3599.

```text
count = 26;
  }
  oneof _tournament_game_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11430"></a>
## FND-11430: chesscom.user_properties.v1.StatsLiveProperty.tournament_game_loss_count = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_game_loss_count = 28;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3637.

```text
me_win_count {
  uint32 tournament_game_win_count = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tourn
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11431"></a>
## FND-11431: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_game_draw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_game_draw_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3683.

```text
unt = 27;
  }
  oneof _tournament_game_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11432"></a>
## FND-11432: chesscom.user_properties.v1.StatsLiveProperty.tournament_game_draw_count = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_game_draw_count = 29;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3721.

```text
_loss_count {
  uint32 tournament_game_loss_count = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_pl
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11433"></a>
## FND-11433: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_host_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_host_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3767.

```text
unt = 28;
  }
  oneof _tournament_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_co
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11434"></a>
## FND-11434: chesscom.user_properties.v1.StatsLiveProperty.tournament_host_count = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_host_count = 30;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3800.

```text
_game_draw_count {
  uint32 tournament_game_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_us
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11435"></a>
## FND-11435: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_1st_place

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_1st_place {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3841.

```text
me_draw_count = 29;
  }
  oneof _tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_wi
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11436"></a>
## FND-11436: chesscom.user_properties.v1.StatsLiveProperty.tournament_1st_place = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_1st_place = 31;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3873.

```text
_tournament_host_count {
  uint32 tournament_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tourname
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11437"></a>
## FND-11437: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_2nd_place

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_2nd_place {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3913.

```text
ment_host_count = 30;
  }
  oneof _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tou
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11438"></a>
## FND-11438: chesscom.user_properties.v1.StatsLiveProperty.tournament_2nd_place = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_2nd_place = 32;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3945.

```text
f _tournament_1st_place {
  uint32 tournament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  ui
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11439"></a>
## FND-11439: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_3rd_place

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_3rd_place {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 3985.

```text
ament_1st_place = 31;
  }
  oneof _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11440"></a>
## FND-11440: chesscom.user_properties.v1.StatsLiveProperty.tournament_3rd_place = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_3rd_place = 33;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4017.

```text
f _tournament_2nd_place {
  uint32 tournament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_c
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11441"></a>
## FND-11441: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_host_user_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_host_user_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4057.

```text
ament_2nd_place = 32;
  }
  oneof _tournament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11442"></a>
## FND-11442: chesscom.user_properties.v1.StatsLiveProperty.tournament_host_user_count = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_host_user_count = 34;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4095.

```text
rnament_3rd_place {
  uint32 tournament_3rd_place = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11443"></a>
## FND-11443: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_withdraw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_withdraw_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4141.

```text
ace = 33;
  }
  oneof _tournament_host_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11444"></a>
## FND-11444: chesscom.user_properties.v1.StatsLiveProperty.tournament_withdraw_count = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_withdraw_count = 35;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4178.

```text
t_user_count {
  uint32 tournament_host_user_count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 to
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11445"></a>
## FND-11445: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_in_progress_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_in_progress_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4223.

```text
count = 34;
  }
  oneof _tournament_withdraw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tourn
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11446"></a>
## FND-11446: chesscom.user_properties.v1.StatsLiveProperty.tournament_in_progress_count = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_in_progress_count = 36;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4263.

```text
draw_count {
  uint32 tournament_withdraw_count = 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11447"></a>
## FND-11447: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_cancel_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_cancel_count {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4311.

```text
= 35;
  }
  oneof _tournament_in_progress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_coun
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11448"></a>
## FND-11448: chesscom.user_properties.v1.StatsLiveProperty.tournament_cancel_count = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_cancel_count = 37;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4346.

```text
ogress_count {
  uint32 tournament_in_progress_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_co
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11449"></a>
## FND-11449: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_points

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_points {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4389.

```text
ess_count = 36;
  }
  oneof _tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11450"></a>
## FND-11450: chesscom.user_properties.v1.StatsLiveProperty.tournament_points = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_points = 38;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4418.

```text
tournament_cancel_count {
  uint32 tournament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 to
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11451"></a>
## FND-11451: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_count_total

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_count_total {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4455.

```text
urnament_cancel_count = 37;
  }
  oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11452"></a>
## FND-11452: chesscom.user_properties.v1.StatsLiveProperty.tournament_count_total = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_count_total = 39;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4489.

```text
oneof _tournament_points {
  uint32 tournament_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11453"></a>
## FND-11453: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_points_total

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_points_total {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4531.

```text
ment_points = 38;
  }
  oneof _tournament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11454"></a>
## FND-11454: chesscom.user_properties.v1.StatsLiveProperty.tournament_points_total = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_points_total = 40;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4566.

```text
nament_count_total {
  uint32 tournament_count_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11455"></a>
## FND-11455: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_count_previous

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_count_previous {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4609.

```text
unt_total = 39;
  }
  oneof _tournament_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11456"></a>
## FND-11456: chesscom.user_properties.v1.StatsLiveProperty.tournament_count_previous = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_count_previous = 41;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4646.

```text
nt_points_total {
  uint32 tournament_points_total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11457"></a>
## FND-11457: oneof declaration: chesscom.user_properties.v1.StatsLiveProperty._tournament_points_previous

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_points_previous {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4691.

```text
total = 40;
  }
  oneof _tournament_count_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11458"></a>
## FND-11458: chesscom.user_properties.v1.StatsLiveProperty.tournament_points_previous = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_points_previous = 42;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 4729.

```text
unt_previous {
  uint32 tournament_count_previous = 41;
  }
  oneof _tournament_points_previous {
  uint32 tournament_points_previous = 42;
  }
}

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11459"></a>
## FND-11459: enum declaration: chesscom.user_properties.v1.SubscriptionPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SubscriptionPropertyDefinition {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 126.

```text
roperties/v1/properties_subscription.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SubscriptionPropertyDefinition {
  SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11460"></a>
## FND-11460: chesscom.user_properties.v1.SubscriptionPropertyDefinition.SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 166.

```text
to
// syntax: proto3

package chesscom.user_properties.v1;

enum SubscriptionPropertyDefinition {
  SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT 
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11461"></a>
## FND-11461: chesscom.user_properties.v1.SubscriptionPropertyDefinition.LAST_TRANSITION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_TRANSITION = 1;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 207.

```text
er_properties.v1;

enum SubscriptionPropertyDefinition {
  SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11462"></a>
## FND-11462: chesscom.user_properties.v1.SubscriptionPropertyDefinition.MEMBERSHIP_LEVEL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL = 2;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 230.

```text
 SubscriptionPropertyDefinition {
  SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11463"></a>
## FND-11463: chesscom.user_properties.v1.SubscriptionPropertyDefinition.IS_TRIAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_TRIAL = 4;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 254.

```text
inition {
  SUBSCRIPTION_PROPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STA
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11464"></a>
## FND-11464: chesscom.user_properties.v1.SubscriptionPropertyDefinition.LTV = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LTV = 5;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 270.

```text
CRIPTION_PROPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEW
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11465"></a>
## FND-11465: chesscom.user_properties.v1.SubscriptionPropertyDefinition.LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 281.

```text
OPERTY_UNSPECIFIED = 0;
  LAST_TRANSITION = 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 1
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11466"></a>
## FND-11466: chesscom.user_properties.v1.SubscriptionPropertyDefinition.LAST_SUBSCRIPTION_ACTIVATION_DATE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 324.

```text
 1;
  MEMBERSHIP_LEVEL = 2;
  IS_TRIAL = 4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBER
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11467"></a>
## FND-11467: chesscom.user_properties.v1.SubscriptionPropertyDefinition.LAST_TRIAL_DEACTIVATION_DATE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_TRIAL_DEACTIVATION_DATE = 8;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 365.

```text
4;
  LTV = 5;
  LAST_SUBSCRIPTION_DEACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11468"></a>
## FND-11468: chesscom.user_properties.v1.SubscriptionPropertyDefinition.LAST_TRIAL_ACTIVATION_DATE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_TRIAL_ACTIVATION_DATE = 9;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 401.

```text
ACTIVATION_DATE = 6;
  LAST_SUBSCRIPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11469"></a>
## FND-11469: chesscom.user_properties.v1.SubscriptionPropertyDefinition.PLAN = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN = 10;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 435.

```text
IPTION_ACTIVATION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_PLAN_BILLING_AMOUNT = 23;
  IS_TRI
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11470"></a>
## FND-11470: chesscom.user_properties.v1.SubscriptionPropertyDefinition.PLAN_CODE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_CODE = 11;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 448.

```text
TION_DATE = 7;
  LAST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_PLAN_BILLING_AMOUNT = 23;
  IS_TRIAL_ELIGIBLE =
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11471"></a>
## FND-11471: chesscom.user_properties.v1.SubscriptionPropertyDefinition.PLAN_BILLING_AMOUNT = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_BILLING_AMOUNT = 12;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 466.

```text
AST_TRIAL_DEACTIVATION_DATE = 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_PLAN_BILLING_AMOUNT = 23;
  IS_TRIAL_ELIGIBLE = 24;
  CANCELLATIO
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11472"></a>
## FND-11472: chesscom.user_properties.v1.SubscriptionPropertyDefinition.PLAN_STATE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_STATE = 13;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 494.

```text
= 8;
  LAST_TRIAL_ACTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_PLAN_BILLING_AMOUNT = 23;
  IS_TRIAL_ELIGIBLE = 24;
  CANCELLATION_DATE = 25;
  CUMULATIVE_SP
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11473"></a>
## FND-11473: chesscom.user_properties.v1.SubscriptionPropertyDefinition.PAYMENT_METHOD = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD = 14;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 513.

```text
CTIVATION_DATE = 9;
  PLAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_PLAN_BILLING_AMOUNT = 23;
  IS_TRIAL_ELIGIBLE = 24;
  CANCELLATION_DATE = 25;
  CUMULATIVE_SPEND = 26;
  MEMBERS
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11474"></a>
## FND-11474: chesscom.user_properties.v1.SubscriptionPropertyDefinition.TRIAL_STATE = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRIAL_STATE = 15;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 536.

```text
LAN = 10;
  PLAN_CODE = 11;
  PLAN_BILLING_AMOUNT = 12;
  PLAN_STATE = 13;
  PAYMENT_METHOD = 14;
  TRIAL_STATE = 15;
  USER_LIFECYCLE_STATE = 16;
  RENEWAL_DATE = 17;
  IS_DEACTIVATED = 18;
  PREVIOUS_MEMBERSHIP_LEVEL = 19;
  PREVIOUS_PLAN = 21;
  PREVIOUS_PLAN_CODE = 22;
  PREVIOUS_PLAN_BILLING_AMOUNT = 23;
  IS_TRIAL_ELIGIBLE = 24;
  CANCELLATION_DATE = 25;
  CUMULATIVE_SPEND = 26;
  MEMBERSHIP_NAME = 27;
  PREVIO
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
