# data_models — findings 7601–7700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07875"></a>
## FND-07875: oneof declaration: chesscom.settings.v1.NotificationSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 142.

```text
otification.proto
// syntax: proto3

package chesscom.settings.v1;

message NotificationSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07876"></a>
## FND-07876: chesscom.settings.v1.NotificationSetting.auto_track_content = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 158.

```text
o
// syntax: proto3

package chesscom.settings.v1;

message NotificationSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
  .chesscom.set
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07877"></a>
## FND-07877: chesscom.settings.v1.NotificationSetting.web = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 227.

```text
ionSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_internal_ads = 5;
  }
  message No
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07878"></a>
## FND-07878: chesscom.settings.v1.NotificationSetting.mobile = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 303.

```text
to_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValu
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07879"></a>
## FND-07879: chesscom.settings.v1.NotificationSetting.email = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 385.

```text
etting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_e
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07880"></a>
## FND-07880: chesscom.settings.v1.NotificationSetting.show_internal_ads = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_internal_ads = 5;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 465.

```text
tting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chess
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07881"></a>
## FND-07881: message declaration: chesscom.settings.v1.NotificationSetting.NotificationWebSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NotificationWebSetting {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 537.

```text
onEmailSetting email = 4;
  .chesscom.settings.v1.SettingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07882"></a>
## FND-07882: oneof declaration: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 142.

```text
otification.proto
// syntax: proto3

package chesscom.settings.v1;

message NotificationSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07883"></a>
## FND-07883: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.my_turn_to_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 590.

```text
tingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy =
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07884"></a>
## FND-07884: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.game_event = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_event = 2;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 656.

```text
nWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment 
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07885"></a>
## FND-07885: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.new_message = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_message = 3;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 717.

```text
ngValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07886"></a>
## FND-07886: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.new_friend_request = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 779.

```text
ettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07887"></a>
## FND-07887: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.new_social_trophy = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 848.

```text
lue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;

```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07888"></a>
## FND-07888: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.new_user_comment = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 916.

```text
olean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chess
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07889"></a>
## FND-07889: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.new_content = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_content = 7;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 983.

```text
Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07890"></a>
## FND-07890: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.new_comment = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_comment = 8;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1045.

```text
Value.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07891"></a>
## FND-07891: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.hero_playing = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1107.

```text
ttingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07892"></a>
## FND-07892: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.chess_tv = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1170.

```text
tingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practi
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07893"></a>
## FND-07893: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.lesson_quota = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1230.

```text
ettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07894"></a>
## FND-07894: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.vote_chess = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1294.

```text
ttingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boo
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07895"></a>
## FND-07895: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.news_and_announcements = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1356.

```text
ingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingVa
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07896"></a>
## FND-07896: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.lesson_and_practice = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1430.

```text
oolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.B
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07897"></a>
## FND-07897: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.friend_activity_updates = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1501.

```text
ws_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07898"></a>
## FND-07898: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.streaks_reminders = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1576.

```text
son_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_r
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07899"></a>
## FND-07899: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.leagues_reminders = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1645.

```text
riend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean co
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07900"></a>
## FND-07900: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.contact_match = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean contact_match = 18;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1714.

```text
lean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean spec
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07901"></a>
## FND-07901: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.puzzle_reminders = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean puzzle_reminders = 19;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1779.

```text
.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean cou
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07902"></a>
## FND-07902: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.game_review_reminders = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 20;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1847.

```text
e.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean co
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07903"></a>
## FND-07903: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.coach_reminders = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1920.

```text
n puzzle_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
   
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07904"></a>
## FND-07904: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.special_offers = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean special_offers = 23;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1987.

```text
an game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07905"></a>
## FND-07905: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.courses_reminders = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2053.

```text
e.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_ev
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07906"></a>
## FND-07906: chesscom.settings.v1.NotificationSetting.NotificationWebSetting.community_updates = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean community_updates = 25;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2122.

```text
Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07907"></a>
## FND-07907: message declaration: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NotificationMobileSetting {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2201.

```text
es_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chess
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07908"></a>
## FND-07908: oneof declaration: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 142.

```text
otification.proto
// syntax: proto3

package chesscom.settings.v1;

message NotificationSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07909"></a>
## FND-07909: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.my_turn_to_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 590.

```text
tingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy =
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07910"></a>
## FND-07910: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.game_event = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_event = 2;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 656.

