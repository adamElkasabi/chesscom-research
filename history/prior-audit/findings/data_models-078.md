# data_models — findings 7701–7800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07975"></a>
## FND-07975: message declaration: chesscom.settings.v1.PuzzleSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSetting {

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 104.

```text
ource: chesscom/settings/v1/settings_puzzle.proto
// syntax: proto3

package chesscom.settings.v1;

message PuzzleSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String show_details = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_timer = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07976, FND-07977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07976"></a>
## FND-07976: oneof declaration: chesscom.settings.v1.PuzzleSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 130.

```text
1/settings_puzzle.proto
// syntax: proto3

package chesscom.settings.v1;

message PuzzleSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String show_details = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_timer = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07977"></a>
## FND-07977: chesscom.settings.v1.PuzzleSetting.show_details = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String show_details = 1;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 146.

```text
e.proto
// syntax: proto3

package chesscom.settings.v1;

message PuzzleSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String show_details = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_timer = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_mistake_feedbac
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07978"></a>
## FND-07978: chesscom.settings.v1.PuzzleSetting.show_timer = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_timer = 2;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 208.

```text
age PuzzleSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String show_details = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_timer = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_mistake_feedback = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_puzzl
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07979"></a>
## FND-07979: chesscom.settings.v1.PuzzleSetting.show_classic_mode = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 269.

```text
ettingValue.String show_details = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_timer = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_mistake_feedback = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_puzzle_goals = 6;
  .chesscom.settings.v1.SettingValue.Boolean col
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07980"></a>
## FND-07980: chesscom.settings.v1.PuzzleSetting.show_chat_hints = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 337.

```text
Value.Boolean show_timer = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_mistake_feedback = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_puzzle_goals = 6;
  .chesscom.settings.v1.SettingValue.Boolean collect_puzzle_points = 7;
  .chesscom.settings.v1.SettingValue.Boolean
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07981"></a>
## FND-07981: chesscom.settings.v1.PuzzleSetting.show_mistake_feedback = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_mistake_feedback = 5;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 403.

```text
.Boolean show_classic_mode = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_mistake_feedback = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_puzzle_goals = 6;
  .chesscom.settings.v1.SettingValue.Boolean collect_puzzle_points = 7;
  .chesscom.settings.v1.SettingValue.Boolean always_show_rating = 8;
  .chesscom.settings.v1.SettingValue.Stri
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07982"></a>
## FND-07982: chesscom.settings.v1.PuzzleSetting.show_puzzle_goals = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_puzzle_goals = 6;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 475.

```text
lean show_chat_hints = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_mistake_feedback = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_puzzle_goals = 6;
  .chesscom.settings.v1.SettingValue.Boolean collect_puzzle_points = 7;
  .chesscom.settings.v1.SettingValue.Boolean always_show_rating = 8;
  .chesscom.settings.v1.SettingValue.String difficulty_mode = 9;
  .chesscom.settings.v1.SettingValue.Boolean sho
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07983"></a>
## FND-07983: chesscom.settings.v1.PuzzleSetting.collect_puzzle_points = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean collect_puzzle_points = 7;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 543.

```text
an show_mistake_feedback = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_puzzle_goals = 6;
  .chesscom.settings.v1.SettingValue.Boolean collect_puzzle_points = 7;
  .chesscom.settings.v1.SettingValue.Boolean always_show_rating = 8;
  .chesscom.settings.v1.SettingValue.String difficulty_mode = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_hints_automatically = 10;
  .chesscom.settings.v1.SettingValue.Boo
```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07984"></a>
## FND-07984: chesscom.settings.v1.PuzzleSetting.always_show_rating = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean always_show_rating = 8;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 615.

```text
an show_puzzle_goals = 6;
  .chesscom.settings.v1.SettingValue.Boolean collect_puzzle_points = 7;
  .chesscom.settings.v1.SettingValue.Boolean always_show_rating = 8;
  .chesscom.settings.v1.SettingValue.String difficulty_mode = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_hints_automatically = 10;
  .chesscom.settings.v1.SettingValue.Boolean daily_puzzle_hard_mode = 11;
  }
}

```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07985"></a>
## FND-07985: chesscom.settings.v1.PuzzleSetting.difficulty_mode = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String difficulty_mode = 9;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 684.

