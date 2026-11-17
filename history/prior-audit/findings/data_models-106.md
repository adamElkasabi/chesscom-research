# data_models — findings 10501–10600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10775"></a>
## FND-10775: chesscom.user_properties.v1.ProductActivityRankingsProperty.live_blitz_games_rank = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double live_blitz_games_rank = 12;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2151.

```text
ve_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10776"></a>
## FND-10776: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._live_rapid_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _live_rapid_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2192.

```text
et_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10777"></a>
## FND-10777: chesscom.user_properties.v1.ProductActivityRankingsProperty.live_rapid_games_rank = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double live_rapid_games_rank = 13;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2225.

```text
live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10778"></a>
## FND-10778: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._lesson_start_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lesson_start_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2266.

```text
tz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_even
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10779"></a>
## FND-10779: chesscom.user_properties.v1.ProductActivityRankingsProperty.lesson_start_rank = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double lesson_start_rank = 14;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2295.

```text
of _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _li
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10780"></a>
## FND-10780: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._social_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _social_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2332.

```text
live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_r
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10781"></a>
## FND-10781: chesscom.user_properties.v1.ProductActivityRankingsProperty.social_activity_rank = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double social_activity_rank = 15;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2364.

```text
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournamen
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10782"></a>
## FND-10782: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._bot_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bot_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2404.

```text
sson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10783"></a>
## FND-10783: chesscom.user_properties.v1.ProductActivityRankingsProperty.bot_games_rank = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double bot_games_rank = 16;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2430.

```text
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _t
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10784"></a>
## FND-10784: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._upgrade_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _upgrade_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2464.

```text
double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_ran
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10785"></a>
## FND-10785: chesscom.user_properties.v1.ProductActivityRankingsProperty.upgrade_activity_rank = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double upgrade_activity_rank = 17;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2497.

```text

  }
  oneof _bot_games_rank {
  double bot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushe
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10786"></a>
## FND-10786: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._active_events_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _active_events_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2538.

```text
ot_games_rank = 16;
  }
  oneof _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10787"></a>
## FND-10787: chesscom.user_properties.v1.ProductActivityRankingsProperty.active_events_rank = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double active_events_rank = 18;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2568.

```text
f _upgrade_activity_rank {
  double upgrade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10788"></a>
## FND-10788: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._live_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _live_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2606.

```text
grade_activity_rank = 17;
  }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10789"></a>
## FND-10789: chesscom.user_properties.v1.ProductActivityRankingsProperty.live_games_rank = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double live_games_rank = 19;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2633.

```text
 }
  oneof _active_events_rank {
  double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzz
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10790"></a>
## FND-10790: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._tournament_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2668.

```text
double active_events_rank = 18;
  }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_r
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10791"></a>
## FND-10791: chesscom.user_properties.v1.ProductActivityRankingsProperty.tournament_games_rank = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double tournament_games_rank = 20;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2701.

```text
 }
  oneof _live_games_rank {
  double live_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_st
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10792"></a>
## FND-10792: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._tactics_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tactics_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2742.

```text
ve_games_rank = 19;
  }
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_ran
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10793"></a>
## FND-10793: chesscom.user_properties.v1.ProductActivityRankingsProperty.tactics_rank = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double tactics_rank = 21;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2766.

```text
  oneof _tournament_games_rank {
  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _pra
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10794"></a>
## FND-10794: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._puzzle_rushes_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_rushes_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2798.

```text

  double tournament_games_rank = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  d
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10795"></a>
## FND-10795: chesscom.user_properties.v1.ProductActivityRankingsProperty.puzzle_rushes_rank = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double puzzle_rushes_rank = 22;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2828.

```text
k = 20;
  }
  oneof _tactics_rank {
  double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10796"></a>
## FND-10796: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._puzzle_battles_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_battles_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2866.

```text
double tactics_rank = 21;
  }
  oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_star
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10797"></a>
## FND-10797: chesscom.user_properties.v1.ProductActivityRankingsProperty.puzzle_battles_rank = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double puzzle_battles_rank = 23;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2897.

```text
 oneof _puzzle_rushes_rank {
  double puzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_st
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10798"></a>
## FND-10798: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._daily_puzzles_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_puzzles_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2936.

```text
uzzle_rushes_rank = 22;
  }
  oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_pag
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10799"></a>
## FND-10799: chesscom.user_properties.v1.ProductActivityRankingsProperty.daily_puzzles_rank = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double daily_puzzles_rank = 24;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2966.

