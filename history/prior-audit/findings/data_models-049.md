# data_models — findings 4801–4900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05075"></a>
## FND-05075: chesscom.game_gateway.v2.Criteria.color = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color color = 13;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4782.

```text
om = 11;
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
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05076"></a>
## FND-05076: oneof declaration: chesscom.game_gateway.v2.Criteria._are_friends

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _are_friends {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4825.

```text
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
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05077"></a>
## FND-05077: chesscom.game_gateway.v2.Criteria.are_friends = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool are_friends = 14;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4848.

```text
g_to = 12;
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
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05078"></a>
## FND-05078: oneof declaration: chesscom.game_gateway.v2.Criteria._theme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4877.

```text
 {
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
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05079"></a>
## FND-05079: chesscom.game_gateway.v2.Criteria.theme = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string theme = 15;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4894.

```text
ess.v1.Color color = 13;
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
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05080"></a>
## FND-05080: oneof declaration: chesscom.game_gateway.v2.Criteria._opponent_theme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opponent_theme {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4919.

```text
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
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05081"></a>
## FND-05081: chesscom.game_gateway.v2.Criteria.opponent_theme = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opponent_theme = 16;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4945.

```text

  bool are_friends = 14;
  }
  oneof _theme {
  string theme = 15;
  }
  oneof _opponent_theme {
  string opponent_theme = 16;
  }
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  one
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05082"></a>
## FND-05082: oneof declaration: chesscom.game_gateway.v2.Criteria._opening

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

<a id="FND-05083"></a>
## FND-05083: chesscom.game_gateway.v2.Criteria.opening = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_gateway.v2.OpeningCriteria opening = 17;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 4998.

```text
ng theme = 15;
  }
  oneof _opponent_theme {
  string opponent_theme = 16;
  }
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameP
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05084"></a>
## FND-05084: oneof declaration: chesscom.game_gateway.v2.Criteria._ply_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ply_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5060.