```text
n collect_puzzle_points = 7;
  .chesscom.settings.v1.SettingValue.Boolean always_show_rating = 8;
  .chesscom.settings.v1.SettingValue.String difficulty_mode = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_hints_automatically = 10;
  .chesscom.settings.v1.SettingValue.Boolean daily_puzzle_hard_mode = 11;
  }
}

```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07986"></a>
## FND-07986: chesscom.settings.v1.PuzzleSetting.show_hints_automatically = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_hints_automatically = 10;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 749.

```text
.Boolean always_show_rating = 8;
  .chesscom.settings.v1.SettingValue.String difficulty_mode = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_hints_automatically = 10;
  .chesscom.settings.v1.SettingValue.Boolean daily_puzzle_hard_mode = 11;
  }
}

```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07987"></a>
## FND-07987: chesscom.settings.v1.PuzzleSetting.daily_puzzle_hard_mode = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean daily_puzzle_hard_mode = 11;

### Evidence

- **SRC-0538** `research/proto/chesscom/settings/v1/settings_puzzle.proto` — [preserved redacted evidence](../evidence/text/7c3a909964c77d6f4cfaa234a6e15831093bdb21b88575043b112ad26773ea00.proto)
  Character offset 825.

```text
 difficulty_mode = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_hints_automatically = 10;
  .chesscom.settings.v1.SettingValue.Boolean daily_puzzle_hard_mode = 11;
  }
}

```

**Source references:** SRC-0538, SRC-1509  
**URL references:** None independently associated  
**Related findings:** FND-07975, FND-07976, FND-07977

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07988"></a>
## FND-07988: message declaration: chesscom.settings.v1.ToasterCenterSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ToasterCenterSetting {

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 112.

```text
hesscom/settings/v1/settings_toaster_center.proto
// syntax: proto3

package chesscom.settings.v1;

message ToasterCenterSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean show_club_request_toasters = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_friend_request_toasters = 2;
  .chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;
  .chesscom.settings.v1.SettingValue.
```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07989, FND-07990

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07989"></a>
## FND-07989: oneof declaration: chesscom.settings.v1.ToasterCenterSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 145.

```text
ter_center.proto
// syntax: proto3

package chesscom.settings.v1;

message ToasterCenterSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean show_club_request_toasters = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_friend_request_toasters = 2;
  .chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_
```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07990

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07990"></a>
## FND-07990: chesscom.settings.v1.ToasterCenterSetting.show_club_request_toasters = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_club_request_toasters = 1;

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 161.

```text

// syntax: proto3

package chesscom.settings.v1;

message ToasterCenterSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean show_club_request_toasters = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_friend_request_toasters = 2;
  .chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_toasters = 4;
  
```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07989

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07991"></a>
## FND-07991: chesscom.settings.v1.ToasterCenterSetting.show_friend_request_toasters = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_friend_request_toasters = 2;

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 238.

```text
ng {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean show_club_request_toasters = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_friend_request_toasters = 2;
  .chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_toasters = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_move_made_toasters = 5;
  .ch
```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07989, FND-07990

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07992"></a>
## FND-07992: chesscom.settings.v1.ToasterCenterSetting.automatically_expand_toasters = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 317.

```text
uest_toasters = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_friend_request_toasters = 2;
  .chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_toasters = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_move_made_toasters = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_toasters = 6;
  }
}

```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07989, FND-07990

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07993"></a>
## FND-07993: chesscom.settings.v1.ToasterCenterSetting.show_tournament_reminder_toasters = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_toasters = 4;

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 397.

```text
est_toasters = 2;
  .chesscom.settings.v1.SettingValue.Boolean automatically_expand_toasters = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_toasters = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_move_made_toasters = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_toasters = 6;
  }
}

```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07989, FND-07990

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07994"></a>
## FND-07994: chesscom.settings.v1.ToasterCenterSetting.show_move_made_toasters = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_move_made_toasters = 5;

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 481.

```text
toasters = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_tournament_reminder_toasters = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_move_made_toasters = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_toasters = 6;
  }
}

```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07989, FND-07990

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07995"></a>
## FND-07995: chesscom.settings.v1.ToasterCenterSetting.show_toasters = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_toasters = 6;

### Evidence