```text
oneof _puzzle_battles_rank {
  double puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10800"></a>
## FND-10800: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._courses_started_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _courses_started_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3004.

```text
puzzle_battles_rank = 23;
  }
  oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _che
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10801"></a>
## FND-10801: chesscom.user_properties.v1.ProductActivityRankingsProperty.courses_started_rank = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double courses_started_rank = 25;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3036.

```text
oneof _daily_puzzles_rank {
  double daily_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  doubl
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10802"></a>
## FND-10802: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._practice_endgame_started_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _practice_endgame_started_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3076.

```text
ly_puzzles_rank = 24;
  }
  oneof _courses_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10803"></a>
## FND-10803: chesscom.user_properties.v1.ProductActivityRankingsProperty.practice_endgame_started_rank = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double practice_endgame_started_rank = 26;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3117.

```text
s_started_rank {
  double courses_started_rank = 25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10804"></a>
## FND-10804: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._analysis_started_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _analysis_started_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3166.

```text
25;
  }
  oneof _practice_endgame_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10805"></a>
## FND-10805: chesscom.user_properties.v1.ProductActivityRankingsProperty.analysis_started_rank = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double analysis_started_rank = 27;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3199.

```text
_started_rank {
  double practice_endgame_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_ra
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10806"></a>
## FND-10806: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._stats_page_views_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_page_views_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3240.

```text
_started_rank = 26;
  }
  oneof _analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10807"></a>
## FND-10807: chesscom.user_properties.v1.ProductActivityRankingsProperty.stats_page_views_rank = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double stats_page_views_rank = 28;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3273.

```text
analysis_started_rank {
  double analysis_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10808"></a>
## FND-10808: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._chess_tv_event_views_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chess_tv_event_views_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3314.

```text
_started_rank = 27;
  }
  oneof _stats_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  on
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10809"></a>
## FND-10809: chesscom.user_properties.v1.ProductActivityRankingsProperty.chess_tv_event_views_rank = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double chess_tv_event_views_rank = 29;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3351.

```text
s_page_views_rank {
  double stats_page_views_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double fr
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10810"></a>
## FND-10810: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._article_news_blog_forum_views_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _article_news_blog_forum_views_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3396.

```text
_rank = 28;
  }
  oneof _chess_tv_event_views_rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_in
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10811"></a>
## FND-10811: chesscom.user_properties.v1.ProductActivityRankingsProperty.article_news_blog_forum_views_rank = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double article_news_blog_forum_views_rank = 30;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3442.

```text
rank {
  double chess_tv_event_views_rank = 29;
  }
  oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10812"></a>
## FND-10812: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._social_shares_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _social_shares_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3496.

```text
oneof _article_news_blog_forum_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10813"></a>
## FND-10813: chesscom.user_properties.v1.ProductActivityRankingsProperty.social_shares_rank = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double social_shares_rank = 31;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3526.

```text
_views_rank {
  double article_news_blog_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10814"></a>
## FND-10814: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._chat_messages_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chat_messages_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3564.

```text
og_forum_views_rank = 30;
  }
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10815"></a>
## FND-10815: chesscom.user_properties.v1.ProductActivityRankingsProperty.chat_messages_rank = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double chat_messages_rank = 32;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3594.

```text
  oneof _social_shares_rank {
  double social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10816"></a>
## FND-10816: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._friends_added_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _friends_added_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3632.

```text
 social_shares_rank = 31;
  }
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10817"></a>
## FND-10817: chesscom.user_properties.v1.ProductActivityRankingsProperty.friends_added_rank = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double friends_added_rank = 33;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3662.

```text
  oneof _chat_messages_rank {
  double chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10818"></a>
## FND-10818: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._friend_invites_sent_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _friend_invites_sent_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3700.

```text
 chat_messages_rank = 32;
  }
  oneof _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10819"></a>
## FND-10819: chesscom.user_properties.v1.ProductActivityRankingsProperty.friend_invites_sent_rank = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double friend_invites_sent_rank = 34;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 3736.

```text
f _friends_added_rank {
  double friends_added_rank = 33;
  }
  oneof _friend_invites_sent_rank {
  double friend_invites_sent_rank = 34;
  }
}

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10820"></a>
## FND-10820: enum declaration: chesscom.user_properties.v1.PuzzleBattlePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleBattlePropertyDefinition {

### Evidence

- **SRC-0622** `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto` — [preserved redacted evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto)
  Character offset 127.

```text
operties/v1/properties_puzzle_battle.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PuzzleBattlePropertyDefinition {
  PUZZLES_BATTLE_UNSPECIFIED = 0;
  PUZZLE_BATTLE_WIN_STREAK = 1;
}

