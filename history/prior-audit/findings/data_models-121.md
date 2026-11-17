# data_models — findings 12001–12100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12275"></a>
## FND-12275: chesscom.user_properties.v1.UserSettingsProperty.notification_auto_track_content = 110

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_auto_track_content = 110;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15398.

```text
hess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_r
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12276"></a>
## FND-12276: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_filter_hide_variants

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_filter_hide_variants {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15448.

```text

  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12277"></a>
## FND-12277: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_filter_hide_variants = 111

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_seek_filter_hide_variants = 111;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15499.

```text
ool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_m
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12278"></a>
## FND-12278: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_messages_privacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_messages_privacy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15557.

```text
meplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12279"></a>
## FND-12279: chesscom.user_properties.v1.UserSettingsProperty.privacy_messages_privacy = 112

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string privacy_messages_privacy = 112;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15593.

```text
s {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12280"></a>
## FND-12280: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_filter_rated_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_filter_rated_only {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15638.

```text
iants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_pl
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12281"></a>
## FND-12281: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_filter_rated_only = 113

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_seek_filter_rated_only = 113;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15686.

```text
cy {
  string privacy_messages_privacy = 112;
  }
  oneof _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 1
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12282"></a>
## FND-12282: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_my_turn_to_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_my_turn_to_move {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15741.

```text
of _gameplay_live_seek_filter_rated_only {
  bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12283"></a>
## FND-12283: chesscom.user_properties.v1.UserSettingsProperty.notification_web_my_turn_to_move = 114

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_my_turn_to_move = 114;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15785.

```text
 bool gameplay_live_seek_filter_rated_only = 113;
  }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12284"></a>
## FND-12284: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_auto_switch_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_auto_switch_game {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15836.

```text
 }
  oneof _notification_web_my_turn_to_move {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_an
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12285"></a>
## FND-12285: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_auto_switch_game = 115

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_auto_switch_game = 115;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15878.

```text
ve {
  bool notification_web_my_turn_to_move = 114;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notificat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12286"></a>
## FND-12286: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_hero_playing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_hero_playing {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15927.

```text
4;
  }
  oneof _gameplay_live_auto_switch_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notificat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12287"></a>
## FND-12287: chesscom.user_properties.v1.UserSettingsProperty.notification_web_hero_playing = 116

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_hero_playing = 116;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15968.

```text
_game {
  bool gameplay_live_auto_switch_game = 115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12288"></a>
## FND-12288: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_daily_auto_win_on_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_daily_auto_win_on_time {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16016.

```text
115;
  }
  oneof _notification_web_hero_playing {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12289"></a>
## FND-12289: chesscom.user_properties.v1.UserSettingsProperty.gameplay_daily_auto_win_on_time = 117

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_daily_auto_win_on_time = 117;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16059.

```text
ying {
  bool notification_web_hero_playing = 116;
  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notifi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12290"></a>
## FND-12290: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_animation_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_animation_type {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16109.

```text

  }
  oneof _gameplay_daily_auto_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12291"></a>
## FND-12291: chesscom.user_properties.v1.UserSettingsProperty.board_animation_type = 118

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_animation_type = 118;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16141.

```text
o_win_on_time {
  bool gameplay_daily_auto_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12292"></a>
## FND-12292: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_lesson_and_practice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_lesson_and_practice {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16182.

```text
o_win_on_time = 117;
  }
  oneof _board_animation_type {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_re
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12293"></a>
## FND-12293: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_lesson_and_practice = 119

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_lesson_and_practice = 119;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16233.

```text
ype {
  string board_animation_type = 118;
  }
  oneof _notification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_remind
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12294"></a>
## FND-12294: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_win_celebration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_win_celebration {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16291.

```text
tification_mobile_lesson_and_practice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminde
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12295"></a>
## FND-12295: chesscom.user_properties.v1.UserSettingsProperty.board_win_celebration = 120

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_win_celebration = 120;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16324.

```text
tice {
  bool notification_mobile_lesson_and_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_st
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12296"></a>
## FND-12296: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_streaks_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_streaks_reminders {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16366.

```text
nd_practice = 119;
  }
  oneof _board_win_celebration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notifi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12297"></a>