```text
nWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment 
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07911"></a>
## FND-07911: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.new_message = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_message = 3;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 717.

```text
ngValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07912"></a>
## FND-07912: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.new_friend_request = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 779.

```text
ettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07913"></a>
## FND-07913: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.new_social_trophy = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 848.

```text
lue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;

```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07914"></a>
## FND-07914: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.new_user_comment = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 916.

```text
olean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chess
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07915"></a>
## FND-07915: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.new_content = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_content = 7;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 983.

```text
Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07916"></a>
## FND-07916: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.new_comment = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_comment = 8;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1045.

```text
Value.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07917"></a>
## FND-07917: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.hero_playing = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1107.

```text
ttingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07918"></a>
## FND-07918: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.chess_tv = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1170.

```text
tingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practi
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07919"></a>
## FND-07919: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.lesson_quota = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1230.

```text
ettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07920"></a>
## FND-07920: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.vote_chess = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1294.

```text
ttingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boo
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07921"></a>
## FND-07921: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.news_and_announcements = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1356.

```text
ingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingVa
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07922"></a>
## FND-07922: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.lesson_and_practice = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1430.

```text
oolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.B
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07923"></a>
## FND-07923: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.friend_activity_updates = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1501.

```text
ws_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07924"></a>
## FND-07924: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.recommended_match = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean recommended_match = 16;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3243.

```text
son_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean recommended_match = 16;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 17;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean con
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07925"></a>
## FND-07925: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.puzzle_reminder = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 17;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3312.

```text
riend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean recommended_match = 16;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 17;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_re
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07926"></a>
## FND-07926: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.streaks_reminders = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 18;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3379.

```text
oolean recommended_match = 16;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 17;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean c
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07927"></a>
## FND-07927: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.leagues_reminders = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 19;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3448.

```text
oolean puzzle_reminder = 17;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean spe
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07928"></a>
## FND-07928: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.contact_match = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean contact_match = 20;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3517.

```text
lean streaks_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean course
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07929"></a>
## FND-07929: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.game_review_reminders = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3582.

```text
.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean co
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07930"></a>
## FND-07930: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.coach_reminders = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3655.

```text
lean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationEmailSetting {
    
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07931"></a>
## FND-07931: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.special_offers = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean special_offers = 23;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1987.

```text
an game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07932"></a>
## FND-07932: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.courses_reminders = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2053.

```text
e.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_ev
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07933"></a>
## FND-07933: chesscom.settings.v1.NotificationSetting.NotificationMobileSetting.community_updates = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean community_updates = 25;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2122.

```text
Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07934"></a>
## FND-07934: message declaration: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NotificationEmailSetting {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3936.

```text
es_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationEmailSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chessc
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07935"></a>
## FND-07935: oneof declaration: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 142.

```text
otification.proto
// syntax: proto3

package chesscom.settings.v1;

message NotificationSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean auto_track_content = 1;
  .chesscom.settings.v1.NotificationSetting.NotificationWebSetting web = 2;
  .chesscom.settings.v1.NotificationSetting.NotificationMobileSetting mobile = 3;
  .chesscom.settings.v1.NotificationSetting.NotificationEmailSetting email = 4;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07936"></a>
## FND-07936: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.my_turn_to_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 590.

```text
tingValue.Boolean show_internal_ads = 5;
  }
  message NotificationWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy =
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07937"></a>
## FND-07937: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.game_event = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_event = 2;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 656.

```text
nWebSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment 
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07938"></a>
## FND-07938: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.new_message = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_message = 3;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 717.

```text
ngValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07939"></a>
## FND-07939: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.new_friend_request = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 779.

```text
ettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07940"></a>
## FND-07940: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.new_social_trophy = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 848.

```text
lue.Boolean new_message = 3;
  .chesscom.settings.v1.SettingValue.Boolean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;

```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07941"></a>
## FND-07941: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.new_user_comment = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 916.

```text
olean new_friend_request = 4;
  .chesscom.settings.v1.SettingValue.Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chess
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07942"></a>
## FND-07942: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.new_content = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_content = 7;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 983.