- **SRC-0539** `research/proto/chesscom/settings/v1/settings_toaster_center.proto` — [preserved redacted evidence](../evidence/text/01b456860ad612e2a059ecf8ed424243c26bac4a52c30d05029b6efe601a8c1a.proto)
  Character offset 555.

```text
_reminder_toasters = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_move_made_toasters = 5;
  .chesscom.settings.v1.SettingValue.Boolean show_toasters = 6;
  }
}

```

**Source references:** SRC-0539, SRC-1510  
**URL references:** None independently associated  
**Related findings:** FND-07988, FND-07989, FND-07990

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07996"></a>
## FND-07996: message declaration: chesscom.settings.v1.UiSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UiSetting {

### Evidence

- **SRC-0540** `research/proto/chesscom/settings/v1/settings_ui.proto` — [preserved redacted evidence](../evidence/text/4586f45be3ed1a108893e8310c2063b2b13f3134be89083b3cb88ce184699e98.proto)
  Character offset 100.

```text
// source: chesscom/settings/v1/settings_ui.proto
// syntax: proto3

package chesscom.settings.v1;

message UiSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String mode = 1;
  .chesscom.settings.v1.SettingValue.Boolean enable_special_theme_forcing = 2;
  }
}

```

**Source references:** SRC-0540, SRC-1511  
**URL references:** None independently associated  
**Related findings:** FND-07997, FND-07998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07997"></a>
## FND-07997: oneof declaration: chesscom.settings.v1.UiSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0540** `research/proto/chesscom/settings/v1/settings_ui.proto` — [preserved redacted evidence](../evidence/text/4586f45be3ed1a108893e8310c2063b2b13f3134be89083b3cb88ce184699e98.proto)
  Character offset 122.

```text
ttings/v1/settings_ui.proto
// syntax: proto3

package chesscom.settings.v1;

message UiSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String mode = 1;
  .chesscom.settings.v1.SettingValue.Boolean enable_special_theme_forcing = 2;
  }
}

```

**Source references:** SRC-0540, SRC-1511  
**URL references:** None independently associated  
**Related findings:** FND-07996, FND-07998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07998"></a>
## FND-07998: chesscom.settings.v1.UiSetting.mode = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String mode = 1;

### Evidence

- **SRC-0540** `research/proto/chesscom/settings/v1/settings_ui.proto` — [preserved redacted evidence](../evidence/text/4586f45be3ed1a108893e8310c2063b2b13f3134be89083b3cb88ce184699e98.proto)
  Character offset 138.

```text
gs_ui.proto
// syntax: proto3

package chesscom.settings.v1;

message UiSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String mode = 1;
  .chesscom.settings.v1.SettingValue.Boolean enable_special_theme_forcing = 2;
  }
}

```

**Source references:** SRC-0540, SRC-1511  
**URL references:** None independently associated  
**Related findings:** FND-07996, FND-07997

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07999"></a>
## FND-07999: chesscom.settings.v1.UiSetting.enable_special_theme_forcing = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean enable_special_theme_forcing = 2;

### Evidence

- **SRC-0540** `research/proto/chesscom/settings/v1/settings_ui.proto` — [preserved redacted evidence](../evidence/text/4586f45be3ed1a108893e8310c2063b2b13f3134be89083b3cb88ce184699e98.proto)
  Character offset 192.

```text
gs.v1;

message UiSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String mode = 1;
  .chesscom.settings.v1.SettingValue.Boolean enable_special_theme_forcing = 2;
  }
}

```

**Source references:** SRC-0540, SRC-1511  
**URL references:** None independently associated  
**Related findings:** FND-07996, FND-07997, FND-07998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08000"></a>
## FND-08000: message declaration: chesscom.settings.v1.WatchSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message WatchSetting {

### Evidence

- **SRC-0541** `research/proto/chesscom/settings/v1/settings_watch.proto` — [preserved redacted evidence](../evidence/text/cad394230a01534d613729a1d90ebe34b85b1de99ba8ee862705c73e7f327eeb.proto)
  Character offset 103.

```text
source: chesscom/settings/v1/settings_watch.proto
// syntax: proto3

package chesscom.settings.v1;

message WatchSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean advanced_engine_settings = 1;
  .chesscom.settings.v1.SettingValue.Boolean player_names_above_and_below = 2;
  }
}

```

