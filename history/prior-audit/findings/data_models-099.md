# data_models — findings 9801–9900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10075"></a>
## FND-10075: chesscom.user_properties.v1.ActivityProperty.last_lesson_history_reset_date = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_lesson_history_reset_date = 41;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5312.

```text
el_id {
  int32 completed_lesson_max_level_id = 39;
  }
  oneof _last_lesson_history_reset_date {
  .google.protobuf.Timestamp last_lesson_history_reset_date = 41;
  }
  oneof _blocked_by_count {
  int32 blocked_by_count = 42;
  }
  oneof _last_session_start_date {
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
 
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10076"></a>
## FND-10076: oneof declaration: chesscom.user_properties.v1.ActivityProperty._blocked_by_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _blocked_by_count {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5382.

```text
lesson_history_reset_date {
  .google.protobuf.Timestamp last_lesson_history_reset_date = 41;
  }
  oneof _blocked_by_count {
  int32 blocked_by_count = 42;
  }
  oneof _last_session_start_date {
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_pro
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10077"></a>
## FND-10077: chesscom.user_properties.v1.ActivityProperty.blocked_by_count = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 blocked_by_count = 42;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5410.

```text
  .google.protobuf.Timestamp last_lesson_history_reset_date = 41;
  }
  oneof _blocked_by_count {
  int32 blocked_by_count = 42;
  }
  oneof _last_session_start_date {
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneo
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10078"></a>
## FND-10078: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_session_start_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_session_start_date {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5445.

```text
esson_history_reset_date = 41;
  }
  oneof _blocked_by_count {
  int32 blocked_by_count = 42;
  }
  oneof _last_session_start_date {
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10079"></a>
## FND-10079: chesscom.user_properties.v1.ActivityProperty.last_session_start_date = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_session_start_date = 43;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5480.

```text
  oneof _blocked_by_count {
  int32 blocked_by_count = 42;
  }
  oneof _last_session_start_date {
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_i
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10080"></a>
## FND-10080: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_session_end_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_session_end_date {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5543.

```text
  oneof _last_session_start_date {
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_p
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10081"></a>
## FND-10081: chesscom.user_properties.v1.ActivityProperty.last_session_end_date = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_session_end_date = 44;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5576.

```text
{
  .google.protobuf.Timestamp last_session_start_date = 43;
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_g
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10082"></a>
## FND-10082: oneof declaration: chesscom.user_properties.v1.ActivityProperty._daily_games_in_progress_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_games_in_progress_count {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5637.

```text
  }
  oneof _last_session_end_date {
  .google.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_ga
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10083"></a>
## FND-10083: chesscom.user_properties.v1.ActivityProperty.daily_games_in_progress_count = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 daily_games_in_progress_count = 45;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5678.

```text
oogle.protobuf.Timestamp last_session_end_date = 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10084"></a>
## FND-10084: oneof declaration: chesscom.user_properties.v1.ActivityProperty._daily_games_chess_in_progress_to_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_games_chess_in_progress_to_move {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5726.

```text
 44;
  }
  oneof _daily_games_in_progress_count {
  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_t
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10085"></a>
## FND-10085: chesscom.user_properties.v1.ActivityProperty.daily_games_chess_in_progress_to_move = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 daily_games_chess_in_progress_to_move = 46;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5775.

```text

  int32 daily_games_in_progress_count = 45;
  }
  oneof _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_ti
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10086"></a>
## FND-10086: oneof declaration: chesscom.user_properties.v1.ActivityProperty._daily_games_chess960_in_progress_to_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_games_chess960_in_progress_to_move {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5831.

```text
 _daily_games_chess_in_progress_to_move {
  int32 daily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_time_percentage_used_to_move {
  int32 daily_games_chess96
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10087"></a>
## FND-10087: chesscom.user_properties.v1.ActivityProperty.daily_games_chess960_in_progress_to_move = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 daily_games_chess960_in_progress_to_move = 47;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5883.

```text
ily_games_chess_in_progress_to_move = 46;
  }
  oneof _daily_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_time_percentage_used_to_move {
  int32 daily_games_chess960_time_percentage_used_to_move = 49;
  }
  oneof _ol
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10088"></a>
## FND-10088: oneof declaration: chesscom.user_properties.v1.ActivityProperty._daily_games_chess_time_percentage_used_to_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_games_chess_time_percentage_used_to_move {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 5942.

```text
y_games_chess960_in_progress_to_move {
  int32 daily_games_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_time_percentage_used_to_move {
  int32 daily_games_chess960_time_percentage_used_to_move = 49;
  }
  oneof _old_mobile_client_played_on_lc_date {
  .google.protobuf.Time
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10089"></a>
## FND-10089: chesscom.user_properties.v1.ActivityProperty.daily_games_chess_time_percentage_used_to_move = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 daily_games_chess_time_percentage_used_to_move = 48;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6000.

```text
_chess960_in_progress_to_move = 47;
  }
  oneof _daily_games_chess_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_time_percentage_used_to_move {
  int32 daily_games_chess960_time_percentage_used_to_move = 49;
  }
  oneof _old_mobile_client_played_on_lc_date {
  .google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneo
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10090"></a>
## FND-10090: oneof declaration: chesscom.user_properties.v1.ActivityProperty._daily_games_chess960_time_percentage_used_to_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_games_chess960_time_percentage_used_to_move {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6065.

```text
s_time_percentage_used_to_move {
  int32 daily_games_chess_time_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_time_percentage_used_to_move {
  int32 daily_games_chess960_time_percentage_used_to_move = 49;
  }
  oneof _old_mobile_client_played_on_lc_date {
  .google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10091"></a>
## FND-10091: chesscom.user_properties.v1.ActivityProperty.daily_games_chess960_time_percentage_used_to_move = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 daily_games_chess960_time_percentage_used_to_move = 49;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6126.

```text
me_percentage_used_to_move = 48;
  }
  oneof _daily_games_chess960_time_percentage_used_to_move {
  int32 daily_games_chess960_time_percentage_used_to_move = 49;
  }
  oneof _old_mobile_client_played_on_lc_date {
  .google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_frien
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10092"></a>
## FND-10092: oneof declaration: chesscom.user_properties.v1.ActivityProperty._old_mobile_client_played_on_lc_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _old_mobile_client_played_on_lc_date {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6194.

```text
ime_percentage_used_to_move {
  int32 daily_games_chess960_time_percentage_used_to_move = 49;
  }
  oneof _old_mobile_client_played_on_lc_date {
  .google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10093"></a>
## FND-10093: chesscom.user_properties.v1.ActivityProperty.old_mobile_client_played_on_lc_date = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6241.

```text
es_chess960_time_percentage_used_to_move = 49;
  }
  oneof _old_mobile_client_played_on_lc_date {
  .google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10094"></a>
## FND-10094: oneof declaration: chesscom.user_properties.v1.ActivityProperty._blocked_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _blocked_count {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6316.

```text
nt_played_on_lc_date {
  .google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10095"></a>
## FND-10095: chesscom.user_properties.v1.ActivityProperty.blocked_count = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 blocked_count = 53;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6341.

```text
.google.protobuf.Timestamp old_mobile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_androi
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10096"></a>
## FND-10096: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_friend_removed_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_friend_removed_date {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6373.

```text
obile_client_played_on_lc_date = 52;
  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_a
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10097"></a>
## FND-10097: chesscom.user_properties.v1.ActivityProperty.last_friend_removed_date = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_friend_removed_date = 54;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6409.

```text

  }
  oneof _blocked_count {
  int32 blocked_count = 53;
  }
  oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneo
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10098"></a>
## FND-10098: oneof declaration: chesscom.user_properties.v1.ActivityProperty._added_to_iterable_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _added_to_iterable_date {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6473.

```text
oneof _last_friend_removed_date {
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10099"></a>
## FND-10099: chesscom.user_properties.v1.ActivityProperty.added_to_iterable_date = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp added_to_iterable_date = 55;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6507.

```text
  .google.protobuf.Timestamp last_friend_removed_date = 54;
  }
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10100"></a>
## FND-10100: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_ios_version_used

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_ios_version_used {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6569.

```text
}
  oneof _added_to_iterable_date {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date 
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10101"></a>
## FND-10101: chesscom.user_properties.v1.ActivityProperty.last_ios_version_used = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_ios_version_used = 56;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6602.

```text
 {
  .google.protobuf.Timestamp added_to_iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_c
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10102"></a>
## FND-10102: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_android_version_used

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_android_version_used {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6643.

```text
iterable_date = 55;
  }
  oneof _last_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Tim
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10103"></a>
## FND-10103: chesscom.user_properties.v1.ActivityProperty.last_android_version_used = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_android_version_used = 57;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6680.

```text
_ios_version_used {
  string last_ios_version_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10104"></a>
## FND-10104: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_web_version_used

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_web_version_used {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6725.

```text
_used = 56;
  }
  oneof _last_android_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10105"></a>
## FND-10105: chesscom.user_properties.v1.ActivityProperty.last_web_version_used = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_web_version_used = 58;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6758.

```text
roid_version_used {
  string last_android_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string acti
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10106"></a>
## FND-10106: oneof declaration: chesscom.user_properties.v1.ActivityProperty._learn_path_completed_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_path_completed_date {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6799.

```text
_version_used = 57;
  }
  oneof _last_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated 
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10107"></a>
## FND-10107: chesscom.user_properties.v1.ActivityProperty.learn_path_completed_date = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp learn_path_completed_date = 59;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6836.

```text
_web_version_used {
  string last_web_version_used = 58;
  }
  oneof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10108"></a>
## FND-10108: oneof declaration: chesscom.user_properties.v1.ActivityProperty._last_game_vs_computer_finished

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_game_vs_computer_finished {

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6901.

```text
eof _learn_path_completed_date {
  .google.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dat
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10109"></a>
## FND-10109: chesscom.user_properties.v1.ActivityProperty.last_game_vs_computer_finished = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_game_vs_computer_finished = 60;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 6943.

```text
.protobuf.Timestamp learn_path_completed_date = 59;
  }
  oneof _last_game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;
  repeated string daily_games_che
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10110"></a>
## FND-10110: chesscom.user_properties.v1.ActivityProperty.activity_streak_days = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string activity_streak_days = 13;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7013.

```text
game_vs_computer_finished {
  .google.protobuf.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;
  repeated string daily_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_pro
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10111"></a>
## FND-10111: chesscom.user_properties.v1.ActivityProperty.activity_streak_frozen_days = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string activity_streak_frozen_days = 14;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7058.

```text
f.Timestamp last_game_vs_computer_finished = 60;
  }
  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;
  repeated string daily_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_progress_ids = 51;
  repeated string last_live_t
```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10112"></a>
## FND-10112: chesscom.user_properties.v1.ActivityProperty.completed_lesson_level_ids = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 completed_lesson_level_ids = 38;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7110.

```text

  repeated string activity_streak_days = 13;
  repeated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;
  repeated string daily_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_progress_ids = 51;
  repeated string last_live_time_controls = 61;
}

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10113"></a>
## FND-10113: chesscom.user_properties.v1.ActivityProperty.last_lesson_completed_dates = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7160.

```text
peated string activity_streak_frozen_days = 14;
  repeated int32 completed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;
  repeated string daily_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_progress_ids = 51;
  repeated string last_live_time_controls = 61;
}

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10114"></a>
## FND-10114: chesscom.user_properties.v1.ActivityProperty.daily_games_chess_in_progress_ids = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string daily_games_chess_in_progress_ids = 50;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7232.

```text
ed_lesson_level_ids = 38;
  repeated .google.protobuf.Timestamp last_lesson_completed_dates = 40;
  repeated string daily_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_progress_ids = 51;
  repeated string last_live_time_controls = 61;
}

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10115"></a>
## FND-10115: chesscom.user_properties.v1.ActivityProperty.daily_games_chess960_in_progress_ids = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string daily_games_chess960_in_progress_ids = 51;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7290.

```text
stamp last_lesson_completed_dates = 40;
  repeated string daily_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_progress_ids = 51;
  repeated string last_live_time_controls = 61;
}

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10116"></a>
## FND-10116: chesscom.user_properties.v1.ActivityProperty.last_live_time_controls = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string last_live_time_controls = 61;

### Evidence

- **SRC-0601** `research/proto/chesscom/user_properties/v1/properties_activity.proto` — [preserved redacted evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto)
  Character offset 7351.

```text
ly_games_chess_in_progress_ids = 50;
  repeated string daily_games_chess960_in_progress_ids = 51;
  repeated string last_live_time_controls = 61;
}

```

**Source references:** SRC-0601, SRC-1572  
**URL references:** None independently associated  
**Related findings:** FND-09938, FND-09939, FND-09940

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10117"></a>
## FND-10117: enum declaration: chesscom.user_properties.v1.AnalysisPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AnalysisPropertyDefinition {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 122.

```text
er_properties/v1/properties_analysis.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum AnalysisPropertyDefinition {
  ANALYSIS_PROPERTY_UNSPECIFIED = 0;
  TOTAL_GAMES_ANALYZED = 1;
  TOTAL_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_F
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10118"></a>
## FND-10118: chesscom.user_properties.v1.AnalysisPropertyDefinition.ANALYSIS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 158.

```text
.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum AnalysisPropertyDefinition {
  ANALYSIS_PROPERTY_UNSPECIFIED = 0;
  TOTAL_GAMES_ANALYZED = 1;
  TOTAL_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10119"></a>
## FND-10119: chesscom.user_properties.v1.AnalysisPropertyDefinition.TOTAL_GAMES_ANALYZED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_GAMES_ANALYZED = 1;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 195.

```text
sscom.user_properties.v1;

enum AnalysisPropertyDefinition {
  ANALYSIS_PROPERTY_UNSPECIFIED = 0;
  TOTAL_GAMES_ANALYZED = 1;
  TOTAL_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT 
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10120"></a>
## FND-10120: chesscom.user_properties.v1.AnalysisPropertyDefinition.TOTAL_GAME_REVIEWS_REQUESTED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_GAME_REVIEWS_REQUESTED = 2;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 223.

```text
num AnalysisPropertyDefinition {
  ANALYSIS_PROPERTY_UNSPECIFIED = 0;
  TOTAL_GAMES_ANALYZED = 1;
  TOTAL_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10121"></a>
## FND-10121: chesscom.user_properties.v1.AnalysisPropertyDefinition.LAST_GAME_REVIEW_REQUESTED_DATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_GAME_REVIEW_REQUESTED_DATE = 3;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 259.

```text
NALYSIS_PROPERTY_UNSPECIFIED = 0;
  TOTAL_GAMES_ANALYZED = 1;
  TOTAL_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProp
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10122"></a>
## FND-10122: chesscom.user_properties.v1.AnalysisPropertyDefinition.IS_LAST_GAME_REVIEWED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_LAST_GAME_REVIEWED = 4;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 298.

```text
AL_GAMES_ANALYZED = 1;
  TOTAL_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10123"></a>
## FND-10123: chesscom.user_properties.v1.AnalysisPropertyDefinition.GAME_REVIEW_LAST_GAME_LEGACY_ID = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 327.

```text
L_GAME_REVIEWS_REQUESTED = 2;
  LAST_GAME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed 
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10124"></a>
## FND-10124: chesscom.user_properties.v1.AnalysisPropertyDefinition.GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 366.

```text
ME_REVIEW_REQUESTED_DATE = 3;
  IS_LAST_GAME_REVIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_re
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10125"></a>
## FND-10125: chesscom.user_properties.v1.AnalysisPropertyDefinition.GAME_REVIEW_LAST_GAME_FINAL_FEN = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 413.

```text
VIEWED = 4;
  GAME_REVIEW_LAST_GAME_LEGACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested 
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10126"></a>
## FND-10126: chesscom.user_properties.v1.AnalysisPropertyDefinition.GAME_REVIEW_LAST_GAME_TYPE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_LAST_GAME_TYPE = 8;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 452.

```text
ACY_ID = 5;
  GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requ
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10127"></a>
## FND-10127: chesscom.user_properties.v1.AnalysisPropertyDefinition.GAME_REVIEW_LAST_GAME_RESULT = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_LAST_GAME_RESULT = 9;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 486.

```text
E_OPPONENT_USERNAME = 6;
  GAME_REVIEW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Ti
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10128"></a>
## FND-10128: chesscom.user_properties.v1.AnalysisPropertyDefinition.GAME_REVIEW_LAST_GAME_COLOR = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_LAST_GAME_COLOR = 10;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 522.

```text
EW_LAST_GAME_FINAL_FEN = 7;
  GAME_REVIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_d
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10129"></a>
## FND-10129: message declaration: chesscom.user_properties.v1.AnalysisProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AnalysisProperty {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 559.

```text
VIEW_LAST_GAME_TYPE = 8;
  GAME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_re
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10130"></a>
## FND-10130: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._total_games_analyzed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_games_analyzed {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 588.

```text
ME_REVIEW_LAST_GAME_RESULT = 9;
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10131"></a>
## FND-10131: chesscom.user_properties.v1.AnalysisProperty.total_games_analyzed = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_games_analyzed = 1;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 620.

```text
  GAME_REVIEW_LAST_GAME_COLOR = 10;
}

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10132"></a>
## FND-10132: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._total_game_reviews_requested

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_game_reviews_requested {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 658.

```text

message AnalysisProperty {
  oneof _total_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 g
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10133"></a>
## FND-10133: chesscom.user_properties.v1.AnalysisProperty.total_game_reviews_requested = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_game_reviews_requested = 2;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 698.

```text
al_games_analyzed {
  int32 total_games_analyzed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10134"></a>
## FND-10134: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._last_game_review_requested_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_game_review_requested_date {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 744.

```text
ed = 1;
  }
  oneof _total_game_reviews_requested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_userna
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10135"></a>
## FND-10135: chesscom.user_properties.v1.AnalysisProperty.last_game_review_requested_date = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_game_review_requested_date = 3;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 787.

```text
uested {
  int32 total_game_reviews_requested = 2;
  }
  oneof _last_game_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponen
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10136"></a>
## FND-10136: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._is_last_game_reviewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_last_game_reviewed {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 857.

```text
ame_review_requested_date {
  .google.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  strin
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10137"></a>
## FND-10137: chesscom.user_properties.v1.AnalysisProperty.is_last_game_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_last_game_reviewed = 4;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 890.

```text
ogle.protobuf.Timestamp last_game_review_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10138"></a>
## FND-10138: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._game_review_last_game_legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_last_game_legacy_id {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 928.

```text
ew_requested_date = 3;
  }
  oneof _is_last_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_ga
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10139"></a>
## FND-10139: chesscom.user_properties.v1.AnalysisProperty.game_review_last_game_legacy_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 game_review_last_game_legacy_id = 5;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 971.

```text
_game_reviewed {
  bool is_last_game_reviewed = 4;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_ty
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10140"></a>
## FND-10140: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._game_review_last_game_opponent_username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_last_game_opponent_username {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1020.

```text
;
  }
  oneof _game_review_last_game_legacy_id {
  int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10141"></a>
## FND-10141: chesscom.user_properties.v1.AnalysisProperty.game_review_last_game_opponent_username = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_review_last_game_opponent_username = 6;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1071.

```text
int64 game_review_last_game_legacy_id = 5;
  }
  oneof _game_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
 
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10142"></a>
## FND-10142: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._game_review_last_game_final_fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_last_game_final_fen {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1129.

```text
me_review_last_game_opponent_username {
  string game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review
```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10143"></a>
## FND-10143: chesscom.user_properties.v1.AnalysisProperty.game_review_last_game_final_fen = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_review_last_game_final_fen = 7;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1172.

```text
tring game_review_last_game_opponent_username = 6;
  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10144"></a>
## FND-10144: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._game_review_last_game_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_last_game_type {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1222.

```text

  }
  oneof _game_review_last_game_final_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10145"></a>
## FND-10145: chesscom.user_properties.v1.AnalysisProperty.game_review_last_game_type = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_review_last_game_type = 8;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1260.

```text
nal_fen {
  string game_review_last_game_final_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10146"></a>
## FND-10146: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._game_review_last_game_result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_last_game_result {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1305.

```text
l_fen = 7;
  }
  oneof _game_review_last_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10147"></a>
## FND-10147: chesscom.user_properties.v1.AnalysisProperty.game_review_last_game_result = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_review_last_game_result = 9;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1345.

```text
_game_type {
  string game_review_last_game_type = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10148"></a>
## FND-10148: oneof declaration: chesscom.user_properties.v1.AnalysisProperty._game_review_last_game_color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_last_game_color {

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1392.

```text
e = 8;
  }
  oneof _game_review_last_game_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10149"></a>
## FND-10149: chesscom.user_properties.v1.AnalysisProperty.game_review_last_game_color = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_review_last_game_color = 10;

### Evidence

- **SRC-0602** `research/proto/chesscom/user_properties/v1/properties_analysis.proto` — [preserved redacted evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto)
  Character offset 1431.

```text
me_result {
  string game_review_last_game_result = 9;
  }
  oneof _game_review_last_game_color {
  string game_review_last_game_color = 10;
  }
}

```

**Source references:** SRC-0602, SRC-1573  
**URL references:** None independently associated  
**Related findings:** FND-10117, FND-10118, FND-10119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10150"></a>
## FND-10150: enum declaration: chesscom.user_properties.v1.AttributionPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AttributionPropertyDefinition {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 125.

```text
properties/v1/properties_attribution.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum AttributionPropertyDefinition {
  ATTRIBUTION_PROPERTY_UNSPECIFIED = 0;
  ATTRIBUTION_CAMPAIGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10151"></a>
## FND-10151: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 164.

```text
oto
// syntax: proto3

package chesscom.user_properties.v1;

enum AttributionPropertyDefinition {
  ATTRIBUTION_PROPERTY_UNSPECIFIED = 0;
  ATTRIBUTION_CAMPAIGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  o
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10152"></a>
## FND-10152: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_CAMPAIGN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_CAMPAIGN = 1;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 204.

```text
user_properties.v1;

enum AttributionPropertyDefinition {
  ATTRIBUTION_PROPERTY_UNSPECIFIED = 0;
  ATTRIBUTION_CAMPAIGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10153"></a>
## FND-10153: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_CONTENT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_CONTENT = 2;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 232.

```text
tributionPropertyDefinition {
  ATTRIBUTION_PROPERTY_UNSPECIFIED = 0;
  ATTRIBUTION_CAMPAIGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10154"></a>
## FND-10154: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_CREATE_DATE_TIME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_CREATE_DATE_TIME = 3;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 259.

```text
 {
  ATTRIBUTION_PROPERTY_UNSPECIFIED = 0;
  ATTRIBUTION_CAMPAIGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initi
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10155"></a>
## FND-10155: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_MEDIUM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_MEDIUM = 4;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 295.

```text
D = 0;
  ATTRIBUTION_CAMPAIGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10156"></a>
## FND-10156: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_REFERER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_REFERER = 5;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 321.

```text
IGN = 1;
  ATTRIBUTION_CONTENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof 
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10157"></a>
## FND-10157: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_ROUTE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_ROUTE = 6;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 348.

```text
ENT = 2;
  ATTRIBUTION_CREATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10158"></a>
## FND-10158: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_SOURCE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_SOURCE = 7;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 373.

```text
EATE_DATE_TIME = 3;
  ATTRIBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobu
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10159"></a>
## FND-10159: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_TERM = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_TERM = 8;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 399.

```text
IBUTION_MEDIUM = 4;
  ATTRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10160"></a>
## FND-10160: chesscom.user_properties.v1.AttributionPropertyDefinition.ATTRIBUTION_VERSION = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ATTRIBUTION_VERSION = 9;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 423.

```text
TRIBUTION_REFERER = 5;
  ATTRIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
 
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10161"></a>
## FND-10161: message declaration: chesscom.user_properties.v1.AttributionProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AttributionProperty {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 451.

```text
RIBUTION_ROUTE = 6;
  ATTRIBUTION_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_m
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10162"></a>
## FND-10162: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_campaign

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_campaign {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 483.

```text
N_SOURCE = 7;
  ATTRIBUTION_TERM = 8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10163"></a>
## FND-10163: chesscom.user_properties.v1.AttributionProperty.signup_initial_campaign = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_campaign = 1;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 518.

```text
8;
  ATTRIBUTION_VERSION = 9;
}

message AttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_ini
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10164"></a>
## FND-10164: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_content

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_content {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 560.

```text
ttributionProperty {
  oneof _signup_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_ref
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10165"></a>
## FND-10165: chesscom.user_properties.v1.AttributionProperty.signup_initial_content = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_content = 2;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 594.

```text
up_initial_campaign {
  string signup_initial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_init
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10166"></a>
## FND-10166: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_create_date_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_create_date_time {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 635.

```text
tial_campaign = 1;
  }
  oneof _signup_initial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10167"></a>
## FND-10167: chesscom.user_properties.v1.AttributionProperty.signup_initial_create_date_time = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp signup_initial_create_date_time = 3;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 678.

```text
ial_content {
  string signup_initial_content = 2;
  }
  oneof _signup_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10168"></a>
## FND-10168: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_medium

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_medium {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 748.

```text
_initial_create_date_time {
  .google.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10169"></a>
## FND-10169: chesscom.user_properties.v1.AttributionProperty.signup_initial_medium = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_medium = 4;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 781.

```text
ogle.protobuf.Timestamp signup_initial_create_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10170"></a>
## FND-10170: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_referer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_referer {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 821.

```text
reate_date_time = 3;
  }
  oneof _signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10171"></a>
## FND-10171: chesscom.user_properties.v1.AttributionProperty.signup_initial_referer = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_referer = 5;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 855.

```text
signup_initial_medium {
  string signup_initial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 
```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10172"></a>
## FND-10172: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_route

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_route {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 896.

```text
nitial_medium = 4;
  }
  oneof _signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10173"></a>
## FND-10173: chesscom.user_properties.v1.AttributionProperty.signup_initial_route = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_route = 6;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 928.

```text
signup_initial_referer {
  string signup_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10174"></a>
## FND-10174: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_source {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 967.

```text
p_initial_referer = 5;
  }
  oneof _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