```text
_theme = 16;
  }
  oneof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bo
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05085"></a>
## FND-05085: chesscom.game_gateway.v2.Criteria.ply_from = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 ply_from = 18;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5080.

```text
neof _opening {
  .chesscom.game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05086"></a>
## FND-05086: oneof declaration: chesscom.game_gateway.v2.Criteria._ply_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ply_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5108.

```text
game_gateway.v2.OpeningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05087"></a>
## FND-05087: chesscom.game_gateway.v2.Criteria.ply_to = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 ply_to = 19;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5126.

```text
eningCriteria opening = 17;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tour
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05088"></a>
## FND-05088: oneof declaration: chesscom.game_gateway.v2.Criteria._base_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _base_time {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5152.

```text
;
  }
  oneof _ply_from {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneo
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05089"></a>
## FND-05089: chesscom.game_gateway.v2.Criteria.base_time = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 base_time = 20;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5173.

```text
om {
  uint32 ply_from = 18;
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05090"></a>
## FND-05090: oneof declaration: chesscom.game_gateway.v2.Criteria._time_increment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_increment {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5202.

```text
  }
  oneof _ply_to {
  uint32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05091"></a>
## FND-05091: chesscom.game_gateway.v2.Criteria.time_increment = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 time_increment = 21;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5228.

```text
nt32 ply_to = 19;
  }
  oneof _base_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05092"></a>
## FND-05092: oneof declaration: chesscom.game_gateway.v2.Criteria._game_provider

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_provider {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5262.

```text
e_time {
  uint32 base_time = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05093"></a>
## FND-05093: chesscom.game_gateway.v2.Criteria.game_provider = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v2.GameProvider game_provider = 23;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5287.

```text
me = 20;
  }
  oneof _time_increment {
  uint32 time_increment = 21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05094"></a>
## FND-05094: oneof declaration: chesscom.game_gateway.v2.Criteria._is_vs_computer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_vs_computer {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5352.

```text
21;
  }
  oneof _game_provider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05095"></a>
## FND-05095: chesscom.game_gateway.v2.Criteria.is_vs_computer = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_vs_computer = 24;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5378.

```text
ider {
  .chesscom.game_storage.v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_en
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05096"></a>
## FND-05096: oneof declaration: chesscom.game_gateway.v2.Criteria._tournament_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_id {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5410.

```text
v2.GameProvider game_provider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05097"></a>
## FND-05097: chesscom.game_gateway.v2.Criteria.tournament_id = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_id = 28;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5435.

```text
ider = 23;
  }
  oneof _is_vs_computer {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05098"></a>
## FND-05098: oneof declaration: chesscom.game_gateway.v2.Criteria._team_match_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _team_match_id {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5468.

```text
puter {
  bool is_vs_computer = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05099"></a>
## FND-05099: chesscom.game_gateway.v2.Criteria.team_match_id = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 team_match_id = 29;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5493.

```text
uter = 24;
  }
  oneof _tournament_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.proto
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05100"></a>
## FND-05100: oneof declaration: chesscom.game_gateway.v2.Criteria._is_tournament

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_tournament {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5526.

```text
t_id {
  uint32 tournament_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05101"></a>
## FND-05101: chesscom.game_gateway.v2.Criteria.is_tournament = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_tournament = 30;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5551.

```text
t_id = 28;
  }
  oneof _team_match_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_sta
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05102"></a>
## FND-05102: oneof declaration: chesscom.game_gateway.v2.Criteria._is_team_match

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_team_match {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5582.

```text
tch_id {
  uint32 team_match_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protob
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05103"></a>
## FND-05103: chesscom.game_gateway.v2.Criteria.is_team_match = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_team_match = 31;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5607.

```text
tch_id = 29;
  }
  oneof _is_tournament {
  bool is_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_t
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05104"></a>
## FND-05104: oneof declaration: chesscom.game_gateway.v2.Criteria._is_rated

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

<a id="FND-05105"></a>
## FND-05105: chesscom.game_gateway.v2.Criteria.is_rated = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_rated = 32;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5658.

```text
_tournament = 30;
  }
  oneof _is_team_match {
  bool is_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05106"></a>
## FND-05106: oneof declaration: chesscom.game_gateway.v2.Criteria._game_end_time_from

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

<a id="FND-05107"></a>
## FND-05107: chesscom.game_gateway.v2.Criteria.game_end_time_from = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_end_time_from = 33;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5714.

```text
_team_match = 31;
  }
  oneof _is_rated {
  bool is_rated = 32;
  }
  oneof _game_end_time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05108"></a>
## FND-05108: oneof declaration: chesscom.game_gateway.v2.Criteria._game_end_time_to

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

<a id="FND-05109"></a>
## FND-05109: chesscom.game_gateway.v2.Criteria.game_end_time_to = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_end_time_to = 34;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5800.

```text
time_from {
  .google.protobuf.Timestamp game_end_time_from = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05110"></a>
## FND-05110: oneof declaration: chesscom.game_gateway.v2.Criteria._game_start_time_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_start_time_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5856.

```text
rom = 33;
  }
  oneof _game_end_time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05111"></a>
## FND-05111: chesscom.game_gateway.v2.Criteria.game_start_time_from = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_start_time_from = 35;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5888.

```text
time_to {
  .google.protobuf.Timestamp game_end_time_to = 34;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05112"></a>
## FND-05112: oneof declaration: chesscom.game_gateway.v2.Criteria._game_start_time_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_start_time_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5948.

```text
;
  }
  oneof _game_start_time_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from =
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05113"></a>
## FND-05113: chesscom.game_gateway.v2.Criteria.game_start_time_to = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp game_start_time_to = 36;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 5978.

```text
_from {
  .google.protobuf.Timestamp game_start_time_from = 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05114"></a>
## FND-05114: oneof declaration: chesscom.game_gateway.v2.Criteria._page

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _page {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6036.

```text
= 35;
  }
  oneof _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05115"></a>
## FND-05115: chesscom.game_gateway.v2.Criteria.page = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 page = 38;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6052.

```text
f _game_start_time_to {
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05116"></a>
## FND-05116: oneof declaration: chesscom.game_gateway.v2.Criteria._page_size

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _page_size {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6076.

```text
  .google.protobuf.Timestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 4
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05117"></a>
## FND-05117: chesscom.game_gateway.v2.Criteria.page_size = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 page_size = 39;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6097.