**Source references:** SRC-0541, SRC-1512  
**URL references:** None independently associated  
**Related findings:** FND-08001, FND-08002

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08001"></a>
## FND-08001: oneof declaration: chesscom.settings.v1.WatchSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0541** `research/proto/chesscom/settings/v1/settings_watch.proto` — [preserved redacted evidence](../evidence/text/cad394230a01534d613729a1d90ebe34b85b1de99ba8ee862705c73e7f327eeb.proto)
  Character offset 128.

```text
/v1/settings_watch.proto
// syntax: proto3

package chesscom.settings.v1;

message WatchSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean advanced_engine_settings = 1;
  .chesscom.settings.v1.SettingValue.Boolean player_names_above_and_below = 2;
  }
}

```

**Source references:** SRC-0541, SRC-1512  
**URL references:** None independently associated  
**Related findings:** FND-08000, FND-08002

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08002"></a>
## FND-08002: chesscom.settings.v1.WatchSetting.advanced_engine_settings = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean advanced_engine_settings = 1;

### Evidence

- **SRC-0541** `research/proto/chesscom/settings/v1/settings_watch.proto` — [preserved redacted evidence](../evidence/text/cad394230a01534d613729a1d90ebe34b85b1de99ba8ee862705c73e7f327eeb.proto)
  Character offset 144.

```text
ch.proto
// syntax: proto3

package chesscom.settings.v1;

message WatchSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean advanced_engine_settings = 1;
  .chesscom.settings.v1.SettingValue.Boolean player_names_above_and_below = 2;
  }
}

```

**Source references:** SRC-0541, SRC-1512  
**URL references:** None independently associated  
**Related findings:** FND-08000, FND-08001

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08003"></a>
## FND-08003: chesscom.settings.v1.WatchSetting.player_names_above_and_below = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean player_names_above_and_below = 2;

### Evidence

- **SRC-0541** `research/proto/chesscom/settings/v1/settings_watch.proto` — [preserved redacted evidence](../evidence/text/cad394230a01534d613729a1d90ebe34b85b1de99ba8ee862705c73e7f327eeb.proto)
  Character offset 219.

```text
ting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean advanced_engine_settings = 1;
  .chesscom.settings.v1.SettingValue.Boolean player_names_above_and_below = 2;
  }
}

```

**Source references:** SRC-0541, SRC-1512  
**URL references:** None independently associated  
**Related findings:** FND-08000, FND-08001, FND-08002

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08004"></a>
## FND-08004: enum declaration: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardAnalysisGameType {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 119.

