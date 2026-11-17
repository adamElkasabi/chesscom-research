# data_models — findings 11001–11100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11275"></a>
## FND-11275: chesscom.user_properties.v1.StatsDailyProperty.last_date = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_date = 43;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 4802.

```text
}
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 42;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 43;
  }
}

```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11276"></a>
## FND-11276: enum declaration: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum StatsDailyChess960PropertyDefinition {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 134.

```text
s/v1/properties_stats_daily_chess960.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum StatsDailyChess960PropertyDefinition {
  STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_CHESS960_LAST_GAME_DATE = 1;
  STATS_DAILY_CHESS960_CURRENT_STREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11277"></a>
## FND-11277: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 180.

```text
syntax: proto3

package chesscom.user_properties.v1;

enum StatsDailyChess960PropertyDefinition {
  STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_CHESS960_LAST_GAME_DATE = 1;
  STATS_DAILY_CHESS960_CURRENT_STREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE =
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11278"></a>
## FND-11278: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_LAST_GAME_DATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_LAST_GAME_DATE = 1;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 229.

```text
v1;

enum StatsDailyChess960PropertyDefinition {
  STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_CHESS960_LAST_GAME_DATE = 1;
  STATS_DAILY_CHESS960_CURRENT_STREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STAT
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11279"></a>
## FND-11279: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_CURRENT_STREAK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_CURRENT_STREAK = 2;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 272.

```text
ion {
  STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_CHESS960_LAST_GAME_DATE = 1;
  STATS_DAILY_CHESS960_CURRENT_STREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STAT
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11280"></a>
## FND-11280: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 315.

```text
CIFIED = 0;
  STATS_DAILY_CHESS960_LAST_GAME_DATE = 1;
  STATS_DAILY_CHESS960_CURRENT_STREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11281"></a>
## FND-11281: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 358.

```text
E_DATE = 1;
  STATS_DAILY_CHESS960_CURRENT_STREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING 
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11282"></a>
## FND-11282: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_RATING = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_RATING = 5;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 402.

```text
TREAK = 2;
  STATS_DAILY_CHESS960_MAX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_I
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11283"></a>
## FND-11283: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_RD = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_RD = 6;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 437.

```text
AX_WIN_STREAK = 3;
  STATS_DAILY_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTA
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11284"></a>
## FND-11284: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_IS_ACTIVE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_IS_ACTIVE = 7;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 468.

```text
Y_CHESS960_MAX_LOSS_STREAK = 4;
  STATS_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STAT
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11285"></a>
## FND-11285: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_IS_UNRATED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_IS_UNRATED = 8;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 506.

```text
S_DAILY_CHESS960_RATING = 5;
  STATS_DAILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11286"></a>
## FND-11286: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_HIGHEST_RATING = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_HIGHEST_RATING = 9;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 545.

```text
ILY_CHESS960_RD = 6;
  STATS_DAILY_CHESS960_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RAT
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11287"></a>
## FND-11287: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 588.

```text
_IS_ACTIVE = 7;
  STATS_DAILY_CHESS960_IS_UNRATED = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11288"></a>
## FND-11288: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 637.

```text
 = 8;
  STATS_DAILY_CHESS960_HIGHEST_RATING = 9;
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS9
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11289"></a>
## FND-11289: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 686.

```text
  STATS_DAILY_CHESS960_HIGHEST_RATING_DATE = 10;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960P
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11290"></a>
## FND-11290: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 732.

```text
0;
  STATS_DAILY_CHESS960_AVG_OPPONENT_RATING = 11;
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11291"></a>
## FND-11291: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 784.

```text
  STATS_DAILY_CHESS960_BEST_WIN_GAME_ID = 12;
  STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11292"></a>
## FND-11292: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 835.

```text
TS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT = 13;
  STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11293"></a>
## FND-11293: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 887.

```text
TS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT = 14;
  STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11294"></a>
## FND-11294: chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition.STATS_DAILY_CHESS960_LAST_DATE = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CHESS960_LAST_DATE = 17;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 939.

```text
S_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT = 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_stre
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11295"></a>
## FND-11295: message declaration: chesscom.user_properties.v1.StatsDailyChess960Property

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StatsDailyChess960Property {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 979.

```text
= 15;
  STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 ra
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11296"></a>
## FND-11296: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._last_game_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_game_date {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1018.

```text
D_LOSS_COUNT = 16;
  STATS_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd 
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11297"></a>
## FND-11297: chesscom.user_properties.v1.StatsDailyChess960Property.last_game_date = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_game_date = 1;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1044.

```text
_DAILY_CHESS960_LAST_DATE = 17;
}

message StatsDailyChess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_activ
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11298"></a>
## FND-11298: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._current_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_streak {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1097.

```text
Chess960Property {
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
 
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11299"></a>
## FND-11299: chesscom.user_properties.v1.StatsDailyChess960Property.current_streak = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 current_streak = 2;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1123.

```text
 _last_game_date {
  .google.protobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11300"></a>
## FND-11300: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._max_win_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_win_streak {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1155.

```text
tobuf.Timestamp last_game_date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int3
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11301"></a>
## FND-11301: chesscom.user_properties.v1.StatsDailyChess960Property.max_win_streak = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_win_streak = 3;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1181.

```text
date = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11302"></a>
## FND-11302: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._max_loss_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_loss_streak {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1213.

```text
treak {
  int32 current_streak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
 
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11303"></a>
## FND-11303: chesscom.user_properties.v1.StatsDailyChess960Property.max_loss_streak = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_loss_streak = 4;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1240.

```text
eak = 2;
  }
  oneof _max_win_streak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11304"></a>
## FND-11304: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1273.

```text
eak {
  int32 max_win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11305"></a>
## FND-11305: chesscom.user_properties.v1.StatsDailyChess960Property.rating = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 5;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1291.

```text
win_streak = 3;
  }
  oneof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponen
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11306"></a>
## FND-11306: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._rd

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rd {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1315.

```text
eof _max_loss_streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_o
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11307"></a>
## FND-11307: chesscom.user_properties.v1.StatsDailyChess960Property.rd = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float rd = 6;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1329.

```text
streak {
  int32 max_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11308"></a>
## FND-11308: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._is_active

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_active {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1349.

```text
_loss_streak = 4;
  }
  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11309"></a>
## FND-11309: chesscom.user_properties.v1.StatsDailyChess960Property.is_active = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_active = 7;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1370.

```text

  oneof _rating {
  int32 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11310"></a>
## FND-11310: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._is_unrated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_unrated {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1396.

```text
 rating = 5;
  }
  oneof _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 1
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11311"></a>
## FND-11311: chesscom.user_properties.v1.StatsDailyChess960Property.is_unrated = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_unrated = 8;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1418.

```text
of _rd {
  float rd = 6;
  }
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11312"></a>
## FND-11312: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._highest_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_rating {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1445.

```text
}
  oneof _is_active {
  bool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11313"></a>
## FND-11313: chesscom.user_properties.v1.StatsDailyChess960Property.highest_rating = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 highest_rating = 9;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1471.

```text
ool is_active = 7;
  }
  oneof _is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 1
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11314"></a>
## FND-11314: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._highest_rating_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_rating_date {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1503.

```text
is_unrated {
  bool is_unrated = 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11315"></a>
## FND-11315: chesscom.user_properties.v1.StatsDailyChess960Property.highest_rating_date = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp highest_rating_date = 10;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1534.

```text
= 8;
  }
  oneof _highest_rating {
  int32 highest_rating = 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11316"></a>
## FND-11316: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._avg_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avg_opponent_rating {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1593.

```text
 9;
  }
  oneof _highest_rating_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11317"></a>
## FND-11317: chesscom.user_properties.v1.StatsDailyChess960Property.avg_opponent_rating = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 avg_opponent_rating = 11;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1624.

```text
_date {
  .google.protobuf.Timestamp highest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11318"></a>
## FND-11318: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._best_win_game_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_win_game_id {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1662.

```text
ighest_rating_date = 10;
  }
  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11319"></a>
## FND-11319: chesscom.user_properties.v1.StatsDailyChess960Property.best_win_game_id = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 best_win_game_id = 12;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1690.

```text

  oneof _avg_opponent_rating {
  int32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11320"></a>
## FND-11320: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._total_rated_game_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_game_count {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1725.

```text
nt32 avg_opponent_rating = 11;
  }
  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11321"></a>
## FND-11321: chesscom.user_properties.v1.StatsDailyChess960Property.total_rated_game_count = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_game_count = 13;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1759.

```text

  oneof _best_win_game_id {
  int64 best_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_dat
```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11322"></a>
## FND-11322: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._total_rated_win_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_win_count {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1800.

```text
_win_game_id = 12;
  }
  oneof _total_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11323"></a>
## FND-11323: chesscom.user_properties.v1.StatsDailyChess960Property.total_rated_win_count = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_win_count = 14;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1833.

```text
otal_rated_game_count {
  int32 total_rated_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11324"></a>
## FND-11324: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._total_rated_loss_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_loss_count {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1873.

```text
ted_game_count = 13;
  }
  oneof _total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11325"></a>
## FND-11325: chesscom.user_properties.v1.StatsDailyChess960Property.total_rated_loss_count = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_loss_count = 15;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1907.

```text
total_rated_win_count {
  int32 total_rated_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11326"></a>
## FND-11326: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._total_rated_draw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_draw_count {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1948.

```text
ed_win_count = 14;
  }
  oneof _total_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11327"></a>
## FND-11327: chesscom.user_properties.v1.StatsDailyChess960Property.total_rated_draw_count = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_draw_count = 16;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 1982.

```text
tal_rated_loss_count {
  int32 total_rated_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11328"></a>
## FND-11328: oneof declaration: chesscom.user_properties.v1.StatsDailyChess960Property._last_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_date {

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 2023.

```text
d_loss_count = 15;
  }
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11329"></a>
## FND-11329: chesscom.user_properties.v1.StatsDailyChess960Property.last_date = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_date = 17;

### Evidence

- **SRC-0631** `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto` — [preserved redacted evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto)
  Character offset 2044.

```text
}
  oneof _total_rated_draw_count {
  int32 total_rated_draw_count = 16;
  }
  oneof _last_date {
  .google.protobuf.Timestamp last_date = 17;
  }
}

```

**Source references:** SRC-0631, SRC-1602  
**URL references:** None independently associated  
**Related findings:** FND-11276, FND-11277, FND-11278

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11330"></a>
## FND-11330: enum declaration: chesscom.user_properties.v1.StatsLivePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum StatsLivePropertyDefinition {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 124.

```text
_properties/v1/properties_stats_live.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum StatsLivePropertyDefinition {
  STATS_LIVE_PROPERTY_UNSPECIFIED = 0;
  STATS_LIVE_RATING = 1;
  STATS_LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  S
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11331"></a>
## FND-11331: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 161.

```text
proto
// syntax: proto3

package chesscom.user_properties.v1;

enum StatsLivePropertyDefinition {
  STATS_LIVE_PROPERTY_UNSPECIFIED = 0;
  STATS_LIVE_RATING = 1;
  STATS_LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11332"></a>
## FND-11332: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_RATING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_RATING = 1;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 200.

```text
om.user_properties.v1;

enum StatsLivePropertyDefinition {
  STATS_LIVE_PROPERTY_UNSPECIFIED = 0;
  STATS_LIVE_RATING = 1;
  STATS_LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHE
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11333"></a>
## FND-11333: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_GAME_TIME_CLASS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_GAME_TIME_CLASS = 2;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 225.

```text
num StatsLivePropertyDefinition {
  STATS_LIVE_PROPERTY_UNSPECIFIED = 0;
  STATS_LIVE_RATING = 1;
  STATS_LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  ST
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11334"></a>
## FND-11334: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOTAL_MOVE_COUNT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOTAL_MOVE_COUNT = 3;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 259.

```text
  STATS_LIVE_PROPERTY_UNSPECIFIED = 0;
  STATS_LIVE_RATING = 1;
  STATS_LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  ST
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11335"></a>
## FND-11335: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_UNRATED_GAME_COUNT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_UNRATED_GAME_COUNT = 4;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 294.

```text
 0;
  STATS_LIVE_RATING = 1;
  STATS_LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LI
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11336"></a>
## FND-11336: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_DISCONNECT_COUNT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_DISCONNECT_COUNT = 5;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 331.

```text
LIVE_GAME_TIME_CLASS = 2;
  STATS_LIVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STA
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11337"></a>
## FND-11337: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_BEST_WIN_GAME_ID = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_BEST_WIN_GAME_ID = 6;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 366.

```text
IVE_TOTAL_MOVE_COUNT = 3;
  STATS_LIVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11338"></a>
## FND-11338: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_HIGHEST_OPPONENT_RATING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 401.

```text
IVE_UNRATED_GAME_COUNT = 4;
  STATS_LIVE_DISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUN
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11339"></a>
## FND-11339: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_LAST_DATE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_LAST_DATE = 8;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 443.

```text
ISCONNECT_COUNT = 5;
  STATS_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUN
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11340"></a>
## FND-11340: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_HIGHEST_RATING = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_HIGHEST_RATING = 9;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 471.

```text
_LIVE_BEST_WIN_GAME_ID = 6;
  STATS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11341"></a>
## FND-11341: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_HIGHEST_RATING_DATE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_HIGHEST_RATING_DATE = 10;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 504.

```text
TS_LIVE_HIGHEST_OPPONENT_RATING = 7;
  STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WI
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11342"></a>
## FND-11342: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_LAST_GAME_DATE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_LAST_GAME_DATE = 11;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 543.

```text
STATS_LIVE_LAST_DATE = 8;
  STATS_LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_ST
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11343"></a>
## FND-11343: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_IS_ACTIVE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_IS_ACTIVE = 12;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 577.

```text
LIVE_HIGHEST_RATING = 9;
  STATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11344"></a>
## FND-11344: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 606.

```text
ATS_LIVE_HIGHEST_RATING_DATE = 10;
  STATS_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPON
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11345"></a>
## FND-11345: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 648.

```text
_LIVE_LAST_GAME_DATE = 11;
  STATS_LIVE_IS_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAM
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11346"></a>
## FND-11346: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 689.

```text
S_ACTIVE = 12;
  STATS_LIVE_TOTAL_RATED_GAME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11347"></a>
## FND-11347: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 731.

```text
ME_COUNT = 13;
  STATS_LIVE_TOTAL_RATED_WIN_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  ST
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11348"></a>
## FND-11348: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_CURRENT_STREAK = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_CURRENT_STREAK = 17;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 773.

```text
N_COUNT = 14;
  STATS_LIVE_TOTAL_RATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURN
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11349"></a>
## FND-11349: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_MAX_WIN_STREAK = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_MAX_WIN_STREAK = 18;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 807.

```text
ATED_LOSS_COUNT = 15;
  STATS_LIVE_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOU
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11350"></a>
## FND-11350: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_MAX_LOSS_STREAK = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_MAX_LOSS_STREAK = 19;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 841.

```text
_TOTAL_RATED_DRAW_COUNT = 16;
  STATS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STA
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11351"></a>
## FND-11351: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_IS_UNRATED = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_IS_UNRATED = 20;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 876.

```text
TS_LIVE_CURRENT_STREAK = 17;
  STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT 
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11352"></a>
## FND-11352: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_AVG_OPPONENT_RATING = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_AVG_OPPONENT_RATING = 21;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 906.

```text
 STATS_LIVE_MAX_WIN_STREAK = 18;
  STATS_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11353"></a>
## FND-11353: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_BEST_WIN_GAME = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_BEST_WIN_GAME = 22;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 945.

```text
S_LIVE_MAX_LOSS_STREAK = 19;
  STATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOUR
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11354"></a>
## FND-11354: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_MOVES_PER_GAME = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_MOVES_PER_GAME = 23;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 978.

```text
ATS_LIVE_IS_UNRATED = 20;
  STATS_LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_L
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11355"></a>
## FND-11355: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_ADJUDICATED_COUNT = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_ADJUDICATED_COUNT = 24;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1012.

```text
LIVE_AVG_OPPONENT_RATING = 21;
  STATS_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  S
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11356"></a>
## FND-11356: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_DW_COUNT = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_DW_COUNT = 25;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1049.

```text
S_LIVE_BEST_WIN_GAME = 22;
  STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;

```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11357"></a>
## FND-11357: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_COUNT = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_COUNT = 26;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1077.

```text
 STATS_LIVE_MOVES_PER_GAME = 23;
  STATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11358"></a>
## FND-11358: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1113.

```text
TATS_LIVE_ADJUDICATED_COUNT = 24;
  STATS_LIVE_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11359"></a>
## FND-11359: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1158.

```text
E_DW_COUNT = 25;
  STATS_LIVE_TOURNAMENT_COUNT = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11360"></a>
## FND-11360: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1204.

```text
 = 26;
  STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT = 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11361"></a>
## FND-11361: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_HOST_COUNT = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1250.

```text
= 27;
  STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMEN
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11362"></a>
## FND-11362: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_1ST_PLACE = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1291.

```text
OUNT = 28;
  STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAM
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11363"></a>
## FND-11363: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_2ND_PLACE = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1331.

```text
DRAW_COUNT = 29;
  STATS_LIVE_TOURNAMENT_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11364"></a>
## FND-11364: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_3RD_PLACE = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1371.

```text
_HOST_COUNT = 30;
  STATS_LIVE_TOURNAMENT_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAME
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11365"></a>
## FND-11365: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1411.

```text
T_1ST_PLACE = 31;
  STATS_LIVE_TOURNAMENT_2ND_PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURN
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11366"></a>
## FND-11366: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1457.

```text
PLACE = 32;
  STATS_LIVE_TOURNAMENT_3RD_PLACE = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
  STATS_LIVE_TOURNA
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11367"></a>
## FND-11367: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1502.

```text
 = 33;
  STATS_LIVE_TOURNAMENT_HOST_USER_COUNT = 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
  STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;
}

message StatsLi
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11368"></a>
## FND-11368: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1550.

```text
 34;
  STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
  STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;
}

message StatsLiveProperty {
  oneof _rating {
  uint32 rating =
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11369"></a>
## FND-11369: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_POINTS = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_POINTS = 38;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1593.

```text
 = 35;
  STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
  STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;
}

message StatsLiveProperty {
  oneof _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11370"></a>
## FND-11370: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1630.

```text
GRESS_COUNT = 36;
  STATS_LIVE_TOURNAMENT_CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
  STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;
}

message StatsLiveProperty {
  oneof _rating {
  uint32 rating = 1;
  }
  oneof _game_time_class {
  string game_time_class = 2;
  }
  oneof _to
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11371"></a>
## FND-11371: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1672.

```text
CANCEL_COUNT = 37;
  STATS_LIVE_TOURNAMENT_POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
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
  uint32 total_move_count
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11372"></a>
## FND-11372: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1715.

```text
POINTS = 38;
  STATS_LIVE_TOURNAMENT_COUNT_TOTAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
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
  u
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11373"></a>
## FND-11373: chesscom.user_properties.v1.StatsLivePropertyDefinition.STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS = 42;

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1760.

```text
TAL = 49;
  STATS_LIVE_TOURNAMENT_POINTS_TOTAL = 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
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
  oneof _di
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11374"></a>
## FND-11374: message declaration: chesscom.user_properties.v1.StatsLiveProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StatsLiveProperty {

### Evidence

- **SRC-0632** `research/proto/chesscom/user_properties/v1/properties_stats_live.proto` — [preserved redacted evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto)
  Character offset 1807.

```text
= 40;
  STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS = 41;
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
```

**Source references:** SRC-0632, SRC-1603  
**URL references:** None independently associated  
**Related findings:** FND-11330, FND-11331, FND-11332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