## FND-12297: chesscom.user_properties.v1.UserSettingsProperty.notification_web_streaks_reminders = 121

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_streaks_reminders = 121;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16412.

```text
bration {
  string board_win_celebration = 120;
  }
  oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notifica
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12298"></a>
## FND-12298: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_streaks_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_streaks_reminders {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16465.

```text
 oneof _notification_web_streaks_reminders {
  bool notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notifi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12299"></a>
## FND-12299: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_streaks_reminders = 122

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_streaks_reminders = 122;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16514.

```text
ol notification_web_streaks_reminders = 121;
  }
  oneof _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notifica
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12300"></a>
## FND-12300: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_streaks_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_streaks_reminders {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16570.

```text
 _notification_mobile_streaks_reminders {
  bool notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notifi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12301"></a>
## FND-12301: chesscom.user_properties.v1.UserSettingsProperty.notification_email_streaks_reminders = 123

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_streaks_reminders = 123;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16618.

```text
 notification_mobile_streaks_reminders = 122;
  }
  oneof _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notifica
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12302"></a>
## FND-12302: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_leagues_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_leagues_reminders {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16673.

```text
of _notification_email_streaks_reminders {
  bool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzle
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12303"></a>
## FND-12303: chesscom.user_properties.v1.UserSettingsProperty.notification_web_leagues_reminders = 124

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_leagues_reminders = 124;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16719.

```text
ool notification_email_streaks_reminders = 123;
  }
  oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_clas
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12304"></a>
## FND-12304: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_leagues_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_leagues_reminders {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16772.

```text
 oneof _notification_web_leagues_reminders {
  bool notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12305"></a>
## FND-12305: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_leagues_reminders = 125

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_leagues_reminders = 125;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16821.

```text
ol notification_web_leagues_reminders = 124;
  }
  oneof _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12306"></a>
## FND-12306: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_leagues_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_leagues_reminders {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16877.

```text
 _notification_mobile_leagues_reminders {
  bool notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coac
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12307"></a>
## FND-12307: chesscom.user_properties.v1.UserSettingsProperty.notification_email_leagues_reminders = 126

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_leagues_reminders = 126;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16925.

```text
 notification_mobile_leagues_reminders = 125;
  }
  oneof _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  b
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12308"></a>
## FND-12308: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._puzzles_show_classic_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzles_show_classic_mode {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 16980.

```text
of _notification_email_leagues_reminders {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_cente
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12309"></a>
## FND-12309: chesscom.user_properties.v1.UserSettingsProperty.puzzles_show_classic_mode = 127

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool puzzles_show_classic_mode = 127;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17017.

```text
ers {
  bool notification_email_leagues_reminders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12310"></a>
## FND-12310: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_show_membership_badges

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_show_membership_badges {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17061.

```text
nders = 126;
  }
  oneof _puzzles_show_classic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters =
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12311"></a>
## FND-12311: chesscom.user_properties.v1.UserSettingsProperty.gameplay_show_membership_badges = 128

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_show_membership_badges = 128;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17104.

```text
sic_mode {
  bool puzzles_show_classic_mode = 127;
  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_frie
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12312"></a>
## FND-12312: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._learn_coach_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_coach_id {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17154.

```text

  }
  oneof _gameplay_show_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_f
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12313"></a>
## FND-12313: chesscom.user_properties.v1.UserSettingsProperty.learn_coach_id = 129

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string learn_coach_id = 129;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17180.

```text
w_membership_badges {
  bool gameplay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 1
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12314"></a>
## FND-12314: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._learn_coach_nudge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_coach_nudge {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17215.

```text
ay_show_membership_badges = 128;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_aut
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12315"></a>
## FND-12315: chesscom.user_properties.v1.UserSettingsProperty.learn_coach_nudge = 130

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool learn_coach_nudge = 130;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17244.

```text
28;
  }
  oneof _learn_coach_id {
  string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12316"></a>
## FND-12316: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._toaster_center_show_club_request_toasters

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _toaster_center_show_club_request_toasters {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17280.

```text
string learn_coach_id = 129;
  }
  oneof _learn_coach_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {
  bool toaster_center_automatically_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12317"></a>
## FND-12317: chesscom.user_properties.v1.UserSettingsProperty.toaster_center_show_club_request_toasters = 131

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool toaster_center_show_club_request_toasters = 131;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17333.

```text
_nudge {
  bool learn_coach_nudge = 130;
  }
  oneof _toaster_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_ty
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12318"></a>
## FND-12318: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._toaster_center_show_friend_request_toasters

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _toaster_center_show_friend_request_toasters {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17393.

```text
r_center_show_club_request_toasters {
  bool toaster_center_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_type {
  string board_castling_type = 134;
  }
}

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12319"></a>
## FND-12319: chesscom.user_properties.v1.UserSettingsProperty.toaster_center_show_friend_request_toasters = 132

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool toaster_center_show_friend_request_toasters = 132;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17448.

```text
nter_show_club_request_toasters = 131;
  }
  oneof _toaster_center_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_type {
  string board_castling_type = 134;
  }
}

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12320"></a>
## FND-12320: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._toaster_center_automatically_expand_toasters

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _toaster_center_automatically_expand_toasters {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17510.

```text
nter_show_friend_request_toasters {
  bool toaster_center_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_type {
  string board_castling_type = 134;
  }
}

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12321"></a>
## FND-12321: chesscom.user_properties.v1.UserSettingsProperty.toaster_center_automatically_expand_toasters = 133

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool toaster_center_automatically_expand_toasters = 133;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17566.

```text
r_show_friend_request_toasters = 132;
  }
  oneof _toaster_center_automatically_expand_toasters {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_type {
  string board_castling_type = 134;
  }
}

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12322"></a>
## FND-12322: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_castling_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_castling_type {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17629.

```text
er_automatically_expand_toasters {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_type {
  string board_castling_type = 134;
  }
}

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12323"></a>
## FND-12323: chesscom.user_properties.v1.UserSettingsProperty.board_castling_type = 134

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_castling_type = 134;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 17660.

```text
s {
  bool toaster_center_automatically_expand_toasters = 133;
  }
  oneof _board_castling_type {
  string board_castling_type = 134;
  }
}

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12324"></a>
## FND-12324: enum declaration: chesscom.user_properties.v1.UserStreakV2PropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserStreakV2PropertyDefinition {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 128.

```text
perties/v1/properties_user_streak_v2.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserStreakV2PropertyDefinition {
  USER_STREAK_V2_UNSPECIFIED = 0;
  USER_STREAK_V2_UPDATED_AT = 1;
  USER_STREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE 
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12325"></a>
## FND-12325: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_UNSPECIFIED = 0;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 168.

```text
to
// syntax: proto3

package chesscom.user_properties.v1;

enum UserStreakV2PropertyDefinition {
  USER_STREAK_V2_UNSPECIFIED = 0;
  USER_STREAK_V2_UPDATED_AT = 1;
  USER_STREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
 
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12326"></a>
## FND-12326: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_UPDATED_AT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_UPDATED_AT = 1;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 202.

```text
scom.user_properties.v1;

enum UserStreakV2PropertyDefinition {
  USER_STREAK_V2_UNSPECIFIED = 0;
  USER_STREAK_V2_UPDATED_AT = 1;
  USER_STREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.pro
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12327"></a>
## FND-12327: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_DURATION_DAYS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_DURATION_DAYS = 2;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 235.

```text
erStreakV2PropertyDefinition {
  USER_STREAK_V2_UNSPECIFIED = 0;
  USER_STREAK_V2_UPDATED_AT = 1;
  USER_STREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
 
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12328"></a>
## FND-12328: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_STATUS_BY_DAYS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_STATUS_BY_DAYS = 3;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 271.

```text
R_STREAK_V2_UNSPECIFIED = 0;
  USER_STREAK_V2_UPDATED_AT = 1;
  USER_STREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12329"></a>
## FND-12329: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_EXPIRES_AT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_EXPIRES_AT = 4;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 308.

```text
TREAK_V2_UPDATED_AT = 1;
  USER_STREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expir
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12330"></a>
## FND-12330: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_RESETS_COUNT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_RESETS_COUNT = 5;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 341.

```text
TREAK_V2_DURATION_DAYS = 2;
  USER_STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timest
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12331"></a>
## FND-12331: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_LONGEST_STREAK = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_LONGEST_STREAK = 6;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 376.

```text
STREAK_V2_STATUS_BY_DAYS = 3;
  USER_STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _re
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12332"></a>
## FND-12332: chesscom.user_properties.v1.UserStreakV2PropertyDefinition.USER_STREAK_V2_LONGEST_STREAK_DATE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_STREAK_V2_LONGEST_STREAK_DATE = 7;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 413.

```text
STREAK_V2_EXPIRES_AT = 4;
  USER_STREAK_V2_RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12333"></a>
## FND-12333: message declaration: chesscom.user_properties.v1.UserStreakV2Property

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserStreakV2Property {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 456.

```text
RESETS_COUNT = 5;
  USER_STREAK_V2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 lon
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12334"></a>
## FND-12334: oneof declaration: chesscom.user_properties.v1.UserStreakV2Property._updated_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _updated_at {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 489.

```text
2_LONGEST_STREAK = 6;
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _lon
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12335"></a>
## FND-12335: chesscom.user_properties.v1.UserStreakV2Property.updated_at = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp updated_at = 1;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 511.

```text
  USER_STREAK_V2_LONGEST_STREAK_DATE = 7;
}

message UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12336"></a>
## FND-12336: oneof declaration: chesscom.user_properties.v1.UserStreakV2Property._duration_days

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _duration_days {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 560.

```text
age UserStreakV2Property {
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12337"></a>
## FND-12337: chesscom.user_properties.v1.UserStreakV2Property.duration_days = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 duration_days = 2;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 585.

```text
{
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string s
```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12338"></a>
## FND-12338: oneof declaration: chesscom.user_properties.v1.UserStreakV2Property._expires_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _expires_at {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 616.

```text
le.protobuf.Timestamp updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12339"></a>
## FND-12339: chesscom.user_properties.v1.UserStreakV2Property.expires_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp expires_at = 4;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 638.

```text
updated_at = 1;
  }
  oneof _duration_days {
  int32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12340"></a>
## FND-12340: oneof declaration: chesscom.user_properties.v1.UserStreakV2Property._resets_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _resets_count {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 687.

```text
t32 duration_days = 2;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12341"></a>
## FND-12341: chesscom.user_properties.v1.UserStreakV2Property.resets_count = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 resets_count = 5;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 711.

```text
 }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12342"></a>
## FND-12342: oneof declaration: chesscom.user_properties.v1.UserStreakV2Property._longest_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _longest_streak {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 741.

```text
ogle.protobuf.Timestamp expires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12343"></a>
## FND-12343: chesscom.user_properties.v1.UserStreakV2Property.longest_streak = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 longest_streak = 6;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 767.

```text
pires_at = 4;
  }
  oneof _resets_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12344"></a>
## FND-12344: oneof declaration: chesscom.user_properties.v1.UserStreakV2Property._longest_streak_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _longest_streak_date {

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 799.

```text
s_count {
  int32 resets_count = 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12345"></a>
## FND-12345: chesscom.user_properties.v1.UserStreakV2Property.longest_streak_date = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp longest_streak_date = 7;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 830.

```text
= 5;
  }
  oneof _longest_streak {
  int32 longest_streak = 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12346"></a>
## FND-12346: chesscom.user_properties.v1.UserStreakV2Property.status_by_days = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string status_by_days = 3;

### Evidence

- **SRC-0644** `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto` — [preserved redacted evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto)
  Character offset 888.

```text
= 6;
  }
  oneof _longest_streak_date {
  .google.protobuf.Timestamp longest_streak_date = 7;
  }
  repeated string status_by_days = 3;
}

```

**Source references:** SRC-0644, SRC-1615  
**URL references:** None independently associated  
**Related findings:** FND-12324, FND-12325, FND-12326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12347"></a>
## FND-12347: enum declaration: chesscom.user_properties.v1.WDLPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum WDLPropertyDefinition {

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 117.

```text
om/user_properties/v1/properties_wdl.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum WDLPropertyDefinition {
  WDL_PROPERTY_UNSPECIFIED = 0;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 1
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12348"></a>
## FND-12348: chesscom.user_properties.v1.WDLPropertyDefinition.WDL_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WDL_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 148.

```text
s_wdl.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum WDLPropertyDefinition {
  WDL_PROPERTY_UNSPECIFIED = 0;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12349"></a>
## FND-12349: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS = 1;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 180.

```text
ackage chesscom.user_properties.v1;

enum WDLPropertyDefinition {
  WDL_PROPERTY_UNSPECIFIED = 0;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOT
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12350"></a>
## FND-12350: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_BUGHOUSE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_BUGHOUSE = 2;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 198.

```text
er_properties.v1;

enum WDLPropertyDefinition {
  WDL_PROPERTY_UNSPECIFIED = 0;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUS
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12351"></a>
## FND-12351: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_CHESS960 = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_CHESS960 = 3;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 225.

```text
PropertyDefinition {
  WDL_PROPERTY_UNSPECIFIED = 0;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGO
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12352"></a>
## FND-12352: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_CHESS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_CHESS = 4;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 252.

```text
PROPERTY_UNSPECIFIED = 0;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAW
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12353"></a>
## FND-12353: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_CRAZYHOUSE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_CRAZYHOUSE = 5;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 276.

```text
;
  TOTAL_WINS = 1;
  TOTAL_WINS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTA
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12354"></a>
## FND-12354: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_KINGOFTHEHILL = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_KINGOFTHEHILL = 6;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 305.

```text
INS_BUGHOUSE = 2;
  TOTAL_WINS_CHESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TO
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12355"></a>
## FND-12355: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_ODDSCHESS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_ODDSCHESS = 7;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 337.

```text
HESS960 = 3;
  TOTAL_WINS_CHESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12356"></a>
## FND-12356: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_WINS_THREECHECK = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_WINS_THREECHECK = 8;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 365.

```text
ESS = 4;
  TOTAL_WINS_CRAZYHOUSE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSE
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12357"></a>
## FND-12357: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS = 9;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 394.

```text
USE = 5;
  TOTAL_WINS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSS
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12358"></a>
## FND-12358: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_BUGHOUSE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_BUGHOUSE = 10;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 413.

```text
NS_KINGOFTHEHILL = 6;
  TOTAL_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TO
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12359"></a>
## FND-12359: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_CHESS960 = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_CHESS960 = 11;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 442.

```text
_WINS_ODDSCHESS = 7;
  TOTAL_WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
 
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12360"></a>
## FND-12360: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_CHESS = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_CHESS = 12;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 471.

```text
WINS_THREECHECK = 8;
  TOTAL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL =
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12361"></a>
## FND-12361: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_CRAZYHOUSE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_CRAZYHOUSE = 13;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 497.

```text
AL_DRAWS = 9;
  TOTAL_DRAWS_BUGHOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCH
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12362"></a>
## FND-12362: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_KINGOFTHEHILL = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_KINGOFTHEHILL = 14;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 528.

```text
HOUSE = 10;
  TOTAL_DRAWS_CHESS960 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREEC
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12363"></a>
## FND-12363: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_ODDSCHESS = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_ODDSCHESS = 15;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 562.

```text
 = 11;
  TOTAL_DRAWS_CHESS = 12;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  T
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12364"></a>
## FND-12364: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_DRAWS_THREECHECK = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_DRAWS_THREECHECK = 16;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 592.

```text
2;
  TOTAL_DRAWS_CRAZYHOUSE = 13;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_G
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12365"></a>
## FND-12365: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES = 17;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 623.

```text
3;
  TOTAL_DRAWS_KINGOFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAM
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12366"></a>
## FND-12366: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_BUGHOUSE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_BUGHOUSE = 18;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 644.

```text
OFTHEHILL = 14;
  TOTAL_DRAWS_ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  T
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12367"></a>
## FND-12367: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_CHESS960 = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_CHESS960 = 19;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 674.

```text
ODDSCHESS = 15;
  TOTAL_DRAWS_THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12368"></a>
## FND-12368: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_CHESS = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_CHESS = 20;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 704.

```text
THREECHECK = 16;
  TOTAL_LOSSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTA
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12369"></a>
## FND-12369: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_CRAZYHOUSE = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_CRAZYHOUSE = 21;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 731.

```text
SSES = 17;
  TOTAL_LOSSES_BUGHOUSE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTAL_GAMES_KINGOFTHEHILL = 31;
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12370"></a>
## FND-12370: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_KINGOFTHEHILL = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_KINGOFTHEHILL = 22;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 763.

```text
SE = 18;
  TOTAL_LOSSES_CHESS960 = 19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTAL_GAMES_KINGOFTHEHILL = 31;
  TOTAL_GAMES_ODDSCHESS = 32;
 
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12371"></a>
## FND-12371: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_ODDSCHESS = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_ODDSCHESS = 23;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 798.

```text
19;
  TOTAL_LOSSES_CHESS = 20;
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTAL_GAMES_KINGOFTHEHILL = 31;
  TOTAL_GAMES_ODDSCHESS = 32;
  TOTAL_GAMES_THREECHECK = 33;
  TOT
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12372"></a>
## FND-12372: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_LOSSES_THREECHECK = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_LOSSES_THREECHECK = 24;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 829.

```text
  TOTAL_LOSSES_CRAZYHOUSE = 21;
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTAL_GAMES_KINGOFTHEHILL = 31;
  TOTAL_GAMES_ODDSCHESS = 32;
  TOTAL_GAMES_THREECHECK = 33;
  TOTAL_GAMES_VS_COMPUTER = 34;
  LA
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12373"></a>
## FND-12373: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_GAMES = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_GAMES = 25;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 861.

```text
  TOTAL_LOSSES_KINGOFTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTAL_GAMES_KINGOFTHEHILL = 31;
  TOTAL_GAMES_ODDSCHESS = 32;
  TOTAL_GAMES_THREECHECK = 33;
  TOTAL_GAMES_VS_COMPUTER = 34;
  LAST_GAME_RESULT = 35;
  LAST_GAME
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12374"></a>
## FND-12374: chesscom.user_properties.v1.WDLPropertyDefinition.TOTAL_GAMES_4PC = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_GAMES_4PC = 26;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 881.

```text
FTHEHILL = 22;
  TOTAL_LOSSES_ODDSCHESS = 23;
  TOTAL_LOSSES_THREECHECK = 24;
  TOTAL_GAMES = 25;
  TOTAL_GAMES_4PC = 26;
  TOTAL_GAMES_BUGHOUSE = 27;
  TOTAL_GAMES_CHESS960 = 28;
  TOTAL_GAMES_CHESS = 29;
  TOTAL_GAMES_CRAZYHOUSE = 30;
  TOTAL_GAMES_KINGOFTHEHILL = 31;
  TOTAL_GAMES_ODDSCHESS = 32;
  TOTAL_GAMES_THREECHECK = 33;
  TOTAL_GAMES_VS_COMPUTER = 34;
  LAST_GAME_RESULT = 35;
  LAST_GAME_RESULT_CODE = 36;
 
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
