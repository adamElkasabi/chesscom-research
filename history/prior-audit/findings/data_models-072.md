# data_models — findings 7101–7200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07375"></a>
## FND-07375: enum declaration: chesscom.progression.v1.EventProgressBonusType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum EventProgressBonusType {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 303.

```text
;
  EVENT_REWARD_TYPE_BOARD = 2;
  EVENT_REWARD_TYPE_PIECES = 3;
  EVENT_REWARD_TYPE_SOUNDS = 4;
}

enum EventProgressBonusType {
  EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED = 0;
  EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1;
  EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionR
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07376"></a>
## FND-07376: chesscom.progression.v1.EventProgressBonusType.EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 335.

```text

  EVENT_REWARD_TYPE_PIECES = 3;
  EVENT_REWARD_TYPE_SOUNDS = 4;
}

enum EventProgressBonusType {
  EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED = 0;
  EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1;
  EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _re
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07377"></a>
## FND-07377: chesscom.progression.v1.EventProgressBonusType.EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 380.

```text
RD_TYPE_SOUNDS = 4;
}

enum EventProgressBonusType {
  EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED = 0;
  EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1;
  EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Transl
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07378"></a>
## FND-07378: chesscom.progression.v1.EventProgressBonusType.EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 425.

```text
sType {
  EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED = 0;
  EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1;
  EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _pr
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07379"></a>
## FND-07379: chesscom.progression.v1.EventProgressBonusType.EVENT_PROGRESS_BONUS_TYPE_BASE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_PROGRESS_BONUS_TYPE_BASE = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 467.

```text
IFIED = 0;
  EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS = 1;
  EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07380"></a>
## FND-07380: chesscom.progression.v1.EventProgressBonusType.EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 505.

```text
_DAILY_BONUS = 1;
  EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07381"></a>
## FND-07381: chesscom.progression.v1.EventProgressBonusType.EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 557.

```text
FF = 2;
  EVENT_PROGRESS_BONUS_TYPE_BASE = 3;
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07382"></a>
## FND-07382: message declaration: chesscom.progression.v1.ProgressionRewardConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ProgressionRewardConfiguration {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 603.

```text
  EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.Unlockabl
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07383"></a>
## FND-07383: oneof declaration: chesscom.progression.v1.ProgressionRewardConfiguration._reward_description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _reward_description {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 646.

```text
IER = 4;
  EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

mess
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07384"></a>
## FND-07384: chesscom.progression.v1.ProgressionRewardConfiguration.reward_description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.i18n.v1.Translation reward_description = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 676.

```text
S_TYPE_GAME_REVIEW = 5;
}

message ProgressionRewardConfiguration {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07385"></a>
## FND-07385: oneof declaration: chesscom.progression.v1.ProgressionRewardConfiguration._premium_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _premium_only {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 736.

```text
ation {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp sta
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07386"></a>
## FND-07386: chesscom.progression.v1.ProgressionRewardConfiguration.premium_only = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool premium_only = 5;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 760.

```text
description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 sta
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07387"></a>
## FND-07387: chesscom.progression.v1.ProgressionRewardConfiguration.required_points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 required_points = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 789.

```text
n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  in
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07388"></a>
## FND-07388: chesscom.progression.v1.ProgressionRewardConfiguration.reward_asset = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset reward_asset = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 828.

```text
;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07389"></a>
## FND-07389: chesscom.progression.v1.ProgressionRewardConfiguration.unlockable = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 880.

```text
5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07390"></a>
## FND-07390: message declaration: chesscom.progression.v1.ProgressionModifierTrigger

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ProgressionModifierTrigger {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 962.

```text
ward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_spec
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07391"></a>
## FND-07391: oneof declaration: chesscom.progression.v1.ProgressionModifierTrigger.start_criteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof start_criteria {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1001.

```text
lockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotE
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07392"></a>
## FND-07392: chesscom.progression.v1.ProgressionModifierTrigger.start_time = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp start_time = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1026.

```text
sourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_s
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07393"></a>
## FND-07393: chesscom.progression.v1.ProgressionModifierTrigger.start_max_games_played = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 start_max_games_played = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1071.

```text
rogressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_p
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07394"></a>
## FND-07394: chesscom.progression.v1.ProgressionModifierTrigger.start_max_wins = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 start_max_wins = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1107.

```text
start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.prog
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07395"></a>
## FND-07395: oneof declaration: chesscom.progression.v1.ProgressionModifierTrigger.end_criteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof end_criteria {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1139.

```text
buf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards =
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07396"></a>
## FND-07396: chesscom.progression.v1.ProgressionModifierTrigger.end_time = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp end_time = 4;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1162.

```text
e = 1;
  int32 start_max_games_played = 2;
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string e
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07397"></a>
## FND-07397: chesscom.progression.v1.ProgressionModifierTrigger.duration_minutes = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 duration_minutes = 5;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1205.

```text
  int32 start_max_wins = 3;
  }
  oneof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlock
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07398"></a>
## FND-07398: message declaration: chesscom.progression.v1.EventProgress

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventProgress {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1240.

```text
neof end_criteria {
  .google.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bo
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07399"></a>
## FND-07399: oneof declaration: chesscom.progression.v1.EventProgress.event_specifics

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof event_specifics {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1266.

```text
gle.protobuf.Timestamp end_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07400"></a>
## FND-07400: chesscom.progression.v1.EventProgress.bot_event_specifics = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1292.

```text
_time = 4;
  int32 duration_minutes = 5;
  }
}

message EventProgress {
  oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_externa
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07401"></a>
## FND-07401: chesscom.progression.v1.EventProgress.current_points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 current_points = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1366.

```text
oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07402"></a>
## FND-07402: chesscom.progression.v1.EventProgress.rewards = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.progression.v1.EventReward rewards = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1404.

```text
ogression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07403"></a>
## FND-07403: chesscom.progression.v1.EventProgress.event_config_key = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string event_config_key = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1465.

```text
 optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  opt
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07404"></a>
## FND-07404: message declaration: chesscom.progression.v1.EventUnlockable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventUnlockable {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1506.

```text
peated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  optional .chesscom.unlockables.v1.Unlockable
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07405"></a>
## FND-07405: oneof declaration: chesscom.progression.v1.EventUnlockable._premium_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _premium_only {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 736.

```text
ation {
  oneof _reward_description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp sta
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07406"></a>
## FND-07406: chesscom.progression.v1.EventUnlockable.premium_only = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool premium_only = 5;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 760.

```text
description {
  .chesscom.i18n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 sta
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07407"></a>
## FND-07407: oneof declaration: chesscom.progression.v1.EventUnlockable._user_meets_external_requirements

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_meets_external_requirements {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1587.

```text
config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional st
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07408"></a>
## FND-07408: chesscom.progression.v1.EventUnlockable.user_meets_external_requirements = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool user_meets_external_requirements = 6;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1631.

```text

  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  on
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07409"></a>
## FND-07409: oneof declaration: chesscom.progression.v1.EventUnlockable._is_premium_reward

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_premium_reward {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1680.

```text

  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp u
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07410"></a>
## FND-07410: chesscom.progression.v1.EventUnlockable.is_premium_reward = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_premium_reward = 7;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1709.

```text
rnal_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optiona
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07411"></a>
## FND-07411: chesscom.progression.v1.EventUnlockable.required_points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 required_points = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 789.

```text
n.v1.Translation reward_description = 3;
  }
  oneof _premium_only {
  bool premium_only = 5;
  }
  optional uint32 required_points = 1;
  optional .chesscom.api.v1.Asset reward_asset = 2;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 4;
}

message ProgressionModifierTrigger {
  oneof start_criteria {
  .google.protobuf.Timestamp start_time = 1;
  int32 start_max_games_played = 2;
  in
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07412"></a>
## FND-07412: chesscom.progression.v1.EventUnlockable.unlockable = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1782.

```text
eof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.Ev
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07413"></a>
## FND-07413: chesscom.progression.v1.EventUnlockable.image_url = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string image_url = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1863.

```text
ired_points = 1;
  optional .chesscom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventPr
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07414"></a>
## FND-07414: chesscom.progression.v1.EventUnlockable.name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 4;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1896.

```text
scom.unlockables.v1.UnlockableResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07415"></a>
## FND-07415: message declaration: chesscom.progression.v1.EventReward

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventReward {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1925.

```text
eResourceIdentifier unlockable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeate
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07416"></a>
## FND-07416: oneof declaration: chesscom.progression.v1.EventReward._unlocked_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _unlocked_at {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1949.

```text
ckable = 2;
  optional string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07417"></a>
## FND-07417: chesscom.progression.v1.EventReward.unlocked_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp unlocked_at = 4;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1972.

```text
string image_url = 3;
  optional string name = 4;
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventProgressUpdateS
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07418"></a>
## FND-07418: chesscom.progression.v1.EventReward.icon = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset icon = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2022.

```text
}

message EventReward {
  oneof _unlocked_at {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventProgressUpdateStep progress_update_steps = 2;
  optional string e
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07419"></a>
## FND-07419: chesscom.progression.v1.EventReward.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.progression.v1.EventRewardType type = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2066.

```text
t {
  .google.protobuf.Timestamp unlocked_at = 4;
  }
  optional .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventProgressUpdateStep progress_update_steps = 2;
  optional string event_config_key = 3;
}

message EventProgres
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07420"></a>
## FND-07420: chesscom.progression.v1.EventReward.required_points = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 required_points = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2128.

```text
al .chesscom.api.v1.Asset icon = 1;
  optional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventProgressUpdateStep progress_update_steps = 2;
  optional string event_config_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07421"></a>
## FND-07421: message declaration: chesscom.progression.v1.EventProgressUpdate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventProgressUpdate {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2168.

```text
tional .chesscom.progression.v1.EventRewardType type = 2;
  optional uint32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventProgressUpdateStep progress_update_steps = 2;
  optional string event_config_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07422"></a>
## FND-07422: chesscom.progression.v1.EventProgressUpdate.current_points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 current_points = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1366.

```text
oneof event_specifics {
  .chesscom.progression.v1.BotEventSpecifics bot_event_specifics = 4;
  }
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07423"></a>
## FND-07423: chesscom.progression.v1.EventProgressUpdate.progress_update_steps = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.progression.v1.EventProgressUpdateStep progress_update_steps = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2238.

```text
int32 required_points = 3;
}

message EventProgressUpdate {
  optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventProgressUpdateStep progress_update_steps = 2;
  optional string event_config_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;
  optional .chesscom.progression.v1.EventProgressBonusType bonus_type 
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07424"></a>
## FND-07424: chesscom.progression.v1.EventProgressUpdate.event_config_key = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string event_config_key = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 1465.

```text
 optional uint32 current_points = 1;
  repeated .chesscom.progression.v1.EventReward rewards = 2;
  optional string event_config_key = 3;
}

message EventUnlockable {
  oneof _premium_only {
  bool premium_only = 5;
  }
  oneof _user_meets_external_requirements {
  bool user_meets_external_requirements = 6;
  }
  oneof _is_premium_reward {
  bool is_premium_reward = 7;
  }
  optional uint32 required_points = 1;
  opt
```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07425"></a>
## FND-07425: message declaration: chesscom.progression.v1.EventProgressUpdateStep

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventProgressUpdateStep {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2366.

```text
on.v1.EventProgressUpdateStep progress_update_steps = 2;
  optional string event_config_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;
  optional .chesscom.progression.v1.EventProgressBonusType bonus_type = 2;
}

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07426"></a>
## FND-07426: oneof declaration: chesscom.progression.v1.EventProgressUpdateStep._multiplier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _multiplier {

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2402.

```text
ss_update_steps = 2;
  optional string event_config_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;
  optional .chesscom.progression.v1.EventProgressBonusType bonus_type = 2;
}

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07427"></a>
## FND-07427: chesscom.progression.v1.EventProgressUpdateStep.multiplier = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 multiplier = 3;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2424.

```text
 optional string event_config_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;
  optional .chesscom.progression.v1.EventProgressBonusType bonus_type = 2;
}

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07428"></a>
## FND-07428: chesscom.progression.v1.EventProgressUpdateStep.points_to_add = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points_to_add = 1;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2453.

```text
_key = 3;
}

message EventProgressUpdateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;
  optional .chesscom.progression.v1.EventProgressBonusType bonus_type = 2;
}

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07429"></a>
## FND-07429: chesscom.progression.v1.EventProgressUpdateStep.bonus_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.progression.v1.EventProgressBonusType bonus_type = 2;

### Evidence

- **SRC-0518** `research/proto/chesscom/progression/v1/event_configuration.proto` — [preserved redacted evidence](../evidence/text/92fb1352d59814fbc551fa4bc3699687b702059277c4a1840096f80dc3855b24.proto)
  Character offset 2490.

```text
ateStep {
  oneof _multiplier {
  uint32 multiplier = 3;
  }
  optional uint32 points_to_add = 1;
  optional .chesscom.progression.v1.EventProgressBonusType bonus_type = 2;
}

```

**Source references:** SRC-0518, SRC-1489  
**URL references:** None independently associated  
**Related findings:** FND-07369, FND-07370, FND-07371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07430"></a>
## FND-07430: enum declaration: chesscom.progression.v1.BotVariationSupport

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BotVariationSupport {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 110.

```text
 chesscom/progression/v1/event_specifics.proto
// syntax: proto3

package chesscom.progression.v1;

enum BotVariationSupport {
  BOT_VARIATION_SUPPORT_UNSPECIFIED = 0;
  BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariations
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07431"></a>
## FND-07431: chesscom.progression.v1.BotVariationSupport.BOT_VARIATION_SUPPORT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_VARIATION_SUPPORT_UNSPECIFIED = 0;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 139.

```text
t_specifics.proto
// syntax: proto3

package chesscom.progression.v1;

enum BotVariationSupport {
  BOT_VARIATION_SUPPORT_UNSPECIFIED = 0;
  BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07432"></a>
## FND-07432: chesscom.progression.v1.BotVariationSupport.BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 180.

```text
age chesscom.progression.v1;

enum BotVariationSupport {
  BOT_VARIATION_SUPPORT_UNSPECIFIED = 0;
  BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp var
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07433"></a>
## FND-07433: enum declaration: chesscom.progression.v1.BotLabel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BotLabel {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 221.

```text
iationSupport {
  BOT_VARIATION_SUPPORT_UNSPECIFIED = 0;
  BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVar
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07434"></a>
## FND-07434: chesscom.progression.v1.BotLabel.BOT_LABEL_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_LABEL_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 239.

```text
BOT_VARIATION_SUPPORT_UNSPECIFIED = 0;
  BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  o
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07435"></a>
## FND-07435: chesscom.progression.v1.BotLabel.BOT_LABEL_TYPE_HARDER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_LABEL_TYPE_HARDER = 1;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 273.

```text
= 0;
  BOT_VARIATION_SUPPORT_CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07436"></a>
## FND-07436: chesscom.progression.v1.BotLabel.BOT_LABEL_TYPE_EASIER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_LABEL_TYPE_EASIER = 2;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 302.

```text
CUSTOM_FEN = 1;
}

enum BotLabel {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.Bot
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07437"></a>
## FND-07437: message declaration: chesscom.progression.v1.BotEventSpecifics

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotEventSpecifics {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 332.

```text
el {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

me
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07438"></a>
## FND-07438: chesscom.progression.v1.BotEventSpecifics.active_variations = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 362.

```text
IED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEventSpecifics {
  repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07439"></a>
## FND-07439: chesscom.progression.v1.BotEventSpecifics.variation_timestamp = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp variation_timestamp = 2;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 461.

```text
 repeated .chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
 
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07440"></a>
## FND-07440: message declaration: chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ActiveVariationsEntry {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 524.

```text
ationsEntry active_variations = 1;
  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_bla
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07441"></a>
## FND-07441: chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 558.

```text

  optional .google.protobuf.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black 
```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07442"></a>
## FND-07442: chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.progression.v1.BotOverrides value = 2;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 585.

```text
f.Timestamp variation_timestamp = 2;
  message ActiveVariationsEntry {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07443"></a>
## FND-07443: message declaration: chesscom.progression.v1.BotOverrides

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotOverrides {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 650.

```text
try {
  optional string key = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07444"></a>
## FND-07444: oneof declaration: chesscom.progression.v1.BotOverrides._bot_label

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bot_label {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 675.

```text
ey = 1;
  optional .chesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07445"></a>
## FND-07445: chesscom.progression.v1.BotOverrides.bot_label = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.progression.v1.BotLabel bot_label = 1;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 696.

```text
hesscom.progression.v1.BotOverrides value = 2;
  }
}

message BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07446"></a>
## FND-07446: oneof declaration: chesscom.progression.v1.BotOverrides._fen_player_is_white

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_player_is_white {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 751.

```text
essage BotOverrides {
  oneof _bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07447"></a>
## FND-07447: chesscom.progression.v1.BotOverrides.fen_player_is_white = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen_player_is_white = 2;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 782.

```text
bot_label {
  .chesscom.progression.v1.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07448"></a>
## FND-07448: oneof declaration: chesscom.progression.v1.BotOverrides._fen_player_is_black

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_player_is_black {

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 820.

```text
.BotLabel bot_label = 1;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07449"></a>
## FND-07449: chesscom.progression.v1.BotOverrides.fen_player_is_black = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen_player_is_black = 3;

### Evidence

- **SRC-0519** `research/proto/chesscom/progression/v1/event_specifics.proto` — [preserved redacted evidence](../evidence/text/d40c2ad2566f31d9a48e1c1a5b0d044bc82682642c1914b629e0a7b6574f5125.proto)
  Character offset 851.

```text
oneof _fen_player_is_white {
  string fen_player_is_white = 2;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 3;
  }
}

```

**Source references:** SRC-0519, SRC-1490  
**URL references:** None independently associated  
**Related findings:** FND-07430, FND-07431, FND-07432

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07450"></a>
## FND-07450: enum declaration: chesscom.proto_options.annotations.v1.Platform

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Platform {

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 134.

```text
annotations/v1/annotations.proto
// syntax: proto3

package chesscom.proto_options.annotations.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.pro
```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07451"></a>
## FND-07451: chesscom.proto_options.annotations.v1.Platform.PLATFORM_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_UNSPECIFIED = 0;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 152.

```text
otations.proto
// syntax: proto3

package chesscom.proto_options.annotations.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotat
```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07452"></a>
## FND-07452: chesscom.proto_options.annotations.v1.Platform.PLATFORM_MOBILE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_MOBILE = 1;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 180.

```text
oto3

package chesscom.proto_options.annotations.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07453"></a>
## FND-07453: chesscom.proto_options.annotations.v1.Platform.PLATFORM_WEB = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_WEB = 2;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 203.

```text
proto_options.annotations.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07454"></a>
## FND-07454: chesscom.proto_options.annotations.v1.Platform.PLATFORM_BACKEND = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_BACKEND = 3;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 223.

```text
tions.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07455"></a>
## FND-07455: enum declaration: chesscom.proto_options.annotations.v1.Project

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Project {

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 248.

```text
{
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07456"></a>
## FND-07456: chesscom.proto_options.annotations.v1.Project.PROJECT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROJECT_UNSPECIFIED = 0;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 265.

```text
ECIFIED = 0;
  PLATFORM_MOBILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07457"></a>
## FND-07457: chesscom.proto_options.annotations.v1.Project.PROJECT_CHESSCOM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROJECT_CHESSCOM = 1;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 292.

```text
ILE = 1;
  PLATFORM_WEB = 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07458"></a>
## FND-07458: chesscom.proto_options.annotations.v1.Project.PROJECT_CHESSKID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROJECT_CHESSKID = 2;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 316.

```text
= 2;
  PLATFORM_BACKEND = 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07459"></a>
## FND-07459: message declaration: chesscom.proto_options.annotations.v1.Usage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Usage {

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 341.

```text
 3;
}

enum Project {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07460"></a>
## FND-07460: chesscom.proto_options.annotations.v1.Usage.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 359.

```text
t {
  PROJECT_UNSPECIFIED = 0;
  PROJECT_CHESSCOM = 1;
  PROJECT_CHESSKID = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07461"></a>
## FND-07461: chesscom.proto_options.annotations.v1.Usage.project = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.annotations.v1.Project project = 2;

### Evidence

- **SRC-0520** `research/proto/chesscom/proto_options/annotations/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/40e9fb1b430935abdf4198b5f26e3582891ee5b285afd13ec079856531780043.proto)
  Character offset 432.

```text
 = 2;
}

message Usage {
  repeated .chesscom.proto_options.annotations.v1.Platform platform = 1;
  repeated .chesscom.proto_options.annotations.v1.Project project = 2;
}

```

**Source references:** SRC-0520, SRC-1491  
**URL references:** None independently associated  
**Related findings:** FND-07450, FND-07451, FND-07452

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07462"></a>
## FND-07462: enum declaration: chesscom.proto_options.api.v1.RpcProtocol

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RpcProtocol {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 118.

```text
m/proto_options/api/v1/api_options.proto
// syntax: proto3

package chesscom.proto_options.api.v1;

enum RpcProtocol {
  RPC_PROTOCOL_UNSPECIFIED = 0;
  RPC_PROTOCOL_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07463"></a>
## FND-07463: chesscom.proto_options.api.v1.RpcProtocol.RPC_PROTOCOL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RPC_PROTOCOL_UNSPECIFIED = 0;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 139.

```text
1/api_options.proto
// syntax: proto3

package chesscom.proto_options.api.v1;

enum RpcProtocol {
  RPC_PROTOCOL_UNSPECIFIED = 0;
  RPC_PROTOCOL_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthentic
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07464"></a>
## FND-07464: chesscom.proto_options.api.v1.RpcProtocol.RPC_PROTOCOL_TWIRP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RPC_PROTOCOL_TWIRP = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 171.

```text
roto3

package chesscom.proto_options.api.v1;

enum RpcProtocol {
  RPC_PROTOCOL_UNSPECIFIED = 0;
  RPC_PROTOCOL_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07465"></a>
## FND-07465: chesscom.proto_options.api.v1.RpcProtocol.RPC_PROTOCOL_CONNECT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RPC_PROTOCOL_CONNECT = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 197.

```text
oto_options.api.v1;

enum RpcProtocol {
  RPC_PROTOCOL_UNSPECIFIED = 0;
  RPC_PROTOCOL_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07466"></a>
## FND-07466: message declaration: chesscom.proto_options.api.v1.ApiNoAuth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiNoAuth {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 226.

```text
Protocol {
  RPC_PROTOCOL_UNSPECIFIED = 0;
  RPC_PROTOCOL_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07467"></a>
## FND-07467: message declaration: chesscom.proto_options.api.v1.ApiSecurityBasicAuth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiSecurityBasicAuth {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 249.

```text
OL_UNSPECIFIED = 0;
  RPC_PROTOCOL_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_opt
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07468"></a>
## FND-07468: message declaration: chesscom.proto_options.api.v1.ApiSecurityBearerAuth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiSecurityBearerAuth {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 283.

```text
_TWIRP = 1;
  RPC_PROTOCOL_CONNECT = 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth b
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07469"></a>
## FND-07469: message declaration: chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiSecurityApiKeyAuth {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 318.

```text
= 2;
}

message ApiNoAuth {
}

message ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_op
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07470"></a>
## FND-07470: oneof declaration: chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth._header

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _header {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 352.

```text
sage ApiSecurityBasicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07471"></a>
## FND-07471: chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth.header = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string header = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 370.

```text
sicAuth {
}

message ApiSecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;

```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07472"></a>
## FND-07472: oneof declaration: chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth._cookie

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _cookie {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 395.

```text
ecurityBearerAuth {
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07473"></a>
## FND-07473: chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth.cookie = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string cookie = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 413.

```text
{
}

message ApiSecurityApiKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurit
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07474"></a>
## FND-07474: message declaration: chesscom.proto_options.api.v1.ApiAuthenticationDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiAuthenticationDefinition {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 439.

```text
iKeyAuth {
  oneof _header {
  string header = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth =
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