```text
/shared_board/v1alpha/shared_board.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardAnalysisGameType {
  SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOAR
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08005"></a>
## FND-08005: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 156.

```text
oto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardAnalysisGameType {
  SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHA
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08006"></a>
## FND-08006: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 207.

```text
d.v1alpha;

enum SharedBoardAnalysisGameType {
  SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum 
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08007"></a>
## FND-08007: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 252.

```text
{
  SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_M
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08008"></a>
## FND-08008: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 296.

```text
IED = 0;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY = 1;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08009"></a>
## FND-08009: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 342.

```text
LY = 1;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08010"></a>
## FND-08010: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 385.

```text
IVE = 2;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTR
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08011"></a>
## FND-08011: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 428.

```text
MASTER = 3;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08012"></a>
## FND-08012: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType.SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 473.

```text
_PGN = 4;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB = 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string i
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08013"></a>
## FND-08013: enum declaration: chesscom.shared_board.v1alpha.SharedBoardKeyModifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardKeyModifier {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 522.

```text
 5;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  option
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08014"></a>
## FND-08014: chesscom.shared_board.v1alpha.SharedBoardKeyModifier.SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 554.

```text
_TYPE_COACH = 6;
  SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optiona
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08015"></a>
## FND-08015: chesscom.shared_board.v1alpha.SharedBoardKeyModifier.SHARED_BOARD_KEY_MODIFIER_NONE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_KEY_MODIFIER_NONE = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 599.

```text
_TYPE_COMPUTER = 7;
}

enum SharedBoardKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08016"></a>
## FND-08016: chesscom.shared_board.v1alpha.SharedBoardKeyModifier.SHARED_BOARD_KEY_MODIFIER_SHIFT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 637.

```text
dKeyModifier {
  SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn =
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08017"></a>
## FND-08017: chesscom.shared_board.v1alpha.SharedBoardKeyModifier.SHARED_BOARD_KEY_MODIFIER_CTRL = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_KEY_MODIFIER_CTRL = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 676.

```text
IER_UNSPECIFIED = 0;
  SHARED_BOARD_KEY_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  option
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08018"></a>
## FND-08018: chesscom.shared_board.v1alpha.SharedBoardKeyModifier.SHARED_BOARD_KEY_MODIFIER_ALT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_KEY_MODIFIER_ALT = 4;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 714.

```text
Y_MODIFIER_NONE = 1;
  SHARED_BOARD_KEY_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chessco
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08019"></a>
## FND-08019: message declaration: chesscom.shared_board.v1alpha.SharedBoard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoard {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 752.

```text
Y_MODIFIER_SHIFT = 2;
  SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSqua
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08020"></a>
## FND-08020: chesscom.shared_board.v1alpha.SharedBoard.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 776.

```text
SHARED_BOARD_KEY_MODIFIER_CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08021"></a>
## FND-08021: chesscom.shared_board.v1alpha.SharedBoard.session_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 802.

```text
CTRL = 3;
  SHARED_BOARD_KEY_MODIFIER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shar
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08022"></a>
## FND-08022: chesscom.shared_board.v1alpha.SharedBoard.user_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 836.

```text
IER_ALT = 4;
}

message SharedBoard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow 
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08023"></a>
## FND-08023: chesscom.shared_board.v1alpha.SharedBoard.flipped = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool flipped = 4;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 867.

```text
oard {
  optional string id = 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chessc
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08024"></a>
## FND-08024: chesscom.shared_board.v1alpha.SharedBoard.initial_position = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string initial_position = 5;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 896.

```text
 1;
  optional string session_id = 2;
  optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.Share
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08025"></a>
## FND-08025: chesscom.shared_board.v1alpha.SharedBoard.pgn = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn = 6;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 936.

```text
optional string user_id = 3;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  option
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08026"></a>
## FND-08026: chesscom.shared_board.v1alpha.SharedBoard.line = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 line = 7;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 963.

```text
;
  optional bool flipped = 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optio
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08027"></a>
## FND-08027: chesscom.shared_board.v1alpha.SharedBoard.move = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 move = 8;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 990.

```text
 4;
  optional string initial_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  o
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08028"></a>
## FND-08028: chesscom.shared_board.v1alpha.SharedBoard.squares = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1017.

```text
al_position = 5;
  optional string pgn = 6;
  optional int32 line = 7;
  optional int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08029"></a>
## FND-08029: chesscom.shared_board.v1alpha.SharedBoard.arrows = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1099.

```text
int32 move = 8;
  repeated .chesscom.shared_board.v1alpha.SharedBoardSquareHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protob
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08030"></a>
## FND-08030: chesscom.shared_board.v1alpha.SharedBoard.images = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1171.

```text
areHighlight squares = 9;
  repeated .chesscom.shared_board.v1alpha.SharedBoardArrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08031"></a>
## FND-08031: chesscom.shared_board.v1alpha.SharedBoard.draft = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool draft = 12;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1250.

```text
Arrow arrows = 10;
  repeated .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  option
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08032"></a>
## FND-08032: chesscom.shared_board.v1alpha.SharedBoard.version = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 version = 13;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1278.

```text
d .chesscom.shared_board.v1alpha.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08033"></a>
## FND-08033: chesscom.shared_board.v1alpha.SharedBoard.sequence = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 sequence = 14;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1309.

```text
a.SharedBoardImageMarking images = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08034"></a>
## FND-08034: chesscom.shared_board.v1alpha.SharedBoard.created_at = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 15;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1341.

```text
 = 11;
  optional bool draft = 12;
  optional int32 version = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.sh
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08035"></a>
## FND-08035: chesscom.shared_board.v1alpha.SharedBoard.updated_at = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp updated_at = 16;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1396.

```text
sion = 13;
  optional int32 sequence = 14;
  optional .google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_gam
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08036"></a>
## FND-08036: chesscom.shared_board.v1alpha.SharedBoard.source = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1451.

```text
google.protobuf.Timestamp created_at = 15;
  optional .google.protobuf.Timestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnal
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08037"></a>
## FND-08037: chesscom.shared_board.v1alpha.SharedBoard.hide_engine_lines = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool hide_engine_lines = 18;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1524.

```text
mestamp updated_at = 16;
  optional .chesscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSour
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08038"></a>
## FND-08038: chesscom.shared_board.v1alpha.SharedBoard.hide_move_list = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool hide_move_list = 19;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1564.

```text
sscom.shared_board.v1alpha.SharedBoardSource source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
 
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08039"></a>
## FND-08039: message declaration: chesscom.shared_board.v1alpha.SharedBoardSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSource {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1602.

```text
Source source = 17;
  optional bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  opt
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08040"></a>
## FND-08040: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardSource.source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof source {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1632.

```text
 bool hide_engine_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08041"></a>
## FND-08041: chesscom.shared_board.v1alpha.SharedBoardSource.event_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1649.

```text
_lines = 18;
  optional bool hide_move_list = 19;
}

message SharedBoardSource {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string g
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08042"></a>
## FND-08042: chesscom.shared_board.v1alpha.SharedBoardSource.analysis_game = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1725.

```text
ce {
  oneof source {
  .chesscom.shared_board.v1alpha.SharedBoardEventGameSource event_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .che
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08043"></a>
## FND-08043: message declaration: chesscom.shared_board.v1alpha.SharedBoardEventGameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardEventGameSource {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1812.

```text
_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .ch
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08044"></a>
## FND-08044: chesscom.shared_board.v1alpha.SharedBoardEventGameSource.event_slug = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string event_slug = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1851.

```text
lpha.SharedBoardAnalysisGameSource analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoard
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08045"></a>
## FND-08045: chesscom.shared_board.v1alpha.SharedBoardEventGameSource.round_slug = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string round_slug = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1885.

```text
 analysis_game = 2;
  }
}

message SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chessco
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08046"></a>
## FND-08046: chesscom.shared_board.v1alpha.SharedBoardEventGameSource.game_slug = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_slug = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1919.

```text
 SharedBoardEventGameSource {
  optional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedB
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08047"></a>
## FND-08047: chesscom.shared_board.v1alpha.SharedBoardEventGameSource.game_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_id = 4;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1952.

```text
ptional string event_slug = 1;
  optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
 
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08048"></a>
## FND-08048: message declaration: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardAnalysisGameSource {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 1984.

```text
 optional string round_slug = 2;
  optional string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
  optional string library_user_co
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08049"></a>
## FND-08049: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource.game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof game {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2026.

```text
l string game_slug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
  optional string library_user_collection_game_id = 1;
  optional string co
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08050"></a>
## FND-08050: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource.library_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2041.

```text
lug = 3;
  optional string game_id = 4;
}

message SharedBoardAnalysisGameSource {
  oneof game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
  optional string library_user_collection_game_id = 1;
  optional string collection_slug =
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08051"></a>
## FND-08051: chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource.chesscom_game = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2129.

```text
of game {
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource library_game = 1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
  optional string library_user_collection_game_id = 1;
  optional string collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

messa
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08052"></a>
## FND-08052: message declaration: chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardAnalysisLibraryGameSource {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2224.

```text
1;
  .chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
  optional string library_user_collection_game_id = 1;
  optional string collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoar
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08053"></a>
## FND-08053: chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource.library_user_collection_game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string library_user_collection_game_id = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2273.

```text
alysisChesscomGameSource chesscom_game = 2;
  }
}

