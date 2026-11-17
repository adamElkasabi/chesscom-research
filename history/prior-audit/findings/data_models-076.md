# data_models — findings 7501–7600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07775"></a>
## FND-07775: message declaration: chesscom.settings.v1.HomeSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HomeSetting {

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 102.

```text
 source: chesscom/settings/v1/settings_home.proto
// syntax: proto3

package chesscom.settings.v1;

message HomeSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean recommended_games = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_recommended_activities = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .c
```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07776, FND-07777

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07776"></a>
## FND-07776: oneof declaration: chesscom.settings.v1.HomeSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 126.

```text
gs/v1/settings_home.proto
// syntax: proto3

package chesscom.settings.v1;

message HomeSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean recommended_games = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_recommended_activities = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .chesscom.settings.v1.Sett
```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07775, FND-07777

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07777"></a>
## FND-07777: chesscom.settings.v1.HomeSetting.recommended_games = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean recommended_games = 1;

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 142.

```text
ome.proto
// syntax: proto3

package chesscom.settings.v1;

message HomeSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean recommended_games = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_recommended_activities = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .chesscom.settings.v1.SettingValue.String 
```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07775, FND-07776

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07778"></a>
## FND-07778: chesscom.settings.v1.HomeSetting.show_recommended_activities = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_recommended_activities = 2;

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 210.

```text
HomeSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean recommended_games = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_recommended_activities = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .chesscom.settings.v1.SettingValue.String default_tab = 5;
  }
}

```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07775, FND-07776, FND-07777

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07779"></a>
## FND-07779: chesscom.settings.v1.HomeSetting.show_chess_tv = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 288.

```text
ommended_games = 1;
  .chesscom.settings.v1.SettingValue.Boolean show_recommended_activities = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .chesscom.settings.v1.SettingValue.String default_tab = 5;
  }
}

```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07775, FND-07776, FND-07777

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07780"></a>
## FND-07780: chesscom.settings.v1.HomeSetting.show_daily_puzzle = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 352.

```text
 show_recommended_activities = 2;
  .chesscom.settings.v1.SettingValue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .chesscom.settings.v1.SettingValue.String default_tab = 5;
  }
}

```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07775, FND-07776, FND-07777

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07781"></a>
## FND-07781: chesscom.settings.v1.HomeSetting.default_tab = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String default_tab = 5;

### Evidence

- **SRC-0532** `research/proto/chesscom/settings/v1/settings_home.proto` — [preserved redacted evidence](../evidence/text/376dfe77ad26de4e4bfc71ee6cea79726dfd7fade3e073f5fc89ae0287dcaab8.proto)
  Character offset 420.

```text
ue.Boolean show_chess_tv = 3;
  .chesscom.settings.v1.SettingValue.Boolean show_daily_puzzle = 4;
  .chesscom.settings.v1.SettingValue.String default_tab = 5;
  }
}

```

**Source references:** SRC-0532, SRC-1503  
**URL references:** None independently associated  
**Related findings:** FND-07775, FND-07776, FND-07777

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07782"></a>
## FND-07782: message declaration: chesscom.settings.v1.LearnSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LearnSetting {

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 103.

```text
source: chesscom/settings/v1/settings_learn.proto
// syntax: proto3

package chesscom.settings.v1;

message LearnSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coach = 1;
  .chesscom.settings.v1.SettingValue.String coach_id = 2;
  .chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07783, FND-07784

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07783"></a>
## FND-07783: oneof declaration: chesscom.settings.v1.LearnSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 128.

```text
/v1/settings_learn.proto
// syntax: proto3

package chesscom.settings.v1;

message LearnSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coach = 1;
  .chesscom.settings.v1.SettingValue.String coach_id = 2;
  .chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed 
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07784

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07784"></a>
## FND-07784: chesscom.settings.v1.LearnSetting.coach = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String coach = 1;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 144.

```text
rn.proto
// syntax: proto3

package chesscom.settings.v1;

message LearnSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coach = 1;
  .chesscom.settings.v1.SettingValue.String coach_id = 2;
  .chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;
  .chesscom
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07785"></a>
## FND-07785: chesscom.settings.v1.LearnSetting.coach_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String coach_id = 2;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 199.

```text
1;

message LearnSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coach = 1;
  .chesscom.settings.v1.SettingValue.String coach_id = 2;
  .chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;
  .
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07786"></a>
## FND-07786: chesscom.settings.v1.LearnSetting.coach_nudge = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 257.

```text
tings.v1.SettingValue.String coach = 1;
  .chesscom.settings.v1.SettingValue.String coach_id = 2;
  .chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;
  .chesscom.settings.v1.SettingValue.Boolean enable_motivatio
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07787"></a>
## FND-07787: chesscom.settings.v1.LearnSetting.enable_coach_voice = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 319.

```text
1.SettingValue.String coach_id = 2;
  .chesscom.settings.v1.SettingValue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;
  .chesscom.settings.v1.SettingValue.Boolean enable_motivational = 7;
  .chesscom.settings.v1.SettingValue.Boolean show_coa
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07788"></a>
## FND-07788: chesscom.settings.v1.LearnSetting.coach_voice_speed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 388.

```text
lue.Boolean coach_nudge = 3;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;
  .chesscom.settings.v1.SettingValue.Boolean enable_motivational = 7;
  .chesscom.settings.v1.SettingValue.Boolean show_coach_avatar_game_review = 8;
  .chesscom.settings.v1.SettingValue.Strin
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07789"></a>
## FND-07789: chesscom.settings.v1.LearnSetting.enable_coach = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 455.

```text
oolean enable_coach_voice = 4;
  .chesscom.settings.v1.SettingValue.Double coach_voice_speed = 5;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;
  .chesscom.settings.v1.SettingValue.Boolean enable_motivational = 7;
  .chesscom.settings.v1.SettingValue.Boolean show_coach_avatar_game_review = 8;
  .chesscom.settings.v1.SettingValue.String lesson_view = 9;
  .chesscom.settings.v1.SettingValue.Boolean aut
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07790"></a>
## FND-07790: chesscom.settings.v1.LearnSetting.enable_motivational = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean enable_motivational = 7;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 518.

```text
alue.Double coach_voice_speed = 5;
  .chesscom.settings.v1.SettingValue.Boolean enable_coach = 6;
  .chesscom.settings.v1.SettingValue.Boolean enable_motivational = 7;
  .chesscom.settings.v1.SettingValue.Boolean show_coach_avatar_game_review = 8;
  .chesscom.settings.v1.SettingValue.String lesson_view = 9;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_coach_games = 10;
  .chesscom.settings.v1.SettingValue.B
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07791"></a>
## FND-07791: chesscom.settings.v1.LearnSetting.show_coach_avatar_game_review = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_coach_avatar_game_review = 8;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 588.

```text
e.Boolean enable_coach = 6;
  .chesscom.settings.v1.SettingValue.Boolean enable_motivational = 7;
  .chesscom.settings.v1.SettingValue.Boolean show_coach_avatar_game_review = 8;
  .chesscom.settings.v1.SettingValue.String lesson_view = 9;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_coach_games = 10;
  .chesscom.settings.v1.SettingValue.Boolean skills_enabled = 11;
  .chesscom.settings.v1.SettingValue.Boole
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07792"></a>
## FND-07792: chesscom.settings.v1.LearnSetting.lesson_view = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String lesson_view = 9;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 668.

```text
motivational = 7;
  .chesscom.settings.v1.SettingValue.Boolean show_coach_avatar_game_review = 8;
  .chesscom.settings.v1.SettingValue.String lesson_view = 9;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_coach_games = 10;
  .chesscom.settings.v1.SettingValue.Boolean skills_enabled = 11;
  .chesscom.settings.v1.SettingValue.Boolean coach_evaluation_bar = 12;
  .chesscom.settings.v1.SettingValue.Boolean coach
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07793"></a>
## FND-07793: chesscom.settings.v1.LearnSetting.auto_save_coach_games = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_save_coach_games = 10;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 729.

```text
n show_coach_avatar_game_review = 8;
  .chesscom.settings.v1.SettingValue.String lesson_view = 9;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_coach_games = 10;
  .chesscom.settings.v1.SettingValue.Boolean skills_enabled = 11;
  .chesscom.settings.v1.SettingValue.Boolean coach_evaluation_bar = 12;
  .chesscom.settings.v1.SettingValue.Boolean coach_suggestion_arrows = 13;
  .chesscom.settings.v1.SettingValue
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07794"></a>
## FND-07794: chesscom.settings.v1.LearnSetting.skills_enabled = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean skills_enabled = 11;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 802.