```text
Boolean new_social_trophy = 5;
  .chesscom.settings.v1.SettingValue.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07943"></a>
## FND-07943: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.new_comment = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean new_comment = 8;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1045.

```text
Value.Boolean new_user_comment = 6;
  .chesscom.settings.v1.SettingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07944"></a>
## FND-07944: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.hero_playing = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1107.

```text
ttingValue.Boolean new_content = 7;
  .chesscom.settings.v1.SettingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07945"></a>
## FND-07945: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.chess_tv = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1170.

```text
tingValue.Boolean new_comment = 8;
  .chesscom.settings.v1.SettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practi
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07946"></a>
## FND-07946: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.lesson_quota = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1230.

```text
ettingValue.Boolean hero_playing = 9;
  .chesscom.settings.v1.SettingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07947"></a>
## FND-07947: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.vote_chess = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1294.

```text
ttingValue.Boolean chess_tv = 10;
  .chesscom.settings.v1.SettingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boo
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07948"></a>
## FND-07948: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.news_and_announcements = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1356.

```text
ingValue.Boolean lesson_quota = 11;
  .chesscom.settings.v1.SettingValue.Boolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingVa
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07949"></a>
## FND-07949: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.lesson_and_practice = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1430.

```text
oolean vote_chess = 12;
  .chesscom.settings.v1.SettingValue.Boolean news_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.B
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07950"></a>
## FND-07950: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.friend_activity_updates = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1501.

```text
ws_and_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean lesson_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 16;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 18;
  .chesscom.settings.v1.SettingValue.Boolean
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07951"></a>
## FND-07951: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.puzzle_reminder = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 16;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 4977.

```text
son_and_practice = 14;
  .chesscom.settings.v1.SettingValue.Boolean friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 16;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_re
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07952"></a>
## FND-07952: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.streaks_reminders = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 17;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 5044.

```text
 friend_activity_updates = 15;
  .chesscom.settings.v1.SettingValue.Boolean puzzle_reminder = 16;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean c
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07953"></a>
## FND-07953: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.leagues_reminders = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 18;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 5113.

```text
oolean puzzle_reminder = 16;
  .chesscom.settings.v1.SettingValue.Boolean streaks_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean spe
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07954"></a>
## FND-07954: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.contact_match = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean contact_match = 19;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 5182.

```text
lean streaks_reminders = 17;
  .chesscom.settings.v1.SettingValue.Boolean leagues_reminders = 18;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 19;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean course
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07955"></a>
## FND-07955: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.game_review_reminders = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3582.

```text
.Boolean leagues_reminders = 19;
  .chesscom.settings.v1.SettingValue.Boolean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean co
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07956"></a>
## FND-07956: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.coach_reminders = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 3655.

```text
lean contact_match = 20;
  .chesscom.settings.v1.SettingValue.Boolean game_review_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 22;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationEmailSetting {
    
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07957"></a>
## FND-07957: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.special_offers = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean special_offers = 23;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 1987.

```text
an game_review_reminders = 20;
  .chesscom.settings.v1.SettingValue.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07958"></a>
## FND-07958: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.courses_reminders = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2053.

```text
e.Boolean coach_reminders = 21;
  .chesscom.settings.v1.SettingValue.Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_ev
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07959"></a>
## FND-07959: chesscom.settings.v1.NotificationSetting.NotificationEmailSetting.community_updates = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean community_updates = 25;

### Evidence

- **SRC-0536** `research/proto/chesscom/settings/v1/settings_notification.proto` — [preserved redacted evidence](../evidence/text/5b86eeb18962aa548b2ea8a747f66cf08b219624cac10b0393972d6d22af91c7.proto)
  Character offset 2122.

```text
Boolean special_offers = 23;
  .chesscom.settings.v1.SettingValue.Boolean courses_reminders = 24;
  .chesscom.settings.v1.SettingValue.Boolean community_updates = 25;
    }
  }
  message NotificationMobileSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean my_turn_to_move = 1;
  .chesscom.settings.v1.SettingValue.Boolean game_event = 2;
  .chesscom.settings.v1.SettingValue.Boolean new_message = 3
