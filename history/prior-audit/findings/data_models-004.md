# data_models — findings 301–400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00575"></a>
## FND-00575: message declaration: chesscom.bots.v1.BotGroup

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotGroup {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 90.

```text
// source: chesscom/bots/v1/bot_group.proto
// syntax: proto3

package chesscom.bots.v1;

message BotGroup {
  oneof _club_uuid {
  string club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00576"></a>
## FND-00576: oneof declaration: chesscom.bots.v1.BotGroup._club_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _club_uuid {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 111.

```text
chesscom/bots/v1/bot_group.proto
// syntax: proto3

package chesscom.bots.v1;

message BotGroup {
  oneof _club_uuid {
  string club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enab
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00577"></a>
## FND-00577: chesscom.bots.v1.BotGroup.club_uuid = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string club_uuid = 9;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 132.

```text
group.proto
// syntax: proto3

package chesscom.bots.v1;

message BotGroup {
  oneof _club_uuid {
  string club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_en
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00578"></a>
## FND-00578: oneof declaration: chesscom.bots.v1.BotGroup._avatar

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avatar {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 160.

```text
3

package chesscom.bots.v1;

message BotGroup {
  oneof _club_uuid {
  string club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional s
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00579"></a>
## FND-00579: chesscom.bots.v1.BotGroup.avatar = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string avatar = 14;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 178.

```text
m.bots.v1;

message BotGroup {
  oneof _club_uuid {
  string club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00580"></a>
## FND-00580: oneof declaration: chesscom.bots.v1.BotGroup._configuration_key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _configuration_key {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 204.

```text
up {
  oneof _club_uuid {
  string club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00581"></a>
## FND-00581: chesscom.bots.v1.BotGroup.configuration_key = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string configuration_key = 16;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 233.

```text
tring club_uuid = 9;
  }
  oneof _avatar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_descri
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00582"></a>
## FND-00582: oneof declaration: chesscom.bots.v1.BotGroup._event

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _event {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 270.

```text
tar {
  string avatar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00583"></a>
## FND-00583: chesscom.bots.v1.BotGroup.event = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.bots.v1.BotEvent event = 17;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 287.

```text
atar = 14;
  }
  oneof _configuration_key {
  string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00584"></a>
## FND-00584: oneof declaration: chesscom.bots.v1.BotGroup._url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _url {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 332.

```text
 string configuration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool feat
```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00585"></a>
## FND-00585: chesscom.bots.v1.BotGroup.url = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string url = 18;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 347.

```text
ration_key = 16;
  }
  oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00586"></a>
## FND-00586: oneof declaration: chesscom.bots.v1.BotGroup._enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enabled {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 370.

```text
oneof _event {
  .chesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00587"></a>
## FND-00587: chesscom.bots.v1.BotGroup.enabled = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enabled = 19;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 389.

```text
hesscom.bots.v1.BotEvent event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00588"></a>
## FND-00588: oneof declaration: chesscom.bots.v1.BotGroup._staff_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _staff_enabled {

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 414.

```text
event = 17;
  }
  oneof _url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00589"></a>
## FND-00589: chesscom.bots.v1.BotGroup.staff_enabled = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool staff_enabled = 20;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 439.

```text
url {
  string url = 18;
  }
  oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00590"></a>
## FND-00590: chesscom.bots.v1.BotGroup.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 470.

```text
oneof _enabled {
  bool enabled = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00591"></a>
## FND-00591: chesscom.bots.v1.BotGroup.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 498.

```text
led = 19;
  }
  oneof _staff_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00592"></a>
## FND-00592: chesscom.bots.v1.BotGroup.hint_description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string hint_description = 3;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 526.

```text
_enabled {
  bool staff_enabled = 20;
  }
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00593"></a>
## FND-00593: chesscom.bots.v1.BotGroup.bot_personalities = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 566.

```text
}
  optional string uuid = 1;
  optional string name = 2;
  optional string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00594"></a>
## FND-00594: chesscom.bots.v1.BotGroup.featured = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool featured = 15;

### Evidence

- **SRC-0224** `research/proto/chesscom/bots/v1/bot_group.proto` — [preserved redacted evidence](../evidence/text/9b240b3ceff07c1050fe9fe92065c9695c71152a56f031de69be1dd28540328e.proto)
  Character offset 634.

```text
 string hint_description = 3;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 12;
  optional bool featured = 15;
}

```

**Source references:** SRC-0224, SRC-1195  
**URL references:** None independently associated  
**Related findings:** FND-00575, FND-00576, FND-00577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00595"></a>
## FND-00595: message declaration: chesscom.bots.v1.ListBotGroupsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListBotGroupsRequest {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 98.

```text
// source: chesscom/bots/v1/bot_group_service.proto
// syntax: proto3

package chesscom.bots.v1;

message ListBotGroupsRequest {
  oneof _bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup 
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00596"></a>
## FND-00596: oneof declaration: chesscom.bots.v1.ListBotGroupsRequest._bot_group_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bot_group_uuid {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 131.

```text
_group_service.proto
// syntax: proto3

package chesscom.bots.v1;

message ListBotGroupsRequest {
  oneof _bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAl
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00597"></a>
## FND-00597: chesscom.bots.v1.ListBotGroupsRequest.bot_group_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string bot_group_uuid = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 157.

```text
ntax: proto3

package chesscom.bots.v1;

message ListBotGroupsRequest {
  oneof _bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  op
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00598"></a>
## FND-00598: oneof declaration: chesscom.bots.v1.ListBotGroupsRequest._with_bots

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _with_bots {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 190.

```text
ts.v1;

message ListBotGroupsRequest {
  oneof _bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00599"></a>
## FND-00599: chesscom.bots.v1.ListBotGroupsRequest.with_bots = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool with_bots = 5;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 211.

```text
otGroupsRequest {
  oneof _bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string su
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00600"></a>
## FND-00600: chesscom.bots.v1.ListBotGroupsRequest.supported_languages = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string supported_languages = 6;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 237.

```text
_bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}


```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00601"></a>
## FND-00601: message declaration: chesscom.bots.v1.ListBotGroupsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListBotGroupsResponse {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 281.

```text
1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optio
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00602"></a>
## FND-00602: oneof declaration: chesscom.bots.v1.ListBotGroupsResponse._recommended_bot_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _recommended_bot_id {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 315.

```text
 with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00603"></a>
## FND-00603: chesscom.bots.v1.ListBotGroupsResponse.recommended_bot_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string recommended_bot_id = 2;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 345.

```text
 string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chessc
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00604"></a>
## FND-00604: chesscom.bots.v1.ListBotGroupsResponse.bot_groups = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.bots.v1.BotGroup bot_groups = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 382.

```text
essage ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_persona
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00605"></a>
## FND-00605: message declaration: chesscom.bots.v1.ListAllBotsInGroupRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllBotsInGroupRequest {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 437.

```text
_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  op
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00606"></a>
## FND-00606: chesscom.bots.v1.ListAllBotsInGroupRequest.bot_group_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_group_uuid = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 475.

```text

  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

messag
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00607"></a>
## FND-00607: chesscom.bots.v1.ListAllBotsInGroupRequest.supported_languages = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string supported_languages = 6;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 237.

```text
_bot_group_uuid {
  string bot_group_uuid = 1;
  }
  oneof _with_bots {
  bool with_bots = 5;
  }
  repeated string supported_languages = 6;
}

message ListBotGroupsResponse {
  oneof _recommended_bot_id {
  string recommended_bot_id = 2;
  }
  repeated .chesscom.bots.v1.BotGroup bot_groups = 1;
}

message ListAllBotsInGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}


```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00608"></a>
## FND-00608: message declaration: chesscom.bots.v1.ListAllBotsInGroupResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllBotsInGroupResponse {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 557.

```text
nGroupRequest {
  optional string bot_group_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00609"></a>
## FND-00609: chesscom.bots.v1.ListAllBotsInGroupResponse.bot_group = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotGroup bot_group = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 596.

```text
roup_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPerso
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00610"></a>
## FND-00610: chesscom.bots.v1.ListAllBotsInGroupResponse.bot_personalities = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 649.

```text
= 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNa
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00611"></a>
## FND-00611: message declaration: chesscom.bots.v1.ListAllBotsForClubRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllBotsForClubRequest {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 717.

```text
ts.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNamesRequest {
}

message ListAllBotNamesResponse {
  repeated .chessc
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00612"></a>
## FND-00612: chesscom.bots.v1.ListAllBotsForClubRequest.club_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string club_uuid = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 755.

```text
ed .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNamesRequest {
}

message ListAllBotNamesResponse {
  repeated .chesscom.bots.v1.SupportedBot supported_bot 
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00613"></a>
## FND-00613: message declaration: chesscom.bots.v1.ListAllBotsForClubResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllBotsForClubResponse {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 789.

```text
y bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNamesRequest {
}

message ListAllBotNamesResponse {
  repeated .chesscom.bots.v1.SupportedBot supported_bot = 1;
}

```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00614"></a>
## FND-00614: chesscom.bots.v1.ListAllBotsForClubResponse.bot_group = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotGroup bot_group = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 596.

```text
roup_uuid = 1;
  repeated string supported_languages = 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPerso
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00615"></a>
## FND-00615: chesscom.bots.v1.ListAllBotsForClubResponse.bot_personalities = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 649.

```text
= 6;
}

message ListAllBotsInGroupResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotsForClubRequest {
  optional string club_uuid = 1;
}

message ListAllBotsForClubResponse {
  optional .chesscom.bots.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNa
```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00616"></a>
## FND-00616: message declaration: chesscom.bots.v1.ListAllBotNamesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllBotNamesRequest {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 949.

```text
ts.v1.BotGroup bot_group = 1;
  repeated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNamesRequest {
}

message ListAllBotNamesResponse {
  repeated .chesscom.bots.v1.SupportedBot supported_bot = 1;
}

```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00617"></a>
## FND-00617: message declaration: chesscom.bots.v1.ListAllBotNamesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllBotNamesResponse {

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 985.

```text
ated .chesscom.bots.v1.BotPersonality bot_personalities = 2;
}

message ListAllBotNamesRequest {
}

message ListAllBotNamesResponse {
  repeated .chesscom.bots.v1.SupportedBot supported_bot = 1;
}

```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00618"></a>
## FND-00618: chesscom.bots.v1.ListAllBotNamesResponse.supported_bot = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.bots.v1.SupportedBot supported_bot = 1;

### Evidence

- **SRC-0225** `research/proto/chesscom/bots/v1/bot_group_service.proto` — [preserved redacted evidence](../evidence/text/6d4e796ee77335acbc82930a9f07aba0a63c5b751d9c54e61cb7c9c34553a3f5.proto)
  Character offset 1021.

```text
y bot_personalities = 2;
}

message ListAllBotNamesRequest {
}

message ListAllBotNamesResponse {
  repeated .chesscom.bots.v1.SupportedBot supported_bot = 1;
}

```

**Source references:** SRC-0225, SRC-1196  
**URL references:** None independently associated  
**Related findings:** FND-00595, FND-00596, FND-00597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00619"></a>
## FND-00619: message declaration: chesscom.bots.v1.BotMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotMetadata {

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 93.

```text
// source: chesscom/bots/v1/bot_metadata.proto
// syntax: proto3

package chesscom.bots.v1;

message BotMetadata {
  oneof _theme_uuid {
  string theme_uuid = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00620, FND-00621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00620"></a>
## FND-00620: oneof declaration: chesscom.bots.v1.BotMetadata._theme_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme_uuid {

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 117.

```text
om/bots/v1/bot_metadata.proto
// syntax: proto3

package chesscom.bots.v1;

message BotMetadata {
  oneof _theme_uuid {
  string theme_uuid = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00619, FND-00621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00621"></a>
## FND-00621: chesscom.bots.v1.BotMetadata.theme_uuid = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string theme_uuid = 4;

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 139.

```text
a.proto
// syntax: proto3

package chesscom.bots.v1;

message BotMetadata {
  oneof _theme_uuid {
  string theme_uuid = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00619, FND-00620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00622"></a>
## FND-00622: chesscom.bots.v1.BotMetadata.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 168.

```text
ckage chesscom.bots.v1;

message BotMetadata {
  oneof _theme_uuid {
  string theme_uuid = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00619, FND-00620, FND-00621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00623"></a>
## FND-00623: chesscom.bots.v1.BotMetadata.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 194.

```text
essage BotMetadata {
  oneof _theme_uuid {
  string theme_uuid = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00619, FND-00620, FND-00621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00624"></a>
## FND-00624: chesscom.bots.v1.BotMetadata.rating_text = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string rating_text = 3;

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 222.

```text
 _theme_uuid {
  string theme_uuid = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00619, FND-00620, FND-00621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00625"></a>
## FND-00625: chesscom.bots.v1.BotMetadata.image_url = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string image_url = 5;

### Evidence

- **SRC-0226** `research/proto/chesscom/bots/v1/bot_metadata.proto` — [preserved redacted evidence](../evidence/text/323ab8f1cfd6d745ee56ff62a2ba69962cea819161a8e950ec25d5169f5bc49d.proto)
  Character offset 257.

```text
= 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional string rating_text = 3;
  optional string image_url = 5;
}

```

**Source references:** SRC-0226, SRC-1197  
**URL references:** None independently associated  
**Related findings:** FND-00619, FND-00620, FND-00621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00626"></a>
## FND-00626: enum declaration: chesscom.bots.v1.Personality

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Personality {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 96.

```text
// source: chesscom/bots/v1/bot_personality.proto
// syntax: proto3

package chesscom.bots.v1;

enum Personality {
  PERSONALITY_UNSPECIFIED = 0;
  PERSONALITY_UNSPECIFIED_DEFAULT = 1;
  PERSONALITY_UNSPECIFIED_BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_H
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00627"></a>
## FND-00627: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 117.

```text
om/bots/v1/bot_personality.proto
// syntax: proto3

package chesscom.bots.v1;

enum Personality {
  PERSONALITY_UNSPECIFIED = 0;
  PERSONALITY_UNSPECIFIED_DEFAULT = 1;
  PERSONALITY_UNSPECIFIED_BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALI
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00628"></a>
## FND-00628: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_DEFAULT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_DEFAULT = 1;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 148.

```text
o
// syntax: proto3

package chesscom.bots.v1;

enum Personality {
  PERSONALITY_UNSPECIFIED = 0;
  PERSONALITY_UNSPECIFIED_DEFAULT = 1;
  PERSONALITY_UNSPECIFIED_BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PE
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00629"></a>
## FND-00629: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_BEGINNER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_BEGINNER = 2;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 187.

```text
ots.v1;

enum Personality {
  PERSONALITY_UNSPECIFIED = 0;
  PERSONALITY_UNSPECIFIED_DEFAULT = 1;
  PERSONALITY_UNSPECIFIED_BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERS
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00630"></a>
## FND-00630: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 227.

```text
Y_UNSPECIFIED = 0;
  PERSONALITY_UNSPECIFIED_DEFAULT = 1;
  PERSONALITY_UNSPECIFIED_BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSO
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00631"></a>
## FND-00631: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_POSITIONAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_POSITIONAL = 4;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 269.

```text
ED_DEFAULT = 1;
  PERSONALITY_UNSPECIFIED_BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PE
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00632"></a>
## FND-00632: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_DEFENSIVE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 311.

```text
BEGINNER = 2;
  PERSONALITY_UNSPECIFIED_AGGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

m
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00633"></a>
## FND-00633: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_ENDGAME = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_ENDGAME = 6;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 352.

```text
GGRESSIVE = 3;
  PERSONALITY_UNSPECIFIED_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium 
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00634"></a>
## FND-00634: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_HUMAN = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_HUMAN = 7;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 391.

```text
D_POSITIONAL = 4;
  PERSONALITY_UNSPECIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _kom
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00635"></a>
## FND-00635: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_HIKARU = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_HIKARU = 8;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 428.

```text
CIFIED_DEFENSIVE = 5;
  PERSONALITY_UNSPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skil
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00636"></a>
## FND-00636: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_DANNY = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_DANNY = 9;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 466.

```text
SPECIFIED_ENDGAME = 6;
  PERSONALITY_UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skil
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00637"></a>
## FND-00637: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_ACTIVE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_ACTIVE = 10;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 503.

```text
UNSPECIFIED_HUMAN = 7;
  PERSONALITY_UNSPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00638"></a>
## FND-00638: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 542.

```text
SPECIFIED_HIKARU = 8;
  PERSONALITY_UNSPECIFIED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
 
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00639"></a>
## FND-00639: chesscom.bots.v1.Personality.PERSONALITY_UNSPECIFIED_UNLEASHED = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PERSONALITY_UNSPECIFIED_UNLEASHED = 12;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 587.

```text
ED_DANNY = 9;
  PERSONALITY_UNSPECIFIED_ACTIVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  on
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00640"></a>
## FND-00640: message declaration: chesscom.bots.v1.BotPersonality

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotPersonality {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 630.

```text
IVE = 10;
  PERSONALITY_UNSPECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00641"></a>
## FND-00641: oneof declaration: chesscom.bots.v1.BotPersonality._premium

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _premium {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 657.

```text
PECIFIED_NEW_TO_CHESS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string c
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00642"></a>
## FND-00642: chesscom.bots.v1.BotPersonality.premium = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool premium = 10;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 676.

```text
SS = 11;
  PERSONALITY_UNSPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
 
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00643"></a>
## FND-00643: oneof declaration: chesscom.bots.v1.BotPersonality._komodo_skill_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _komodo_skill_level {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 701.

```text
SPECIFIED_UNLEASHED = 12;
}

message BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  st
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00644"></a>
## FND-00644: chesscom.bots.v1.BotPersonality.komodo_skill_level = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 komodo_skill_level = 11;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 731.

```text
essage BotPersonality {
  oneof _premium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof 
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00645"></a>
## FND-00645: oneof declaration: chesscom.bots.v1.BotPersonality._komodo_skill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _komodo_skill {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 768.

```text
ium {
  bool premium = 10;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00646"></a>
## FND-00646: chesscom.bots.v1.BotPersonality.komodo_skill = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 komodo_skill = 12;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 792.

```text
0;
  }
  oneof _komodo_skill_level {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  s
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00647"></a>
## FND-00647: oneof declaration: chesscom.bots.v1.BotPersonality._adapt

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _adapt {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 823.

```text
vel {
  int32 komodo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  o
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00648"></a>
## FND-00648: chesscom.bots.v1.BotPersonality.adapt = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool adapt = 13;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 840.

```text
odo_skill_level = 11;
  }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00649"></a>
## FND-00649: oneof declaration: chesscom.bots.v1.BotPersonality._human

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _human {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 863.

```text
 }
  oneof _komodo_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00650"></a>
## FND-00650: chesscom.bots.v1.BotPersonality.human = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string human = 14;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 880.

```text
o_skill {
  int32 komodo_skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 2
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00651"></a>
## FND-00651: oneof declaration: chesscom.bots.v1.BotPersonality._book

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _book {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 905.

```text
skill = 12;
  }
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _descripti
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00652"></a>
## FND-00652: chesscom.bots.v1.BotPersonality.book = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string book = 16;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 921.

```text
  oneof _adapt {
  bool adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string de
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00653"></a>
## FND-00653: oneof declaration: chesscom.bots.v1.BotPersonality._country_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _country_code {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 945.

```text
adapt = 13;
  }
  oneof _human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  on
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00654"></a>
## FND-00654: chesscom.bots.v1.BotPersonality.country_code = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string country_code = 17;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 969.

```text
_human {
  string human = 14;
  }
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  st
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00655"></a>
## FND-00655: oneof declaration: chesscom.bots.v1.BotPersonality._gender

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gender {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1001.

```text
}
  oneof _book {
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  on
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00656"></a>
## FND-00656: chesscom.bots.v1.BotPersonality.gender = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gender = 18;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1019.

```text
  string book = 16;
  }
  oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_e
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00657"></a>
## FND-00657: oneof declaration: chesscom.bots.v1.BotPersonality._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1045.

```text
oneof _country_code {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_pi
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00658"></a>
## FND-00658: chesscom.bots.v1.BotPersonality.rating = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 19;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1063.

```text
e {
  string country_code = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00659"></a>
## FND-00659: oneof declaration: chesscom.bots.v1.BotPersonality._rating_text

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_text {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1088.

```text
 = 17;
  }
  oneof _gender {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00660"></a>
## FND-00660: chesscom.bots.v1.BotPersonality.rating_text = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string rating_text = 20;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1111.

```text
der {
  string gender = 18;
  }
  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string mino
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00661"></a>
## FND-00661: oneof declaration: chesscom.bots.v1.BotPersonality._live_online_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _live_online_rating {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1142.

```text

  oneof _rating {
  int32 rating = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  one
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00662"></a>
## FND-00662: chesscom.bots.v1.BotPersonality.live_online_rating = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 live_online_rating = 21;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1172.

```text
ing = 19;
  }
  oneof _rating_text {
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string them
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00663"></a>
## FND-00663: oneof declaration: chesscom.bots.v1.BotPersonality._description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _description {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1209.

```text
  string rating_text = 20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00664"></a>
## FND-00664: chesscom.bots.v1.BotPersonality.description = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string description = 22;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1232.

```text
20;
  }
  oneof _live_online_rating {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string min
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00665"></a>
## FND-00665: oneof declaration: chesscom.bots.v1.BotPersonality._pawn_endgame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pawn_endgame {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1263.

```text
ting {
  int32 live_online_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  on
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00666"></a>
## FND-00666: chesscom.bots.v1.BotPersonality.pawn_endgame = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string pawn_endgame = 23;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1287.

```text
ne_rating = 21;
  }
  oneof _description {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  in
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00667"></a>
## FND-00667: oneof declaration: chesscom.bots.v1.BotPersonality._major_piece_endgame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _major_piece_endgame {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1319.

```text
cription {
  string description = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  one
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00668"></a>
## FND-00668: chesscom.bots.v1.BotPersonality.major_piece_endgame = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string major_piece_endgame = 24;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1350.

```text
 = 22;
  }
  oneof _pawn_endgame {
  string pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00669"></a>
## FND-00669: oneof declaration: chesscom.bots.v1.BotPersonality._minor_piece_endgame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _minor_piece_endgame {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1389.

```text
ring pawn_endgame = 23;
  }
  oneof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_overri
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00670"></a>
## FND-00670: chesscom.bots.v1.BotPersonality.minor_piece_endgame = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string minor_piece_endgame = 25;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1420.

```text
neof _major_piece_endgame {
  string major_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_overrid
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00671"></a>
## FND-00671: oneof declaration: chesscom.bots.v1.BotPersonality._theme_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme_uuid {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1459.

```text
jor_piece_endgame = 24;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00672"></a>
## FND-00672: chesscom.bots.v1.BotPersonality.theme_uuid = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string theme_uuid = 27;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1481.

```text
;
  }
  oneof _minor_piece_endgame {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_she
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00673"></a>
## FND-00673: oneof declaration: chesscom.bots.v1.BotPersonality._minimum_cee_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _minimum_cee_version {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1511.

```text
game {
  string minor_piece_endgame = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fal
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00674"></a>
## FND-00674: chesscom.bots.v1.BotPersonality.minimum_cee_version = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string minimum_cee_version = 28;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1542.

```text
game = 25;
  }
  oneof _theme_uuid {
  string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback 
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