message PuzzleBattleProperty {
  oneof _win_streak {
  int32 win_streak = 1;
  }
}

```

**Source references:** SRC-0622, SRC-1593  
**URL references:** None independently associated  
**Related findings:** FND-10821, FND-10822

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10821"></a>
## FND-10821: chesscom.user_properties.v1.PuzzleBattlePropertyDefinition.PUZZLES_BATTLE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_BATTLE_UNSPECIFIED = 0;

### Evidence

- **SRC-0622** `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto` — [preserved redacted evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto)
  Character offset 167.

```text
to
// syntax: proto3

package chesscom.user_properties.v1;

enum PuzzleBattlePropertyDefinition {
  PUZZLES_BATTLE_UNSPECIFIED = 0;
  PUZZLE_BATTLE_WIN_STREAK = 1;
}

message PuzzleBattleProperty {
  oneof _win_streak {
  int32 win_streak = 1;
  }
}

```

**Source references:** SRC-0622, SRC-1593  
**URL references:** None independently associated  
**Related findings:** FND-10820, FND-10822

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10822"></a>
## FND-10822: chesscom.user_properties.v1.PuzzleBattlePropertyDefinition.PUZZLE_BATTLE_WIN_STREAK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_BATTLE_WIN_STREAK = 1;

### Evidence

- **SRC-0622** `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto` — [preserved redacted evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto)
  Character offset 201.

```text
scom.user_properties.v1;

enum PuzzleBattlePropertyDefinition {
  PUZZLES_BATTLE_UNSPECIFIED = 0;
  PUZZLE_BATTLE_WIN_STREAK = 1;
}

message PuzzleBattleProperty {
  oneof _win_streak {
  int32 win_streak = 1;
  }
}

```

**Source references:** SRC-0622, SRC-1593  
**URL references:** None independently associated  
**Related findings:** FND-10820, FND-10821

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10823"></a>
## FND-10823: message declaration: chesscom.user_properties.v1.PuzzleBattleProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleBattleProperty {

### Evidence

- **SRC-0622** `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto` — [preserved redacted evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto)
  Character offset 234.

```text
zzleBattlePropertyDefinition {
  PUZZLES_BATTLE_UNSPECIFIED = 0;
  PUZZLE_BATTLE_WIN_STREAK = 1;
}

message PuzzleBattleProperty {
  oneof _win_streak {
  int32 win_streak = 1;
  }
}

```

**Source references:** SRC-0622, SRC-1593  
**URL references:** None independently associated  
**Related findings:** FND-10820, FND-10821, FND-10822

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10824"></a>
## FND-10824: oneof declaration: chesscom.user_properties.v1.PuzzleBattleProperty._win_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _win_streak {

### Evidence

- **SRC-0622** `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto` — [preserved redacted evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto)
  Character offset 267.

```text
PUZZLES_BATTLE_UNSPECIFIED = 0;
  PUZZLE_BATTLE_WIN_STREAK = 1;
}

message PuzzleBattleProperty {
  oneof _win_streak {
  int32 win_streak = 1;
  }
}

```

**Source references:** SRC-0622, SRC-1593  
**URL references:** None independently associated  
**Related findings:** FND-10820, FND-10821, FND-10822

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10825"></a>
## FND-10825: chesscom.user_properties.v1.PuzzleBattleProperty.win_streak = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 win_streak = 1;

### Evidence

- **SRC-0622** `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto` — [preserved redacted evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto)
  Character offset 289.

```text
FIED = 0;
  PUZZLE_BATTLE_WIN_STREAK = 1;
}

message PuzzleBattleProperty {
  oneof _win_streak {
  int32 win_streak = 1;
  }
}