```text
.String lesson_view = 9;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_coach_games = 10;
  .chesscom.settings.v1.SettingValue.Boolean skills_enabled = 11;
  .chesscom.settings.v1.SettingValue.Boolean coach_evaluation_bar = 12;
  .chesscom.settings.v1.SettingValue.Boolean coach_suggestion_arrows = 13;
  .chesscom.settings.v1.SettingValue.Boolean coach_threat_arrows = 14;
  .chesscom.settings.v1.SettingValue.B
```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07795"></a>
## FND-07795: chesscom.settings.v1.LearnSetting.coach_evaluation_bar = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_evaluation_bar = 12;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 868.

```text
ean auto_save_coach_games = 10;
  .chesscom.settings.v1.SettingValue.Boolean skills_enabled = 11;
  .chesscom.settings.v1.SettingValue.Boolean coach_evaluation_bar = 12;
  .chesscom.settings.v1.SettingValue.Boolean coach_suggestion_arrows = 13;
  .chesscom.settings.v1.SettingValue.Boolean coach_threat_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean teach_legal_moves = 15;
  }
}

```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07796"></a>
## FND-07796: chesscom.settings.v1.LearnSetting.coach_suggestion_arrows = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_suggestion_arrows = 13;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 940.

```text
lean skills_enabled = 11;
  .chesscom.settings.v1.SettingValue.Boolean coach_evaluation_bar = 12;
  .chesscom.settings.v1.SettingValue.Boolean coach_suggestion_arrows = 13;
  .chesscom.settings.v1.SettingValue.Boolean coach_threat_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean teach_legal_moves = 15;
  }
}

```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07797"></a>
## FND-07797: chesscom.settings.v1.LearnSetting.coach_threat_arrows = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_threat_arrows = 14;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 1015.

```text
h_evaluation_bar = 12;
  .chesscom.settings.v1.SettingValue.Boolean coach_suggestion_arrows = 13;
  .chesscom.settings.v1.SettingValue.Boolean coach_threat_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean teach_legal_moves = 15;
  }
}

```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07798"></a>
## FND-07798: chesscom.settings.v1.LearnSetting.teach_legal_moves = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean teach_legal_moves = 15;

### Evidence

- **SRC-0533** `research/proto/chesscom/settings/v1/settings_learn.proto` — [preserved redacted evidence](../evidence/text/eb36dabcaae85921c8962d484efd1b6d9a19f89b0a665ddd903505b0bae78a08.proto)
  Character offset 1086.

```text
ch_suggestion_arrows = 13;
  .chesscom.settings.v1.SettingValue.Boolean coach_threat_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean teach_legal_moves = 15;
  }
}

```

**Source references:** SRC-0533, SRC-1504  
**URL references:** None independently associated  
**Related findings:** FND-07782, FND-07783, FND-07784

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07799"></a>
## FND-07799: message declaration: chesscom.settings.v1.SettingMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SettingMetadata {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 106.

```text
rce: chesscom/settings/v1/settings_metadata.proto
// syntax: proto3

package chesscom.settings.v1;

message SettingMetadata {
  oneof _allow_null_values {
  bool allow_null_values = 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .c
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07800"></a>
## FND-07800: oneof declaration: chesscom.settings.v1.SettingMetadata._allow_null_values

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _allow_null_values {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 134.

```text
ttings_metadata.proto
// syntax: proto3

package chesscom.settings.v1;