```text
mestamp game_start_time_to = 36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05118"></a>
## FND-05118: oneof declaration: chesscom.game_gateway.v2.Criteria._sort_direction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sort_direction {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6126.

```text
36;
  }
  oneof _page {
  uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05119"></a>
## FND-05119: chesscom.game_gateway.v2.Criteria.sort_direction = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_gateway.v2.SortDirection sort_direction = 40;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6152.

```text
uint32 page = 38;
  }
  oneof _page_size {
  uint32 page_size = 39;
  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  o
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05120"></a>
## FND-05120: oneof declaration: chesscom.game_gateway.v2.Criteria._base_time_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _base_time_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6219.

```text

  }
  oneof _sort_direction {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_c
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05121"></a>
## FND-05121: chesscom.game_gateway.v2.Criteria.base_time_from = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 base_time_from = 42;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6245.

```text
on {
  .chesscom.game_gateway.v2.SortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brill
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05122"></a>
## FND-05122: oneof declaration: chesscom.game_gateway.v2.Criteria._base_time_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _base_time_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6279.

```text
ortDirection sort_direction = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05123"></a>
## FND-05123: chesscom.game_gateway.v2.Criteria.base_time_to = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 base_time_to = 43;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6303.

```text
ion = 40;
  }
  oneof _base_time_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05124"></a>
## FND-05124: oneof declaration: chesscom.game_gateway.v2.Criteria._time_increment_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_increment_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6335.

```text
_from {
  uint32 base_time_from = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05125"></a>
## FND-05125: chesscom.game_gateway.v2.Criteria.time_increment_from = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 time_increment_from = 44;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6366.

```text
 = 42;
  }
  oneof _base_time_to {
  uint32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05126"></a>
## FND-05126: oneof declaration: chesscom.game_gateway.v2.Criteria._time_increment_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_increment_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6405.

```text
nt32 base_time_to = 43;
  }
  oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accurac
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05127"></a>
## FND-05127: chesscom.game_gateway.v2.Criteria.time_increment_to = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 time_increment_to = 45;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6434.

```text
 oneof _time_increment_from {
  uint32 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05128"></a>
## FND-05128: oneof declaration: chesscom.game_gateway.v2.Criteria._player_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _player_id {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6471.

```text
2 time_increment_from = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  fl
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05129"></a>
## FND-05129: chesscom.game_gateway.v2.Criteria.player_id = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string player_id = 47;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6492.

```text
 = 44;
  }
  oneof _time_increment_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05130"></a>
## FND-05130: oneof declaration: chesscom.game_gateway.v2.Criteria._brilliant_count_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _brilliant_count_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6521.

```text
ement_to {
  uint32 time_increment_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05131"></a>
## FND-05131: chesscom.game_gateway.v2.Criteria.brilliant_count_from = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 brilliant_count_from = 49;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6553.

```text
nt_to = 45;
  }
  oneof _player_id {
  string player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05132"></a>
## FND-05132: oneof declaration: chesscom.game_gateway.v2.Criteria._brilliant_count_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _brilliant_count_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6593.

```text
tring player_id = 47;
  }
  oneof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05133"></a>
## FND-05133: chesscom.game_gateway.v2.Criteria.brilliant_count_to = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 brilliant_count_to = 50;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6623.

```text
eof _brilliant_count_from {
  uint32 brilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _r
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05134"></a>
## FND-05134: oneof declaration: chesscom.game_gateway.v2.Criteria._is_arena

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_arena {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6661.

```text
rilliant_count_from = 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_ord
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05135"></a>
## FND-05135: chesscom.game_gateway.v2.Criteria.is_arena = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_arena = 52;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6681.

```text
= 49;
  }
  oneof _brilliant_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05136"></a>
## FND-05136: oneof declaration: chesscom.game_gateway.v2.Criteria._has_accuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_accuracy {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6707.

```text
nt_count_to {
  uint32 brilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  boo
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05137"></a>
## FND-05137: chesscom.game_gateway.v2.Criteria.has_accuracy = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_accuracy = 53;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6731.

```text
rilliant_count_to = 50;
  }
  oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }

```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05138"></a>
## FND-05138: oneof declaration: chesscom.game_gateway.v2.Criteria._toggle_rate_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _toggle_rate_from {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6761.

```text
oneof _is_arena {
  bool is_arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05139"></a>
## FND-05139: chesscom.game_gateway.v2.Criteria.toggle_rate_from = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float toggle_rate_from = 54;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6789.

```text
arena = 52;
  }
  oneof _has_accuracy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05140"></a>
## FND-05140: oneof declaration: chesscom.game_gateway.v2.Criteria._toggle_rate_to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _toggle_rate_to {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6824.

```text
cy {
  bool has_accuracy = 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_id
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05141"></a>
## FND-05141: chesscom.game_gateway.v2.Criteria.toggle_rate_to = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float toggle_rate_to = 55;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6850.

```text
 53;
  }
  oneof _toggle_rate_from {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chessco
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05142"></a>
## FND-05142: oneof declaration: chesscom.game_gateway.v2.Criteria._is_vs_coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_vs_coach {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6883.

```text
m {
  float toggle_rate_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opp
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05143"></a>
## FND-05143: chesscom.game_gateway.v2.Criteria.is_vs_coach = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_vs_coach = 56;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6906.

```text
_from = 54;
  }
  oneof _toggle_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  rep
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05144"></a>
## FND-05144: oneof declaration: chesscom.game_gateway.v2.Criteria._random_order_seed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _random_order_seed {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6935.