```

**Source references:** SRC-0622, SRC-1593  
**URL references:** None independently associated  
**Related findings:** FND-10820, FND-10821, FND-10822

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10826"></a>
## FND-10826: enum declaration: chesscom.user_properties.v1.PuzzleRushPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleRushPropertyDefinition {

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 125.

```text
properties/v1/properties_puzzle_rush.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PuzzleRushPropertyDefinition {
  PUZZLE_RUSH_UNSPECIFIED = 0;
  PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1;
  PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
 
```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10827"></a>
## FND-10827: chesscom.user_properties.v1.PuzzleRushPropertyDefinition.PUZZLE_RUSH_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_RUSH_UNSPECIFIED = 0;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 163.

```text
roto
// syntax: proto3

package chesscom.user_properties.v1;

enum PuzzleRushPropertyDefinition {
  PUZZLE_RUSH_UNSPECIFIED = 0;
  PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1;
  PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int
```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10828"></a>
## FND-10828: chesscom.user_properties.v1.PuzzleRushPropertyDefinition.PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 194.

```text
 chesscom.user_properties.v1;

enum PuzzleRushPropertyDefinition {
  PUZZLE_RUSH_UNSPECIFIED = 0;
  PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1;
  PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10829"></a>
## FND-10829: chesscom.user_properties.v1.PuzzleRushPropertyDefinition.PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 241.

```text
ropertyDefinition {
  PUZZLE_RUSH_UNSPECIFIED = 0;
  PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1;
  PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .g
```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10830"></a>
## FND-10830: chesscom.user_properties.v1.PuzzleRushPropertyDefinition.PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 283.

```text
IED = 0;
  PUZZLE_RUSH_NUMBER_OF_PUZZLE_RUSH_GAMES = 1;
  PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_
```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10831"></a>
## FND-10831: message declaration: chesscom.user_properties.v1.PuzzleRushProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleRushProperty {

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 331.

```text
ES = 1;
  PUZZLE_RUSH_BEST_PUZZLE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10832"></a>
## FND-10832: oneof declaration: chesscom.user_properties.v1.PuzzleRushProperty._number_of_puzzle_rush_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_puzzle_rush_games {

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 362.

```text
LE_RUSH_SCORE = 2;
  PUZZLE_RUSH_LAST_PUZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10833"></a>
## FND-10833: chesscom.user_properties.v1.PuzzleRushProperty.number_of_puzzle_rush_games = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_puzzle_rush_games = 1;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 401.

```text
UZZLE_RUSH_EVENT_DATE = 3;
}

message PuzzleRushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10834"></a>
## FND-10834: oneof declaration: chesscom.user_properties.v1.PuzzleRushProperty._best_puzzle_rush_score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_puzzle_rush_score {

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 446.

```text
ushProperty {
  oneof _number_of_puzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10835"></a>
## FND-10835: chesscom.user_properties.v1.PuzzleRushProperty.best_puzzle_rush_score = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 best_puzzle_rush_score = 2;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 480.

```text
uzzle_rush_games {
  int32 number_of_puzzle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10836"></a>
## FND-10836: oneof declaration: chesscom.user_properties.v1.PuzzleRushProperty._last_puzzle_rush_event_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_puzzle_rush_event_date {

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 520.

```text
zle_rush_games = 1;
  }
  oneof _best_puzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10837"></a>
## FND-10837: chesscom.user_properties.v1.PuzzleRushProperty.last_puzzle_rush_event_date = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_puzzle_rush_event_date = 3;

### Evidence

- **SRC-0623** `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto` — [preserved redacted evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto)
  Character offset 559.

```text
uzzle_rush_score {
  int32 best_puzzle_rush_score = 2;
  }
  oneof _last_puzzle_rush_event_date {
  .google.protobuf.Timestamp last_puzzle_rush_event_date = 3;
  }
}

```

**Source references:** SRC-0623, SRC-1594  
**URL references:** None independently associated  
**Related findings:** FND-10826, FND-10827, FND-10828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10838"></a>
## FND-10838: enum declaration: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzlesAttemptedPropertyDefinition {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 131.

```text
ties/v1/properties_puzzles_attempted.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PuzzlesAttemptedPropertyDefinition {
  PUZZLES_ATTEMPTED_UNSPECIFIED = 0;
  PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1;
  PUZZLES_ATTEMPTED_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10839"></a>
## FND-10839: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_UNSPECIFIED = 0;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 175.

```text
/ syntax: proto3

package chesscom.user_properties.v1;

enum PuzzlesAttemptedPropertyDefinition {
  PUZZLES_ATTEMPTED_UNSPECIFIED = 0;
  PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1;
  PUZZLES_ATTEMPTED_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10840"></a>
## FND-10840: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 212.

```text
er_properties.v1;

enum PuzzlesAttemptedPropertyDefinition {
  PUZZLES_ATTEMPTED_UNSPECIFIED = 0;
  PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1;
  PUZZLES_ATTEMPTED_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAM
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10841"></a>
## FND-10841: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_RATING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_RATING = 2;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 252.

```text
PropertyDefinition {
  PUZZLES_ATTEMPTED_UNSPECIFIED = 0;
  PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1;
  PUZZLES_ATTEMPTED_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10842"></a>
## FND-10842: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 284.

```text
TTEMPTED_UNSPECIFIED = 0;
  PUZZLES_ATTEMPTED_LAST_TIMESTAMP = 1;
  PUZZLES_ATTEMPTED_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATIN
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10843"></a>
## FND-10843: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 323.

```text
EMPTED_LAST_TIMESTAMP = 1;
  PUZZLES_ATTEMPTED_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_R
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10844"></a>
## FND-10844: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 368.

```text
D_RATING = 2;
  PUZZLES_ATTEMPTED_TOTAL_SECONDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10845"></a>
## FND-10845: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 412.

```text
NDS = 3;
  PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZ
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10846"></a>
## FND-10846: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MIN_RATING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MIN_RATING = 7;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 459.

```text
T = 4;
  PUZZLES_ATTEMPTED_RATED_PASSED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZ
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10847"></a>
## FND-10847: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 495.

```text
SED_COUNT = 5;
  PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIM
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10848"></a>
## FND-10848: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MAX_RATING = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MAX_RATING = 9;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 541.

```text
EMPT_COUNT = 6;
  PUZZLES_ATTEMPTED_MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10849"></a>
## FND-10849: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 577.

```text
MIN_RATING = 7;
  PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADO
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10850"></a>
## FND-10850: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 624.

```text
TIMESTAMP = 8;
  PUZZLES_ATTEMPTED_MAX_RATING = 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_R
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10851"></a>
## FND-10851: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 671.

```text
 9;
  PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP = 10;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_S
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10852"></a>
## FND-10852: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 728.

```text
LES_ATTEMPTED_RATED_LONGEST_STREAK = 11;
  PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10853"></a>
## FND-10853: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 775.

```text
LES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP = 12;
  PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHA
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10854"></a>
## FND-10854: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_SHADOW_RATING = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_SHADOW_RATING = 15;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 830.

```text
ZZLES_ATTEMPTED_RATED_CURRENT_STREAK = 13;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10855"></a>
## FND-10855: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 870.

```text
3;
  PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BO
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10856"></a>
## FND-10856: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 914.

```text
MESTAMP = 14;
  PUZZLES_ATTEMPTED_SHADOW_RATING = 15;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLE
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10857"></a>
## FND-10857: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 968.

```text
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING = 16;
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10858"></a>
## FND-10858: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1012.

```text
  PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP = 17;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAM
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10859"></a>
## FND-10859: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1066.

```text
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING = 18;
  PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10860"></a>
## FND-10860: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1114.

```text
ZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP = 19;
  PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp l
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10861"></a>
## FND-10861: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1166.

```text
PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING = 20;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rat
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10862"></a>
## FND-10862: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1228.

```text
TED_MIN_BOOSTED_SHADOW_RATING = 21;
  PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10863"></a>
## FND-10863: chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition.PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1280.

```text
TED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP = 22;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10864"></a>
## FND-10864: message declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzlesAttemptedProperty {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1343.

```text
ED_MAX_BOOSTED_SHADOW_RATING = 23;
  PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 ra
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10865"></a>
## FND-10865: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._last_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1380.

```text
PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _un
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10866"></a>
## FND-10866: chesscom.user_properties.v1.PuzzlesAttemptedProperty.last_timestamp = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_timestamp = 1;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1406.

```text
TED_SHADOW_RATING_TIMESTAMP = 24;
}

message PuzzlesAttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  in
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10867"></a>
## FND-10867: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1459.

```text
ttemptedProperty {
  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_ratin
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10868"></a>
## FND-10868: chesscom.user_properties.v1.PuzzlesAttemptedProperty.rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 2;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1477.

```text

  oneof _last_timestamp {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_ra
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10869"></a>
## FND-10869: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._total_seconds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_seconds {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1501.

```text
 {
  .google.protobuf.Timestamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _m
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10870"></a>
## FND-10870: chesscom.user_properties.v1.PuzzlesAttemptedProperty.total_seconds = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_seconds = 3;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1526.

```text
estamp last_timestamp = 1;
  }
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10871"></a>
## FND-10871: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._rated_attempt_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rated_attempt_count {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1557.

```text
  oneof _rating {
  int32 rating = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_r
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10872"></a>
## FND-10872: chesscom.user_properties.v1.PuzzlesAttemptedProperty.rated_attempt_count = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rated_attempt_count = 4;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1588.

```text
g = 2;
  }
  oneof _total_seconds {
  int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneo
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10873"></a>
## FND-10873: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._rated_passed_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rated_passed_count {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1625.

```text
 int32 total_seconds = 3;
  }
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10874"></a>
## FND-10874: chesscom.user_properties.v1.PuzzlesAttemptedProperty.rated_passed_count = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rated_passed_count = 5;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1655.

```text
  oneof _rated_attempt_count {
  int32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_tim
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