```

**Source references:** SRC-0536, SRC-1507  
**URL references:** None independently associated  
**Related findings:** FND-07874, FND-07875, FND-07876

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07960"></a>
## FND-07960: message declaration: chesscom.settings.v1.PrivacySetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PrivacySetting {

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 105.

```text
urce: chesscom/settings/v1/settings_privacy.proto
// syntax: proto3

package chesscom.settings.v1;

message PrivacySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String allow_global_chat_requests_from = 1;
  .chesscom.settings.v1.SettingValue.String messages_privacy = 2;
  .chesscom.settings.v1.SettingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .ches
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07961, FND-07962

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07961"></a>
## FND-07961: oneof declaration: chesscom.settings.v1.PrivacySetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 132.

```text
settings_privacy.proto
// syntax: proto3

package chesscom.settings.v1;

message PrivacySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String allow_global_chat_requests_from = 1;
  .chesscom.settings.v1.SettingValue.String messages_privacy = 2;
  .chesscom.settings.v1.SettingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingVal
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07962

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07962"></a>
## FND-07962: chesscom.settings.v1.PrivacySetting.allow_global_chat_requests_from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String allow_global_chat_requests_from = 1;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 148.

```text
.proto
// syntax: proto3

package chesscom.settings.v1;

message PrivacySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String allow_global_chat_requests_from = 1;
  .chesscom.settings.v1.SettingValue.String messages_privacy = 2;
  .chesscom.settings.v1.SettingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingValue.String friend
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07963"></a>
## FND-07963: chesscom.settings.v1.PrivacySetting.messages_privacy = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String messages_privacy = 2;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 229.

```text

  oneof value {
  .chesscom.settings.v1.SettingValue.String allow_global_chat_requests_from = 1;
  .chesscom.settings.v1.SettingValue.String messages_privacy = 2;
  .chesscom.settings.v1.SettingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingValue.String friends_list_privacy = 5;
  .chesscom.settings.v1.SettingValue.String insights_privacy 
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07964"></a>
## FND-07964: chesscom.settings.v1.PrivacySetting.notes_privacy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String notes_privacy = 3;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 295.

```text
_global_chat_requests_from = 1;
  .chesscom.settings.v1.SettingValue.String messages_privacy = 2;
  .chesscom.settings.v1.SettingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingValue.String friends_list_privacy = 5;
  .chesscom.settings.v1.SettingValue.String insights_privacy = 6;
  .chesscom.settings.v1.SettingValue.Boolean allow_friend_req
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07965"></a>
## FND-07965: chesscom.settings.v1.PrivacySetting.blog_privacy = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String blog_privacy = 4;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 358.

```text
Value.String messages_privacy = 2;
  .chesscom.settings.v1.SettingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingValue.String friends_list_privacy = 5;
  .chesscom.settings.v1.SettingValue.String insights_privacy = 6;
  .chesscom.settings.v1.SettingValue.Boolean allow_friend_requests = 7;
  .chesscom.settings.v1.SettingValue.Boolean allow_c
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07966"></a>
## FND-07966: chesscom.settings.v1.PrivacySetting.friends_list_privacy = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String friends_list_privacy = 5;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 420.

```text
tingValue.String notes_privacy = 3;
  .chesscom.settings.v1.SettingValue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingValue.String friends_list_privacy = 5;
  .chesscom.settings.v1.SettingValue.String insights_privacy = 6;
  .chesscom.settings.v1.SettingValue.Boolean allow_friend_requests = 7;
  .chesscom.settings.v1.SettingValue.Boolean allow_club_invitations = 8;
  .chesscom.settings.v1.SettingValue.Bool
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07967"></a>
## FND-07967: chesscom.settings.v1.PrivacySetting.insights_privacy = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String insights_privacy = 6;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 490.

```text
ue.String blog_privacy = 4;
  .chesscom.settings.v1.SettingValue.String friends_list_privacy = 5;
  .chesscom.settings.v1.SettingValue.String insights_privacy = 6;
  .chesscom.settings.v1.SettingValue.Boolean allow_friend_requests = 7;
  .chesscom.settings.v1.SettingValue.Boolean allow_club_invitations = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_tournament_invitations = 9;
  .chesscom.settings.v1.SettingV
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07968"></a>
## FND-07968: chesscom.settings.v1.PrivacySetting.allow_friend_requests = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean allow_friend_requests = 7;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 556.

```text
tring friends_list_privacy = 5;
  .chesscom.settings.v1.SettingValue.String insights_privacy = 6;
  .chesscom.settings.v1.SettingValue.Boolean allow_friend_requests = 7;
  .chesscom.settings.v1.SettingValue.Boolean allow_club_invitations = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_tournament_invitations = 9;
  .chesscom.settings.v1.SettingValue.Boolean safe_mode = 10;
  .chesscom.settings.v1.SettingValue.
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07969"></a>
## FND-07969: chesscom.settings.v1.PrivacySetting.allow_club_invitations = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean allow_club_invitations = 8;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 628.