```text
le_rate_to {
  float toggle_rate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.Time
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05145"></a>
## FND-05145: chesscom.game_gateway.v2.Criteria.random_order_seed = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string random_order_seed = 57;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 6964.

```text
ate_to = 55;
  }
  oneof _is_vs_coach {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  re
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05146"></a>
## FND-05146: oneof declaration: chesscom.game_gateway.v2.Criteria._is_favorite

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_favorite {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7001.

```text
 {
  bool is_vs_coach = 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.Game
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05147"></a>
## FND-05147: chesscom.game_gateway.v2.Criteria.is_favorite = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_favorite = 58;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7024.

```text
 56;
  }
  oneof _random_order_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 2
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05148"></a>
## FND-05148: oneof declaration: chesscom.game_gateway.v2.Criteria._tournament_round

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_round {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7053.

```text
r_seed {
  string random_order_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05149"></a>
## FND-05149: chesscom.game_gateway.v2.Criteria.tournament_round = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 tournament_round = 59;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7081.

```text
er_seed = 57;
  }
  oneof _is_favorite {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult play
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05150"></a>
## FND-05150: chesscom.game_gateway.v2.Criteria.opponent_ids = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string opponent_ids = 6;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7117.

```text
te {
  bool is_favorite = 58;
  }
  oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;
  repeated .chessco
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05151"></a>
## FND-05151: chesscom.game_gateway.v2.Criteria.opponent_titles = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7153.

```text
oneof _tournament_round {
  uint32 tournament_round = 59;
  }
  repeated string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;
  repeated .chesscom.game_storage.v2.PlayerResult oppon
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05152"></a>
## FND-05152: chesscom.game_gateway.v2.Criteria.time_classes = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.TimeClass time_classes = 22;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7223.

```text
ed string opponent_ids = 6;
  repeated .chesscom.game_storage.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;
  repeated .chesscom.game_storage.v2.PlayerResult opponent_player_results = 27;
  repeated .chesscom.chess.v1.Variant variant
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05153"></a>
## FND-05153: chesscom.game_gateway.v2.Criteria.game_results = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v2.GameResult game_results = 25;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7282.

```text
ge.v2.PlayerTitle opponent_titles = 8;
  repeated .chesscom.chess.v1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;
  repeated .chesscom.game_storage.v2.PlayerResult opponent_player_results = 27;
  repeated .chesscom.chess.v1.Variant variants = 37;
  repeated .chesscom.game_gateway.v2.SortField sort
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05154"></a>
## FND-05154: chesscom.game_gateway.v2.Criteria.player_results = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7349.

```text
1.TimeClass time_classes = 22;
  repeated .chesscom.game_storage.v2.GameResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;
  repeated .chesscom.game_storage.v2.PlayerResult opponent_player_results = 27;
  repeated .chesscom.chess.v1.Variant variants = 37;
  repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 to
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05155"></a>
## FND-05155: chesscom.game_gateway.v2.Criteria.opponent_player_results = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v2.PlayerResult opponent_player_results = 27;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7420.

```text
eResult game_results = 25;
  repeated .chesscom.game_storage.v2.PlayerResult player_results = 26;
  repeated .chesscom.game_storage.v2.PlayerResult opponent_player_results = 27;
  repeated .chesscom.chess.v1.Variant variants = 37;
  repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chessc
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05156"></a>
## FND-05156: chesscom.game_gateway.v2.Criteria.variants = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Variant variants = 37;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7500.

```text
yer_results = 26;
  repeated .chesscom.game_storage.v2.PlayerResult opponent_player_results = 27;
  repeated .chesscom.chess.v1.Variant variants = 37;
  repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriter
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05157"></a>
## FND-05157: chesscom.game_gateway.v2.Criteria.sort_fields = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7553.

```text
2.PlayerResult opponent_player_results = 27;
  repeated .chesscom.chess.v1.Variant variants = 37;
  repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Crit
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05158"></a>
## FND-05158: chesscom.game_gateway.v2.Criteria.game_ids = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string game_ids = 46;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7618.

```text
.chess.v1.Variant variants = 37;
  repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  op
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05159"></a>
## FND-05159: chesscom.game_gateway.v2.Criteria.tournament_ids = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 tournament_ids = 48;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7651.

```text
  repeated .chesscom.game_gateway.v2.SortField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

messa
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05160"></a>
## FND-05160: chesscom.game_gateway.v2.Criteria.arena_ids = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 arena_ids = 51;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7690.

```text
rtField sort_fields = 41;
  repeated string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional strin
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05161"></a>
## FND-05161: chesscom.game_gateway.v2.Criteria.player_titles = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7724.

```text
ed string game_ids = 46;
  repeated uint32 tournament_ids = 48;
  repeated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameRe
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05162"></a>
## FND-05162: message declaration: chesscom.game_gateway.v2.CountGamesByCriteriaRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CountGamesByCriteriaRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7794.

```text
ated uint32 arena_ids = 51;
  repeated .chesscom.game_storage.v2.PlayerTitle player_titles = 60;
}

message CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 l
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05163"></a>
## FND-05163: chesscom.game_gateway.v2.CountGamesByCriteriaRequest.criteria = 1

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

<a id="FND-05164"></a>
## FND-05164: message declaration: chesscom.game_gateway.v2.CountGamesByCriteriaResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CountGamesByCriteriaResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7895.

```text
essage CountGamesByCriteriaRequest {
  optional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeC
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05165"></a>
## FND-05165: chesscom.game_gateway.v2.CountGamesByCriteriaResponse.count = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint64 count = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7936.

```text
tional .chesscom.game_gateway.v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chessc
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05166"></a>
## FND-05166: message declaration: chesscom.game_gateway.v2.DeleteGameRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeleteGameRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7966.

```text
v2.Criteria criteria = 1;
}

message CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvide
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05167"></a>
## FND-05167: chesscom.game_gateway.v2.DeleteGameRequest.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 7996.

```text
essage CountGamesByCriteriaResponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optiona
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05168"></a>
## FND-05168: message declaration: chesscom.game_gateway.v2.DeleteGameResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeleteGameResponse {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8024.

```text
esponse {
  optional uint64 count = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optional bool is_vs_computer = 5;
 
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05169"></a>
## FND-05169: message declaration: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HydrateGameByLegacyIdRequest {

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8056.

```text
t = 1;
}

message DeleteGameRequest {
  optional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optional bool is_vs_computer = 5;
  optional .google.protobuf.Field
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05170"></a>
## FND-05170: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.legacy_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint64 legacy_id = 1;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8097.

```text
ptional string key = 1;
}

message DeleteGameResponse {
}

message HydrateGameByLegacyIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optional bool is_vs_computer = 5;
  optional .google.protobuf.FieldMask field_mask = 6;
  optional bool is_v
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05171"></a>
## FND-05171: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.variants = 2

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

<a id="FND-05172"></a>
## FND-05172: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.time_classes = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.TimeClass time_classes = 3;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8182.

```text
yIdRequest {
  optional uint64 legacy_id = 1;
  repeated .chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optional bool is_vs_computer = 5;
  optional .google.protobuf.FieldMask field_mask = 6;
  optional bool is_vs_coach = 7;
}

message HydrateGameByLegacyIdResponse {
  optional .chesscom.game_gat
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05173"></a>
## FND-05173: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.game_provider = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GameProvider game_provider = 4;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8240.

```text
chesscom.chess.v1.Variant variants = 2;
  repeated .chesscom.chess.v1.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
  optional bool is_vs_computer = 5;
  optional .google.protobuf.FieldMask field_mask = 6;
  optional bool is_vs_coach = 7;
}

message HydrateGameByLegacyIdResponse {
  optional .chesscom.game_gateway.v2.HydratedGame hydrated_game = 1;
}

message Opening
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05174"></a>
## FND-05174: chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest.is_vs_computer = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_vs_computer = 5;

### Evidence

- **SRC-0451** `research/proto/chesscom/game_gateway/v2/game_gateway_service.proto` — [preserved redacted evidence](../evidence/text/ed2d502e647730dbab0761c479cd0cc57450c5b5ac5de75b7c0f4b0630126190.proto)
  Character offset 8309.

```text
.TimeClass time_classes = 3;
  optional .chesscom.game_storage.v2.GameProvider game_provider = 4;
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
  uint32 eco_famil
```

**Source references:** SRC-0451, SRC-1422  
**URL references:** None independently associated  
**Related findings:** FND-04948, FND-04949, FND-04950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