message SettingMetadata {
  oneof _allow_null_values {
  bool allow_null_values = 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingV
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07801"></a>
## FND-07801: chesscom.settings.v1.SettingMetadata.allow_null_values = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool allow_null_values = 8;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 163.

```text
ax: proto3

package chesscom.settings.v1;

message SettingMetadata {
  oneof _allow_null_values {
  bool allow_null_values = 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  re
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07802"></a>
## FND-07802: chesscom.settings.v1.SettingMetadata.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 197.

```text
ngs.v1;

message SettingMetadata {
  oneof _allow_null_values {
  bool allow_null_values = 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.Setti
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07803"></a>
## FND-07803: chesscom.settings.v1.SettingMetadata.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 223.

```text
tadata {
  oneof _allow_null_values {
  bool allow_null_values = 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator valid
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07804"></a>
## FND-07804: chesscom.settings.v1.SettingMetadata.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 3;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 251.

```text
_values {
  bool allow_null_values = 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
   
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07805"></a>
## FND-07805: chesscom.settings.v1.SettingMetadata.type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.settings.v1.SettingMetadata.Type type = 4;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 286.

```text
= 8;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOO
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07806"></a>
## FND-07806: chesscom.settings.v1.SettingMetadata.default_value = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.settings.v1.SettingValue default_value = 5;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 350.

```text
 optional string description = 3;
  optional .chesscom.settings.v1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LO
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07807"></a>
## FND-07807: chesscom.settings.v1.SettingMetadata.allowed_values = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.settings.v1.SettingValue allowed_values = 6;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 415.

```text
1.SettingMetadata.Type type = 4;
  optional .chesscom.settings.v1.SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07808"></a>
## FND-07808: chesscom.settings.v1.SettingMetadata.validators = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 481.

```text
SettingValue default_value = 5;
  repeated .chesscom.settings.v1.SettingValue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeVal
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07809"></a>
## FND-07809: enum declaration: chesscom.settings.v1.SettingMetadata.Type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Type {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 556.

```text
ue allowed_values = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlan
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07810"></a>
## FND-07810: chesscom.settings.v1.SettingMetadata.Type.TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 572.

```text
s = 6;
  repeated .chesscom.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_b
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07811"></a>
## FND-07811: chesscom.settings.v1.SettingMetadata.Type.TYPE_BOOLEAN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE_BOOLEAN = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 598.

```text
m.settings.v1.SettingMetadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.sett
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07812"></a>
## FND-07812: chesscom.settings.v1.SettingMetadata.Type.TYPE_STRING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE_STRING = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 620.

```text
etadata.Validator validators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadat
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07813"></a>
## FND-07813: chesscom.settings.v1.SettingMetadata.Type.TYPE_INTEGER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE_INTEGER = 3;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 641.

```text
idators = 7;
  enum Type {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthVal
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07814"></a>
## FND-07814: chesscom.settings.v1.SettingMetadata.Type.TYPE_LONG = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE_LONG = 4;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 663.

```text
pe {
    TYPE_UNSPECIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07815"></a>
## FND-07815: chesscom.settings.v1.SettingMetadata.Type.TYPE_DOUBLE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE_DOUBLE = 5;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 682.

```text
CIFIED = 0;
    TYPE_BOOLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07816"></a>
## FND-07816: message declaration: chesscom.settings.v1.SettingMetadata.Validator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Validator {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 705.

```text
OLEAN = 1;
    TYPE_STRING = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Valid
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07817"></a>
## FND-07817: oneof declaration: chesscom.settings.v1.SettingMetadata.Validator.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 729.

```text
NG = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator rege
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07818"></a>
## FND-07818: chesscom.settings.v1.SettingMetadata.Validator.range = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 745.

```text
_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
   
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07819"></a>
## FND-07819: chesscom.settings.v1.SettingMetadata.Validator.not_blank = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 821.

```text
r {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07820"></a>
## FND-07820: chesscom.settings.v1.SettingMetadata.Validator.length = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 904.

```text
tor range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07821"></a>
## FND-07821: chesscom.settings.v1.SettingMetadata.Validator.regex = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingMetadata.Validator.RegexValidator regex = 4;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 982.

```text
ator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
     
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07822"></a>
## FND-07822: message declaration: chesscom.settings.v1.SettingMetadata.Validator.RangeValidator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RangeValidator {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1066.

```text
r length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07823"></a>
## FND-07823: oneof declaration: chesscom.settings.v1.SettingMetadata.Validator.RangeValidator._min

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1097.

```text
ngs.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07824"></a>
## FND-07824: chesscom.settings.v1.SettingMetadata.Validator.RangeValidator.min = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1112.

```text
etadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message Sett
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07825"></a>
## FND-07825: oneof declaration: chesscom.settings.v1.SettingMetadata.Validator.RangeValidator._max

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1141.

```text
tor regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07826"></a>
## FND-07826: chesscom.settings.v1.SettingMetadata.Validator.RangeValidator.max = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1156.

```text
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.setti
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07827"></a>
## FND-07827: message declaration: chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NotBlankValidator {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1189.

```text
{
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boole
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07828"></a>
## FND-07828: message declaration: chesscom.settings.v1.SettingMetadata.Validator.LengthValidator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LengthValidator {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1227.

```text
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.Settin
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07829"></a>
## FND-07829: oneof declaration: chesscom.settings.v1.SettingMetadata.Validator.LengthValidator._min

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1097.

```text
ngs.v1.SettingMetadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07830"></a>
## FND-07830: chesscom.settings.v1.SettingMetadata.Validator.LengthValidator.min = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1112.

```text
etadata.Validator.RegexValidator regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message Sett
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07831"></a>
## FND-07831: oneof declaration: chesscom.settings.v1.SettingMetadata.Validator.LengthValidator._max

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1141.

```text
tor regex = 4;
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07832"></a>
## FND-07832: chesscom.settings.v1.SettingMetadata.Validator.LengthValidator.max = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1156.

```text
    }
    message RangeValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message NotBlankValidator {
    }
    message LengthValidator {
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.setti
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07833"></a>
## FND-07833: message declaration: chesscom.settings.v1.SettingMetadata.Validator.RegexValidator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RegexValidator {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1351.

```text
{
      oneof _min {
  int32 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Lon
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07834"></a>
## FND-07834: chesscom.settings.v1.SettingMetadata.Validator.RegexValidator.pattern = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pattern = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1378.

```text
2 min = 1;
      }
      oneof _max {
  int32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.set
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07835"></a>
## FND-07835: message declaration: chesscom.settings.v1.SettingValue

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SettingValue {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1420.

```text
t32 max = 2;
      }
    }
    message RegexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07836"></a>
## FND-07836: oneof declaration: chesscom.settings.v1.SettingValue.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 729.

```text
NG = 2;
    TYPE_INTEGER = 3;
    TYPE_LONG = 4;
    TYPE_DOUBLE = 5;
  }
  message Validator {
    oneof value {
  .chesscom.settings.v1.SettingMetadata.Validator.RangeValidator range = 1;
  .chesscom.settings.v1.SettingMetadata.Validator.NotBlankValidator not_blank = 2;
  .chesscom.settings.v1.SettingMetadata.Validator.LengthValidator length = 3;
  .chesscom.settings.v1.SettingMetadata.Validator.RegexValidator rege
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07837"></a>
## FND-07837: chesscom.settings.v1.SettingValue.boolean = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean boolean = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1461.

```text
gexValidator {
  optional string pattern = 1;
    }
  }
}

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07838"></a>
## FND-07838: chesscom.settings.v1.SettingValue.string = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String string = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1519.

```text

message SettingValue {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07839"></a>
## FND-07839: chesscom.settings.v1.SettingValue.integer = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer integer = 3;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1575.

```text
ings.v1.SettingValue.Boolean boolean = 1;
  .chesscom.settings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07840"></a>
## FND-07840: chesscom.settings.v1.SettingValue.long = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Long long = 4;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1633.

```text
ings.v1.SettingValue.String string = 2;
  .chesscom.settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07841"></a>
## FND-07841: chesscom.settings.v1.SettingValue.double = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Double double = 5;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1685.

```text
settings.v1.SettingValue.Integer integer = 3;
  .chesscom.settings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07842"></a>
## FND-07842: message declaration: chesscom.settings.v1.SettingValue.Boolean

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Boolean {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1745.

```text
ttings.v1.SettingValue.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
   
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07843"></a>
## FND-07843: oneof declaration: chesscom.settings.v1.SettingValue.Boolean.wrapped_value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof wrapped_value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1767.

```text
.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07844"></a>
## FND-07844: chesscom.settings.v1.SettingValue.Boolean.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool value = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1791.

```text
com.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_valu
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07845"></a>
## FND-07845: chesscom.settings.v1.SettingValue.Boolean.null = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Empty null = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1809.

```text
ttingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07846"></a>
## FND-07846: message declaration: chesscom.settings.v1.SettingValue.String

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message String {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1854.

```text
oolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07847"></a>
## FND-07847: oneof declaration: chesscom.settings.v1.SettingValue.String.wrapped_value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof wrapped_value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1767.

```text
.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07848"></a>
## FND-07848: chesscom.settings.v1.SettingValue.String.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string value = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1899.

```text
ue = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_val
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07849"></a>
## FND-07849: chesscom.settings.v1.SettingValue.String.null = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Empty null = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1809.

```text
ttingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07850"></a>
## FND-07850: message declaration: chesscom.settings.v1.SettingValue.Integer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Integer {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1964.

```text
ring {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_value {
  double value = 1;
  .google.protobuf.Empty null = 2;
    }
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07851"></a>
## FND-07851: oneof declaration: chesscom.settings.v1.SettingValue.Integer.wrapped_value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof wrapped_value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1767.

```text
.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07852"></a>
## FND-07852: chesscom.settings.v1.SettingValue.Integer.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 value = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 2010.

```text
e = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_value {
  double value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
}

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07853"></a>
## FND-07853: chesscom.settings.v1.SettingValue.Integer.null = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Empty null = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1809.

```text
ttingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07854"></a>
## FND-07854: message declaration: chesscom.settings.v1.SettingValue.Long

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Long {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 2074.

```text
teger {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_value {
  double value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
}

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07855"></a>
## FND-07855: oneof declaration: chesscom.settings.v1.SettingValue.Long.wrapped_value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof wrapped_value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1767.

```text
.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07856"></a>
## FND-07856: chesscom.settings.v1.SettingValue.Long.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 value = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 2117.

```text
alue = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_value {
  double value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
}

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07857"></a>
## FND-07857: chesscom.settings.v1.SettingValue.Long.null = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Empty null = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1809.

```text
ttingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07858"></a>
## FND-07858: message declaration: chesscom.settings.v1.SettingValue.Double

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Double {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 2181.

```text
 Long {
    oneof wrapped_value {
  int64 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_value {
  double value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
}

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07859"></a>
## FND-07859: oneof declaration: chesscom.settings.v1.SettingValue.Double.wrapped_value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof wrapped_value {

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1767.

```text
.Long long = 4;
  .chesscom.settings.v1.SettingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07860"></a>
## FND-07860: chesscom.settings.v1.SettingValue.Double.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double value = 1;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 2226.

```text
ue = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Double {
    oneof wrapped_value {
  double value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
}

```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07861"></a>
## FND-07861: chesscom.settings.v1.SettingValue.Double.null = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Empty null = 2;

### Evidence

- **SRC-0534** `research/proto/chesscom/settings/v1/settings_metadata.proto` — [preserved redacted evidence](../evidence/text/e8ef6ccf9cf9c5bf7819bc21c53eae6ecfbda99e2c56a8d66fada3b622d392b2.proto)
  Character offset 1809.

```text
ttingValue.Double double = 5;
  }
  message Boolean {
    oneof wrapped_value {
  bool value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message String {
    oneof wrapped_value {
  string value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Integer {
    oneof wrapped_value {
  int32 value = 1;
  .google.protobuf.Empty null = 2;
    }
  }
  message Long {
    oneof wrapped_value {
  int64 value 
```

**Source references:** SRC-0534, SRC-1505  
**URL references:** None independently associated  
**Related findings:** FND-07799, FND-07800, FND-07801

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07862"></a>
## FND-07862: message declaration: chesscom.settings.v1.Setting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Setting {

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 103.

```text
source: chesscom/settings/v1/settings_model.proto
// syntax: proto3

package chesscom.settings.v1;

message Setting {
  oneof value {
  .chesscom.settings.v1.GameplaySetting gameplay = 1;
  .chesscom.settings.v1.NotificationSetting notification = 2;
  .chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings
```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07863, FND-07864

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07863"></a>
## FND-07863: oneof declaration: chesscom.settings.v1.Setting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 123.

```text
tings/v1/settings_model.proto
// syntax: proto3

package chesscom.settings.v1;

message Setting {
  oneof value {
  .chesscom.settings.v1.GameplaySetting gameplay = 1;
  .chesscom.settings.v1.NotificationSetting notification = 2;
  .chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting lea
```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07864

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07864"></a>
## FND-07864: chesscom.settings.v1.Setting.gameplay = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.GameplaySetting gameplay = 1;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 139.

```text
s_model.proto
// syntax: proto3

package chesscom.settings.v1;

message Setting {
  oneof value {
  .chesscom.settings.v1.GameplaySetting gameplay = 1;
  .chesscom.settings.v1.NotificationSetting notification = 2;
  .chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chess
```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07865"></a>
## FND-07865: chesscom.settings.v1.Setting.notification = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.NotificationSetting notification = 2;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 193.

```text
ings.v1;

message Setting {
  oneof value {
  .chesscom.settings.v1.GameplaySetting gameplay = 1;
  .chesscom.settings.v1.NotificationSetting notification = 2;
  .chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings
```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07866"></a>
## FND-07866: chesscom.settings.v1.Setting.privacy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.PrivacySetting privacy = 3;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 255.

```text
gs.v1.GameplaySetting gameplay = 1;
  .chesscom.settings.v1.NotificationSetting notification = 2;
  .chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.setti
```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07867"></a>
## FND-07867: chesscom.settings.v1.Setting.board = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.BoardSetting board = 4;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 307.

```text
ings.v1.NotificationSetting notification = 2;
  .chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1
```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07868"></a>
## FND-07868: chesscom.settings.v1.Setting.puzzle = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.PuzzleSetting puzzle = 5;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 355.

```text
.chesscom.settings.v1.PrivacySetting privacy = 3;
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1.WatchSetting watch = 10;
  }
}

```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07869"></a>
## FND-07869: chesscom.settings.v1.Setting.learn = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.LearnSetting learn = 6;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 405.

```text
  .chesscom.settings.v1.BoardSetting board = 4;
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1.WatchSetting watch = 10;
  }
}

```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07870"></a>
## FND-07870: chesscom.settings.v1.Setting.ui = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.UiSetting ui = 7;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 453.

```text
  .chesscom.settings.v1.PuzzleSetting puzzle = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1.WatchSetting watch = 10;
  }
}

```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07871"></a>
## FND-07871: chesscom.settings.v1.Setting.toaster_center = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 495.

```text
le = 5;
  .chesscom.settings.v1.LearnSetting learn = 6;
  .chesscom.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1.WatchSetting watch = 10;
  }
}

```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07872"></a>
## FND-07872: chesscom.settings.v1.Setting.home = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.HomeSetting home = 9;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 560.

```text
om.settings.v1.UiSetting ui = 7;
  .chesscom.settings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1.WatchSetting watch = 10;
  }
}

```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07873"></a>
## FND-07873: chesscom.settings.v1.Setting.watch = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.WatchSetting watch = 10;

### Evidence

- **SRC-0535** `research/proto/chesscom/settings/v1/settings_model.proto` — [preserved redacted evidence](../evidence/text/058556bfd2ac7ce77ec51c950c4a4127d94c5d26981b37f7959f9220db9ea781.proto)
  Character offset 606.

```text
ettings.v1.ToasterCenterSetting toaster_center = 8;
  .chesscom.settings.v1.HomeSetting home = 9;
  .chesscom.settings.v1.WatchSetting watch = 10;
  }
}

```

**Source references:** SRC-0535, SRC-1506  
**URL references:** None independently associated  
**Related findings:** FND-07862, FND-07863, FND-07864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07874"></a>
## FND-07874: message declaration: chesscom.settings.v1.NotificationSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NotificationSetting {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 110.

```text
 chesscom/settings/v1/settings_notification.proto
// syntax: proto3

package chesscom.settings.v1;

message NotificationSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.Not
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