```text
ing insights_privacy = 6;
  .chesscom.settings.v1.SettingValue.Boolean allow_friend_requests = 7;
  .chesscom.settings.v1.SettingValue.Boolean allow_club_invitations = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_tournament_invitations = 9;
  .chesscom.settings.v1.SettingValue.Boolean safe_mode = 10;
  .chesscom.settings.v1.SettingValue.Boolean allow_contact_matching = 11;
  .chesscom.settings.v1.SettingValu
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07970"></a>
## FND-07970: chesscom.settings.v1.PrivacySetting.allow_tournament_invitations = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean allow_tournament_invitations = 9;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 701.

```text
low_friend_requests = 7;
  .chesscom.settings.v1.SettingValue.Boolean allow_club_invitations = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_tournament_invitations = 9;
  .chesscom.settings.v1.SettingValue.Boolean safe_mode = 10;
  .chesscom.settings.v1.SettingValue.Boolean allow_contact_matching = 11;
  .chesscom.settings.v1.SettingValue.Boolean suspicious_login_protection_otvc = 12;
  .chesscom.settings.v1.
```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07971"></a>
## FND-07971: chesscom.settings.v1.PrivacySetting.safe_mode = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean safe_mode = 10;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 780.

```text
b_invitations = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_tournament_invitations = 9;
  .chesscom.settings.v1.SettingValue.Boolean safe_mode = 10;
  .chesscom.settings.v1.SettingValue.Boolean allow_contact_matching = 11;
  .chesscom.settings.v1.SettingValue.Boolean suspicious_login_protection_otvc = 12;
  .chesscom.settings.v1.SettingValue.Boolean allow_classroom_invitations = 13;
  }
}

```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07972"></a>
## FND-07972: chesscom.settings.v1.PrivacySetting.allow_contact_matching = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean allow_contact_matching = 11;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 841.

```text
an allow_tournament_invitations = 9;
  .chesscom.settings.v1.SettingValue.Boolean safe_mode = 10;
  .chesscom.settings.v1.SettingValue.Boolean allow_contact_matching = 11;
  .chesscom.settings.v1.SettingValue.Boolean suspicious_login_protection_otvc = 12;
  .chesscom.settings.v1.SettingValue.Boolean allow_classroom_invitations = 13;
  }
}

```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07973"></a>
## FND-07973: chesscom.settings.v1.PrivacySetting.suspicious_login_protection_otvc = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean suspicious_login_protection_otvc = 12;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 915.

```text
Boolean safe_mode = 10;
  .chesscom.settings.v1.SettingValue.Boolean allow_contact_matching = 11;
  .chesscom.settings.v1.SettingValue.Boolean suspicious_login_protection_otvc = 12;
  .chesscom.settings.v1.SettingValue.Boolean allow_classroom_invitations = 13;
  }
}

```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07974"></a>
## FND-07974: chesscom.settings.v1.PrivacySetting.allow_classroom_invitations = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean allow_classroom_invitations = 13;

### Evidence

- **SRC-0537** `research/proto/chesscom/settings/v1/settings_privacy.proto` — [preserved redacted evidence](../evidence/text/bb4a417b146c4aa96984adc7ea377f514eedb98df9d9d8e2bfaebf022bca369d.proto)
  Character offset 999.

```text
atching = 11;
  .chesscom.settings.v1.SettingValue.Boolean suspicious_login_protection_otvc = 12;
  .chesscom.settings.v1.SettingValue.Boolean allow_classroom_invitations = 13;
  }
}

```

**Source references:** SRC-0537, SRC-1508  
**URL references:** None independently associated  
**Related findings:** FND-07960, FND-07961, FND-07962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