message SharedBoardAnalysisLibraryGameSource {
  optional string library_user_collection_game_id = 1;
  optional string collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional strin
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08054"></a>
## FND-08054: chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource.collection_slug = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string collection_slug = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2328.

```text
age SharedBoardAnalysisLibraryGameSource {
  optional string library_user_collection_game_id = 1;
  optional string collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

mess
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08055"></a>
## FND-08055: chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource.library_item_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string library_item_id = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2367.

```text
e {
  optional string library_user_collection_game_id = 1;
  optional string collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  opti
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08056"></a>
## FND-08056: chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource.collection_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string collection_id = 4;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2406.

```text
ection_game_id = 1;
  optional string collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.Sha
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08057"></a>
## FND-08057: message declaration: chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardAnalysisChesscomGameSource {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2444.

```text
collection_slug = 2;
  optional string library_item_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08058"></a>
## FND-08058: chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource.game_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2494.

```text
m_id = 3;
  optional string collection_id = 4;
}

message SharedBoardAnalysisChesscomGameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08059"></a>
## FND-08059: chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource.game_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_id = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2579.

```text
GameSource {
  optional .chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKey
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08060"></a>
## FND-08060: chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource.game_uuid = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_uuid = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2610.

```text
om.shared_board.v1alpha.SharedBoardAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  op
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08061"></a>
## FND-08061: message declaration: chesscom.shared_board.v1alpha.SharedBoardSquareHighlight

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSquareHighlight {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2644.

```text
dAnalysisGameType game_type = 1;
  optional string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square f
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08062"></a>
## FND-08062: chesscom.shared_board.v1alpha.SharedBoardSquareHighlight.key_modifier = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2683.

```text
onal string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08063"></a>
## FND-08063: chesscom.shared_board.v1alpha.SharedBoardSquareHighlight.square = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2766.

```text
areHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  o
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08064"></a>
## FND-08064: message declaration: chesscom.shared_board.v1alpha.SharedBoardArrow

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardArrow {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2816.

```text
1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.ches
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08065"></a>
## FND-08065: chesscom.shared_board.v1alpha.SharedBoardArrow.key_modifier = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2683.

```text
onal string game_id = 2;
  optional string game_uuid = 3;
}

message SharedBoardSquareHighlight {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message SharedBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.
```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08066"></a>
## FND-08066: chesscom.shared_board.v1alpha.SharedBoardArrow.from = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square from = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2928.

```text
edBoardArrow {
  optional .chesscom.shared_board.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.chess.v1.Square square = 3;
}

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08067"></a>
## FND-08067: chesscom.shared_board.v1alpha.SharedBoardArrow.to = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square to = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 2975.

```text
d.v1alpha.SharedBoardKeyModifier key_modifier = 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.chess.v1.Square square = 3;
}

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08068"></a>
## FND-08068: message declaration: chesscom.shared_board.v1alpha.SharedBoardImageMarking

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardImageMarking {

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 3021.

```text
= 1;
  optional .chesscom.chess.v1.Square from = 2;
  optional .chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.chess.v1.Square square = 3;
}

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08069"></a>
## FND-08069: chesscom.shared_board.v1alpha.SharedBoardImageMarking.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string type = 1;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 3057.

```text
quare from = 2;
  optional .chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.chess.v1.Square square = 3;
}

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08070"></a>
## FND-08070: chesscom.shared_board.v1alpha.SharedBoardImageMarking.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 3085.

```text
chesscom.chess.v1.Square to = 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.chess.v1.Square square = 3;
}

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08071"></a>
## FND-08071: chesscom.shared_board.v1alpha.SharedBoardImageMarking.square = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square = 3;

### Evidence

- **SRC-0542** `research/proto/chesscom/shared_board/v1alpha/shared_board.proto` — [preserved redacted evidence](../evidence/text/10883b5ae44b1f372cdb75ded8ad328fdd8b0910c823e9edb2abc1692ef11467.proto)
  Character offset 3113.

```text
= 3;
}

message SharedBoardImageMarking {
  optional string type = 1;
  optional string name = 2;
  optional .chesscom.chess.v1.Square square = 3;
}

```

**Source references:** SRC-0542, SRC-1513  
**URL references:** None independently associated  
**Related findings:** FND-08004, FND-08005, FND-08006

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08072"></a>
## FND-08072: enum declaration: chesscom.shared_board.v1alpha.SharedBoardClockType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardClockType {

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 125.

```text
d_board/v1alpha/shared_board_clock.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardClockType {
  SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1;
  SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARE
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08073"></a>
## FND-08073: chesscom.shared_board.v1alpha.SharedBoardClockType.SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 155.

```text
lock.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardClockType {
  SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1;
  SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08074"></a>
## FND-08074: chesscom.shared_board.v1alpha.SharedBoardClockType.SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 198.

```text
com.shared_board.v1alpha;

enum SharedBoardClockType {
  SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1;
  SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
